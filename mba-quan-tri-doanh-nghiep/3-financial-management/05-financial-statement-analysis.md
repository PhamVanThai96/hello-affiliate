# Financial Statement Analysis – Phân Tích Báo Cáo Tài Chính

> **Mục tiêu**: Đọc hiểu 3 báo cáo tài chính, phân tích tỷ số tài chính (profitability, liquidity, leverage, efficiency), phát hiện dấu hiệu bất thường, DuPont Analysis.

---

## I. ĐỊNH NGHĨA VÀ LÝ THUYẾT NỀN TẢNG

### 1. Định nghĩa

**Financial Statement Analysis** là quá trình **phân tích các báo cáo tài chính** (BCTC) của doanh nghiệp để đánh giá hiệu quả hoạt động, tình hình tài chính, khả năng sinh lời – từ đó đưa ra quyết định đầu tư, tín dụng, hoặc quản lý.

> **"Accounting is the language of business."** – Warren Buffett

### 2. Ba Báo cáo Tài chính Chính

```
┌───────────────────────────────────────────────────────────────┐
│                 3 BÁO CÁO TÀI CHÍNH CHÍNH                    │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  1. BALANCE SHEET (Bảng cân đối kế toán)                     │
│     → SNAPSHOT: DN SỞ HỮU gì & NỢ gì tại 1 thời điểm        │
│     → Assets = Liabilities + Equity                           │
│                                                               │
│  2. INCOME STATEMENT (Báo cáo kết quả kinh doanh)            │
│     → FLOW: DN KIẾM & CHI bao nhiêu trong 1 kỳ               │
│     → Revenue - Expenses = Net Income                         │
│                                                               │
│  3. CASH FLOW STATEMENT (Báo cáo lưu chuyển tiền tệ)         │
│     → FLOW: TIỀN MẶT vào/ra thực tế trong 1 kỳ               │
│     → Operating + Investing + Financing = ΔCash               │
│                                                               │
│  Bổ sung:                                                     │
│  4. Statement of Changes in Equity                            │
│  5. Notes to Financial Statements (Thuyết minh BCTC)          │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### 3. Mục đích phân tích theo đối tượng

| Đối tượng | Mục đích | Focus |
|-----------|---------|-------|
| **Nhà đầu tư** | Cổ phiếu đáng mua? | Profitability, growth, valuation |
| **Chủ nợ/Ngân hàng** | Cho vay có an toàn? | Leverage, liquidity, coverage |
| **Ban quản lý** | Điều hành hiệu quả? | Efficiency, profitability, trends |
| **Đối thủ** | Competitive intelligence | Revenue growth, margins, strategy |
| **Nhà cung cấp** | Khách hàng trả được không? | Liquidity, cash flow |
| **Cơ quan thuế** | Khai thuế đúng? | Revenue recognition, expenses |

---

## II. CHI TIẾT TỪNG BÁO CÁO TÀI CHÍNH

### A. Balance Sheet (Bảng cân đối kế toán)

#### Phương trình cơ bản

$$\text{Assets} = \text{Liabilities} + \text{Equity}$$

#### Cấu trúc

```
┌─────────────────────────────────────────────────────────┐
│                     BALANCE SHEET                        │
├──────────────────────────┬──────────────────────────────┤
│       ASSETS             │     LIABILITIES + EQUITY     │
├──────────────────────────┼──────────────────────────────┤
│ Current Assets:          │ Current Liabilities:         │
│  • Cash                  │  • Accounts Payable          │
│  • Accounts Receivable   │  • Short-term Debt           │
│  • Inventory             │  • Accrued Expenses          │
│  • Prepaid Expenses      │  • Current portion LT Debt   │
│                          │                              │
│ Non-Current Assets:      │ Non-Current Liabilities:     │
│  • PP&E (net)            │  • Long-term Debt            │
│  • Intangible Assets     │  • Deferred Tax              │
│  • Goodwill              │  • Pension Obligations       │
│  • Investments           │                              │
│                          │ Shareholders' Equity:        │
│                          │  • Common Stock              │
│                          │  • Retained Earnings         │
│                          │  • Treasury Stock (-)        │
│                          │  • AOCI                      │
├──────────────────────────┼──────────────────────────────┤
│ TOTAL ASSETS = XXX       │ TOTAL L + E = XXX           │
└──────────────────────────┴──────────────────────────────┘
```

### B. Income Statement (Báo cáo KQKD)

```
Revenue (Doanh thu thuần)                    1,000
- COGS (Giá vốn hàng bán)                    (600)
─────────────────────────────────────────────────
= GROSS PROFIT (Lãi gộp)                      400   [Gross Margin = 40%]
- SG&A (Chi phí BH & QLDN)                   (200)
- R&D                                          (50)
- Depreciation & Amortization                  (30)
─────────────────────────────────────────────────
= EBIT / Operating Income                     120   [Operating Margin = 12%]
- Interest Expense                             (20)
+ Other Income                                   5
─────────────────────────────────────────────────
= EBT (Lợi nhuận trước thuế)                  105
- Income Tax (20%)                             (21)
─────────────────────────────────────────────────
= NET INCOME (Lợi nhuận sau thuế)              84   [Net Margin = 8.4%]

EPS = Net Income / Shares Outstanding
```

### C. Cash Flow Statement (Báo cáo LCTT)

```
OPERATING ACTIVITIES (Hoạt động kinh doanh):
  Net Income                                    84
  + Depreciation & Amortization                 30  (non-cash add back)
  - Increase in Accounts Receivable            (15) (sold but not collected)
  - Increase in Inventory                      (10) (bought but not sold)
  + Increase in Accounts Payable                 8  (bought but not paid)
  = NET CASH FROM OPERATIONS                    97

INVESTING ACTIVITIES (Hoạt động đầu tư):
  - Purchase PP&E (CAPEX)                      (50)
  - Acquisitions                               (30)
  + Sale of investments                         10
  = NET CASH FROM INVESTING                    (70)

FINANCING ACTIVITIES (Hoạt động tài chính):
  + New debt issued                             40
  - Debt repayment                             (20)
  - Dividends paid                             (25)
  - Share buyback                              (15)
  = NET CASH FROM FINANCING                    (20)

NET CHANGE IN CASH = 97 - 70 - 20 = +7
```

---

## III. PHÂN TÍCH TỶ SỐ TÀI CHÍNH

### A. Profitability Ratios (Tỷ số sinh lời)

| Tỷ số | Công thức | Ý nghĩa | Benchmark |
|--------|----------|---------|-----------|
| **Gross Margin** | Gross Profit / Revenue | Hiệu quả sản xuất | >30% tốt |
| **Operating Margin** | EBIT / Revenue | Hiệu quả vận hành | >15% tốt |
| **Net Margin** | Net Income / Revenue | Bottom line profitability | >10% tốt |
| **ROE** | Net Income / Equity | Return cho cổ đông | >15% tốt |
| **ROA** | Net Income / Total Assets | Hiệu quả sử dụng tài sản | >5% tốt |
| **ROIC** | NOPAT / Invested Capital | True return on capital | >WACC! |

### B. Liquidity Ratios (Tỷ số thanh khoản)

| Tỷ số | Công thức | Ý nghĩa | Benchmark |
|--------|----------|---------|-----------|
| **Current Ratio** | Current Assets / Current Liabilities | Khả năng trả nợ ngắn hạn | 1.5-2.5 |
| **Quick Ratio** | (CA - Inventory) / CL | Acid test (loại hàng tồn) | >1.0 |
| **Cash Ratio** | Cash / CL | Strictest liquidity | >0.2 |
| **Operating CF Ratio** | Operating CF / CL | CF thực trả nợ NH | >1.0 |

### C. Leverage Ratios (Tỷ số đòn bẩy)

| Tỷ số | Công thức | Ý nghĩa | Warning |
|--------|----------|---------|---------|
| **D/E Ratio** | Total Debt / Equity | Cơ cấu vốn | >2.0 caution |
| **Debt/Assets** | Total Debt / Total Assets | % assets funded by debt | >60% risky |
| **Interest Coverage** | EBIT / Interest Expense | Khả năng trả lãi | <3x danger! |
| **Debt/EBITDA** | Total Debt / EBITDA | Years to repay debt | >4x risky |

### D. Efficiency Ratios (Tỷ số hoạt động)

| Tỷ số | Công thức | Ý nghĩa |
|--------|----------|---------|
| **Inventory Turnover** | COGS / Avg Inventory | Hàng tồn quay nhanh? |
| **Days Inventory** | 365 / Inventory Turnover | Số ngày tồn kho |
| **AR Turnover** | Revenue / Avg AR | Thu tiền nhanh? |
| **Days Sales Outstanding** | 365 / AR Turnover | Số ngày chờ thu tiền |
| **AP Turnover** | COGS / Avg AP | Trả nhà cung cấp nhanh? |
| **Days Payable** | 365 / AP Turnover | Số ngày trì hoãn trả |
| **Cash Conversion Cycle** | DSO + DIO - DPO | Vòng quay tiền mặt |
| **Asset Turnover** | Revenue / Total Assets | Hiệu quả dùng tài sản |

### E. DuPont Analysis – Phân rã ROE

#### 3-Component DuPont

$$ROE = \frac{Net Income}{Revenue} \times \frac{Revenue}{Assets} \times \frac{Assets}{Equity}$$

$$ROE = \text{Net Margin} \times \text{Asset Turnover} \times \text{Equity Multiplier}$$

#### 5-Component DuPont

$$ROE = \frac{EBT}{EBIT} \times \frac{EBIT}{Revenue} \times \frac{Revenue}{Assets} \times \frac{Assets}{Equity} \times (1-T)$$

$$= \text{Tax Burden} \times \text{Interest Burden} \times \text{Operating Margin} \times \text{Turnover} \times \text{Leverage}$$

#### Ví dụ DuPont

| Company | Net Margin | Asset Turnover | Equity Multiplier | ROE |
|---------|-----------|---------------|------------------|-----|
| **Luxury brand** | 20% | 0.5x | 1.5x | 15% |
| **Retail (Walmart)** | 3% | 2.5x | 2.5x | 18.75% |
| **Bank** | 25% | 0.08x | 10x | 20% |

→ Same ROE, VERY different business models! DuPont reveals how ROE is generated.

---

## IV. PHƯƠNG PHÁP PHÂN TÍCH

### A. Trend Analysis (Phân tích xu hướng)
So sánh qua nhiều năm (3-5 năm) → Xu hướng cải thiện hay xấu đi?

### B. Common-Size Analysis (Phân tích cơ cấu)
- Income Statement: Mọi line item ÷ Revenue
- Balance Sheet: Mọi line item ÷ Total Assets

### C. Cross-Sectional Analysis (So sánh ngành)
So sánh với competitors & industry average

### D. Red Flags – Dấu hiệu cảnh báo

| Red Flag | Implication | Check |
|----------|-----------|-------|
| Revenue ↑ nhưng CF from Ops ↓ | Aggressive revenue recognition | Possible manipulation |
| AR growing >> Revenue growth | Bán chịu quá nhiều hoặc fake revenue | Quality of earnings |
| Inventory ↑ rapidly | Hàng tồn obsolete, overstocking | Write-down risk |
| Frequent "one-time charges" | Hiding recurring costs | True earnings lower |
| Gross margin declining | Competitive pressure, cost increase | Pricing power lost |
| Operating CF < Net Income (nhiều năm) | Earnings quality poor | Accrual manipulation |
| D/E rapidly increasing | Funding growth by debt | Distress risk |
| Change in accounting policies | May inflate earnings | Dig into notes |

---

## V. ƯU ĐIỂM VÀ NHƯỢC ĐIỂM

### ✅ Ưu điểm:
1. **Standardized** – GAAP/IFRS cho format thống nhất, so sánh được
2. **Objective** – Dựa trên số liệu thực, audited
3. **Comprehensive** – 3 statements cover tất cả: profitability, position, cash
4. **Historical track record** – Trends reveal trajectory
5. **Decision support** – Invest, lend, manage decisions backed by data

### ❌ Nhược điểm:
1. **Backward-looking** – Phản ánh QUÁ KHỨ, không dự báo tương lai
2. **Accounting choices** – Different policies → different numbers (cùng 1 DN!)
3. **Intangibles missed** – Brand, talent, IP → Off-balance-sheet hoặc understated
4. **Manipulation possible** – Earnings management, window dressing
5. **Inflation distortion** – Historical cost ≠ current value (especially PP&E, inventory)
6. **Different standards** – VAS vs IFRS vs US GAAP → comparability issues
7. **Static snapshot** – Balance Sheet = 1 day. Tomorrow may be very different

---

## VI. CASE STUDY THÀNH CÔNG: Phân tích Apple Inc. – Reading Financial Statements

### Apple FY2023 Key Metrics

| Metric | Value | Insight |
|--------|-------|---------|
| Revenue | $383B | Slight decline (-3%), but services growing |
| Gross Margin | 44.1% | Premium pricing power! (vs Samsung ~40%) |
| Operating Margin | 29.8% | Extraordinary efficiency |
| Net Margin | 25.3% | $97B net income! |
| ROE | 171% (!!) | Heavily leveraged (buybacks reduce equity) |
| ROIC | 55-60% | Massive value creation vs WACC 10% |
| Cash & Securities | $162B | Fortress balance sheet |
| Free Cash Flow | $100B/yr | Cash generation machine |
| Debt | $110B | Conservative vs $3T market cap |

### DuPont Analysis Apple

$$ROE = 25.3\% \times 1.15x \times 5.87x = 171\%$$

- Net Margin 25.3% → Premium brand
- Asset Turnover 1.15x → Capital-light model (outsource manufacturing)
- Equity Multiplier 5.87x → HIGH leverage from buybacks reducing equity denominator!

### Key Insight
Apple's ROE > 100% does NOT mean it's "better" than 20% ROE company. The extreme equity multiplier (from $600B+ buybacks reducing equity to ~$57B) artificially inflates ROE. **ROIC (55-60%) is the TRUE measure of operational excellence.**

---

## VII. CASE STUDY THẤT BẠI: Enron – Financial Statement Fraud

### Bối cảnh
- 2001: Enron – America's 7th largest company → filed bankruptcy
- **Largest accounting fraud in US history** (tại thời điểm đó)
- Revenue: "reported" $101B (2000) → Much was fake

### Red Flags mà analysts MISSed

| Red Flag | What happened |
|----------|--------------|
| Revenue ↑↑ but OCF flat/negative | Mark-to-market accounting: "recognized" decade of future profits immediately |
| **SPEs** (Special Purpose Entities) | Moved $30B+ debt OFF balance sheet → D/E appeared low |
| Complex financial statements | 3,000+ SPEs, nobody understood → Hiding losses |
| Related party transactions | CFO (Fastow) personally profited from SPEs |
| Stock options = compensation | Incentive to inflate stock price at ALL costs |
| Analyst questions dodged | CEO called analyst "asshole" on earnings call |
| High executive turnover | COO, Treasurer resigned before collapse |
| Auditor conflict | Arthur Andersen: $25M audit + $27M consulting → Independence? |

### Financial Statement Comparison

| Metric | Reported by Enron | Reality |
|--------|------------------|---------|
| Revenue 2000 | $101B | Much was "pass-through" trading |
| Debt on B/S | $13B | $38B+ (including off-balance SPEs) |
| Net Income | $979M profit | LOSS (massive) |
| Cash from Ops | Positive | Negative (reclassified as financing!) |
| Shareholder Equity | $11.5B | Negative (after restatements) |

### Bài học

```
1. CASH FLOW > NET INCOME: Nếu OCF consistently < NI → Nghi ngờ!
2. SIMPLICITY RULE: Nếu BCTC quá phức tạp → Có thể cố tình obfuscate
3. OFF-BALANCE SHEET: Đọc kỹ Notes → SPEs, operating leases, guarantees
4. RELATED PARTY: Ai benefit từ transactions? Conflict of interest?
5. AUDITOR INDEPENDENCE: Audit firm = consulting firm → Red flag
6. MARGIN OF SAFETY: Nếu too good to be true → Probably is
7. GOVERNANCE: Board oversight + independent directors essential
```

### Impact
- Arthur Andersen (auditor): destroyed, 85,000 jobs lost
- SOX Act 2002: Tighter regulations (CEO/CFO certification, auditor independence)
- $74B shareholder value → $0
- 20,000+ employees lost jobs AND retirement savings (in Enron stock)

---

## VIII. LƯU Ý VỀ PHƯƠNG PHÁP

### Quality of Earnings Checklist

```
□ Operating CF > Net Income? (consistently)
□ Revenue growth supported by cash collection?
□ No frequent "extraordinary items" or "one-time charges"?
□ Consistent accounting policies year over year?
□ Depreciation reasonable vs industry?
□ Working capital trends healthy?
□ No aggressive revenue recognition (bill-and-hold, channel stuffing)?
□ Management discussion matches number reality?
□ Auditor opinion clean (unqualified)?
□ Insider buying or selling? (selling = warning)
```

### VAS vs IFRS Key Differences (Vietnam)

| Topic | VAS (Vietnam) | IFRS |
|-------|--------------|------|
| Fair value | Limited use | Widely applied |
| Lease capitalization | Less strict | IFRS 16: all leases on B/S |
| Revenue recognition | Less detailed | IFRS 15: 5-step model |
| Financial instruments | Simpler | IFRS 9: complex (fair value, impairment) |
| Disclosure | Less extensive | Very extensive notes required |

---

## IX. CHECKLIST PHÂN TÍCH BCTC

```
READING:
□ Balance Sheet: A = L + E balanced?
□ Income Statement: Revenue → Gross → Operating → Net trend?
□ Cash Flow: OCF positive? OCF > NI?
□ Notes: Any unusual items, related party, contingent liabilities?

RATIOS:
□ Profitability: Gross/Operating/Net margins? ROE? ROIC?
□ Liquidity: Current ratio > 1.5? Quick > 1?
□ Leverage: D/E reasonable? Interest coverage > 3x?
□ Efficiency: CCC improving? Asset turnover trend?
□ DuPont decomposition done?

COMPARISON:
□ Trend analysis (3-5 years)?
□ Peer comparison (same industry)?
□ Common-size analysis?
□ Industry benchmarks checked?

RED FLAGS:
□ OCF vs NI divergence?
□ AR growing faster than revenue?
□ Inventory buildup?
□ Off-balance sheet items?
□ Frequent accounting changes?
□ Aggressive revenue recognition?
```

---

*Tài liệu tham khảo: Penman "Financial Statement Analysis & Security Valuation" 6th Ed; Subramanyam "Financial Statement Analysis" 12th Ed; CFA Level I & II – Financial Reporting and Analysis*
