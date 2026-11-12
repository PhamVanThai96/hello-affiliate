This project is designed to monitor financial data using the Yahoo Finance API. It provides tools for analyzing stock market trends and generating reports based on the specified configurations.

## Activate a virtual environment (optional but recommended):

    python3 -m venv venv
    source venv/bin/activate

## To install the required packages, run the following command in your terminal:
    
    pip install -r dev/requirements.txt

## Folder Structure:

/dev: Contains development-related files, including requirements.txt and configuration files for analysis.
/output: Directory where analysis results and reports will be saved.
/skills: Contains scripts and modules for performing various financial analyses.
/documents: Documentation and additional resources related to the project.
/ai-session: Stores session data for the AI agent used in the analysis.

## Configuration:
The configuration for the analysis is specified in the `dev/config_analysis.json` file. You can modify the following parameters:
- `tickers`: A list of stock tickers to analyze (e.g., ["STB.VN", "VNM.VN"]).
- `period`: The time period for the analysis (e.g., "12mo" for 12 months).
- `interval`: The data interval (e.g., "1d" for daily data).
- `candle_order`: The order of the candlestick chart to be generated.
- `lookback`: The number of past data points to consider for analysis.
- `output_dir`: The directory where output files will be saved.

After modifying the configuration file and activate the virtual environment, you can run the analysis script to generate reports based on the specified parameters.

    python3 dev/analysis_script.py

## Please update ai-sesion at the end of the analysis to save the session data for future reference.

## Nhận định xu hướng v3.0 (outlook_v3) và kiểm chứng

- `dev/outlook_v3.py`: nhận định THIÊN HƯỚNG có hiệu chuẩn xác suất (theo chế độ thị trường chung + điểm xu hướng) và vùng biến động 80% (cone ATR) thay cho mũi tên "dự báo" theo luật. `dev/outlook_calibration.json` là bảng hiệu chuẩn, tạo bằng `python3 dev/calibrate_outlook.py`.
- Mã kiểm thử walk-forward một lần (validate_*) đã được gỡ khỏi repo sau khi chạy xong; kết quả và phương pháp nằm ở `documents/VERIFICATION_FINDINGS.md`. Làm mới bảng hiệu chuẩn định kỳ bằng `python3 dev/calibrate_outlook.py`. Gọi công cụ cho agent: `dev/cli.py` (qua `mba-agent-office/tools/stock_cli.py`).
- Kết quả kiểm chứng ngoài mẫu (hiệu chuẩn trên dữ liệu đến 2019 và mã khác MSN/VRE/HPG; chấm từ 2020): mũi tên cũ đúng ~47,6% (10 phiên); v3 đúng ~52% nhưng không hơn "luôn tăng" (50,8%); vùng biến động 80% phủ ~82,7%. Kết luận: hướng giá 10-20 phiên gần như không dự báo được chỉ từ giá; vùng biến động thì dự báo tốt.
- Tắt gửi Telegram khi kiểm thử: `STOCK_NO_TELEGRAM=1` hoặc `send_telegram=False`.
- Kênh giá v3 (`compute_trend_channel`): chỉ dùng giai đoạn gần nhất (60-150 phiên, bắt đầu từ nhịp sóng đáng kể gần nhất), đường giữa hồi quy + biên song song ở phân vị 99%/1% của High/Low. Kiểm chứng (xem VERIFICATION_FINDINGS): kênh cũ chứa 10 phiên kế tiếp ~31%, kênh mới ~77% (bề rộng 15-17% so với 8-10%); "phá vỡ kênh" cũ báo ở ~26% số ngày, kênh mới ~2% và 57-67% là phá vỡ giả (quay lại trong 5 phiên).
