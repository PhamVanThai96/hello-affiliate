# Sổ Tay Hướng Dẫn Vận Hành Hệ Thống Phân Tích Chứng Khoán AI (Quantitative Stock Analysis System)

> **Phiên bản:** v1.0  
> **Dự án:** `yh-fin-monitor`  
> **Mục tiêu:** Hệ thống tự động hóa phân tích kỹ thuật chứng khoán kết hợp mô hình nến Nhật thực chiến (Steve Nison) và thuật toán toán học (Cực trị địa phương, Hồi quy tuyến tính, Tỷ lệ R:R kỷ luật).

---

## 1. Cấu Trúc Dự Án & Luồng Dữ Liệu

```
yh-fin-monitor/
├── prompt-stock-analyze.md       # Tài liệu đặc tả vai trò và quy trình 6 bước của AI Agent
├── dev/                          # Thư mục chứa toàn bộ mã nguồn thực thi
│   ├── analysis_script.py        # [MỚI - v2.0] Script phân tích nâng cao (MFI, MA Cross, Hộp cam, Nến Steve Nison mở rộng, Đồ thị 3 bảng)
│   ├── chart_analysis_skill.py   # Module kỹ năng chuẩn v1.0
│   ├── config_analysis.json      # File cấu hình phân tích đa mã
│   └── requirements.txt          # Danh sách thư viện phụ thuộc Python
├── documents/                    # Tài liệu kiến thức và dữ liệu đồ thị tham chiếu
│   ├── HUONG_DAN_SU_DUNG.md      # Tài liệu này (hướng dẫn vận hành chi tiết)
│   ├── Đồ thị nến Nhật - Steve Nison.pdf  # Cẩm nang lý thuyết nến Nhật nền tảng
│   └── Chart/                    # Kho 407 biểu đồ thực chiến thị trường VN 2019-2020
├── ai-session/                   # Bộ nhớ phiên làm việc và nhật ký RAG
│   ├── agent_session.json        # Trạng thái watchlist và kết quả quét gần nhất
│   ├── recommendation_log.jsonl  # Nhật ký kiểm toán các khuyến nghị Mua/Bán/Theo dõi
│   └── doc_index.json            # Chỉ mục MD5 băm tài liệu phục vụ RAG Sync tự động
├── skills/                       # Thư mục đóng gói AI Skill độc lập
│   ├── SKILL.md                  # Hướng dẫn kỹ năng chuẩn Antigravity
│   └── references/               # Các module tri thức YAML chi tiết
└── output/                       # Thư mục lưu trữ biểu đồ phân tích xuất ra (.png)
```

---

## 2. Cài Đặt & Kích Hoạt Môi Trường Ảo (Virtual Environment)

Yêu cầu môi trường: **Python 3.10+**.

### 2.1. Kích hoạt Virtual Environment (Bắt buộc trước khi chạy code)
Trước khi chạy bất kỳ script Python nào, luôn kích hoạt môi trường ảo để đảm bảo nạp đầy đủ các thư viện (`numpy`, `scipy`, `pandas`, `mplfinance`, `yfinance`):

```bash
# 1. Tạo môi trường ảo nếu chưa có:
python3 -m venv yh-fin-monitor/venv

# 2. Kích hoạt môi trường ảo:
source yh-fin-monitor/venv/bin/activate
# (Hoặc: source google-ads/venv/bin/activate)

# 3. Cài đặt các thư viện phụ thuộc:
pip install -r yh-fin-monitor/dev/requirements.txt
```

Các thư viện chính được sử dụng:
* `yfinance`: Tải dữ liệu lịch sử giá OHLCV thị trường chứng khoán Việt Nam (hậu tố `.VN`, ví dụ: `STB.VN`, `HPG.VN`).
* `scipy`: Tìm điểm cực trị địa phương (`scipy.signal.argrelextrema`).
* `numpy` & `pandas`: Tính toán chỉ báo kỹ thuật (MA, RSI Wilder, Bollinger Bands) và hồi quy tuyến tính `polyfit`.
* `mplfinance` & `matplotlib`: Dựng biểu đồ nến Nhật chuyên nghiệp và xuất file ảnh.

---

## 3. Hướng Dẫn Sử Dụng (Usage)

> [!IMPORTANT]
> Luôn đảm bảo đã kích hoạt Virtual Environment (`source yh-fin-monitor/venv/bin/activate`) trước khi chạy các lệnh dưới đây.

### 3.1. Phân tích Kỹ thuật Toàn diện v2.0 (Khuyến nghị dùng `analysis_script.py`)
Phiên bản v2.0 tích hợp đầy đủ MFI dòng tiền, MA Cross (9, 26), tự động vẽ Hộp tích lũy, thư viện nến Steve Nison mở rộng và đồ thị chuyên nghiệp 3 bảng con:
```bash
# Đảm bảo đã activate venv:
source yh-fin-monitor/venv/bin/activate

# 1. Phân tích 1 mã cụ thể:
python3 yh-fin-monitor/dev/analysis_script.py STB.VN

# 2. Phân tích hàng loạt theo config_analysis.json:
python3 yh-fin-monitor/dev/analysis_script.py
```
Kết quả hiển thị trên màn hình:
* Xu hướng dài hạn (`MA200`), Kênh giá, Median Line & Trạng thái Hộp tích lũy.
* Chỉ số RSI(14) và Dòng tiền MFI(14).
* Mô hình nến Nhật được phát hiện kèm dấu xác nhận khối lượng (`vol_surge ★`).
* Khuyến nghị đa kịch bản: Điểm mua, TP1 (Median / Cản gần), TP2 (Biên trên / Cản cứng), Cắt lỗ ($\le 7\%$).
* Biểu đồ 3 bảng con xuất tại `output/[TICKER]-[DD-MM-YYYY]-[KHUYẾN NGHỊ].png` (Ví dụ: `STB-17-09-2026-THEO-DOI.png`).

### 3.2. Chạy Phân tích Phiên bản Chuẩn v1.0 (`chart_analysis_skill.py`)
```bash
source yh-fin-monitor/venv/bin/activate
python3 yh-fin-monitor/dev/chart_analysis_skill.py STB.VN
```
* Biểu đồ xuất tại: `output/[TICKER]-[DD-MM-YYYY]-[KHUYẾN NGHỊ].png`.
Chỉnh sửa file `yh-fin-monitor/dev/config_analysis.json` để khai báo danh sách các mã cổ phiếu cần quét:
```json
{
  "tickers": ["STB.VN", "HPG.VN", "VCB.VN", "VNM.VN", "MWG.VN"],
  "period": "12mo",
  "interval": "1d",
  "candle_order": 5,
  "lookback": 5,
  "output_dir": "output",
  "session_file": "ai-session/agent_session.json"
}
```
Sau đó chạy lệnh mà không cần đối số:
```bash
python3 yh-fin-monitor/dev/chart_analysis_skill.py
```
Hệ thống sẽ lần lượt phân tích từng mã, tự động lưu biểu đồ riêng biệt vào `output/`, ghi log vào `recommendation_log.jsonl`, và cập nhật `agent_session.json`. Nếu một mã bị lỗi, các mã còn lại vẫn tiếp tục bình thường.

### 3.3. Sử dụng Trong Code Python (Nhúng Module)
```python
from yh_fin_monitor.dev.chart_analysis_skill import run_stock_analysis_skill

result = run_stock_analysis_skill("STB.VN", interval="1d")
print("Hành động:", result["recommendation"]["action"])
print("Vùng mua:", result["recommendation"]["entry_zone"])
print("Chốt lời:", result["recommendation"]["take_profit"])
print("Cắt lỗ:", result["recommendation"]["stop_loss"])
print("Biểu đồ lưu tại:", result["chart_path"])
```

---

## 4. Ý Nghĩa Các Thành Phần & Màu Sắc Trên Biểu Đồ

Mỗi biểu đồ được sinh ra trong `output/` đều tuân thủ quy chuẩn hiển thị trực quan:

| Thành phần | Màu sắc / Kiểu nét | Ý nghĩa kỹ thuật |
|---|---|---|
| **Đường MA20** | Xanh dương (`blue`), nét liền mảnh | Xu hướng ngắn hạn (Hỗ trợ động trong sóng tăng) |
| **Đường MA50** | Cam (`orange`), nét liền mảnh | Xu hướng trung hạn (Đường phòng thủ nhịp chỉnh vừa) |
| **Đường MA200** | Tím (`purple`), nét liền mảnh | Đường sinh tử: Trên MA200 = Bull Market; Dưới MA200 = Bear Market |
| **Biên trên kênh giá** | Đỏ (`red`), nét đứt (`--`) | Kháng cự kênh xu hướng (Vùng kỳ vọng chốt lời) |
| **Biên dưới kênh giá** | Xanh lá (`green`), nét đứt (`--`) | Hỗ trợ kênh xu hướng (Vùng tìm kiếm điểm mua) |
| **Hỗ trợ tĩnh** | Xanh dương đậm (`darkblue`), nét liền | Vùng đáy/cụm fractal có nhiều lần nến chạm bật tăng |
| **Kháng cự tĩnh** | Đỏ đậm (`darkred`), nét liền | Vùng đỉnh/cụm fractal có áp lực bán tháo lịch sử |
| **Chú thích mô hình nến** | Chữ đen kèm mũi tên trỏ vào nến | Tên mô hình nến Nhật được thuật toán phát hiện |
| **Badge Khuyến nghị** | Góc trên bên trái đồ thị | Xanh lá đậm = **MUA**; Đỏ = **BÁN**; Vàng = **THEO DÕI** |

---

## 5. Khung Quản Trị Rủi Ro & Kỷ Luật Vào Lệnh

1. **Bộ lọc MUA (Bắt buộc hội tụ 100% điều kiện):**
   * Giá nằm **TRÊN MA200** (Tuyệt đối không mua cổ phiếu dưới MA200).
   * Giá điều chỉnh pullback về sát **Hỗ trợ mạnh** hoặc **cạnh dưới Kênh tăng** (trong biên độ $\le 3\%$).
   * Chỉ báo **RSI(14) < 65** (Không mua khi thị trường đã quá hưng phấn).
   * Không có dấu hiệu **False Breakout** (phá vỡ giả).
   * Tỷ lệ **Reward / Risk $\ge 2.0$** (Tối thiểu $1:2$).
   * Mức cắt lỗ tối đa **không vượt quá $7\%$** từ giá mua.
2. **Bộ lọc BÁN:**
   * Kích hoạt ngay khi giá **gãy xuống dưới MA200** (kết thúc chu kỳ tăng).
   * Hoặc khi giá vi phạm điểm cắt lỗ $7\%$.
3. **Bộ lọc THEO DÕI:**
   * Khi thị trường đi ngang, giá nằm lơ lửng giữa kênh, hoặc tỷ lệ R:R không đạt $1:2$.

---

## 6. Câu Hỏi Thường Gặp (FAQ)

**Q1: Tại sao hệ thống luôn ưu tiên khung thời gian Ngày (Daily)?**  
*Trả lời:* Khung thời gian Ngày là chuẩn mực cho phong cách Swing Trading và Quantitative Position Trading, loại bỏ nhiễu giá trong phiên (intraday noise) và đảm bảo các mẫu hình nến Nhật mang trọng số tâm lý thực chất nhất.

**Q2: Tại sao một số cổ phiếu rất tốt nhưng hệ thống lại khuyến nghị "THEO DÕI"?**  
*Trả lời:* Hệ thống bảo vệ nhà đầu tư khỏi rủi ro mua đuổi. Nếu giá đã tăng xa khỏi vùng hỗ trợ, dù xu hướng là tăng thì tỷ lệ R:R sẽ $< 1:2$, do đó hệ thống kiên nhẫn xếp vào diện "THEO DÕI" để chờ nhịp pullback an toàn.

**Q3: Cơ chế RAG Sync hoạt động như thế nào?**  
*Trả lời:* Mỗi lần khởi chạy, hệ thống băm mã MD5 toàn bộ các file trong `documents/`. Nếu bạn thêm biểu đồ mới vào `documents/Chart/` hoặc tài liệu PDF/MD mới, hệ thống sẽ phát hiện trạng thái `updated` và cập nhật chỉ mục `ai-session/doc_index.json`.

---

> [!NOTE]
> **Tuyên bố Miễn trừ Trách nhiệm:**  
> Toàn bộ thông tin, số liệu tính toán và biểu đồ do hệ thống sinh ra nhằm mục đích nghiên cứu và hỗ trợ phân tích kỹ thuật. Nhà đầu tư cần tự đánh giá mức độ chấp nhận rủi ro trước khi ra quyết định đầu tư.
