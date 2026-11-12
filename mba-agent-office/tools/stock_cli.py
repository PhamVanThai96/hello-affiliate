#!/usr/bin/env python3
"""
stock_cli.py - Cầu nối để agent Investor gọi công cụ phân tích kỹ thuật `stock-analysist` (thư mục anh em của mba-agent-office).

  python3 tools/stock_cli.py MSN.VN                      # JSON phân tích + vẽ biểu đồ (đường dẫn ảnh trong trường chart_path)
  python3 tools/stock_cli.py HPG.VN --no-chart
  python3 tools/stock_cli.py MSN.VN --fundamentals       # snapshot cơ bản yfinance cho định giá (giá, số cổ phiếu, P/E, P/B, EPS, BVPS, beta, nợ, thiểu số)
  python3 tools/stock_cli.py VRE.VN --as-of 2025-05-29   # kiểm tra lại tại một ngày trong quá khứ
  python3 tools/stock_cli.py --setup                     # tạo .venv + cài thư viện cho stock-analysist (cần Internet)

Biến môi trường: STOCK_ANALYSIS_DIR (mặc định ../stock-analysist), STOCK_ANALYSIS_PY (mặc định <dir>/.venv/bin/python).
"""
import os
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.abspath(os.environ.get("STOCK_ANALYSIS_DIR") or os.path.join(HERE, "..", "..", "stock-analysist"))
# Ảnh biểu đồ + file phiên chỉ là trung gian: để ở thư mục tạm (KHÔNG vào reports/) để báo cáo nhúng ảnh vào đúng 1 file HTML.
OUT = os.environ.get("STOCK_ANALYSIS_OUT") or os.path.join(tempfile.gettempdir(), "mba-stock-charts")


def python_exe():
    cand = os.environ.get("STOCK_ANALYSIS_PY") or os.path.join(DIR, ".venv", "bin", "python")
    return cand if os.path.exists(cand) else sys.executable


if __name__ == "__main__":
    if not os.path.isdir(os.path.join(DIR, "dev")):
        sys.exit(f"Không thấy thư mục công cụ: {DIR} (đặt STOCK_ANALYSIS_DIR).")
    if "--setup" in sys.argv:
        venv = os.path.join(DIR, ".venv")
        subprocess.check_call([sys.executable, "-m", "venv", venv])
        subprocess.check_call([os.path.join(venv, "bin", "pip"), "install", "-q", "yfinance>=0.2.36", "pandas>=2.0,<3.0", "numpy>=1.26,<2.0",
                               "scipy", "matplotlib", "mplfinance", "tabulate", "requests", "six"])
        print("Đã tạo", venv)
        sys.exit(0)
    args = sys.argv[1:]
    if "--out" not in args:
        os.makedirs(OUT, exist_ok=True)
        for f in os.listdir(OUT):  # dọn ảnh cũ > 2 ngày
            fp = os.path.join(OUT, f)
            if os.path.isfile(fp) and time.time() - os.path.getmtime(fp) > 2 * 86400:
                os.remove(fp)
        args += ["--out", os.path.abspath(OUT)]
    env = dict(os.environ, MPLBACKEND="Agg", STOCK_NO_TELEGRAM="1")
    r = subprocess.run([python_exe(), os.path.join(DIR, "dev", "cli.py"), *args], env=env, capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    if r.returncode:
        sys.stderr.write((r.stderr or "")[-1500:])
    sys.exit(r.returncode)
