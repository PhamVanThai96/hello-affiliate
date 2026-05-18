# Capital Structure – Cơ Cấu Vốn (Modigliani-Miller)

> **Mục tiêu**: Hiểu lý thuyết cơ cấu vốn tối ưu, Modigliani-Miller, Trade-off Theory, Pecking Order Theory và ứng dụng thực tiễn trong quyết định tài trợ.

---

## I. ĐỊNH NGHĨA VÀ LÝ THUYẾT NỀN TẢNG

### 1. Định nghĩa

**Capital Structure** (Cơ cấu vốn) là **tỷ lệ phối hợp giữa NỢ (Debt) và VỐN CHỦ SỞ HỮU (Equity)** mà doanh nghiệp sử dụng để tài trợ cho hoạt động và đầu tư.

> **Câu hỏi cốt lõi**: DN nên vay bao nhiêu và huy động vốn cổ đông bao nhiêu? Có tỷ lệ D/E TỐI ƯU để minimize WACC & maximize firm value?

### 2. Debt vs Equity

| Tiêu chí | Debt (Nợ) | Equity (Vốn CSH) |
|----------|----------|------------------|
| **Bản chất** | Vay, bắt buộc trả | Góp vốn, không bắt buộc trả |
| **Chi phí** | Lãi suất cố định | Cổ tức + capital gain (biến động) |
| **Tax** | Lãi vay khấu trừ thuế ✅ | Cổ tức KHÔNG khấu trừ ❌ |
| **Rủi ro cho DN** | Cao (phá sản nếu không trả) | Thấp (không bắt buộc trả cổ tức) |
| **Quyền kiểm soát** | Không pha loãng ownership | Pha loãng ownership |
| **Chi phí vốn** | Thấp hơn (Kd < Ke) | Cao hơn (Ke > Kd) |
| **Priority** | Trả TRƯỚC khi phá sản | Nhận SAU cùng (residual) |

### 3. Các lý thuyết chính

```
┌──────────────────────────────────────────────────────────────┐
│              CÁC LÝ THUYẾT CƠ CẤU VỐN                      │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  1. MODIGLIANI-MILLER (1958, 1963)                          │
│     → Capital structure irrelevance (no tax)                 │
│     → Tax shield makes debt valuable (with tax)             │
│                                                              │
│  2. TRADE-OFF THEORY                                         │
│     → Optimal D/E = Balance tax shield vs distress costs     │
│                                                              │
│  3. PECKING ORDER THEORY (Myers & Majluf, 1984)             │
│     → Internal funds > Debt > Equity (info asymmetry)        │
│                                                              │
│  4. MARKET TIMING THEORY (Baker & Wurgler, 2002)            │
│     → Issue equity when overvalued, debt when undervalued    │
│                                                              │
│  5. AGENCY THEORY (Jensen, 1986)                             │
│     → Debt disciplines managers (reduce free cash flow)      │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## II. PHÂN TÍCH ĐỊNH LƯỢNG – MODIGLIANI-MILLER

### A. M&M Proposition I – Without Taxes (1958)

#### Statement
> Trong thị trường hoàn hảo (no taxes, no bankruptcy costs, no asymmetric info), **giá trị doanh nghiệp KHÔNG phụ thuộc vào cơ cấu vốn**.

$$V_L = V_U$$

- $V_L$ = Value of levered firm (có nợ)
- $V_U$ = Value of unlevered firm (không nợ)

#### Ý nghĩa
"Cắt pizza thành 4 hay 8 miếng không thay đổi kích thước pizza." – Cơ cấu vốn chỉ là cách CHIA value, không THAY ĐỔI value.

#### Assumptions (Rất quan trọng!)
1. No taxes
2. No bankruptcy/distress costs
3. No transaction costs
4. Symmetric information
5. Individuals can borrow at same rate as firms
6. No agency costs

→ **Trong thực tế**: KHÔNG có giả định nào đúng 100% → M&M I là benchmark lý thuyết

---

### B. M&M Proposition II – Without Taxes

$$K_e = K_0 + (K_0 - K_d) \times \frac{D}{E}$$

- $K_0$ = Cost of capital of all-equity firm (unlevered)
- $K_e$ tăng linear với D/E ratio

#### Biểu đồ

```
Cost of Capital
  │
  │         Ke ↗ (tăng linear với D/E)
  │       ╱
  │     ╱
  │   ╱
  │─╱──────────── K₀ (WACC = constant!)
  │╱
  │─────────────── Kd (constant)
  │
  └──────────────────────→ D/E ratio

WACC = KHÔNG ĐỔI (vì Ke tăng exactly offset lợi ích debt rẻ hơn)
→ Leverage tăng Ke đủ để offset Kd thấp → WACC flat
```

---

### C. M&M Proposition I – With Taxes (1963)

$$V_L = V_U + T \times D$$

- **Tax Shield** = $T \times D$ = Giá trị hiện tại của tax shield từ debt
- Debt TẠO GIÁ TRỊ vì lãi vay khấu trừ thuế!

#### Ví dụ

DN có EBIT = 100 tỷ, T = 20%:

| | All-Equity (VU) | 50% Debt (VL) |
|-|-----------------|---------------|
| EBIT | 100 | 100 |
| Interest (D=500, Kd=8%) | 0 | -40 |
| EBT | 100 | 60 |
| Tax (20%) | -20 | -12 |
| Net Income | 80 | 48 |
| + Interest to debtholders | 0 | +40 |
| **Total to all investors** | **80** | **88** |

→ Total CF tăng 8 tỷ = Tax Shield = 40 × 20% = 8 tỷ/năm

$$PV(Tax Shield) = \frac{T \times K_d \times D}{K_d} = T \times D = 20\% \times 500 = 100 \text{ tỷ}$$

#### Implication
**Theo M&M with taxes**: 100% debt = maximize value???

→ Nhưng thực tế KHÔNG ai dùng 100% debt vì... **Bankruptcy Costs**!

---

### D. Trade-Off Theory

$$V_L = V_U + PV(Tax Shield) - PV(Financial Distress Costs)$$

#### Biểu đồ Trade-Off

```
Firm Value (V)
  │
  │           VL = VU + Tax Shield (M&M with tax)
  │          ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
  │        ╱     ╭─── Optimal!
  │      ╱     ╱│ ╲
  │    ╱     ╱  │   ╲   ← PV(Distress) tăng
  │  ╱    ╱    │     ╲
  │╱───────────│───────╲──── VU (no debt)
  │            │         ╲
  │       Optimal         ╲
  │        D/E*              ╲
  └────────────┼──────────────╲──→ D/E ratio
               │
          Tax Shield = Distress Cost at margin
```

#### Financial Distress Costs

| Loại | Ví dụ | Estimate |
|------|-------|----------|
| **Direct** | Legal fees, court costs, accountants | 3-5% firm value |
| **Indirect** | Customer loss, supplier tightening, talent flight | 10-20% firm value |
| **Agency** | Risk shifting, underinvestment, asset stripping | 5-10% firm value |

#### Optimal Capital Structure

$$Optimal D/E: \text{ where marginal tax shield = marginal distress cost}$$

Typical optimal ranges by industry:

| Industry | Optimal D/E | Lý do |
|----------|------------|-------|
| Utilities | 60-70% debt | Stable CF, tangible assets |
| Real Estate | 50-60% debt | Asset-backed, predictable income |
| Manufacturing | 30-50% debt | Moderately stable, tangible |
| Technology | 0-20% debt | Volatile, intangible assets |
| Biotech/Startup | 0-5% debt | No revenue, burning cash |

---

### E. Pecking Order Theory (Myers & Majluf, 1984)

#### Core Idea
Do **information asymmetry** (manager biết nhiều hơn market), DN follow hierarchy:

```
1️⃣ INTERNAL FUNDS (Retained Earnings) ← Preferred
   │ Không cần approval, no dilution, no issuance cost
   ▼
2️⃣ DEBT
   │ Less info-sensitive, fixed claim, tax shield
   │ Market "underreacts" to debt issue
   ▼
3️⃣ EQUITY (Last resort) ← Least preferred
   Market interprets equity issue as "stock overvalued"
   → Stock price drops 2-3% on announcement
```

#### Empirical Evidence
- Profitable firms ITHƯỜNG có LESS debt (dùng retained earnings) → Ngược Trade-Off!
- Equity issuance → Stock drops 2-3% (consistent with adverse selection)
- Leverage increases when firms have funding deficits

---

### F. Agency Theory & Free Cash Flow

#### Jensen's Free Cash Flow Theory (1986)
- **Debt = Discipline device**: Buộc managers trả interest → Ít tiền để invest lãng phí
- Firms with high free cash flow + low growth → Nên dùng MORE debt
- LBO (Leveraged Buyout) = extreme form: load debt to discipline

#### Agency Costs of Equity vs Debt

| | Equity Agency Cost | Debt Agency Cost |
|-|-------------------|-----------------|
| Problem | Managers waste FCF (empire building) | Risk shifting, underinvestment |
| Solution | More debt, buyback | Covenants, monitoring |
| Example | Conglomerate discount | Risky project cho "Hail Mary" |

---

## III. ỨNG DỤNG VÀ HOÀN CẢNH ÁP DỤNG

### Capital Structure Decision Framework

```
CÂU HỎI QUYẾT ĐỊNH CƠ CẤU VỐN:

1. Thuế suất cao không?
   • Cao → Debt có tax shield lớn → More debt
   • Thấp/0 → Tax shield nhỏ → Less debt

2. Thu nhập ổn định không?
   • Stable (utilities) → Chịu được debt cao
   • Volatile (tech, startup) → Debt thấp

3. Tài sản hữu hình nhiều không?
   • Tangible (BĐS, máy móc) → Collateral dễ → Debt OK
   • Intangible (tech, brand) → Khó thế chấp → Less debt

4. Growth opportunities cao không?
   • High growth → Cần flexibility → Less debt (Pecking Order)
   • Low growth, high FCF → More debt (discipline)

5. Industry norm?
   • So sánh D/E với peers → Deviation cần justified

6. Financial flexibility cần không?
   • Uncertain future → Giữ debt capacity reserve
   • "Dry powder" for opportunities
```

### EBIT-EPS Analysis

Tìm EBIT breakeven giữa Debt vs Equity financing:

$$EPS_{Debt} = \frac{(EBIT - Interest) \times (1-T)}{Shares_{existing}}$$

$$EPS_{Equity} = \frac{EBIT \times (1-T)}{Shares_{existing} + New shares}$$

Set equal → Find EBIT* indifference point

---

## IV. ƯU ĐIỂM VÀ NHƯỢC ĐIỂM

### ✅ Ưu điểm sử dụng Debt:
1. **Tax shield** – Lãi vay khấu trừ thuế → giảm WACC
2. **Discipline** – Buộc management cẩn trọng (Jensen FCF theory)
3. **No dilution** – Không pha loãng ownership/control
4. **Lower cost** – Kd < Ke (always)
5. **Leverage amplifies ROE** – Khi ROIC > Kd → ROE tăng

### ❌ Nhược điểm sử dụng Debt:
1. **Bankruptcy risk** – Không trả được → phá sản, mất toàn bộ
2. **Financial distress costs** – Direct + Indirect costs rất lớn
3. **Reduced flexibility** – Fixed obligations reduce strategic options
4. **Covenants** – Ràng buộc hoạt động (D/E < 2x, DSCR > 1.5x)
5. **Amplifies losses** – Khi ROIC < Kd → ROE giảm nhanh, equity wiped out

### Financial Leverage Effect on ROE

| ROIC | All-Equity ROE | D/E = 1.0, Kd = 6% | D/E = 2.0, Kd = 7% |
|------|---------------|--------------------|--------------------|
| 15% | 15% | 24% ✅ Amplified! | 31% ✅✅ |
| 10% | 10% | 14% ✅ Still good | 16% ✅ |
| 6% | 6% | 6% ⚠️ No benefit | 5% ⚠️ |
| 3% | 3% | 0% ❌ Wiped | -5% ❌❌ Destroyed! |

---

## V. CASE STUDY THÀNH CÔNG: Microsoft – Thay đổi Capital Structure chiến lược

### Bối cảnh
- Pre-2009: Microsoft gần như ZERO debt (pure equity financed)
- 2009+: Bắt đầu phát hành bonds, tăng leverage
- 2024: ~$80B debt, D/E ≈ 0.35

### Tại sao Microsoft thêm Debt?

| Lý do | Chi tiết |
|-------|---------|
| **Tax shield** | $80B × Kd(3%) × T(21%) = ~$500M/yr tax savings |
| **Low interest rates** | 2010-2021: borrowed at 2-3% (historically cheap) |
| **Excess cash overseas** | Pre-2017 tax reform: repatriation costly → borrow domestically |
| **Acquisition financing** | $69B Activision deal partly debt-funded |
| **Shareholder returns** | Fund $20B+/yr buybacks without selling assets |
| **Still conservative** | D/E = 0.35 vs industry avg higher → AAA credit maintained |

### WACC Impact

| Period | D/E | Ke | Kd(after-tax) | WACC |
|--------|-----|-----|--------------|------|
| Pre-2009 | 0% | 10% | - | 10.0% |
| 2015 | 20% | 9.5% | 2.0% | 8.0% |
| 2024 | 35% | 9.5% | 2.5% | 7.3% |

→ WACC decreased 2.7% → **Enterprise value increased ~30-40%** just from capital structure optimization!

### Bài học
1. Zero debt ≠ optimal (miss tax shield value)
2. High credit quality → very cheap debt available
3. Gradual leverage increase = safe optimization
4. Fund growth (M&A) without diluting shareholders

---

## VI. CASE STUDY THẤT BẠI: Evergrande – Debt-fueled Growth → Catastrophic Collapse

### Bối cảnh
- China Evergrande: Largest Chinese property developer
- Strategy: Borrow aggressively → Buy land → Build → Sell → Borrow more
- Peak debt: **$300B+** (!!!) D/E ≈ 6-8x

### Capital Structure Timeline

| Year | Total Debt | D/E Ratio | Strategy |
|------|-----------|-----------|----------|
| 2010 | $30B | 2.0x | Growing fast |
| 2015 | $95B | 3.5x | Aggressive expansion |
| 2018 | $180B | 5.0x | Diversifying (EV, football) |
| 2020 | $300B | 6-8x | **"Three Red Lines" hit** |
| 2021 | $300B+ | Negative equity | **DEFAULT → Collapse** |

### Tại sao thất bại?

| Factor | Chi tiết |
|--------|---------|
| **"Three Red Lines" policy** | China gov: cap D/E, limit borrowing → Evergrande CANNOT refinance |
| **Trade-Off Theory violation** | D/E = 6-8x → WAY beyond optimal → Distress costs dominates |
| **Maturity mismatch** | Short-term debt fund long-term projects → Liquidity crisis |
| **Asset-liability mismatch** | Illiquid real estate assets vs callable short-term liabilities |
| **No margin of safety** | ZERO financial flexibility. Any shock → cascade failure |
| **Ponzi-like structure** | Need new borrowing to pay old debt → Unsustainable |

### Pecking Order Theory Perspective
- Evergrande violated ALL theories:
  - No internal funds (paying massive dividends despite debt!)
  - Debt not "conservative step 2" → Went ALL IN on debt
  - Equity issued at peak to insiders (market timing for personal gain)

### Kết quả
- 2021: Defaulted on $300B+ debt
- 2024: Ordered to liquidate
- Founder's wealth: $42B → $0
- Contagion: Broader China property crisis, affecting Country Garden, Sunac, etc.
- Homebuyers: 1.6 million undelivered homes

### Bài học Capital Structure
1. **There IS an optimal leverage** – Trade-Off Theory correct. Beyond it → destruction
2. **Growth funded by debt alone = house of cards** – Duh needs internal CF generation
3. **Regulatory risk** – Capital structure must account for policy changes
4. **D/E > 3x for non-financials = danger zone** – Especially with short-term debt
5. **Pecking Order wisdom** – Conservative financing → survival in downturns

---

## VII. LƯU Ý VỀ PHƯƠNG PHÁP

### So sánh các lý thuyết – Khi nào đúng?

| Lý thuyết | Predicts | Empirical support | Best for |
|-----------|---------|------------------|----------|
| M&M (no tax) | D/E doesn't matter | ❌ In practice it does | Benchmark/teaching |
| M&M (tax) | 100% debt optimal | ❌ No firm does this | Showing tax shield value |
| Trade-Off | Optimal D/E exists | ✅ Cross-sectional | Mature, profitable firms |
| Pecking Order | Profitable firms = less debt | ✅ Time-series | Growth firms, tech |
| Market Timing | Structure = cumulative timing | ⚠️ Some evidence | IPO decisions |
| Agency | Debt disciplines FCF | ✅ LBOs, oil companies | High FCF, low growth |

### Key Formulas

| Formula | Use |
|---------|-----|
| $V_L = V_U + T \times D$ | M&M with tax |
| $K_e = K_0 + (K_0 - K_d)(1-T)(D/E)$ | M&M Ke with tax |
| $WACC = (E/V)K_e + (D/V)K_d(1-T)$ | Weighted cost |
| $\beta_L = \beta_U[1 + (1-T)(D/E)]$ | Hamada equation |
| $Degree\,of\,Financial\,Leverage = \%\Delta EPS / \%\Delta EBIT$ | DFL |

---

## VIII. CHECKLIST CAPITAL STRUCTURE

```
PHÂN TÍCH:
□ D/E ratio hiện tại vs peers/industry?
□ WACC tối ưu tại D/E nào?
□ Tax shield value bao nhiêu?
□ Distress probability & costs estimated?
□ Debt capacity (max debt before distress)?

QUYẾT ĐỊNH:
□ Business stability → chịu được leverage?
□ Asset tangibility → collateral available?
□ Growth needs → need flexibility?
□ Tax rate → tax shield meaningful?
□ Management discipline needed → more debt?
□ Pecking Order: Internal funds available first?

RISK CHECKS:
□ Interest Coverage Ratio > 3x?
□ Debt/EBITDA < 3-4x?
□ Debt maturity schedule → no cliff?
□ Covenant compliance comfortable?
□ Stress test: Can survive revenue -30%?
□ Financial flexibility reserve maintained?
```

---

*Tài liệu tham khảo: Modigliani & Miller (1958, 1963); Myers & Majluf "Pecking Order" (1984); Jensen "Agency Costs of FCF" (1986); Brealey, Myers & Allen 14th Ed; Damodaran "Applied Corporate Finance"*
