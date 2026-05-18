# Corporate Valuation – Định Giá Doanh Nghiệp (DCF, Comparables, Precedent)

> **Mục tiêu**: Nắm vững 3 phương pháp định giá chính: DCF (Discounted Cash Flow), Comparable Companies Analysis, Precedent Transactions – với phân tích định lượng đầy đủ và case study thực tiễn.

---

## I. ĐỊNH NGHĨA VÀ LÝ THUYẾT NỀN TẢNG

### 1. Định nghĩa

**Corporate Valuation** (Định giá doanh nghiệp) là quá trình **xác định giá trị kinh tế nội tại** (intrinsic value) của một doanh nghiệp, dựa trên phân tích tài chính, dòng tiền tương lai, và so sánh thị trường.

> **"Price is what you pay, value is what you get."** – Warren Buffett
> Price (giá thị trường) ≠ Value (giá trị thực). Valuation đi tìm VALUE.

### 2. Khi nào cần định giá?

| Tình huống | Mục đích |
|-----------|---------|
| **M&A** | Bên mua: trả bao nhiêu? Bên bán: chấp nhận bao nhiêu? |
| **IPO** | Xác định giá phát hành cổ phiếu lần đầu |
| **Investment** | Cổ phiếu overvalued hay undervalued? Buy/Sell/Hold? |
| **Fundraising** | Startup gọi vốn: pre-money valuation bao nhiêu? |
| **Legal/Tax** | Ly hôn, thừa kế, thuế chuyển nhượng |
| **Internal strategy** | Nên giữ, bán, hay spin-off division? |
| **Restructuring** | Bankruptcy, turnaround – value of going concern vs liquidation |
| **Fairness opinion** | Independent valuation for board/shareholder approval |

### 3. Enterprise Value vs Equity Value

```
┌──────────────────────────────────────────────────────┐
│                                                      │
│  ENTERPRISE VALUE (EV) = Giá trị DN toàn bộ         │
│  (cho cả Debt holders + Equity holders)              │
│                                                      │
│  EV = Equity Value + Net Debt                        │
│     = Market Cap + Total Debt - Cash & Equivalents   │
│                                                      │
│  ┌─────────────────────────────────┐                 │
│  │  EQUITY VALUE                   │                 │
│  │  = Giá trị phần cổ đông        │                 │
│  │  = EV - Net Debt                │                 │
│  │  = Market Cap                   │                 │
│  │  = Share Price × Shares O/S     │                 │
│  └─────────────────────────────────┘                 │
│  ┌─────────────────────────────────┐                 │
│  │  NET DEBT                       │                 │
│  │  = Total Debt - Cash            │                 │
│  │  = Phần chủ nợ                  │                 │
│  └─────────────────────────────────┘                 │
│                                                      │
│  BRIDGE:                                             │
│  EV    → discount FCFF (Free CF to Firm) at WACC    │
│  Equity → discount FCFE (Free CF to Equity) at Ke   │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### 4. Tổng quan 3 phương pháp

```
┌────────────────────────────────────────────────────────────────┐
│                   3 APPROACHES TO VALUATION                    │
├─────────────────┬──────────────────────┬───────────────────────┤
│   INTRINSIC     │     RELATIVE         │     RELATIVE          │
│   (DCF)         │  (Comps - Trading)   │  (Precedent Txns)     │
├─────────────────┼──────────────────────┼───────────────────────┤
│ PV of future    │ Compare multiples    │ Compare multiples     │
│ free cash flows │ to PUBLICLY TRADED   │ from PAST M&A         │
│                 │ similar companies    │ TRANSACTIONS           │
├─────────────────┼──────────────────────┼───────────────────────┤
│ What is the     │ What is the market   │ What have acquirers   │
│ company WORTH?  │ PAYING for similar?  │ PAID for similar?     │
├─────────────────┼──────────────────────┼───────────────────────┤
│ • Forward-look  │ • Market-based       │ • Includes control    │
│ • Most rigorous │ • Easy to compute    │   premium             │
│ • Most          │ • Market consensus   │ • Transaction-based   │
│   assumptions   │ • May be mispriced   │ • Data may be stale   │
└─────────────────┴──────────────────────┴───────────────────────┘
```

---

## II. PHÂN TÍCH ĐỊNH LƯỢNG

### A. DCF – Discounted Cash Flow (Phương pháp chiết khấu dòng tiền)

#### Core Formula

$$EV = \sum_{t=1}^{n} \frac{FCFF_t}{(1+WACC)^t} + \frac{Terminal\,Value}{(1+WACC)^n}$$

#### Step-by-Step DCF Process

```
Step 1: PROJECT FREE CASH FLOW (5-10 years)
   │  Revenue → EBIT → NOPAT → FCFF
   ▼
Step 2: CALCULATE WACC
   │  Ke (CAPM) + Kd(1-T) weighted
   ▼
Step 3: CALCULATE TERMINAL VALUE
   │  Gordon Growth OR Exit Multiple
   ▼
Step 4: DISCOUNT ALL CASH FLOWS
   │  PV(FCF) + PV(TV) = Enterprise Value
   ▼
Step 5: BRIDGE TO EQUITY VALUE
   │  Equity = EV - Net Debt + Non-operating assets
   ▼
Step 6: PER-SHARE VALUE
   Equity Value / Diluted Shares = Intrinsic Value per Share
```

#### Free Cash Flow to Firm (FCFF)

$$FCFF = EBIT \times (1-T) + D\&A - CAPEX - \Delta NWC$$

| Component | Source | Note |
|-----------|--------|------|
| EBIT × (1-T) | Income Statement | = NOPAT |
| + D&A | Income Statement/CF | Add back non-cash expense |
| - CAPEX | CF Statement (Investing) | Maintenance + Growth |
| - ΔNWC | Balance Sheet changes | Increase = cash outflow |

#### Terminal Value – 2 Methods

**Method 1: Gordon Growth Model (Perpetuity)**

$$TV = \frac{FCFF_{n+1}}{WACC - g} = \frac{FCFF_n \times (1+g)}{WACC - g}$$

- $g$ = Long-term sustainable growth rate (typically 2-4%, ≤ GDP growth)
- **WARNING**: TV usually = 60-80% of total DCF value → Extremely sensitive to g!

**Method 2: Exit Multiple**

$$TV = EBITDA_n \times Exit\,Multiple$$

- Exit Multiple = EV/EBITDA multiple at exit (from comparables)
- More "market-based" but circular (uses relative valuation IN intrinsic method)

#### DCF Example – Tech Company Valuation

**Assumptions**:
- Revenue Y1: 1,000 tỷ VND, growing 15% → tapering to 5%
- EBIT margin: 20% → expanding to 25%
- Tax: 20%, D&A: 5% revenue, CAPEX: 7% revenue
- ΔNWC: 3% of ΔRevenue
- WACC: 11%, Terminal g: 3%

| Year | Revenue | EBIT | NOPAT | D&A | CAPEX | ΔNWC | FCFF |
|------|---------|------|-------|-----|-------|------|------|
| 1 | 1,000 | 200 | 160 | 50 | 70 | 0 | 140 |
| 2 | 1,150 | 242 | 193 | 58 | 81 | 5 | 165 |
| 3 | 1,300 | 286 | 229 | 65 | 91 | 5 | 198 |
| 4 | 1,450 | 333 | 266 | 73 | 102 | 5 | 232 |
| 5 | 1,580 | 395 | 316 | 79 | 111 | 4 | 280 |

$$TV = \frac{280 \times 1.03}{0.11 - 0.03} = \frac{288.4}{0.08} = 3,605 \text{ tỷ}$$

| Component | Value | PV (at WACC 11%) |
|-----------|-------|-----------------|
| PV(FCFF Year 1-5) | | 720 tỷ |
| PV(Terminal Value) | 3,605 | 2,135 tỷ |
| **Enterprise Value** | | **2,855 tỷ** |
| - Net Debt | | (300 tỷ) |
| **Equity Value** | | **2,555 tỷ** |
| ÷ Shares | | 100 triệu |
| **Value per Share** | | **25,550 VND** |

→ TV = 75% of total value! Very sensitive to growth assumption.

#### DCF Sensitivity Table

| | g = 2% | g = 3% | g = 4% |
|-|--------|--------|--------|
| **WACC = 9%** | 28,200 | 33,500 | 42,100 |
| **WACC = 10%** | 25,100 | 28,900 | 34,500 |
| **WACC = 11%** | 22,500 | 25,550 | 29,600 |
| **WACC = 12%** | 20,300 | 22,700 | 25,800 |
| **WACC = 13%** | 18,500 | 20,400 | 22,800 |

→ Range: 18,500 – 42,100 VND! WACC and g assumptions dominate!

---

### B. Comparable Companies Analysis ("Comps" / Trading Multiples)

#### Process

```
1. SELECT comparable companies (same industry, size, growth, profitability)
2. CALCULATE their trading multiples
3. APPLY median/mean multiple to target's metrics
4. DERIVE implied valuation range
```

#### Key Multiples

| Multiple | Formula | Best for |
|----------|---------|----------|
| **EV/Revenue** | Enterprise Value / Revenue | Pre-profit companies (SaaS, biotech) |
| **EV/EBITDA** | EV / EBITDA | Most common corporate valuation |
| **EV/EBIT** | EV / EBIT | When D&A distorts EBITDA |
| **P/E** | Price / EPS | Equity value, mature companies |
| **P/B** | Price / Book Value | Banks, asset-heavy industries |
| **P/FCF** | Price / Free Cash Flow | Cash flow-focused analysis |
| **EV/Subscribers** | | Telecom, streaming, SaaS |

#### Comps Example

**Target**: VN-based e-commerce company, Revenue = 5,000 tỷ, EBITDA = 400 tỷ

| Comparable | EV/Revenue | EV/EBITDA |
|-----------|-----------|-----------|
| MWG (VN) | 0.8x | 10.5x |
| FPT Retail (VN) | 0.5x | 8.2x |
| Sea Limited (SE Asia) | 2.5x | 25x |
| Tokopedia/GoTo (Indo) | 1.5x | NM (not meaningful, negative EBITDA) |
| **Median** | **1.15x** | **10.5x** |

**Implied Valuation**:
- EV/Revenue: 5,000 × 1.15 = **5,750 tỷ VND**
- EV/EBITDA: 400 × 10.5 = **4,200 tỷ VND**
- Range: **4,200 – 5,750 tỷ VND**

#### Advantages & Disadvantages of Comps

| ✅ Advantages | ❌ Disadvantages |
|-------------|---------------|
| Market-based (reflects investor sentiment) | May be over/undervalued (market mispricing) |
| Simple, quick calculation | "No two companies truly comparable" |
| Always available (if public peers) | Different growth, margin, risk → different multiple |
| Consensus view | Multiples change with market sentiment |

---

### C. Precedent Transactions Analysis

#### Process

```
1. IDENTIFY past M&A transactions in similar industry
2. CALCULATE transaction multiples (include control premium!)
3. APPLY to target's metrics
4. ADJUST for market conditions, timing, synergies
```

#### Key Differences vs Trading Comps

| | Trading Comps | Precedent Transactions |
|-|---------------|----------------------|
| Data source | Current stock prices | Past M&A deal prices |
| Premium | No control premium | INCLUDES 20-50% control premium |
| Timing | Current market | Historical (may be stale) |
| Relevance | Market value | Acquisition value |
| Availability | Always (if public) | Limited (fewer deals) |

#### Precedent Transactions Example

| Transaction | Year | EV/EBITDA | EV/Revenue | Premium |
|-------------|------|-----------|-----------|---------|
| Deal A (same sector) | 2024 | 12.0x | 1.8x | 35% |
| Deal B | 2023 | 11.5x | 1.5x | 28% |
| Deal C | 2023 | 14.0x | 2.2x | 42% |
| Deal D | 2022 | 10.0x | 1.3x | 25% |
| **Median** | | **11.75x** | **1.65x** | **31.5%** |

**Implied Valuation** (Target EBITDA = 400 tỷ):
- EV = 400 × 11.75 = **4,700 tỷ VND** (including control premium)

---

### D. Tổng hợp – "Football Field" Valuation

```
Method              │ Low    │  Mid   │  High  │
────────────────────┼────────┼────────┼────────┤
52-Week Range       │ 3,500  │ 4,200  │  4,800 │
                    │████████│████████│████████│
DCF (WACC ±1%)     │ 4,000  │ 5,100  │  6,500 │
                    │████████│████████│████████│████
Trading Comps       │ 4,200  │ 5,000  │  5,750 │
                    │████████│████████│████████│
Precedent Txns      │ 4,500  │ 5,300  │  6,200 │
                    │████████│████████│████████│████
LBO (PE buyer)      │ 3,800  │ 4,500  │  5,500 │
                    │████████│████████│████████│
                    └────────┴────────┴────────┘
                             (tỷ VND)

→ CONCLUSION: Fair value range 4,500 – 5,500 tỷ VND
→ Offer price (with premium): 5,000 – 6,000 tỷ VND
```

---

## III. ƯU ĐIỂM VÀ NHƯỢC ĐIỂM

### ✅ DCF Ưu điểm:
1. **Intrinsic** – Based on fundamentals, not market sentiment
2. **Forward-looking** – Future cash flows, not just current state
3. **Flexible** – Can model ANY business, ANY assumption
4. **Theoretically sound** – PV of future cash = true value

### ❌ DCF Nhược điểm:
1. **Sensitive** – Small changes in WACC/g → huge valuation swing
2. **Terminal value dominated** – TV = 60-80% of value → uncertain assumption drives all
3. **Garbage in = Garbage out** – FCF projections highly uncertain (5-10+ years)
4. **Complex** – Requires many assumptions, easy to manipulate
5. **Difficult for pre-revenue** – No cash flow → DCF = $0? (need creative approaches)

### ✅ Comps Ưu điểm:
1. **Simple & Quick** – Calculate in minutes
2. **Market-based** – Reflects what investors actually pay
3. **Always available** – If peer companies are public
4. **Easy to explain** – "Trading at 12x EBITDA like peers"

### ❌ Comps Nhược điểm:
1. **No true comp** – Every company is unique
2. **Circular** – If all peers overvalued → you get overvaluation
3. **Ignores DCF fundamentals** – Might miss growth/risk differences
4. **Manipulation** – Cherry-pick comps to get desired answer

---

## IV. CASE STUDY THÀNH CÔNG: Microsoft mua LinkedIn ($26.2B, 2016)

### Valuation Analysis

**LinkedIn at acquisition**:
- Market Cap: ~$26B (at offer, including premium)
- Revenue: $3B (growing 35%/yr)
- EBITDA: $450M
- Users: 433 million professionals

| Method | Implied Value | Multiple |
|--------|--------------|---------|
| DCF (WACC 9%, g 3%) | $28-35B | - |
| EV/Revenue (peers: 6-8x) | $18-24B | 8.7x revenue (paid) |
| EV/EBITDA | - | 58x EBITDA (!!) |
| Precedent (social/platform deals) | $22-30B | Consistent |
| **Paid** | **$26.2B** | **Premium 50%** |

### Why $26.2B was justified (despite 58x EBITDA!)

| Revenue Synergy | Microsoft Estimate | Realized? |
|-----------------|-------------------|-----------|
| LinkedIn Sales Navigator + Dynamics CRM | $1B+ | ✅ $1.5B+ |
| LinkedIn data + Microsoft products | $500M+ | ✅ Yes |
| LinkedIn Learning (enterprise) | $300M+ | ✅ Yes |
| Advertising growth (Microsoft Audience Network) | $500M+ | ✅ Yes |

### Result (2024):
- LinkedIn Revenue: **$16B+** (from $3B at acquisition!)
- Growth: 5x revenue in 8 years
- Users: 1 billion+
- Strategic value: Microsoft ecosystem integration (Teams, Outlook, Office)
- **ROI: $26B invested → Business worth $80-100B+ today**

### Bài học
1. **Pay for growth**: 58x EBITDA looks crazy, but if revenue 5x in 8 years → reasonable
2. **Strategic value > financial**: LinkedIn IN Microsoft ecosystem > standalone
3. **Platform network effects**: More users → more value → more users
4. **Patient capital**: Microsoft didn't demand immediate profitability

---

## V. CASE STUDY THẤT BẠI: HP mua Autonomy ($11.1B, 2012) – Valuation Disaster

### Bối cảnh
- 2011: HP acquires UK software company Autonomy for **$11.1B**
- 1 year later: HP writes off **$8.8B** (79% of purchase price!)
- Allegation: Autonomy inflated revenues through accounting fraud

### Valuation at Acquisition

| Metric | Autonomy (reported) | Reality |
|--------|--------------------|---------| 
| Revenue | $1B | ~$700M (after excluding hardware reselling) |
| EBITDA margin | 40%+ | ~25% (real software only) |
| Growth rate | 15-20% | 5-10% (organic) |
| EV/Revenue paid | 11x | 16x (on real revenue) |
| EV/EBITDA paid | 25x | 40x+ (on real metrics) |

### What Went Wrong

| Factor | Detail |
|--------|--------|
| **Revenue inflation** | Autonomy sold hardware at LOSS to boost revenue (recognized as "software") |
| **Channel stuffing** | Pre-loaded revenue into resellers |
| **Accounting manipulation** | Capitalized expenses, extended payment terms |
| **Due diligence failure** | HP's DD team missed/ignored red flags |
| **Overpayment** | Even without fraud: 11x revenue for 10-15% growth = crazy premium |
| **No synergy logic** | HP = hardware. Autonomy = enterprise search software. Synergy where? |
| **CEO pressure** | Léo Apotheker (HP CEO) desperate for "software transformation" |
| **Board rubber-stamp** | Deal pushed through in weeks (not months) |

### Red Flags Missed

```
1. MARGIN TOO GOOD: Autonomy reported 40%+ EBITDA margin
   → Typical enterprise software: 20-30%
   → Should have triggered DEEP DD

2. CUSTOMER CONCENTRATION: Few large deals = lumpy, risky

3. HARDWARE REVENUE: Autonomy buying/reselling hardware to boost topline
   → Obvious manipulation if you LOOK

4. AUDITOR CHANGES: UK accounting standard differences
   → Should have reconciled to US GAAP carefully

5. NO STRATEGIC FIT: Why would HP (printers/PCs) need enterprise search?
   → Forced thesis, no compelling logic

6. PRICE PREMIUM: 64% premium to stock price
   → What synergies justify 64%?? (Answer: NONE real)
```

### Financial Impact
- HP total write-down: **$8.8B** (goodwill impairment)
- If invested $11.1B in S&P 500 instead: would be $25B+ today
- Opportunity cost: **>$30B** in value destroyed

### Bài học Valuation
1. **Verify revenue quality** – Not all $1 of revenue is equal
2. **Conservative multiples** – If you can't justify premium with SPECIFIC synergies, don't pay it
3. **Independent DD** – Never rely solely on seller's numbers
4. **Strategic fit first** – "Wanting to be in software" ≠ good M&A thesis
5. **Walk away discipline** – Better to miss deal than overpay

---

## VI. LƯU Ý VỀ PHƯƠNG PHÁP

### DCF Best Practices

| Practice | Rationale |
|----------|-----------|
| Use FCFF + WACC for EV (not FCFE) | More stable, standard approach |
| Terminal growth ≤ GDP growth | Company can't outgrow economy forever |
| Sensitivity on WACC ± 1-2% | Shows valuation uncertainty |
| Cross-check TV with exit multiple | Two methods should converge |
| Build detailed model Year 1-3, simplify Year 4-5 | Near-term more certain |
| Explicitly state ALL assumptions | Transparency, reviewability |

### Valuation Pitfalls

| Pitfall | How to Avoid |
|---------|-------------|
| **Anchoring** on initial estimate | Run DCF blind, then check vs market |
| **Terminal value too high** | Always >50% but watch if >85% |
| **Cherry-picking comps** | Include ALL reasonable peers, explain exclusions |
| **Ignoring quality of earnings** | Adjust for non-recurring, normalize |
| **Mixing EV and Equity** | EV multiples (EV/EBITDA) vs Equity multiples (P/E) |
| **Forgetting dilution** | Options, warrants, convertibles → diluted shares |
| **Snapshot fallacy** | One multiple ≠ answer. Range is the answer |

### Valuation for Special Situations

| Situation | Recommended Approach |
|-----------|---------------------|
| **Pre-revenue startup** | VC method, Option pricing, Revenue multiples with heavy discount |
| **Financial institution** | P/B, Dividend Discount Model (DDM), Excess Return model |
| **Natural resources** | NAV (Net Asset Value of reserves), DCF with commodity assumptions |
| **Real estate** | Cap Rate, NAV, DCF of rental income |
| **Distressed company** | Liquidation value, Sum-of-Parts, Adjusted PV |
| **High-growth tech** | EV/Revenue (no earnings), DCF with high growth period |

---

## VII. CHECKLIST CORPORATE VALUATION

```
DCF:
□ Revenue projection reasonable (vs historical, market)?
□ Margin assumptions sourced (vs peers)?
□ CAPEX and D&A consistent with growth?
□ Working capital changes included?
□ WACC correctly calculated (market values, CAPM)?
□ Terminal value method chosen and justified?
□ Terminal growth ≤ economy growth?
□ TV as % of total reasonable (50-80%)?
□ Sensitivity analysis (WACC, g, margins)?

COMPS:
□ Peer set appropriate (similar size, growth, industry)?
□ Multiples calculated correctly (EV vs Equity)?
□ Medians AND ranges reported?
□ Outliers explained/excluded?
□ Forward vs trailing multiples considered?
□ Adjustments for differences in growth/risk?

PRECEDENT TRANSACTIONS:
□ Relevant (same industry, recent)?
□ Control premium included naturally?
□ Market conditions at time of deal considered?
□ Strategic vs financial buyers distinguished?
□ Synergy-driven premium separated?

SYNTHESIS:
□ "Football field" with all methods plotted?
□ Range makes sense (methods converge)?
□ Key value drivers identified?
□ Upside and downside cases?
□ Final recommendation supported by analysis?
```

---

## VIII. CÔNG THỨC TỔNG HỢP

| Formula | Use |
|---------|-----|
| $EV = \sum FCFF/(1+WACC)^t + TV/(1+WACC)^n$ | DCF valuation |
| $TV = FCFF_{n+1} / (WACC - g)$ | Terminal Value (Gordon) |
| $TV = EBITDA_n \times Exit Multiple$ | Terminal Value (Multiple) |
| $Equity = EV - Net Debt$ | Bridge to equity |
| $FCFF = NOPAT + D\&A - CAPEX - \Delta NWC$ | Free Cash Flow |
| $EV/EBITDA_{implied} = EV / EBITDA$ | Multiple calculation |
| $P/E_{implied} = Equity / Net Income$ | Equity multiple |
| $Share Value = Equity / Diluted Shares$ | Per-share intrinsic value |

---

*Tài liệu tham khảo: Damodaran "Investment Valuation" 4th Ed; McKinsey "Valuation" 7th Ed; Rosenbaum & Pearl "Investment Banking" 3rd Ed; Koller, Goedhart & Wessels "Valuation"; CFA Level II – Equity Valuation*
