# Time Value of Money – Giá Trị Thời Gian Của Tiền

> **Mục tiêu**: Hiểu rõ PV, FV, NPV, IRR – nền tảng quan trọng nhất của toàn bộ tài chính doanh nghiệp. Phân tích định lượng, công thức, biểu đồ, case study chi tiết.

---

## I. ĐỊNH NGHĨA VÀ LÝ THUYẾT NỀN TẢNG

### 1. Định nghĩa

**Time Value of Money (TVM)** là nguyên lý tài chính nền tảng nhất: **1 đồng tiền nhận được hôm nay có giá trị CAO HƠN 1 đồng tiền nhận được trong tương lai**.

> **"A dollar today is worth more than a dollar tomorrow."** – Nguyên lý cốt lõi nhất của Finance

TVM là xương sống của MỌI quyết định tài chính: từ gửi tiết kiệm, vay mua nhà, đầu tư cổ phiếu, đến định giá doanh nghiệp hàng tỷ đô.

### 2. Nguồn gốc lý thuyết

| Học giả | Đóng góp | Năm |
|---------|----------|-----|
| **Irving Fisher** | "The Theory of Interest" – lý thuyết lãi suất & TVM hiện đại | 1930 |
| **John Burr Williams** | DCF valuation lần đầu trong "The Theory of Investment Value" | 1938 |
| **Eugene Böhm-Bawerk** | "Positive Theory of Capital" – time preference & roundabout production | 1889 |
| **Modigliani & Miller** | Áp dụng TVM vào capital structure & cost of capital | 1958 |

### 3. Tại sao 1 đồng hôm nay > 1 đồng ngày mai?

| Lý do | Giải thích | Ví dụ |
|-------|-----------|-------|
| **Opportunity Cost** | Tiền hôm nay có thể đầu tư → sinh lời | 100 triệu gửi bank 8% → 108 triệu sau 1 năm |
| **Inflation** | Lạm phát làm giảm sức mua | Phở 50k hôm nay, 55k năm sau (lạm phát 10%) |
| **Risk/Uncertainty** | Tương lai bất định, tiền hứa trả sau có rủi ro | Khách hàng hứa trả 100 triệu sau 2 năm → có thể phá sản |
| **Consumption Preference** | Con người prefer tiêu dùng ngay (impatience) | Mua iPhone bây giờ vs đợi 2 năm |
| **Reinvestment Risk** | Lãi suất tương lai không chắc bằng hôm nay | Lãi 8% hôm nay, năm sau có thể chỉ 5% |

### 4. Sơ đồ tổng quan TVM

```
                        TIME VALUE OF MONEY
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
     ┌────▼────┐       ┌─────▼─────┐       ┌─────▼─────┐
     │ Present │       │  Future   │       │  Discount │
     │  Value  │       │  Value    │       │   Rate    │
     │  (PV)   │       │  (FV)     │       │   (r)     │
     └────┬────┘       └─────┬─────┘       └─────┬─────┘
          │                  │                   │
          └──────────────────┼───────────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
    ┌────▼────┐        ┌────▼────┐        ┌─────▼─────┐
    │  NPV    │        │  IRR    │        │ Annuity   │
    │(Net PV) │        │(Internal│        │ Perpetuity│
    │         │        │ Return) │        │           │
    └─────────┘        └─────────┘        └───────────┘
         │                   │                   │
    ┌────▼────────────┐ ┌───▼───────────┐ ┌────▼──────────┐
    │Capital Budgeting│ │ Project       │ │ Loan/Mortgage │
    │DCF Valuation    │ │ Evaluation    │ │ Bond Pricing  │
    │M&A Pricing      │ │ Performance   │ │ Retirement    │
    └─────────────────┘ └───────────────┘ └───────────────┘
```

---

## II. PHÂN TÍCH ĐỊNH LƯỢNG – CÁC KHÁI NIỆM CỐT LÕI

### A. Future Value (FV) – Giá trị tương lai

#### Định nghĩa
FV là giá trị của một khoản tiền **tại một thời điểm trong tương lai**, sau khi được đầu tư/gửi với lãi suất r trong n kỳ.

#### Công thức cơ bản (Lãi kép - Compound Interest)

$$FV = PV \times (1 + r)^n$$

Trong đó:
- $PV$ = Giá trị hiện tại (Present Value)
- $r$ = Lãi suất mỗi kỳ (interest rate per period)
- $n$ = Số kỳ (number of periods)
- $(1 + r)^n$ = **Compounding Factor** (hệ số tích lũy)

#### Công thức mở rộng - Lãi kép nhiều lần trong năm

$$FV = PV \times \left(1 + \frac{r}{m}\right)^{m \times n}$$

- $m$ = Số lần ghép lãi trong 1 năm (monthly: m=12, quarterly: m=4, daily: m=365)

#### Công thức - Continuous Compounding (Ghép lãi liên tục)

$$FV = PV \times e^{r \times n}$$

#### Ví dụ thực tế - So sánh các phương pháp ghép lãi

**Bài toán**: Gửi 100 triệu VND, lãi suất 12%/năm, kỳ hạn 5 năm.

| Phương pháp | Công thức | Kết quả |
|------------|-----------|---------|
| Lãi đơn (Simple) | 100 × (1 + 0.12×5) | 160.00 triệu |
| Lãi kép năm (Annual) | 100 × (1.12)⁵ | 176.23 triệu |
| Lãi kép quý (Quarterly) | 100 × (1.03)²⁰ | 180.61 triệu |
| Lãi kép tháng (Monthly) | 100 × (1.01)⁶⁰ | 181.67 triệu |
| Lãi kép liên tục (Continuous) | 100 × e^(0.6) | 182.21 triệu |

→ **Ghép lãi càng thường xuyên → FV càng lớn** (nhưng diminishing returns)

#### Sức mạnh Lãi Kép (Compound Interest)

```
Gửi 100 triệu, lãi 8%/năm (compound annually):

Năm 1:   108.0 triệu    (+8.0)
Năm 5:   146.9 triệu    (+46.9)
Năm 10:  215.9 triệu    (+115.9)
Năm 20:  466.1 triệu    (+366.1)  ← Gấp gần 5 lần!
Năm 30:  1,006.3 triệu  (+906.3)  ← Gấp 10 lần!
Năm 40:  2,172.5 triệu  (+2,072)  ← Gấp 21.7 lần!

→ "Compound interest is the eighth wonder of the world." – Einstein
```

#### Rule of 72 (Quy tắc 72)

| Lãi suất | Thời gian gấp đôi | Chính xác (ln2/r) |
|----------|-------------------|--------------------|
| 6% | 12 năm | 11.90 năm |
| 8% | 9 năm | 8.66 năm |
| 10% | 7.2 năm | 7.27 năm |
| 12% | 6 năm | 6.12 năm |
| 15% | 4.8 năm | 4.96 năm |
| 20% | 3.6 năm | 3.80 năm |

---

### B. Present Value (PV) – Giá trị hiện tại

#### Định nghĩa
PV là giá trị **hiện tại** của một khoản tiền sẽ nhận được trong tương lai, được chiết khấu (discount) về hôm nay.

#### Công thức

$$PV = \frac{FV}{(1 + r)^n} = FV \times (1 + r)^{-n}$$

#### Bảng Discount Factor

| Năm | r = 5% | r = 8% | r = 10% | r = 12% | r = 15% |
|-----|--------|--------|---------|---------|---------|
| 1 | 0.9524 | 0.9259 | 0.9091 | 0.8929 | 0.8696 |
| 3 | 0.8638 | 0.7938 | 0.7513 | 0.7118 | 0.6575 |
| 5 | 0.7835 | 0.6806 | 0.6209 | 0.5674 | 0.4972 |
| 10 | 0.6139 | 0.4632 | 0.3855 | 0.3220 | 0.2472 |
| 20 | 0.3769 | 0.2145 | 0.1486 | 0.1037 | 0.0611 |
| 30 | 0.2314 | 0.0994 | 0.0573 | 0.0334 | 0.0151 |

→ Tiền càng xa tương lai, giá trị hiện tại càng nhỏ. 1 triệu sau 30 năm (r=15%) chỉ đáng 15,100 VND!

#### Ví dụ thực tế

**Bài toán**: Đối tác hứa trả 500 triệu sau 5 năm. Discount rate = 10%. Giá trị thực hôm nay?

$$PV = \frac{500}{(1.10)^5} = \frac{500}{1.6105} = 310.46 \text{ triệu VND}$$

---

### C. Net Present Value (NPV) – Giá trị hiện tại ròng

#### Định nghĩa
NPV = Tổng PV của TẤT CẢ dòng tiền tương lai TRỪ đi vốn đầu tư ban đầu.

> **NPV là "Gold Standard" – chỉ số QUAN TRỌNG NHẤT trong quyết định đầu tư.**

#### Công thức

$$NPV = -C_0 + \sum_{t=1}^{n} \frac{CF_t}{(1+r)^t}$$

#### Quy tắc quyết định

```
NPV > 0  →  DỰ ÁN TẠO GIÁ TRỊ      →  ĐẦU TƯ ✅
NPV = 0  →  Hòa vốn (risk-adjusted)  →  TÙY CHIẾN LƯỢC ⚠️
NPV < 0  →  PHÁ HỦY GIÁ TRỊ         →  TỪ CHỐI ❌
```

#### Ví dụ chi tiết – Mở chuỗi cà phê

| Năm | CF (triệu VND) | Discount Factor (r=12%) | PV (triệu VND) |
|-----|-----------------|------------------------|----------------|
| 0 | -500 | 1.0000 | -500.00 |
| 1 | +120 | 0.8929 | +107.14 |
| 2 | +150 | 0.7972 | +119.58 |
| 3 | +180 | 0.7118 | +128.12 |
| 4 | +200 | 0.6355 | +127.10 |
| 5 | +250 | 0.5674 | +141.84 |
| **NPV** | | | **+123.78** |

---

### D. Internal Rate of Return (IRR)

#### Định nghĩa
IRR là **discount rate** mà tại đó **NPV = 0**. Đo "lãi suất thực" mà dự án tạo ra.

#### Công thức

$$0 = -C_0 + \sum_{t=1}^{n} \frac{CF_t}{(1+IRR)^t}$$

#### Quy tắc: IRR > WACC → Đầu tư ✅

#### NPV Profile Chart

```
NPV (triệu)
250│•
200│  •
150│    •
100│      •←── r=12%: NPV=123.8
 50│          •
  0│──────────────•──── ←── IRR ≈ 21.5%
-50│                •
   └─┬──┬──┬──┬──┬──┬──→ r(%)
     5  8  12 15 18 22 25
```

---

### E. Annuity & Perpetuity

#### Ordinary Annuity

$$PV_{Annuity} = PMT \times \frac{1 - (1+r)^{-n}}{r}$$

#### Perpetuity

$$PV_{Perpetuity} = \frac{PMT}{r}$$

#### Growing Perpetuity (Gordon Growth Model)

$$PV = \frac{CF_1}{r - g} \quad (r > g)$$

---

## III. ƯU ĐIỂM VÀ NHƯỢC ĐIỂM

### ✅ Ưu điểm:
1. **Gold standard** – 100% Fortune 500 và MBA programs sử dụng
2. **Time value** – Phản ánh đúng: 1 đồng năm 1 ≠ 1 đồng năm 10
3. **Risk-adjusted** – Discount rate phản ánh rủi ro dự án
4. **Additive** – NPV(A) + NPV(B) = NPV(Portfolio)
5. **Objective** – Dựa trên cash flows thực, không accounting tricks
6. **Wealth maximization** – NPV > 0 = tăng shareholder wealth

### ❌ Nhược điểm:
1. **Phụ thuộc r** – Thay đổi r 2% → NPV thay đổi 20-50%
2. **Dự báo CF khó** – Cash flow 5-10 năm → sai số lớn
3. **Multiple IRR** – CF đổi dấu nhiều lần → nhiều IRR (dùng MIRR)
4. **Scale-blind (IRR)** – Không tính đến quy mô dự án
5. **Ignore intangibles** – Strategic value, brand không nằm trong CF
6. **Ignore flexibility** – Option to expand/delay → Real Options

---

## IV. CASE STUDY THÀNH CÔNG: GRAB – Đốt tiền chiếm thị phần

### Bối cảnh
- 2012: Ra đời tại Malaysia, mở rộng ĐNÁ
- 2014-2018: Đốt hàng tỷ USD subsidy, NPV ngắn hạn âm
- SoftBank đầu tư $2B (2017) với IRR dự kiến ~28%

### NPV Analysis (discount rate 15%)

$$NPV \approx -2,000 + \sum PV(CF_{year4-10}) + PV(Exit_{year10}) \approx +\$1,800M$$

### Kết quả: IPO NASDAQ 12/2021, mkt cap $40B, adjusted EBITDA breakeven Q4/2023

**Bài học**: Long-term NPV thinking + Network effects → Winner-take-most payoff

---

## V. CASE STUDY THẤT BẠI: WeWork – NPV Analysis sai hoàn toàn

### Bối cảnh
- Valuation peak $47B (2019) → IPO collapse → Chapter 11 bankruptcy (2023)

### Tại sao NPV analysis thất bại?
1. **Garbage In, Garbage Out** – CF projections unrealistic (50%+ growth forever)
2. **Discount rate quá thấp** – Dùng r=10-12% cho company lỗ nặng
3. **Ignore unit economics** – NPV mỗi location NEGATIVE
4. **No worst case scenario** – Chỉ có bull case
5. **"Community Adjusted EBITDA"** – Manipulate metrics, loại bỏ chi phí thực

### Bài học: NPV chỉ tốt khi INPUTS đúng. Cần independent validation + conservative assumptions.

---

## VI. NHỮNG LƯU Ý QUAN TRỌNG

### Sai lầm phổ biến

| Sai lầm | Cách tránh |
|---------|-----------|
| Dùng nominal rate với real CF | Nhất quán: nominal+nominal HOẶC real+real |
| Include sunk costs | Sunk cost = irrelevant, chỉ tính incremental CF |
| Discount rate = "cảm tính" | Dùng WACC, CAPM, comparable |
| Optimism bias trong CF | Independent validation, conservative base case |
| Quên working capital changes | ΔWC = real cash outflow |
| Chỉ dùng single NPV number | Luôn làm sensitivity + scenario analysis |

### Best Practices

```
✅ NPV làm primary decision tool
✅ Kết hợp NPV + IRR + Payback
✅ Sensitivity Analysis (tornado diagram)
✅ Scenario Analysis (best/base/worst)
✅ Document ALL assumptions

❌ Chỉ dùng IRR alone
❌ Assume discount rate constant forever
❌ Trust single NPV number
❌ Forget post-investment audit
```

---

## VII. CÔNG THỨC TỔNG HỢP

| Công thức | Ý nghĩa |
|-----------|---------|
| $FV = PV(1+r)^n$ | Giá trị tương lai |
| $PV = FV/(1+r)^n$ | Giá trị hiện tại |
| $NPV = -C_0 + \sum CF_t/(1+r)^t$ | Giá trị hiện tại ròng |
| $PV_{annuity} = PMT \times [1-(1+r)^{-n}]/r$ | PV dòng tiền đều |
| $PV_{perpetuity} = PMT/r$ | PV dòng tiền vĩnh viễn |
| $PV_{growing} = CF_1/(r-g)$ | Gordon Growth Model |
| Rule of 72: $n \approx 72/r$ | Thời gian gấp đôi |

---

*Tài liệu tham khảo: Brealey, Myers & Allen "Principles of Corporate Finance" 14th Ed; Damodaran "Applied Corporate Finance" 4th Ed; CFA Level I – Quantitative Methods*
