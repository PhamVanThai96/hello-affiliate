# Working Capital Management – Quản Lý Vốn Lưu Động

> **Mục tiêu**: Hiểu quản lý vốn lưu động (NWC), Cash Conversion Cycle, chính sách tín dụng, quản lý tồn kho – tối ưu hóa thanh khoản và hiệu quả hoạt động.

---

## I. ĐỊNH NGHĨA VÀ LÝ THUYẾT NỀN TẢNG

### 1. Định nghĩa

**Working Capital Management** là quá trình quản lý **tài sản ngắn hạn** (current assets) và **nợ ngắn hạn** (current liabilities) để đảm bảo doanh nghiệp có đủ **thanh khoản** hoạt động hàng ngày, đồng thời **tối ưu hóa hiệu quả** sử dụng vốn.

$$\text{Net Working Capital (NWC)} = \text{Current Assets} - \text{Current Liabilities}$$

$$NWC = (Cash + AR + Inventory + Prepaid) - (AP + Accrued + ST Debt)$$

> **Bản chất**: Working Capital = Vốn "chôn" trong hoạt động kinh doanh hàng ngày. Càng ít vốn chôn → Càng hiệu quả (nhưng phải đủ an toàn).

### 2. Tại sao Working Capital Management quan trọng?

| Lý do | Giải thích |
|-------|-----------|
| **Survival** | 82% SME phá sản do cash flow problem, không phải do thua lỗ |
| **Opportunity cost** | Vốn kẹt trong AR/Inventory = mất cơ hội đầu tư khác |
| **Profitability** | Quản lý tốt → giảm chi phí lãi vay, tăng return |
| **Relationship** | Thanh toán đúng hạn → supplier trust, customer loyalty |
| **Growth fuel** | Tăng trưởng nhanh = NWC tăng nhanh → Cash crunch! |

### 3. Cấu trúc Working Capital

```
┌─────────────────────────────────────────────────────────┐
│              WORKING CAPITAL COMPONENTS                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  CURRENT ASSETS (Tài sản ngắn hạn):                   │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │   CASH   │ │   A/R    │ │INVENTORY │ │ PREPAID  │  │
│  │ & equiv  │ │Phải thu  │ │Hàng tồn  │ │Trả trước │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
│                                                         │
│  CURRENT LIABILITIES (Nợ ngắn hạn):                   │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │   A/P    │ │ ACCRUED  │ │ ST DEBT  │ │TAX PAYBL │  │
│  │Phải trả  │ │Chi phí   │ │Vay NH    │ │Thuế phải │  │
│  │nhà CC    │ │phải trả  │ │          │ │trả       │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
│                                                         │
│  NWC = Current Assets - Current Liabilities             │
│                                                         │
│  OPERATING WC = AR + Inventory - AP                     │
│  (excludes cash & ST debt)                              │
└─────────────────────────────────────────────────────────┘
```

---

## II. PHÂN TÍCH ĐỊNH LƯỢNG

### A. Cash Conversion Cycle (CCC) – Vòng quay tiền mặt

#### Công thức

$$CCC = DSO + DIO - DPO$$

Trong đó:
- **DSO** (Days Sales Outstanding) = 365 / (Revenue / Avg AR) = Số ngày thu tiền từ khách
- **DIO** (Days Inventory Outstanding) = 365 / (COGS / Avg Inventory) = Số ngày tồn kho
- **DPO** (Days Payable Outstanding) = 365 / (COGS / Avg AP) = Số ngày trả NCC

#### Biểu đồ CCC

```
Timeline (ngày):
│
├─── Mua nguyên liệu ──── Bán hàng ──── Thu tiền KH
│    (nhập kho)           (xuất kho)     (AR collected)
│         │                    │              │
│    ◄────┼──── DIO = 45 ────►│              │
│         │                    │              │
│         │    ◄───── DSO = 30 ──────────────►│
│         │                                   │
│    ◄────┼──── DPO = 40  ───►│              │
│         │    (trả NCC)      │              │
│         │                    │              │
│         CCC = 45 + 30 - 40 = 35 ngày       │
│         │                                   │
│    ◄────┼───── CCC = 35 ngày ──────────────►│
│         │                                   │
│  "35 ngày DN phải TỰ TÀI TRỢ bằng vốn riêng/vay"
```

#### CCC theo ngành (benchmarks)

| Industry | DSO | DIO | DPO | CCC |
|----------|-----|-----|-----|-----|
| **Grocery retail** | 3 | 25 | 35 | **-7** (negative! = funded by suppliers) |
| **Amazon** | 20 | 35 | 80 | **-25** (suppliers fund Amazon!) |
| **Manufacturing** | 45 | 60 | 40 | **65** |
| **Construction** | 90 | 30 | 60 | **60** |
| **Software SaaS** | 40 | 0 | 20 | **20** |
| **Real Estate** | 15 | 365+ | 60 | **320+** (very long!) |

#### Negative CCC = Competitive MOAT
Amazon, Costco, Dell (cũ) có CCC âm → Thu tiền trước khi trả suppliers → **"Free" working capital** = Nhà cung cấp tài trợ hoạt động!

---

### B. Operating Working Capital (OWC)

$$OWC = Accounts Receivable + Inventory - Accounts Payable$$

$$\Delta OWC = OWC_{end} - OWC_{begin}$$

- **ΔOWC > 0**: Vốn lưu động TĂNG → Cash GIẢM (tied up)
- **ΔOWC < 0**: Vốn lưu động GIẢM → Cash TĂNG (released)

#### Impact on Free Cash Flow

$$FCF = EBIT(1-T) + Depreciation - CAPEX - \Delta OWC$$

→ ΔOWC tăng = **giảm FCF** (working capital "eats" cash!)

#### Ví dụ: Startup tăng trưởng 50%/năm

| Year | Revenue | AR (30 days) | Inventory | AP | OWC | ΔOWC (Cash needed!) |
|------|---------|-------------|-----------|-----|-----|-------------------|
| 1 | 10 tỷ | 0.82 tỷ | 1.5 tỷ | 0.8 tỷ | 1.52 tỷ | - |
| 2 | 15 tỷ | 1.23 tỷ | 2.25 tỷ | 1.2 tỷ | 2.28 tỷ | +0.76 tỷ |
| 3 | 22.5 tỷ | 1.85 tỷ | 3.38 tỷ | 1.8 tỷ | 3.43 tỷ | +1.15 tỷ |

→ **Growth burns cash!** Mỗi năm tăng trưởng 50% = cần thêm ~0.8-1.2 tỷ working capital

---

### C. Quản lý Accounts Receivable

#### Credit Policy Components

| Component | Nội dung | Ví dụ |
|-----------|---------|-------|
| **Credit Standards** | Ai được mua chịu? | Credit score > 700, operating > 3 years |
| **Credit Terms** | Bao lâu, discount? | "2/10, net 30" = 2% discount if pay in 10 days |
| **Collection Policy** | Thu thế nào? | Reminder day 25, call day 35, lawyer day 60 |

#### Chi phí cho terms "2/10, net 30"

Nếu KH KHÔNG lấy discount, effective annual rate:

$$\text{Annual cost} = \frac{Discount\%}{1 - Discount\%} \times \frac{365}{Full\,period - Discount\,period}$$

$$= \frac{0.02}{0.98} \times \frac{365}{20} = 0.0204 \times 18.25 = \mathbf{37.2\%/năm!}$$

→ Rất đắt! KH nên lấy discount (≈ vay 37.2%/năm nếu không lấy)

#### AR Aging Schedule

| Age | Amount | % Total | Action |
|-----|--------|---------|--------|
| 0-30 days (current) | 800 triệu | 53% | Normal |
| 31-60 days | 400 triệu | 27% | Follow up |
| 61-90 days | 200 triệu | 13% | Warning call |
| >90 days | 100 triệu | 7% | Legal/Write-off |
| **Total AR** | **1,500 triệu** | 100% | |

---

### D. Quản lý Inventory

#### Economic Order Quantity (EOQ)

$$EOQ = \sqrt{\frac{2 \times D \times S}{H}}$$

- $D$ = Annual demand (units)
- $S$ = Ordering cost per order
- $H$ = Holding cost per unit per year

**Ví dụ**: D = 10,000 units, S = 500,000 VND/order, H = 50,000 VND/unit/year

$$EOQ = \sqrt{\frac{2 \times 10,000 \times 500,000}{50,000}} = \sqrt{200,000,000} = 14,142 \approx \mathbf{447 units/order}$$

#### Inventory Management Methods

| Method | Description | Best for |
|--------|------------|----------|
| **EOQ** | Mathematical optimal order quantity | Stable demand, known costs |
| **JIT (Just-In-Time)** | Zero/minimal inventory, order on demand | Toyota-style lean |
| **ABC Analysis** | A(80% value, 20% items), B, C classification | Prioritize management effort |
| **Safety Stock** | Buffer for demand uncertainty | Unpredictable demand |
| **Reorder Point** | Order when inventory hits threshold | Automated replenishment |

---

### E. Quản lý Cash

#### Motives for Holding Cash

| Motive | Explanation |
|--------|-------------|
| **Transaction** | Day-to-day operations (payroll, suppliers) |
| **Precautionary** | Emergency buffer (unexpected expenses) |
| **Speculative** | Seize opportunities (discounts, investments) |
| **Compensating balance** | Bank requirement for credit line |

#### Optimal Cash Balance – Baumol Model

$$C^* = \sqrt{\frac{2 \times T \times F}{r}}$$

- $T$ = Total cash needed per period
- $F$ = Fixed cost per transaction (bán securities)
- $r$ = Opportunity cost (interest rate)

---

## III. ƯU ĐIỂM VÀ NHƯỢC ĐIỂM

### ✅ Ưu điểm Working Capital Management hiệu quả:
1. **Cash flow stability** – Luôn đủ tiền hoạt động, tránh insolvency
2. **Lower financing costs** – Ít phải vay ngắn hạn → tiết kiệm lãi suất
3. **Better relationships** – Trả NCC đúng hạn → discounts, priority supply
4. **Higher profitability** – Vốn xoay nhanh → cùng vốn tạo nhiều doanh thu hơn
5. **Growth enabler** – Cash freed up → fund expansion
6. **Competitive advantage** – Negative CCC = structural advantage (Amazon, Dell)

### ❌ Nhược điểm / Rủi ro:
1. **Too aggressive** – Giảm NWC quá mức → stockout, lost sales, strained suppliers
2. **Too conservative** – NWC quá cao → inefficient, low ROA
3. **Growth trap** – Tăng trưởng nhanh nhưng NWC growth outpaces → cash crunch
4. **Seasonality** – Demand fluctuation → WC needs vary wildly
5. **Supply chain disruption** – JIT vulnerable to external shocks (COVID!)
6. **Customer concentration** – 1 big customer delays = major AR problem

### Working Capital Strategy Spectrum

```
AGGRESSIVE                              CONSERVATIVE
(Low NWC, High Risk, High Return)       (High NWC, Low Risk, Low Return)
◄────────────────────────────────────────────────────────►
• Minimal cash reserves               • Large cash buffer
• Tight credit terms                   • Generous credit
• JIT inventory                        • High safety stock
• Stretch AP max                       • Pay early for discounts
• Higher profitability                 • Lower profitability
• Higher insolvency risk               • Very safe but inefficient
```

---

## IV. CASE STUDY THÀNH CÔNG: Dell – Negative Working Capital Revolution

### Bối cảnh
- 1990s-2000s: Dell Computer pioneered **Build-to-Order** model
- Key innovation: **Negative Cash Conversion Cycle** = Customers pay BEFORE Dell pays suppliers

### Dell's Working Capital Magic

| Metric | Dell (2004) | HP (competitor) | Apple (2004) |
|--------|------------|-----------------|--------------|
| DSO | 30 days | 49 days | 25 days |
| DIO | 4 days (!!) | 29 days | 3 days |
| DPO | 70 days | 42 days | 54 days |
| **CCC** | **-36 days** | **+36 days** | **-26 days** |

→ Dell collected from customers 36 days BEFORE paying suppliers!

### Financial Impact

| Impact | Value |
|--------|-------|
| Working Capital "generated" | ~$3.5B (at peak) |
| Interest savings | ~$200M/year (didn't need to borrow for operations) |
| Growth without external capital | Funded expansion from operations |
| ROE boost | Higher due to less capital needed |

### How Dell Achieved Negative CCC:
1. **Build-to-Order**: No finished goods inventory (DIO = 4 days!)
2. **Customer prepayment**: Credit card/upfront payment (DSO low)
3. **Supplier stretch**: Paid components suppliers in 70 days (DPO high)
4. **Direct sales**: No retailer/distributor inventory needed

### Bài học
- Working capital management = **strategic competitive weapon**
- Negative CCC = business model innovation, not just finance optimization
- Suppliers fund YOUR operations → Free float → Invest in growth

---

## V. CASE STUDY THẤT BẠI: Toys "R" Us – Working Capital Mismanagement

### Bối cảnh
- Post-LBO (2005): $6.6B debt loaded onto Toys "R" Us
- Cash flow barely covered interest → No investment in operations
- Working capital squeezed to survive

### The Vicious Cycle

```
High Debt → Cash for interest payments → No money for:
    │
    ├── Store renovation (stores look dated vs Target/Walmart)
    ├── E-commerce investment (fell behind Amazon)
    ├── Inventory quality (stockouts during holidays!)
    └── Marketing/customer experience
    
→ Customers leave → Revenue falls → WC needs stressed → Cut deeper
→ DEATH SPIRAL
```

### Working Capital Indicators (deterioration)

| Year | Current Ratio | CCC | Inventory Freshness | Customer Traffic |
|------|--------------|-----|--------------------|----|
| 2005 | 1.5 | 45 | Good | Stable |
| 2010 | 1.2 | 55 | Declining | -10% |
| 2015 | 0.9 (!!) | 65 | Poor (obsolete toys) | -25% |
| 2017 | 0.7 | 70+ | Critical | -40% |

### Key Failure
- **Inventory mismatch**: Stocked wrong toys (not trending items)
- **Supplier trust eroded**: Couldn't get hot products due to payment delays
- **Holiday cash crunch**: 40% revenue in Q4, but couldn't stock enough
- **Result**: Bankruptcy 2017, Liquidation 2018

### Bài học thất bại
1. **WC management ≠ just cutting** – Cutting too deep destroys customer value
2. **Liquidity = Survival** – Current ratio < 1.0 = death warrant
3. **Investment required** – Must invest in competitiveness (stores, online)
4. **Supplier relationships** – Break trust → lose access to products
5. **Seasonal business** – WC planning must account for peak needs

---

## VI. LƯU Ý VỀ PHƯƠNG PHÁP

### Common Mistakes

| Mistake | Consequence | Fix |
|---------|-----------|-----|
| Ignore ΔOWC in DCF | Overvalue growing companies | Always include WC investment in FCF |
| Same WC policy for all customers | Bad customers get same terms as good ones | Segment credit policy by credit quality |
| JIT without backup plan | Supply chain shock → production stops | Keep safety stock for critical items |
| Stretch AP too aggressively | Lose early payment discounts (37%!) + damage relationships | Calculate cost of forgone discount |
| Focus only on NWC absolute level | Miss efficiency metrics | Track CCC, turnover ratios |
| Annual budget only | Miss seasonal spikes | Monthly cash forecasting |

### WC Optimization Levers

```
REDUCE DSO (Faster collection):
• Invoice immediately (not end of month!)
• Offer early payment discount (2/10 net 30)
• Automate AR follow-up
• Credit check before extending terms
• Factoring/invoice financing for urgent needs

REDUCE DIO (Less inventory):
• ABC analysis → focus on A items
• Demand forecasting improvement
• JIT for predictable items
• Sell slow-moving stock at discount
• Supplier-managed inventory (VMI)

INCREASE DPO (Slower payment to NCC):
• Negotiate longer terms (30 → 45 → 60 days)
• Take advantage of standard terms fully
• Supply chain financing programs
• BUT: Don't damage supplier relationships!

REDUCE CASH HOLDINGS:
• Cash pooling (centralize group cash)
• Sweep accounts (automatic investment of excess)
• Accurate cash forecasting
• Line of credit as backup (don't hold cash "just in case")
```

---

## VII. CHECKLIST WORKING CAPITAL MANAGEMENT

```
METRICS:
□ NWC calculated? Positive?
□ CCC calculated? Improving vs last year?
□ DSO vs industry average?
□ DIO vs industry average?  
□ DPO vs industry average?
□ Current Ratio > 1.5?
□ Quick Ratio > 1.0?

AR MANAGEMENT:
□ Credit policy documented?
□ AR aging monitored weekly?
□ Bad debt provision adequate?
□ Collection process automated?
□ Customer credit limits set?

INVENTORY:
□ ABC classification done?
□ EOQ/reorder points set for A items?
□ Slow-moving inventory identified?
□ Obsolete inventory written off?
□ Safety stock calculated?

AP MANAGEMENT:
□ Payment terms negotiated?
□ Early payment discounts evaluated?
□ AP automation in place?
□ Supplier relationship maintained?

CASH:
□ Cash forecast (13-week rolling)?
□ Minimum cash balance defined?
□ Credit line as backup?
□ Excess cash invested short-term?
□ Seasonal needs planned?
```

---

*Tài liệu tham khảo: Brealey, Myers & Allen "Principles of Corporate Finance" 14th Ed; Sagner "Working Capital Management" 2014; CFA Level I – Working Capital Management*
