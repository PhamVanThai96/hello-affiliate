# Integrated Case Studies – Kết Hợp Các Phương Pháp Accounting

> **Mục tiêu**: Phân tích các case study thực tế áp dụng **kết hợp** nhiều phương pháp accounting: Financial Accounting + Managerial Accounting + Cost Accounting + Budgeting + Variance Analysis + Financial Ratios. Thể hiện sự tương tác và bổ trợ giữa các phương pháp.

---

## CASE STUDY 1: STARTUP F&B "PHỞ VIỆT CHAIN" – Từ 1 Quán Đến Chuỗi

### Bối cảnh

**Phở Việt** là chuỗi phở cao cấp tại Việt Nam, bắt đầu với 1 quán tại Q1 TP.HCM năm 2020. Đến 2024, mở rộng 8 chi nhánh và đang cân nhắc mở thêm 5 chi nhánh + franchise. Doanh thu 2024: 30 tỷ VNĐ.

### Giai đoạn 1: Khởi nghiệp (1 quán) – Managerial Accounting + CVP

**Câu hỏi:** Quán có khả thi không? Bao giờ hòa vốn?

**Áp dụng CVP Analysis (Kế toán quản trị, File 02):**

| Thông số | Giá trị |
|----------|---------|
| Giá bán trung bình/tô | 80,000 VNĐ |
| Biến phí/tô (nguyên liệu, phụ kiện, gas) | 32,000 VNĐ |
| Định phí/tháng (thuê, lương, điện, khấu hao) | 120,000,000 VNĐ |

$$\text{CM/tô} = 80,000 - 32,000 = 48,000 \text{ VNĐ}$$

$$\text{CM\%} = \frac{48,000}{80,000} = 60\%$$

$$\text{BEP} = \frac{120,000,000}{48,000} = 2,500 \text{ tô/tháng} \approx 83 \text{ tô/ngày}$$

**Kết luận:** Cần bán tối thiểu 83 tô/ngày để hòa vốn. Quán 60 chỗ, 3 turn/ngày, occupancy rate 50% = 90 khách → **Khả thi** ✅

### Giai đoạn 2: Tối ưu menu – Cost Accounting (ABC)

**Câu hỏi:** Món nào lãi nhất? Nên focus vào đâu?

**Áp dụng ABC (File 03):**

Khi chỉ có 1 quán, owner nhận ra traditional costing (phân bổ overhead đều) không phản ánh đúng:

| Món | Doanh thu % | Food Cost % | Prep Time (phút) | # Ingredients | Traditional Margin | ABC Margin |
|-----|-----------|-------------|-----------------|--------------|-------------------|-----------|
| Phở bò truyền thống | 40% | 35% | 15 | 8 | 40% | **42%** |
| Phở bò Wagyu | 15% | 55% | 20 | 12 | 40% | **28%** |
| Bún bò Huế | 20% | 30% | 25 | 15 | 40% | **35%** |
| Phở gà | 15% | 25% | 10 | 6 | 40% | **52%** |
| Đồ uống | 10% | 15% | 3 | 2 | 40% | **75%** |

**ABC Cost Drivers:**
- Setup/prep complexity → Số nguyên liệu × thời gian chuẩn bị
- Quality checking → Các món premium cần QC nhiều hơn
- Waste handling → Phở Wagyu waste rate cao hơn

**Menu Engineering Matrix (kết hợp popularity × profitability):**

```
  High Profit │   ⭐ STAR        │  ❓ PUZZLE
  Margin      │   Phở gà         │  Đồ uống
              │   Phở bò TT      │  (push harder)
  ────────────┼──────────────────┼──────────────
  Low Profit  │   🐴 PLOW HORSE  │  🐕 DOG
  Margin      │   Bún bò Huế     │  Phở Wagyu
              │   (optimize cost)│  (re-price or cut)
              │                  │
              └──Low Volume──────┴──High Volume──
```

**Hành động:**
1. **Phở Wagyu**: Tăng giá từ 150k → 180k (khách premium chấp nhận)
2. **Phở gà**: Push marketing (margin cao nhất, ít phức tạp nhất)
3. **Đồ uống**: Cross-sell combo (margin siêu cao 75%)
4. **Bún bò Huế**: Optimize nguyên liệu (giảm từ 15 → 10 ingredients)

### Giai đoạn 3: Mở rộng chuỗi – Budgeting & Forecasting

**Câu hỏi:** Mở thêm bao nhiêu quán? Cần bao nhiêu vốn?

**Áp dụng Master Budget + Rolling Forecast (File 04):**

**Capital Budget cho 1 chi nhánh mới:**

| Khoản mục | Chi phí |
|----------|---------|
| Tiền thuê deposit (6 tháng) | 300,000,000 |
| Thiết kế & thi công nội thất | 500,000,000 |
| Thiết bị bếp | 250,000,000 |
| Working capital (3 tháng) | 450,000,000 |
| Marketing khai trương | 100,000,000 |
| **Tổng đầu tư** | **1,600,000,000** |

**Rolling Forecast (13 tuần) cho chi nhánh mới:**

```
  Tuần    1    2    3    4    5    6   ...  13
  ─────────────────────────────────────────────
  Tô/ngày  40   50   55   60   65   70  ...  90
  Revenue  96tr 120tr 132tr 144tr 156tr 168tr... 216tr
  (tháng)
  Chi phí  130tr 130tr 125tr 125tr 120tr 120tr... 115tr
  
  BEP reached: ~Tuần 5 (65 tô/ngày)
  Payback: ~Tháng 20 (tổng vốn 1.6 tỷ / lãi ~80tr/tháng)
```

**Scenario Analysis:**

| Scenario | Assumptions | NPV (5 năm) | Decision |
|----------|------------|-------------|----------|
| **Bull** | 100 tô/ngày by month 3 | +1.2 tỷ | ✅ Mở |
| **Base** | 85 tô/ngày by month 6 | +400 triệu | ✅ Mở |
| **Bear** | 60 tô/ngày (max) | -300 triệu | ❌ Đừng mở |
| **Probability-weighted** | 25%/50%/25% | **+425 triệu** | ✅ Mở |

### Giai đoạn 4: Kiểm soát chuỗi – Variance Analysis

**Câu hỏi:** Chi nhánh nào hoạt động tốt/kém? Vì sao?

**Áp dụng Variance Analysis (File 05):**

**Monthly Variance Report – 8 chi nhánh:**

| Chi nhánh | Revenue Var | Food Cost Var | Labor Var | Profit Var | Status |
|----------|------------|--------------|----------|-----------|--------|
| Q1 (flagship) | +5% (F) | -2% (F) | +3% (U) | +4% (F) | 🟢 |
| Q3 | +2% (F) | +1% (U) | -1% (F) | +2% (F) | 🟢 |
| Q7 | -3% (U) | +5% (U) | +2% (U) | -10% (U) | 🔴 |
| Thủ Đức | -8% (U) | +8% (U) | +5% (U) | -21% (U) | 🔴🔴 |
| Bình Thạnh | +1% (F) | -1% (F) | +1% (U) | +1% (F) | 🟢 |
| Tân Bình | -1% (U) | +2% (U) | -2% (F) | -1% (U) | 🟡 |
| Hà Nội 1 | +10% (F) | +3% (U) | +4% (U) | +3% (F) | 🟢 |
| Hà Nội 2 | -5% (U) | +6% (U) | +7% (U) | -18% (U) | 🔴 |

**Deep dive: Chi nhánh Thủ Đức (worst performer)**

| Variance | Amount | Root Cause (5-Why) |
|----------|--------|--------------------|
| Revenue -8% (U) | -32 triệu | Khu vực ít dân văn phòng, foot traffic thấp vào trưa |
| Food Cost +8% (U) | +25.6 triệu | Manager mới chưa control portioning, waste 18% vs standard 8% |
| Labor +5% (U) | +12 triệu | Thuê thêm 2 NV do thiếu kinh nghiệm, OT nhiều |
| **Total Profit Var** | **-69.6 triệu** | |

**Corrective Actions:**

| # | Action | Responsible | Deadline | Expected Impact |
|---|--------|-------------|----------|----------------|
| 1 | Training portioning cho manager | Ops Director | 2 tuần | Food cost -5% |
| 2 | Implement Kanban prep system | Head Chef | 1 tháng | Waste giảm 10% |
| 3 | Chạy marketing local (Grab, ShopeeFood) | Marketing | Ngay | Revenue +5% |
| 4 | Nếu không improve 3 tháng → Consider close | CEO | 3 tháng | – |

### Giai đoạn 5: Đánh giá tổng thể – Financial Ratios + DuPont

**Câu hỏi:** Chuỗi có khỏe mạnh không? Nên tiếp tục mở rộng?

**Áp dụng Financial Ratios & DuPont (File 06):**

| Ratio | Phở Việt 2024 | F&B Industry Avg | Verdict |
|-------|--------------|-----------------|---------|
| **Gross Margin** | 62% | 60-70% | 🟢 Tốt |
| **Operating Margin** | 12% | 8-15% | 🟢 Tốt |
| **Net Margin** | 8% | 5-10% | 🟢 Tốt |
| **Current Ratio** | 1.4 | 1.0-1.5 | 🟢 OK |
| **D/E** | 1.2 | 1.0-2.0 | 🟢 OK |
| **ROE** | 28% | 15-25% | 🟢 Tốt |
| **ROA** | 14% | 8-12% | 🟢 Tốt |
| **Inventory Turnover** | 45x | 30-60x | 🟢 Tốt |
| **CCC** | -5 ngày | 0-15 ngày | 🟢 Xuất sắc |

**DuPont Analysis:**

$$\text{ROE} = 8\% \times 1.75 \times 2.0 = 28\%$$

| Component | Giá trị | Đánh giá |
|-----------|---------|---------|
| Net Margin | 8% | Khỏe – có thể improve bằng reduce food cost |
| Asset Turnover | 1.75x | Tốt cho F&B – sử dụng tài sản hiệu quả |
| Equity Multiplier | 2.0x | Vừa phải – leverage hợp lý |

**Quyết định mở rộng:**

```
  Financial Health Check: ✅ PASS

  ┌─────────────────────────────────────────────┐
  │ GO / NO-GO DECISION MATRIX                  │
  │                                              │
  │ Profitability (ratios):       ✅ PASS        │
  │ Liquidity (current/quick):    ✅ PASS        │
  │ Leverage (D/E < 2):           ✅ PASS        │
  │ Unit Economics (positive):    ✅ PASS        │
  │ Variance control:             🟡 2/8 RED    │
  │ Budget accuracy:              ✅ Within 10%  │
  │                                              │
  │ RECOMMENDATION: ✅ Proceed with expansion    │
  │ BUT: Fix underperforming locations FIRST     │
  │ AND: Don't open more than 3 new in Year 1   │
  └─────────────────────────────────────────────┘
```

### Bài học tổng hợp

| Accounting Tool | Vai trò trong câu chuyện | Giai đoạn |
|----------------|------------------------|----------|
| **CVP (Managerial)** | Quyết định mở quán đầu tiên | Khởi nghiệp |
| **ABC (Cost)** | Tối ưu menu, phát hiện món lỗ | Tối ưu hóa |
| **Budgeting** | Lập kế hoạch mở rộng, scenario planning | Mở rộng |
| **Variance Analysis** | Kiểm soát chất lượng vận hành chuỗi | Kiểm soát |
| **Financial Ratios** | Đánh giá sức khỏe tổng thể, quyết định Go/No-go | Đánh giá |
| **Financial Accounting** | Báo cáo cho nhà đầu tư, ngân hàng | Gọi vốn |

---

## CASE STUDY 2: CÔNG TY SẢN XUẤT "GREENPACK" – Bao Bì Thân Thiện Môi Trường

### Bối cảnh

**GreenPack** sản xuất bao bì từ nguyên liệu tái chế & phân hủy sinh học. Founded 2019, hiện có 1 nhà máy, 50 nhân viên, doanh thu 15 tỷ/năm. Đang cần gọi vốn Series A để mở nhà máy thứ 2.

### Vấn đề 1: Investor hỏi – "Show me the numbers"

**Financial Accounting (File 01) – Chuẩn bị BCTC cho nhà đầu tư:**

| Báo cáo | Trước chỉnh sửa | Sau chỉnh sửa (IFRS-ready) |
|---------|-----------------|---------------------------|
| Balance Sheet | VAS, historical cost | Revalue TSCĐ theo fair value |
| Income Statement | Ghi nhận doanh thu khi xuất hóa đơn | IFRS 15: 5-step model |
| Cash Flow | Không lập | Lập đầy đủ (indirect method) |
| Notes | Sơ sài | Chi tiết: chính sách, segment, related party |

**Vấn đề phát hiện khi chuyển sang IFRS:**
- Doanh thu bị ghi nhận sớm 1 tháng (ghi khi xuất kho, chưa giao hàng)
- TSCĐ: máy ép trị giá thực tế 800tr (sổ sách: 1.2 tỷ) → impairment 400tr
- Operating lease chưa ghi nhận trên Balance Sheet (IFRS 16)

→ **Net Income giảm 15%** sau điều chỉnh, NHƯNG BCTC đáng tin cậy hơn → Investor tin tưởng

### Vấn đề 2: Giá thành sản phẩm chưa rõ

**Cost Accounting – Job + ABC kết hợp (File 03):**

GreenPack có 3 dòng sản phẩm, mỗi đơn hàng khác nhau (Job Costing) nhưng overhead phân bổ bằng ABC:

| Activity | Cost Pool | Driver | Hộp A (đơn giản) | Hộp B (in ấn custom) | Túi C (compostable) |
|----------|----------|--------|-----------------|---------------------|-------------------|
| Machine setup | 500tr | # setups | 20 setups | 80 setups | 30 setups |
| Quality testing | 300tr | # tests | 50 tests | 100 tests | 200 tests |
| Design/Engineering | 200tr | # designs | 5 designs | 30 designs | 10 designs |

**Kết quả ABC:**

| | Hộp A | Hộp B | Túi C |
|---|-------|-------|-------|
| DM/unit | 1,200 | 2,500 | 3,800 |
| DL/unit | 800 | 1,200 | 1,500 |
| **Traditional OH/unit** | 1,500 | 1,500 | 1,500 |
| **ABC OH/unit** | **700** | **2,800** | **1,800** |
| **Total Traditional** | 3,500 | 5,200 | 6,800 |
| **Total ABC** | **2,700** | **6,500** | **7,100** |
| Giá bán | 4,000 | 7,000 | 8,000 |
| **Traditional Margin** | **14.3%** | **34.6%** | **17.6%** |
| **ABC Margin** | **32.5%** | **7.7%** | **11.3%** |

**Insight quyết định:**
- **Hộp A**: Thực tế lãi **32.5%** (không phải 14.3%) → Cash cow, push sản lượng!
- **Hộp B**: Thực tế chỉ lãi **7.7%** → Đang bị trợ giá, cần tăng giá hoặc tối ưu
- **Túi C**: Margin vừa phải → Cần scale để giảm cost/unit

### Vấn đề 3: Budget cho nhà máy mới

**Budgeting & Forecasting (File 04):**

**5-Year Pro-forma với nhà máy mới:**

| | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|--------|--------|--------|--------|--------|
| Revenue (tỷ) | 18 | 25 | 35 | 45 | 55 |
| Growth % | 20% | 39% | 40% | 29% | 22% |
| COGS | (10.8) | (14.0) | (18.9) | (23.4) | (27.5) |
| Gross Margin | 40% | 44% | 46% | 48% | 50% |
| OpEx | (5.5) | (7.0) | (9.0) | (10.5) | (12.0) |
| EBIT | 1.7 | 4.0 | 7.1 | 11.1 | 15.5 |
| EBIT Margin | 9.4% | 16% | 20.3% | 24.7% | 28.2% |
| CapEx (nhà máy 2) | (8.0) | (2.0) | – | – | – |
| FCF | (5.5) | 2.0 | 6.5 | 10.5 | 14.5 |

**ZBB cho OpEx Year 1:**

| Package | Chi phí | Rank | Decision |
|---------|---------|------|----------|
| Core production team | 2.0 tỷ | 1 | ✅ Must-have |
| Sales team (5 người) | 1.2 tỷ | 2 | ✅ Revenue-generating |
| R&D (material science) | 0.8 tỷ | 3 | ✅ Competitive advantage |
| Digital marketing | 0.5 tỷ | 4 | ✅ Growth driver |
| Office & Admin | 0.6 tỷ | 5 | ✅ Necessary |
| Trade show participation | 0.3 tỷ | 6 | ✅ Within budget |
| CSR activities | 0.1 tỷ | 7 | ❌ Defer to Year 2 |

### Vấn đề 4: Performance monitoring

**Variance + Ratios kết hợp (File 05 + 06):**

**Monthly Scorecard:**

```
┌──────────────────────────────────────────────────────┐
│  GREENPACK MONTHLY SCORECARD – THÁNG XX/20XX         │
│                                                        │
│  ══ BUDGET vs ACTUAL ══                                │
│  Revenue:    Budget 1.5 tỷ  │ Actual 1.6 tỷ │ +6.7%(F)│
│  COGS:       Budget 0.9 tỷ  │ Actual 0.95 tỷ│ +5.6%(U)│
│  EBIT:       Budget 0.15 tỷ │ Actual 0.17 tỷ│ +13% (F)│
│                                                        │
│  ══ COST VARIANCES ══                                  │
│  DM Price:   -2.1% (F) → Đàm phán giá NVL tốt       │
│  DM Quantity: +3.5% (U) → Waste rate tăng             │
│  DL Efficiency: +1.2% (U) → OT ngày lễ               │
│                                                        │
│  ══ KEY RATIOS ══                                      │
│  Gross Margin:    41% (target 40%) ✅                  │
│  CCC:             25 ngày (target 30) ✅               │
│  Current Ratio:   1.8 ✅                               │
│  D/E:             0.8 ✅                               │
│  Inventory Turn:  12x ✅                               │
│                                                        │
│  ══ ACTION ITEMS ══                                    │
│  1. DM Qty variance: Investigate waste                 │
│     → Root cause: Batch #237 NVL lỗi                  │
│     → Action: Claim nhà cung cấp, QC input stricter   │
│  2. Start IFRS conversion for Series A DD              │
└──────────────────────────────────────────────────────┘
```

### Vấn đề 5: Pitch cho Investor

**Kết hợp tất cả (File 01-06):**

Trong pitch deck cho Series A, GreenPack trình bày:

| Slide | Accounting Tool | Nội dung |
|-------|----------------|---------|
| Market & Revenue | Financial Accounting | BCTC kiểm toán 3 năm, revenue CAGR 35% |
| Unit Economics | ABC (Cost Accounting) | Cost per unit breakdown, margin roadmap |
| Profitability | Financial Ratios | Gross Margin expansion: 38% → 50% in 5 years |
| Growth Plan | Budgeting | 5-year pro-forma, scenario analysis |
| Operational Excellence | Variance Analysis | Monthly variance dashboard, corrective system |
| Capital Efficiency | DuPont Analysis | ROE decomposition: margin × turnover × leverage |

**Kết quả:** GreenPack raise Series A thành công **$3 triệu** với valuation **$15 triệu**.

### Bài học tổng hợp

> **Accounting tools không hoạt động riêng lẻ.** Sức mạnh thật sự đến từ sự **kết hợp**:
>
> 1. **Financial Accounting** cung cấp "language" để communicate với bên ngoài
> 2. **Cost Accounting** cho biết "truth" về chi phí thực sự
> 3. **Managerial Accounting** hỗ trợ "decisions" nội bộ
> 4. **Budgeting** tạo ra "roadmap" đi tới tương lai
> 5. **Variance Analysis** là "GPS navigation" – biết bạn lạc đường hay đúng hướng
> 6. **Financial Ratios** là "health check" – sức khỏe tổng thể

---

## CASE STUDY 3: THẤT BẠI – "TECHMART" – Chuỗi Bán Lẻ Điện Tử (Tên Giả Định)

### Bối cảnh

**TechMart** là chuỗi bán lẻ điện tử 15 cửa hàng tại Việt Nam. Doanh thu đỉnh 500 tỷ (2019), nhưng suy giảm liên tục và đóng cửa 10/15 cửa hàng vào 2023.

### Lỗi 1: Financial Accounting – "Số liệu đẹp che đậy thực tế"

| Vấn đề | Chi tiết |
|--------|---------|
| **Revenue recognition** | Ghi doanh thu khi xuất kho cho showroom (chưa bán cho khách hàng cuối) |
| **Inventory valuation** | Không write-down hàng tồn kho lỗi thời (điện thoại cũ 2+ năm) |
| **Lease accounting** | Off-balance-sheet: 15 hợp đồng thuê mặt bằng 5-10 năm không ghi nhận |
| **Depreciation** | Nội thất showroom khấu hao 10 năm (thực tế lỗi thời sau 3 năm) |

**Tác động:**
- Revenue **phình to** so với thực tế (ghi nhận sớm)
- Tài sản **phình to** (tồn kho lỗi thời + nội thất chưa khấu hao đủ)
- Nợ **nhỏ hơn thực tế** (lease off-balance-sheet)
- → BCTC cho thấy "healthy" nhưng reality = **suy yếu dần**

### Lỗi 2: Cost Accounting – "Không biết chi phí thực"

| Sai lầm | Chi tiết | Hệ quả |
|--------|---------|--------|
| **Không ABC** | Overhead phân bổ đều cho mọi SP | Điện thoại giá rẻ (margin 3%) ăn promotional budget bằng premium (margin 15%) |
| **Không P&L per store** | Chỉ có consolidated P&L | Không biết store nào lỗ → keep hết |
| **Không P&L per category** | Tổng margin 8% | Laptop lãi 12%, phụ kiện lãi 40%, điện thoại phổ thông lỗ 2% |
| **Ignore logistics cost** | "Free shipping" = marketing cost? | Thực tế logistics = 4% revenue → ăn hết margin |

### Lỗi 3: Budgeting – "Budget lạc quan, không scenario planning"

| Năm | Budget Revenue | Actual Revenue | Variance | Đã adjust? |
|-----|---------------|---------------|----------|-----------|
| 2020 | 520 tỷ | 380 tỷ (-27%) | -140 tỷ (U) | Đổ lỗi COVID |
| 2021 | 450 tỷ | 350 tỷ (-22%) | -100 tỷ (U) | Đổ lỗi "phục hồi chậm" |
| 2022 | 420 tỷ | 280 tỷ (-33%) | -140 tỷ (U) | Mới bắt đầu lo |
| 2023 | 350 tỷ | 180 tỷ (-49%) | -170 tỷ (U) | Quá muộn |

**Sai lầm:**
- **Incremental budget** dựa trên peak revenue (2019) – luôn "budget giảm nhẹ"
- **Không rolling forecast** – Không cập nhật khi market shift sang online
- **Không worst-case scenario** – Chưa bao giờ model "nếu revenue giảm 50%?"
- **Không ZBB** – Vẫn giữ chi phí thuê 15 mặt bằng dù 8 cửa hàng dưới BEP

### Lỗi 4: Variance Analysis – "Biết nhưng không hành động"

```
  VARIANCE REPORT – Hàng tháng

  Month 1:  Revenue -15% (U)  → "Chờ xem"
  Month 2:  Revenue -18% (U)  → "Tháng tới sẽ khá hơn"
  Month 3:  Revenue -22% (U)  → "Đợi đến mùa peak"
  Month 4:  Revenue -12% (U)  → "Thấy chưa, đang phục hồi!" (nhưng YoY vẫn -20%)
  Month 5:  Revenue -25% (U)  → "Do thị trường, không phải lỗi mình"
  ...
  Month 12: Revenue -30% (U)  → "Cần restructure" (quá muộn 11 tháng)
  
  PROBLEM: Variance detected monthly 
           but NO CORRECTIVE ACTION TAKEN
           → Variance analysis vô nghĩa nếu không act
```

### Lỗi 5: Financial Ratios – "Red flags bị bỏ qua"

| Ratio | 2019 | 2020 | 2021 | 2022 | Red Flag? |
|-------|------|------|------|------|----------|
| **Inventory Turnover** | 8x | 5x | 3.5x | 2x | 🔴 Tồn kho ứ đọng |
| **DIO** | 46 ngày | 73 ngày | 104 ngày | 183 ngày | 🔴 Hàng không bán được |
| **Gross Margin** | 12% | 10% | 8% | 5% | 🔴 Pricing war |
| **Current Ratio** | 1.5 | 1.2 | 0.9 | 0.6 | 🔴 Mất thanh khoản |
| **D/E** | 1.0 | 1.8 | 2.5 | 4.0 | 🔴 Nợ chồng nợ |
| **Interest Coverage** | 5x | 2.5x | 1.2x | 0.5x | 🔴🔴 Không trả nổi lãi |
| **ROE** | 15% | 5% | -8% | -35% | 🔴 Mất vốn |
| **CCC** | 55 ngày | 85 ngày | 120 ngày | 200 ngày | 🔴 Tiền bị "đóng băng" |

**DuPont cho thấy câu chuyện sụp đổ:**

| | 2019 | 2022 |
|---|------|------|
| Net Margin | 3% | -12% |
| Asset Turnover | 2.5x | 0.8x |
| Equity Multiplier | 2.0 | 5.0 |
| **ROE** | **15%** | **-48%** (EM khuếch đại lỗ) |

→ **Equity Multiplier khuếch đại cả chiều thuận lẫn chiều ngược!** Khi lãi, EM amplify ROE. Khi lỗ, EM amplify lỗ.

### Tổng hợp: Đâu là nơi mỗi tool THẤT BẠI?

```
┌──────────────────────────────────────────────────────────────┐
│  FAILURE CASCADE – TechMart                                   │
│                                                                │
│  Financial Accounting     → BCTC misleading (revenue sớm,     │
│  (File 01)                   inventory inflated)               │
│       ↓                                                        │
│  Cost Accounting          → Không biết store/product nào lỗ   │
│  (File 03)                   Cross-subsidy che giấu lỗ        │
│       ↓                                                        │
│  Budgeting                → Budget lạc quan, không scenario    │
│  (File 04)                   Chi phí cố định quá lớn          │
│       ↓                                                        │
│  Variance Analysis        → Detected but NOT ACTED upon       │
│  (File 05)                   "Next month will be better"      │
│       ↓                                                        │
│  Financial Ratios         → Red flags visible for 2+ years    │
│  (File 06)                   Management ignored               │
│       ↓                                                        │
│  RESULT: Close 10/15 stores, massive losses                   │
│                                                                │
│  LESSON: Tools are USELESS without ACTION & ACCOUNTABILITY    │
└──────────────────────────────────────────────────────────────┘
```

### Bài học

> 1. **Accounting tools chỉ có giá trị khi đi kèm HÀNH ĐỘNG** – TechMart có đủ dữ liệu, nhưng leadership không sẵn sàng đưa ra quyết định đau đớn (đóng cửa hàng sớm)
>
> 2. **Mỗi tool bổ trợ cho nhau** – Financial Accounting che giấu → Cost Accounting không phát hiện → Budget sai → Variance bị ignore → Ratios cảnh báo muộn
>
> 3. **"Optimism bias" là kẻ thù của Accounting** – Budget lạc quan + "tháng sau sẽ khá hơn" = tardy decisions
>
> 4. **DuPont Analysis là "MRI scan"** – Không chỉ thấy ROE, mà thấy TẠI SAO ROE thay đổi (margin, turnover, hay leverage)

---

## TỔNG HỢP: SƠ ĐỒ KẾT HỢP 6 PHƯƠNG PHÁP ACCOUNTING

```
┌─────────────────────────────────────────────────────────────┐
│               INTEGRATED ACCOUNTING FRAMEWORK                │
│                                                               │
│                    ┌──────────────┐                           │
│                    │  FINANCIAL   │                           │
│                    │  ACCOUNTING  │ ← Report to external      │
│                    │  (IFRS/VAS)  │    stakeholders           │
│                    └──────┬───────┘                           │
│                           │                                   │
│              Feed data    │    Extract data                   │
│                           │                                   │
│        ┌──────────────────┼──────────────────┐               │
│        │                  │                  │               │
│  ┌─────▼──────┐   ┌──────▼──────┐   ┌───────▼──────┐       │
│  │   COST     │   │ MANAGERIAL  │   │  FINANCIAL   │       │
│  │ ACCOUNTING │   │ ACCOUNTING  │   │   RATIOS     │       │
│  │ (ABC/Job/  │   │ (CVP/       │   │ (DuPont/     │       │
│  │  Process)  │   │  Decision)  │   │  Liquidity)  │       │
│  └─────┬──────┘   └──────┬──────┘   └───────┬──────┘       │
│        │                 │                   │               │
│        │    ┌────────────┤                   │               │
│        │    │            │                   │               │
│  ┌─────▼────▼──┐  ┌─────▼──────┐   ┌───────▼──────┐       │
│  │  BUDGETING  │  │  VARIANCE  │   │   HEALTH     │       │
│  │  & FORECAST │──│  ANALYSIS  │──►│   CHECK      │       │
│  │  (Plan)     │  │  (Control) │   │  (Evaluate)  │       │
│  └─────────────┘  └────────────┘   └──────────────┘       │
│                                                               │
│  Flow: Plan → Execute → Measure → Compare → Improve → Plan  │
│        (PDCA: Plan-Do-Check-Act)                              │
└─────────────────────────────────────────────────────────────┘
```

---

## CHECKLIST: ÁP DỤNG KẾT HỢP CHO SME

| # | Câu hỏi | Tool | Tần suất |
|---|---------|------|---------|
| 1 | BCTC có đúng chuẩn VAS/IFRS không? | Financial Accounting | Quý + Năm |
| 2 | Chi phí từng SP/DV/dự án là bao nhiêu? | Cost Accounting (Job/ABC) | Quý |
| 3 | Sản phẩm nào nên focus/cắt? | Managerial (CVP + ABC) | Quý |
| 4 | Năm tới doanh thu/chi phí bao nhiêu? | Budgeting + Forecasting | Năm + Rolling |
| 5 | Tháng này có đúng kế hoạch không? | Variance Analysis | Tháng |
| 6 | DN có khỏe mạnh không? | Financial Ratios + DuPont | Quý |
| 7 | Nên mở rộng hay consolidate? | Kết hợp tất cả | Ad-hoc |
| 8 | Nhà đầu tư/ngân hàng cần gì? | Financial Accounting + Ratios | Khi cần |

---

## TÀI LIỆU THAM KHẢO

1. **Kaplan & Norton** – "The Balanced Scorecard" (Integrated performance management)
2. **Horngren, Datar & Rajan** – "Cost Accounting: A Managerial Emphasis"
3. **Garrison, Noreen & Brewer** – "Managerial Accounting"
4. **McKinsey** – "Valuation" (Integrated financial analysis)
5. **Harvard Business School** – Case Study methodology
6. **IMA** – Management Accounting Competency Framework
7. **CFA Institute** – Financial Reporting and Analysis (Level I-III)
