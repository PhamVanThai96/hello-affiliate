#!/usr/bin/env python3
"""Tạo bảng hiệu chuẩn xác suất cho outlook_v3 từ lịch sử yfinance.

  python3 dev/calibrate_outlook.py --out dev/outlook_calibration.json                       # bản dùng thật (mọi năm)
  python3 dev/calibrate_outlook.py --end-year 2019 --exclude MSN.VN VRE.VN HPG.VN --out /tmp/calib_oos.json   # bản hiệu chuẩn chỉ dùng dữ liệu đến 2019, loại 3 mã (để kiểm chứng ngoài mẫu)
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import outlook_v3 as o3  # noqa: E402

TRAIN_TICKERS = ["VNM.VN", "FPT.VN", "MWG.VN", "STB.VN", "VCB.VN", "SSI.VN", "PNJ.VN",
                 "VIC.VN", "VHM.VN", "TCB.VN", "ACB.VN", "MBB.VN", "MSN.VN", "VRE.VN", "HPG.VN"]

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--end-year", type=int, default=None)
    ap.add_argument("--exclude", nargs="*", default=[])
    ap.add_argument("--out", default=o3.CALIB_FILE)
    a = ap.parse_args()
    proxy = o3.market_proxy()
    hist = {}
    for tk in TRAIN_TICKERS:
        if tk in a.exclude:
            continue
        try:
            hist[tk] = o3._load_close(tk)
        except Exception as e:  # noqa: BLE001
            print("bỏ qua", tk, e)
    cal = o3.build_calibration(hist, proxy, end_year=a.end_year)
    cal["tickers"] = sorted(hist)
    json.dump(cal, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("n_total", cal["n_total"], "base_p_up", cal["base_p_up"], "cone_k80", cal["cone_k80"], "->", a.out)
    for k, v in sorted(cal["table"].items()):
        print(k, v)
