# Mergers & Acquisitions – M&A (Sáp Nhập & Mua Lại)

> **Mục tiêu**: Hiểu M&A process, valuation, synergies, deal structures, hostile vs friendly, LBO, và tại sao phần lớn M&A thất bại. Case study chi tiết.

---

## I. ĐỊNH NGHĨA VÀ LÝ THUYẾT NỀN TẢNG

### 1. Định nghĩa

**Merger** (Sáp nhập): Hai công ty HỢP NHẤT thành một thực thể mới (A + B = C).

**Acquisition** (Mua lại): Một công ty MUA và kiểm soát công ty khác (A mua B → A sở hữu B).

> Trong thực tế, "merger" thường vẫn là acquisition được "rebrand" để cả hai bên vui (merger of equals).

### 2. Phân loại M&A

```
┌────────────────────────────────────────────────────────────┐
│                    CÁC LOẠI M&A                            │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  THEO QUAN HỆ KINH DOANH:                                │
│  1. HORIZONTAL: Cùng ngành, cùng chuỗi giá trị           │
│     VD: Facebook mua Instagram, Disney mua Fox            │
│                                                            │
│  2. VERTICAL: Khác vị trí trong chuỗi giá trị            │
│     VD: Apple mua nhà cung cấp chip, Amazon mua Whole Foods│
│                                                            │
│  3. CONGLOMERATE: Khác ngành hoàn toàn                    │
│     VD: Berkshire mua See's Candies, GEICO, BNSF Railroad │
│                                                            │
│  THEO THÁI ĐỘ:                                           │
│  • FRIENDLY: Board đồng ý, negotiate price               │
│  • HOSTILE: Target board REJECT → Bidder goes to          │
│    shareholders directly (tender offer)                    │
│                                                            │
│  THEO CẤU TRÚC:                                           │
│  • Stock deal: Thanh toán bằng cổ phiếu acquirer         │
│  • Cash deal: Thanh toán bằng tiền mặt                    │
│  • Mixed: Kết hợp cash + stock                            │
│  • LBO: Leveraged Buyout (dùng debt của target để mua!)   │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 3. Động lực M&A – Tại sao mua?

| Động lực | Giải thích | Ví dụ |
|----------|-----------|-------|
| **Synergies** | 1+1 = 3 (cost savings, revenue enhancement) | Disney + Pixar: content library |
| **Growth** | Mua growth nhanh hơn organic build | Facebook mua WhatsApp (2B users) |
| **Market power** | Giảm cạnh tranh, pricing power | T-Mobile + Sprint |
| **Diversification** | Giảm risk qua ngành khác | Amazon mua Whole Foods |
| **Technology/IP** | Mua công nghệ/patent | Google mua DeepMind (AI) |
| **Talent** | Acqui-hire (mua team) | Big Tech acqui-hires AI startups |
| **Tax benefit** | NOL carry-forward, tax-efficient structure | Corporate inversions |
| **Empire building** | CEO ego, compensation tied to size | Many failed conglomerates |
| **Undervaluation** | Target undervalued → buy cheap | Activist investors |

---

## II. PHÂN TÍCH ĐỊNH LƯỢNG

### A. Valuation trong M&A

#### 3 Phương pháp chính

| Method | Approach | Best for |
|--------|----------|----------|
| **DCF** | Intrinsic: PV of future FCF | Fundamental value |
| **Comparable Companies** | Relative: Multiples of peers | Market benchmark |
| **Precedent Transactions** | Relative: Past M&A deal multiples | Control premium |

#### Valuation dẫn đến "Football Field"

```
                    Valuation Range (tỷ USD)
Method              │ Low    │ Mid    │ High   │
────────────────────┼────────┼────────┼────────┤
52-Week Trading     │   8    │  10    │   12   │
                    │████████│████████│████████│
DCF                 │   9    │  12    │   15   │
                    │████████│████████│████████│████
Comparable Cos      │   10   │  11    │   13   │
                    │████████│████████│████████│
Precedent Txns      │   11   │  13    │   16   │
                    │████████│████████│████████│████
                    └────────┴────────┴────────┘
                         ◄── Offer range ──►
                         ($11-14B typical)
```

---

### B. Synergies Valuation

#### Types of Synergies

$$\text{Value of Synergies} = V_{Combined} - V_A - V_B$$

| Synergy Type | Source | NPV Estimate | Probability |
|-------------|--------|-------------|-------------|
| **Cost synergies** | Eliminate duplicate functions (HR, IT, HQ) | High confidence | 70-80% |
| **Revenue synergies** | Cross-sell, new markets, pricing power | Low confidence | 30-50% |
| **Financial synergies** | Lower cost of debt, tax benefits | Medium | 60-70% |
| **Operational synergies** | Economies of scale, best practices | Medium | 50-60% |

#### Premium Analysis

$$\text{Acquisition Premium} = \frac{Offer Price - Market Price}{Market Price}$$

Typical premiums: **20-50%** over unaffected stock price

$$\text{Value created for acquirer} = Synergies - Premium Paid$$

**Ví dụ**: 
- Target market cap = $10B
- Premium = 30% → Offer = $13B
- Premium paid = $3B
- Synergies NPV = $5B
- **Value created = $5B - $3B = $2B** ✅

If Synergies < Premium → **Value DESTROYED** for acquirer shareholders ❌

---

### C. Deal Structure & Financing

#### Cash vs Stock

| | Cash Deal | Stock Deal |
|-|-----------|-----------|
| **Tax for target** | Taxable event immediately | Tax deferred (stock swap) |
| **Risk sharing** | Acquirer bears ALL risk | Shared (if overpay, dilution) |
| **Signal** | "Our stock is undervalued" (pay cash) | "Our stock is overvalued" (pay stock) |
| **Confidence level** | HIGH – pay real money | Lower – share risk |
| **EPS impact** | No dilution | Dilution (more shares) |
| **Financing** | Need cash/debt | No cash needed |

#### Leveraged Buyout (LBO)

```
LBO Structure:
┌──────────────────────────────────────────────┐
│         BUY TARGET COMPANY ($100M)           │
├──────────────────────────────────────────────┤
│                                              │
│  FINANCING:                                  │
│  • Equity (PE fund): $30M (30%)              │
│  • Senior Debt:      $50M (50%)              │
│  • Mezzanine:        $20M (20%)              │
│                     ─────────                │
│  Total:              $100M                   │
│                                              │
│  RETURN MECHANISM:                           │
│  1. Use target's cash flow to pay down debt  │
│  2. Improve operations → increase EBITDA     │
│  3. Exit in 3-7 years (IPO or sale)          │
│  4. Equity grows from $30M → $90M+ (3x!)    │
│                                              │
│  KEY: PE fund uses OTHER PEOPLE'S MONEY      │
│  (debt) to amplify equity returns            │
│                                              │
└──────────────────────────────────────────────┘
```

#### LBO Return Drivers

$$IRR_{LBO} = f(Entry\,Multiple, Exit\,Multiple, Leverage, EBITDA\,Growth, FCF\,Paydown)$$

| Driver | Contribution to returns |
|--------|----------------------|
| EBITDA growth (operational improvement) | 30-40% |
| Debt paydown (de-leveraging) | 30-40% |
| Multiple expansion (sell at higher EV/EBITDA) | 20-30% |
| **Target IRR for PE fund** | **20-25%+** |

---

### D. Accretion/Dilution Analysis

**Question**: Does the deal INCREASE or DECREASE acquirer's EPS?

$$\text{Accretive if: } EPS_{pro\,forma} > EPS_{standalone}$$

$$\text{Dilutive if: } EPS_{pro\,forma} < EPS_{standalone}$$

**Quick test**: If target's Earnings Yield (E/P) > Acquirer's Cost of Financing → Accretive

---

### E. M&A Process

```
SELL-SIDE M&A PROCESS (Typical 3-6 months):

Phase 1: PREPARATION (4-6 weeks)
  │ • Hire investment bank (advisor)
  │ • Prepare Information Memo (IM)  
  │ • Identify potential buyers (50-100)
  │ • Set up data room
  ▼
Phase 2: MARKETING (4-6 weeks)
  │ • Contact buyers (teaser → NDA → IM)
  │ • Management presentations
  │ • Receive Indications of Interest (IOI)
  │ • Select shortlist (5-10 buyers)
  ▼
Phase 3: DUE DILIGENCE (4-8 weeks)
  │ • Open data room to shortlisted buyers
  │ • Management meetings, site visits
  │ • Buyers perform financial, legal, commercial DD
  │ • Receive final binding bids
  ▼
Phase 4: NEGOTIATION & SIGNING (2-4 weeks)
  │ • Select preferred buyer
  │ • Negotiate SPA (Sale and Purchase Agreement)
  │ • Board approval, fairness opinion
  │ • Sign definitive agreement
  ▼
Phase 5: CLOSING (4-12 weeks)
  │ • Regulatory approval (antitrust)
  │ • Shareholder vote (if required)
  │ • Satisfy conditions precedent
  │ • Close deal → Money transfers → Ownership changes
  ▼
Phase 6: INTEGRATION (6-24 months)
  │ • PMI (Post-Merger Integration)
  │ • Realize synergies
  │ • Retain key talent
  │ • Merge systems, culture
  └→ SUCCESS or FAILURE determined here!
```

---

## III. ƯU ĐIỂM VÀ NHƯỢC ĐIỂM

### ✅ Ưu điểm M&A:
1. **Speed** – Mua nhanh hơn xây (organic takes years)
2. **Market position** – Instant market share, customer base
3. **Synergies** – Cost savings, revenue enhancement
4. **Technology/IP** – Acquire innovation immediately
5. **Talent** – Get entire teams with expertise
6. **Diversification** – Reduce business concentration risk
7. **Tax benefits** – NOL utilization, amortization

### ❌ Nhược điểm / Rủi ro:
1. **Overpayment** – #1 reason M&A destroys value (winner's curse)
2. **Integration failure** – Cultural clash, system incompatibility
3. **Synergy overestimation** – "Revenue synergies" rarely materialize fully
4. **Management distraction** – 12-18 months focus on integration vs operations
5. **Talent flight** – Key people leave post-acquisition
6. **Debt burden** – LBO can overleverage → financial distress
7. **Regulatory risk** – Antitrust blocks deal after spending millions
8. **Cultural destruction** – Acquiring creativity/innovation → kills it

### M&A Success Rate

```
RESEARCH SHOWS:
• 60-70% of M&A DESTROY value for acquirer shareholders
• Average acquirer stock drops 1-3% on announcement
• Target shareholders gain 20-30% (premium)
• Synergies realized: typically 50-70% of projected
• Integration takes 2-3x longer than planned

"M&A is like second marriages – triumph of hope over experience"
```

---

## IV. CASE STUDY THÀNH CÔNG: Disney + Pixar ($7.4B, 2006)

### Bối cảnh
- 2005: Disney Animation in decline (failures: Treasure Planet, Home on the Range)
- Pixar = gold standard (Toy Story, Finding Nemo, Incredibles – 100% hit rate)
- Disney-Pixar contract EXPIRING → Lose partnership OR buy

### Deal Summary

| Item | Detail |
|------|--------|
| Price | $7.4B (all stock) |
| Premium | ~-5% (bought at market, below typical M&A premium!) |
| Metric | 29x trailing EBITDA |
| Structure | Stock deal (Disney shares to Pixar shareholders) |
| Key term | Steve Jobs → Disney's largest shareholder + Board seat |
| Key term | Pixar retains creative INDEPENDENCE |

### Synergies Realized

| Synergy | Value (estimated) |
|---------|-------------------|
| Sequel rights (Toy Story 3, 4; Incredibles 2; Finding Dory) | $10B+ box office |
| Theme park content (Pixar lands, rides) | $3-5B revenue |
| Revitalized Disney Animation (Frozen, Moana, Encanto) | $8B+ box office |
| Merchandise & streaming (Disney+) | $5B+ annually |
| **Total value created** | **>>$50B** (vs $7.4B paid!) |

### Why It Worked

| Factor | Detail |
|--------|--------|
| **Cultural preservation** | Pixar kept its culture, creative process, leadership |
| **No forced integration** | Separate studio, separate identity |
| **Visionary leadership** | Steve Jobs + Bob Iger = mutual respect |
| **Complementary strengths** | Disney = distribution/brand. Pixar = creativity/technology |
| **Talent retention** | John Lasseter, Ed Catmull stayed |
| **Right price** | $7.4B for what became $50B+ in value |
| **Strategic clarity** | Clear thesis: "Win in animation category" |

### ROI Calculation

$$ROI = \frac{Value\,Created - Price\,Paid}{Price\,Paid} = \frac{50B+ - 7.4B}{7.4B} = 575\%+$$

→ One of the greatest acquisitions in corporate history

---

## V. CASE STUDY THẤT BẠI: AOL + Time Warner ($182B, 2000)

### Bối cảnh
- 2000: "Merger of the Century" – AOL (internet) + Time Warner (media)
- Largest merger in history at the time: **$182 billion**
- Vision: "Convergence of content + internet distribution"

### Deal Summary

| Item | Detail |
|------|--------|
| Price | $182B (all stock) |
| Combined revenue | $33B |
| AOL market cap | $163B (!!!) – at dot-com peak |
| Time Warner market cap | $83B |
| Premium | 71% to Time Warner shareholders |
| CEO | Gerald Levin (Time Warner) |
| Thesis | Internet + Content = Unstoppable media empire |

### What Went Wrong

| Factor | Detail |
|--------|--------|
| **Dot-com crash** | AOL's market cap went $163B → $20B within 2 years |
| **Overlaid valuation** | AOL stock was massively overvalued → Used fake currency to buy real assets |
| **No synergies** | Internet + Cable + Magazine → ZERO meaningful synergy realization |
| **Cultural WAR** | AOL (young, tech, casual) vs TW (old media, corporate, hierarchy) |
| **Revenue synergies = myth** | "Cross-sell" never materialized. Different customers, different needs |
| **Management conflict** | AOL vs TW executives fought constantly |
| **Technology shift** | Broadband killed AOL's dial-up model within 3 years! |
| **Write-down** | $99B goodwill write-off (2002) – largest in history |

### Financial Disaster

| Metric | At Merger (2000) | 3 Years Later (2003) |
|--------|-----------------|---------------------|
| Market Cap | $280B (combined) | $72B |
| Value destroyed | | **$208 BILLION** |
| Stock price (AOL-TW) | $56 | $15 |
| Goodwill write-off | $0 | $99B |
| AOL subscribers | 27 million | 24 million (declining) |

### Bài học M&A Thất bại

```
1. VALUATION MATTERS MOST:
   AOL used INFLATED stock to "buy" real assets
   → When stock normalizes, overpayment becomes apparent
   → LESSON: Stock-deal at market peak = dangerous

2. "SYNERGIES" REQUIRE LOGIC:
   "Internet + Cable + Magazines" = what synergy exactly?
   → If you can't articulate SPECIFIC synergies in $, don't do the deal

3. CULTURAL FIT IS NON-NEGOTIABLE:
   AOL = startup culture. TW = old-school corporate.
   Mixing oil and water → both sides miserable, talent leaves

4. INTEGRATION PLAN BEFORE DEAL:
   No clear integration plan → 2 years of chaos
   → Plan integration BEFORE signing, not after

5. TECHNOLOGY RISK:
   AOL's core business (dial-up) was DYING
   → Acquiring DOESN'T fix a broken business model

6. HUBRIS:
   "Merger of the Century" → biggest FAILURE of the century
   → The more grandiose the claim, the harder the fall

7. "MERGER OF EQUALS" IS A LIE:
   Someone is always the acquirer. Pretending otherwise → confusion
```

---

## VI. DEFENSIVE TACTICS (Chống thâu tóm)

| Tactic | Description |
|--------|-------------|
| **Poison Pill** | Rights plan: existing shareholders buy shares at 50% discount if hostile bidder acquires >15% |
| **Staggered Board** | Only 1/3 board up for election each year → Can't replace board in 1 vote |
| **White Knight** | Find friendly bidder to outbid hostile acquirer |
| **Crown Jewel Defense** | Sell most valuable asset → target less attractive |
| **Pac-Man Defense** | Counter-bid to acquire the hostile acquirer! |
| **Golden Parachute** | Huge severance for executives if acquired → Increases cost |
| **Shark Repellent** | Supermajority vote required for merger (80%+) |

---

## VII. LƯU Ý VỀ PHƯƠNG PHÁP

### Due Diligence Checklist

| Area | Key Items |
|------|----------|
| **Financial** | Revenue quality, recurring vs one-time, working capital, debt, off-balance |
| **Legal** | Lawsuits, IP ownership, contracts, regulatory compliance |
| **Commercial** | Market position, customer concentration, competitive moat |
| **Operational** | Capacity, technology, supply chain, employee contracts |
| **Tax** | NOL, transfer pricing, tax exposure |
| **HR** | Key talent retention risk, culture assessment, employment contracts |
| **IT** | Systems compatibility, tech debt, cybersecurity |
| **Environmental** | Contamination liability, compliance costs |

### Common M&A Mistakes

| Mistake | Prevention |
|---------|-----------|
| Overpaying (winner's curse) | Discipline: walk away if above max price |
| Hubris/empire building | Independent board oversight, shareholder vote |
| Synergy overestimation | Discount revenue synergies 50%+, conservative timeline |
| Cultural clash ignored | Pre-deal cultural assessment, integration plan |
| Key talent not retained | Golden handcuffs, role clarity BEFORE close |
| Integration too slow | 100-day plan, dedicated PMI team |
| No post-audit | Track synergy realization quarterly |

---

## VIII. CHECKLIST M&A

```
PRE-DEAL:
□ Clear strategic rationale (not just "growth")?
□ Valuation range established (DCF + Comps + Precedent)?
□ Synergies identified AND quantified conservatively?
□ Maximum price ("walk-away price") defined?
□ Financing secured (cash/debt/stock)?
□ Integration plan drafted BEFORE signing?

DUE DILIGENCE:
□ Financial DD: revenue quality, margins, working capital?
□ Legal DD: litigation risk, contract issues?
□ Commercial DD: market competitive dynamics?
□ Cultural assessment: compatible or clash?
□ Key talent identified: retention plans?
□ IT systems: compatible? Integration cost?

EXECUTION:
□ Accretion/Dilution analysis positive?
□ Regulatory approval pathway clear?
□ Shareholder support expected?
□ Communication plan ready (employees, customers)?
□ Day 1 readiness planned?

POST-MERGE (PMI):
□ Integration office established?
□ 100-day plan with milestones?
□ Synergy tracking dashboard?
□ Key talent monitored (retention bonuses)?
□ Cultural integration initiatives?
□ Post-audit at 1-year and 3-year?
□ "Kill criteria" if synergies not materializing?
```

---

*Tài liệu tham khảo: DePamphilis "Mergers, Acquisitions, and Other Restructuring Activities" 10th Ed; Rosenbaum & Pearl "Investment Banking" 3rd Ed; Bruner "Applied M&A"; McKinsey "Valuation" 7th Ed; CFA Level II – Corporate Issuers*
