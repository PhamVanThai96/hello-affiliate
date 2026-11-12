#!/usr/bin/env python3
"""
outlook_v3.py - Nhận định thiên hướng (xu hướng) có HIỆU CHUẨN XÁC SUẤT, thay cho mũi tên "dự báo" dựa trên luật.

Vì sao thay thế (kết quả kiểm chứng walk-forward trên MSN/VRE/HPG, xem documents/VERIFICATION_FINDINGS.md):
  * Mũi tên cũ (suy ra từ nhãn MUA/BÁN/THEO DÕI) chỉ đúng ~47,7% ở khung 10 phiên (thua tung đồng xu); riêng nhãn
    "BÁN" (giá < MA200) chiếm 52% số nhận định nhưng tỷ lệ tăng sau đó vẫn 50% -> không có giá trị dự báo ngắn hạn.
  * Các đặc trưng giá (động lượng, vị trí so với MA) có hiệu ứng ĐỔI DẤU theo "chế độ thị trường":
    thị trường chung trên MA200 -> quán tính (xu hướng tiếp diễn); dưới MA200 -> hồi quy (đảo chiều). Dùng một
    luật cố định cho mọi giai đoạn nên sai 2022/2026.
  * Hướng giá 10-20 phiên gần như không dự báo được chính xác (IC ~ 0,05-0,1), nhưng BIÊN ĐỘ (biến động) thì dự báo
    tốt (tương quan ATR% với |lợi suất tương lai| ~ 0,22). Vì vậy đầu ra gồm: (1) thiên hướng + xác suất đã hiệu
    chuẩn + số mẫu, có "CHƯA RÕ" khi xác suất sát 50%; (2) vùng biến động kỳ vọng (cone) theo ATR.

Không phải khuyến nghị đầu tư. Xác suất là tần suất lịch sử có điều kiện, không bảo đảm tương lai.
"""
from __future__ import annotations

import json
import os

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
CALIB_FILE = os.path.join(HERE, "outlook_calibration.json")
# Rổ đại diện "thị trường chung" (yfinance không có ^VNINDEX). Không chứa MSN/VRE/HPG để kiểm chứng độc lập.
MARKET_BASKET = ["VNM.VN", "FPT.VN", "MWG.VN", "STB.VN", "VCB.VN", "SSI.VN", "PNJ.VN"]
HORIZON = 10                      # số phiên của nhận định chính
SCORE_EDGES = [-1.01, -0.45, -0.15, 0.15, 0.45, 1.01]   # 5 nhóm điểm
NEUTRAL_BAND = 0.045              # |P(tăng) - 0,5| < band  -> CHƯA RÕ (kiểm chứng: lệch < 4-5 điểm % nằm trong nhiễu mẫu)
MIN_BUCKET_N = 300                # nhóm ít mẫu hơn -> CHƯA RÕ


# ---------------------------------------------------------------------------------------------- đặc trưng
def compute_features(df: pd.DataFrame) -> pd.DataFrame:
    """Đặc trưng véc-tơ hoá (mọi giá trị tại hàng t chỉ dùng dữ liệu <= t)."""
    c, h, l, v = df["Close"], df["High"], df["Low"], df["Volume"]
    f = pd.DataFrame({"Date": df["Date"].values})
    ma20, ma50, ma200 = (c.rolling(w).mean() for w in (20, 50, 200))
    f["c_ma50"] = (c / ma50 - 1).values
    f["c_ma200"] = (c / ma200 - 1).values
    f["roc20"] = c.pct_change(20).values
    f["roc60"] = c.pct_change(60).values
    hh, ll = h.rolling(60).max(), l.rolling(60).min()
    f["pos60"] = ((c - ll) / (hh - ll).replace(0, np.nan)).values
    tr = pd.concat([h - l, (h - c.shift()).abs(), (l - c.shift()).abs()], axis=1).max(axis=1)
    f["atrp"] = (tr.rolling(14).mean() / c).values
    f["volr"] = (v / v.rolling(20).mean()).values
    return f


def raw_score(f: pd.DataFrame) -> pd.Series:
    """Điểm "xu hướng thuần" trong [-1, 1]: >0 = giá đang mạnh/đi lên so với nền."""
    s_trend = (f["c_ma50"] / 0.10).clip(-1, 1)
    s_mom = (f["roc20"] / 0.10).clip(-1, 1)
    s_mom60 = (f["roc60"] / 0.20).clip(-1, 1)
    s_pos = (f["pos60"] - 0.5) * 2
    return (s_trend + s_mom + s_mom60 + s_pos) / 4.0


# ---------------------------------------------------------------------------------------------- thị trường chung
_PROXY_CACHE: dict = {}


def _load_close(ticker: str) -> pd.DataFrame:
    import yfinance as yf
    cache_dir = os.environ.get("OUTLOOK_CACHE", "/tmp")
    path = os.path.join(cache_dir, f"hist_{ticker}.pkl")
    if os.path.exists(path):
        d = pd.read_pickle(path)
        last = pd.Timestamp(d["Date"].iloc[-1])
        if (pd.Timestamp.now().normalize() - last).days <= 3:
            return d
    d = yf.Ticker(ticker).history(period="max", interval="1d").reset_index()
    d["Date"] = pd.to_datetime(d["Date"]).dt.tz_localize(None)
    d = d[["Date", "Open", "High", "Low", "Close", "Volume"]].dropna()
    d = d[d["Volume"] > 0].reset_index(drop=True)
    d.to_pickle(path)
    return d


def market_proxy(basket: list | None = None) -> pd.DataFrame:
    """Chỉ số "thị trường chung" = trung bình đều lợi suất ngày của rổ; trả về mk_up (trên MA200) và mk_roc60."""
    basket = tuple(basket or MARKET_BASKET)
    if basket in _PROXY_CACHE:
        return _PROXY_CACHE[basket]
    rets = {}
    for tk in basket:
        try:
            d = _load_close(tk)
            rets[tk] = d.set_index("Date")["Close"].pct_change()
        except Exception:  # noqa: BLE001 - một mã lỗi không làm hỏng cả rổ
            continue
    if not rets:
        raise RuntimeError("Không tải được dữ liệu thị trường chung (rổ trống).")
    mk = (1 + pd.DataFrame(rets).mean(axis=1).fillna(0)).cumprod()
    out = pd.DataFrame({"mk": mk})
    out["mk_up"] = (out["mk"] > out["mk"].rolling(200).mean()).astype(float)
    out.loc[out["mk"].rolling(200).mean().isna(), "mk_up"] = np.nan
    out["mk_roc60"] = out["mk"].pct_change(60)
    _PROXY_CACHE[basket] = out
    return out


def regime_at(proxy: pd.DataFrame, date) -> tuple[str, float | None]:
    """Chế độ thị trường tại ngày (dùng giá trị gần nhất <= date)."""
    sub = proxy.loc[:pd.Timestamp(date)]
    sub = sub.dropna(subset=["mk_up"])
    if sub.empty:
        return "UNKNOWN", None
    last = sub.iloc[-1]
    return ("UP" if last["mk_up"] >= 0.5 else "DOWN"), float(last["mk_roc60"]) if pd.notna(last["mk_roc60"]) else None


# ---------------------------------------------------------------------------------------------- hiệu chuẩn
def signed_score(raw: pd.Series | float, regime: str):
    """Chế độ UP: giữ dấu (xu hướng tiếp diễn). Chế độ DOWN: đảo dấu (hồi quy)."""
    sign = 1.0 if regime != "DOWN" else -1.0
    return raw * sign


def _bucket(score: float) -> int:
    for i in range(len(SCORE_EDGES) - 1):
        if SCORE_EDGES[i] <= score < SCORE_EDGES[i + 1]:
            return i
    return len(SCORE_EDGES) - 2


def build_calibration(histories: dict, proxy: pd.DataFrame, end_year: int | None = None) -> dict:
    """Bảng tần suất lịch sử có điều kiện: (chế độ, nhóm điểm) -> P(tăng 10 phiên), lợi suất TB, số mẫu.
    `end_year`: chỉ dùng dữ liệu có ngày <= 31/12/end_year (để kiểm chứng ngoài mẫu)."""
    rows = []
    for tk, d in histories.items():
        f = compute_features(d)
        f["fwd"] = (d["Close"].shift(-HORIZON) / d["Close"] - 1).values
        f["fwd_sigma"] = f["fwd"] / (f["atrp"] * np.sqrt(HORIZON))
        f["tk"] = tk
        rows.append(f)
    F = pd.concat(rows).dropna(subset=["c_ma50", "roc20", "roc60", "pos60", "atrp", "fwd"])
    F = F.merge(proxy[["mk_up"]], left_on="Date", right_index=True).dropna(subset=["mk_up"])
    if end_year:
        F = F[F["Date"].dt.year <= end_year]
    F["regime"] = np.where(F["mk_up"] >= 0.5, "UP", "DOWN")
    F["raw"] = raw_score(F)
    F["score"] = F["raw"] * np.where(F["regime"] == "DOWN", -1.0, 1.0)
    F["bucket"] = F["score"].apply(_bucket)
    table = {}
    for (rg, b), s in F.groupby(["regime", "bucket"]):
        table[f"{rg}|{b}"] = {"n": int(len(s)), "p_up": round(float((s["fwd"] > 0).mean()), 4),
                              "mean_ret": round(float(s["fwd"].mean()), 5)}
    # cone: hệ số k để ~80% lợi suất 10 phiên nằm trong ±k * ATR% * sqrt(h)
    z = F["fwd_sigma"].abs()
    k80 = float(np.quantile(z, 0.80))
    base_up = float((F["fwd"] > 0).mean())
    return {"horizon": HORIZON, "edges": SCORE_EDGES, "table": table, "cone_k80": round(k80, 3),
            "base_p_up": round(base_up, 4), "n_total": int(len(F)),
            "end_year": end_year, "basket": MARKET_BASKET}


def load_calibration(path: str | None = None) -> dict:
    path = path or CALIB_FILE
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------------------------------- nhận định
LABELS = {1: "NGHIÊNG TĂNG (nhẹ)", -1: "NGHIÊNG GIẢM (nhẹ)", 0: "CHƯA RÕ HƯỚNG"}
STRONG_BAND = 0.09                # lệch >= 9 điểm % mới gọi "THIÊN HƯỚNG" (rất hiếm trong dữ liệu lịch sử)


def trend_state(df: pd.DataFrame) -> dict:
    """Mô tả TRẠNG THÁI xu hướng hiện tại (khách quan, không phải dự báo)."""
    c = df["Close"]
    ma20, ma50, ma200 = (c.rolling(w).mean().iloc[-1] for w in (20, 50, 200))
    close = float(c.iloc[-1])
    if pd.notna(ma200) and close > ma50 > ma200:
        structure = "TĂNG (giá > MA50 > MA200)"
    elif pd.notna(ma200) and close < ma50 < ma200:
        structure = "GIẢM (giá < MA50 < MA200)"
    elif pd.notna(ma50) and close > ma50:
        structure = "PHỤC HỒI / HỖN HỢP (giá trên MA50 nhưng chưa xếp hàng tăng)"
    elif pd.notna(ma50):
        structure = "YẾU / HỖN HỢP (giá dưới MA50)"
    else:
        structure = "KHÔNG ĐỦ DỮ LIỆU"
    hh, ll = df["High"].tail(60).max(), df["Low"].tail(60).min()
    return {"structure": structure, "close": close,
            "ma50": None if pd.isna(ma50) else float(ma50), "ma200": None if pd.isna(ma200) else float(ma200),
            "roc20_pct": round(float(c.pct_change(20).iloc[-1] * 100), 1) if len(c) > 20 else None,
            "pos60_pct": round(float((close - ll) / (hh - ll) * 100), 0) if hh > ll else None}


def build_outlook(df: pd.DataFrame, proxy: pd.DataFrame | None = None, calib: dict | None = None) -> dict:
    """Nhận định thiên hướng tại phiên cuối của df (df chỉ chứa dữ liệu <= ngày phân tích)."""
    calib = calib or load_calibration()
    proxy = proxy if proxy is not None else market_proxy()
    f = compute_features(df).iloc[-1]
    date = df["Date"].iloc[-1]
    close = float(df["Close"].iloc[-1])
    regime, mk_roc60 = regime_at(proxy, date)
    need = ["c_ma50", "roc20", "roc60", "pos60", "atrp"]
    if any(pd.isna(f[k]) for k in need):
        return {"direction": 0, "label": LABELS[0], "regime": regime, "p_up": None, "n": 0,
                "reason": "Không đủ dữ liệu lịch sử (cần >= 60 phiên).", "close": close, "horizon": calib["horizon"]}
    raw = float(raw_score(pd.DataFrame([f])).iloc[0])
    score = float(signed_score(raw, regime))
    b = _bucket(score)
    cell = calib["table"].get(f"{regime if regime != 'UNKNOWN' else 'UP'}|{b}")
    p_up = cell["p_up"] if cell else None
    n = cell["n"] if cell else 0
    mean_ret = cell["mean_ret"] if cell else None
    direction, strong = 0, False
    if p_up is not None and n >= MIN_BUCKET_N:
        if p_up >= 0.5 + NEUTRAL_BAND:
            direction = 1
        elif p_up <= 0.5 - NEUTRAL_BAND:
            direction = -1
        strong = abs(p_up - 0.5) >= STRONG_BAND
    h = calib["horizon"]
    sigma_h = float(f["atrp"]) * np.sqrt(h) * calib["cone_k80"]
    drift = float(mean_ret) if mean_ret is not None else 0.0
    cone_lo, cone_hi = close * (1 + drift - sigma_h), close * (1 + drift + sigma_h)
    regime_txt = {"UP": "thị trường chung trên MA200 (ưu tiên quán tính)",
                  "DOWN": "thị trường chung dưới MA200 (ưu tiên hồi quy: đà giảm/tăng mạnh dễ đảo chiều)",
                  "UNKNOWN": "chưa xác định chế độ thị trường"}[regime]
    reason = (f"Chế độ: {regime_txt}. Điểm xu hướng thuần {raw:+.2f} -> điểm điều chỉnh {score:+.2f} "
              f"(nhóm {b + 1}/5). Tần suất lịch sử có điều kiện: tăng sau {h} phiên {p_up*100:.0f}% (n={n}), "
              f"lợi suất TB {drift*100:+.1f}%." if p_up is not None else "Chưa có hiệu chuẩn cho nhóm này.")
    label = LABELS[direction].replace("NGHIÊNG", "THIÊN HƯỚNG").replace(" (nhẹ)", "") if strong else LABELS[direction]
    return {"direction": direction, "label": label, "trend_state": trend_state(df), "regime": regime, "p_up": p_up, "n": n,
            "score": round(score, 3), "raw_score": round(raw, 3), "mean_ret": mean_ret, "horizon": h,
            "close": close, "cone_low": float(cone_lo), "cone_high": float(cone_hi),
            "sigma_h_pct": round(sigma_h * 100, 2), "market_roc60": mk_roc60, "reason": reason,
            "caveat": "Tần suất lịch sử có điều kiện, không phải dự báo hay khuyến nghị đầu tư."}
