# Budgeting & Forecasting – Lập Ngân Sách & Dự Báo

> **Mục tiêu**: Hiểu rõ quy trình lập ngân sách (budgeting), các phương pháp dự báo (forecasting), Master Budget, Flexible Budget, Rolling Forecast, và ứng dụng cho SME Việt Nam.

---

## I. ĐỊNH NGHĨA VÀ LÝ THUYẾT NỀN TẢNG

### 1. Định nghĩa

**Budgeting (Lập ngân sách)** là quá trình **lập kế hoạch tài chính chi tiết** cho một khoảng thời gian (thường 1 năm), thể hiện bằng con số cụ thể: doanh thu dự kiến, chi phí, lợi nhuận, dòng tiền.

**Forecasting (Dự báo)** là quá trình **ước tính kết quả tương lai** dựa trên dữ liệu lịch sử, xu hướng, và giả định. Forecast có thể cập nhật liên tục, trong khi budget thường cố định.

> **"A budget tells your money where to go instead of wondering where it went."** – Dave Ramsey

### 2. Phân biệt Budget vs Forecast

| Tiêu chí | Budget | Forecast |
|----------|--------|----------|
| **Mục đích** | Kế hoạch & kiểm soát | Dự đoán & điều chỉnh |
| **Thời gian** | Thường 1 năm, cố định | Liên tục cập nhật (rolling) |
| **Tần suất lập** | 1 lần/năm | Hàng tháng/quý |
| **Phê duyệt** | Cần approval từ leadership | Không nhất thiết |
| **Độ chi tiết** | Rất chi tiết (dòng chi phí) | Tổng quát hơn |
| **Linh hoạt** | Cứng (fixed target) | Mềm (rolling adjustment) |
| **Đánh giá hiệu suất** | Chuẩn so sánh (benchmark) | Không dùng để đánh giá |

### 3. Vai trò của Budgeting

```
┌──────────────────────────────────────────────────┐
│           VAI TRÒ CỦA BUDGETING                  │
│                                                    │
│  ┌─────────────┐  ┌──────────────┐                │
│  │ PLANNING    │  │ COMMUNICATION│                │
│  │ Lập kế hoạch│  │ Truyền thông │                │
│  │ chiến lược  │  │ mục tiêu     │                │
│  └──────┬──────┘  └──────┬───────┘                │
│         │                │                         │
│  ┌──────▼──────┐  ┌──────▼───────┐                │
│  │ COORDINATION│  │ MOTIVATION   │                │
│  │ Phối hợp    │  │ Tạo động lực │                │
│  │ các bộ phận │  │ đạt target   │                │
│  └──────┬──────┘  └──────┬───────┘                │
│         │                │                         │
│  ┌──────▼──────┐  ┌──────▼───────┐                │
│  │ CONTROL     │  │ EVALUATION   │                │
│  │ Kiểm soát   │  │ Đánh giá     │                │
│  │ chi tiêu    │  │ hiệu suất    │                │
│  └─────────────┘  └──────────────┘                │
└──────────────────────────────────────────────────┘
```

---

## II. MASTER BUDGET – NGÂN SÁCH TỔNG THỂ

### 1. Cấu trúc Master Budget

```
                    MASTER BUDGET
                         │
          ┌──────────────┼──────────────┐
          │              │              │
   OPERATING         FINANCIAL      CAPITAL
   BUDGET            BUDGET         BUDGET
          │              │              │
   ┌──────┼──────┐  ┌────┼────┐    ┌────┼────┐
   │      │      │  │    │    │    │         │
Sales  Production Cash Pro-forma CapEx    Project
Budget Budget    Budget  B/S     Budget   Budgets
   │      │         │    P&L
   │   ┌──┼──┐      │
   │   │  │  │      │
  DM  DL MOH Selling & Admin
Budget Budget Budget  Budget
```

### 2. Quy trình lập Master Budget

```
  Bước 1: Sales Budget (Ngân sách bán hàng)
  ► Nền tảng – mọi budget khác đều xuất phát từ đây
       │
  Bước 2: Production Budget (Ngân sách sản xuất)
  ► Sản lượng cần SX = Bán + Tồn kho cuối kỳ - Tồn kho đầu kỳ
       │
  Bước 3: Direct Materials Budget (NVL trực tiếp)
       │
  Bước 4: Direct Labor Budget (Nhân công trực tiếp)
       │
  Bước 5: Manufacturing Overhead Budget
       │
  Bước 6: Selling & Administrative Budget
       │
  Bước 7: Cash Budget (Ngân sách tiền mặt)
  ► Tổng hợp thu – chi tiền thực tế
       │
  Bước 8: Pro-forma Financial Statements
  ► Projected Income Statement + Balance Sheet
```

### 3. Ví dụ chi tiết: SME sản xuất nước ép

**Dữ liệu cơ bản:**

| Thông tin | Q1 | Q2 | Q3 | Q4 | Cả năm |
|----------|------|------|------|------|-------|
| **BƯỚC 1: Sales Budget** | | | | | |
| Dự kiến bán (chai) | 10,000 | 15,000 | 20,000 | 12,000 | 57,000 |
| Giá bán/chai | 30k | 30k | 30k | 30k | |
| **Doanh thu** | **300tr** | **450tr** | **600tr** | **360tr** | **1,710tr** |

**BƯỚC 2: Production Budget**

Chính sách: Tồn kho cuối kỳ = 20% nhu cầu bán quý sau (Q1 năm sau dự kiến 11,000 chai)

| | Q1 | Q2 | Q3 | Q4 |
|---|------|------|------|------|
| Dự kiến bán | 10,000 | 15,000 | 20,000 | 12,000 |
| + Tồn kho cuối kỳ mong muốn | 3,000 | 4,000 | 2,400 | 2,200 |
| - Tồn kho đầu kỳ | (2,000) | (3,000) | (4,000) | (2,400) |
| **= Sản lượng cần SX** | **11,000** | **16,000** | **18,400** | **11,800** |

**BƯỚC 3: Direct Materials Budget**

Mỗi chai cần 0.5 lít nước ép nguyên liệu (10k/lít):

| | Q1 | Q2 | Q3 | Q4 |
|---|------|------|------|------|
| NVL cần (lít) | 5,500 | 8,000 | 9,200 | 5,900 |
| + TK NVL cuối kỳ (10% quý sau) | 800 | 920 | 590 | 550 |
| - TK NVL đầu kỳ | (550) | (800) | (920) | (590) |
| = NVL cần mua (lít) | 5,750 | 8,120 | 8,870 | 5,860 |
| **Chi phí NVL** (×10k/lít) | **57.5tr** | **81.2tr** | **88.7tr** | **58.6tr** |

**BƯỚC 7: Cash Budget (Tóm tắt)**

| | Q1 | Q2 | Q3 | Q4 |
|---|------|------|------|------|
| Tiền đầu kỳ | 50tr | 32.5tr | 41.3tr | 95.6tr |
| + Thu tiền bán hàng* | 270tr | 375tr | 525tr | 480tr |
| - Chi NVL | (57.5tr) | (81.2tr) | (88.7tr) | (58.6tr) |
| - Chi nhân công | (55tr) | (80tr) | (92tr) | (59tr) |
| - Chi overhead | (40tr) | (45tr) | (50tr) | (42tr) |
| - Chi S&A | (35tr) | (38tr) | (40tr) | (36tr) |
| - Chi CapEx | (50tr) | – | – | – |
| **= Tiền cuối kỳ** | **32.5tr** | **41.3tr** | **95.6tr** | **180tr** |

*Thu tiền: 90% trong quý, 10% quý sau (phải thu)

---

## III. CÁC PHƯƠNG PHÁP BUDGETING

### 1. So sánh các phương pháp

| Phương pháp | Cách tiếp cận | Ưu điểm | Nhược điểm | Phù hợp |
|-------------|-------------|---------|-----------|---------|
| **Incremental** | Budget năm trước + % tăng | Đơn giản, nhanh | Giữ nguyên bất hợp lý, không tối ưu | DN ổn định |
| **Zero-Based (ZBB)** | Bắt đầu từ 0, justify mọi khoản | Loại bỏ lãng phí | Tốn rất nhiều thời gian | Cần cắt giảm |
| **Activity-Based (ABB)** | Budget dựa trên activity & driver | Chính xác, link tới output | Phức tạp, cần ABC system | DN lớn |
| **Flexible Budget** | Điều chỉnh theo actual volume | So sánh fair hơn | Phức tạp hơn static | Sản lượng biến động |
| **Rolling Budget** | Luôn có 12 tháng tới | Luôn forward-looking | Tốn effort cập nhật | Mọi DN |
| **Beyond Budgeting** | Bỏ budget cố định, dùng KPI | Linh hoạt, phi tập trung | Khó kiểm soát, cần văn hóa mạnh | DN innovate |

### 2. Zero-Based Budgeting (ZBB) – Chi tiết

**Quy trình:**

```
  Bước 1: Xác định "Decision Units" (đơn vị quyết định)
       │   Mỗi bộ phận / dự án / hoạt động
       │
  Bước 2: Tạo "Decision Packages" cho mỗi unit
       │   - Mức tối thiểu (base)
       │   - Mức hiện tại (current)
       │   - Mức tăng cường (enhanced)
       │
  Bước 3: Xếp hạng (Ranking) tất cả decision packages
       │   Theo ROI, độ cấp thiết, chiến lược
       │
  Bước 4: Phân bổ ngân sách từ trên xuống
       │   Packages có rank cao → approved
       │   Packages rank thấp → cut / defer
```

**Ví dụ ZBB cho Marketing Department (150 triệu budget):**

| Package | Mô tả | Chi phí | Rank | Approved? |
|---------|-------|---------|------|----------|
| MKT-1: SEO cơ bản | Duy trì SEO website | 15tr | 1 | ✅ |
| MKT-2: Facebook Ads | Chạy ads FB/IG | 40tr | 2 | ✅ |
| MKT-3: Content team | 2 content creators | 60tr | 3 | ✅ |
| MKT-4: KOL campaign | Hợp tác 5 KOL | 30tr | 4 | ✅ (budget còn 35tr) |
| MKT-5: Billboard | Quảng cáo ngoài trời | 50tr | 5 | ❌ (hết budget) |
| MKT-6: TikTok Ads | Mở thêm kênh TikTok | 25tr | 6 | ❌ |

→ **ZBB force justify từng khoản** → Loại bỏ chi phí "vì năm trước cũng chi"

### 3. Flexible Budget – Chi tiết

**Static Budget vs Flexible Budget:**

Giả sử budget cho 10,000 sản phẩm, thực tế bán 12,000:

| | Static Budget (10,000 SP) | Flexible Budget (12,000 SP) | Actual (12,000 SP) |
|---|--------------------------|---------------------------|-------------------|
| Doanh thu | 500tr | 600tr | 580tr |
| Biến phí | (200tr) | (240tr) | (260tr) |
| Định phí | (150tr) | (150tr) | (155tr) |
| **Lợi nhuận** | **150tr** | **210tr** | **165tr** |
| | | | |
| **Variance** | Favorable 15tr? | **Unfavorable (45tr)** | |

**Insight:** Static budget cho thấy "vượt target 15tr" → sai lệch! Flexible budget cho thấy thực tế lợi nhuận kém hơn kỳ vọng 45tr ở mức 12,000 SP → **biến phí vượt kiểm soát**.

### 4. Rolling Forecast

```
  Tháng       1  2  3  4  5  6  7  8  9  10 11 12  1  2  3
              ├──┤──┤──┤──┤──┤──┤──┤──┤──┤──┤──┤──┤
  Jan Budget  ════════════════════════════════════════
              Actual → → → →  Forecast → → → → → → →

  Apr Update           ├──┤──┤──┤──┤──┤──┤──┤──┤──┤──┤──┤
                       Act│ ► ► ► ► ► ► ► ► ► ► ► ►
                           Updated forecast with new data
                           + Add 3 months (Jan-Mar next yr)

  → Luôn có 12 tháng forecast phía trước
  → Cập nhật hàng quý (hoặc hàng tháng)
```

---

## IV. PHƯƠNG PHÁP DỰ BÁO (FORECASTING METHODS)

### 1. Tổng quan

```
           FORECASTING METHODS
                  │
     ┌────────────┼────────────┐
     │            │            │
QUALITATIVE    TIME SERIES   CAUSAL
(Định tính)    (Chuỗi thời   (Nhân quả)
               gian)
     │            │            │
- Expert       - Moving      - Regression
  judgment       Average     - Correlation
- Delphi       - Exponential - Econometric
  Method         Smoothing     models
- Market       - Trend
  survey         analysis
- Sales force  - Seasonal
  estimates      decomposition
```

### 2. Phương pháp định lượng chi tiết

#### a) Moving Average (Trung bình di động)

$$\text{Forecast}_{t+1} = \frac{\sum_{i=t-n+1}^{t} \text{Actual}_i}{n}$$

**Ví dụ (3-month MA):**

| Tháng | Doanh thu (triệu) | 3-Month MA | Error |
|-------|-------------------|-----------|-------|
| 1 | 100 | – | – |
| 2 | 120 | – | – |
| 3 | 110 | – | – |
| 4 | 130 | (100+120+110)/3 = **110** | +20 |
| 5 | 125 | (120+110+130)/3 = **120** | +5 |
| 6 | 140 | (110+130+125)/3 = **122** | +18 |
| **7** | ? | (130+125+140)/3 = **132** | – |

#### b) Exponential Smoothing (San mũ)

$$F_{t+1} = \alpha \times A_t + (1-\alpha) \times F_t$$

Trong đó $\alpha$ (alpha) = hệ số san mũ (0 < α < 1)
- α cao (0.7-0.9): Phản ứng nhanh với thay đổi
- α thấp (0.1-0.3): Phản ứng chậm, stable hơn

**Ví dụ (α = 0.3):**

| Tháng | Actual | Forecast | Tính toán |
|-------|--------|----------|----------|
| 1 | 100 | 100 | Khởi tạo |
| 2 | 120 | 100 | 0.3×100 + 0.7×100 |
| 3 | 110 | 106 | 0.3×120 + 0.7×100 |
| 4 | 130 | 107.2 | 0.3×110 + 0.7×106 |
| 5 | 125 | 114.0 | 0.3×130 + 0.7×107.2 |
| 6 | 140 | 117.3 | 0.3×125 + 0.7×114.0 |
| **7** | ? | **124.1** | 0.3×140 + 0.7×117.3 |

#### c) Linear Regression (Hồi quy tuyến tính)

$$Y = a + bX$$

$$b = \frac{n\sum{XY} - \sum{X}\sum{Y}}{n\sum{X^2} - (\sum{X})^2}$$

$$a = \bar{Y} - b\bar{X}$$

**Ví dụ:** Dự báo doanh thu dựa trên chi phí marketing

| Tháng (X) | Marketing (triệu) | Doanh thu (triệu) (Y) |
|-----------|-------------------|----------------------|
| 1 | 20 | 200 |
| 2 | 25 | 240 |
| 3 | 30 | 280 |
| 4 | 22 | 210 |
| 5 | 35 | 320 |
| 6 | 28 | 260 |

Regression: Y = 20 + 8.5X → Nếu tháng 7 chi 40 triệu marketing → Doanh thu dự kiến = 20 + 8.5 × 40 = **360 triệu**

### 3. Đo lường độ chính xác dự báo

| Metric | Công thức | Ý nghĩa |
|--------|----------|---------|
| **MAD** (Mean Absolute Deviation) | $\frac{\sum\|A-F\|}{n}$ | Sai số trung bình tuyệt đối |
| **MAPE** (Mean Absolute % Error) | $\frac{\sum\|\frac{A-F}{A}\|}{n} \times 100\%$ | % sai số trung bình |
| **MSE** (Mean Square Error) | $\frac{\sum(A-F)^2}{n}$ | Phạt nặng sai số lớn |
| **Tracking Signal** | $\frac{\text{Running Sum of Errors}}{\text{MAD}}$ | Phát hiện bias (trong ±4) |

---

## V. ƯU VÀ NHƯỢC ĐIỂM

### 1. Budgeting

| Ưu điểm | Nhược điểm |
|---------|-----------|
| ✅ Đặt mục tiêu rõ ràng bằng con số | ❌ Tốn thời gian lập (3-6 tháng cho DN lớn) |
| ✅ Phối hợp giữa các bộ phận | ❌ Nhanh lỗi thời trong môi trường biến động |
| ✅ Kiểm soát chi tiêu | ❌ Gaming/Padding – bộ phận inflate budget |
| ✅ Chuẩn so sánh cho variance analysis | ❌ Cứng nhắc, khó thích ứng |
| ✅ Tạo accountability (trách nhiệm) | ❌ Có thể khuyến khích "spend it or lose it" |
| ✅ Buộc leadership nghĩ về tương lai | ❌ Focus ngắn hạn (1 năm) |

### 2. Forecasting

| Ưu điểm | Nhược điểm |
|---------|-----------|
| ✅ Linh hoạt, cập nhật liên tục | ❌ Không thay thế được budget cho accountability |
| ✅ Phản ứng nhanh với thay đổi | ❌ Phụ thuộc chất lượng dữ liệu & giả định |
| ✅ Forward-looking | ❌ "Garbage in, garbage out" |
| ✅ Hỗ trợ quyết định ngắn hạn | ❌ Black swan events không dự đoán được |

---

## VI. HOÀN CẢNH VÀ MÔI TRƯỜNG ÁP DỤNG

### 1. Theo giai đoạn DN

| Giai đoạn | Budget approach | Forecast approach |
|----------|----------------|------------------|
| **Startup (<1 năm)** | 13-week cash flow budget | Monthly rolling forecast |
| **Early stage (1-3 năm)** | Annual budget (simple) | Quarterly rolling |
| **Growth (3-7 năm)** | Master budget + Flexible | Monthly rolling + Scenario |
| **Mature (>7 năm)** | Full master budget + ZBB cycle | Rolling + Driver-based |

### 2. Theo mức độ biến động

| Biến động | Budget | Forecast | Tần suất update |
|----------|--------|----------|----------------|
| **Thấp** (utilities, FMCG) | Static budget đủ | Quarterly update | Quý |
| **Trung bình** (dịch vụ, retail) | Flexible budget | Monthly rolling | Tháng |
| **Cao** (tech, startup) | Rolling budget hoặc Beyond Budgeting | Weekly/Bi-weekly | Tuần |

### 3. Sơ đồ quyết định

```
     DN của bạn ở giai đoạn nào?
              │
     ┌────────┼────────┐
     │                 │
  Startup           Established
     │                 │
  13-week          ┌───┴───┐
  cash flow        │       │
  + Monthly      Ổn định  Biến động
  forecast         │       │
                 Static   Flexible
                 Budget   + Rolling
                   +        +
                 Quarterly Monthly
                 Forecast  Forecast
```

---

## VII. CASE STUDY THÀNH CÔNG

### Case Study: **Unilever – Zero-Based Budgeting transformation**

**Bối cảnh:**
Năm 2016, Unilever (consumer goods, $52 tỷ revenue) đối mặt áp lực từ Kraft Heinz (backed by 3G Capital) muốn mua lại. Cần chứng minh có thể tự cải thiện profitability.

**Giải pháp: Áp dụng ZBB toàn diện**

| Giai đoạn | Hành động | Kết quả |
|----------|----------|---------|
| **Phase 1** (2016) | Pilot ZBB tại 3 thị trường | Tiết kiệm €200 triệu |
| **Phase 2** (2017-18) | Roll-out toàn cầu, mọi bộ phận | Operating margin: 16% → 19% |
| **Phase 3** (2019-20) | ZBB + Digital transformation | Tổng tiết kiệm > €2 tỷ |

**Chi tiết triển khai:**

| Lĩnh vực | Trước ZBB | Sau ZBB | Tiết kiệm |
|----------|----------|--------|----------|
| Marketing spend | €7.7 tỷ (15% revenue) | €7.1 tỷ (14%) – hiệu quả hơn | €600 triệu |
| Supply chain | Nhiều nhà máy dư thừa | Đóng 15 nhà máy, optimize logistics | €500 triệu |
| Corporate overhead | Hàng ngàn consultant, travel | Cut consulting 30%, travel 40% | €400 triệu |
| Procurement | Buying fragmented | Centralized, negotiate volume | €500 triệu |

**Nguyên tắc ZBB của Unilever:**
1. **Visibility**: Mọi chi phí phải visible, không "ẩn" trong budget tổng
2. **Ownership**: Mỗi khoản chi phải có "owner" chịu trách nhiệm
3. **Benchmarking**: So sánh với best-in-class, không chỉ so với năm trước
4. **Zero-base**: Justify mọi khoản, không auto-approve

**Kết quả tổng thể:**
- Operating Margin: **16.4% (2015) → 19.1% (2019) → 18.4% (2022)**
- Từ chối thành công Kraft Heinz takeover bid ($143 tỷ)
- Chứng minh tự cải thiện được mà không cần bán công ty

**Bài học:**
> ZBB không phải "cắt giảm chi phí" đơn thuần – mà là **phân bổ lại nguồn lực vào nơi tạo giá trị cao nhất**. Tiết kiệm marketing spend nhưng marketing HIỆU QUẢ hơn.

---

## VIII. CASE STUDY THẤT BẠI

### Case Study: **Sears – Budget cứng nhắc góp phần cho sụp đổ**

**Bối cảnh:**
Sears (từng là retailer lớn nhất nước Mỹ) dần suy thoái từ 2000s và phá sản năm 2018.

**Vấn đề với Budgeting:**

| Yếu tố | Chi tiết | Hệ quả |
|--------|---------|--------|
| **Incremental budgeting** | Budget năm sau = năm trước ± 5% | Không tái phân bổ cho digital |
| **Silo budgets** | Mỗi department fight for budget | Không collaborate, internal competition |
| **Short-term focus** | Budget 1 năm, maximize bonus | Cắt giảm R&D, training, maintenance |
| **No rolling forecast** | Không cập nhật khi market thay đổi | Amazon/Walmart thay đổi game, Sears vẫn budget theo cách cũ |
| **Gaming culture** | Managers pad budget 20-30% | Hoang phí nguồn lực |

**So sánh Sears vs Amazon cùng thời kỳ:**

| Yếu tố | Sears (2010-2018) | Amazon (2010-2018) |
|--------|------------------|-------------------|
| Budget approach | Incremental, rigid | Driver-based, rolling |
| CapEx allocation | Dàn đều cửa hàng | Focus vào AWS, logistics |
| Forecast | Annual, static | Real-time, data-driven |
| React to change | Budget approved → cannot change | Forecast update weekly |
| Innovation budget | 0.5% revenue | 12% revenue (R&D) |

**Hệ quả:**
- Sears: Revenue giảm từ **$53 tỷ (2006) → $16 tỷ (2017) → phá sản (2018)**
- "Budget lock-in" ngăn cản chuyển đổi digital
- Không có rolling forecast → Không thấy xu hướng suy giảm đến khi quá muộn

**Bài học:**
> 1. **Incremental budgeting trong môi trường disruptive = chết chậm** – Cần ZBB hoặc driver-based
> 2. **Budget phải align với strategy** – Nếu chiến lược là digital transformation, budget phải reflect
> 3. **Rolling forecast cần thiết** – Đợi đến budget cycle năm sau mới thay đổi = quá chậm
> 4. **Anti-gaming culture** – Budget padding tạo ra lãng phí có hệ thống

---

## IX. ÁP DỤNG CHO SME VIỆT NAM

### 1. Template ngân sách đơn giản cho SME

```
┌──────────────────────────────────────────────────┐
│     NGÂN SÁCH NĂM 20XX – CÔNG TY ABC            │
│                                                    │
│  I. DOANH THU DỰ KIẾN                             │
│     Sản phẩm A: _____ × _____ = _____            │
│     Sản phẩm B: _____ × _____ = _____            │
│     Dịch vụ:   _____                              │
│     Tổng doanh thu:          _____________        │
│                                                    │
│  II. CHI PHÍ BIẾN ĐỔI                             │
│     NVL: ___% doanh thu =   _____                │
│     Nhân công trực tiếp:     _____                │
│     Hoa hồng bán hàng:      _____                │
│     Shipping:                _____                │
│     Tổng biến phí:          _____________        │
│                                                    │
│  III. CONTRIBUTION MARGIN    _____________        │
│       CM% =                  _____%               │
│                                                    │
│  IV. CHI PHÍ CỐ ĐỊNH                              │
│     Thuê mặt bằng:          _____                │
│     Lương quản lý:           _____                │
│     Bảo hiểm:               _____                │
│     Marketing:               _____                │
│     Phần mềm/IT:            _____                │
│     Khấu hao:               _____                │
│     Khác:                    _____                │
│     Tổng định phí:          _____________        │
│                                                    │
│  V. LỢI NHUẬN DỰ KIẾN      _____________        │
│     Operating Margin:        _____%               │
│                                                    │
│  VI. DÒNG TIỀN                                     │
│     Thu tiền dự kiến:        _____                │
│     Chi tiền dự kiến:        _____                │
│     Net Cash Flow:           _____________        │
└──────────────────────────────────────────────────┘
```

### 2. Quy trình lập ngân sách cho SME (6 bước)

| Bước | Hành động | Người thực hiện | Timeline |
|------|----------|----------------|---------|
| 1 | CEO đặt target tổng (revenue, profit) | CEO | T11 tuần 1 |
| 2 | Các bộ phận lập budget chi tiết | Managers | T11 tuần 2-3 |
| 3 | Kế toán tổng hợp & check consistency | CFO/Kế toán | T11 tuần 4 |
| 4 | Review & điều chỉnh | CEO + Team | T12 tuần 1 |
| 5 | Phê duyệt | CEO | T12 tuần 2 |
| 6 | Triển khai & follow-up hàng tháng | Kế toán | Hàng tháng |

### 3. 13-Week Cash Flow Forecast (Cho Startup)

**Tại sao 13 tuần?** = 1 quý, đủ ngắn để chính xác, đủ dài để hành động.

```
  Tuần →          1    2    3    4    5   ...  13
  ────────────────────────────────────────────────
  Tiền đầu tuần   50   42   35   28   31  ...  XX
  + Thu tiền        0   10   25   30   15  ...
  - Trả NCC       (5)  (8)  (20) (15) (12) ...
  - Lương          0    0  (10)   0    0   (10)
  - Thuê           0    0    0  (10)   0    0
  - Khác          (3)  (9)  (2)  (2)  (5)  ...
  ────────────────────────────────────────────────
  Tiền cuối tuần  42   35   28   31   29  ...  XX
  ────────────────────────────────────────────────
  Alert nếu <20 triệu → NGUY HIỂM
```

### 4. Checklist Budgeting & Forecasting cho SME

| # | Hạng mục | Tần suất | Ưu tiên |
|---|---------|---------|---------|
| 1 | Lập Annual Budget (tối thiểu Sales + Expenses + Cash) | Năm | ⭐⭐⭐ |
| 2 | 13-week Cash Flow Forecast | Cập nhật tuần | ⭐⭐⭐ |
| 3 | Monthly Actual vs Budget comparison | Tháng | ⭐⭐⭐ |
| 4 | Quarterly forecast update | Quý | ⭐⭐ |
| 5 | Scenario planning (Best/Base/Worst) | Năm hoặc khi có biến động | ⭐⭐ |
| 6 | Zero-Based review cho chi phí lớn nhất | Năm | ⭐ |

---

## X. CÔNG THỨC TỔNG HỢP

### Budget

$$\text{Production Budget} = \text{Sales} + \text{Ending Inventory} - \text{Beginning Inventory}$$

$$\text{DM Purchase} = \text{DM Needed} + \text{Ending DM Inv} - \text{Beginning DM Inv}$$

### Forecasting

$$\text{Moving Average}_{t+1} = \frac{\sum_{i=t-n+1}^{t} A_i}{n}$$

$$\text{Exponential Smoothing}: F_{t+1} = \alpha A_t + (1-\alpha)F_t$$

$$\text{MAPE} = \frac{1}{n}\sum\left|\frac{A_i - F_i}{A_i}\right| \times 100\%$$

### Flexible Budget

$$\text{Flexible Budget} = \text{Variable Rate} \times \text{Actual Volume} + \text{Fixed Costs}$$

---

## XI. TÀI LIỆU THAM KHẢO

1. **Garrison, Noreen & Brewer** – "Managerial Accounting" Ch. 8-10 (Budgeting)
2. **Horngren** – "Cost Accounting" Ch. 6 (Master Budget)
3. **Pyhrr, Peter** – "Zero-Base Budgeting" (ZBB originator)
4. **Hope & Fraser** – "Beyond Budgeting" (BBRT – Beyond Budgeting Round Table)
5. **FP&A Body of Knowledge** – AFP (Association for Financial Professionals)
6. **McKinsey** – "The case for Zero-Based Budgeting" (2018)
7. **Deloitte** – "Rolling Forecasts: A Proactive Approach to Planning"
