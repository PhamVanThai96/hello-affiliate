#! /usr/bin/env python3

"""
chart_analysis_skill.py
========================
AI Skill độc lập tái sử dụng: Phân tích kỹ thuật cổ phiếu tự động theo
khung thời gian NGÀY (Daily timeframe - interval mặc định "1d").

Bao gồm:
- Tải dữ liệu OHLCV theo ngày (yfinance, interval="1d")
- Tính toán Kênh xu hướng (Trend Channel) bằng argrelextrema + polyfit
- Tính các chỉ báo kỹ thuật (MA20/50/200, RSI14, Bollinger Bands)
- Nhận diện mô hình nến Nhật (Engulfing, Hammer, Shooting Star, Doji, Morning/Evening Star)
- Xác định Hỗ trợ/Kháng cự
- Khung quản trị rủi ro & khuyến nghị Mua/Bán/Theo dõi
- Vẽ và xuất biểu đồ (mplfinance)

File này nằm trong thư mục `dev/`. Các thư mục dữ liệu (`ai-session/`, `documents/`,
`output/`) và file `config_analysis.json` nằm ở thư mục gốc dự án (một cấp trên `dev/`) -
đường dẫn được tự động phân giải qua PROJECT_ROOT bên dưới, nên script chạy đúng
dù được gọi từ thư mục gốc hay từ bên trong `dev/`.

Sử dụng:
    from chart_analysis_skill import run_stock_analysis_skill
    result = run_stock_analysis_skill("STB.VN", interval="1d")
    # Cấu hình phân tích được đọc từ config_analysis.json nếu chạy hàng loạt
"""

import os
import json
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import yfinance as yf
from scipy.signal import argrelextrema

# Thư mục gốc dự án = thư mục cha của thư mục chứa file này (dev/)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------------------
# Bước 2: Thu thập dữ liệu (mặc định khung NGÀY - interval="1d")
# ---------------------------------------------------------------------------
def fetch_stock_data(ticker: str, period: str = "12mo", interval: str = "1d") -> pd.DataFrame:
    """Tải dữ liệu OHLCV lịch sử theo NGÀY (Daily) cho mã cổ phiếu qua yfinance.
    interval="1d" là bắt buộc mặc định để đảm bảo phân tích trên khung ngày,
    không dùng khung tuần ("1wk") hay tháng ("1mo")."""
    t = yf.Ticker(ticker)
    df = t.history(period=period, interval=interval)
    if df.empty:
        raise ValueError(f"Không tải được dữ liệu cho mã {ticker}. Kiểm tra lại mã cổ phiếu.")
    df = df.reset_index()
    df.columns = [c if c != "Date" else "Date" for c in df.columns]
    df["Date"] = pd.to_datetime(df["Date"]).dt.tz_localize(None)
    df = df[["Date", "Open", "High", "Low", "Close", "Volume"]].dropna().reset_index(drop=True)
    return df


# ---------------------------------------------------------------------------
# Bước 2b: Kênh xu hướng (Trend Channel) bằng thuật toán
# ---------------------------------------------------------------------------
def compute_trend_channel(df: pd.DataFrame, order: int = 5) -> dict:
    """
    Nhận diện Kênh xu hướng bằng toán học:
    1. Tìm đỉnh/đáy cụm (fractals) bằng argrelextrema.
    2. Hồi quy tuyến tính (polyfit) qua các đáy -> đường biên dưới (support trendline).
    3. Hồi quy tuyến tính qua các đỉnh -> đường biên trên (channel line).
    4. Đánh giá độ song song (sai số độ dốc < 15%) -> phân loại kênh.
    """
    highs = df["High"].values
    lows = df["Low"].values
    n = len(df)
    x = np.arange(n)

    peak_idx = argrelextrema(highs, np.greater_equal, order=order)[0]
    trough_idx = argrelextrema(lows, np.less_equal, order=order)[0]

    # Loại bỏ điểm trùng lặp liền kề (do np.greater_equal có thể chọn cả dải bằng nhau)
    peak_idx = np.unique(peak_idx)
    trough_idx = np.unique(trough_idx)

    result = {
        "peak_idx": peak_idx.tolist(),
        "trough_idx": trough_idx.tolist(),
    }

    if len(peak_idx) >= 2 and len(trough_idx) >= 2:
        upper_slope, upper_intercept = np.polyfit(peak_idx, highs[peak_idx], 1)
        lower_slope, lower_intercept = np.polyfit(trough_idx, lows[trough_idx], 1)

        upper_line = upper_slope * x + upper_intercept
        lower_line = lower_slope * x + lower_intercept

        # Sai số độ dốc tương đối để đánh giá độ song song
        denom = max(abs(upper_slope), abs(lower_slope), 1e-9)
        slope_diff_ratio = abs(upper_slope - lower_slope) / denom
        is_parallel = slope_diff_ratio < 0.15

        avg_slope = (upper_slope + lower_slope) / 2
        # Ngưỡng phần trăm/phiên so với giá trung bình để phân loại đi ngang
        avg_price = float(df["Close"].mean())
        slope_pct_per_bar = (avg_slope / avg_price) * 100 if avg_price else 0

        if abs(slope_pct_per_bar) < 0.03:
            channel_type = "Horizontal (Đi ngang)"
        elif avg_slope > 0:
            channel_type = "Ascending (Kênh tăng)"
        else:
            channel_type = "Descending (Kênh giảm)"

        result.update({
            "upper_slope": float(upper_slope),
            "upper_intercept": float(upper_intercept),
            "lower_slope": float(lower_slope),
            "lower_intercept": float(lower_intercept),
            "upper_line": upper_line.tolist(),
            "lower_line": lower_line.tolist(),
            "is_parallel": bool(is_parallel),
            "slope_diff_ratio": float(slope_diff_ratio),
            "channel_type": channel_type if is_parallel else "Không xác định rõ kênh (không song song)",
            "valid": True,
        })
    else:
        result.update({
            "valid": False,
            "channel_type": "Không đủ dữ liệu đỉnh/đáy để xác định kênh",
        })

    return result


# ---------------------------------------------------------------------------
# Bước 3: Chỉ báo kỹ thuật (tự viết bằng pandas/numpy - thay thế pandas-ta
# vì pandas-ta yêu cầu Python >=3.12)
# ---------------------------------------------------------------------------
def compute_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Tính MA20/50/200, RSI14, Bollinger Bands (20, 2)."""
    out = df.copy()
    out["MA20"] = out["Close"].rolling(window=20).mean()
    out["MA50"] = out["Close"].rolling(window=50).mean()
    out["MA200"] = out["Close"].rolling(window=200).mean()

    # RSI(14) - công thức Wilder's smoothing
    delta = out["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / 14, min_periods=14, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / 14, min_periods=14, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    out["RSI14"] = 100 - (100 / (1 + rs))

    # Bollinger Bands (20, 2)
    bb_mid = out["Close"].rolling(window=20).mean()
    bb_std = out["Close"].rolling(window=20).std()
    out["BB_MID"] = bb_mid
    out["BB_UPPER"] = bb_mid + 2 * bb_std
    out["BB_LOWER"] = bb_mid - 2 * bb_std

    return out


# ---------------------------------------------------------------------------
# Bước 3b: Nhận diện Mô hình Nến Nhật bằng thuật toán
# ---------------------------------------------------------------------------
def _body(row):
    return abs(row["Close"] - row["Open"])


def _range(row):
    return row["High"] - row["Low"]


def _is_bullish(row):
    return row["Close"] > row["Open"]


def detect_candlestick_patterns(df: pd.DataFrame, lookback: int = 5) -> list:
    """
    Quét N phiên gần nhất để phát hiện các mẫu hình nến đảo chiều cốt lõi:
    Bullish/Bearish Engulfing, Hammer, Shooting Star, Doji, Morning/Evening Star.
    Trả về danh sách dict: {index, date, pattern, meaning}
    """
    patterns = []
    n = len(df)
    start = max(1, n - lookback)

    for i in range(start, n):
        row = df.iloc[i]
        prev = df.iloc[i - 1]
        rng = _range(row)
        body = _body(row)
        if rng == 0:
            continue
        upper_shadow = row["High"] - max(row["Close"], row["Open"])
        lower_shadow = min(row["Close"], row["Open"]) - row["Low"]
        body_ratio = body / rng

        found = None
        meaning = None

        # Doji: thân nến rất nhỏ so với biên độ
        if body_ratio < 0.1:
            found, meaning = "Doji", "Lưỡng lự, tâm lý thị trường giằng co giữa bên mua/bán"

        # Hammer: thân nhỏ ở trên, bóng dưới dài (>= 2 lần thân), bóng trên ngắn
        elif lower_shadow >= 2 * body and upper_shadow <= body * 0.5 and body_ratio < 0.4:
            found, meaning = "Hammer (Nến búa)", "Tín hiệu đảo chiều tăng, lực cầu xuất hiện tại đáy"

        # Shooting Star: thân nhỏ ở dưới, bóng trên dài, bóng dưới ngắn
        elif upper_shadow >= 2 * body and lower_shadow <= body * 0.5 and body_ratio < 0.4:
            found, meaning = "Shooting Star (Sao băng)", "Tín hiệu đảo chiều giảm, áp lực bán xuất hiện tại đỉnh"

        # Bullish Engulfing: nến trước giảm, nến sau tăng và "nhấn chìm" thân nến trước
        elif (not _is_bullish(prev)) and _is_bullish(row) and \
                row["Close"] >= prev["Open"] and row["Open"] <= prev["Close"]:
            found, meaning = "Bullish Engulfing (Nhấn chìm tăng)", "Phe mua áp đảo hoàn toàn phe bán, tín hiệu đảo chiều tăng"

        # Bearish Engulfing: nến trước tăng, nến sau giảm và "nhấn chìm" thân nến trước
        elif _is_bullish(prev) and (not _is_bullish(row)) and \
                row["Open"] >= prev["Close"] and row["Close"] <= prev["Open"]:
            found, meaning = "Bearish Engulfing (Nhấn chìm giảm)", "Phe bán áp đảo hoàn toàn phe mua, tín hiệu đảo chiều giảm"

        # Morning Star / Evening Star (cần 3 nến)
        if found is None and i >= 2:
            c1, c2, c3 = df.iloc[i - 2], df.iloc[i - 1], row
            c1_body = _body(c1)
            c2_body = _body(c2)
            c3_body = _body(c3)
            if (not _is_bullish(c1)) and c2_body < c1_body * 0.4 and _is_bullish(c3) and \
                    c3["Close"] > (c1["Open"] + c1["Close"]) / 2:
                found, meaning = "Morning Star (Sao mai)", "Mẫu hình đảo chiều tăng mạnh sau xu hướng giảm"
            elif _is_bullish(c1) and c2_body < c1_body * 0.4 and (not _is_bullish(c3)) and \
                    c3["Close"] < (c1["Open"] + c1["Close"]) / 2:
                found, meaning = "Evening Star (Sao hôm)", "Mẫu hình đảo chiều giảm mạnh sau xu hướng tăng"

        if found:
            patterns.append({
                "index": int(i),
                "date": str(df.iloc[i]["Date"].date()),
                "pattern": found,
                "meaning": meaning,
            })

    return patterns


# ---------------------------------------------------------------------------
# Bước 4.1: Hỗ trợ / Kháng cự (dựa trên đỉnh/đáy fractal đã tìm được)
# ---------------------------------------------------------------------------
def find_support_resistance(df: pd.DataFrame, channel: dict, tolerance_pct: float = 1.5) -> dict:
    """
    Gom cụm các đỉnh/đáy lịch sử thành vùng Hỗ trợ/Kháng cự (theo % dung sai giá),
    vùng nào được chạm nhiều lần nhất được coi là mạnh nhất.
    """
    highs = df["High"].values
    lows = df["Low"].values
    peak_idx = channel.get("peak_idx", [])
    trough_idx = channel.get("trough_idx", [])

    def cluster(values, tol_pct):
        if len(values) == 0:
            return []
        sorted_vals = sorted(values)
        clusters = [[sorted_vals[0]]]
        for v in sorted_vals[1:]:
            if abs(v - clusters[-1][-1]) / clusters[-1][-1] * 100 <= tol_pct:
                clusters[-1].append(v)
            else:
                clusters.append([v])
        return [{"level": float(np.mean(c)), "touches": len(c)} for c in clusters]

    resistance_zones = sorted(cluster([highs[i] for i in peak_idx], tolerance_pct),
                               key=lambda x: -x["touches"])
    support_zones = sorted(cluster([lows[i] for i in trough_idx], tolerance_pct),
                            key=lambda x: -x["touches"])

    return {
        "support_zones": support_zones[:5],
        "resistance_zones": resistance_zones[:5],
        "strongest_support": support_zones[0] if support_zones else None,
        "strongest_resistance": resistance_zones[0] if resistance_zones else None,
    }


# ---------------------------------------------------------------------------
# Bước 4.2: Khung Quản trị Rủi ro & Khuyến nghị
# ---------------------------------------------------------------------------
def generate_recommendation(df_ind: pd.DataFrame, channel: dict, sr: dict) -> dict:
    """
    Áp dụng bộ lọc quản trị rủi ro nghiêm ngặt:
    - MUA: giá > MA200 VÀ giá pullback về hỗ trợ mạnh hoặc cạnh dưới kênh tăng VÀ RSI < 65.
    - R:R tối thiểu 1:2, Stop Loss tối đa 7% từ điểm mua.
    - Nếu không hội tụ đủ điều kiện hoặc phá vỡ giả -> THEO DÕI hoặc BÁN.
    """
    last = df_ind.iloc[-1]
    close = float(last["Close"])
    ma200 = last["MA200"]
    rsi = float(last["RSI14"]) if not np.isnan(last["RSI14"]) else None

    long_term_trend = "Không đủ dữ liệu (thiếu MA200)"
    above_ma200 = None
    if not np.isnan(ma200):
        above_ma200 = bool(close > ma200)
        long_term_trend = "Tăng" if above_ma200 else "Giảm"

    channel_valid = channel.get("valid", False)
    lower_edge = channel["lower_line"][-1] if channel_valid else None
    upper_edge = channel["upper_line"][-1] if channel_valid else None

    near_lower_channel = False
    if channel_valid and lower_edge:
        near_lower_channel = abs(close - lower_edge) / lower_edge * 100 <= 3.0

    near_support = False
    support_level = sr.get("strongest_support", {}).get("level") if sr.get("strongest_support") else None
    if support_level:
        near_support = abs(close - support_level) / support_level * 100 <= 3.0

    # Phát hiện phá vỡ giả: giá vượt biên kênh trước đó rồi quay lại trong kênh ở phiên gần nhất
    false_breakout = False
    if channel_valid and len(df_ind) >= 3:
        prev_close = float(df_ind.iloc[-2]["Close"])
        prev_upper = channel["upper_line"][-2]
        prev_lower = channel["lower_line"][-2]
        if (prev_close > prev_upper and close < upper_edge) or (prev_close < prev_lower and close > lower_edge):
            false_breakout = True

    action = "THEO DÕI"
    reason = []
    entry_zone = tp = sl = rr = None

    buy_condition = (
        above_ma200 is True and
        (near_support or near_lower_channel) and
        rsi is not None and rsi < 65 and
        not false_breakout
    )

    if buy_condition:
        entry_low = close * 0.99
        entry_high = close * 1.01
        sl_candidate = lower_edge * 0.98 if lower_edge else close * 0.93
        # Đảm bảo SL luôn thấp hơn giá đóng cửa hiện tại (đề phòng giá đã nằm sát/dưới cạnh kênh)
        sl_candidate = min(sl_candidate, close * 0.98)
        sl_pct = (close - sl_candidate) / close * 100
        if sl_pct > 7:
            sl_candidate = close * 0.93  # giới hạn cắt lỗ tối đa 7%
        tp_candidate = upper_edge if upper_edge else close * 1.15
        # đảm bảo có kháng cự cũ làm mục tiêu thay thế nếu xa hơn kênh
        if sr.get("strongest_resistance") and sr["strongest_resistance"]["level"] > close:
            tp_candidate = max(tp_candidate, sr["strongest_resistance"]["level"])

        risk = close - sl_candidate
        reward = tp_candidate - close
        rr = round(reward / risk, 2) if risk > 0 else None

        if rr is not None and rr >= 2:
            action = "MUA"
            entry_zone = (round(entry_low), round(entry_high))
            tp = round(tp_candidate)
            sl = round(sl_candidate)
            reason.append("Giá trên MA200 (xu hướng dài hạn Tăng)")
            reason.append("Giá đang pullback về vùng Hỗ trợ/cạnh dưới kênh tăng")
            reason.append(f"RSI={rsi:.1f} < 65, chưa quá mua")
            reason.append(f"Tỷ lệ R:R = 1:{rr} đạt tối thiểu 1:2")
        else:
            action = "THEO DÕI"
            reason.append(f"Đủ điều kiện xu hướng/kỹ thuật nhưng R:R ({rr}) chưa đạt tối thiểu 1:2")
    else:
        if false_breakout:
            action = "THEO DÕI"
            reason.append("Phát hiện khả năng Phá vỡ giả (False Breakout) khỏi kênh xu hướng")
        elif above_ma200 is False:
            action = "BÁN"
            reason.append("Giá nằm dưới MA200 - xu hướng dài hạn Giảm")
        elif rsi is not None and rsi >= 65:
            action = "THEO DÕI"
            reason.append(f"RSI={rsi:.1f} đã tiệm cận/vượt vùng quá mua (>=65)")
        else:
            action = "THEO DÕI"
            reason.append("Giá chưa điều chỉnh về vùng Hỗ trợ mạnh hoặc cạnh dưới kênh tăng")

    return {
        "action": action,
        "close": close,
        "long_term_trend": long_term_trend,
        "rsi": rsi,
        "channel_type": channel.get("channel_type"),
        "near_support": near_support,
        "near_lower_channel": near_lower_channel,
        "false_breakout": false_breakout,
        "entry_zone": entry_zone,
        "take_profit": tp,
        "stop_loss": sl,
        "risk_reward": rr,
        "reasons": reason,
    }


# Màu chú thích khuyến nghị trên biểu đồ theo hành động (action)
ACTION_COLORS = {
    "MUA": "darkgreen",
    "BÁN": "red",
    "THEO DÕI": "gold",
}


# ---------------------------------------------------------------------------
# Bước 5: Vẽ và xuất biểu đồ (mplfinance)
# ---------------------------------------------------------------------------
def plot_chart(df_ind: pd.DataFrame, channel: dict, sr: dict, patterns: list,
               ticker: str, output_dir: str = "output", rec: dict = None) -> str:
    """Vẽ biểu đồ nến + MA + Kênh xu hướng + Hỗ trợ/Kháng cự + chú thích mô hình nến.

    Nếu `rec` (khuyến nghị từ `generate_recommendation`) được truyền vào, chú thích
    khuyến nghị (action) và lý do (reason) sẽ được vẽ lên góc trên bên trái biểu đồ,
    với màu nền: xanh lá đậm = MUA, đỏ = BÁN, vàng = THEO DÕI.
    """
    import mplfinance as mpf

    os.makedirs(output_dir, exist_ok=True)
    plot_df = df_ind.set_index("Date")[["Open", "High", "Low", "Close", "Volume"]].copy()

    add_plots = []
    for col, color in [("MA20", "blue"), ("MA50", "orange"), ("MA200", "purple")]:
        if col in df_ind.columns and df_ind[col].notna().any():
            add_plots.append(mpf.make_addplot(df_ind[col].values, color=color, width=0.9))

    if channel.get("valid"):
        add_plots.append(mpf.make_addplot(np.array(channel["upper_line"]), color="red", width=1.2, linestyle="--"))
        add_plots.append(mpf.make_addplot(np.array(channel["lower_line"]), color="green", width=1.2, linestyle="--"))

    fig, axlist = mpf.plot(
        plot_df,
        type="candle",
        style="yahoo",
        addplot=add_plots if add_plots else None,
        volume=True,
        returnfig=True,
        figsize=(14, 8),
        title=f"\n{ticker} - Phân tích Kỹ thuật & Kênh xu hướng",
    )
    ax = axlist[0]

    for sup in sr.get("support_zones", [])[:3]:
        ax.axhline(y=sup["level"], color="darkblue", linestyle="-", linewidth=1.5, alpha=0.9)
    for res in sr.get("resistance_zones", [])[:3]:
        ax.axhline(y=res["level"], color="darkred", linestyle="-", linewidth=1.5, alpha=0.9)

    n = len(df_ind)
    for p in patterns:
        idx = p["index"]
        if 0 <= idx < n:
            y = float(df_ind.iloc[idx]["High"]) * 1.01
            ax.annotate(
                p["pattern"].split(" (")[0],
                xy=(idx, y),
                xytext=(idx, y * 1.03),
                fontsize=8,
                color="black",
                arrowprops=dict(arrowstyle="->", color="black", lw=1),
                ha="center",
            )

    if rec:
        action = rec.get("action", "THEO DÕI")
        box_color = ACTION_COLORS.get(action, "gray")
        label = f"KHUYẾN NGHỊ: {action}"
        reasons = rec.get("reasons") or []
        if reasons:
            label += "\n" + "\n".join(f"- {r}" for r in reasons)
        # Chữ đen trên nền vàng để dễ đọc; chữ trắng trên nền xanh lá đậm/đỏ
        text_color = "black" if action == "THEO DÕI" else "white"
        ax.text(
            0.01, 0.98, label,
            transform=ax.transAxes,
            fontsize=9,
            fontweight="bold",
            color=text_color,
            va="top",
            ha="left",
            bbox=dict(boxstyle="round,pad=0.4", facecolor=box_color, edgecolor="black", alpha=0.9),
        )

    # Mở rộng trục x để có khoảng trống cho mũi tên dự báo xu hướng
    ax.set_xlim(-1, n + 8)
    curr_x = n - 1
    curr_y = float(df_ind.iloc[-1]["Close"])
    act = rec.get("action", "THEO DÕI") if rec else "THEO DÕI"

    if act == "MUA":
        tgt_y = rec.get("take_profit") or curr_y * 1.12
        ax.annotate("", xy=(curr_x + 6, tgt_y), xytext=(curr_x, curr_y),
                    arrowprops=dict(facecolor="#00e676", edgecolor="#004d40", arrowstyle="-|>", mutation_scale=20, lw=2.2), zorder=8)
        ax.text(curr_x + 6, tgt_y * 1.01, f"Dự báo TĂNG\nTarget: {tgt_y:,.0f}",
                fontsize=8, fontweight="bold", color="#00796b", ha="center", va="bottom", zorder=9)
    elif act == "BÁN":
        tgt_y = curr_y * 0.90
        ax.annotate("", xy=(curr_x + 6, tgt_y), xytext=(curr_x, curr_y),
                    arrowprops=dict(facecolor="#ff1744", edgecolor="#b71c1c", arrowstyle="-|>", mutation_scale=20, lw=2.2), zorder=8)
        ax.text(curr_x + 6, tgt_y * 0.99, f"Dự báo GIẢM\nHỗ trợ: {tgt_y:,.0f}",
                fontsize=8, fontweight="bold", color="#c62828", ha="center", va="top", zorder=9)
    else:
        tgt_y = curr_y * 1.05
        ax.annotate("", xy=(curr_x + 6, tgt_y), xytext=(curr_x, curr_y),
                    arrowprops=dict(facecolor="#ff9100", edgecolor="#e65100", arrowstyle="-|>", mutation_scale=18, lw=2.0), zorder=8)
        ax.text(curr_x + 6, tgt_y * 1.01, f"Dự báo Hồi\nCản: {tgt_y:,.0f}",
                fontsize=8, fontweight="bold", color="#e65100", ha="center", va="bottom", zorder=9)

    clean_tk = ticker.split(".")[0]
    if "Date" in df_ind.columns and len(df_ind) > 0:
        date_str = pd.to_datetime(df_ind.iloc[-1]["Date"]).strftime("%d-%m-%Y")
    else:
        date_str = datetime.now().strftime("%d-%m-%Y")

    act_raw = rec.get("action", "THEO DÕI") if rec else "THEO DÕI"
    if "MUA" in act_raw.upper():
        slug = "MUA"
    elif "BÁN" in act_raw.upper() or "BAN" in act_raw.upper():
        slug = "BAN"
    else:
        slug = "THEO-DOI"

    # Định dạng tên file output có thông tin khuyến nghị: [MÃ]-[NGÀY]-[KHUYẾN NGHỊ]-v1.png
    filename = f"{clean_tk}-{date_str}-{slug}-v1.png"
    out_path = os.path.join(output_dir, filename)
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    import matplotlib.pyplot as plt
    plt.close(fig)
    return out_path


# ---------------------------------------------------------------------------
# Bước 6: Sơ đồ tư duy Mermaid.js
# ---------------------------------------------------------------------------
def generate_mindmap(ticker: str, macro_state: str, channel: dict, patterns: list, rec: dict) -> str:
    """Tạo sơ đồ tư duy Mermaid.js: Vĩ mô -> Kênh xu hướng -> Mô hình nến -> Khuyến nghị."""
    recent_patterns = patterns[-3:] if patterns else []
    if recent_patterns:
        pattern_lines = "\n".join(
            f'        P{i}["{p["pattern"]}"]' for i, p in enumerate(recent_patterns)
        )
        pattern_links = "\n".join(f"    Channel --> P{i}" for i in range(len(recent_patterns)))
        last_pattern_node = f"P{len(recent_patterns) - 1}"
    else:
        pattern_lines = '        P0["Không phát hiện mô hình nổi bật"]'
        pattern_links = "    Channel --> P0"
        last_pattern_node = "P0"

    reason_text = "; ".join(rec["reasons"][:2]) if rec.get("reasons") else "Không có ghi chú thêm"

    mindmap = f"""graph TD
    Macro["Trạng thái vĩ mô: {macro_state}"] --> Channel["Kênh xu hướng: {channel.get('channel_type')}"]
{pattern_lines}
{pattern_links}
    {last_pattern_node} --> Action["Khuyến nghị: {rec['action']}"]
    Action --> Reason["{reason_text}"]
"""
    return mindmap


# ---------------------------------------------------------------------------
# Session & RAG sync (dùng chung với ai-session/doc_index.json)
# ---------------------------------------------------------------------------
def load_session(session_file: str = None) -> dict:
    session_file = session_file or os.path.join(PROJECT_ROOT, "ai-session", "agent_session.json")
    if os.path.exists(session_file):
        with open(session_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_session(state: dict, session_file: str = None) -> None:
    session_file = session_file or os.path.join(PROJECT_ROOT, "ai-session", "agent_session.json")
    session_dir = os.path.dirname(session_file)
    if session_dir:
        os.makedirs(session_dir, exist_ok=True)
    with open(session_file, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def log_recommendation(ticker: str, rec: dict, chart_path: str = None, log_file: str = None) -> None:
    """Ghi khuyến nghị (action + reason) của mỗi lần phân tích vào file log JSON Lines
    (mỗi dòng là 1 JSON object), lưu tại `ai-session/recommendation_log.jsonl`.
    """
    log_file = log_file or os.path.join(PROJECT_ROOT, "ai-session", "recommendation_log.jsonl")
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "ticker": ticker,
        "action": rec.get("action"),
        "close": rec.get("close"),
        "reasons": rec.get("reasons"),
        "entry_zone": rec.get("entry_zone"),
        "take_profit": rec.get("take_profit"),
        "stop_loss": rec.get("stop_loss"),
        "risk_reward": rec.get("risk_reward"),
        "chart_path": chart_path,
    }
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def rag_sync_check(knowledge_dirs=None, index_file: str = None) -> dict:
    """Kiểm tra thay đổi tài liệu bằng MD5, cập nhật index nếu có thay đổi."""
    import hashlib

    knowledge_dirs = knowledge_dirs or (
        os.path.join(PROJECT_ROOT, "knowledge"),
        os.path.join(PROJECT_ROOT, "documents"),
    )
    index_file = index_file or os.path.join(PROJECT_ROOT, "ai-session", "doc_index.json")

    def md5_of_file(path):
        h = hashlib.md5()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()

    def scan_docs():
        docs = {}
        for d in knowledge_dirs:
            if not os.path.isdir(d):
                continue
            for root, _, files in os.walk(d):
                for fn in files:
                    p = os.path.join(root, fn)
                    docs[p] = {"md5": md5_of_file(p), "mtime": os.path.getmtime(p)}
        return docs

    old_index = {}
    if os.path.exists(index_file):
        with open(index_file, "r", encoding="utf-8") as f:
            old_index = json.load(f)
    new_index = scan_docs()
    changed = [p for p, m in new_index.items() if p in old_index and old_index[p]["md5"] != m["md5"]]
    new_files = [p for p in new_index if p not in old_index]
    removed = [p for p in old_index if p not in new_index]

    status = "no_documents"
    if new_index:
        status = "updated" if (changed or new_files or removed) else "in_sync"

    os.makedirs(os.path.dirname(index_file), exist_ok=True)
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(new_index, f, ensure_ascii=False, indent=2)

    return {"status": status, "num_docs": len(new_index), "new_files": new_files,
             "changed_files": changed, "removed_files": removed}


# ---------------------------------------------------------------------------
# Hàm tổng hợp - AI Skill độc lập tái sử dụng
# ---------------------------------------------------------------------------
def run_stock_analysis_skill(ticker: str, period: str = "12mo", interval: str = "1d",
                              output_dir: str = None,
                              session_file: str = None,
                              candle_order: int = 5,
                              lookback: int = 5) -> dict:
    """
    Chạy toàn bộ pipeline phân tích kỹ thuật cho một mã cổ phiếu, trên khung
    thời gian NGÀY (Daily, interval="1d" mặc định):
    RAG sync -> tải dữ liệu -> kênh xu hướng -> chỉ báo -> mô hình nến ->
    hỗ trợ/kháng cự -> khuyến nghị -> vẽ biểu đồ -> mindmap -> lưu session.

    `lookback`: số phiên giao dịch gần nhất để quét mô hình nến Nhật
    (tham số của `detect_candlestick_patterns`), mặc định 5.

    Trả về dict chứa toàn bộ kết quả phân tích, sẵn sàng để dựng báo cáo.
    """
    output_dir = output_dir or os.path.join(PROJECT_ROOT, "output")
    session_file = session_file or os.path.join(PROJECT_ROOT, "ai-session", "agent_session.json")

    doc_sync = rag_sync_check()

    df = fetch_stock_data(ticker, period=period, interval=interval)
    df_ind = compute_indicators(df)
    channel = compute_trend_channel(df, order=candle_order)
    patterns = detect_candlestick_patterns(df_ind, lookback=lookback)
    sr = find_support_resistance(df, channel)
    rec = generate_recommendation(df_ind, channel, sr)
    chart_path = plot_chart(df_ind, channel, sr, patterns, ticker.split(".")[0], output_dir=output_dir, rec=rec)

    macro_state = "Thị trường chung ổn định (giả định theo dữ liệu giá quan sát)"
    mindmap = generate_mindmap(ticker, macro_state, channel, patterns, rec)

    log_recommendation(ticker, rec, chart_path=chart_path)

    session_state = load_session(session_file)
    session_state.setdefault("watchlist", {})
    session_state["watchlist"][ticker] = {
        "last_run": datetime.now(timezone.utc).isoformat(),
        "config": {"period": period, "interval": interval, "candle_order": candle_order, "lookback": lookback},
        "last_action": rec["action"],
        "last_close": rec["close"],
        "last_reasons": rec.get("reasons"),
    }
    session_state["last_ticker"] = ticker
    session_state["last_run_at"] = datetime.now(timezone.utc).isoformat()
    save_session(session_state, session_file)

    return {
        "ticker": ticker,
        "data": df_ind,
        "channel": channel,
        "patterns": patterns,
        "support_resistance": sr,
        "recommendation": rec,
        "chart_path": chart_path,
        "mindmap": mindmap,
        "doc_sync": doc_sync,
        "session_file": session_file,
    }


# ---------------------------------------------------------------------------
# Config đa mã cổ phiếu (dev/config_analysis.json) & chạy hàng loạt
# ---------------------------------------------------------------------------
DEFAULT_CONFIG_FILE = os.path.join(PROJECT_ROOT, "dev", "config_analysis.json")

DEFAULT_CONFIG = {
    "tickers": ["STB.VN"],
    "period": "12mo",
    "interval": "1d",
    "candle_order": 5,
    "lookback": 5,
    "output_dir": os.path.join(PROJECT_ROOT, "output"),
    "session_file": os.path.join(PROJECT_ROOT, "ai-session", "agent_session.json"),
}


def load_config(config_file: str = DEFAULT_CONFIG_FILE) -> dict:
    """
    Đọc cấu hình phân tích từ dev/config_analysis.json, cho phép khai báo NHIỀU mã cổ phiếu
    cùng lúc (key "tickers": [...]) cùng các tham số chung (period, interval,
    candle_order, lookback, output_dir, session_file). Khung thời gian mặc định là
    "1d" (Ngày) - có thể đổi sang "1wk" (Tuần) nếu cần, nhưng theo yêu cầu
    chuẩn của hệ thống, phân tích luôn dùng biểu đồ NGÀY.
    Nếu file không tồn tại, trả về cấu hình mặc định (chỉ phân tích STB.VN).
    """
    cfg = dict(DEFAULT_CONFIG)
    user_cfg = {}
    if os.path.exists(config_file):
        with open(config_file, "r", encoding="utf-8") as f:
            user_cfg = json.load(f)
        cfg.update(user_cfg)

    # Cho phép người dùng khai báo "ticker" (số ít) thay vì "tickers"
    if "ticker" in user_cfg and "tickers" not in user_cfg:
        cfg["tickers"] = [user_cfg["ticker"]]

    if isinstance(cfg.get("tickers"), str):
        cfg["tickers"] = [cfg["tickers"]]

    if not cfg.get("tickers"):
        cfg["tickers"] = DEFAULT_CONFIG["tickers"]

    if not cfg.get("interval"):
        cfg["interval"] = "1d"

    if not cfg.get("lookback"):
        cfg["lookback"] = DEFAULT_CONFIG["lookback"]

    # Chuẩn hóa đường dẫn tương đối (output_dir, session_file) về PROJECT_ROOT
    # để script chạy đúng dù được gọi từ thư mục gốc hay từ bên trong dev/
    for path_key in ("output_dir", "session_file"):
        val = cfg.get(path_key)
        if val and not os.path.isabs(val):
            cfg[path_key] = os.path.join(PROJECT_ROOT, val)

    return cfg


def run_batch_analysis(config_file: str = DEFAULT_CONFIG_FILE) -> dict:
    """
    Chạy phân tích kỹ thuật cho TẤT CẢ mã cổ phiếu khai báo trong dev/config_analysis.json,
    trên khung thời gian NGÀY (interval="1d" mặc định, có thể ghi đè trong config).
    Trả về dict: {"<ticker>": <kết quả run_stock_analysis_skill>, ...}
    kèm khóa "_errors" ghi nhận các mã lỗi (nếu có) để không làm gián đoạn cả lô.
    """
    cfg = load_config(config_file)
    results = {}
    errors = {}
    for ticker in cfg["tickers"]:
        try:
            results[ticker] = run_stock_analysis_skill(
                ticker,
                period=cfg.get("period", "12mo"),
                interval=cfg.get("interval", "1d"),
                output_dir=cfg.get("output_dir") or os.path.join(PROJECT_ROOT, "output"),
                session_file=cfg.get("session_file") or os.path.join(PROJECT_ROOT, "ai-session", "agent_session.json"),
                candle_order=cfg.get("candle_order", 5),
                lookback=cfg.get("lookback", 5),
            )
        except Exception as e:
            errors[ticker] = str(e)
    results["_errors"] = errors
    return results


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        # Chạy nhanh cho 1 mã chỉ định qua tham số dòng lệnh (khung Ngày mặc định)
        tk = sys.argv[1]
        result = run_stock_analysis_skill(tk)
        print(f"Phân tích hoàn tất cho {tk} (khung Ngày - Daily)")
        print("Khuyến nghị:", result["recommendation"]["action"])
        print("Biểu đồ lưu tại:", result["chart_path"])
    else:
        # Không có tham số -> đọc config_analysis.json để phân tích hàng loạt nhiều mã
        batch = run_batch_analysis()
        for tk, res in batch.items():
            if tk == "_errors":
                continue
            print(f"[{tk}] Khuyến nghị: {res['recommendation']['action']} | Biểu đồ: {res['chart_path']}")
        if batch.get("_errors"):
            print("Các mã lỗi:", batch["_errors"])

