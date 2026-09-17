#! /usr/bin/env python3

"""
analysis_script.py (Phiên bản Nâng cấp v2.0)
==============================================
Hệ thống Phân tích Kỹ thuật Định lượng & Nến Nhật Toàn diện:
Tích hợp tri thức từ 407 đồ thị thực chiến thị trường chứng khoán Việt Nam
và cẩm nang "Mô hình Nến Nhật" của Steve Nison.

Các cải tiến đột phá so với v1.0:
1. MỞ RỘNG MÔ HÌNH NẾN STEVE NISON:
   - Thêm Piercing Line (Xuyên thấu), Dark Cloud Cover (Mây đen bao phủ)
   - Thêm Hanging Man (Người treo cổ) vs Hammer (Nến búa)
   - Thêm Inverted Hammer (Búa ngược)
   - Thêm Tweezer Tops/Bottoms (Đỉnh/Đáy nhíp)
   - Thêm Windows (Khoảng trống giá - Gap Up / Gap Down)
   - Bổ sung chỉ số Khối lượng xác nhận (Volume Surge Confirmation > 1.3x SMA20)

2. BỔ SUNG CHỈ BÁO & DÒNG TIỀN NÂNG CAO (Theo chuẩn 407 đồ thị thực chiến):
   - MFI(14) - Money Flow Index (Chỉ số dòng tiền thông minh)
   - MA Cross (9, 26) - Bộ đôi trung bình phát hiện sớm giao cắt đảo chiều (Golden/Death Cross)
   - Volume SMA20 và đo lường xung lực cung/cầu

3. TỰ ĐỘNG NHẬN DIỆN VÙNG HỘP TÍCH LŨY (Auto Box Consolidation):
   - Quét thuật toán phát hiện vùng nén giá chặt chẽ (Orange Box)

4. KÊNH GIÁ ĐA TRỤC (Regression Channel với Median Line):
   - Vẽ đường trung trục (Median Line) đóng vai trò hỗ trợ/kháng cự động cấp 1

5. KHUNG QUẢN TRỊ RỦI RO ĐA KỊCH BẢN (Dual-Scenario Framework):
   - Target 1 (TP1 - Chốt lời từng phần tại Median Line / Cản gần)
   - Target 2 (TP2 - Chốt lời toàn phần tại Biên trên kênh / Cản cứng)
   - Khống chế Cắt lỗ (Stop Loss) nghiêm ngặt <= 7%
"""

import os
import json
import hashlib
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import yfinance as yf
from scipy.signal import argrelextrema

# Thiết lập thư mục gốc
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------------------
# 1. Thu thập dữ liệu OHLCV (Khung Ngày)
# ---------------------------------------------------------------------------
def fetch_stock_data(ticker: str, period: str = "12mo", interval: str = "1d") -> pd.DataFrame:
    """Tải dữ liệu OHLCV lịch sử theo NGÀY qua yfinance."""
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
# 2. Tính toán Chỉ báo Kỹ thuật Mở rộng (MA Cross 9/26, RSI, MFI, Bollinger)
# ---------------------------------------------------------------------------
def compute_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tính toán hệ thống chỉ báo kỹ thuật toàn diện:
    - MA9, MA26 (Tín hiệu giao cắt ngắn-trung hạn)
    - MA50, MA200 (Định hình xu hướng trung và dài hạn)
    - RSI(14) (Wilder's Smoothing)
    - MFI(14) (Money Flow Index - Dòng tiền tích lũy)
    - Bollinger Bands (20, 2)
    - Volume SMA20 & Tỷ lệ đột biến khối lượng
    """
    out = df.copy()

    # Đường trung bình động
    out["MA9"] = out["Close"].rolling(window=9).mean()
    out["MA26"] = out["Close"].rolling(window=26).mean()
    out["MA50"] = out["Close"].rolling(window=50).mean()
    out["MA200"] = out["Close"].rolling(window=200).mean()

    # Tín hiệu giao cắt MA9 và MA26 (Golden Cross / Death Cross)
    ma_cross = [None] * len(out)
    for i in range(1, len(out)):
        prev_9, prev_26 = out.iloc[i - 1]["MA9"], out.iloc[i - 1]["MA26"]
        curr_9, curr_26 = out.iloc[i]["MA9"], out.iloc[i]["MA26"]
        if pd.notna(prev_9) and pd.notna(prev_26) and pd.notna(curr_9) and pd.notna(curr_26):
            if prev_9 <= prev_26 and curr_9 > curr_26:
                ma_cross[i] = "GOLDEN_CROSS"
            elif prev_9 >= prev_26 and curr_9 < curr_26:
                ma_cross[i] = "DEATH_CROSS"
    out["MA_CROSS"] = ma_cross

    # RSI(14) - Wilder's smoothing
    delta = out["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / 14, min_periods=14, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / 14, min_periods=14, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    out["RSI14"] = 100 - (100 / (1 + rs))

    # MFI(14) - Money Flow Index (Chỉ số dòng tiền thông minh)
    typical_price = (out["High"] + out["Low"] + out["Close"]) / 3
    money_flow = typical_price * out["Volume"]
    tp_diff = typical_price.diff()

    pos_flow = np.where(tp_diff > 0, money_flow, 0.0)
    neg_flow = np.where(tp_diff < 0, money_flow, 0.0)

    pos_mf = pd.Series(pos_flow, index=out.index).rolling(window=14).sum()
    neg_mf = pd.Series(neg_flow, index=out.index).rolling(window=14).sum()

    mfr = pos_mf / neg_mf.replace(0, np.nan)
    out["MFI14"] = 100 - (100 / (1 + mfr))

    # Bollinger Bands (20, 2)
    bb_mid = out["Close"].rolling(window=20).mean()
    bb_std = out["Close"].rolling(window=20).std()
    out["BB_MID"] = bb_mid
    out["BB_UPPER"] = bb_mid + 2 * bb_std
    out["BB_LOWER"] = bb_mid - 2 * bb_std

    # Khối lượng SMA20 & Tỷ lệ đột biến
    out["VOL_SMA20"] = out["Volume"].rolling(window=20).mean()
    out["VOL_RATIO"] = out["Volume"] / out["VOL_SMA20"].replace(0, np.nan)

    return out


# ---------------------------------------------------------------------------
# 3. Kênh Xu hướng Toán học & Đường Trung trục (Median Line)
# ---------------------------------------------------------------------------
def compute_trend_channel(df: pd.DataFrame, order: int = 5) -> dict:
    """
    Xác định kênh xu hướng tuyến tính bằng argrelextrema + polyfit,
    đồng thời tính đường trung trục (Median Line).
    """
    highs = df["High"].values
    lows = df["Low"].values
    n = len(df)
    x = np.arange(n)

    peak_idx = argrelextrema(highs, np.greater_equal, order=order)[0]
    trough_idx = argrelextrema(lows, np.less_equal, order=order)[0]

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
        median_line = (upper_line + lower_line) / 2

        denom = max(abs(upper_slope), abs(lower_slope), 1e-9)
        slope_diff_ratio = abs(upper_slope - lower_slope) / denom
        is_parallel = slope_diff_ratio < 0.15

        avg_slope = (upper_slope + lower_slope) / 2
        avg_price = float(df["Close"].mean())
        slope_pct_per_bar = (avg_slope / avg_price) * 100 if avg_price else 0

        if abs(slope_pct_per_bar) < 0.03:
            channel_type = "Horizontal (Đi ngang / Tích lũy)"
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
            "median_line": median_line.tolist(),
            "is_parallel": bool(is_parallel),
            "slope_diff_ratio": float(slope_diff_ratio),
            "channel_type": channel_type if is_parallel else "Không tạo thành kênh song song",
            "valid": True,
        })
    else:
        result.update({
            "valid": False,
            "channel_type": "Không đủ đỉnh/đáy để thiết lập kênh giá",
        })

    return result


# ---------------------------------------------------------------------------
# 4. Tự động Nhận diện Hộp Tích lũy (Consolidation Box)
# ---------------------------------------------------------------------------
def detect_consolidation_boxes(df: pd.DataFrame, min_bars: int = 12, max_spread_pct: float = 8.0) -> list:
    """
    Tự động phát hiện các giai đoạn tích lũy đi ngang hình hộp (như hộp màu cam trong 407 chart tham chiếu).
    Điều kiện: Trong khoảng min_bars phiên, biên độ (Highest High - Lowest Low) / Lowest Low <= max_spread_pct.
    """
    boxes = []
    n = len(df)
    if n < min_bars:
        return boxes

    i = 0
    while i <= n - min_bars:
        window = df.iloc[i:i + min_bars]
        hh = float(window["High"].max())
        ll = float(window["Low"].min())
        spread = (hh - ll) / ll * 100 if ll else 999

        if spread <= max_spread_pct:
            # Mở rộng hộp về phía sau nếu biên độ vẫn được duy trì
            end_idx = i + min_bars
            while end_idx < n:
                next_row = df.iloc[end_idx]
                new_hh = max(hh, float(next_row["High"]))
                new_ll = min(ll, float(next_row["Low"]))
                new_spread = (new_hh - new_ll) / new_ll * 100 if new_ll else 999
                if new_spread <= max_spread_pct + 2.0:  # cho phép nới lỏng nhẹ 2%
                    hh, ll = new_hh, new_ll
                    end_idx += 1
                else:
                    break

            boxes.append({
                "start_idx": i,
                "end_idx": end_idx - 1,
                "start_date": str(df.iloc[i]["Date"].date()),
                "end_date": str(df.iloc[end_idx - 1]["Date"].date()),
                "top": hh,
                "bottom": ll,
                "spread_pct": round((hh - ll) / ll * 100, 2),
                "is_current": (end_idx - 1) >= (n - 3),
            })
            i = end_idx
        else:
            i += 2

    return boxes


# ---------------------------------------------------------------------------
# 5. Nhận diện Mẫu hình Nến Nhật Mở rộng (Steve Nison Full Library)
# ---------------------------------------------------------------------------
def _body(row):
    return abs(row["Close"] - row["Open"])


def _range(row):
    return row["High"] - row["Low"]


def _is_bullish(row):
    return row["Close"] > row["Open"]


def detect_candlestick_patterns_v2(df: pd.DataFrame, lookback: int = 8) -> list:
    """
    Nhận diện các mẫu hình nến Nhật đảo chiều kinh điển từ Steve Nison:
    - Doji, Hammer, Inverted Hammer, Shooting Star, Hanging Man
    - Bullish Engulfing, Bearish Engulfing
    - Piercing Line (Xuyên thấu) & Dark Cloud Cover (Mây đen bao phủ)
    - Tweezer Bottom (Đáy nhíp) & Tweezer Top (Đỉnh nhíp)
    - Windows (Gap Up / Gap Down)
    Kèm xác nhận khối lượng giao dịch đột biến (Volume Surge).
    """
    patterns = []
    n = len(df)
    start = max(2, n - lookback)

    for i in range(start, n):
        row = df.iloc[i]
        prev = df.iloc[i - 1]
        rng = _range(row)
        body = _body(row)
        prev_rng = _range(prev)
        prev_body = _body(prev)

        if rng == 0:
            continue

        upper_shadow = row["High"] - max(row["Close"], row["Open"])
        lower_shadow = min(row["Close"], row["Open"]) - row["Low"]
        body_ratio = body / rng

        vol_ratio = row.get("VOL_RATIO", 1.0)
        vol_surge = bool(pd.notna(vol_ratio) and vol_ratio >= 1.3)

        found = None
        meaning = None
        category = "Reversal"

        # 1. Doji
        if body_ratio < 0.10:
            found = "Doji"
            meaning = "Lưỡng lự tuyệt đối, cung cầu cân bằng sau nhịp biến động"
            category = "Indecision"

        # 2. Hammer (ở đáy) vs Hanging Man (ở đỉnh)
        elif lower_shadow >= 2 * body and upper_shadow <= body * 0.5 and body_ratio < 0.35:
            if not _is_bullish(prev):
                found = "Hammer (Nến búa)"
                meaning = "Từ chối giá thấp tại hỗ trợ, lực cầu bắt đáy xuất hiện mạnh"
                category = "Bullish Reversal"
            else:
                found = "Hanging Man (Người treo cổ)"
                meaning = "Bóng dưới dài xuất hiện tại đỉnh cảnh báo áp lực bán âm thầm gia tăng"
                category = "Bearish Reversal"

        # 3. Inverted Hammer (ở đáy) vs Shooting Star (ở đỉnh)
        elif upper_shadow >= 2 * body and lower_shadow <= body * 0.5 and body_ratio < 0.35:
            if _is_bullish(prev):
                found = "Shooting Star (Sao băng)"
                meaning = "Từ chối giá cao tại kháng cự, phe bán dội ngược phe mua"
                category = "Bearish Reversal"
            else:
                found = "Inverted Hammer (Búa ngược)"
                meaning = "Thử thách lực cầu tại đáy, tín hiệu nhen nhóm đảo chiều tăng"
                category = "Bullish Reversal"

        # 4. Bullish Engulfing
        elif (not _is_bullish(prev)) and _is_bullish(row) and \
                row["Close"] >= prev["Open"] and row["Open"] <= prev["Close"]:
            found = "Bullish Engulfing (Nhấn chìm tăng)"
            meaning = "Phe mua nuốt trọn toàn bộ thân nến giảm trước đó, xác nhận đảo chiều tăng"
            category = "Bullish Reversal"

        # 5. Bearish Engulfing
        elif _is_bullish(prev) and (not _is_bullish(row)) and \
                row["Open"] >= prev["Close"] and row["Close"] <= prev["Open"]:
            found = "Bearish Engulfing (Nhấn chìm giảm)"
            meaning = "Phe gấu nuốt trọn nỗ lực tăng phiên trước, cảnh báo bán tháo"
            category = "Bearish Reversal"

        # 6. Piercing Line (Đường xuyên thấu)
        elif (not _is_bullish(prev)) and _is_bullish(row) and \
                row["Open"] < prev["Low"] and row["Close"] > (prev["Open"] + prev["Close"]) / 2 and \
                row["Close"] < prev["Open"]:
            found = "Piercing Line (Xuyên thấu)"
            meaning = "Nến tăng mở cửa dưới đáy cũ nhưng đóng cửa vượt quá 50% thân nến trước"
            category = "Bullish Reversal"

        # 7. Dark Cloud Cover (Mây đen bao phủ)
        elif _is_bullish(prev) and (not _is_bullish(row)) and \
                row["Open"] > prev["High"] and row["Close"] < (prev["Open"] + prev["Close"]) / 2 and \
                row["Close"] > prev["Open"]:
            found = "Dark Cloud Cover (Mây đen bao phủ)"
            meaning = "Nến giảm mở cửa vượt đỉnh cũ nhưng đóng cửa chìm sâu dưới 50% thân nến trước"
            category = "Bearish Reversal"

        # 8. Tweezer Bottom (Đáy nhíp) & Tweezer Top (Đỉnh nhíp)
        if found is None:
            low_diff_pct = abs(row["Low"] - prev["Low"]) / prev["Low"] * 100 if prev["Low"] else 999
            high_diff_pct = abs(row["High"] - prev["High"]) / prev["High"] * 100 if prev["High"] else 999

            if low_diff_pct <= 0.3 and (not _is_bullish(prev)) and _is_bullish(row):
                found = "Tweezer Bottom (Đáy nhíp)"
                meaning = "Hai phiên liên tiếp kiểm định thành công cùng một mốc hỗ trợ thấp nhất"
                category = "Bullish Reversal"
            elif high_diff_pct <= 0.3 and _is_bullish(prev) and (not _is_bullish(row)):
                found = "Tweezer Top (Đỉnh nhíp)"
                meaning = "Hai phiên liên tiếp bị từ chối tại cùng một mức đỉnh kháng cự cao nhất"
                category = "Bearish Reversal"

        # 9. Windows / Gaps (Khoảng trống giá)
        if found is None:
            if row["Low"] > prev["High"]:
                found = "Rising Window (Gap Up)"
                meaning = f"Khoảng trống tăng giá [{prev['High']:.0f} - {row['Low']:.0f}], trở thành vùng hỗ trợ mạnh"
                category = "Continuation/Support"
            elif row["High"] < prev["Low"]:
                found = "Falling Window (Gap Down)"
                meaning = f"Khoảng trống giảm giá [{row['High']:.0f} - {prev['Low']:.0f}], trở thành vùng kháng cự mạnh"
                category = "Continuation/Resistance"

        # 10. Morning Star & Evening Star (cần 3 nến)
        if found is None and i >= 2:
            c1, c2, c3 = df.iloc[i - 2], df.iloc[i - 1], row
            c1_b = _body(c1)
            c2_b = _body(c2)
            if (not _is_bullish(c1)) and c2_b < c1_b * 0.4 and _is_bullish(c3) and \
                    c3["Close"] > (c1["Open"] + c1["Close"]) / 2:
                found = "Morning Star (Sao mai)"
                meaning = "Bộ 3 nến đảo chiều tăng mạnh: Giảm mạnh -> Cạn kiệt -> Tăng bùng nổ"
                category = "Bullish Reversal"
            elif _is_bullish(c1) and c2_b < c1_b * 0.4 and (not _is_bullish(c3)) and \
                    c3["Close"] < (c1["Open"] + c1["Close"]) / 2:
                found = "Evening Star (Sao hôm)"
                meaning = "Bộ 3 nến đảo chiều giảm mạnh: Tăng mạnh -> Lưỡng lự đỉnh -> Bán tháo"
                category = "Bearish Reversal"

        if found:
            patterns.append({
                "index": int(i),
                "date": str(df.iloc[i]["Date"].date()),
                "pattern": found,
                "meaning": meaning,
                "category": category,
                "vol_surge": vol_surge,
                "vol_ratio": round(float(vol_ratio), 2) if pd.notna(vol_ratio) else 1.0,
            })

    return patterns


# ---------------------------------------------------------------------------
# 6. Gom cụm Hỗ trợ / Kháng cự
# ---------------------------------------------------------------------------
def find_support_resistance(df: pd.DataFrame, channel: dict, tolerance_pct: float = 1.5) -> dict:
    """Gom cụm các đỉnh/đáy fractal thành vùng Hỗ trợ/Kháng cự then chốt."""
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

    resistance_zones = sorted(cluster([highs[i] for i in peak_idx], tolerance_pct), key=lambda x: -x["touches"])
    support_zones = sorted(cluster([lows[i] for i in trough_idx], tolerance_pct), key=lambda x: -x["touches"])

    return {
        "support_zones": support_zones[:5],
        "resistance_zones": resistance_zones[:5],
        "strongest_support": support_zones[0] if support_zones else None,
        "strongest_resistance": resistance_zones[0] if resistance_zones else None,
    }


# ---------------------------------------------------------------------------
# 7. Khung Quản trị Rủi ro & Khuyến nghị Đa Kịch bản (Dual-Scenario)
# ---------------------------------------------------------------------------
def generate_recommendation_v2(df_ind: pd.DataFrame, channel: dict, sr: dict, boxes: list, patterns: list) -> dict:
    """
    Bộ quy tắc ra quyết định kỷ luật v2.0 kết hợp MFI, MA Cross, Hộp tích lũy và Kênh giá:
    - Kịch bản mục tiêu kép: TP1 (Median Line / Cản gần) & TP2 (Biên trên kênh / Cản cứng).
    - Tỷ lệ R:R tính toán cho từng mục tiêu (Yêu cầu TP2 đạt R:R >= 2.0).
    - Cắt lỗ nghiêm ngặt không quá 7%.
    """
    last = df_ind.iloc[-1]
    close = float(last["Close"])
    ma200 = last["MA200"]
    rsi = float(last["RSI14"]) if pd.notna(last["RSI14"]) else None
    mfi = float(last["MFI14"]) if pd.notna(last["MFI14"]) else None
    vol_ratio = float(last["VOL_RATIO"]) if pd.notna(last["VOL_RATIO"]) else 1.0

    long_term_trend = "Không xác định (thiếu MA200)"
    above_ma200 = None
    if pd.notna(ma200):
        above_ma200 = bool(close > ma200)
        long_term_trend = "Tăng (Bull Market)" if above_ma200 else "Giảm (Bear Market)"

    channel_valid = channel.get("valid", False)
    lower_edge = channel["lower_line"][-1] if channel_valid else None
    upper_edge = channel["upper_line"][-1] if channel_valid else None
    median_edge = channel.get("median_line", [None])[-1] if channel_valid else None

    # Kiểm tra vị thế giá
    near_lower_channel = False
    if channel_valid and lower_edge:
        near_lower_channel = abs(close - lower_edge) / lower_edge * 100 <= 3.5

    near_support = False
    support_level = sr.get("strongest_support", {}).get("level") if sr.get("strongest_support") else None
    if support_level:
        near_support = abs(close - support_level) / support_level * 100 <= 3.5

    # Kiểm tra đang trong hộp tích lũy
    in_box = False
    current_box = None
    for b in boxes:
        if b.get("is_current") and b["bottom"] * 0.98 <= close <= b["top"] * 1.02:
            in_box = True
            current_box = b
            break

    # Phát hiện mẫu nến đảo chiều tăng gần nhất
    recent_bullish_pattern = None
    for p in reversed(patterns[-3:] if patterns else []):
        if "Bullish" in p.get("category", "") or "Hammer" in p.get("pattern", "") or "Piercing" in p.get("pattern", ""):
            recent_bullish_pattern = p
            break

    # Điều kiện MUA
    buy_condition = (
        above_ma200 is True and
        (near_support or near_lower_channel or (in_box and close <= current_box["bottom"] * 1.03)) and
        (rsi is not None and rsi < 65) and
        (mfi is None or mfi < 70)
    )

    action = "THEO DÕI"
    reasons = []
    entry_zone = tp1 = tp2 = sl = rr1 = rr2 = None

    if buy_condition:
        entry_low = close * 0.99
        entry_high = close * 1.01

        # Cắt lỗ đặt dưới hỗ trợ hoặc dưới kênh 2%, khống chế tối đa 7%
        sl_base = lower_edge * 0.98 if lower_edge else close * 0.95
        if support_level:
            sl_base = min(sl_base, support_level * 0.98)
        sl_candidate = min(sl_base, close * 0.98)

        # Áp trần cắt lỗ 7%
        if (close - sl_candidate) / close * 100 > 7.0:
            sl_candidate = close * 0.93

        # Mục tiêu 1 (TP1): Đường Median hoặc biên trên hộp
        tp1_candidate = median_edge if (median_edge and median_edge > close) else close * 1.08
        if in_box and current_box["top"] > close:
            tp1_candidate = min(tp1_candidate, current_box["top"])

        # Mục tiêu 2 (TP2): Cạnh trên kênh hoặc kháng cự mạnh
        tp2_candidate = upper_edge if (upper_edge and upper_edge > close) else close * 1.15
        if sr.get("strongest_resistance") and sr["strongest_resistance"]["level"] > close:
            tp2_candidate = max(tp2_candidate, sr["strongest_resistance"]["level"])

        risk = close - sl_candidate
        reward1 = tp1_candidate - close
        reward2 = tp2_candidate - close

        rr1 = round(reward1 / risk, 2) if risk > 0 else 0
        rr2 = round(reward2 / risk, 2) if risk > 0 else 0

        if rr2 >= 2.0:
            action = "MUA"
            entry_zone = (round(entry_low), round(entry_high))
            tp1 = round(tp1_candidate)
            tp2 = round(tp2_candidate)
            sl = round(sl_candidate)
            reasons.append("Giá nằm trên MA200 - Xu hướng tăng dài hạn được xác nhận")
            reasons.append("Giá pullback kiểm định thành công vùng hỗ trợ / cạnh dưới kênh")
            if recent_bullish_pattern:
                reasons.append(f"Mô hình nến xác nhận: {recent_bullish_pattern['pattern']}")
            if mfi and mfi < 40:
                reasons.append(f"Dòng tiền MFI={mfi:.1f} ở vùng tích lũy an toàn")
            reasons.append(f"Tỷ lệ R:R mục tiêu 2 đạt 1:{rr2} (vượt ngưỡng chuẩn 1:2)")
        else:
            action = "THEO DÕI"
            reasons.append(f"Đủ điều kiện kỹ thuật nhưng khoảng cách cản hẹp khiến R:R ({rr2}) chưa đạt tối thiểu 1:2")
    else:
        if above_ma200 is False:
            action = "BÁN"
            reasons.append("Giá nằm dưới MA200 - Rủi ro xu hướng giảm dài hạn (Bear Market)")
        elif rsi and rsi >= 65:
            action = "THEO DÕI"
            reasons.append(f"Chỉ số RSI={rsi:.1f} tiệm cận/vượt quá mua, rủi ro mua đuổi đỉnh")
        elif mfi and mfi >= 75:
            action = "THEO DÕI"
            reasons.append(f"Dòng tiền MFI={mfi:.1f} đã rơi vào vùng quá mua ngắn hạn")
        else:
            action = "THEO DÕI"
            reasons.append("Giá đang lơ lửng giữa kênh, chưa có điểm tựa hỗ trợ tỷ lệ R:R tối ưu")

    return {
        "action": action,
        "close": close,
        "long_term_trend": long_term_trend,
        "rsi": rsi,
        "mfi": mfi,
        "vol_ratio": round(vol_ratio, 2),
        "channel_type": channel.get("channel_type"),
        "in_box": in_box,
        "current_box": current_box,
        "entry_zone": entry_zone,
        "tp1": tp1,
        "tp2": tp2,
        "stop_loss": sl,
        "risk_reward_tp1": rr1,
        "risk_reward_tp2": rr2,
        "reasons": reasons,
    }


# ---------------------------------------------------------------------------
# 8. Vẽ Biểu đồ Nâng cao (3 Bảng: Giá/Kênh/Nến + Volume + MFI/RSI)
# ---------------------------------------------------------------------------
def plot_advanced_chart(df_ind: pd.DataFrame, channel: dict, sr: dict, boxes: list,
                        patterns: list, ticker: str, output_dir: str = "output",
                        rec: dict = None) -> str:
    """
    Xuất đồ thị nến kỹ thuật chuyên nghiệp 3 bảng con (Subplots) tương tự TradingView:
    - Bảng 1 (Chính): Nến Nhật, Kênh giá, Median Line, Hộp cam, MA9/26/50/200, Annotations nến, Badge khuyến nghị.
    - Bảng 2: Khối lượng giao dịch + MA20 Volume.
    - Bảng 3: Chỉ số RSI(14) và MFI(14) với các vùng 30/70.
    """
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
    import matplotlib.dates as mdates

    os.makedirs(output_dir, exist_ok=True)
    n = len(df_ind)
    x = np.arange(n)

    fig, (ax1, ax2, ax3) = plt.subplots(
        3, 1, figsize=(15, 10),
        gridspec_kw={"height_ratios": [5, 1.5, 1.5]},
        sharex=True
    )
    plt.subplots_adjust(hspace=0.05)

    # --- Bảng 1: Biểu đồ nến & Kênh giá ---
    up = df_ind["Close"] >= df_ind["Open"]
    down = ~up

    # Vẽ bóng nến
    ax1.vlines(x, df_ind["Low"], df_ind["High"], color="black", linewidth=0.8, alpha=0.7)
    # Vẽ thân nến
    width = 0.6
    ax1.bar(x[up], (df_ind["Close"] - df_ind["Open"])[up], bottom=df_ind["Open"][up],
            color="#26a69a", width=width, edgecolor="black", linewidth=0.5)
    ax1.bar(x[down], (df_ind["Open"] - df_ind["Close"])[down], bottom=df_ind["Close"][down],
            color="#ef5350", width=width, edgecolor="black", linewidth=0.5)

    # Đường trung bình MA
    ax1.plot(x, df_ind["MA9"], color="cyan", linewidth=1.0, label="MA9")
    ax1.plot(x, df_ind["MA26"], color="magenta", linewidth=1.0, label="MA26")
    ax1.plot(x, df_ind["MA50"], color="orange", linewidth=1.2, label="MA50")
    if "MA200" in df_ind.columns and df_ind["MA200"].notna().any():
        ax1.plot(x, df_ind["MA200"], color="purple", linewidth=1.5, label="MA200 (Baseline)")

    # Kênh giá
    if channel.get("valid"):
        u_line = np.array(channel["upper_line"])
        l_line = np.array(channel["lower_line"])
        m_line = np.array(channel.get("median_line", []))
        ax1.plot(x, u_line, color="red", linestyle="--", linewidth=1.3, label="Biên trên kênh (Resistance)")
        ax1.plot(x, l_line, color="green", linestyle="--", linewidth=1.3, label="Biên dưới kênh (Support)")
        if len(m_line) == n:
            ax1.plot(x, m_line, color="blue", linestyle=":", linewidth=1.0, alpha=0.8, label="Median Line")
        # Tô bóng vùng kênh
        ax1.fill_between(x, l_line, u_line, color="purple", alpha=0.06)

    # Vẽ hộp tích lũy màu cam (Orange Box Consolidation)
    for b in boxes:
        s_idx = b["start_idx"]
        e_idx = b["end_idx"]
        w = e_idx - s_idx + 1
        h = b["top"] - b["bottom"]
        rect = Rectangle(
            (s_idx - 0.4, b["bottom"]), w, h,
            linewidth=1.2, edgecolor="darkorange", facecolor="orange", alpha=0.2, zorder=2
        )
        ax1.add_patch(rect)
        ax1.text(
            s_idx, b["top"] * 1.005, f"Tích lũy ({b['spread_pct']}%)",
            fontsize=8, color="darkorange", fontweight="bold"
        )

    # Hỗ trợ / Kháng cự ngang
    for sup in sr.get("support_zones", [])[:2]:
        ax1.axhline(y=sup["level"], color="darkblue", linestyle="-", linewidth=1.2, alpha=0.85)
    for res in sr.get("resistance_zones", [])[:2]:
        ax1.axhline(y=res["level"], color="darkred", linestyle="-", linewidth=1.2, alpha=0.85)

    # Chú thích mô hình nến Nhật (chỉ lấy tối đa 4 mẫu hình gần nhất và so le độ cao để tránh đè chữ)
    display_patterns = patterns[-4:] if len(patterns) > 4 else patterns
    for idx_p, p in enumerate(display_patterns):
        idx = p["index"]
        if 0 <= idx < n:
            y = float(df_ind.iloc[idx]["High"]) * 1.01
            star_vol = " ★" if p.get("vol_surge") else ""
            y_offset = y * (1.03 if (idx_p % 2 == 0) else 1.055)
            ax1.annotate(
                p["pattern"].split(" (")[0] + star_vol,
                xy=(idx, y),
                xytext=(idx, y_offset),
                fontsize=7.5,
                fontweight="bold",
                color="black",
                arrowprops=dict(arrowstyle="->", color="black", lw=0.9),
                ha="center",
            )

    # Badge khuyến nghị ở góc trái
    if rec:
        action = rec.get("action", "THEO DÕI")
        colors = {"MUA": "darkgreen", "BÁN": "red", "THEO DÕI": "#fbc02d"}
        text_color = "black" if action == "THEO DÕI" else "white"
        label = f"KHUYẾN NGHỊ: {action}"
        if rec.get("reasons"):
            label += "\n" + "\n".join(f"- {r}" for r in rec["reasons"][:3])
        if action == "MUA":
            label += f"\n• Vùng mua: {rec['entry_zone'][0]:,} - {rec['entry_zone'][1]:,}"
            label += f"\n• TP1: {rec['tp1']:,} (R:R 1:{rec['risk_reward_tp1']}) | TP2: {rec['tp2']:,} (R:R 1:{rec['risk_reward_tp2']})"
            label += f"\n• Cắt lỗ: {rec['stop_loss']:,}"

        ax1.text(
            0.01, 0.98, label, transform=ax1.transAxes,
            fontsize=8.5, fontweight="bold", color=text_color, va="top", ha="left",
            bbox=dict(boxstyle="round,pad=0.5", facecolor=colors.get(action, "gray"), edgecolor="black", alpha=0.92)
        )

    clean_tk = ticker.split(".")[0]
    ax1.set_title(f"{clean_tk} - Phân tích Kỹ thuật Định lượng, Kênh Xu hướng & Nến Nhật (v2.0)", fontsize=13, fontweight="bold")
    ax1.legend(loc="upper right", fontsize=8, ncol=2)
    ax1.grid(True, linestyle="--", alpha=0.4)
    ax1.set_ylabel("Giá (VNĐ)", fontsize=10)

    # --- Bảng 2: Khối lượng giao dịch (Volume) ---
    vol_colors = ["#26a69a" if c else "#ef5350" for c in up]
    ax2.bar(x, df_ind["Volume"], color=vol_colors, width=0.6, alpha=0.8)
    if "VOL_SMA20" in df_ind.columns:
        ax2.plot(x, df_ind["VOL_SMA20"], color="blue", linewidth=1.0, label="SMA20 Vol")
    ax2.set_ylabel("Khối lượng", fontsize=9)
    ax2.grid(True, linestyle="--", alpha=0.3)
    ax2.legend(loc="upper left", fontsize=8)

    # --- Bảng 3: Chỉ báo RSI & MFI ---
    if "RSI14" in df_ind.columns:
        ax3.plot(x, df_ind["RSI14"], color="purple", linewidth=1.2, label="RSI(14)")
    if "MFI14" in df_ind.columns:
        ax3.plot(x, df_ind["MFI14"], color="teal", linewidth=1.2, label="MFI(14) Dòng tiền")
    ax3.axhline(y=70, color="red", linestyle=":", linewidth=0.9, alpha=0.8)
    ax3.axhline(y=30, color="green", linestyle=":", linewidth=0.9, alpha=0.8)
    ax3.axhline(y=50, color="gray", linestyle="-", linewidth=0.5, alpha=0.5)
    ax3.fill_between(x, 30, 70, color="purple", alpha=0.04)
    ax3.set_ylim(0, 100)
    ax3.set_ylabel("RSI & MFI", fontsize=9)
    ax3.grid(True, linestyle="--", alpha=0.3)
    ax3.legend(loc="upper left", fontsize=8)

    # --- Bảng 1: Mũi tên dự báo xu hướng tương lai (Forecast Arrow) ---
    future_bars = 10
    ax1.set_xlim(-1, n + future_bars)
    curr_x = n - 1
    curr_y = float(df_ind.iloc[-1]["Close"])
    action = rec.get("action", "THEO DÕI") if rec else "THEO DÕI"

    if action == "MUA":
        # Mũi tên xanh lá cây hướng lên mục tiêu TP2 hoặc TP1
        target_y = rec.get("tp2") or (channel["upper_line"][-1] if channel.get("valid") else curr_y * 1.12)
        target_x = curr_x + 8
        ax1.annotate(
            "",
            xy=(target_x, target_y),
            xytext=(curr_x, curr_y),
            arrowprops=dict(
                facecolor="#00e676",
                edgecolor="#004d40",
                arrowstyle="-|>",
                mutation_scale=22,
                linewidth=2.5,
            ),
            zorder=8,
        )
        ax1.text(
            target_x, target_y * 1.012, f"Dự báo Sóng TĂNG\nTarget: {target_y:,.0f}",
            fontsize=8.5, fontweight="bold", color="#00796b", ha="center", va="bottom",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="#e8f5e9", edgecolor="#00e676", alpha=0.92),
            zorder=9,
        )
    elif action == "BÁN":
        # Mũi tên đỏ hướng xuống tìm hỗ trợ mới
        target_y = sr.get("strongest_support", {}).get("level", curr_y * 0.90) if sr.get("strongest_support") else curr_y * 0.90
        if target_y >= curr_y:
            target_y = curr_y * 0.90
        target_x = curr_x + 8
        ax1.annotate(
            "",
            xy=(target_x, target_y),
            xytext=(curr_x, curr_y),
            arrowprops=dict(
                facecolor="#ff1744",
                edgecolor="#b71c1c",
                arrowstyle="-|>",
                mutation_scale=22,
                linewidth=2.5,
            ),
            zorder=8,
        )
        ax1.text(
            target_x, target_y * 0.988, f"Dự báo GIẢM\nHỗ trợ: {target_y:,.0f}",
            fontsize=8.5, fontweight="bold", color="#c62828", ha="center", va="top",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="#ffebee", edgecolor="#ff1744", alpha=0.92),
            zorder=9,
        )
    else:  # THEO DÕI
        # Xác định cận trên và cận dưới vùng dao động
        upper_target = None
        if rec and rec.get("current_box"):
            upper_target = rec["current_box"]["top"]
        elif channel.get("valid"):
            upper_target = channel.get("median_line", [curr_y * 1.05])[-1]
        elif sr.get("strongest_resistance"):
            upper_target = sr["strongest_resistance"]["level"]
        if not upper_target or upper_target <= curr_y:
            upper_target = curr_y * 1.06

        lower_target = None
        if rec and rec.get("current_box"):
            lower_target = rec["current_box"]["bottom"]
        elif sr.get("strongest_support"):
            lower_target = sr["strongest_support"]["level"]
        elif channel.get("valid"):
            lower_target = channel["lower_line"][-1]
        if not lower_target or lower_target >= curr_y:
            lower_target = curr_y * 0.94

        mid_val = (upper_target + lower_target) / 2
        target_x = curr_x + 7

        if curr_y <= mid_val:
            # Giá ở vùng hỗ trợ / đáy hộp -> Mũi tên xanh lá cây hướng lên cản gần (Swing hồi)
            ax1.annotate(
                "",
                xy=(target_x, upper_target),
                xytext=(curr_x, curr_y),
                arrowprops=dict(
                    facecolor="#00e676",
                    edgecolor="#1b5e20",
                    arrowstyle="-|>",
                    mutation_scale=20,
                    linewidth=2.2,
                ),
                zorder=8,
            )
            ax1.text(
                target_x, upper_target * 1.012, f"Dự báo Sóng Hồi\nCản: {upper_target:,.0f}",
                fontsize=8, fontweight="bold", color="#1b5e20", ha="center", va="bottom",
                bbox=dict(boxstyle="round,pad=0.25", facecolor="#e8f5e9", edgecolor="#66bb6a", alpha=0.92),
                zorder=9,
            )
        else:
            # Giá ở vùng cản -> Mũi tên cam hướng xuống retest hỗ trợ
            ax1.annotate(
                "",
                xy=(target_x, lower_target),
                xytext=(curr_x, curr_y),
                arrowprops=dict(
                    facecolor="#ff9100",
                    edgecolor="#e65100",
                    arrowstyle="-|>",
                    mutation_scale=20,
                    linewidth=2.2,
                ),
                zorder=8,
            )
            ax1.text(
                target_x, lower_target * 0.988, f"Dự báo Chỉnh Test Cầu\nHỗ trợ: {lower_target:,.0f}",
                fontsize=8, fontweight="bold", color="#bf360c", ha="center", va="top",
                bbox=dict(boxstyle="round,pad=0.25", facecolor="#fff3e0", edgecolor="#ffa726", alpha=0.92),
                zorder=9,
            )

    # Định dạng trục hoành ngày tháng
    step = max(1, n // 10)
    tick_indices = list(range(0, n, step))
    if tick_indices[-1] != n - 1:
        tick_indices.append(n - 1)
    ax3.set_xticks(tick_indices)
    ax3.set_xticklabels([str(df_ind.iloc[i]["Date"].date()) for i in tick_indices], rotation=25, ha="right", fontsize=9)

    # Xác định ngày theo nến cuối cùng (hoặc ngày hiện tại)
    if "Date" in df_ind.columns and len(df_ind) > 0:
        dt_val = pd.to_datetime(df_ind.iloc[-1]["Date"])
        date_str = dt_val.strftime("%d-%m-%Y")
    else:
        date_str = datetime.now().strftime("%d-%m-%Y")

    # Xác định action slug không dấu
    action_raw = rec.get("action", "THEO DÕI") if rec else "THEO DÕI"
    if "MUA" in action_raw.upper():
        action_slug = "MUA"
    elif "BÁN" in action_raw.upper() or "BAN" in action_raw.upper():
        action_slug = "BAN"
    else:
        action_slug = "THEO-DOI"

    filename = f"V2-{clean_tk}-{date_str}-{action_slug}.png"
    out_path = os.path.join(output_dir, filename)
    fig.savefig(out_path, dpi=160, bbox_inches="tight")
    plt.close(fig)
    return out_path


# ---------------------------------------------------------------------------
# 9. Sinh Sơ đồ Tư duy Mermaid.js Nâng cao
# ---------------------------------------------------------------------------
def generate_advanced_mindmap(ticker: str, channel: dict, boxes: list, patterns: list, rec: dict) -> str:
    """Tạo sơ đồ tư duy Mermaid.js đa tầng."""
    clean_tk = ticker.split(".")[0]
    box_str = f"Hộp tích lũy: {boxes[-1]['spread_pct']}%" if boxes else "Không trong hộp tích lũy"

    pattern_nodes = []
    pattern_edges = []
    recent_p = patterns[-3:] if patterns else []
    if recent_p:
        for i, p in enumerate(recent_p):
            nid = f"P{i}"
            star = " (Vol cao)" if p.get("vol_surge") else ""
            pattern_nodes.append(f'        {nid}["{p["pattern"]}{star}"]')
            pattern_edges.append(f"    Channel --> {nid}")
        last_node = f"P{len(recent_p) - 1}"
    else:
        pattern_nodes.append('        P0["Không có mô hình nến đảo chiều"]')
        pattern_edges.append("    Channel --> P0")
        last_node = "P0"

    p_lines = "\n".join(pattern_nodes)
    e_lines = "\n".join(pattern_edges)

    mindmap = f"""graph TD
    Root["Cổ phiếu: {clean_tk}"] --> Macro["Xu hướng MA200: {rec['long_term_trend']}"]
    Macro --> Channel["Cấu trúc: {channel.get('channel_type')}"]
    Channel --> Box["Trạng thái nén: {box_str}"]
{p_lines}
{e_lines}
    {last_node} --> Action["Khuyến nghị: {rec['action']}"]
    Action --> Target["TP1: {rec.get('tp1') or 'N/A'} | TP2: {rec.get('tp2') or 'N/A'}"]
    Action --> Stop["Cắt lỗ: {rec.get('stop_loss') or 'N/A'}"]
"""
    return mindmap


# ---------------------------------------------------------------------------
# 10. Pipeline Thực thi Hoàn chỉnh & Quản lý Session
# ---------------------------------------------------------------------------
def run_stock_analysis_skill(ticker: str, period: str = "12mo", interval: str = "1d",
                              output_dir: str = None, session_file: str = None,
                              candle_order: int = 5, lookback: int = 8) -> dict:
    """Chạy toàn bộ pipeline phân tích kỹ thuật v2.0 cho một mã cổ phiếu."""
    output_dir = output_dir or os.path.join(PROJECT_ROOT, "output")
    session_file = session_file or os.path.join(PROJECT_ROOT, "ai-session", "agent_session.json")

    # 1. Tải dữ liệu & tính chỉ báo
    df = fetch_stock_data(ticker, period=period, interval=interval)
    df_ind = compute_indicators(df)

    # 2. Kênh giá & Hộp tích lũy
    channel = compute_trend_channel(df, order=candle_order)
    boxes = detect_consolidation_boxes(df)

    # 3. Nến Nhật Steve Nison mở rộng
    patterns = detect_candlestick_patterns_v2(df_ind, lookback=lookback)

    # 4. Hỗ trợ / Kháng cự & Khuyến nghị mục tiêu kép
    sr = find_support_resistance(df, channel)
    rec = generate_recommendation_v2(df_ind, channel, sr, boxes, patterns)

    # 5. Xuất biểu đồ 3 bảng con
    chart_path = plot_advanced_chart(df_ind, channel, sr, boxes, patterns, ticker, output_dir=output_dir, rec=rec)

    # 6. Sơ đồ tư duy & Ghi log
    mindmap = generate_advanced_mindmap(ticker, channel, boxes, patterns, rec)

    # Cập nhật session
    if os.path.exists(session_file):
        with open(session_file, "r", encoding="utf-8") as f:
            session_state = json.load(f)
    else:
        session_state = {}

    session_state.setdefault("watchlist", {})
    session_state["watchlist"][ticker] = {
        "last_run": datetime.now(timezone.utc).isoformat(),
        "config": {"period": period, "interval": interval, "candle_order": candle_order, "lookback": lookback},
        "last_action": rec["action"],
        "last_close": rec["close"],
        "tp1": rec.get("tp1"),
        "tp2": rec.get("tp2"),
        "stop_loss": rec.get("stop_loss"),
        "last_reasons": rec.get("reasons"),
    }
    session_state["last_ticker"] = ticker
    session_state["last_run_at"] = datetime.now(timezone.utc).isoformat()

    with open(session_file, "w", encoding="utf-8") as f:
        json.dump(session_state, f, ensure_ascii=False, indent=2)

    return {
        "ticker": ticker,
        "data": df_ind,
        "channel": channel,
        "boxes": boxes,
        "patterns": patterns,
        "support_resistance": sr,
        "recommendation": rec,
        "chart_path": chart_path,
        "mindmap": mindmap,
    }


def run_batch_analysis(config_file: str = None) -> dict:
    """Chạy phân tích hàng loạt theo dev/config_analysis.json."""
    config_file = config_file or os.path.join(PROJECT_ROOT, "dev", "config_analysis.json")
    if os.path.exists(config_file):
        with open(config_file, "r", encoding="utf-8") as f:
            cfg = json.load(f)
    else:
        cfg = {"tickers": ["STB.VN"]}

    tickers = cfg.get("tickers", ["STB.VN"])
    if isinstance(tickers, str):
        tickers = [tickers]

    results = {}
    errors = {}
    for tk in tickers:
        try:
            results[tk] = run_stock_analysis_skill(
                tk,
                period=cfg.get("period", "12mo"),
                interval=cfg.get("interval", "1d"),
                candle_order=cfg.get("candle_order", 5),
                lookback=cfg.get("lookback", 8)
            )
        except Exception as e:
            errors[tk] = str(e)
    results["_errors"] = errors
    return results


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        tk = sys.argv[1]
        res = run_stock_analysis_skill(tk)
        print(f"=== PHÂN TÍCH NÂNG CAO V2.0 CHO {tk} ===")
        print(f"Hành động: {res['recommendation']['action']}")
        print(f"Lý do: {'; '.join(res['recommendation']['reasons'])}")
        if res['recommendation']['action'] == 'MUA':
            print(f"Vùng mua: {res['recommendation']['entry_zone']}")
            print(f"TP1 (Median): {res['recommendation']['tp1']} | TP2 (Upper): {res['recommendation']['tp2']}")
            print(f"Cắt lỗ: {res['recommendation']['stop_loss']}")
        print(f"Biểu đồ đã lưu tại: {res['chart_path']}")
    else:
        batch = run_batch_analysis()
        for tk, res in batch.items():
            if tk == "_errors":
                continue
            print(f"[{tk}] Khuyến nghị: {res['recommendation']['action']} | Biểu đồ: {res['chart_path']}")
        if batch.get("_errors"):
            print("Các mã lỗi:", batch["_errors"])
