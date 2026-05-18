# Capital Budgeting – Hoạch Định Ngân Sách Vốn

> **Mục tiêu**: Nắm vững các phương pháp đánh giá dự án đầu tư – NPV, IRR, Payback, PI – quy trình ra quyết định phân bổ vốn, case study chi tiết.

---

## I. ĐỊNH NGHĨA VÀ LÝ THUYẾT NỀN TẢNG

### 1. Định nghĩa

**Capital Budgeting** là quy trình **đánh giá và lựa chọn các dự án đầu tư dài hạn** (thường > 1 năm) để quyết định phân bổ vốn nhằm tối đa hóa giá trị doanh nghiệp.

> **"The most important decision a CEO makes is how to allocate capital."** – Warren Buffett

### 2. Nguồn gốc lý thuyết

| Học giả | Đóng góp | Năm |
|---------|----------|-----|
| **Joel Dean** | "Capital Budgeting" – đặt tên & hệ thống hóa lý thuyết | 1951 |
| **Fisher & Hirshleifer** | NPV rule – tách biệt investment & financing decisions | 1930s-1950s |
| **Lorie & Savage** | Multiple IRR problem, capital rationing | 1955 |
| **Myers** | Real Options trong capital budgeting | 1977 |

### 3. Tại sao Capital Budgeting quan trọng?

| Lý do | Giải thích |
|-------|-----------|
| **Số tiền lớn** | Quyết định hàng tỷ → sai lầm cực tốn kém, không thể sửa |
| **Irreversibility** | Xây nhà máy xong không "undo" dễ dàng |
| **Long-term impact** | Ảnh hưởng 5-20 năm, shape toàn bộ tương lai DN |
| **Opportunity cost** | Đầu tư A = từ bỏ B (vốn scarce) |
| **Competitive advantage** | Đầu tư đúng → competitive edge; sai → tụt hậu |
| **Shareholder value** | Mục tiêu cuối: maximize NPV = maximize wealth |

### 4. Các loại dự án Capital Budgeting

```
┌─────────────────────────────────────────────────────────────────┐
│                  CÁC LOẠI DỰ ÁN ĐẦU TƯ                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. EXPANSION (Mở rộng)                                        │
│     - Mở nhà máy mới, chi nhánh mới, thị trường mới           │
│     - Ra sản phẩm/dịch vụ mới                                  │
│                                                                 │
│  2. REPLACEMENT (Thay thế)                                      │
│     - Thay máy cũ bằng máy mới hiệu quả hơn                   │
│     - Nâng cấp hệ thống IT, ERP                                │
│                                                                 │
│  3. MANDATORY (Bắt buộc)                                        │
│     - Tuân thủ pháp luật (môi trường, PCCC, an toàn)           │
│     - Không có lựa chọn "không đầu tư"                          │
│                                                                 │
│  4. R&D / INNOVATION                                            │
│     - Nghiên cứu sản phẩm mới, patent                          │
│     - Chuyển đổi số, AI implementation                          │
│                                                                 │
│  5. M&A (Mua lại / Sáp nhập)                                   │
│     - Mua đối thủ, startup, vertical integration                │
│     - Đặc biệt: capital budgeting + valuation                   │
│                                                                 │
│  6. STRATEGIC / EXPLORATORY                                     │
│     - Pilot projects, market entry test                         │
│     - Option value > immediate NPV                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

PHÂN LOẠI THEO QUAN HỆ:
• Independent projects: Chấp nhận/từ chối độc lập (NPV > 0 → accept all)
• Mutually exclusive: Chọn 1 trong nhiều (chọn NPV cao nhất)
• Contingent: Dự án B phụ thuộc vào dự án A
```

---

## II. CÁC PHƯƠNG PHÁP ĐÁNH GIÁ DỰ ÁN

### A. Net Present Value (NPV) – Gold Standard

#### Công thức

$$NPV = \sum_{t=0}^{n} \frac{CF_t}{(1+r)^t} = -C_0 + \frac{CF_1}{(1+r)^1} + \frac{CF_2}{(1+r)^2} + ... + \frac{CF_n}{(1+r)^n}$$

#### Quy tắc
- **NPV > 0** → Đầu tư (dự án tạo giá trị)
- **NPV < 0** → Từ chối (phá hủy giá trị)
- **Multiple projects** → Chọn NPV cao nhất

#### Ưu điểm
- Chính xác nhất, tính đến TVM và risk
- Additive: NPV(A+B) = NPV(A) + NPV(B)
- Đo absolute value creation

#### Nhược điểm
- Phụ thuộc discount rate
- CF dài hạn khó dự báo chính xác

---

### B. Internal Rate of Return (IRR)

#### Công thức

$$0 = -C_0 + \sum_{t=1}^{n} \frac{CF_t}{(1+IRR)^t}$$

#### Quy tắc: IRR > WACC → Đầu tư

#### Vấn đề Multiple IRR

```
Khi CF đổi dấu nhiều lần: -100, +230, -132
→ Hai IRR: 10% và 20% → Không biết chọn cái nào!

Giải pháp: Dùng MIRR hoặc dựa vào NPV
```

#### Modified IRR (MIRR)

$$MIRR = \left(\frac{FV_{positive}}{PV_{negative}}\right)^{1/n} - 1$$

- Reinvest positive CF at WACC (realistic)
- Luôn cho 1 giá trị duy nhất

---

### C. Payback Period (PP)

#### Định nghĩa
Thời gian để **tổng CF tích lũy = vốn đầu tư ban đầu**.

#### Ví dụ

| Năm | CF (triệu) | CF tích lũy |
|-----|-----------|-------------|
| 0 | -500 | -500 |
| 1 | +150 | -350 |
| 2 | +150 | -200 |
| 3 | +150 | -50 |
| 4 | +150 | +100 |

PP = 3 + 50/150 = **3.33 năm**

#### Nhược điểm nghiêm trọng
- ❌ Bỏ qua TVM
- ❌ Bỏ qua CF sau payback
- ❌ Threshold tùy ý

---

### D. Discounted Payback Period (DPP)

Chiết khấu CF trước khi tính → Khắc phục nhược điểm TVM.

---

### E. Profitability Index (PI)

$$PI = \frac{PV \text{ of future CF}}{Initial Investment} = 1 + \frac{NPV}{C_0}$$

- **PI > 1** → Đầu tư
- Hữu ích khi **capital rationing** (vốn hạn chế)

---

### F. Bảng tổng hợp so sánh

| Phương pháp | TVM? | Risk? | Scale? | Dễ hiểu? | Rank |
|------------|------|-------|--------|----------|------|
| **NPV** | ✅ | ✅ | ✅ | ⚠️ | **#1** |
| **IRR** | ✅ | ✅ | ❌ | ✅ | #2 |
| **MIRR** | ✅ | ✅ | ❌ | ✅ | #2.5 |
| **PI** | ✅ | ✅ | ✅(relative) | ✅ | #3 |
| **Payback** | ❌ | ❌ | ❌ | ✅✅ | Bổ trợ |
| **DPP** | ✅ | ⚠️ | ❌ | ✅ | Bổ trợ |

---

## III. QUY TRÌNH CAPITAL BUDGETING

### Quy trình 7 bước

```
Bước 1: IDEA GENERATION
   │  ← R&D, market research, competition, employees
   ▼
Bước 2: PRELIMINARY SCREENING
   │  ← Loại dự án không phù hợp chiến lược
   ▼
Bước 3: CASH FLOW ESTIMATION
   │  ← Initial, operating, terminal cash flows
   │  ← Incremental CF, after-tax, exclude sunk costs
   ▼
Bước 4: FINANCIAL ANALYSIS
   │  ← NPV, IRR, Payback, PI → Ranking
   ▼
Bước 5: PROJECT SELECTION
   │  ← Capital constraint, strategic fit, risk
   ▼
Bước 6: IMPLEMENTATION
   │  ← Project management, milestones, budget control
   ▼
Bước 7: POST-AUDIT
   ← Actual vs Projected  → Rút kinh nghiệm
```

### Cash Flow Estimation – Chi tiết

#### Nguyên tắc cốt lõi

| Nguyên tắc | Mô tả | Ví dụ |
|-----------|-------|-------|
| **Incremental CF** | Chỉ tính CF THAY ĐỔI do dự án | CF với dự án - CF không có dự án |
| **After-tax** | CF sau thuế | EBIT × (1-T) + Dep |
| **Include opportunity cost** | Chi phí cơ hội | Đất sẵn có → opportunity cost = giá thuê/bán |
| **Exclude sunk cost** | Chi phí đã chi trước quyết định | 500 triệu R&D đã chi → KHÔNG tính |
| **Include externalities** | Side effects lên dự án khác | Sản phẩm mới cannibalize sản phẩm cũ |
| **Ignore financing CF** | Không tính lãi vay, trả nợ | Đã reflect trong discount rate (WACC) |

#### Operating Cash Flow

$$OCF = EBIT \times (1 - Tax) + Depreciation$$

$$= Revenue - COGS - OpEx - Dep) \times (1-T) + Dep$$

$$= Net Income + Depreciation$$

#### Cấu trúc dòng tiền đầy đủ

```
INITIAL INVESTMENT (Năm 0):
  - CAPEX (mua tài sản, xây dựng)
  - Chi phí lắp đặt, vận chuyển
  + Thu từ bán tài sản cũ (nếu replacement)
  - Thuế bán tài sản cũ
  - Tăng Net Working Capital (NWC)
  = TOTAL INITIAL OUTFLOW

OPERATING CF (Năm 1 → n):
  = EBIT × (1-Tax) + Depreciation
  - ΔNet Working Capital hàng năm
  - Maintenance CAPEX

TERMINAL CF (Năm cuối):
  + Salvage value (giá trị thu hồi tài sản)
  - Thuế trên gain từ salvage
  + Thu hồi NWC
  = TOTAL TERMINAL CF
```

### Depreciation Tax Shield

$$\text{Tax Shield} = Depreciation \times Tax Rate$$

**Ví dụ**: Máy giá 1 tỷ, khấu hao thẳng 5 năm = 200 triệu/năm. Tax = 20%.
→ Tax Shield = 200 × 20% = **40 triệu/năm tiết kiệm thuế**

---

## IV. PHÂN TÍCH RỦI RO TRONG CAPITAL BUDGETING

### A. Sensitivity Analysis (Phân tích độ nhạy)

Thay đổi MỘT biến, giữ nguyên các biến khác → NPV thay đổi thế nào?

| Biến thay đổi | Base Case | Pessimistic | Optimistic | ΔNPV |
|--------------|-----------|-------------|------------|------|
| Revenue -20% / +20% | NPV = 124 | NPV = -15 | NPV = 263 | ±139 |
| WACC +3% / -3% | NPV = 124 | NPV = 52 | NPV = 215 | ±82 |
| CAPEX +30% / -30% | NPV = 124 | NPV = -26 | NPV = 274 | ±150 |
| Operating cost +15% / -15% | NPV = 124 | NPV = 41 | NPV = 207 | ±83 |

→ **Nhạy nhất**: CAPEX và Revenue → Cần focus accuracy cho 2 biến này

### B. Scenario Analysis

| Scenario | Probability | NPV | Weighted NPV |
|----------|-------------|-----|-------------|
| Best case | 25% | +350 tr | +87.5 |
| Base case | 50% | +124 tr | +62.0 |
| Worst case | 25% | -80 tr | -20.0 |
| **Expected NPV** | | | **+129.5** |

$$\sigma_{NPV} = \sqrt{\sum p_i \times (NPV_i - E[NPV])^2}$$

### C. Real Options

| Option | Giá trị | Khi nào? |
|--------|--------|---------|
| **Option to Expand** | Mở rộng nếu dự án thành công | Pilot → Full rollout |
| **Option to Delay** | Chờ thêm thông tin trước khi đầu tư | Uncertain market |
| **Option to Abandon** | Dừng & bán tài sản nếu thất bại | Salvage value > continue |
| **Option to Switch** | Chuyển đổi sản phẩm/công nghệ | Flexible production |

$$\text{Strategic NPV} = \text{Traditional NPV} + \text{Option Value}$$

---

## V. ƯU ĐIỂM VÀ NHƯỢC ĐIỂM CAPITAL BUDGETING

### ✅ Ưu điểm:
1. **Systematic decision-making** – Framework rõ ràng, không dựa cảm tính
2. **Value maximization** – NPV positive = tăng shareholder wealth
3. **Efficient allocation** – Scarce capital → đúng dự án nhất
4. **Accountability** – Post-audit giúp improve future decisions
5. **Risk awareness** – Sensitivity/Scenario analysis quantify risk
6. **Discipline** – Buộc management justify investments với data

### ❌ Nhược điểm:
1. **CF estimation difficult** – Revenue/cost 5-10 năm → high uncertainty
2. **Discount rate uncertain** – WACC thay đổi, project risk hard to estimate
3. **Intangibles ignored** – Strategic value, brand, knowledge khó lượng hóa
4. **Optimism bias** – Managers inflate projections để dự án được duyệt
5. **Real Options overlooked** – Traditional NPV bỏ qua flexibility value
6. **Short-term pressure** – Payback preference → miss long-term value
7. **Silo thinking** – Evaluate project individually, miss portfolio effects

---

## VI. CASE STUDY THÀNH CÔNG: Amazon AWS – Capital Budgeting Táo Bạo

### Bối cảnh
- 2003-2006: Amazon quyết định đầu tư **hàng tỷ USD** vào cloud computing (AWS)
- Thị trường "cloud" chưa tồn tại → Uncertainty cực cao
- Board question: Dùng tiền cho e-commerce hay infrastructure?

### Capital Budgeting Analysis (Giả lập)

| Năm | Item | CF (USD M) |
|-----|------|-----------|
| 0-2 | Data centers CAPEX | -$3,000 |
| 1-3 | Operating losses | -$1,500 |
| 4-5 | Break-even, revenue ramp | +$500 → +$2,000 |
| 6-8 | Market leader, scale | +$5,000 → +$15,000 |
| 10+ | Dominant, margin expansion | +$25,000/yr |

**NPV (r=12%, 10-year)**: >> +$50B

**IRR**: >> 35%

### Kết quả thực tế (2024)
- AWS Revenue: **$100B+/year**
- Operating Income: **$37B** (margin 37%)
- AWS = 62% tổng lợi nhuận Amazon
- Market share: **31%** global cloud (#1)
- Implied valuation: **$600-800B**

### Bài học Capital Budgeting
1. **Real Options massive**: $3B initial = "bought option" on entire cloud market. Fail → lose $3B. Win → gain $600B+. Asymmetric payoff!
2. **Traditional NPV undervalued**: NPV with conservative estimates → negative. But strategic value + option value → wildly positive
3. **Post-audit & iterate**: Liên tục thêm services → compound value
4. **Courage required**: CEO vision + conviction to invest despite short-term pain

---

## VII. CASE STUDY THẤT BẠI: Iridium Satellite – $5B Capital Budgeting Disaster

### Bối cảnh
- 1987-1998: Motorola đầu tư **$5 billion** vào 66 vệ tinh quỹ đạo thấp
- Mục tiêu: Global phone connectivity trước khi cellular towers phủ sóng
- **Dự án capital budgeting thất bại kinh điển nhất lịch sử**

### NPV Analysis lúc phê duyệt (1987)

| Giả định | Projected | Actual |
|----------|-----------|--------|
| Subscribers by 2000 | 5 million | 55,000 (!!!) |
| Revenue/user/month | $3,000 | Không đủ users |
| CAPEX | $3.4B | $5B (overrun 47%) |
| Time to profit | 2001 | NEVER |
| NPV (r=15%) | +$8B | << -$5B |

### Tại sao Capital Budgeting sai?

| Nguyên nhân | Chi tiết |
|------------|---------|
| **Technology change ignored** | Cell towers phủ sóng nhanh hơn dự kiến → Iridium obsolete TRƯỚC khi launch |
| **Sunk cost fallacy** | Đã đầu tư $2B → "Phải tiếp tục" → Throw good money after bad |
| **No scenario analysis** | Không xét "What if cellular wins?" |
| **CAPEX overrun** | $3.4B → $5B (+47%). Không có contingency |
| **Market research failure** | 5M subscribers assumed → Reality: phone to $3,000/unit, size bằng cục gạch |
| **Lack of flexibility** | 66 satellites committed → Cannot stop/modify midway |
| **Optimism bias** | Motorola engineers oversold technology vision |

### Kết quả
- 1999: Filed Chapter 11 bankruptcy (chỉ 9 tháng sau launch!)
- Loss: **$5 billion → bán cho nhà đầu tư mới với giá $25 million** (0.5% of cost)
- Motorola write-off: $2.6B

### Bài học từ thất bại

```
1. STAGE-GATE PROCESS: Không commit toàn bộ $5B upfront
   → Chia thành stages, review mỗi stage
   
2. REAL OPTIONS THINKING: Option to abandon at each gate
   → Kill early if assumptions wrong

3. COMPETITIVE DYNAMICS: Capital budgeting PHẢI xét
   competitive response & technology substitution

4. SUNK COST DISCIPLINE: "Already spent $2B" ≠ reason to continue
   → Evaluate FORWARD-LOOKING NPV only

5. POST-AUDIT CULTURE: Monitor assumptions quarterly
   → If subscribers << projection → STOP

6. INDEPENDENT REVIEW: Engineers too optimistic about own tech
   → External market validation required
```

### So sánh AWS vs Iridium

| Tiêu chí | AWS (Success) | Iridium (Failure) |
|----------|--------------|------------------|
| Market timing | Right (cloud demand growing) | Wrong (cellular killed need) |
| Alternatives | No competing solution existed | Cellular towers = better & cheaper |
| Flexibility | Modular (add services) | Committed (66 satellites fixed) |
| Capital commitment | Staged investment | Massive upfront $5B locked |
| Demand validation | Internal use first (Amazon.com) | Zero validation before $5B |
| Competitive response | First-mover, no substitute | Cell companies dropped prices |
| Post-audit | Continuous monitoring | Ignored warning signals |

---

## VIII. CAPITAL BUDGETING TRONG THỜI ĐẠI SỐ (4.0)

### Thay đổi trong kỷ nguyên số

| Traditional | Digital Era |
|------------|-------------|
| Linear CF growth | Exponential/S-curve growth |
| Tangible assets (nhà máy) | Intangible (data, platform, network) |
| Known market size | Market may not exist yet |
| Stable competition | Winner-take-all/most |
| 5-year horizon | 10-15+ year payoff |
| CAPEX then OPEX | OPEX-heavy (cloud, subscription) |

### Adjusted Framework

$$\text{Digital NPV} = NPV_{traditional} + NPV_{network\,effects} + NPV_{data\,asset} + Option\,Value$$

---

## IX. CHECKLIST CAPITAL BUDGETING

```
CHUẨN BỊ:
□ Dự án phù hợp chiến lược DN?
□ Xác định đầy đủ CF: initial + operating + terminal?
□ Incremental CF only (loại sunk cost, tính opportunity cost)?
□ After-tax cash flows?
□ Depreciation tax shield calculated?
□ Working capital changes included?

PHÂN TÍCH:
□ NPV calculated? NPV > 0?
□ IRR calculated? IRR > WACC?
□ Payback Period acceptable?
□ PI > 1? (especially if capital rationed)
□ NPV vs IRR conflict resolved?

RISK:
□ Sensitivity Analysis done?
□ Scenario Analysis (best/base/worst)?
□ Real Options considered?
□ Break-even analysis?
□ Competitive response considered?

DECISION & FOLLOW-UP:
□ Independent review of assumptions?
□ Stage-gate process for large projects?
□ Post-audit plan established?
□ Actual vs Projected tracking?
□ Kill criteria defined? (when to abandon)
```

---

*Tài liệu tham khảo: Brealey, Myers & Allen "Principles of Corporate Finance" 14th Ed; Ross, Westerfield & Jordan "Corporate Finance" 13th Ed; Dixit & Pindyck "Investment Under Uncertainty" (Real Options); CFA Level I – Corporate Issuers*
