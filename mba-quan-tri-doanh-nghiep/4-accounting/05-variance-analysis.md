# Variance Analysis – Phân Tích Chênh Lệch

> **Mục tiêu**: Hiểu rõ phân tích chênh lệch (variance analysis) – công cụ so sánh kết quả thực tế vs kế hoạch. Các loại variance, phân tích nguyên nhân, hành động khắc phục, và ứng dụng cho SME Việt Nam.

---

## I. ĐỊNH NGHĨA VÀ LÝ THUYẾT NỀN TẢNG

### 1. Định nghĩa

**Variance Analysis (Phân tích chênh lệch)** là quá trình **so sánh kết quả thực tế (Actual) với tiêu chuẩn/kế hoạch (Standard/Budget)**, xác định nguyên nhân chênh lệch, và đề xuất hành động khắc phục.

$$\text{Variance} = \text{Actual} - \text{Standard (Budget)}$$

- **Favorable Variance (F)**: Thực tế TỐT HƠN kế hoạch (doanh thu cao hơn hoặc chi phí thấp hơn)
- **Unfavorable Variance (U)**: Thực tế XẤU HƠN kế hoạch (doanh thu thấp hơn hoặc chi phí cao hơn)

> **"What gets measured gets managed. What gets compared gets improved."**

### 2. Vai trò trong Management Control

```
┌──────────────────────────────────────────────────┐
│         MANAGEMENT CONTROL CYCLE                  │
│                                                    │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    │
│  │ PLAN     │───►│ EXECUTE  │───►│ MEASURE  │    │
│  │ (Budget) │    │ (Do)     │    │ (Actual) │    │
│  └────┬─────┘    └──────────┘    └────┬─────┘    │
│       │                              │           │
│       │         ┌──────────┐         │           │
│       └────────►│ COMPARE  │◄────────┘           │
│                 │ VARIANCE │                     │
│                 │ ANALYSIS │                     │
│                 └────┬─────┘                     │
│                      │                           │
│               ┌──────▼──────┐                    │
│               │ CORRECTIVE  │                    │
│               │ ACTION      │                    │
│               │ (Act)       │                    │
│               └─────────────┘                    │
└──────────────────────────────────────────────────┘
```

### 3. Standard Costs (Chi phí tiêu chuẩn)

**Standard Cost** là chi phí **kỳ vọng/mục tiêu** cho mỗi đơn vị sản phẩm, được xác định dựa trên:

| Loại Standard | Mức độ | Sử dụng khi |
|-------------|--------|-------------|
| **Ideal Standard** | Hoàn hảo, không lãng phí | Mục tiêu dài hạn (Toyota, Lean) |
| **Currently Attainable** | Khả thi, cho phép lãng phí hợp lý | Phổ biến nhất – budget & evaluation |
| **Basic Standard** | Cố định, không đổi nhiều năm | So sánh xu hướng dài hạn |

**Ví dụ Standard Cost Card:**

```
┌──────────────────────────────────────────────┐
│  STANDARD COST CARD – Sản phẩm: Áo thun     │
│                                                │
│  Direct Materials:                             │
│    Vải:    1.2m × 50,000/m     = 60,000       │
│    Phụ kiện (nút, nhãn):      =  5,000       │
│                                                │
│  Direct Labor:                                 │
│    Cắt:    0.5h × 40,000/h    = 20,000       │
│    May:    1.0h × 40,000/h    = 40,000       │
│    QC:     0.2h × 35,000/h    =  7,000       │
│                                                │
│  Variable MOH:                                 │
│    1.7 DLH × 15,000/DLH      = 25,500       │
│                                                │
│  Fixed MOH (phân bổ):                         │
│    1.7 DLH × 20,000/DLH      = 34,000       │
│                                                │
│  ═══════════════════════════════════════       │
│  TOTAL STANDARD COST/unit:      191,500      │
└──────────────────────────────────────────────┘
```

---

## II. CÁC LOẠI VARIANCE CHI TIẾT

### 1. Sơ đồ tổng quan

```
                    TOTAL VARIANCE
              (Actual Profit - Budgeted Profit)
                          │
            ┌─────────────┼─────────────┐
            │                           │
      REVENUE                      COST
      VARIANCE                   VARIANCE
            │                           │
     ┌──────┼──────┐          ┌────────┼────────┐
     │             │          │        │        │
  Sales         Sales       DM       DL      MOH
  Price        Volume     Variance Variance Variance
  Var          Var          │        │        │
                         ┌──┴──┐  ┌──┴──┐  ┌──┴──┐
                         Price Qty Rate Eff Spend Vol
                         Var   Var Var  Var Var   Var
```

### 2. Direct Materials Variance (Chênh lệch NVL trực tiếp)

$$\text{Total DM Variance} = \text{Actual Cost} - \text{Standard Cost for Actual Output}$$

**Chia thành 2 thành phần:**

$$\text{DM Price Variance} = (\text{AP} - \text{SP}) \times \text{AQ}$$

$$\text{DM Quantity Variance} = (\text{AQ} - \text{SQ}) \times \text{SP}$$

Trong đó:
- AP = Actual Price (Giá mua thực tế)
- SP = Standard Price (Giá mua tiêu chuẩn)
- AQ = Actual Quantity (Lượng sử dụng thực tế)
- SQ = Standard Quantity allowed for actual output

**Ví dụ chi tiết:**

Sản xuất 1,000 áo thun trong tháng:

| | Tiêu chuẩn (Standard) | Thực tế (Actual) |
|---|----------------------|-----------------|
| Lượng vải/áo | 1.2m | 1.35m (tổng: 1,350m) |
| Giá vải/m | 50,000 | 48,000 |
| SQ allowed | 1,000 × 1.2m = 1,200m | – |

$$\text{Price Variance} = (48,000 - 50,000) \times 1,350 = \textbf{-2,700,000 (F)}$$

→ Mua rẻ hơn 2k/m → Favorable

$$\text{Quantity Variance} = (1,350 - 1,200) \times 50,000 = \textbf{+7,500,000 (U)}$$

→ Dùng nhiều hơn 150m → Unfavorable

$$\text{Total DM Variance} = -2,700,000 + 7,500,000 = \textbf{+4,800,000 (U)}$$

**Sơ đồ phân tích:**

```
       AQ × AP              AQ × SP              SQ × SP
      (Actual Cost)    (Actual Qty @ Std Price)  (Standard Cost)
       1,350 × 48k          1,350 × 50k          1,200 × 50k
       = 64,800,000         = 67,500,000         = 60,000,000
            │                     │                    │
            ├─────────────────────┤                    │
            │  Price Variance     │                    │
            │  = -2.7tr (F)       │                    │
            │                     ├────────────────────┤
            │                     │  Quantity Variance  │
            │                     │  = +7.5tr (U)       │
            │                     │                    │
            ├──────────────────────────────────────────┤
            │          Total DM Variance               │
            │          = +4.8tr (U)                     │
```

**Nguyên nhân có thể:**

| Variance | Favorable | Unfavorable |
|----------|----------|-------------|
| **Price** | Đàm phán giá tốt, mua sỉ | NVL tăng giá, khan hiếm |
|  | Đổi nhà cung cấp rẻ hơn | Mua gấp, không có deal |
|  | Seasonal discount | Nhà cung cấp thay đổi chính sách |
| **Quantity** | Thợ lành nghề, ít phế phẩm | Thợ mới, chất lượng NVL kém |
|  | Cải tiến quy trình | Máy cũ, hao phí nhiều |
|  | NVL chất lượng cao hơn | Thiết kế phức tạp hơn dự kiến |

**⚠️ LƯU Ý:** Price Favorable + Quantity Unfavorable có thể liên quan: Mua vải rẻ hơn → chất lượng kém → hao phí nhiều hơn. **Phải phân tích CẶP, không tách rời!**

### 3. Direct Labor Variance (Chênh lệch nhân công)

$$\text{DL Rate Variance} = (\text{AR} - \text{SR}) \times \text{AH}$$

$$\text{DL Efficiency Variance} = (\text{AH} - \text{SH}) \times \text{SR}$$

Trong đó:
- AR = Actual Rate (Lương thực tế/giờ)
- SR = Standard Rate (Lương tiêu chuẩn/giờ)
- AH = Actual Hours (Giờ làm thực tế)
- SH = Standard Hours allowed for actual output

**Ví dụ (tiếp tục 1,000 áo thun):**

| | Standard | Actual |
|---|---------|--------|
| Giờ/áo | 1.7h | 1.9h (tổng: 1,900h) |
| Lương/giờ | 40,000 | 42,000 |
| SH allowed | 1,000 × 1.7 = 1,700h | – |

$$\text{Rate Var} = (42k - 40k) \times 1,900 = \textbf{+3,800,000 (U)}$$

$$\text{Efficiency Var} = (1,900 - 1,700) \times 40k = \textbf{+8,000,000 (U)}$$

**Giải thích:**
- Rate U: Trả lương cao hơn → thuê thợ lành nghề hơn? Overtime? Tăng lương?
- Efficiency U: Làm chậm hơn → thợ mới chưa quen? Máy hỏng? NVL kém?

### 4. Manufacturing Overhead Variance (Chênh lệch chi phí SX chung)

**Chia thành Variable MOH và Fixed MOH:**

#### Variable MOH Variance

$$\text{Variable MOH Spending Var} = \text{Actual VOH} - (\text{AH} \times \text{SRate}_\text{var})$$

$$\text{Variable MOH Efficiency Var} = (\text{AH} - \text{SH}) \times \text{SRate}_\text{var}$$

#### Fixed MOH Variance

$$\text{Fixed MOH Budget Var} = \text{Actual FOH} - \text{Budgeted FOH}$$

$$\text{Fixed MOH Volume Var} = \text{Budgeted FOH} - \text{Applied FOH}$$

$$\text{Applied FOH} = \text{SH}_\text{allowed} \times \text{FOH Rate}$$

**Ví dụ:**

| | Budget | Actual |
|---|-------|--------|
| Variable MOH rate | 15,000/DLH | – |
| Actual Variable MOH | – | 30,000,000 |
| Budgeted Fixed MOH | 40,000,000 | 42,000,000 |
| Budgeted output | 1,200 áo | 1,000 áo (actual) |
| FOH Rate | 40,000,000 / (1,200×1.7h) = 19,608/DLH | – |

$$\text{VOH Spending} = 30,000,000 - (1,900 \times 15,000) = 30tr - 28.5tr = \textbf{+1.5tr (U)}$$

$$\text{VOH Efficiency} = (1,900 - 1,700) \times 15,000 = \textbf{+3.0tr (U)}$$

$$\text{FOH Budget} = 42,000,000 - 40,000,000 = \textbf{+2.0tr (U)}$$

$$\text{FOH Volume} = 40,000,000 - (1,700 \times 19,608) = 40tr - 33.3tr = \textbf{+6.7tr (U)}$$

→ Volume Variance (U) = Sản xuất ít hơn capacity → Fixed cost spread trên ít sản phẩm hơn

### 5. Sales Variance (Chênh lệch doanh thu)

$$\text{Sales Price Var} = (\text{Actual Price} - \text{Budgeted Price}) \times \text{Actual Qty}$$

$$\text{Sales Volume Var} = (\text{Actual Qty} - \text{Budgeted Qty}) \times \text{Budgeted CM/unit}$$

**Ví dụ:**

| | Budget | Actual |
|---|-------|--------|
| Giá bán/áo | 350,000 | 330,000 |
| Số lượng bán | 1,200 | 1,000 |
| CM/unit (budgeted) | 158,500 | – |

$$\text{Price Var} = (330k - 350k) \times 1,000 = \textbf{-20,000,000 (U)}$$

$$\text{Volume Var} = (1,000 - 1,200) \times 158.5k = \textbf{-31,700,000 (U)}$$

→ Bán GIÁ THẤP hơn VÀ SỐ LƯỢNG ÍT hơn → Double hit!

---

## III. BẢNG TỔNG HỢP VARIANCE

### Ví dụ tổng hợp (Công ty áo thun)

```
┌──────────────────────────────────────────────────────────┐
│     VARIANCE ANALYSIS REPORT – THÁNG XX/20XX             │
│     Sản phẩm: Áo thun | Output: 1,000 cái               │
│                                                            │
│  VARIANCE              AMOUNT        STATUS   PRIORITY    │
│  ──────────────────────────────────────────────────────    │
│  Sales Price            (20.0)tr       (U)      🔴        │
│  Sales Volume           (31.7)tr       (U)      🔴        │
│  ──────────────────────────────────────────────────────    │
│  DM Price                (2.7)tr        F       🟢        │
│  DM Quantity             +7.5 tr       (U)      🔴        │
│  DL Rate                 +3.8 tr       (U)      🟡        │
│  DL Efficiency           +8.0 tr       (U)      🔴        │
│  VOH Spending            +1.5 tr       (U)      🟡        │
│  VOH Efficiency          +3.0 tr       (U)      🟡        │
│  FOH Budget              +2.0 tr       (U)      🟡        │
│  FOH Volume              +6.7 tr       (U)      🔴        │
│  ──────────────────────────────────────────────────────    │
│  TOTAL VARIANCE          +49.0 tr      (U)      🔴🔴     │
│                                                            │
│  🔴 = Investigate immediately                             │
│  🟡 = Monitor closely                                     │
│  🟢 = Positive, but verify sustainability                 │
└──────────────────────────────────────────────────────────┘
```

---

## IV. FRAMEWORK PHÂN TÍCH NGUYÊN NHÂN

### 1. Quy trình điều tra Variance

```
  Bước 1: Xác định variance có significant không?
       │   Rule of thumb: > 5% hoặc > X triệu
       │
  Bước 2: Favorable hay Unfavorable?
       │
  Bước 3: Root Cause Analysis (5 Whys)
       │   Why? → Why? → Why? → Why? → Why?
       │
  Bước 4: Controllable hay Uncontrollable?
       │   - Controllable: Manager có thể fix
       │   - Uncontrollable: Thị trường, thiên tai
       │
  Bước 5: Corrective Action
       │
  Bước 6: Update Standard nếu cần
```

### 2. Ma trận nguyên nhân Variance

| Variance | Nguyên nhân Controllable | Nguyên nhân Uncontrollable |
|----------|------------------------|--------------------------|
| **DM Price (U)** | Mua ngoài deal, không tender | Giá nguyên liệu thế giới tăng |
| **DM Qty (U)** | Thợ tay nghề kém, machine setup sai | NVL chất lượng kém đợt này |
| **DL Rate (U)** | OT nhiều, thuê thợ đắt hơn | Tăng lương tối thiểu vùng |
| **DL Eff (U)** | Training không đủ, workflow sai | Mất điện, máy hỏng |
| **Sales Price (U)** | Discount nhiều, sales push volume | Đối thủ giảm giá, chiến tranh giá |
| **Sales Vol (U)** | Marketing yếu, salesforce kém | Suy thoái kinh tế, mùa thấp điểm |
| **FOH Volume (U)** | Kế hoạch sản xuất kém | Đơn hàng giảm đột ngột |

### 3. Ví dụ 5-Why Analysis

**Variance:** DM Quantity Unfavorable (+7.5 triệu)

```
  Why 1: Tại sao dùng nhiều vải hơn standard?
  → Tỷ lệ phế phẩm tăng từ 5% lên 15%

  Why 2: Tại sao phế phẩm tăng?
  → Máy cắt bị lệch, cắt sai kích thước

  Why 3: Tại sao máy cắt lệch?
  → Lưỡi dao cũ, chưa được thay đúng lịch

  Why 4: Tại sao chưa thay lưỡi dao?
  → Không có lịch bảo trì định kỳ (preventive maintenance)

  Why 5: Tại sao không có lịch bảo trì?
  → Quản đốc mới chưa được training về SOP bảo trì

  ROOT CAUSE: Thiếu training SOP cho quản đốc mới
  ACTION: Lập SOP bảo trì máy + training bắt buộc cho manager mới
```

### 4. Nguyên tắc Management by Exception

Không phải mọi variance đều cần điều tra. Áp dụng **Management by Exception**:

| Tiêu chí | Threshold | Hành động |
|----------|----------|----------|
| **Insignificant** | < 3% VÀ < 2 triệu | Bỏ qua |
| **Moderate** | 3-10% HOẶC 2-10 triệu | Monitor, report hàng tháng |
| **Significant** | > 10% HOẶC > 10 triệu | Điều tra ngay, corrective action |
| **Recurring** | Cùng variance 3+ tháng liên tiếp | Review standard, possible systemic issue |

---

## V. ƯU VÀ NHƯỢC ĐIỂM

### Ưu điểm

| Ưu điểm | Chi tiết |
|---------|---------|
| **Accountability** | Gắn trách nhiệm rõ ràng: Price var → Purchasing, Qty var → Production |
| **Early Warning** | Phát hiện vấn đề sớm trước khi tích lũy |
| **Continuous Improvement** | Tạo văn hóa so sánh & cải tiến |
| **Data-driven** | Quyết định dựa trên số liệu, không cảm tính |
| **Cost Control** | Kiểm soát chi phí chặt chẽ |
| **Performance Evaluation** | Đánh giá hiệu suất bộ phận/cá nhân |

### Nhược điểm

| Nhược điểm | Chi tiết |
|-----------|---------|
| **Backward-looking** | Phân tích SAU khi xảy ra, không ngăn ngừa |
| **Gaming** | Managers có thể set standard dễ → luôn favorable |
| **Blame culture** | Nếu dùng sai → tạo văn hóa đổ lỗi |
| **Standard outdated** | Standard cũ không phản ánh thực tế mới |
| **Ignore qualitative** | Chỉ thấy con số, không thấy root cause |
| **Short-term focus** | Tối ưu chi phí ngắn hạn, bỏ qua long-term (cắt R&D, training) |
| **Complexity** | Phân tích chi tiết tốn thời gian & effort |

---

## VI. HOÀN CẢNH VÀ MÔI TRƯỜNG ÁP DỤNG

### 1. Khi nào variance analysis hiệu quả nhất?

| Hoàn cảnh | Vì sao hiệu quả |
|----------|----------------|
| **Sản xuất lặp lại** | Standard cost dễ xác định, so sánh có ý nghĩa |
| **Chi phí chiếm tỷ trọng lớn** | Variance nhỏ % nhưng lớn về giá trị |
| **Nhiều yếu tố biến động** | Cần tracking giá NVL, năng suất, overhead |
| **DN đã có budget system** | Variance analysis bổ sung cho budgeting |
| **Cần kiểm soát chi phí chặt** | Startup cần optimize burn rate |

### 2. Khi nào KHÔNG nên quá focus vào variance?

| Hoàn cảnh | Vì sao |
|----------|--------|
| **Innovation/R&D** | Standard không có ý nghĩa cho sáng tạo |
| **Startup phase** | Chưa có đủ data lập standard |
| **Volatile market** | Standard lỗi thời nhanh |
| **Service business** | Khó standardize từng dịch vụ |

---

## VII. CASE STUDY THÀNH CÔNG

### Case Study: **Toyota – Variance Analysis trong Kaizen Culture**

**Bối cảnh:**
Toyota sử dụng variance analysis như một phần không thể tách rời của **Toyota Production System (TPS)** và triết lý **Kaizen** (cải tiến liên tục).

**Cách Toyota sử dụng Variance Analysis:**

| Khía cạnh | Cách làm | Khác biệt so với DN thường |
|----------|---------|---------------------------|
| **Tần suất** | Hàng ngày (daily variance report) | DN thường: hàng tháng/quý |
| **Mức chi tiết** | Từng dây chuyền, từng ca, từng công đoạn | DN thường: tổng nhà máy |
| **Ai phân tích** | Team leader + workers (genba = hiện trường) | DN thường: Kế toán |
| **Standard** | Ideal standard (mục tiêu cải tiến) | DN thường: Currently attainable |
| **Phản ứng** | Andon system: dừng dây chuyền ngay khi có variance | DN thường: đợi cuối tháng |
| **Văn hóa** | Variance = cơ hội cải tiến, không phải đổ lỗi | DN thường: tìm người chịu trách nhiệm |

**Ví dụ cụ thể – Nhà máy Toyota Tsutsumi:**

```
  Standard: Lắp ráp 1 xe mất 18.0 giờ nhân công (DL)
  
  Tuần 1: Actual = 18.3h → DL Efficiency Var = +0.3h (U)
  → Root cause: Bước gắn dashboard mất thêm 0.3h
  → Kaizen: Thiết kế jig mới
  
  Tuần 4: Actual = 17.8h → DL Efficiency Var = -0.2h (F)
  → Jig mới hiệu quả
  → CẬP NHẬT Standard: 18.0h → 17.8h
  
  Tuần 8: Actual = 17.5h → Tiếp tục Kaizen
  ...
  
  Sau 1 năm: Standard giảm từ 18.0h → 16.5h
  → Tiết kiệm 1.5h × 400,000 xe = 600,000 giờ/năm
```

**Kết quả:**
- Toyota duy trì **#1 quality ranking** toàn cầu
- Cost/car thấp hơn đối thủ 15-20% (dù lương Nhật cao)
- Idea suggestion system: 700,000+ ý tưởng/năm từ nhân viên

**Bài học:**
> Variance analysis hiệu quả nhất khi:
> 1. **Real-time** – Phân tích ngay, không đợi cuối tháng
> 2. **At the source** – Người trực tiếp sản xuất phân tích, không phải accountant
> 3. **Improvement, not blame** – Variance = cơ hội, không phải lỗi
> 4. **Update standards** – Standard phải evolve theo kaizen

---

## VIII. CASE STUDY THẤT BẠI

### Case Study: **General Motors (GM) – Variance Analysis tạo văn hóa đổ lỗi**

**Bối cảnh:**
Trước khi phá sản năm 2009, GM sử dụng variance analysis theo cách **phản tác dụng**, tạo ra văn hóa "hit the number" thay vì cải tiến thực sự.

**Vấn đề:**

| Sai lầm | Chi tiết | Hệ quả |
|--------|---------|--------|
| **Standards quá dễ** | Set standard dựa trên historical (kém), không phải best practice | Luôn "hit target" nhưng vẫn kém đối thủ |
| **Blame game** | Unfavorable → Managers bị penalty | Che giấu vấn đề thay vì fix |
| **Short-term fixes** | Để hit monthly variance targets → cắt giảm maintenance, training | Chất lượng giảm dần, reliability issues |
| **Volume variance obsession** | Focus sản xuất nhiều để spread fixed cost | Tồn kho phình to, bán phá giá, brand damage |
| **Silo analysis** | Mỗi bộ phận optimize cho mình | Purchasing mua NVL rẻ → Quality kém → Warranty cost tăng |

**Ví dụ Volume Variance Trap:**

```
  GM Logic:
  FOH Volume Variance (U) khi sản xuất < capacity
  → Giải pháp: Sản xuất THẬT NHIỀU để Volume Var = 0

  Reality:
  Sản xuất 500k xe       Nhu cầu chỉ 350k xe
  Volume Var: Favorable!  Tồn kho: 150k xe
                          ↓
                    Phải discount 20% để bán
                          ↓
                    Brand devaluation
                          ↓
                    Khách chờ giảm giá, không mua giá gốc
                          ↓
                    Revenue & Margin giảm liên tục
```

**So sánh GM vs Toyota:**

| | GM approach | Toyota approach |
|---|------------|----------------|
| Variance = | Vấn đề → tìm người chịu lỗi | Cơ hội → cải tiến quy trình |
| Standard = | Dễ đạt → comfortable | Khó → stretch target |
| Phản ứng khi (U) | Che giấu hoặc gaming | Andon: dừng & fix ngay |
| Volume | Sản xuất max → giảm unit cost | Sản xuất theo demand (pull system) |
| Kết quả | Phá sản 2009 | #1 toàn cầu |

**Bài học:**
> 1. **Variance analysis là công cụ cải tiến, không phải vũ khí đổ lỗi**
> 2. **Volume Variance Favorable ≠ Good** – Sản xuất thừa tạo vấn đề lớn hơn
> 3. **Standards must be challenging** – Standard dễ = complacency
> 4. **Holistic view** – Tối ưu cục bộ (local optimization) có thể harm toàn cục

---

## IX. ÁP DỤNG CHO SME VIỆT NAM

### 1. Template Variance Report đơn giản cho SME

```
┌──────────────────────────────────────────────────┐
│  VARIANCE REPORT THÁNG XX/20XX                    │
│  Sản phẩm: __________                             │
│                                                    │
│              Budget    Actual   Variance  Status   │
│  ──────────────────────────────────────────────── │
│  Doanh thu    ____     ____     ____      F/U     │
│  - COGS       ____     ____     ____      F/U     │
│    NVL        ____     ____     ____      F/U     │
│    Nhân công  ____     ____     ____      F/U     │
│    Overhead   ____     ____     ____      F/U     │
│  ──────────────────────────────────────────────── │
│  Lãi gộp      ____     ____     ____      F/U     │
│  - Sales exp  ____     ____     ____      F/U     │
│  - Admin exp  ____     ____     ____      F/U     │
│  ──────────────────────────────────────────────── │
│  Lợi nhuận    ____     ____     ____      F/U     │
│                                                    │
│  TOP 3 VARIANCE CẦN CHÚT:                         │
│  1. ______________ → Action: __________            │
│  2. ______________ → Action: __________            │
│  3. ______________ → Action: __________            │
└──────────────────────────────────────────────────┘
```

### 2. Quy trình đơn giản cho SME

| Bước | Hành động | Công cụ | Tần suất |
|------|----------|---------|---------|
| 1 | So sánh Doanh thu & Chi phí thực tế vs Budget | Excel/Google Sheets | Hàng tháng |
| 2 | Highlight variance > 10% hoặc > 5 triệu | Conditional formatting | Hàng tháng |
| 3 | Top 3 variance → Hỏi "Why?" 3 lần | Team meeting 30 phút | Hàng tháng |
| 4 | Ghi nhận action items | Notion/Trello | Hàng tháng |
| 5 | Follow up action items tháng sau | Review meeting | Hàng tháng |
| 6 | Update budget/forecast nếu cần | Quý review | Hàng quý |

### 3. Checklist Monthly Variance Review

| # | Check | Done? |
|---|-------|-------|
| 1 | So sánh Revenue: Actual vs Budget (theo sản phẩm/kênh) | ☐ |
| 2 | So sánh COGS: NVL, nhân công, overhead | ☐ |
| 3 | So sánh Operating Expenses: Marketing, Admin, IT | ☐ |
| 4 | Highlight top 3 largest variances | ☐ |
| 5 | Root cause analysis cho significant variances | ☐ |
| 6 | Assign corrective actions với deadline | ☐ |
| 7 | Follow up actions từ tháng trước | ☐ |
| 8 | Update rolling forecast nếu trend thay đổi | ☐ |

---

## X. CÔNG THỨC TỔNG HỢP

### Direct Materials

$$\text{DM Price Var} = (AP - SP) \times AQ$$

$$\text{DM Quantity Var} = (AQ - SQ) \times SP$$

### Direct Labor

$$\text{DL Rate Var} = (AR - SR) \times AH$$

$$\text{DL Efficiency Var} = (AH - SH) \times SR$$

### Variable Overhead

$$\text{VOH Spending Var} = \text{Actual VOH} - (AH \times \text{Standard VOH Rate})$$

$$\text{VOH Efficiency Var} = (AH - SH) \times \text{Standard VOH Rate}$$

### Fixed Overhead

$$\text{FOH Budget Var} = \text{Actual FOH} - \text{Budgeted FOH}$$

$$\text{FOH Volume Var} = \text{Budgeted FOH} - (\text{SH} \times \text{FOH Rate})$$

### Sales

$$\text{Sales Price Var} = (AP - BP) \times AQ$$

$$\text{Sales Volume Var} = (AQ - BQ) \times \text{Budgeted CM/unit}$$

---

## XI. TÀI LIỆU THAM KHẢO

1. **Horngren, Datar & Rajan** – "Cost Accounting" Ch. 7-8 (Flexible Budgets & Variances)
2. **Garrison, Noreen & Brewer** – "Managerial Accounting" Ch. 10-11
3. **Kaplan & Norton** – "The Balanced Scorecard" (beyond variance)
4. **Imai, Masaaki** – "Kaizen: The Key to Japan's Competitive Success"
5. **Womack & Jones** – "Lean Thinking" (Toyota's approach)
6. **CMA** – Part 1: Planning, Budgeting & Forecasting (variance analysis)
7. **Harvard Business Review** – "Stop Using Cost Variance Analysis" (critical view)