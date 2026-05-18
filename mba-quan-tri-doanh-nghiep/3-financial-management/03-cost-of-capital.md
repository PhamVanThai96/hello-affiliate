# Cost of Capital – Chi Phí Sử Dụng Vốn (WACC)

> **Mục tiêu**: Hiểu cách tính WACC, Cost of Equity (CAPM), Cost of Debt, và ứng dụng làm discount rate trong capital budgeting và định giá doanh nghiệp.

---

## I. ĐỊNH NGHĨA VÀ LÝ THUYẾT NỀN TẢNG

### 1. Định nghĩa

**Cost of Capital** (Chi phí sử dụng vốn) là **tỷ suất lợi nhuận tối thiểu** mà doanh nghiệp phải đạt được trên vốn đầu tư để **duy trì giá trị DN** và **thỏa mãn nhà đầu tư** (cả chủ nợ lẫn cổ đông).

> **Nói đơn giản**: Cost of Capital = "Giá thuê tiền". DN vay phải trả lãi (cost of debt), huy động cổ đông phải tạo return (cost of equity). **WACC = giá trung bình weighted của tất cả nguồn vốn.**

### 2. Nguồn gốc lý thuyết

| Học giả | Đóng góp | Năm |
|---------|----------|-----|
| **Modigliani & Miller** | M&M Proposition I & II – cost of capital & capital structure | 1958 |
| **William Sharpe** | CAPM – Capital Asset Pricing Model | 1964 |
| **John Lintner** | CAPM development song song | 1965 |
| **Eugene Fama & Kenneth French** | 3-Factor Model → thay thế/bổ sung CAPM | 1993 |
| **Aswath Damodaran** | Practical WACC & cost of capital estimation | 1990s-now |

### 3. Vai trò của Cost of Capital

| Vai trò | Giải thích |
|---------|-----------|
| **Discount rate cho NPV** | WACC dùng làm r trong NPV = Σ CF/(1+WACC)^t |
| **Hurdle rate** | Dự án phải có IRR > WACC mới được đầu tư |
| **DCF Valuation** | Enterprise Value = Σ FCF/(1+WACC)^t |
| **Optimal capital structure** | Minimize WACC = Maximize firm value |
| **Performance measurement** | EVA = NOPAT - (Capital × WACC). EVA > 0 = tạo giá trị |
| **Benchmark** | So sánh ROIC vs WACC → DN có tạo giá trị? |

### 4. Cấu trúc Cost of Capital

```
            ┌────────────────────────────────┐
            │            WACC                │
            │  (Weighted Average Cost        │
            │   of Capital)                  │
            └────────────┬───────────────────┘
                         │
           ┌─────────────┼──────────────┐
           │                            │
      ┌────▼──────┐             ┌──────▼──────┐
      │ Cost of   │             │  Cost of    │
      │ EQUITY    │             │  DEBT       │
      │ (Ke)      │             │  (Kd)       │
      │           │             │             │
      │ CAPM:     │             │ Kd × (1-T)  │
      │ Rf + β×   │             │ (after-tax) │
      │ (Rm - Rf) │             │             │
      └───────────┘             └─────────────┘
           ↑                         ↑
      Cổ đông yêu cầu          Chủ nợ yêu cầu
      return CAO HƠN            return THẤP HƠN
      (rủi ro cao hơn,         (ưu tiên thanh toán,
       residual claim)           tax deductible)
```

---

## II. PHÂN TÍCH ĐỊNH LƯỢNG

### A. WACC – Weighted Average Cost of Capital

#### Công thức WACC

$$WACC = \frac{E}{V} \times K_e + \frac{D}{V} \times K_d \times (1 - T)$$

Trong đó:
- $E$ = Market value of Equity (vốn hóa thị trường)
- $D$ = Market value of Debt (giá trị thị trường nợ vay)
- $V$ = E + D = Total firm value
- $K_e$ = Cost of Equity (chi phí vốn cổ phần)
- $K_d$ = Cost of Debt (chi phí nợ vay trước thuế)
- $T$ = Corporate tax rate
- $(1-T)$ = Tax shield factor (lãi vay được khấu trừ thuế)

#### Tại sao dùng Market Value (không dùng Book Value)?

| | Market Value | Book Value |
|-|-------------|-----------|
| Phản ánh | Kỳ vọng tương lai | Chi phí lịch sử |
| Relevant? | ✅ (đầu tư dựa trên tương lai) | ❌ (past ≠ future) |
| WACC chính xác? | ✅ | ❌ (có thể sai lệch lớn) |

#### Ví dụ tính WACC

**Doanh nghiệp ABC**:
- Market cap (E) = 600 tỷ VND
- Market value Debt (D) = 400 tỷ VND
- V = 600 + 400 = 1,000 tỷ
- Cost of Equity (Ke) = 14%
- Cost of Debt (Kd) = 9% (before tax)
- Tax rate = 20%

$$WACC = \frac{600}{1000} \times 14\% + \frac{400}{1000} \times 9\% \times (1-0.20)$$

$$WACC = 0.6 \times 14\% + 0.4 \times 9\% \times 0.8$$

$$WACC = 8.4\% + 2.88\% = \mathbf{11.28\%}$$

---

### B. Cost of Equity (Ke) – CAPM

#### Capital Asset Pricing Model

$$K_e = R_f + \beta \times (R_m - R_f)$$

Trong đó:
- $R_f$ = Risk-free rate (lãi suất phi rủi ro – thường = Government Bond 10-year)
- $\beta$ = Beta – hệ số đo lường rủi ro hệ thống (systematic risk)
- $R_m$ = Expected market return (return kỳ vọng thị trường)
- $(R_m - R_f)$ = Market Risk Premium (MRP) – phần bù rủi ro thị trường

#### Giải thích từng thành phần

```
Ke = Rf + β × (Rm - Rf)
     │     │      │
     │     │      └── Market Risk Premium: Phần bù cổ đông
     │     │          yêu cầu vì đầu tư vào stocks > bonds
     │     │          (trung bình 5-7% cho thị trường phát triển,
     │     │           7-10% cho emerging markets như VN)
     │     │
     │     └── β: Mức biến động so với thị trường
     │         β = 1.0: biến động = thị trường
     │         β > 1.0: biến động CAO hơn (aggressive)
     │         β < 1.0: biến động THẤP hơn (defensive)
     │
     └── Risk-free rate: Return "zero risk"
         VN: Trái phiếu CP 10 năm (~3-4%)
         US: 10-year Treasury (~4-5% hiện tại)
```

#### Ví dụ tính Cost of Equity

**Vinamilk (VNM)**:
- Rf = 3.5% (TPCP VN 10 năm)
- β = 0.75 (defensive stock – food/beverage)
- Market risk premium VN = 8%

$$K_e = 3.5\% + 0.75 \times 8\% = 3.5\% + 6\% = \mathbf{9.5\%}$$

**FPT Corporation**:
- Rf = 3.5%
- β = 1.3 (tech stock, higher volatility)
- MRP = 8%

$$K_e = 3.5\% + 1.3 \times 8\% = 3.5\% + 10.4\% = \mathbf{13.9\%}$$

#### Bảng Beta theo ngành (Việt Nam estimates)

| Ngành | Beta | Ke (Rf=3.5%, MRP=8%) |
|-------|------|---------------------|
| Utilities (Điện) | 0.4-0.6 | 6.7% - 8.3% |
| F&B (Thực phẩm) | 0.6-0.8 | 8.3% - 9.9% |
| Banking | 0.8-1.1 | 9.9% - 12.3% |
| Real Estate | 1.1-1.5 | 12.3% - 15.5% |
| Technology | 1.2-1.6 | 13.1% - 16.3% |
| Startup (early) | 2.0-3.0 | 19.5% - 27.5% |

#### Phương pháp thay thế CAPM

| Phương pháp | Công thức | Khi nào dùng? |
|------------|-----------|---------------|
| **Fama-French 3-Factor** | Ke = Rf + β₁(Market) + β₂(SMB) + β₃(HML) | Academic, more accurate |
| **Build-up Method** | Ke = Rf + ERP + Size Premium + Company Premium | Private company, no β |
| **Dividend Growth (Gordon)** | Ke = D₁/P₀ + g | Stable dividend payers |
| **Bond Yield + Premium** | Ke = Company Bond Yield + 3-5% | No market data |

---

### C. Cost of Debt (Kd)

#### Cách tính

$$K_d (after-tax) = K_d (before-tax) \times (1 - T)$$

#### Các cách xác định Kd (before-tax)

| Phương pháp | Mô tả |
|------------|-------|
| **Yield to Maturity (YTM)** | Kd = YTM trái phiếu DN đang lưu hành |
| **Current borrowing rate** | Lãi suất vay ngân hàng hiện tại |
| **Credit rating + spread** | Rf + Credit Spread (theo rating S&P/Moody's) |
| **Interest expense / Total debt** | Ước lượng đơn giản (book value) |

#### Ví dụ

**DN vay bank 9%/năm, thuế suất 20%**:

$$K_d (after-tax) = 9\% \times (1 - 0.20) = 9\% \times 0.80 = \mathbf{7.2\%}$$

→ **Tax Shield**: Nhà nước "trợ cấp" 1.8% (9% × 20%) vì lãi vay khấu trừ thuế!

#### Tại sao Kd < Ke? (Luôn luôn)

```
1. Priority: Chủ nợ được trả TRƯỚC cổ đông (khi phá sản)
   → Risk thấp hơn → Required return thấp hơn

2. Tax advantage: Lãi vay = tax deductible 
   → After-tax cost thực sự thấp hơn stated rate

3. Contractual: Lãi suất CỐ ĐỊNH, biết trước
   → Ít uncertainty hơn equity return (residual)

Kết quả: Ke = 12-15% vs Kd(after-tax) = 5-8% (typical)
```

---

### D. WACC Sensitivity – Tác động lên Valuation

$$\text{Enterprise Value} = \sum_{t=1}^{n} \frac{FCF_t}{(1+WACC)^t} + \frac{Terminal Value}{(1+WACC)^n}$$

| WACC | Enterprise Value (VD) | % Change |
|------|----------------------|----------|
| 8% | 15,000 tỷ | +36% |
| 9% | 13,200 tỷ | +20% |
| 10% | 11,000 tỷ | Base |
| 11% | 9,500 tỷ | -14% |
| 12% | 8,200 tỷ | -25% |
| 13% | 7,100 tỷ | -35% |

→ **WACC thay đổi 1% → Valuation thay đổi 10-15%!** Cực kỳ sensitive.

---

## III. ỨNG DỤNG VÀ HOÀN CẢNH ÁP DỤNG

### Khi nào dùng WACC?

| Tình huống | Dùng WACC? | Lý do |
|-----------|-----------|-------|
| DCF valuation (whole firm) | ✅ | Discount FCF to firm → Enterprise Value |
| Capital budgeting (dự án tương tự rủi ro DN) | ✅ | Hurdle rate = WACC |
| Dự án rủi ro KHÁC DN | ❌ | Dùng project-specific cost of capital |
| Evaluating division performance | ⚠️ | Dùng divisional WACC (different β) |
| Leveraged buyout (LBO) | ❌ | Capital structure thay đổi liên tục → APV method |
| Startup valuation | ❌ | No debt, no β → VC method or build-up |

### Project-Specific Discount Rate

$$r_{project} = R_f + \beta_{project} \times MRP$$

- Dự án rủi ro cao hơn DN → dùng β cao hơn → r cao hơn
- Dự án rủi ro thấp hơn → dùng β thấp hơn → r thấp hơn

**Ví dụ**: WACC overall = 11%. Nhưng dự án R&D mới (β = 2.0) → r = 3.5% + 2.0 × 8% = 19.5%

---

## IV. ƯU ĐIỂM VÀ NHƯỢC ĐIỂM

### ✅ Ưu điểm WACC/CAPM:
1. **Widely accepted** – Chuẩn industry cho DCF, capital budgeting
2. **Intuitive** – "Giá trung bình của vốn" dễ hiểu
3. **Accounts for capital structure** – Phản ánh mix D/E
4. **Tax shield included** – (1-T) factor cho debt
5. **Objective (CAPM)** – Market data-driven, ít subjective
6. **Benchmark** – ROIC > WACC = value creation

### ❌ Nhược điểm:
1. **CAPM assumptions unrealistic** – Perfect markets, rational investors, homogeneous expectations
2. **Beta unstable** – β thay đổi over time, khác theo estimation period
3. **MRP controversial** – Market Risk Premium: 5%? 7%? 10%? Experts disagree
4. **Static** – WACC = snapshot. Real capital structure/rates change
5. **Circular logic** – WACC needs E (market cap), but DCF produces E
6. **Emerging markets difficulty** – Rf, β, MRP hard to estimate in VN
7. **Single-rate limitation** – Dùng 1 WACC cho TẤT CẢ dự án → inaccurate

---

## V. CASE STUDY THÀNH CÔNG: Apple – Low WACC = Massive Value Creation

### Apple's WACC (2023 estimate)
- Market Cap (E): ~$3,000B
- Debt (D): ~$110B
- E/V = 96.4%, D/V = 3.6%
- Ke (CAPM): Rf=4.5% + β(1.2) × MRP(5%) = **10.5%**
- Kd (after-tax): 3.5% × (1-21%) = **2.77%**

$$WACC = 96.4\% \times 10.5\% + 3.6\% \times 2.77\% = 10.12\% + 0.10\% = \mathbf{10.22\%}$$

### Value Creation
- ROIC Apple ≈ **55-60%** (return on invested capital)
- WACC ≈ **10.2%**
- **Spread = ROIC - WACC = 45-50%!** → Massive value creation

$$EVA = Invested Capital \times (ROIC - WACC) = \$100B \times 50\% = \$50B/year$$

### Bài học
1. Low WACC (do low debt, strong brand → low β) cho phép NPV positive dễ hơn
2. High ROIC vs WACC = flywheel of value creation
3. Apple giữ minimal debt → E/V ≈ 97% → WACC driven by Ke

---

## VI. CASE STUDY THẤT BẠI: Toys "R" Us – WACC tăng vọt sau LBO

### Bối cảnh
- 2005: Leveraged Buyout bởi KKR, Bain, Vornado → $6.6B debt loaded
- D/E ratio: từ 50% → 95% (extreme leverage!)

### WACC Before vs After LBO

| | Before LBO | After LBO |
|-|-----------|-----------|
| D/V | 30% | 85% |
| E/V | 70% | 15% |
| Kd (after-tax) | 4% | 7.5% (higher due to risk) |
| Ke | 12% | 25% (extreme financial risk) |
| **WACC** | **9.8%** | **10.1%** |

Paradox: WACC tăng nhẹ because Ke skyrockets (financial distress risk). Tax shield của debt BỊ OFFSET bởi increased cost of equity + cost of financial distress.

### Kết quả
- Operating income không đủ cover interest expense ($400M/year)
- Cannot invest in stores → Competitive position eroded
- 2017: Filed Chapter 11 bankruptcy
- 2018: Liquidated → 33,000 jobs lost

### Bài học
1. **Tax shield has limits** – Beyond optimal leverage, distress costs > tax benefit
2. **WACC is U-shaped** – Minimize at optimal D/E, then increases
3. **Operating flexibility crushed** – High fixed debt = no capacity to invest
4. **Cost of financial distress** not captured in simple WACC formula

---

## VII. LƯU Ý VỀ PHƯƠNG PHÁP

### Sai lầm phổ biến khi tính WACC

| Sai lầm | Hậu quả | Cách tránh |
|---------|---------|-----------|
| Dùng book value thay market value | WACC sai → valuation sai | Luôn dùng market value weights |
| Dùng historical β thay forward β | Under/over-estimate risk | Adjust β cho changes in business |
| Ignore country risk (emerging markets) | Ke quá thấp | Thêm Country Risk Premium |
| Dùng current risk-free rate ngắn hạn | Mismatch horizon | Dùng 10-year government bond |
| Constant WACC trong LBO/changing structure | Misleading valuation | APV method cho changing D/E |
| Forget to unlever/relever β | Wrong β for target structure | Hamada equation |

### Hamada Equation (Lever/Unlever Beta)

$$\beta_{Levered} = \beta_{Unlevered} \times [1 + (1-T) \times \frac{D}{E}]$$

$$\beta_{Unlevered} = \frac{\beta_{Levered}}{1 + (1-T) \times \frac{D}{E}}$$

**Khi nào dùng**: Tính Ke cho dự án/DN với capital structure KHÁC công ty comparable.

### Country Risk Premium cho Việt Nam

$$K_e (VN) = R_f (local) + \beta \times MRP_{global} + Country Risk Premium$$

Hoặc:

$$K_e (VN) = R_f (US) + \beta \times MRP_{US} + Country Risk Premium_{VN}$$

Country Risk Premium VN ≈ 2-4% (Damodaran database, updated annually)

---

## VIII. CHECKLIST COST OF CAPITAL

```
WACC CALCULATION:
□ Xác định market value E và D? (không dùng book value)
□ Tính E/V và D/V weights?
□ Cost of Equity qua CAPM? (Rf + β × MRP)
□ Rf = 10-year government bond?
□ β estimated correctly? (relevered if needed)
□ Market Risk Premium source identified?
□ Country Risk Premium nếu emerging market?
□ Cost of Debt = YTM or current borrowing rate?
□ After-tax Kd = Kd × (1-T)?

VALIDATION:
□ WACC reasonable (8-15% cho đa số DN)?
□ Ke > Kd? (luôn phải đúng)
□ WACC < Ke? (must be true with debt)
□ Consistent with comparable company WACCs?
□ Sensitivity analysis on WACC? (±1-2%)

APPLICATION:
□ Dùng project-specific rate nếu rủi ro khác DN?
□ APV nếu capital structure thay đổi lớn?
□ ROIC > WACC? (company creating value?)
```

---

*Tài liệu tham khảo: Sharpe "Capital Asset Prices" 1964; Modigliani & Miller 1958; Damodaran "Investment Valuation" 4th Ed; Brealey, Myers & Allen "Principles of Corporate Finance" 14th Ed; CFA Level I & II – Corporate Issuers*
