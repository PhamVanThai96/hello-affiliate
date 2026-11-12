#!/usr/bin/env python3
"""
cli.py - Giao diện dòng lệnh cho agent (Investor) gọi công cụ phân tích kỹ thuật, in KẾT QUẢ JSON (không gửi Telegram).

  python3 dev/cli.py MSN.VN                      # phân tích kỹ thuật 12 tháng khung ngày + biểu đồ
  python3 dev/cli.py HPG.VN --period 12mo --out /tmp/out
  python3 dev/cli.py MSN.VN --no-chart           # chỉ số liệu, không vẽ
  python3 dev/cli.py MSN.VN --as-of 2025-05-29   # phân tích tại một ngày trong quá khứ (chỉ dùng dữ liệu <= ngày đó)
  python3 dev/cli.py MSN.VN --fundamentals       # snapshot cơ bản từ yfinance (giá, số cổ phiếu, P/E, P/B, EPS, BVPS, beta, nợ, thiểu số) để định giá

Đầu ra JSON: ticker, as_of, close, trend_state, outlook (thiên hướng + xác suất đã hiệu chuẩn + vùng biến động),
channel, support/resistance, volume_profile (AMT), boxes, patterns (chỉ thông tin), rule_filter (nhãn luật), chart_path,
`validation` (kết quả kiểm chứng của từng thành phần) và `disclaimer`.
"""
import argparse
import json
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.environ.setdefault("STOCK_NO_TELEGRAM", "1")
import stock_analysis_script as sas  # noqa: E402
import auction_market_theory as amt  # noqa: E402

VALIDATION = {
    "outlook": "Hướng 10 phiên đúng ~52% (ngang 'luôn tăng' 51%); vùng biến động 80% phủ ~83% (đã kiểm chứng).",
    "channel": "Kênh gần nhất chứa 10 phiên kế tiếp ~77% (kênh cũ 31%); vượt biên trên: 57-67% là phá vỡ giả.",
    "candles": "Mẫu hình nến đảo chiều KHÔNG có giá trị dự báo 10 phiên (đã kiểm chứng ngoài mẫu); chỉ mang tính mô tả.",
    "boxes": "Mua gần đáy hộp tích lũy: kém nền ~0,8-1,1%/10 phiên (đã kiểm chứng); breakout + khối lượng >=2x: nhỉnh hơn nền nhẹ.",
    "support_resistance": "Vùng hỗ trợ từng đảo chiều >=3 lần KHÔNG giữ giá tốt hơn mức ngẫu nhiên (đã kiểm chứng).",
    "rule_filter": "Nhãn MUA (bộ lọc luật, đã bỏ nhánh mua đáy hộp): tăng 10 phiên ~61%, +1,3% (nền ~+0,7%), mô phỏng giao dịch +0,7%/lệnh trước phí, mẫu dồn cụm nên chưa kết luận chắc; BÁN/THEO DÕI không hơn nền.",
    "value_area": "Giá đóng cửa trên VAH 60 phiên: tăng sau 10 phiên ~55-56% (nền ~51-53%); dưới VAL: không có lợi thế.",
}
DISCLAIMER = ("Phân tích tham khảo dựa trên dữ liệu yfinance, không phải khuyến nghị mua/bán. Hướng giá ngắn hạn gần như không "
              "dự báo được từ giá; xác suất là tần suất lịch sử có điều kiện. Dữ liệu có thể trễ/thiếu.")


def _clean(o):
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items() if k not in ("upper_line", "lower_line", "median_line", "edges", "bin_volume", "peak_idx", "trough_idx")}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, (np.floating,)):
        return None if np.isnan(o) else float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, float) and np.isnan(o):
        return None
    if isinstance(o, (pd.Timestamp,)):
        return str(o.date())
    return o


def analyze(ticker, period="12mo", out_dir=None, chart=True, as_of=None):
    import yfinance as yf
    if as_of:
        d = yf.Ticker(ticker).history(period="max", interval="1d").reset_index()
        d["Date"] = pd.to_datetime(d["Date"]).dt.tz_localize(None)
        d = d[["Date", "Open", "High", "Low", "Close", "Volume"]].dropna()
        d = d[(d["Volume"] > 0) & (d["Date"] <= pd.Timestamp(as_of))].tail(300).reset_index(drop=True)
    else:
        d = sas.fetch_stock_data(ticker, period=period, interval="1d")
    if len(d) < 80:
        raise ValueError(f"Không đủ dữ liệu cho {ticker} ({len(d)} phiên).")
    out_dir = out_dir or os.path.join(sas.PROJECT_ROOT, "output")
    res = sas.run_stock_analysis_skill(ticker, period=period, interval="1d", output_dir=out_dir,
                                       session_file=os.path.join(out_dir, "_cli_session.json"), indicators=None,
                                       send_telegram=False, df_override=d) if chart else None
    df_ind = sas.compute_indicators(d)
    channel = sas.compute_trend_channel(d)
    boxes = sas.detect_consolidation_boxes(d)
    patterns = sas.detect_candlestick_patterns_v2(df_ind, lookback=5)
    sr = sas.find_support_resistance(d, channel)
    rec = res["recommendation"] if res else sas.generate_recommendation_v2(df_ind, channel, sr, boxes, patterns)
    try:
        import outlook_v3 as o3
        outlook = rec.get("outlook") or o3.build_outlook(d)
    except Exception as e:  # noqa: BLE001
        outlook = {"error": str(e)}
    try:
        vp = amt.compute_volume_profile(d.tail(60).reset_index(drop=True), num_bins=40)
        c = float(d["Close"].iloc[-1])
        pos = "trên VAH" if c > vp["vah"] else ("dưới VAL" if c < vp["val"] else "trong Value Area")
        value_area = {"window": 60, "poc": vp["poc"], "vah": vp["vah"], "val": vp["val"], "position": pos}
    except Exception as e:  # noqa: BLE001
        value_area = {"error": str(e)}
    payload = {
        "ticker": ticker, "as_of": str(d["Date"].iloc[-1].date()), "close": float(d["Close"].iloc[-1]), "bars": len(d),
        "trend_state": outlook.get("trend_state") if isinstance(outlook, dict) else None, "outlook": outlook,
        "channel": {k: v for k, v in channel.items() if k not in ("upper_line", "lower_line", "median_line", "peak_idx", "trough_idx")},
        "channel_edges_now": ({"upper": channel["upper_line"][-1], "lower": channel["lower_line"][-1], "median": channel["median_line"][-1]}
                              if channel.get("valid") else None),
        "support_resistance": sr, "value_area": value_area, "boxes_recent": boxes[-3:],
        "patterns_info_only": patterns[-5:],
        "rule_filter": {"label": rec.get("action"), "reasons": rec.get("reasons"), "note": "Nhãn luật chưa chứng minh khả năng dự báo."},
        "indicators": {"rsi14": rec.get("rsi"), "mfi14": rec.get("mfi"), "vol_ratio": rec.get("vol_ratio"), "long_term": rec.get("long_term_trend")},
        "chart_path": res["chart_path"] if res else None, "validation": VALIDATION, "disclaimer": DISCLAIMER,
    }
    return _clean(payload)


FUND_NOTE = ("Nguồn yfinance (Yahoo), có thể trễ/khác với CafeF/Vietstock: số cổ phiếu, EPS, BVPS, beta tính theo cách của Yahoo (BVPS thường là vốn chủ CÔNG TY MẸ, "
             "không gồm lợi ích cổ đông thiểu số; beta so với chỉ số Yahoo chọn). Phải đối chiếu với nguồn Việt Nam/BCTC và nêu chênh lệch; không dùng làm số kiểm toán.")


def fundamentals(ticker):
    """Snapshot cơ bản cho định giá từ yfinance (VND, đơn vị tỷ đồng cho tổng giá trị)."""
    import yfinance as yf
    t = yf.Ticker(ticker)
    info = t.info or {}
    g = lambda k: info.get(k)
    ty = lambda v: None if v is None else round(float(v) / 1e9, 1)
    out = {"ticker": ticker, "source": "yfinance", "price": g("currentPrice") or g("regularMarketPrice"),
           "shares_outstanding_m": None if g("sharesOutstanding") is None else round(g("sharesOutstanding") / 1e6, 2),
           "market_cap_bn": ty(g("marketCap")), "pe_ttm": g("trailingPE"), "pe_forward_yahoo": g("forwardPE"), "pb": g("priceToBook"),
           "eps_ttm": g("trailingEps"), "bvps": g("bookValue"), "beta": g("beta"), "roe": g("returnOnEquity"),
           "net_income_ttm_bn": ty(g("netIncomeToCommon")), "total_debt_bn": ty(g("totalDebt")), "cash_bn": ty(g("totalCash")),
           "ebitda_ttm_bn": ty(g("ebitda")), "free_cashflow_bn": ty(g("freeCashflow")), "operating_cashflow_bn": ty(g("operatingCashflow")),
           "enterprise_value_bn": ty(g("enterpriseValue")), "week52_low": g("fiftyTwoWeekLow"), "week52_high": g("fiftyTwoWeekHigh"),
           "float_shares_m": None if g("floatShares") is None else round(g("floatShares") / 1e6, 2), "note": FUND_NOTE}
    try:
        bs = t.quarterly_balance_sheet
        col = bs.columns[0]
        pick = lambda name: (None if name not in bs.index or pd.isna(bs.loc[name, col]) else round(float(bs.loc[name, col]) / 1e9, 1))
        out["balance_sheet"] = {"as_of": str(col.date()), "total_debt_bn": pick("Total Debt"), "net_debt_bn": pick("Net Debt"),
                                "equity_parent_bn": pick("Stockholders Equity"), "minority_interest_bn": pick("Minority Interest"),
                                "equity_total_bn": pick("Total Equity Gross Minority Interest")}
    except Exception as e:  # noqa: BLE001
        out["balance_sheet"] = {"error": str(e)}
    sector = (g("sector") or "") + " " + (g("industry") or "")
    if any(k in sector.lower() for k in ("bank", "financial", "insurance", "capital markets")):
        out["is_financial"] = True
        out["financial_warning"] = ("Ngân hàng/tài chính: nợ vay, tiền, EBITDA, EV, FCF, EPS TTM của Yahoo KHÔNG có ý nghĩa như doanh nghiệp thường (tiền gửi là nguyên liệu, "
                                    "lợi nhuận TTM có thể bị méo/âm do cách ghép số). Chỉ dùng giá, số cổ phiếu, P/B, BVPS, ROE làm tham chiếu và LẤY lợi nhuận, NPL, LLR, CAR, "
                                    "NIM từ BCTC/nguồn Việt Nam; định giá bằng FCFE/DDM/P/B theo ROE (pb_bank_valuation), không dùng FCFF/WACC.")
    if out["price"] and out["bvps"]:
        out["check_pb"] = round(out["price"] / out["bvps"], 2)
    if out["price"] and out["eps_ttm"]:
        out["check_pe"] = round(out["price"] / out["eps_ttm"], 2)
    return _clean(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("ticker")
    ap.add_argument("--period", default="12mo")
    ap.add_argument("--out", default=None)
    ap.add_argument("--no-chart", action="store_true")
    ap.add_argument("--as-of", default=None)
    ap.add_argument("--fundamentals", action="store_true")
    a = ap.parse_args()
    if a.fundamentals:
        print(json.dumps(fundamentals(a.ticker), ensure_ascii=False, indent=1, default=str))
        sys.exit(0)
    print(json.dumps(analyze(a.ticker, a.period, a.out, not a.no_chart, a.as_of), ensure_ascii=False, indent=1, default=str))
