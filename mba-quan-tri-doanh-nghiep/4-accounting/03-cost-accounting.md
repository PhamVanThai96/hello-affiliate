# Cost Accounting – Kế Toán Chi Phí (ABC, Job Costing, Process Costing)

> **Mục tiêu**: Hiểu rõ 3 phương pháp tính giá thành sản phẩm/dịch vụ: Activity-Based Costing, Job Order Costing, Process Costing. So sánh, ưu nhược điểm, và ứng dụng cho SME Việt Nam.

---

## I. ĐỊNH NGHĨA VÀ LÝ THUYẾT NỀN TẢNG

### 1. Định nghĩa

**Cost Accounting (Kế toán chi phí)** là nhánh kế toán chuyên về **đo lường, phân tích, và phân bổ chi phí** vào sản phẩm, dịch vụ, dự án, hoặc bộ phận. Mục tiêu: **biết chính xác mỗi sản phẩm tốn bao nhiêu tiền** để định giá và ra quyết định.

> **"You can't manage what you can't measure."** – Peter Drucker

### 2. Tại sao Cost Accounting quan trọng?

| Lý do | Giải thích | Ví dụ |
|-------|-----------|-------|
| **Pricing** (Định giá) | Biết chi phí → Định giá hợp lý | Chi phí 100k → Bán 150k (margin 33%) |
| **Profitability** (Lợi nhuận) | Biết SP nào lãi/lỗ thực sự | SP A lãi 30%, SP B lỗ 5% |
| **Cost Control** (Kiểm soát) | Phát hiện chi phí bất thường | Chi phí NVL tăng 20% → điều tra |
| **Decision Making** (Ra QĐ) | Make-or-Buy, Accept/Reject | Outsource nếu chi phí nội bộ cao hơn |
| **Budgeting** (Ngân sách) | Lập ngân sách chính xác | Dự án mới cần bao nhiêu tiền? |

### 3. Sơ đồ tổng quan các phương pháp

```
              COST ACCOUNTING METHODS
                      │
     ┌────────────────┼────────────────┐
     │                │                │
┌────▼────┐     ┌─────▼─────┐    ┌────▼──────┐
│  JOB    │     │  PROCESS  │    │ ACTIVITY  │
│ COSTING │     │  COSTING  │    │  BASED    │
│         │     │           │    │ (ABC)     │
└────┬────┘     └─────┬─────┘    └────┬──────┘
     │                │               │
  Sản phẩm        Sản phẩm        Overhead
  đặt riêng       hàng loạt       allocation
  unique          identical        by activity

  Xây dựng       Nước giải khát   Cả hai loại
  In ấn          Xi măng          trên
  Tư vấn         Hóa chất
  Phần mềm       Giấy
```

---

## II. JOB ORDER COSTING – TÍNH GIÁ THEO ĐƠN ĐẶT HÀNG

### 1. Khái niệm

**Job Order Costing** tích lũy chi phí theo **từng đơn hàng (job/order) riêng biệt**. Mỗi job có tính duy nhất, khác biệt với job khác.

### 2. Đặc điểm

| Đặc điểm | Chi tiết |
|----------|---------|
| **Sản phẩm** | Đặt riêng, unique, khác nhau |
| **Tracking** | Theo từng job/lô cụ thể |
| **Chứng từ** | Job Cost Sheet cho mỗi đơn |
| **Chi phí gom** | DM + DL trực tiếp vào job, MOH phân bổ |

### 3. Quy trình Job Costing

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ Nhận đơn    │     │ Mở Job Cost │     │ Tập hợp     │
│ đặt hàng    │────►│ Sheet       │────►│ chi phí     │
│ (Job #101)  │     │             │     │             │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                                    ┌──────────┼──────────┐
                                    │          │          │
                              ┌─────▼───┐ ┌────▼────┐ ┌──▼─────┐
                              │Direct   │ │Direct   │ │Mfg     │
                              │Materials│ │Labor    │ │Overhead│
                              │(thực tế)│ │(thực tế)│ │(phân bổ│
                              └─────┬───┘ └────┬────┘ └──┬─────┘
                                    │          │          │
                              ┌─────▼──────────▼──────────▼──────┐
                              │         JOB COST SHEET           │
                              │  Job #101: Bàn gỗ tùy chỉnh     │
                              │                                   │
                              │  DM: Gỗ sồi 2m³ × 3tr = 6tr    │
                              │  DL: 40h × 80k/h = 3.2tr        │
                              │  MOH: 40h × 60k/h = 2.4tr       │
                              │  ─────────────────────────        │
                              │  Total Job Cost: 11.6 triệu      │
                              └──────────────────────────────────┘
```

### 4. Ví dụ chi tiết: Xưởng nội thất

**Công ty ABC Furniture nhận 2 đơn hàng tháng 3:**

| | Job #201 (Bàn họp 12 chỗ) | Job #202 (Kệ sách custom) |
|---|---------------------------|---------------------------|
| **Direct Materials** | | |
| - Gỗ | 8,000,000 | 3,000,000 |
| - Phụ kiện (ốc vít, keo) | 500,000 | 200,000 |
| **Direct Labor** | | |
| - Thợ mộc (hrs × rate) | 60h × 100k = 6,000,000 | 25h × 100k = 2,500,000 |
| - Thợ sơn | 15h × 80k = 1,200,000 | 8h × 80k = 640,000 |
| **MOH Applied** | | |
| Rate: 70k/DL hour | 75h × 70k = 5,250,000 | 33h × 70k = 2,310,000 |
| **TOTAL JOB COST** | **20,950,000** | **8,650,000** |
| Giá bán | 30,000,000 | 13,000,000 |
| **Gross Profit** | **9,050,000 (30.2%)** | **4,350,000 (33.5%)** |

### 5. Predetermined Overhead Rate (POHR)

Vì MOH thực tế chỉ biết cuối kỳ, ta dùng **tỷ lệ phân bổ ước tính**:

$$\text{POHR} = \frac{\text{Estimated Total MOH}}{\text{Estimated Total Allocation Base}}$$

**Allocation Base phổ biến:**

| Base | Công thức | Phù hợp khi |
|------|----------|-------------|
| Direct Labor Hours | MOH / Total DL hours | Labor-intensive |
| Machine Hours | MOH / Total machine hours | Capital-intensive |
| Direct Labor Cost | MOH / Total DL cost | Đơn giản |
| Units Produced | MOH / Total units | Sản phẩm đồng nhất |

**Under/Over-applied Overhead:**

$$\text{Applied MOH} = \text{POHR} \times \text{Actual Activity}$$

- **Under-applied**: Applied < Actual → Chi phí thực tế cao hơn → Tăng COGS
- **Over-applied**: Applied > Actual → Chi phí thực tế thấp hơn → Giảm COGS

---

## III. PROCESS COSTING – TÍNH GIÁ THEO QUY TRÌNH

### 1. Khái niệm

**Process Costing** tích lũy chi phí theo **quy trình/công đoạn sản xuất**, sau đó chia đều cho tất cả sản phẩm. Phù hợp cho **sản xuất hàng loạt, sản phẩm đồng nhất**.

### 2. Đặc điểm

| Đặc điểm | Chi tiết |
|----------|---------|
| **Sản phẩm** | Đồng nhất, sản xuất liên tục |
| **Tracking** | Theo department/process |
| **Đơn vị tính** | Equivalent Units (đơn vị quy đổi tương đương) |
| **Dòng chi phí** | Process 1 → Process 2 → ... → Thành phẩm |

### 3. Equivalent Units (Đơn vị tương đương)

**Vấn đề**: Cuối kỳ có sản phẩm dở dang (Work-in-Process). Cần quy đổi về đơn vị hoàn thành tương đương.

$$\text{Equivalent Units} = \text{Units Completed} + (\text{WIP Ending} \times \text{\% Completion})$$

**Ví dụ:** Cuối tháng: 800 SP hoàn thành + 200 SP dở dang (hoàn thành 60%)

$$\text{EU} = 800 + (200 \times 60\%) = 800 + 120 = 920 \text{ EU}$$

### 4. Hai phương pháp Process Costing

| | Weighted Average (BQGQ) | FIFO |
|---|------------------------|------|
| **Nguyên tắc** | Gộp chi phí đầu kỳ + phát sinh | Tách riêng chi phí đầu kỳ & phát sinh |
| **EU tính** | EU = Completed + WIP End × %Done | EU = hoàn thành WIP đầu kỳ + Started & completed + WIP cuối kỳ |
| **Đơn giản** | ✅ Dễ hơn | ❌ Phức tạp hơn |
| **Chính xác** | Ít chính xác khi giá đầu vào biến động | ✅ Chính xác hơn |
| **Phổ biến** | Rất phổ biến | Ít phổ biến hơn |

### 5. Ví dụ chi tiết: Nhà máy sản xuất nước mắm

**Quy trình sản xuất:**

```
  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
  │ Process 1│    │ Process 2│    │ Process 3│    │ Process 4│
  │ Ngâm ủ   │───►│ Lọc      │───►│ Pha chế  │───►│ Đóng chai│
  │ (6 tháng)│    │          │    │          │    │          │
  └──────────┘    └──────────┘    └──────────┘    └──────────┘
```

**Process 3 – Pha chế (tháng 6):**

| Dữ liệu | Số liệu |
|----------|---------|
| WIP đầu kỳ | 500 lít (80% hoàn thành) |
| Bắt đầu sản xuất trong kỳ | 4,000 lít |
| Hoàn thành & chuyển sang P4 | 3,500 lít |
| WIP cuối kỳ | 1,000 lít (40% hoàn thành) |

**Tính Equivalent Units (Weighted Average):**

$$\text{EU}_\text{materials} = 3,500 + (1,000 \times 40\%) = 3,900 \text{ EU}$$

| Chi phí | Số tiền | EU | Cost/EU |
|---------|---------|----|----|
| NVL (từ đầu kỳ + phát sinh) | 78,000,000 | 3,900 | 20,000/lít |
| Nhân công + MOH | 58,500,000 | 3,900 | 15,000/lít |
| **Tổng** | **136,500,000** | | **35,000/lít** |

**Phân bổ chi phí:**

| | Số tiền |
|---|--------|
| Chi phí SP hoàn thành: 3,500 × 35,000 | 122,500,000 |
| Chi phí WIP cuối kỳ: 400 EU × 35,000 | 14,000,000 |
| **Tổng** | **136,500,000** ✓ |

---

## IV. ACTIVITY-BASED COSTING (ABC) – TÍNH GIÁ THEO HOẠT ĐỘNG

### 1. Khái niệm

**ABC (Activity-Based Costing)** phân bổ chi phí gián tiếp (overhead) dựa trên **hoạt động thực tế** gây ra chi phí, thay vì dùng một base duy nhất (như giờ máy hay giờ lao động).

> **"Products consume activities, activities consume resources."** – Robin Cooper & Robert Kaplan (1988)

### 2. Tại sao cần ABC?

**Hạn chế của Traditional Costing:**

```
  TRADITIONAL COSTING                    ABC
  
  Overhead $500k                        Overhead $500k
       │                                     │
       │ (1 base: machine hours)        ┌────┼────┐────────┐
       │                                │    │    │        │
  ┌────▼────┐ ┌────────┐          ┌─────▼─┐ ┌▼──┐ ┌▼────┐ ┌▼────┐
  │Product A│ │Product B│          │Setup  │ │QC │ │Ship │ │Maint│
  │  $250k  │ │  $250k  │          │$150k  │ │$100│ │$150k│ │$100k│
  └─────────┘ └────────┘          └───┬───┘ └─┬─┘ └──┬──┘ └──┬──┘
                                      │       │      │       │
  → Cùng giá?                    # setups  # tests # orders # hrs
  → KHÔNG chính xác!                 │       │      │       │
                                 Phân bổ theo activity driver thực tế
                                 → Product A: $180k
                                 → Product B: $320k
                                 → CHÍNH XÁC hơn!
```

### 3. Quy trình ABC

```
  Bước 1: Xác định HOẠT ĐỘNG (Activities)
       │   Setup máy, Kiểm tra chất lượng, Giao hàng, Bảo trì
       │
  Bước 2: Xác định CHI PHÍ cho mỗi hoạt động (Activity Cost Pool)
       │   Setup: 150 triệu, QC: 100 triệu, Shipping: 150 triệu
       │
  Bước 3: Xác định COST DRIVER (Yếu tố thúc đẩy chi phí)
       │   Setup: Số lần setup, QC: Số lần kiểm tra, Shipping: Số đơn hàng
       │
  Bước 4: Tính ACTIVITY RATE
       │   Rate = Activity Cost Pool / Total Cost Driver
       │
  Bước 5: PHÂN BỔ chi phí cho sản phẩm
           Cost = Activity Rate × Cost Driver consumed by product
```

### 4. Ví dụ chi tiết: So sánh Traditional vs ABC

**Công ty sản xuất bánh (2 sản phẩm):**

| Thông tin | Bánh A (Hàng loạt) | Bánh B (Đặt riêng) | Tổng |
|----------|-------------------|-------------------|------|
| Sản lượng | 10,000 cái | 2,000 cái | 12,000 |
| Giờ máy | 5,000 h | 1,000 h | 6,000 h |
| Số lần setup | 10 lần | 40 lần | 50 |
| Số lần kiểm tra QC | 20 lần | 60 lần | 80 |
| Số đơn giao hàng | 50 đơn | 150 đơn | 200 |

**Tổng MOH: 500 triệu VNĐ**

#### Traditional Costing (Base: Machine Hours)

$$\text{POHR} = \frac{500,000,000}{6,000 \text{h}} = 83,333 \text{ VNĐ/h}$$

| | Bánh A | Bánh B |
|---|--------|--------|
| MOH Applied | 5,000h × 83,333 = **416.7 triệu** | 1,000h × 83,333 = **83.3 triệu** |
| MOH/unit | **41,667 VNĐ** | **41,667 VNĐ** |

→ Cùng chi phí/unit? **Không hợp lý!** Bánh B phức tạp hơn nhiều.

#### ABC (Activity-Based Costing)

**Bước 1-3: Xác định activities & cost drivers**

| Activity | Cost Pool | Cost Driver | Total Driver |
|----------|----------|-------------|-------------|
| Setup máy | 150,000,000 | Số lần setup | 50 lần |
| Kiểm tra QC | 100,000,000 | Số lần kiểm tra | 80 lần |
| Giao hàng | 150,000,000 | Số đơn giao | 200 đơn |
| Bảo trì máy | 100,000,000 | Giờ máy | 6,000 h |

**Bước 4: Tính Activity Rate**

| Activity | Rate |
|----------|------|
| Setup | 150,000,000 / 50 = **3,000,000/lần** |
| QC | 100,000,000 / 80 = **1,250,000/lần** |
| Giao hàng | 150,000,000 / 200 = **750,000/đơn** |
| Bảo trì | 100,000,000 / 6,000 = **16,667/h** |

**Bước 5: Phân bổ**

| Activity | Bánh A | Bánh B |
|----------|--------|--------|
| Setup | 10 × 3,000,000 = 30,000,000 | 40 × 3,000,000 = 120,000,000 |
| QC | 20 × 1,250,000 = 25,000,000 | 60 × 1,250,000 = 75,000,000 |
| Giao hàng | 50 × 750,000 = 37,500,000 | 150 × 750,000 = 112,500,000 |
| Bảo trì | 5,000 × 16,667 = 83,333,000 | 1,000 × 16,667 = 16,667,000 |
| **Total MOH** | **175,833,000** | **324,167,000** |
| **MOH/unit** | **17,583 VNĐ** | **162,084 VNĐ** |

### 5. So sánh kết quả

| | Traditional | ABC | Chênh lệch |
|---|------------|-----|-----------|
| **Bánh A** (MOH/unit) | 41,667 | **17,583** | Traditional cao hơn **137%** |
| **Bánh B** (MOH/unit) | 41,667 | **162,084** | Traditional thấp hơn **74%** |

```
  MOH/unit (VNĐ)
  180k ─┤                           ████  ABC Bánh B
       │                           ████  (162k)
  160k ─┤                           ████
       │                           ████
       │                           ████
       │                           ████
       │                           ████
       │                           ████
       │                           ████
       │                           ████
       │                           ████
   40k ─┤  ████ ████                ████
       │  ████ ████  Traditional   ████
   20k ─┤  ████ ████  (41.7k both) ████  ABC Bánh A
       │  ████ ████                ████  (17.6k)
       └──┴────┴────┴───────────────┴────┴──── 
         Bánh A Bánh B             Bánh A Bánh B
           TRADITIONAL                ABC
```

**Insight:**
- Traditional: **Trợ giá chéo** (cross-subsidization) – Bánh A gánh chi phí cho Bánh B
- ABC: Bánh B thực tế tốn kém gấp **9 lần** Bánh A → cần định giá cao hơn hoặc tối ưu quy trình

---

## V. SO SÁNH 3 PHƯƠNG PHÁP

### Bảng so sánh toàn diện

| Tiêu chí | Job Order Costing | Process Costing | ABC |
|----------|------------------|----------------|-----|
| **Sản phẩm** | Đặt riêng, unique | Đồng nhất, hàng loạt | Cả hai |
| **Đơn vị tracking** | Từng job/order | Từng department/process | Từng activity |
| **Overhead allocation** | POHR × 1 base | POHR × 1 base | Nhiều activity rates |
| **Độ chính xác** | Trung bình | Thấp nhất | Cao nhất |
| **Phức tạp** | Trung bình | Thấp | Cao |
| **Chi phí triển khai** | Thấp-TB | Thấp | Cao |
| **Ngành phù hợp** | Xây dựng, In ấn, Tư vấn, Phần mềm | Thực phẩm, Hóa chất, Xi măng, Dệt may | Đa sản phẩm, Overhead cao |
| **SME áp dụng** | ⭐⭐⭐ Dễ | ⭐⭐⭐ Dễ | ⭐⭐ Vừa |
| **Khi nào dùng** | SP khác nhau, chi phí khác nhiều | SP giống nhau, sản xuất liên tục | Cần chính xác overhead |

### Sơ đồ quyết định chọn phương pháp

```
            Sản phẩm của bạn?
                  │
          ┌───────┴───────┐
          │               │
    Đặt riêng /      Đồng nhất /
    Unique           Hàng loạt
          │               │
          ▼               ▼
   JOB COSTING      PROCESS COSTING
          │               │
          └───────┬───────┘
                  │
          Overhead chiếm >30%
          tổng chi phí?
                  │
            ┌─────┴─────┐
            │           │
          Không         Có
            │           │
            ▼           ▼
     Giữ nguyên    Kết hợp ABC
     Traditional   để phân bổ
                   overhead
                   chính xác hơn
```

---

## VI. ƯU VÀ NHƯỢC ĐIỂM TỪNG PHƯƠNG PHÁP

### Job Order Costing

| Ưu điểm | Nhược điểm |
|---------|-----------|
| ✅ Biết chi phí từng đơn hàng cụ thể | ❌ Tốn thời gian tracking mỗi job |
| ✅ Dễ kiểm soát giá thành từng job | ❌ POHR có thể không chính xác |
| ✅ Hỗ trợ định giá & báo giá | ❌ Không phù hợp sản xuất hàng loạt |
| ✅ Phát hiện job lỗ nhanh | ❌ Phụ thuộc ước tính POHR |

### Process Costing

| Ưu điểm | Nhược điểm |
|---------|-----------|
| ✅ Đơn giản, dễ áp dụng cho mass production | ❌ Không thấy chi phí từng đơn hàng |
| ✅ Chi phí triển khai thấp | ❌ Equivalent Units có thể không chính xác |
| ✅ Phù hợp sản xuất liên tục | ❌ Khó kiểm soát chi phí ở từng SP |
| ✅ Dễ tính giá thành đơn vị | ❌ Giả định mọi SP đều giống nhau |

### Activity-Based Costing (ABC)

| Ưu điểm | Nhược điểm |
|---------|-----------|
| ✅ Chính xác nhất – phản ánh thực tế | ❌ Phức tạp, tốn thời gian & chi phí triển khai |
| ✅ Phát hiện cross-subsidization | ❌ Cần nhiều dữ liệu hoạt động |
| ✅ Hỗ trợ quyết định chiến lược | ❌ Chủ quan trong chọn cost drivers |
| ✅ Cải thiện process & loại bỏ lãng phí | ❌ Kháng cự từ nhân viên (thay đổi) |
| ✅ Phù hợp service & manufacturing | ❌ Overkill cho DN nhỏ, ít sản phẩm |

---

## VII. HOÀN CẢNH VÀ MÔI TRƯỜNG ÁP DỤNG

### 1. Theo ngành nghề

| Ngành | Phương pháp phù hợp | Lý do |
|-------|---------------------|-------|
| **Xây dựng** | Job Costing | Mỗi công trình là 1 job riêng |
| **In ấn** | Job Costing | Mỗi đơn in khác nhau |
| **Phát triển phần mềm** | Job Costing | Mỗi dự án khác nhau |
| **Tư vấn / Agency** | Job Costing | Mỗi client project riêng |
| **Thực phẩm & đồ uống** | Process Costing | Sản xuất hàng loạt |
| **Hóa chất** | Process Costing | Sản xuất liên tục |
| **Dệt may** | Process + Job | Hàng loạt + đơn đặt riêng |
| **Ngân hàng / Bảo hiểm** | ABC | Nhiều service, overhead cao |
| **Bệnh viện** | ABC | Chi phí gián tiếp chiếm tỷ lệ lớn |
| **E-commerce** | ABC | Cần biết cost per order chi tiết |

### 2. Theo giai đoạn phát triển DN

```
  Startup ──────► Tăng trưởng ──────► Trưởng thành
     │                │                    │
  Excel đơn giản    Job/Process         ABC full
  Biến phí/SP       + POHR              + Time-Driven ABC
  CM/unit           + Budget variance    + Target Costing
                                         + Kaizen Costing
```

### 3. Khi nào KHÔNG nên dùng ABC?

| Tình huống | Lý do |
|-----------|-------|
| DN nhỏ, 1-2 sản phẩm | Overhead phân bổ đơn giản, ABC không add value |
| Overhead chiếm < 10% tổng chi phí | Chênh lệch traditional vs ABC không đáng kể |
| Không có dữ liệu hoạt động | Không thể xác định cost drivers |
| Văn hóa DN kháng cự thay đổi | Triển khai thất bại nếu không có buy-in |

---

## VIII. CASE STUDY THÀNH CÔNG

### Case Study: **Hewlett-Packard (HP) – ABC cứu dòng máy in**

**Bối cảnh:**
Những năm 1990, HP phát hiện dòng máy in nhỏ (InkJet) bị traditional costing đánh giá là **rất lãi**, trong khi máy in lớn (LaserJet) bị đánh giá **ít lãi**. Nhưng thực tế không phải vậy.

**Vấn đề với Traditional Costing:**
- Overhead phân bổ theo DL hours
- InkJet: ít giờ lao động trực tiếp → overhead thấp → "rất lãi"
- LaserJet: nhiều giờ lao động → overhead cao → "ít lãi"

**Triển khai ABC:**

| Activity | InkJet (Traditional) | InkJet (ABC) | LaserJet (Traditional) | LaserJet (ABC) |
|----------|---------------------|-------------|----------------------|---------------|
| Procurement | Thấp | **Cao** (nhiều đơn nhỏ) | Cao | **Trung bình** |
| Quality Testing | Thấp | **Cao** (tỷ lệ lỗi cao) | Cao | **Thấp** |
| Customer Support | Thấp | **Rất cao** (nhiều claim) | Cao | **Thấp** |
| Shipping | Thấp | **Cao** (nhiều đơn lẻ) | Cao | **Trung bình** |

**Kết quả ABC:**
- InkJet: Lợi nhuận thực tế **thấp hơn 30%** so với traditional
- LaserJet: Lợi nhuận thực tế **cao hơn 25%** so với traditional

**Hành động:**
1. Tái thiết kế InkJet giảm chi phí hỗ trợ khách hàng
2. Tối ưu procurement cho InkJet (gom đơn mua lớn)
3. Đầu tư thêm vào LaserJet (vì lãi thực cao hơn)
4. Định giá lại InkJet cartridge (strategy chuyển margin sang consumables)

**Bài học:**
> ABC phá vỡ ảo tưởng lợi nhuận do cross-subsidization. **Sản phẩm "đơn giản" chưa chắc rẻ, sản phẩm "phức tạp" chưa chắc đắt nếu quy trình đã tối ưu.**

---

## IX. CASE STUDY THẤT BẠI

### Case Study: **Một chuỗi nhà hàng Việt Nam – Không biết chi phí thực, mở rộng quá nhanh**

**Bối cảnh:**
Chuỗi nhà hàng "TasteVN" (tên đã thay đổi) có 3 chi nhánh tại TP.HCM, quyết định mở thêm 5 chi nhánh trong 1 năm dựa trên financial accounting cho thấy "tổng thể có lãi".

**Vấn đề: thiếu Cost Accounting chi tiết**

| Yếu tố | Biết | Không biết |
|--------|------|-----------|
| Tổng doanh thu | ✅ | – |
| Tổng chi phí | ✅ | – |
| Chi phí / món ăn | ❌ | Food cost % từng món |
| Chi phí / chi nhánh | ❌ | Lãi/lỗ từng location |
| Chi phí delivery vs dine-in | ❌ | P&L theo kênh |

**Thực tế khi phân tích (có tư vấn sau này):**

| Chi nhánh | Doanh thu | Food Cost | Labor | Rent | Other | Profit |
|----------|-----------|-----------|-------|------|-------|--------|
| Q1 (trung tâm) | 500tr | 35% | 25% | 20% | 10% | **+50tr (10%)** |
| Q7 (residential) | 300tr | 33% | 28% | 15% | 12% | **+36tr (12%)** |
| Thủ Đức (mới mở) | 200tr | 40% | 30% | 18% | 15% | **-6tr (-3%)** |

**Và khi phân tích menu (ABC approach):**

| Nhóm món | Doanh thu % | Food cost % | CM % | Verdict |
|----------|------------|-------------|------|---------|
| Món Việt truyền thống | 40% | 28% | **72%** | ⭐ Star – Keep & promote |
| Món Âu fusion | 30% | 45% | **55%** | ⚠️ Cần tối ưu NVL |
| Đồ uống | 20% | 18% | **82%** | ⭐⭐ Cash cow |
| Tráng miệng | 10% | 50% | **50%** | ❌ Xem xét cắt giảm |

**Hệ quả:**
- Mở 5 chi nhánh mới, 3 chi nhánh lỗ nặng (vì nhân rộng mô hình chưa tối ưu)
- Food cost tăng do không control từng món
- Phải đóng 2 chi nhánh sau 18 tháng, mất ~3 tỷ VNĐ

**Bài học:**
> 1. **Biết "tổng thể có lãi" chưa đủ** – Cần biết lãi/lỗ theo chi nhánh, theo sản phẩm, theo kênh
> 2. **Cost Accounting là tiền đề của scaling** – Nhân rộng mô hình chưa tối ưu = nhân rộng lỗ
> 3. **ABC cho F&B**: Phân tích food cost + labor cost + overhead theo từng nhóm món
> 4. **Menu Engineering**: Kết hợp popularity × profitability để tối ưu menu

---

## X. PHƯƠNG PHÁP NÂNG CAO

### 1. Target Costing (Tính giá mục tiêu)

$$\text{Target Cost} = \text{Target Price} - \text{Target Profit}$$

→ Thiết kế sản phẩm **ngược**: Từ giá thị trường → trừ lợi nhuận mong muốn → ra chi phí tối đa → thiết kế sản phẩm trong chi phí đó

**Ví dụ:** Thị trường chấp nhận giá 300k, muốn margin 30% → Target cost = 300k × 70% = 210k → Thiết kế sản phẩm chi phí ≤ 210k

### 2. Kaizen Costing (Cải tiến liên tục)

- Áp dụng **sau** khi sản phẩm đã sản xuất
- Mỗi kỳ đặt mục tiêu **giảm chi phí** so với kỳ trước
- Kết hợp với Lean Manufacturing

### 3. Life-Cycle Costing

- Tính chi phí **toàn bộ vòng đời** sản phẩm: R&D → Production → Distribution → After-sales → Disposal
- 80% chi phí được "khóa" ở giai đoạn thiết kế

### 4. Time-Driven ABC (TDABC)

- Đơn giản hóa ABC bằng cách dùng **thời gian** làm cost driver duy nhất
- Ước tính thời gian cho mỗi hoạt động thay vì surveys phức tạp
- Phù hợp cho SME muốn ABC nhưng không có nhiều resources

$$\text{Cost per unit of time} = \frac{\text{Total department cost}}{\text{Practical capacity (minutes)}}$$

$$\text{Activity cost} = \text{Time per activity} \times \text{Cost per minute}$$

---

## XI. TÀI LIỆU THAM KHẢO

1. **Horngren, Datar & Rajan** – "Cost Accounting: A Managerial Emphasis" 16th Ed
2. **Kaplan & Cooper** – "Cost and Effect: Using Integrated Cost Systems" (ABC bible)
3. **Kaplan & Anderson** – "Time-Driven Activity-Based Costing" (TDABC)
4. **Hilton & Platt** – "Managerial Accounting: Creating Value in a Dynamic Business Environment"
5. **CMA (IMA)** – Part 1: Financial Planning, Performance, and Analytics
6. **CIMA** – Management Accounting study materials
7. **Toyota** – Target Costing & Kaizen Costing practices
8. **Hewlett-Packard case study** – "How ABC Transformed HP's Costing System" (Harvard Business Review)