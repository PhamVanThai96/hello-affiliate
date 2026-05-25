# Managerial Accounting – Kế Toán Quản Trị

> **Mục tiêu**: Hiểu rõ kế toán quản trị – công cụ nội bộ giúp nhà quản lý ra quyết định dựa trên dữ liệu. Phân tích chi phí, định giá, CVP, và ứng dụng cho SME Việt Nam.

---

## I. ĐỊNH NGHĨA VÀ LÝ THUYẾT NỀN TẢNG

### 1. Định nghĩa

**Managerial Accounting (Kế toán quản trị)** là quá trình **thu thập, phân tích, trình bày thông tin tài chính & phi tài chính** nhằm hỗ trợ **nhà quản lý nội bộ** trong việc lập kế hoạch, kiểm soát, và ra quyết định.

> **"Management accounting is the process of identification, measurement, accumulation, analysis, preparation, interpretation, and communication of information used by management to plan, evaluate, and control within an entity."** – IMA (Institute of Management Accountants)

### 2. Sự khác biệt cốt lõi với Financial Accounting

```
┌───────────────────────────────────────────────────────┐
│                KẾ TOÁN QUẢN TRỊ vs KẾ TOÁN TÀI CHÍNH  │
│                                                        │
│  Financial Accounting          Managerial Accounting    │
│  ┌──────────────┐              ┌──────────────┐        │
│  │ Bên ngoài    │              │ Nội bộ       │        │
│  │ (External)   │              │ (Internal)   │        │
│  ├──────────────┤              ├──────────────┤        │
│  │ Quá khứ      │              │ Tương lai    │        │
│  │ (Historical) │              │ (Predictive) │        │
│  ├──────────────┤              ├──────────────┤        │
│  │ Chuẩn mực    │              │ Linh hoạt    │        │
│  │ (IFRS/VAS)   │              │ (Flexible)   │        │
│  ├──────────────┤              ├──────────────┤        │
│  │ Toàn DN      │              │ Bộ phận/SP   │        │
│  │ (Entity)     │              │ (Segment)    │        │
│  └──────────────┘              └──────────────┘        │
│                                                        │
│  Câu hỏi: "Đã xảy ra gì?"   "Nên làm gì tiếp theo?" │
└───────────────────────────────────────────────────────┘
```

### 3. Vai trò của kế toán quản trị

| Vai trò | Mô tả | Ví dụ |
|--------|-------|-------|
| **Planning** (Lập kế hoạch) | Thiết lập mục tiêu & ngân sách | Lập ngân sách doanh thu Q2 |
| **Controlling** (Kiểm soát) | So sánh thực tế vs kế hoạch | Chi phí vượt budget 15% → tìm nguyên nhân |
| **Decision Making** (Ra quyết định) | Cung cấp dữ liệu cho quyết định | Nên tự sản xuất hay outsource? |
| **Performance Evaluation** (Đánh giá) | Đo lường hiệu suất bộ phận/cá nhân | ROI của chi nhánh Đà Nẵng vs Hà Nội |

---

## II. PHÂN LOẠI CHI PHÍ TRONG KẾ TOÁN QUẢN TRỊ

### 1. Theo hành vi chi phí (Cost Behavior)

```
  Chi phí (Cost)
       │
       ├── Biến phí (Variable Cost): Thay đổi tỷ lệ với sản lượng
       │   Ví dụ: Nguyên liệu, hoa hồng bán hàng, phí GrabExpress
       │
       ├── Định phí (Fixed Cost): Không đổi khi sản lượng thay đổi
       │   Ví dụ: Tiền thuê mặt bằng, lương quản lý, bảo hiểm
       │
       ├── Bán biến phí (Semi-variable / Mixed Cost)
       │   Ví dụ: Điện (phí cố định + phí theo kWh), điện thoại
       │
       └── Bước nhảy (Step Cost): Cố định trong khoảng, nhảy bậc
           Ví dụ: Thuê thêm 1 quản lý khi quy mô tăng
```

**Đồ thị hành vi chi phí:**

```
  Cost ($)                                     Cost ($)
     │         /                                  │
     │       /    Variable                        │ ────────── Fixed
     │     /                                      │
     │   /                                        │
     │ /                                          │
     └─────────── Volume                          └─────────── Volume

  Cost ($)                                     Cost ($)
     │       /                                    │        ┌──
     │     /                                      │     ┌──┘
     │   /                                        │  ┌──┘     Step
     │ / ── Fixed component                       │──┘
     │/      Mixed                                │
     └─────────── Volume                          └─────────── Volume
```

### 2. Theo khả năng truy nguyên (Traceability)

| Loại | Định nghĩa | Ví dụ (nhà máy sản xuất bánh) |
|------|-----------|-------------------------------|
| **Chi phí trực tiếp** (Direct Cost) | Truy nguyên trực tiếp đến đối tượng chi phí | Bột mì, đường, trứng → đến "Bánh A" |
| **Chi phí gián tiếp** (Indirect Cost / Overhead) | Không thể truy nguyên trực tiếp, phải phân bổ | Tiền thuê nhà xưởng, lương quản đốc, điện |

### 3. Theo mục đích ra quyết định

| Khái niệm | Định nghĩa | Ví dụ |
|-----------|-----------|-------|
| **Relevant Cost** (Chi phí thích hợp) | Chi phí khác biệt giữa các phương án, ảnh hưởng quyết định | Chi phí thuê máy mới vs cũ |
| **Sunk Cost** (Chi phí chìm) | Đã phát sinh, không thể thu hồi → KHÔNG relevant | Tiền đã trả R&D cho sản phẩm thất bại |
| **Opportunity Cost** (Chi phí cơ hội) | Giá trị bị mất khi chọn phương án này thay vì phương án khác | Không cho thuê mặt bằng để tự kinh doanh |
| **Incremental Cost** (Chi phí tăng thêm) | Chi phí phát sinh khi thay đổi quyết định | Chi phí sản xuất thêm 100 sản phẩm |
| **Controllable Cost** | Chi phí mà manager có thể kiểm soát | Chi phí quảng cáo (quyết định bởi Marketing Manager) |

### 4. Sơ đồ cấu trúc chi phí sản phẩm

```
┌──────────────────────────────────────────────────┐
│              PRODUCT COST (Chi phí sản phẩm)      │
│                                                    │
│  ┌────────────────────┐                            │
│  │ Direct Materials   │ ──── Nguyên vật liệu TT   │
│  │ (NVL trực tiếp)    │                            │
│  └────────┬───────────┘                            │
│           │                                        │
│  ┌────────▼───────────┐                            │
│  │ Direct Labor       │ ──── Nhân công trực tiếp   │
│  │ (NC trực tiếp)     │                            │
│  └────────┬───────────┘                            │
│           │          = PRIME COST                   │
│  ┌────────▼───────────┐                            │
│  │ Manufacturing      │ ──── Chi phí SX chung      │
│  │ Overhead (MOH)     │      (Khấu hao, điện,      │
│  │                    │      lương quản đốc)        │
│  └────────────────────┘                            │
│           = CONVERSION COST                        │
│                                                    │
│  PERIOD COST (Chi phí thời kỳ):                   │
│  - Selling Expenses (Chi phí bán hàng)             │
│  - G&A Expenses (Chi phí quản lý)                  │
└──────────────────────────────────────────────────┘
```

**Phân biệt:**

$$\text{Prime Cost} = \text{Direct Materials} + \text{Direct Labor}$$

$$\text{Conversion Cost} = \text{Direct Labor} + \text{MOH}$$

$$\text{Total Product Cost} = \text{DM} + \text{DL} + \text{MOH}$$

---

## III. PHÂN TÍCH CHI PHÍ – KHỐI LƯỢNG – LỢI NHUẬN (CVP ANALYSIS)

### 1. Khái niệm CVP

**CVP (Cost-Volume-Profit) Analysis** là công cụ phân tích mối quan hệ giữa **chi phí, sản lượng, và lợi nhuận** để hỗ trợ quyết định kinh doanh.

### 2. Công thức cốt lõi

**Contribution Margin (Số dư đảm phí):**

$$\text{CM per unit} = \text{Selling Price} - \text{Variable Cost per unit}$$

$$\text{CM Ratio} = \frac{\text{CM per unit}}{\text{Selling Price}}$$

**Break-Even Point (Điểm hòa vốn):**

$$\text{BEP (units)} = \frac{\text{Fixed Costs}}{\text{CM per unit}}$$

$$\text{BEP (sales \$)} = \frac{\text{Fixed Costs}}{\text{CM Ratio}}$$

**Target Profit (Lợi nhuận mục tiêu):**

$$\text{Required Units} = \frac{\text{Fixed Costs} + \text{Target Profit}}{\text{CM per unit}}$$

**Margin of Safety (Biên an toàn):**

$$\text{MoS} = \frac{\text{Actual Sales} - \text{BEP Sales}}{\text{Actual Sales}} \times 100\%$$

### 3. Ví dụ chi tiết: Quán cà phê SME

| Thông số | Giá trị |
|----------|---------|
| Giá bán trung bình/ly | 50,000 VNĐ |
| Biến phí/ly (nguyên liệu, ly, ống hút) | 15,000 VNĐ |
| Định phí/tháng (thuê, lương, điện, khấu hao) | 70,000,000 VNĐ |

**Tính toán:**

$$\text{CM/ly} = 50,000 - 15,000 = 35,000 \text{ VNĐ}$$

$$\text{CM Ratio} = \frac{35,000}{50,000} = 70\%$$

$$\text{BEP (số ly)} = \frac{70,000,000}{35,000} = 2,000 \text{ ly/tháng} \approx 67 \text{ ly/ngày}$$

$$\text{BEP (doanh thu)} = \frac{70,000,000}{0.7} = 100,000,000 \text{ VNĐ/tháng}$$

**Nếu muốn lãi 30 triệu/tháng:**

$$\text{Required} = \frac{70,000,000 + 30,000,000}{35,000} = 2,857 \text{ ly/tháng} \approx 95 \text{ ly/ngày}$$

**Nếu đang bán 3,000 ly/tháng:**

$$\text{MoS} = \frac{3,000 - 2,000}{3,000} = 33.3\%$$

→ Có thể giảm 33% doanh số mà chưa lỗ → **tương đối an toàn**

### 4. Đồ thị CVP

```
  Revenue/Cost
  (triệu VNĐ)
       │
  200 ─┤                              /  Revenue
       │                           / /
  150 ─┤                        / /
       │                     / /    Total Cost
  100 ─┤ ──── BEP ──── ● /
       │              / /
   70 ─┤ ────── FC ─/─ ─ ─ ─ ─ ─   Fixed Cost
       │         / /
       │       / /
       │     / /
       └───┴───┴────┴────┴────┴──── Volume (ly)
           0   1000  2000  3000  4000
                      ↑
                     BEP
                   (2,000 ly)

       ◄── LOSS ──►◄───── PROFIT ─────►
```

### 5. Operating Leverage (Đòn bẩy hoạt động)

**Degree of Operating Leverage (DOL):**

$$\text{DOL} = \frac{\text{Contribution Margin}}{\text{Operating Income}}$$

**Ý nghĩa:** DOL cao → Lợi nhuận nhạy cảm với thay đổi doanh thu

| DOL | Ý nghĩa | Ví dụ |
|-----|---------|-------|
| DOL = 3 | Doanh thu tăng 10% → Lợi nhuận tăng 30% | DN có định phí cao (công nghệ, SaaS) |
| DOL = 1.5 | Doanh thu tăng 10% → Lợi nhuận tăng 15% | DN có biến phí cao (bán lẻ) |

**So sánh 2 mô hình kinh doanh:**

| Yếu tố | Mô hình A (Định phí cao) | Mô hình B (Biến phí cao) |
|--------|------------------------|-------------------------|
| Ví dụ | Nhà máy sản xuất | Trading/Mua bán |
| Định phí | 100 triệu/tháng | 30 triệu/tháng |
| Biến phí/SP | 10,000 VNĐ | 40,000 VNĐ |
| Giá bán | 50,000 VNĐ | 50,000 VNĐ |
| CM/unit | 40,000 | 10,000 |
| BEP | 2,500 SP | 3,000 SP |
| DOL | Cao | Thấp |
| Rủi ro khi doanh thu giảm | **Rất cao** – lỗ nhanh | Trung bình |
| Lợi khi doanh thu tăng | **Rất cao** – lãi nhanh | Vừa phải |

---

## IV. RA QUYẾT ĐỊNH QUẢN TRỊ (DECISION MAKING)

### 1. Make or Buy (Tự sản xuất hay Mua ngoài)

**Framework:**

$$\text{Nên Make nếu: } \text{Cost}_{\text{make}} < \text{Cost}_{\text{buy}}$$

**Lưu ý:** Phải tính cả **chi phí cơ hội** & **yếu tố phi tài chính** (chất lượng, bí mật kinh doanh, phụ thuộc nhà cung cấp)

**Ví dụ:** Công ty SX nội thất quyết định tự đóng ghế hay đặt gia công:

| Yếu tố | Tự sản xuất | Mua ngoài |
|--------|------------|----------|
| NVL trực tiếp | 200k/ghế | – |
| Nhân công | 100k/ghế | – |
| MOH (biến) | 50k/ghế | – |
| MOH (định – phân bổ) | 80k/ghế | – |
| Giá mua ngoài | – | 380k/ghế |
| **Relevant Cost** | **350k/ghế** (bỏ 80k định phí) | **380k/ghế** |
| **Quyết định** | **✅ Tự sản xuất** (tiết kiệm 30k/ghế) | |

### 2. Accept or Reject Special Order (Đơn hàng đặc biệt)

**Nguyên tắc:** Chấp nhận nếu đơn hàng đặc biệt trang trải được **biến phí tăng thêm** (và không ảnh hưởng bán hàng bình thường)

**Ví dụ:** Đơn hàng 500 ghế, giá 320k/ghế (thấp hơn giá bình thường 450k/ghế)

| | Bình thường | Đơn đặc biệt |
|---|------------|-------------|
| Giá bán | 450k | 320k |
| Biến phí | 350k | 350k |
| CM/unit | 100k | (30k) → Lỗ? |

**Nhưng nếu còn công suất dư thừa:**
- Định phí không tăng thêm (đã trả rồi)
- Relevant cost = chỉ biến phí 350k
- Giá offer 320k < 350k → **Từ chối** ❌

**Nếu biến phí giảm còn 300k (do quy mô lớn):**
- 320k > 300k → **Chấp nhận** ✅ (lãi thêm 20k × 500 = 10 triệu)

### 3. Continue or Discontinue (Tiếp tục hay dừng sản phẩm/bộ phận)

**Nguyên tắc:** Dừng nếu **CM âm** (doanh thu không cover được biến phí). Nếu CM dương, sản phẩm vẫn đang đóng góp vào trang trải định phí.

**Ví dụ:** Chuỗi 3 sản phẩm:

| | SP A | SP B | SP C | Tổng |
|---|------|------|------|------|
| Doanh thu | 500 | 300 | 200 | 1,000 |
| Biến phí | (250) | (180) | (150) | (580) |
| **CM** | **250** | **120** | **50** | **420** |
| Định phí phân bổ | (150) | (100) | (80) | (330) |
| **Lợi nhuận** | **100** | **20** | **(30)** | **90** |

SP C lỗ 30, nên dừng? **KHÔNG!** Vì:
- CM của SP C = +50 (dương) → đang đóng góp trang trải định phí
- Nếu dừng C: Định phí 80 không biến mất (vẫn phải trả thuê mặt bằng)
- Lợi nhuận mới: 90 + 30 (hết lỗ C) - 50 (mất CM C) = 70 < 90 ban đầu

→ **Dừng SP C làm lợi nhuận tổng GIẢM!**

### 4. Sơ đồ ra quyết định

```
┌──────────────────────────────────────────────────┐
│         DECISION MAKING FRAMEWORK                 │
│                                                    │
│  Bước 1: Xác định alternatives (phương án)        │
│       │                                            │
│  Bước 2: Xác định relevant costs & revenues       │
│       │   (loại bỏ sunk costs & allocated costs)  │
│       │                                            │
│  Bước 3: So sánh incremental cash flows           │
│       │                                            │
│  Bước 4: Xem xét qualitative factors              │
│       │   (chất lượng, uy tín, long-term)         │
│       │                                            │
│  Bước 5: Ra quyết định                            │
└──────────────────────────────────────────────────┘
```

---

## V. ƯU VÀ NHƯỢC ĐIỂM

### 1. Ưu điểm

| Ưu điểm | Chi tiết |
|---------|---------|
| **Ra quyết định tốt hơn** | Dữ liệu chi tiết theo sản phẩm, bộ phận, kênh |
| **Linh hoạt** | Tùy chỉnh report theo nhu cầu quản lý |
| **Forward-looking** | Lập kế hoạch & dự báo tương lai |
| **Kiểm soát chi phí** | Phát hiện lãng phí & tối ưu hóa |
| **Đánh giá hiệu suất** | So sánh bộ phận, sản phẩm, nhân viên |
| **Không bị ràng buộc chuẩn mực** | Sử dụng bất kỳ metric nào phù hợp |

### 2. Nhược điểm

| Nhược điểm | Chi tiết |
|-----------|---------|
| **Chủ quan** | Phụ thuộc assumptions & estimates |
| **Tốn nguồn lực** | Cần hệ thống & nhân lực thu thập dữ liệu |
| **Thiên vị ngắn hạn** | Có thể dẫn đến quyết định tối ưu ngắn hạn nhưng hại dài hạn |
| **Không chuẩn hóa** | Khó so sánh giữa các DN |
| **Phức tạp** | CVP, ABC, transfer pricing đòi hỏi expertise |
| **Data quality** | "Garbage in, garbage out" – dữ liệu sai → quyết định sai |

---

## VI. HOÀN CẢNH VÀ MÔI TRƯỜNG ÁP DỤNG

### 1. Khi nào cần kế toán quản trị?

| Tình huống | Câu hỏi cần trả lời | Công cụ KTQT |
|-----------|---------------------|-------------|
| **Startup đang đốt tiền** | Bao lâu nữa hết tiền? Khi nào hòa vốn? | CVP, Burn Rate, Runway |
| **Mở thêm chi nhánh** | Có lãi không? Bao lâu thu hồi vốn? | CVP, NPV, Payback |
| **Sản phẩm nào nên focus** | SP nào lãi nhất? SP nào đang lỗ? | Product Profitability, ABC |
| **Tự sản xuất hay outsource** | Nên tự làm hay thuê ngoài? | Make-or-Buy, Relevant Cost |
| **Giảm chi phí** | Chi phí nào đang lãng phí? | Cost Analysis, Benchmarking |
| **Đánh giá team** | Bộ phận nào hiệu quả nhất? | Responsibility Accounting |

### 2. Theo giai đoạn phát triển DN

```
  Startup ──► Growth ──► Maturity ──► Renewal/Decline
     │           │           │              │
  CVP, BEP   Budgeting   Variance      Strategic
  Burn Rate  Std Costing  Analysis      Cost Mgmt
  Pricing    ABC          Transfer      Target
             Performance  Pricing       Costing
             Measurement  BSC           Kaizen
```

---

## VII. CASE STUDY THÀNH CÔNG

### Case Study 1: **Amazon – Kế toán quản trị hỗ trợ quyết định chiến lược**

**Bối cảnh:**
Amazon nổi tiếng với việc sử dụng kế toán quản trị để **hy sinh lợi nhuận ngắn hạn, tối ưu giá trị dài hạn**.

**Cách Amazon sử dụng Managerial Accounting:**

| Khía cạnh | Thực hiện | Kết quả |
|----------|----------|---------|
| **Unit Economics** | Tính chi phí/đơn hàng chi tiết (fulfillment, shipping, returns) | Tối ưu logistics → giảm cost/order từ $12 xuống $5 |
| **Segment P&L** | P&L riêng cho từng mảng (Retail, AWS, Ads, Prime) | Phát hiện AWS siêu lãi → đầu tư mạnh |
| **Customer LTV** | Tính giá trị trọn đời khách hàng Prime | Prime member chi tiêu gấp 4.6x non-Prime |
| **Relevant Cost** | Quyết định vào mảng mới dựa trên incremental analysis | Vào cloud (AWS) khi nhận ra có dư thừa capacity |
| **Transfer Pricing** | AWS serve nội bộ Amazon trước, sau đó bán ra ngoài | Kiểm soát chất lượng + tạo doanh thu mới |

**Insight quan trọng:**
- Amazon lỗ ròng nhiều năm đầu → Financial Accounting cho thấy hình ảnh "tệ"
- Nhưng **Managerial Accounting nội bộ** cho thấy **unit economics đang cải thiện liên tục**
- Jeff Bezos dùng **Free Cash Flow per share** (metric quản trị) thay vì EPS (metric kế toán tài chính)

**Bài học:**
> Kế toán quản trị giúp nhìn "bên trong" con số. DN có thể lỗ theo BCTC nhưng đang xây dựng nền tảng lãi lớn nếu unit economics đúng hướng.

---

## VIII. CASE STUDY THẤT BẠI

### Case Study 2: **WeWork – Khi kế toán quản trị bị méo mó**

**Bối cảnh:**
WeWork (The We Company) là startup coworking space, định giá $47 tỷ (2019), nhưng IPO thất bại thảm hại.

**Sai lầm kế toán quản trị:**

| Sai lầm | Chi tiết | Hệ quả |
|--------|---------|--------|
| **"Community Adjusted EBITDA"** | Tự tạo metric: EBITDA → loại bỏ marketing, G&A, depreciation, stock comp → "đẹp" | Che giấu lỗ thực tế ~$1.9 tỷ/năm |
| **Phân loại chi phí sai** | Gộp chi phí mặt bằng 15 năm (operating lease) thành "đầu tư tăng trưởng" | Nợ dài hạn khổng lồ không thể hiện rõ |
| **Unit Economics ảo** | Claim mỗi location "profitable" nhưng bỏ qua ramp-up cost & corporate overhead | Thực tế hầu hết locations lỗ |
| **Ignore relevant costs** | Không tính chi phí cơ hội của vốn & rủi ro lease dài hạn | Vỡ trận khi COVID hit |

**Hệ quả:**
- Định giá giảm từ **$47 tỷ → $8 tỷ** (83% mất giá trị)
- CEO Adam Neumann bị buộc rời công ty
- SoftBank mất **>$10 tỷ** đầu tư
- WeWork phá sản (Chapter 11) năm 2023

**Bài học:**
> 1. **Non-GAAP metrics phải có ý nghĩa** – "Community Adjusted EBITDA" là metric vô nghĩa, tự tạo để "làm đẹp"
> 2. **Unit economics phải thật** – Tính đủ ALL relevant costs, bao gồm overhead & cost of capital
> 3. **Sunk cost fallacy** – WeWork tiếp tục ký lease 15 năm dù locations lỗ
> 4. **Operating leverage ngược** – Định phí (lease) quá cao → khi doanh thu giảm (COVID) → lỗ cực lớn

---

## IX. ÁP DỤNG CHO SME VIỆT NAM

### 1. Bắt đầu kế toán quản trị cho SME

| Bước | Hành động | Công cụ đơn giản |
|------|----------|-----------------|
| 1 | Phân loại chi phí thành Biến phí & Định phí | Google Sheets |
| 2 | Tính CM (Contribution Margin) cho mỗi sản phẩm/dịch vụ | Excel template |
| 3 | Tính BEP (Break-Even Point) | Công thức CVP |
| 4 | Lập P&L theo sản phẩm/chi nhánh | Pivot table |
| 5 | So sánh Thực tế vs Kế hoạch hàng tháng | Dashboard đơn giản |
| 6 | Tính Unit Economics cho mỗi đơn hàng | Revenue - All variable costs per order |

### 2. Template P&L theo sản phẩm (đơn giản)

```
┌──────────────────────────────────────────────────┐
│     P&L THEO SẢN PHẨM – THÁNG XX/20XX           │
│                                                    │
│              SP A     SP B     SP C     TỔNG      │
│  Doanh thu   500      300      200      1,000     │
│  - COGS      (250)    (180)    (150)    (580)     │
│  ────────────────────────────────────────────      │
│  Lãi gộp     250      120      50       420       │
│  GM%         50%      40%      25%                │
│                                                    │
│  - Biến phí khác                                  │
│    Marketing (30)      (20)     (15)     (65)     │
│    Shipping  (10)      (8)      (5)      (23)     │
│  ────────────────────────────────────────────      │
│  CM          210      92       30       332       │
│  CM%         42%      31%      15%                │
│                                                    │
│  Định phí (phân bổ)                   (220)       │
│  ────────────────────────────────────────────      │
│  Lợi nhuận HĐKD                       112        │
│  Operating Margin                      11.2%      │
└──────────────────────────────────────────────────┘
│
│  → SP A: CM cao nhất → Focus & scale
│  → SP C: CM thấp → Tăng giá hoặc giảm biến phí
```

### 3. Checklist kế toán quản trị hàng tháng

| # | Check | Tần suất |
|---|-------|---------|
| 1 | Tính CM/unit cho top 5 sản phẩm | Tháng |
| 2 | Review BEP vs doanh thu thực tế | Tháng |
| 3 | So sánh Budget vs Actual (variance) | Tháng |
| 4 | Phân tích chi phí top 10 khoản lớn nhất | Tháng |
| 5 | Tính Customer Acquisition Cost (CAC) | Tháng |
| 6 | Tính Unit Economics cho mỗi kênh bán hàng | Quý |
| 7 | Review Make-or-Buy cho hoạt động chính | Quý |
| 8 | Full product profitability analysis | Quý |

---

## X. CÔNG THỨC TỔNG HỢP

### CVP Analysis

$$\text{CM} = \text{Sales} - \text{Variable Costs}$$

$$\text{BEP}_{\text{units}} = \frac{\text{FC}}{\text{CM per unit}}$$

$$\text{Target Units} = \frac{\text{FC} + \text{Target Profit}}{\text{CM per unit}}$$

$$\text{MoS\%} = \frac{\text{Actual Sales} - \text{BEP Sales}}{\text{Actual Sales}}$$

$$\text{DOL} = \frac{\text{CM}}{\text{Operating Income}}$$

### Product Cost

$$\text{Total Product Cost} = \text{DM} + \text{DL} + \text{MOH}$$

$$\text{Total Cost} = \text{Product Cost} + \text{Period Cost}$$

### Decision Making

$$\text{Make if: } \text{VC}_{\text{make}} + \text{Avoidable FC}_{\text{make}} < \text{Purchase Price}$$

$$\text{Accept Special Order if: } \text{Special Price} > \text{Incremental Cost per unit}$$

---

## XI. TÀI LIỆU THAM KHẢO

1. **Garrison, Noreen & Brewer** – "Managerial Accounting" 17th Ed
2. **Horngren, Datar & Rajan** – "Cost Accounting: A Managerial Emphasis" 16th Ed
3. **Kaplan & Atkinson** – "Advanced Management Accounting" 3rd Ed
4. **IMA (Institute of Management Accountants)** – Management Accounting Competency Framework
5. **CMA (Certified Management Accountant)** – Part 1 & 2 Curriculum
6. **Harvard Business Review** – Management Accounting articles
