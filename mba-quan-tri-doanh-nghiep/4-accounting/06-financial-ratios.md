# Financial Ratios – Các Tỷ Số Tài Chính

> **Mục tiêu**: Hiểu rõ các tỷ số tài chính quan trọng nhất: Thanh khoản, Hiệu quả, Đòn bẩy, Lợi nhuận. Công thức, ý nghĩa, benchmarking, DuPont Analysis, red flags, và ứng dụng cho SME Việt Nam.

---
## I. ĐỊNH NGHĨA VÀ LÝ THUYẾT NỀN TẢNG

### 1. Định nghĩa

**Financial Ratios (Tỷ số tài chính)** là các **chỉ số định lượng** được tính từ BCTC, dùng để **đánh giá sức khỏe tài chính, hiệu quả hoạt động, và rủi ro** của doanh nghiệp.

> **"Ratios are like a doctor's vital signs – they tell you quickly if the patient is healthy, sick, or critical."**

### 2. Tại sao Financial Ratios quan trọng?

| Đối tượng | Sử dụng ratios để | Ratios quan tâm |
|----------|------------------|----------------|
| **Nhà đầu tư** | Quyết định mua/bán cổ phiếu | ROE, P/E, EPS, Dividend Yield |
| **Ngân hàng/Chủ nợ** | Quyết định cho vay | D/E, Interest Coverage, Current Ratio |
| **Nhà quản lý** | Đánh giá hiệu suất, cải thiện | ROA, Inventory Turnover, Operating Margin |
| **Nhà cung cấp** | Đánh giá khả năng thanh toán | Quick Ratio, AP Turnover |
| **Đối thủ** | Benchmarking | Mọi ratios |

### 3. Sơ đồ tổng quan 4 nhóm Ratios

```
                 FINANCIAL RATIOS
                       │
      ┌────────────────┼────────────────┐────────────────┐
      │                │                │                │
 LIQUIDITY       EFFICIENCY       LEVERAGE        PROFITABILITY
 (Thanh khoản)   (Hiệu quả)      (Đòn bẩy)       (Lợi nhuận)
      │                │                │                │
 Current Ratio   Inventory       D/E Ratio        ROE
 Quick Ratio     Turnover        Debt Ratio       ROA
 Cash Ratio      AR Turnover     Interest         Gross Margin
                 AP Turnover     Coverage         Net Margin
                 Asset Turnover  Equity           Operating
                 CCC             Multiplier       Margin
                                                  EBITDA Margin
```

---

## II. NHÓM 1: LIQUIDITY RATIOS (TỶ SỐ THANH KHOẢN)

### 1. Mục đích
Đánh giá khả năng **thanh toán nợ ngắn hạn** của doanh nghiệp.

### 2. Các tỷ số

#### a) Current Ratio (Tỷ số thanh toán hiện hành)

$$\text{Current Ratio} = \frac{\text{Current Assets}}{\text{Current Liabilities}}$$

| Giá trị | Ý nghĩa |
|---------|---------|
| < 1.0 | **Nguy hiểm** – Không đủ TS ngắn hạn cover nợ ngắn hạn |
| 1.0 - 1.5 | **Cảnh báo** – Vừa đủ, nhưng rủi ro nếu có biến động |
| 1.5 - 3.0 | **Khỏe mạnh** – Đủ khả năng thanh toán |
| > 3.0 | **Quá cao** – Có thể sử dụng tài sản không hiệu quả |

**Hạn chế:** Bao gồm hàng tồn kho (có thể khó bán nhanh)

#### b) Quick Ratio / Acid-Test Ratio (Tỷ số thanh toán nhanh)

$$\text{Quick Ratio} = \frac{\text{Current Assets} - \text{Inventory}}{\text{Current Liabilities}}$$

hoặc:

$$\text{Quick Ratio} = \frac{\text{Cash} + \text{Short-term Investments} + \text{AR}}{\text{Current Liabilities}}$$

| Giá trị | Ý nghĩa |
|---------|---------|
| < 0.5 | **Nguy hiểm** – Phụ thuộc bán tồn kho để trả nợ |
| 0.5 - 1.0 | **Chấp nhận được** – Hơi tight |
| 1.0 - 2.0 | **Tốt** – Thanh khoản vững |
| > 2.0 | **Rất tốt** nhưng có thể giữ quá nhiều tiền mặt |

#### c) Cash Ratio (Tỷ số tiền mặt)

$$\text{Cash Ratio} = \frac{\text{Cash} + \text{Cash Equivalents}}{\text{Current Liabilities}}$$

→ Chỉ số nghiêm ngặt nhất – chỉ tính tiền mặt thuần

#### d) So sánh 3 Liquidity Ratios

```
  Strict ◄──────────────────────────────── Lenient
  
  Cash Ratio    <    Quick Ratio    <    Current Ratio
  (Only cash)        (No inventory)      (All current assets)
  
  Ví dụ:
  Current Assets:  Tiền: 100   AR: 200   Inventory: 300   Total: 600
  Current Liab:    400
  
  Cash Ratio:     100/400      = 0.25  → 😟
  Quick Ratio:    (100+200)/400 = 0.75  → 😐
  Current Ratio:  600/400      = 1.50  → 😊
```

**Ví dụ thực tế – So sánh 2 công ty:**

| | Công ty A (Bán lẻ) | Công ty B (SaaS) |
|---|-------------------|-----------------|
| Tiền | 50 triệu | 300 triệu |
| Phải thu (AR) | 100 triệu | 200 triệu |
| Tồn kho | 400 triệu | 0 |
| Current Assets | 550 triệu | 500 triệu |
| Current Liabilities | 300 triệu | 250 triệu |
| **Current Ratio** | **1.83** | **2.00** |
| **Quick Ratio** | **0.50** | **2.00** |
| **Insight** | CR đẹp nhưng QR thấp → phụ thuộc bán hàng tồn kho | Cả hai đều tốt, thanh khoản thực sự mạnh |

---

## III. NHÓM 2: EFFICIENCY RATIOS (TỶ SỐ HIỆU QUẢ)

### 1. Mục đích
Đánh giá **DN sử dụng tài sản hiệu quả như thế nào** để tạo doanh thu.

### 2. Các tỷ số

#### a) Inventory Turnover (Vòng quay hàng tồn kho)

$$\text{Inventory Turnover} = \frac{\text{COGS}}{\text{Average Inventory}}$$

$$\text{Days Inventory Outstanding (DIO)} = \frac{365}{\text{Inventory Turnover}}$$

| Ngành | Turnover tốt | DIO tốt | Ghi chú |
|-------|-------------|---------|---------|
| FMCG (tiêu dùng nhanh) | 8-12x | 30-45 ngày | Nhanh – SP hết hạn sử dụng |
| Thời trang | 4-6x | 60-90 ngày | Theo mùa |
| Điện tử | 6-10x | 35-60 ngày | Mất giá nhanh |
| Nội thất | 2-4x | 90-180 ngày | Chậm hơn |
| Xây dựng | 1-3x | 120-365 ngày | Rất chậm |

**Ví dụ:**

$$\text{COGS} = 2,000 \text{ triệu/năm}, \quad \text{Avg Inventory} = 400 \text{ triệu}$$

$$\text{Turnover} = \frac{2,000}{400} = 5.0 \text{ lần/năm}$$

$$\text{DIO} = \frac{365}{5.0} = 73 \text{ ngày}$$

→ Trung bình mất 73 ngày từ lúc nhập kho đến lúc bán được → Nếu ngành thời trang: chấp nhận được; nếu FMCG: **quá chậm**

#### b) Accounts Receivable Turnover (Vòng quay phải thu)

$$\text{AR Turnover} = \frac{\text{Net Credit Sales}}{\text{Average AR}}$$

$$\text{Days Sales Outstanding (DSO)} = \frac{365}{\text{AR Turnover}}$$

| DSO | Ý nghĩa |
|-----|---------|
| < 30 ngày | Xuất sắc – thu tiền nhanh |
| 30-45 ngày | Tốt |
| 45-60 ngày | Trung bình |
| 60-90 ngày | Cần cải thiện |
| > 90 ngày | Nguy hiểm – rủi ro nợ xấu cao |

#### c) Accounts Payable Turnover (Vòng quay phải trả)

$$\text{AP Turnover} = \frac{\text{COGS (or Purchases)}}{\text{Average AP}}$$

$$\text{Days Payable Outstanding (DPO)} = \frac{365}{\text{AP Turnover}}$$

→ DPO cao = giữ tiền lâu hơn → **tốt cho cash flow** (nhưng không quá lâu để mất tin dụng)

#### d) Cash Conversion Cycle (CCC – Chu kỳ chuyển đổi tiền mặt)

$$\boxed{\text{CCC} = \text{DIO} + \text{DSO} - \text{DPO}}$$

```
  DIO (73 ngày)          DSO (45 ngày)
  ├───────────────────┤├──────────────────┤
  Mua NVL     Bán hàng          Thu tiền
  │                                    │
  ├─────────DPO (60 ngày)──────┤       │
  Nhận NVL                Trả NCC      │
                                       │
  CCC = 73 + 45 - 60 = 58 ngày
  
  → Cần tài trợ vốn lưu động cho 58 ngày
```

| CCC | Ý nghĩa |
|-----|---------|
| < 0 (Negative CCC) | **Tuyệt vời** – Nhận tiền TRƯỚC khi trả (Dell, Amazon) |
| 0 - 30 ngày | Rất tốt |
| 30 - 60 ngày | Bình thường |
| 60 - 90 ngày | Cần optimize |
| > 90 ngày | Quá dài – vốn lưu động bị "đóng băng" |

#### e) Total Asset Turnover (Vòng quay tổng tài sản)

$$\text{Asset Turnover} = \frac{\text{Revenue}}{\text{Average Total Assets}}$$

| Ngành | AT Ratio | Ghi chú |
|-------|---------|---------|
| Bán lẻ | 2.0 - 3.0 | Ít tài sản cố định, doanh thu cao |
| FMCG | 1.0 - 2.0 | Nhà máy + distribution |
| Sản xuất nặng | 0.3 - 0.8 | Nhiều TSCĐ |
| Tech/SaaS | 0.5 - 1.0 | Tài sản vô hình cao |
| Bất động sản | 0.1 - 0.3 | Tài sản rất lớn |

---

## IV. NHÓM 3: LEVERAGE RATIOS (TỶ SỐ ĐÒN BẨY)

### 1. Mục đích
Đánh giá **mức độ sử dụng nợ** và khả năng trả nợ dài hạn.

### 2. Các tỷ số

#### a) Debt-to-Equity Ratio (D/E – Tỷ số nợ trên vốn)

$$\text{D/E Ratio} = \frac{\text{Total Liabilities}}{\text{Total Equity}}$$

| D/E | Ý nghĩa |
|-----|---------|
| < 0.5 | **Bảo thủ** – Ít nợ, rủi ro thấp, nhưng có thể chưa tối ưu leverage |
| 0.5 - 1.5 | **Cân bằng** – Sử dụng đòn bẩy hợp lý |
| 1.5 - 3.0 | **Aggresssive** – Lever nhiều, rủi ro cao, nhưng có thể tối ưu ROE |
| > 3.0 | **Nguy hiểm** – Rủi ro phá sản cao nếu kinh doanh suy giảm |

**Lưu ý:** D/E khác nhau lớn giữa các ngành:

| Ngành | D/E trung bình | Lý do |
|-------|---------------|-------|
| Utilities (điện nước) | 1.5 - 3.0 | Dòng tiền ổn định, tài sản có thể thế chấp |
| BĐS | 2.0 - 5.0 | Đòn bẩy bằng BĐS thế chấp |
| Tech | 0.0 - 0.5 | Cash-rich, ít cần vay |
| Bán lẻ | 0.5 - 1.5 | Vừa phải |
| Ngân hàng | 8.0 - 15.0 | Đặc thù ngành (deposits = liabilities) |

#### b) Debt Ratio (Tỷ số nợ)

$$\text{Debt Ratio} = \frac{\text{Total Liabilities}}{\text{Total Assets}}$$

- Debt Ratio > 50% → Tài sản chủ yếu được tài trợ bằng nợ
- Liên hệ: Debt Ratio = 1 - Equity Ratio

#### c) Interest Coverage Ratio / Times Interest Earned (TIE)

$$\text{Interest Coverage} = \frac{\text{EBIT}}{\text{Interest Expense}}$$

| ICR | Ý nghĩa |
|-----|---------|
| < 1.0 | **Rất nguy** – Không đủ lợi nhuận trả lãi vay |
| 1.0 - 1.5 | **Nguy hiểm** – Chỉ vừa đủ, không có room |
| 1.5 - 3.0 | **Chấp nhận** – Nhưng cần cẩn thận |
| 3.0 - 6.0 | **Tốt** – Dư sức trả lãi |
| > 6.0 | **Rất tốt** – Hoặc ít nợ |

**Ví dụ:**

$$\text{EBIT} = 500 \text{ triệu}, \quad \text{Interest} = 100 \text{ triệu}$$

$$\text{ICR} = \frac{500}{100} = 5.0x$$

→ EBIT có thể giảm 80% mà vẫn cover được interest → **An toàn**

#### d) Equity Multiplier (Hệ số vốn chủ sở hữu)

$$\text{Equity Multiplier} = \frac{\text{Total Assets}}{\text{Total Equity}} = 1 + \text{D/E Ratio}$$

→ Sử dụng trong **DuPont Analysis** (phần dưới)

---

## V. NHÓM 4: PROFITABILITY RATIOS (TỶ SỐ LỢI NHUẬN)

### 1. Mục đích
Đánh giá **khả năng tạo lợi nhuận** từ doanh thu, tài sản, và vốn.

### 2. Các tỷ số

#### a) Gross Margin (Biên lợi nhuận gộp)

$$\text{Gross Margin} = \frac{\text{Revenue} - \text{COGS}}{\text{Revenue}} \times 100\%$$

| Ngành | Gross Margin trung bình | Ghi chú |
|-------|------------------------|---------|
| SaaS/Software | 70-90% | Chi phí biên gần 0 |
| Dược phẩm | 60-80% | R&D cao nhưng SX rẻ |
| Thời trang | 50-65% | Markup cao |
| F&B (nhà hàng) | 60-70% | Food cost 30-40% |
| Bán lẻ | 25-40% | Margin mỏng, volume lớn |
| Xây dựng | 10-20% | Chi phí NVL & nhân công cao |

#### b) Operating Margin (Biên lợi nhuận hoạt động)

$$\text{Operating Margin} = \frac{\text{EBIT}}{\text{Revenue}} \times 100\%$$

→ Phản ánh hiệu quả hoạt động kinh doanh cốt lõi (trước tài chính & thuế)

#### c) Net Profit Margin (Biên lợi nhuận ròng)

$$\text{Net Margin} = \frac{\text{Net Income}}{\text{Revenue}} \times 100\%$$

→ "Bottom line" – Cuối cùng giữ lại bao nhiêu từ mỗi đồng doanh thu

#### d) Return on Equity (ROE – Lợi nhuận trên vốn chủ sở hữu)

$$\boxed{\text{ROE} = \frac{\text{Net Income}}{\text{Average Equity}} \times 100\%}$$

| ROE | Ý nghĩa |
|-----|---------|
| < 5% | Yếu – thấp hơn gửi tiết kiệm |
| 5-10% | Trung bình |
| 10-20% | Tốt |
| 20-30% | Rất tốt |
| > 30% | Xuất sắc (hoặc leverage rất cao) |

**⚠️ ROE cao có thể do:**
1. Kinh doanh thật sự hiệu quả → **Tốt** ✅
2. Sử dụng nợ nhiều (leverage) → **Rủi ro cao** ⚠️
3. Equity thấp (mất vốn) → **Nguy hiểm** ❌

→ Cần phân tích bằng **DuPont** để hiểu rõ

#### e) Return on Assets (ROA – Lợi nhuận trên tài sản)

$$\text{ROA} = \frac{\text{Net Income}}{\text{Average Total Assets}} \times 100\%$$

→ Đo lường hiệu quả sử dụng TÀI SẢN (không phân biệt nguồn vốn)

**So sánh ROE vs ROA:**

| | ROE | ROA |
|---|-----|-----|
| Tử số | Net Income | Net Income |
| Mẫu số | Equity only | Total Assets |
| Ảnh hưởng leverage | Có – leverage tăng ROE | Ít – independent of capital structure |
| Best for | Đánh giá cho cổ đông | Đánh giá hiệu quả quản lý |

---

## VI. DUPONT ANALYSIS – PHÂN TÍCH DUPONT

### 1. DuPont 3 thành phần

$$\boxed{\text{ROE} = \underbrace{\frac{\text{Net Income}}{\text{Revenue}}}_{\text{Net Margin}} \times \underbrace{\frac{\text{Revenue}}{\text{Assets}}}_{\text{Asset Turnover}} \times \underbrace{\frac{\text{Assets}}{\text{Equity}}}_{\text{Equity Multiplier}}}$$

$$\text{ROE} = \text{Profitability} \times \text{Efficiency} \times \text{Leverage}$$

```
                      ROE
                       │
          ┌────────────┼────────────┐
          │            │            │
     Net Margin   Asset Turnover  Equity Multiplier
     (Lợi nhuận)  (Hiệu quả)     (Đòn bẩy)
          │            │            │
     ┌────┴────┐  ┌────┴────┐  ┌───┴───┐
     Net Income   Revenue     Assets
     ─────────    ─────────   ─────────
     Revenue      Assets      Equity
```

### 2. Ví dụ so sánh 2 công ty bằng DuPont

| Component | Công ty X (Luxury) | Công ty Y (Bán lẻ giá rẻ) |
|-----------|-------------------|--------------------------|
| **Net Margin** | 15% | 3% |
| **Asset Turnover** | 0.8x | 3.0x |
| **Equity Multiplier** | 1.5x | 2.5x |
| **ROE** | 15% × 0.8 × 1.5 = **18%** | 3% × 3.0 × 2.5 = **22.5%** |

**Phân tích:**
- **Công ty X**: ROE đến từ **margin cao** (sản phẩm premium)
- **Công ty Y**: ROE đến từ **volume cao** (turnover) + **leverage cao**
- Y có ROE cao hơn nhưng rủi ro hơn (EM = 2.5 vs 1.5)

### 3. DuPont 5 thành phần (Extended)

$$\text{ROE} = \frac{\text{EBT}}{\text{EBIT}} \times \frac{\text{EBIT}}{\text{Revenue}} \times \frac{\text{Revenue}}{\text{Assets}} \times \frac{\text{Assets}}{\text{Equity}} \times \frac{\text{NI}}{\text{EBT}}$$

$$= \text{Interest Burden} \times \text{Operating Margin} \times \text{Asset Turnover} \times \text{Equity Multiplier} \times \text{Tax Efficiency}$$

---

## VII. RED FLAGS & WARNING SIGNS

### 1. Dấu hiệu cảnh báo trong Financial Ratios

| Red Flag | Ratio | Ngưỡng | Ý nghĩa |
|----------|-------|--------|---------|
| 🔴 | Current Ratio < 1.0 | Declining 3 quý liên tiếp | Sắp mất khả năng thanh toán |
| 🔴 | D/E tăng nhanh | +50% trong 1 năm | Vay nợ quá mức |
| 🔴 | Interest Coverage < 1.5 | Và đang giảm | Không đủ trả lãi |
| 🟡 | DIO tăng nhanh | +30% so với cùng kỳ | Hàng tồn kho ứ đọng |
| 🟡 | DSO tăng | > 90 ngày | Khách hàng chậm trả, nợ xấu |
| 🟡 | Gross Margin giảm | -5% YoY | Mất pricing power hoặc NVL tăng |
| 🟡 | ROE tăng do EM tăng | EM tăng nhưng Net Margin giảm | "Đẹp mặt nhưng rỗng ruột" |
| 🟡 | Cash Flow < Net Income | 3+ quý liên tiếp | Earnings quality thấp |

### 2. Sơ đồ cảnh báo

```
  Scenario: DN "trông có vẻ khỏe"
  
  Revenue: ↑ 20%    ← Tốt!
  Net Income: ↑ 25% ← Rất tốt!
  
  NHƯNG nhìn kỹ ratios:
  
  DSO: 45 → 85 ngày       ← Ghi doanh thu nhưng chưa thu được tiền?
  DIO: 30 → 55 ngày       ← Hàng bán không chạy?
  Current Ratio: 2.0 → 1.2 ← Thanh khoản giảm nhanh
  CFO: +100tr → -50tr      ← Cash flow ÂM dù profit DƯƠNG
  
  → CẢNH BÁO: Có thể DN đang "ghi nhận doanh thu ảo" 
     hoặc bán chịu quá nhiều → rủi ro nợ xấu
```

---

## VIII. ƯU VÀ NHƯỢC ĐIỂM

### Ưu điểm

| Ưu điểm | Chi tiết |
|---------|---------|
| **Đơn giản** | Dễ tính toán từ BCTC có sẵn |
| **So sánh được** | Benchmark với ngành, đối thủ, qua các năm |
| **Snapshot nhanh** | "Health check" tài chính trong vài phút |
| **Phổ biến** | Ngôn ngữ chung giữa investor, banker, manager |
| **Early warning** | Phát hiện xu hướng xấu sớm |

### Nhược điểm

| Nhược điểm | Chi tiết |
|-----------|---------|
| **Historical** | Dựa trên quá khứ, không predict tương lai |
| **Manipulation** | BCTC có thể bị "làm đẹp" → ratios sai |
| **Industry-specific** | Phải so sánh cùng ngành, không cross-industry |
| **Single point** | Cần phân tích xu hướng (trend), không chỉ 1 thời điểm |
| **Accounting policies** | Khác biệt VAS/IFRS ảnh hưởng ratios |
| **Non-financial** | Không capture customer satisfaction, innovation, culture |
| **Size bias** | DN nhỏ/lớn có ratios pattern khác nhau |

---

## IX. HOÀN CẢNH VÀ MÔI TRƯỜNG ÁP DỤNG

### 1. Theo mục đích sử dụng

| Mục đích | Ratios quan trọng nhất | Vì sao |
|----------|----------------------|--------|
| **Xin vay ngân hàng** | Current Ratio, D/E, ICR, DSO | NH quan tâm khả năng trả nợ |
| **Gọi vốn đầu tư** | ROE, Revenue Growth, Net Margin | Investor quan tâm return & growth |
| **Quản lý nội bộ** | Gross Margin, CCC, Asset Turnover | Optimize operations |
| **Mua bán DN (M&A)** | EV/EBITDA, ROA, DuPont | Đánh giá giá trị & hiệu quả |
| **Đánh giá đối thủ** | Tất cả, benchmarking | So sánh vị thế cạnh tranh |

### 2. Theo giai đoạn DN

```
  Startup     →  Growth      →  Maturity    →  Decline
  │               │               │               │
  Burn Rate      Revenue         Net Margin      Cash Ratio
  Runway         Growth%         ROE/ROA         D/E
  CAC/LTV        Gross Margin    DuPont          ICR
  CCC            CCC             CCC             Liquidation
                                 Dividend        ratios
                                 Payout
```

---

## X. CASE STUDY THÀNH CÔNG

### Case Study: **Apple Inc. – Ratios phản ánh "cash machine" toàn cầu**

**Financial Ratios của Apple (FY 2023):**

| Ratio | Apple | Industry Avg | Verdict |
|-------|-------|-------------|---------|
| **Gross Margin** | 44.1% | 35% | ⭐ Premium pricing power |
| **Net Margin** | 25.3% | 15% | ⭐ Siêu hiệu quả |
| **ROE** | 160%+ | 20% | ⭐ (nhưng buyback làm equity thấp) |
| **ROA** | 28.3% | 10% | ⭐ Xuất sắc |
| **Current Ratio** | 0.99 | 1.5 | 😐 Thấp – nhưng Apple có cash reserves |
| **D/E** | ~2.0 | 1.0 | 😐 Leverage cao – nhưng chủ ý |
| **Inventory Turnover** | 40x+ | 8x | ⭐⭐ Gần như không giữ tồn kho |
| **DIO** | ~9 ngày | 45 ngày | ⭐⭐ Supply chain xuất sắc |
| **CCC** | ~ -60 ngày | 30 ngày | ⭐⭐ Negative CCC! |

**DuPont Analysis:**

$$\text{ROE} = 25.3\% \times 1.16 \times 5.67 = \sim 166\%$$

| Component | Giá trị | Giải thích |
|-----------|---------|-----------|
| Net Margin | 25.3% | Premium products, ecosystem |
| Asset Turnover | 1.16x | Moderate – ít assets (outsource sản xuất) |
| Equity Multiplier | 5.67x | **Rất cao** – buyback giảm equity |

**Tại sao ROE Apple > 100% nhưng KHÔNG nguy hiểm?**

```
  Normal company:      ROE cao do leverage = RISKY
  Apple:               ROE cao do
                       1. Margin siêu cao (25%)
                       2. Buyback intentional (trả lại cash cho shareholders)
                       3. Cash reserves > $60 billion
                       4. Operating CF > $100 billion/year
  
  → Apple CHỌN leverage, không phải BỊ leverage
  → Cash + CF thừa sức cover mọi nghĩa vụ
```

**Negative CCC giải thích:**

```
  DIO: 9 ngày        (Hầu như không giữ hàng – Foxconn sản xuất & ship thẳng)
  DSO: 28 ngày       (Retailers trả nhanh – Apple có power)
  DPO: 97 ngày       (Apple trả suppliers rất chậm – Apple có power)
  
  CCC = 9 + 28 - 97 = -60 ngày
  
  → Apple NHẬN TIỀN từ khách hàng 
    TRƯỚC KHI TRẢ nhà cung cấp 60 ngày
  → Sử dụng tiền của người khác (suppliers) để hoạt động
  → MIỄN PHÍ working capital financing!
```

**Bài học:**
> 1. **Ratios phải đọc trong context** – Current Ratio < 1 bình thường nguy hiểm, nhưng Apple OK vì cash reserves khổng lồ
> 2. **Negative CCC là đỉnh cao supply chain** – Thu tiền trước, trả sau
> 3. **High leverage can be strategic** – Apple buyback cổ phiếu (giảm equity) để tối ưu return cho shareholders
> 4. **DuPont reveals the story** – ROE 160% nghe "ảo" nhưng phân tích ra thì hợp lý

---

## XI. CASE STUDY THẤT BẠI

### Case Study: **Evergrande – Ratios cảnh báo nhưng bị bỏ qua**

**Bối cảnh:**
China Evergrande Group – tập đoàn BĐS lớn thứ 2 Trung Quốc, nợ $300 tỷ, vỡ nợ năm 2021 và phá sản 2024.

**Financial Ratios cảnh báo NHIỀU NĂM trước vỡ nợ:**

| Ratio | 2018 | 2019 | 2020 | 2021 | Red Flag? |
|-------|------|------|------|------|----------|
| **D/E Ratio** | 4.1x | 5.3x | 6.2x | **7.8x** | 🔴🔴🔴 |
| **Current Ratio** | 1.48 | 1.32 | 1.18 | **0.87** | 🔴 |
| **Interest Coverage** | 2.8x | 2.1x | 1.5x | **0.7x** | 🔴🔴 |
| **Cash Ratio** | 0.15 | 0.12 | 0.08 | **0.03** | 🔴🔴🔴 |
| **Net Margin** | 8.2% | 6.1% | 3.5% | **Negative** | 🔴 |
| **DIO** | 1,200+ ngày | Tăng | Tăng | Tăng | 🔴 |

**Sơ đồ sụp đổ:**

```
  2015-2019: Borrow → Buy land → Build → Sell (pre-sale) → Borrow more
             ↑                                              │
             └──────────────── Loop ────────────────────────┘
             
  2020: "Three Red Lines" policy (Chính phủ TQ):
    1. D/E < 1.0        Evergrande: 6.2x  → 🔴 FAIL
    2. Net Debt/Equity < 1.0    → 🔴 FAIL
    3. Cash/Short-term Debt > 1.0    → 🔴 FAIL
    
  → Không được vay mới → Không trả được nợ cũ
  → Pre-sale buyers không nhận nhà
  → Suppliers & contractors không được trả
  → Domino effect → Default → Bankruptcy
```

**Bài học:**
> 1. **Ratios cảnh báo sớm** – D/E > 5x, ICR < 2x → "ticking time bomb"
> 2. **DIO > 1000 ngày trong BĐS = "inventory" không bán được**
> 3. **Cash Ratio < 0.1 = một cơn gió nhẹ cũng đổ**
> 4. **Leverage trong cyclical industry (BĐS) = cực kỳ nguy hiểm**
> 5. **"Too big to fail" is a myth** – $300 tỷ nợ vẫn phá sản

---

## XII. ÁP DỤNG CHO SME VIỆT NAM

### 1. Top 10 Ratios SME cần theo dõi

| # | Ratio | Vì sao quan trọng | Tần suất check |
|---|-------|-------------------|----------------|
| 1 | **Gross Margin** | Sản phẩm có pricing power không? | Tháng |
| 2 | **Net Margin** | Cuối cùng giữ lại bao nhiêu? | Tháng |
| 3 | **Current Ratio** | Có trả được nợ ngắn hạn? | Tháng |
| 4 | **CCC** | Tiền quay vòng nhanh không? | Quý |
| 5 | **D/E Ratio** | Nợ có quá nhiều không? | Quý |
| 6 | **Burn Rate** | Bao lâu nữa hết tiền? (startup) | Tuần/Tháng |
| 7 | **Revenue Growth** | Đang tăng trưởng không? | Tháng |
| 8 | **DSO** | Khách hàng trả tiền nhanh không? | Tháng |
| 9 | **ROE** | Có xứng đáng với vốn bỏ ra? | Quý |
| 10 | **Operating Margin** | Hoạt động cốt lõi có hiệu quả? | Tháng |

### 2. Dashboard Ratios mẫu cho SME

```
┌──────────────────────────────────────────────────────┐
│     FINANCIAL HEALTH DASHBOARD – THÁNG XX/20XX       │
│     Công ty: _______________                          │
│                                                        │
│  PROFITABILITY           │  LIQUIDITY                  │
│  Gross Margin:  ___% 📊  │  Current Ratio:  ___ 📊    │
│  Net Margin:    ___% 📊  │  Quick Ratio:    ___ 📊    │
│  ROE:           ___% 📊  │  Cash Ratio:     ___ 📊    │
│  ROA:           ___% 📊  │                             │
│                          │  LEVERAGE                    │
│  EFFICIENCY              │  D/E Ratio:      ___ 📊    │
│  Inv Turnover:  ___x     │  Interest Cov:   ___x      │
│  DSO:           ___ days │                             │
│  DPO:           ___ days │  GROWTH                     │
│  CCC:           ___ days │  Revenue Growth:  ___% YoY  │
│  Asset Turnover: ___x    │  Profit Growth:   ___% YoY  │
│                          │                             │
│  🟢 = Good  🟡 = Watch  🔴 = Action needed           │
└──────────────────────────────────────────────────────┘
```

### 3. Checklist phân tích Ratios

| # | Check | Done? |
|---|-------|-------|
| 1 | Tính đủ 4 nhóm ratios (Liquidity, Efficiency, Leverage, Profitability) | ☐ |
| 2 | So sánh với cùng kỳ năm trước (YoY) | ☐ |
| 3 | So sánh với kỳ trước (MoM hoặc QoQ) | ☐ |
| 4 | Benchmark với ngành (nếu có data) | ☐ |
| 5 | DuPont Analysis cho ROE | ☐ |
| 6 | Check red flags (các dấu hiệu cảnh báo) | ☐ |
| 7 | Ghi nhận action items cho ratios xấu | ☐ |
| 8 | Update forecast nếu trend thay đổi | ☐ |

---

## XIII. CÔNG THỨC TỔNG HỢP

### Liquidity

$$\text{Current Ratio} = \frac{\text{CA}}{\text{CL}}$$

$$\text{Quick Ratio} = \frac{\text{CA} - \text{Inventory}}{\text{CL}}$$

### Efficiency

$$\text{Inventory Turnover} = \frac{\text{COGS}}{\text{Avg Inventory}}, \quad \text{DIO} = \frac{365}{\text{Inv Turnover}}$$

$$\text{AR Turnover} = \frac{\text{Revenue}}{\text{Avg AR}}, \quad \text{DSO} = \frac{365}{\text{AR Turnover}}$$

$$\text{CCC} = \text{DIO} + \text{DSO} - \text{DPO}$$

### Leverage

$$\text{D/E} = \frac{\text{Total Liabilities}}{\text{Equity}}, \quad \text{ICR} = \frac{\text{EBIT}}{\text{Interest}}$$

### Profitability

$$\text{ROE} = \frac{\text{NI}}{\text{Equity}}, \quad \text{ROA} = \frac{\text{NI}}{\text{Assets}}$$

$$\text{Gross Margin} = \frac{\text{Revenue} - \text{COGS}}{\text{Revenue}}$$

### DuPont

$$\text{ROE} = \text{Net Margin} \times \text{Asset Turnover} \times \text{Equity Multiplier}$$

---

## XIV. TÀI LIỆU THAM KHẢO

1. **Brealey, Myers & Allen** – "Principles of Corporate Finance" (Ratio Analysis)
2. **Palepu, Healy & Peek** – "Business Analysis & Valuation" (Financial Statement Analysis)
3. **Damodaran** – "The Little Book of Valuation" (Accessible ratios guide)
4. **CFA Institute** – Level I: Financial Reporting and Analysis
5. **Aswath Damodaran** – NYU datasets (industry average ratios)
6. **Kieso, Weygandt** – "Intermediate Accounting" (Ratio interpretation)
7. **McKinsey** – "Valuation" Ch. 6 (Analyzing Performance)
