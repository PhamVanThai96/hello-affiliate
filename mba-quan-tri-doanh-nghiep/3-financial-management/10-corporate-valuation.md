# Corporate Valuation – Định Giá Doanh Nghiệp (DCF, Comparables, Precedent)

> **Mục tiêu**: Nắm vững 3 phương pháp định giá chính – DCF (Discounted Cash Flow), Comparable Companies Analysis, Precedent Transactions – hiểu **bản chất và nguồn gốc** của từng công thức, biết kết hợp chúng thành một khoảng giá trị (Football Field) và áp dụng được cho cả doanh nghiệp lớn lẫn SME Việt Nam.

---

## I. KHÁI NIỆM & LÝ THUYẾT

### 1. Định nghĩa

**Corporate Valuation** (Định giá doanh nghiệp) là quá trình **xác định giá trị kinh tế nội tại** (intrinsic value) của một doanh nghiệp, dựa trên phân tích tài chính, dòng tiền tương lai và so sánh với thị trường.

> **"Price is what you pay, value is what you get."** – Warren Buffett
> Price (giá thị trường) ≠ Value (giá trị thực). Định giá đi tìm VALUE, còn thương lượng mới là nơi quyết định PRICE.

Một điểm rất quan trọng cho người mới: **định giá không cho ra một con số "đúng", mà cho ra một khoảng hợp lý (range)** kèm theo các giả định rõ ràng. Hai chuyên gia có thể ra hai kết quả khác nhau mà cả hai đều "đúng" – miễn là giả định của mỗi người minh bạch và có căn cứ.

### 2. Khi nào cần định giá?

| Tình huống | Mục đích |
|-----------|---------|
| **M&A** | Bên mua: trả bao nhiêu? Bên bán: chấp nhận bao nhiêu? |
| **IPO** | Xác định giá phát hành cổ phiếu lần đầu |
| **Investment** | Cổ phiếu overvalued hay undervalued? Buy/Sell/Hold? |
| **Fundraising** | Startup/SME gọi vốn: pre-money valuation bao nhiêu? Nhường bao nhiêu % cổ phần? |
| **Legal/Tax** | Ly hôn, thừa kế, thuế chuyển nhượng vốn |
| **Internal strategy** | Nên giữ, bán, hay spin-off một bộ phận? |
| **Restructuring** | Phá sản, tái cơ cấu – giá trị hoạt động liên tục (going concern) vs giá trị thanh lý (liquidation) |
| **Fairness opinion** | Định giá độc lập cho HĐQT/cổ đông phê duyệt giao dịch |
| **Kế thừa & chia tách gia đình (SME)** | Chia cổ phần giữa các thành viên, mua lại phần của người rút vốn |

### 3. Bối cảnh lịch sử: Vì sao dòng tiền chiết khấu trở thành "ngôn ngữ chung" của định giá?

- **Irving Fisher (1930, "The Theory of Interest")** là người đặt nền móng tư tưởng: giá trị của bất kỳ tài sản nào bằng **giá trị hiện tại của các khoản tiền nó sẽ mang lại** trong tương lai. Một đồng hôm nay có giá trị hơn một đồng ngày mai (xem lại bài 01 – Time Value of Money).
- **John Burr Williams (1938, "The Theory of Investment Value")** áp dụng ý tưởng đó vào cổ phiếu: giá trị cổ phiếu = chiết khấu toàn bộ cổ tức tương lai. Đây là mô hình DDM (Dividend Discount Model) – tiền thân của DCF.
- **Myron Gordon (1959)** đơn giản hóa chuỗi vô hạn thành công thức tăng trưởng đều (Gordon Growth Model) – nền tảng của Terminal Value.
- **Graham & Dodd (1934, "Security Analysis")** phổ biến cách nhìn "định giá tương đối" qua P/E và các hệ số, dạy nhà đầu tư so sánh giá với lợi nhuận. Đây là tổ tiên của Comps.
- **William Sharpe (CAPM, 1964)** và **Modigliani–Miller (1958)** cho phép tính tỷ lệ chiết khấu (WACC) một cách có hệ thống – mảnh ghép cuối cùng để DCF dùng được cho cả doanh nghiệp.
- **Aswath Damodaran (NYU)** ngày nay là nguồn tham khảo phổ biến nhất về dữ liệu và phương pháp luận (beta, ERP, multiples theo ngành).

> **Vì sao có 2 trường phái?** Định giá **nội tại (DCF)** hỏi "doanh nghiệp này SINH RA bao nhiêu tiền?". Định giá **tương đối (Comps, Precedent)** hỏi "thị trường ĐANG TRẢ bao nhiêu cho những doanh nghiệp giống nó?". Cả hai đều cần: DCF giúp bạn hiểu *vì sao* giá trị như vậy; Comps giúp bạn kiểm tra giá trị đó có *thực tế* trên thị trường không.

### 4. Enterprise Value vs Equity Value

**Tại sao phải tách hai khái niệm này?** Một doanh nghiệp được tài trợ bởi hai nhóm: chủ nợ (ngân hàng, trái chủ) và chủ sở hữu (cổ đông). Dòng tiền hoạt động (FCFF) là "chiếc bánh" chung chia cho cả hai nhóm. Giá trị của chiếc bánh đó là **Enterprise Value (EV)**. Sau khi trả phần của chủ nợ, phần còn lại thuộc về cổ đông là **Equity Value**. Nếu so sánh hai công ty chỉ bằng vốn hóa (Market Cap), công ty vay nhiều sẽ trông "rẻ" một cách giả tạo – vì phần nợ chưa được cộng vào. EV loại bỏ sự méo mó do cơ cấu vốn, nên hai công ty khác đòn bẩy vẫn so sánh được.

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

**Nguyên tắc "khớp tử – mẫu" (cực kỳ quan trọng):**

| Tử số (giá trị) | Mẫu số (chỉ tiêu) | Lý do |
|-----------------|------------------|-------|
| **EV** | EBITDA, EBIT, Revenue (chỉ tiêu *trước* lãi vay) | Chỉ tiêu trước lãi vay thuộc về *cả* chủ nợ và cổ đông → khớp với EV |
| **Equity Value / Giá cổ phiếu** | Net Income, EPS, Book Value (chỉ tiêu *sau* lãi vay) | Chỉ tiêu sau lãi vay chỉ thuộc về cổ đông → khớp với Equity |

Ghép EV với Net Income (hoặc Equity với EBITDA) là một lỗi "ghép sai" rất phổ biến của người mới.

### 5. Tổng quan 3 phương pháp

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

### 6. Quy trình định giá tổng quát (cho người mới)

```
1. Hiểu doanh nghiệp: mô hình kinh doanh, ngành, động lực tăng trưởng
2. Chuẩn hóa số liệu quá khứ (loại khoản bất thường, chi phí cá nhân của chủ)
3. Chạy DCF (nội tại)  ─┐
4. Chạy Comps          ─┼─► 5. Đặt cạnh nhau (Football Field)
5. Chạy Precedent      ─┘          │
                                   ▼
6. Cầu nối sang Equity Value (trừ nợ ròng, cộng tài sản phi hoạt động)
7. Điều chỉnh (thiếu thanh khoản, quyền kiểm soát, pha loãng)
8. Đưa ra KHOẢNG giá trị + khuyến nghị
```

---

## II. CHI TIẾT TỪNG THÀNH PHẦN

### A. DCF – Discounted Cash Flow (Phương pháp chiết khấu dòng tiền)

#### A.1. Tại sao lại là "dòng tiền" chứ không phải "lợi nhuận kế toán"?

Lợi nhuận kế toán chịu ảnh hưởng của các quy ước (khấu hao, dồn tích, trích lập dự phòng) và có thể bị "làm đẹp"; còn **tiền mặt** thì không thể giả. Một doanh nghiệp có lãi trên sổ sách nhưng liên tục tăng khoản phải thu và tồn kho, đầu tư máy móc liên tục, có thể vẫn *không có đồng nào* để trả cho chủ nợ và cổ đông. Nhà đầu tư chỉ thực sự nhận được **tiền mặt còn lại sau khi đã tái đầu tư để duy trì và phát triển hoạt động** – đó chính là Free Cash Flow. Vì vậy DCF định giá bằng FCF.

#### A.2. Công thức lõi

$$EV = \sum_{t=1}^{n} \frac{FCFF_t}{(1+WACC)^t} + \frac{TV}{(1+WACC)^n}$$

- $FCFF_t$: dòng tiền tự do cho toàn bộ nhà cung cấp vốn ở năm $t$
- $WACC$: tỷ lệ chiết khấu (chi phí vốn bình quân gia quyền – xem bài 03)
- $TV$: Terminal Value (giá trị cuối kỳ dự phóng)
- $n$: số năm dự phóng chi tiết (thường 5–10 năm)

**Tại sao chiết khấu bằng WACC?** FCFF thuộc về cả chủ nợ lẫn cổ đông, nên tỷ lệ chiết khấu phải phản ánh *lợi suất đòi hỏi trung bình* của cả hai – đó chính là WACC. Nếu dùng FCFE (dòng tiền sau khi đã trả nợ) thì phải dùng $K_e$ (chi phí vốn chủ), vì chỉ cổ đông nhận dòng tiền này. **Dòng tiền nào thì tỷ lệ chiết khấu đó** – không bao giờ trộn.

#### A.3. Quy trình 6 bước

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

#### A.4. Free Cash Flow to Firm (FCFF)

**Logic xây dựng công thức** – hãy đọc từng thành phần như một câu hỏi "tiền thực sự còn lại bao nhiêu?":

1. Bắt đầu từ lợi nhuận hoạt động **EBIT**.
2. Trừ thuế *như thể công ty không vay nợ*: $EBIT \times (1-T)$ = **NOPAT** (Net Operating Profit After Tax). Dùng thuế "không vay" vì lợi ích thuế của lãi vay đã được tính trong WACC (qua $K_d(1-T)$) – nếu tính cả hai nơi sẽ **đếm trùng**.
3. Cộng lại **D&A** (khấu hao): đây là chi phí kế toán *không* chi ra tiền trong kỳ.
4. Trừ **CAPEX**: tiền thật sự chi mua máy móc, nhà xưởng để duy trì/mở rộng hoạt động.
5. Trừ **ΔNWC** (tăng vốn lưu động): bán chịu nhiều hơn, tồn kho nhiều hơn → tiền bị "kẹt" trong tài sản ngắn hạn.

$$FCFF = EBIT \times (1-T) + D\&A - CAPEX - \Delta NWC$$

| Component | Source | Note |
|-----------|--------|------|
| EBIT × (1-T) | Income Statement | = NOPAT |
| + D&A | Income Statement/CF | Add back non-cash expense |
| - CAPEX | CF Statement (Investing) | Maintenance + Growth |
| - ΔNWC | Balance Sheet changes | Increase = cash outflow |

**Các công thức liên quan**:

$$FCFE = FCFF - Lãi\,vay \times (1-T) + Nợ\,vay\,ròng\,mới$$

$$Tỷ\,lệ\,tái\,đầu\,tư\;(RR) = \frac{CAPEX - D\&A + \Delta NWC}{NOPAT} \qquad g = RR \times ROIC$$

Công thức $g = RR \times ROIC$ rất hữu ích để "kiểm tra thực tế" giả định tăng trưởng: doanh nghiệp chỉ tăng trưởng bền vững được nếu nó **tái đầu tư** và tái đầu tư đó **sinh lời** (ROIC). Tăng trưởng không tốn tiền đầu tư là ảo tưởng.

#### A.5. Terminal Value – Tại sao cần, và 2 cách tính

**Vì sao cần TV?** Doanh nghiệp không "chết" sau năm thứ 5. Nếu chỉ cộng 5 năm FCFF, ta bỏ quên phần giá trị từ năm 6 đến vô hạn – thường chiếm phần lớn giá trị. TV là một "gói gọn" giá trị của mọi dòng tiền sau kỳ dự phóng.

**Method 1: Gordon Growth Model (Perpetuity)**

Nguồn gốc: tổng của một cấp số nhân lùi vô hạn. Nếu FCFF năm $n+1$ tăng đều $g$ mỗi năm và chiết khấu $WACC$, tổng giá trị hiện tại tại năm $n$ là:

$$TV = \frac{FCFF_{n+1}}{WACC - g} = \frac{FCFF_n \times (1+g)}{WACC - g}$$

- $g$ = tốc độ tăng trưởng dài hạn bền vững (thường 2–4%, **không vượt tăng trưởng GDP danh nghĩa** – vì doanh nghiệp không thể to hơn nền kinh tế mãi mãi).
- Điều kiện bắt buộc: $WACC > g$ (nếu không, công thức vô nghĩa).
- **CẢNH BÁO**: TV thường = 60–80% tổng giá trị DCF → cực kỳ nhạy với $g$ và $WACC$ (khi $WACC - g$ nhỏ, mẫu số nhỏ, TV bùng nổ).
- Lưu ý chuẩn hóa: $FCFF_{n+1}$ nên là dòng tiền **trạng thái bền vững** (capex phản ánh tái đầu tư đủ để đạt tăng trưởng $g$, không phải số năm cuối tăng trưởng nhanh).

**Method 2: Exit Multiple**

$$TV = EBITDA_n \times Exit\,Multiple$$

- Exit Multiple = EV/EBITDA của các công ty tương đương (từ Comps).
- Mang tính "thị trường" hơn nhưng có tính **vòng tròn** (dùng định giá tương đối bên trong phương pháp nội tại).
- **Kiểm tra chéo**: từ TV Gordon, tính ngược multiple ngụ ý $TV / EBITDA_n$ và so với thị trường; ngược lại từ Exit Multiple tính ngược $g$ ngụ ý. Hai cách nên cho kết quả hội tụ.

#### A.6. Ví dụ DCF – Công ty công nghệ (từng bước)

**Giả định**:
- Doanh thu Y1: 1,000 tỷ VND, tăng trưởng giảm dần (Y5 = 1,580 tỷ)
- EBIT margin mở rộng từ 20% → 25%
- Thuế $T$ = 20%, D&A = 5% doanh thu, CAPEX = 7% doanh thu
- ΔNWC = 3% × ΔDoanh thu (Y1 bằng 0 để đơn giản hóa)
- WACC = 11%, Terminal $g$ = 3%
- Nợ ròng = 300 tỷ, số cổ phiếu = 100 triệu

**Bước 1: Dự phóng FCFF** (đơn vị: tỷ VND; ví dụ Y3: EBIT = 1,300 × 22% = 286; NOPAT = 286 × 0.8 = 228.8; D&A = 65; CAPEX = 91; ΔNWC = 3% × 150 = 4.5; FCFF = 228.8 + 65 − 91 − 4.5 = 198.3)

| Year | Revenue | EBIT | NOPAT | D&A | CAPEX | ΔNWC | FCFF | Hệ số chiết khấu | PV(FCFF) |
|------|---------|------|-------|-----|-------|------|------|-----------------|----------|
| 1 | 1,000 | 200.0 | 160.0 | 50.0 | 70.0 | 0.0 | 140.0 | 0.9009 | 126.1 |
| 2 | 1,150 | 241.5 | 193.2 | 57.5 | 80.5 | 4.5 | 165.7 | 0.8116 | 134.5 |
| 3 | 1,300 | 286.0 | 228.8 | 65.0 | 91.0 | 4.5 | 198.3 | 0.7312 | 145.0 |
| 4 | 1,450 | 333.5 | 266.8 | 72.5 | 101.5 | 4.5 | 233.3 | 0.6587 | 153.7 |
| 5 | 1,580 | 395.0 | 316.0 | 79.0 | 110.6 | 3.9 | 280.5 | 0.5935 | 166.5 |
| | | | | | | | **Tổng PV(FCFF 1–5)** | | **725.8** |

**Bước 2: Terminal Value** (Gordon):

$$TV = \frac{280.5 \times 1.03}{0.11 - 0.03} = \frac{288.9}{0.08} = 3{,}611 \text{ tỷ} \qquad PV(TV) = \frac{3{,}611}{1.11^5} = 2{,}143 \text{ tỷ}$$

Kiểm tra chéo: $TV / EBITDA_5 = 3{,}611 / (395 + 79) = 7.6x$ → hợp lý so với multiple ngành.

**Bước 3: Enterprise Value và Equity Value**

| Component | Giá trị |
|-----------|--------|
| PV(FCFF Year 1-5) | 725.8 tỷ |
| PV(Terminal Value) | 2,143.2 tỷ |
| **Enterprise Value** | **2,869 tỷ** |
| − Net Debt | (300 tỷ) |
| **Equity Value** | **2,569 tỷ** |
| ÷ Số cổ phiếu | 100 triệu |
| **Value per Share** | **≈ 25,690 VND** |

→ PV(TV)/EV = 2,143 / 2,869 = **74.7%**. Gần 3/4 giá trị nằm ở giả định "sau năm 5" – cực kỳ nhạy cảm.

#### A.7. Bảng độ nhạy (Sensitivity Table)

**Tại sao bắt buộc phải làm?** Vì DCF phụ thuộc vào những giả định không ai biết chắc. Thay vì đưa ra một con số duy nhất tạo cảm giác chính xác giả, bảng độ nhạy cho thấy *khoảng* giá trị khi WACC và $g$ thay đổi – giúp người ra quyết định hiểu mức độ bất định.

Giá trị mỗi cổ phiếu (VND), tính lại toàn bộ mô hình cho từng cặp WACC–g:

| | g = 2% | g = 3% | g = 4% |
|-|--------|--------|--------|
| **WACC = 9%** | 31,251 | 35,982 | 42,606 |
| **WACC = 10%** | 26,674 | 30,095 | 34,656 |
| **WACC = 11%** | 23,123 | **25,690** | 28,989 |
| **WACC = 12%** | 20,291 | 22,272 | 24,748 |
| **WACC = 13%** | 17,981 | 19,545 | 21,457 |

→ Khoảng giá: ~18,000 – 42,600 VND (chênh hơn 2.3 lần) chỉ vì thay đổi WACC ±2% và $g$ ±1%. **WACC và $g$ chi phối kết quả.**

#### A.8. Các biến thể và quy ước nâng cao (tham khảo)

| Chủ đề | Nội dung |
|--------|---------|
| **Mid-year convention** | Dòng tiền phát sinh đều trong năm, nên chiết khấu theo $t - 0.5$ thay vì $t$ → giá trị cao hơn khoảng $(1+WACC)^{0.5}$ lần (~5% với WACC 11%) |
| **Stub period** | Nếu định giá giữa năm tài chính, chỉ chiết khấu phần dòng tiền còn lại của năm đầu |
| **DDM (Dividend Discount Model)** | Chiết khấu cổ tức bằng $K_e$ – dùng cho ngân hàng, bảo hiểm (nơi khó xác định FCFF) |
| **FCFE** | Chiết khấu dòng tiền cho cổ đông bằng $K_e$ → ra thẳng Equity Value |
| **APV (Adjusted Present Value)** | Định giá như không nợ, cộng riêng PV của lá chắn thuế – dùng khi cơ cấu vốn thay đổi mạnh (LBO) |

---

### B. Comparable Companies Analysis ("Comps" / Trading Multiples)

#### B.1. Tại sao có phương pháp này? Logic "định luật một giá"

Nguyên lý nền tảng: **tài sản giống nhau nên có giá gần nhau**. Khi bạn định giá căn nhà, bạn nhìn giá những căn tương tự trong khu phố, chia cho diện tích để ra giá/m², rồi nhân với diện tích căn nhà của bạn. Comps làm đúng như vậy với doanh nghiệp: tính "giá/đơn vị lợi nhuận" (multiple) của các công ty niêm yết tương tự, rồi nhân với chỉ tiêu của công ty mục tiêu. Nhanh, dễ giải thích, phản ánh tâm lý thị trường hiện tại.

#### B.2. Quy trình

```
1. SELECT comparable companies (same industry, size, growth, profitability)
2. CALCULATE their trading multiples
3. APPLY median/mean multiple to target's metrics
4. DERIVE implied valuation range
```

**Tại sao dùng trung vị (median) thay vì trung bình (mean)?** Chỉ một công ty có multiple bất thường (ví dụ 25x vì thị trường "hype") sẽ kéo trung bình lên rất cao, còn trung vị bền vững với giá trị ngoại lai (outlier).

#### B.3. Các multiple chính và khi nào dùng

| Multiple | Công thức | Phù hợp khi |
|----------|----------|-------------|
| **EV/Revenue** | Enterprise Value / Revenue | Công ty chưa có lãi (SaaS, biotech) |
| **EV/EBITDA** | EV / EBITDA | Phổ biến nhất; trung lập với cơ cấu vốn, chính sách khấu hao, thuế |
| **EV/EBIT** | EV / EBIT | Khi D&A lớn và khác biệt (ngành vốn nặng) |
| **P/E** | Price / EPS | Doanh nghiệp trưởng thành, lợi nhuận ổn định |
| **P/B** | Price / Book Value | Ngân hàng, tài chính, ngành nặng tài sản |
| **P/FCF** | Price / Free Cash Flow | Tập trung vào dòng tiền |
| **EV/Subscribers** | EV / số thuê bao | Viễn thông, streaming, SaaS |

**Vì sao EV/EBITDA được ưa chuộng?** EBITDA loại bỏ ba yếu tố khác biệt giữa các công ty: lãi vay (cơ cấu vốn), thuế (quy định mỗi nước) và khấu hao (chính sách kế toán). Nhờ đó, hai công ty khác quốc gia, khác đòn bẩy vẫn có thể so sánh. Hạn chế: EBITDA bỏ qua chi tiêu vốn (CAPEX) – ngành đầu tư nặng dễ bị "thổi phồng".

**Mối quan hệ với DCF**: multiple thực chất là DCF "nén" lại. Trong tăng trưởng đều, $EV/EBITDA$ cao khi tăng trưởng cao, rủi ro (WACC) thấp và tái đầu tư ít – vì vậy các công ty có multiple khác nhau thường do **khác biệt về tăng trưởng, rủi ro, hiệu quả sinh lời**, không chỉ do "thị trường định giá sai".

#### B.4. Ví dụ Comps

**Target**: công ty thương mại điện tử Việt Nam, Revenue = 5,000 tỷ, EBITDA = 400 tỷ (số liệu peer minh họa, không phải số liệu thời điểm thực).

| Comparable | EV/Revenue | EV/EBITDA |
|-----------|-----------|-----------|
| MWG (VN) | 0.8x | 10.5x |
| FPT Retail (VN) | 0.5x | 8.2x |
| Sea Limited (SE Asia) | 2.5x | 25x |
| Tokopedia/GoTo (Indo) | 1.5x | NM (EBITDA âm, không có ý nghĩa) |
| **Median** | **1.15x** | **10.5x** |

Chú ý cách tính trung vị: EV/Revenue gồm 4 giá trị (0.5; 0.8; 1.5; 2.5) → trung vị = (0.8 + 1.5)/2 = 1.15x. EV/EBITDA chỉ có 3 giá trị hợp lệ (8.2; 10.5; 25) → trung vị = 10.5x (NM bị loại).

**Implied Valuation**:
- EV/Revenue: 5,000 × 1.15 = **5,750 tỷ VND**
- EV/EBITDA: 400 × 10.5 = **4,200 tỷ VND**
- Khoảng: **4,200 – 5,750 tỷ VND**

Hai kết quả chênh 37% – phản ánh việc công ty mục tiêu có biên EBITDA (8%) thấp hơn so với các peer có EV/Revenue cao; đây là lý do người định giá **không dựa vào một multiple duy nhất**.

#### B.5. Ưu & nhược điểm của Comps

| ✅ Ưu điểm | ❌ Nhược điểm |
|-------------|---------------|
| Dựa trên thị trường (phản ánh tâm lý nhà đầu tư) | Thị trường có thể định giá sai (cả nhóm peer cùng bị định giá cao/thấp) |
| Đơn giản, tính nhanh | "Không có hai công ty hoàn toàn giống nhau" |
| Luôn có sẵn (nếu có peer niêm yết) | Khác biệt về tăng trưởng, biên lợi nhuận, rủi ro → multiple khác nhau |
| Dễ giải thích: "đang giao dịch ở 12x EBITDA như các peer" | Multiple thay đổi theo chu kỳ thị trường |

---

### C. Precedent Transactions Analysis (Giao dịch tương đương)

#### C.1. Tại sao khác với Comps?

Comps cho biết giá **một cổ phiếu lẻ** (quyền sở hữu thiểu số, không kiểm soát) trên sàn. Nhưng khi một bên mua **toàn bộ** hoặc **phần chi phối** công ty, họ trả thêm phần "phí kiểm soát" (control premium) – vì quyền quyết định chiến lược, bổ nhiệm ban lãnh đạo, hưởng đồng lực hợp nhất (synergy) và hưởng toàn bộ dòng tiền. Precedent Transactions đo đúng mức giá mà người mua đã **thực sự trả** để nắm quyền kiểm soát.

#### C.2. Quy trình

```
1. IDENTIFY past M&A transactions in similar industry
2. CALCULATE transaction multiples (include control premium!)
3. APPLY to target's metrics
4. ADJUST for market conditions, timing, synergies
```

#### C.3. Khác biệt so với Trading Comps

| | Trading Comps | Precedent Transactions |
|-|---------------|----------------------|
| Data source | Giá cổ phiếu hiện tại | Giá giao dịch M&A trong quá khứ |
| Premium | Không có phí kiểm soát | BAO GỒM phí kiểm soát 20–50% |
| Timing | Thị trường hiện tại | Quá khứ (có thể lỗi thời) |
| Relevance | Giá trị thị trường (thiểu số) | Giá trị mua lại (kiểm soát) |
| Availability | Luôn có (nếu niêm yết) | Hạn chế (ít thương vụ, nhiều thương vụ không công bố giá) |

**Công thức phí kiểm soát (Control Premium)**:

$$Control\,Premium = \frac{Giá\,chào\,mua - Giá\,thị\,trường\,trước\,thông\,báo}{Giá\,thị\,trường\,trước\,thông\,báo}$$

#### C.4. Ví dụ Precedent Transactions

| Transaction | Year | EV/EBITDA | EV/Revenue | Premium |
|-------------|------|-----------|-----------|---------|
| Deal A (cùng ngành) | 2024 | 12.0x | 1.8x | 35% |
| Deal B | 2023 | 11.5x | 1.5x | 28% |
| Deal C | 2023 | 14.0x | 2.2x | 42% |
| Deal D | 2022 | 10.0x | 1.3x | 25% |
| **Median** | | **11.75x** | **1.65x** | **31.5%** |

Trung vị EV/EBITDA (4 giá trị: 10.0; 11.5; 12.0; 14.0) = (11.5 + 12.0)/2 = 11.75x.

**Implied Valuation** (Target EBITDA = 400 tỷ): EV = 400 × 11.75 = **4,700 tỷ VND** (đã bao gồm phí kiểm soát).

Lưu ý: giá này **cao hơn** Comps (4,200) là điều bình thường vì có phí kiểm soát; nếu bạn là người *bán 100%* công ty thì Precedent là tham chiếu phù hợp hơn; nếu bạn là cổ đông thiểu số thì Comps phù hợp hơn.

---

### D. Tổng hợp – "Football Field" Valuation

**Tại sao dùng biểu đồ Football Field?** Mỗi phương pháp có điểm mạnh/yếu và cho một khoảng khác nhau. Biểu đồ "sân bóng" đặt các khoảng cạnh nhau (thanh ngang) để người ra quyết định nhìn ra *vùng chồng lấn* – nơi các phương pháp cùng đồng ý – và hiểu mức độ bất định, thay vì tin vào một con số duy nhất.

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

(Số liệu trong sơ đồ chỉ mang tính minh họa cách đọc; 52-Week Range là biên độ giá cổ phiếu 52 tuần, LBO là mức giá tối đa quỹ PE có thể trả để đạt IRR mục tiêu.)

### E. Điều chỉnh để chuyển từ EV sang giá trị phần vốn thực nhận (Equity Bridge và các chiết khấu/phụ trội)

#### E.1. Equity Bridge đầy đủ

$$Equity\,Value = EV - Nợ\,vay - Cổ\,phiếu\,ưu\,đãi - Lợi\,ích\,cổ\,đông\,thiểu\,số - Nợ\,thuê\,tài\,chính + Tiền\,và\,tương\,đương\,tiền + Tài\,sản\,phi\,hoạt\,động$$

Lý do: DCF/multiple chỉ định giá **hoạt động kinh doanh cốt lõi**. Tiền thừa, bất động sản cho thuê ngoài lĩnh vực chính (tài sản phi hoạt động) không nằm trong FCFF nên phải cộng thêm; ngược lại, mọi quyền đòi trước cổ đông (nợ, ưu đãi, cổ đông thiểu số của công ty con) phải trừ ra.

#### E.2. Các điều chỉnh phụ trội/chiết khấu thường gặp

| Điều chỉnh | Khi nào áp dụng | Mức tham khảo |
|-----------|----------------|--------------|
| **Control Premium** (phụ trội kiểm soát) | Mua quyền chi phối, định giá từ Comps (thiểu số) → giá kiểm soát | 20–50% |
| **DLOM** (Discount for Lack of Marketability – chiết khấu thiếu thanh khoản) | Công ty không niêm yết, khó bán cổ phần | 15–30% |
| **DLOC** (Discount for Lack of Control – chiết khấu thiếu kiểm soát) | Bán/mua phần thiểu số | 15–35% |
| **Size premium / Key-person discount** | SME nhỏ, phụ thuộc chủ | Cộng vào $K_e$ 2–5% hoặc chiết khấu giá trị |
| **Diluted shares** | Có ESOP, quyền chọn, trái phiếu chuyển đổi | Dùng số cổ phiếu pha loãng (Treasury Stock Method) |

> Cẩn thận **không đếm trùng**: nếu đã cộng "size premium" vào $K_e$ thì không nên chiết khấu DLOM nặng thêm cho cùng một yếu tố rủi ro.

---

### F. Ưu điểm và Nhược điểm của từng phương pháp

#### F.1. DCF

**✅ Ưu điểm**:
1. **Intrinsic** – dựa trên nền tảng kinh doanh, không phụ thuộc tâm lý thị trường
2. **Forward-looking** – tính dòng tiền tương lai, không chỉ trạng thái hiện tại
3. **Linh hoạt** – mô hình hóa được bất kỳ doanh nghiệp, bất kỳ giả định nào
4. **Vững chắc về lý thuyết** – giá trị = hiện giá dòng tiền tương lai

**❌ Nhược điểm**:
1. **Nhạy cảm** – thay đổi nhỏ về WACC/g tạo chênh lệch giá trị khổng lồ
2. **Phụ thuộc Terminal Value** – TV chiếm 60–80% giá trị → một giả định duy nhất quyết định tất cả
3. **Garbage in = Garbage out** – dự phóng FCF 5–10+ năm rất bất định
4. **Phức tạp** – nhiều giả định, dễ bị thao túng
5. **Khó với doanh nghiệp chưa có doanh thu** – không có dòng tiền → DCF = 0? (cần cách tiếp cận sáng tạo)

#### F.2. Comps

**✅ Ưu điểm**:
1. **Đơn giản & nhanh** – tính trong vài phút
2. **Dựa trên thị trường** – phản ánh cái nhà đầu tư thực sự trả
3. **Luôn có sẵn** – nếu peers niêm yết
4. **Dễ giải thích** – "đang giao dịch 12x EBITDA như các peer"

**❌ Nhược điểm**:
1. **Không có peer hoàn hảo** – mỗi công ty là duy nhất
2. **Vòng tròn** – nếu cả nhóm peer bị định giá cao → bạn cũng định giá cao theo
3. **Bỏ qua nền tảng DCF** – có thể bỏ sót khác biệt về tăng trưởng/rủi ro
4. **Dễ thao túng** – chọn peer "có lợi" để ra đáp số mong muốn

#### F.3. Precedent Transactions

**✅ Ưu điểm**: phản ánh giá thực sự người mua đã trả (đã bao gồm phí kiểm soát và synergy); là chuẩn tham chiếu trực tiếp cho giao dịch M&A.
**❌ Nhược điểm**: ít dữ liệu, dữ liệu cũ (điều kiện thị trường lúc đó khác); đặc biệt khó với SME vì phần lớn thương vụ không công bố giá; mức giá có thể chứa synergy riêng của người mua cụ thể.

---

### G. Lưu ý về phương pháp (Best Practices, Pitfalls, Tình huống đặc biệt)

#### G.1. DCF Best Practices

| Practice | Rationale |
|----------|-----------|
| Dùng FCFF + WACC để ra EV (thay vì FCFE) | Ổn định hơn, phổ biến, tách bạch quyết định hoạt động và tài trợ |
| Terminal growth ≤ tăng trưởng GDP | Công ty không thể lớn hơn nền kinh tế mãi mãi |
| Sensitivity theo WACC ±1–2% | Hiển thị mức bất định của định giá |
| Kiểm tra chéo TV bằng exit multiple | Hai cách nên hội tụ |
| Mô hình chi tiết năm 1–3, đơn giản hóa năm 4–5 | Ngắn hạn chắc chắn hơn |
| Nêu rõ MỌI giả định | Minh bạch, dễ rà soát |
| Dùng giá trị thị trường (không phải sổ sách) cho tỷ trọng vốn trong WACC | Chi phí cơ hội phản ánh giá thị trường |

#### G.2. Valuation Pitfalls (những cái bẫy thường gặp)

| Pitfall | How to Avoid |
|----------|-------------|
| **Anchoring** vào ước tính ban đầu | Chạy DCF "mù" trước, sau đó mới đối chiếu thị trường |
| **Terminal value quá cao** | Thường >50%, nhưng cảnh giác nếu >85% |
| **Cherry-picking comps** | Đưa tất cả peers hợp lý, giải thích lý do loại trừ |
| **Bỏ qua chất lượng lợi nhuận** | Điều chỉnh khoản bất thường, chuẩn hóa |
| **Trộn EV và Equity** | EV multiple (EV/EBITDA) vs Equity multiple (P/E) |
| **Quên pha loãng** | Options, warrants, convertibles → diluted shares |
| **Snapshot fallacy** | Một multiple ≠ đáp số. Khoảng giá trị mới là đáp số |
| **Đếm trùng rủi ro** | Rủi ro đã cộng vào WACC thì đừng trừ vào dòng tiền thêm lần nữa |
| **Tăng trưởng không tốn vốn** | Kiểm tra bằng $g = RR \times ROIC$ |

#### G.3. Valuation cho các tình huống đặc biệt

| Situation | Recommended Approach |
|-----------|---------------------|
| **Startup chưa có doanh thu** | VC method, Option pricing, Revenue multiples chiết khấu mạnh |
| **Tổ chức tài chính (ngân hàng)** | P/B, Dividend Discount Model (DDM), Excess Return model |
| **Tài nguyên thiên nhiên** | NAV (giá trị tài sản ròng của trữ lượng), DCF theo giả định giá hàng hóa |
| **Bất động sản** | Cap Rate, NAV, DCF dòng tiền cho thuê |
| **Doanh nghiệp khó khăn tài chính** | Giá trị thanh lý, Sum-of-Parts, Adjusted PV |
| **Tech tăng trưởng cao** | EV/Revenue (chưa có lợi nhuận), DCF với giai đoạn tăng trưởng cao |

---

## III. CASE STUDIES THỰC TẾ

### 1. Case Study Thành công: Microsoft mua LinkedIn ($26.2B, 2016)

> **Lưu ý về số liệu**: các số liệu quốc tế dưới đây là số liệu công khai làm tròn và một phần là ước tính minh họa (đặc biệt EBITDA, net cash và giá trị hiện tại của LinkedIn); người học nên đối chiếu thêm báo cáo tài chính gốc nếu cần dùng cho mục đích chính thức.

#### Bối cảnh

Tháng 6/2016, Microsoft công bố mua LinkedIn với giá khoảng **196 USD/cổ phiếu**, tổng giá trị vốn chủ **$26.2B**, cao hơn khoảng **50%** so với giá đóng cửa trước ngày thông báo. Thời điểm đó LinkedIn là mạng xã hội nghề nghiệp với **433 triệu thành viên**, doanh thu 2015 khoảng **$3.0B** (tăng ~35%/năm), nhưng **lỗ theo chuẩn GAAP** do chi phí cổ phiếu thưởng (SBC) lớn. Câu hỏi của người định giá: *một công ty trả 8.7 lần doanh thu và hơn 50 lần EBITDA có "điên rồ" không?*

#### Bước 1: Tính các multiple Microsoft đã trả

| Chỉ tiêu | Phép tính | Kết quả |
|----------|----------|---------|
| Equity Value | 26.2 tỷ USD | 26.2 |
| EV (ước tính net cash ~2.5 tỷ) | 26.2 − 2.5 | ≈ 23.7 |
| Equity / Revenue | 26.2 / 3.0 | **8.7x** |
| EV / Revenue | 23.7 / 3.0 | **≈ 7.9x** |
| EV/EBITDA (EBITDA ≈ 0.45 tỷ, theo số cơ bản của tài liệu gốc) | 26.2 / 0.45 | **≈ 58x** (hoặc ≈ 53x nếu dùng EV) |
| EV/EBITDA (EBITDA điều chỉnh, loại SBC, ước tính ≈ 0.78 tỷ) | 26.2 / 0.78 | ≈ 34x (hoặc ≈ 30x nếu dùng EV) |

Con số 58x chỉ "đáng sợ" khi dùng EBITDA thấp sau SBC; khi dùng EBITDA điều chỉnh, con số giảm gần một nửa – minh họa việc **chọn định nghĩa EBITDA thay đổi cảm nhận về mức giá** (một pitfall ở mục G.2).

#### Bước 2: Đối chiếu bằng các phương pháp khác nhau (Football Field)

| Method | Implied Value | Ghi chú |
|--------|--------------|---------|
| DCF (WACC 9%, g 3%) | $28–35B | Giả định tăng trưởng cao kéo dài nhiều năm rồi mới giảm |
| EV/Revenue (peers: 6–8x) | $18–24B | Peer tăng trưởng thấp hơn, nên định giá thấp hơn |
| Precedent (social/platform deals) | $22–30B | Phù hợp với mức giá phải trả |
| **Mức giá thực tế** | **$26.2B** | Nằm trong vùng giữa của Football Field |

#### Bước 3: Phí kiểm soát có được "bù đắp" bởi synergy?

Phần phụ trội so với giá thị trường: giá thị trường trước thông báo ≈ 26.2 / 1.49 ≈ 17.6 tỷ USD; **phụ trội ≈ 26.2 − 17.6 = 8.6 tỷ USD**. Microsoft chỉ đáng trả khoản này nếu **PV của synergy ≥ 8.6 tỷ USD**.

| Nguồn synergy | Ước tính Microsoft | Thực tế |
|---------------|-------------------|---------|
| LinkedIn Sales Navigator + Dynamics CRM | $1B+ | ✅ $1.5B+ |
| Dữ liệu LinkedIn + sản phẩm Microsoft | $500M+ | ✅ Có |
| LinkedIn Learning (doanh nghiệp) | $300M+ | ✅ Có |
| Quảng cáo (Microsoft Audience Network) | $500M+ | ✅ Có |
| **Tổng doanh thu synergy (ước tính)** | **≈ $2.3B/năm** | |

Giả sử biên lợi nhuận hoạt động của doanh thu synergy 30%, thuế 20%, WACC 9%, tăng trưởng dài hạn 3%:

$$\text{Lợi nhuận sau thuế synergy} = 2.3 \times 30\% \times (1-20\%) = 0.552\ \text{tỷ USD/năm}$$

$$PV_{synergy} \approx \frac{0.552}{0.09 - 0.03} = 9.2\ \text{tỷ USD}$$

→ **PV synergy ≈ 9.2 tỷ USD > phụ trội 8.6 tỷ USD** → trả mức giá này là *vừa đủ hợp lý* (giá trị tạo ra cho cổ đông Microsoft chỉ khoảng +0.6 tỷ nếu synergy đạt đúng kỳ vọng) – nghĩa là **biên an toàn mỏng**, mọi thứ phụ thuộc vào việc thực thi.

#### Bước 4: Kiểm tra kết quả bằng "bài toán ngược" (hậu kiểm)

Theo số liệu công khai, doanh thu LinkedIn năm 2024 khoảng **$16B+** (từ $3B), tức tăng gấp ≈ 5.3 lần trong 8 năm → CAGR $(16/3)^{1/8} - 1 ≈ 23.3\%$/năm. Với giá trị thoát (exit) năm thứ 8, tỷ suất sinh lời hàng năm cho Microsoft ($26.2B bỏ ra) phụ thuộc EV/Revenue của LinkedIn năm 2024:

| EV/Revenue giả định (2024) | Giá trị | IRR 8 năm = $(Giá trị/26.2)^{1/8}-1$ |
|---------------------------|--------|--------------------------|
| 3x | $48B | 7.9% |
| 4x | $64B | 11.8% |
| 5x | $80B | **15.0%** |
| 6x | $96B | 17.6% |

Để đạt đúng tỷ suất sinh lời yêu cầu 9%/năm, giá trị LinkedIn năm 2024 phải đạt $26.2 × 1.09^8 ≈ **$52.2B**, tức EV/Revenue ≈ 3.3x – mức rất thấp so với tăng trưởng thực tế. Nếu giá trị hiện tại thật sự khoảng $80–100B như nhiều ước tính (chưa kiểm chứng) thì thương vụ tạo ra giá trị đáng kể.

#### Kết luận và Bài học

1. **Trả tiền cho tăng trưởng**: 58x EBITDA trông phi lý, nhưng nếu doanh thu tăng 5 lần trong 8 năm thì hợp lý. *Multiple phải được đọc cùng với tăng trưởng.*
2. **Giá trị chiến lược > giá trị tài chính độc lập**: LinkedIn nằm trong hệ sinh thái Microsoft (Teams, Outlook, Office, Dynamics) có giá trị cao hơn đứng một mình.
3. **Hiệu ứng mạng lưới (network effects)**: thêm thành viên → giá trị tăng → thu hút thêm thành viên.
4. **Kiểm tra bằng "PV synergy ≥ phụ trội"**: quy tắc đơn giản nhưng quyết định – không tính được thì đừng trả phụ trội.
5. **Vốn kiên nhẫn**: Microsoft không đòi hỏi LinkedIn có lãi ngay.

---

### 2. Case Study Thất bại: HP mua Autonomy ($11.1B, 2011–2012) – Thảm họa định giá

> **Lưu ý về số liệu**: số liệu "thực tế" của Autonomy dưới đây là những con số HP đưa ra sau khi phát hiện vấn đề (và một phần vẫn là đối tượng tranh tụng pháp lý); dùng để minh họa tư duy định giá, không nhằm kết luận pháp lý.

#### Bối cảnh

- Tháng 8/2011: HP công bố mua công ty phần mềm Anh Autonomy với giá **$11.1B** (≈ $42.11/cổ phiếu, phụ trội **~64%** so với giá thị trường).
- Tháng 11/2012 (~1 năm sau): HP ghi giảm giá trị **$8.8B** (≈ **79%** giá mua), công khai cáo buộc Autonomy phóng đại doanh thu qua thủ thuật kế toán (HP nêu hơn $5B trong khoản này liên quan đến "bất thường kế toán").
- Bối cảnh chiến lược: CEO Léo Apotheker muốn chuyển HP từ phần cứng sang phần mềm; thương vụ được thông qua chỉ trong vài tuần.

#### Bước 1: Tính các multiple theo "số liệu công bố" và "số liệu thực"

| Metric | Autonomy (công bố) | Theo HP (thực) |
|--------|--------------------|----------------|
| Doanh thu | $1.0B | ~$0.7B (loại doanh thu bán lại phần cứng) |
| Biên EBITDA | ≥ 40% | ~25% (chỉ phần mềm) |
| EBITDA | ≥ $0.40B | ~$0.175B |
| Tăng trưởng | 15–20% | 5–10% (hữu cơ) |

Tính các multiple:

$$\frac{EV}{Revenue}\Big|_{công\,bố} = \frac{11.1}{1.0} = 11.1x \qquad \frac{EV}{Revenue}\Big|_{thực} = \frac{11.1}{0.7} \approx 15.9x$$

$$\frac{EV}{EBITDA}\Big|_{công\,bố} = \frac{11.1}{0.40} \approx 27.8x \qquad \frac{EV}{EBITDA}\Big|_{thực} = \frac{11.1}{0.7 \times 25\%} = \frac{11.1}{0.175} \approx 63x$$

(Lưu ý: tài liệu cũ ghi "~25x" và "40x+"; phép tính từ giả định trên cho 27.8x và 63x, vì thế các con số được làm lại cho tự nhất quán.)

#### Bước 2: Định giá lại "theo lẽ thường" để thấy mức trả quá cao

Phần mềm doanh nghiệp tăng trưởng 5–10% thời điểm đó thường giao dịch ở khoảng 4–6x doanh thu (giả định minh họa). Áp lên doanh thu thực $0.7B:

| EV/Revenue giả định | Giá trị | Trả thừa so với $11.1B |
|---------------------|--------|-----------------------|
| 4x | 0.7 × 4 = $2.8B | 11.1 − 2.8 = **$8.3B** |
| 5x | $3.5B | $7.6B |
| 6x | 0.7 × 6 = $4.2B | **$6.9B** |

→ Mức trả thừa $6.9–8.3B **gần trùng với khoản ghi giảm $8.8B** (79% giá mua) – tức phần lớn "giá trị" HP mua thực chất chưa từng tồn tại. Và ngay cả khi *không có gian lận*, 11x doanh thu cho tăng trưởng 10–15% với phụ trội 64% vẫn là mức giá cao.

#### Bước 3: Phân tích nguyên nhân

| Factor | Detail |
|--------|--------|
| **Phóng đại doanh thu** | Autonomy bán phần cứng với giá lỗ để tăng doanh thu (ghi nhận như "phần mềm") |
| **Channel stuffing** | Đẩy doanh thu sớm cho các đại lý |
| **Thao túng kế toán** | Vốn hóa chi phí, kéo dài điều khoản thanh toán |
| **Thất bại thẩm định (DD)** | Đội DD của HP bỏ sót/bỏ qua dấu hiệu cảnh báo |
| **Trả quá giá** | Ngay cả không gian lận: 11x doanh thu cho tăng trưởng 10–15% vẫn quá đắt |
| **Không có logic synergy** | HP = phần cứng; Autonomy = tìm kiếm doanh nghiệp – synergy ở đâu? |
| **Áp lực CEO** | Muốn "chuyển đổi sang phần mềm" bằng thương vụ lớn |
| **HĐQT đóng dấu** | Thương vụ thông qua vài tuần thay vì vài tháng |

#### Bước 4: Các dấu hiệu cảnh báo (Red Flags) đã bị bỏ qua

```
1. MARGIN TOO GOOD: Autonomy báo cáo biên EBITDA 40%+
   → Phần mềm doanh nghiệp điển hình: 20-30%
   → Lẽ ra phải kích hoạt DD chuyên sâu

2. KHÁCH HÀNG TẬP TRUNG: ít hợp đồng lớn = doanh thu "lumpy", rủi ro

3. DOANH THU PHẦN CỨNG: Autonomy mua đi bán lại phần cứng để tăng doanh thu
   → Thao túng rõ ràng nếu CHỊU nhìn

4. CHUẨN KẾ TOÁN KHÁC NHAU: Chuẩn Anh (IFRS) vs US GAAP
   → Phải đối chiếu (reconcile) cẩn thận

5. KHÔNG PHÙ HỢP CHIẾN LƯỢC: HP (máy in/PC) cần gì ở tìm kiếm doanh nghiệp?
   → Luận điểm gượng ép

6. PHỤ TRỘI GIÁ: 64% so với giá thị trường
   → Synergy nào biện minh cho 64%?? (Đáp án: KHÔNG có synergy thực)
```

#### Tác động tài chính

- Ghi giảm tổng cộng: **$8.8B** (goodwill impairment, ≈ 79% giá mua)
- Chi phí cơ hội: nếu $11.1B được đầu tư vào chỉ số S&P 500 thay vào đó, giá trị sẽ cao hơn nhiều (ước tính không kiểm chứng: >$25B hiện nay) → giá trị bị phá hủy rất lớn.

#### Bài học Valuation

1. **Kiểm chứng chất lượng doanh thu** – không phải mọi $1 doanh thu đều như nhau.
2. **Multiple thận trọng** – nếu không biện minh được phụ trội bằng synergy CỤ THỂ, đừng trả.
3. **DD độc lập** – không bao giờ dựa hoàn toàn vào số liệu của bên bán.
4. **Phù hợp chiến lược trước** – "muốn vào phần mềm" ≠ luận điểm M&A tốt.
5. **Kỷ luật rút lui (walk away)** – bỏ lỡ thương vụ tốt hơn trả quá giá.
6. **Đối chiếu chéo nhiều phương pháp**: chỉ cần chạy Comps với 5x doanh thu thực là thấy ngay vấn đề.

---

### 3. Case Study SME: Định giá Công ty TNHH Bao Bì Xanh Việt (Bình Dương) khi chủ muốn bán 100% cho nhà đầu tư chiến lược

> Công ty và số liệu dưới đây hoàn toàn **giả định** để minh họa; đơn vị: **triệu VND** trừ khi nêu khác.

#### Bối cảnh doanh nghiệp

Ông Tâm là chủ sở hữu 100% Công ty TNHH Bao Bì Xanh Việt – sản xuất thùng carton và bao bì giấy cho các nhà máy thực phẩm, may mặc tại Bình Dương. Ông 58 tuổi, muốn bán công ty cho một tập đoàn bao bì lớn hơn. Tập đoàn đưa ra mức chào **48 tỷ VND** cho vốn chủ. Ông nhờ tư vấn: *giá đó có công bằng không, và nên đòi bao nhiêu?*

**Số liệu năm hiện tại (Y0)**:

| Chỉ tiêu | Giá trị |
|----------|--------|
| Doanh thu | 80,000 |
| EBIT (biên 9.5%) | 7,600 |
| D&A (3% doanh thu) | 2,400 |
| **EBITDA** | **10,000** |
| Nợ vay ngân hàng | 20,000 (lãi suất 9.5%/năm) |
| Tiền mặt | 5,000 |
| **Nợ ròng** | **15,000** |
| Lợi nhuận sau thuế = (7,600 − 20,000 × 9.5%) × (1 − 20%) = (7,600 − 1,900) × 0.8 | 4,560 |
| Số cổ phần | 1,000,000 |

Giả định kinh doanh 5 năm tới (có căn cứ từ đơn hàng đã ký và kế hoạch mở rộng nhà xưởng): tăng trưởng doanh thu 12% / 10% / 8% / 7% / 6%; biên EBIT 10% → 10.5% → 11% → 11% → 11%; CAPEX 4.5% doanh thu (Y1–2, đầu tư máy mới) rồi 4.0% (Y3–5); D&A 3%; vốn lưu động ròng = 18% doanh thu; thuế TNDN 20%.

#### Bước 1: Chuẩn hóa EBITDA (Normalization)

Với SME, trước khi nhân multiple phải "làm sạch" EBITDA: cộng lại chi phí cá nhân của chủ, trừ phần lương thị trường mà chủ lẽ ra phải nhận. Trong trường hợp này, ông Tâm rà soát cùng kiểm toán: chi phí cá nhân ghi nhầm vào công ty (xe hơi, du lịch gia đình) đã được loại ở số liệu trên; lương ông tự nhận phù hợp mức thị trường cho giám đốc; nên EBITDA chuẩn hóa = **10,000** (không điều chỉnh thêm). *(Nếu có điều chỉnh, phải ghi rõ từng khoản trong hồ sơ để bên mua chấp nhận.)*

#### Bước 2: Xây dựng WACC cho SME (CAPM + Build-up)

**Tại sao SME cần thêm "size premium"?** CAPM gốc dựa trên công ty lớn niêm yết. SME nhỏ, ít thông tin, phụ thuộc người chủ, khó thoái vốn → nhà đầu tư đòi lợi suất cao hơn. Ta cộng thêm 3% (phần bù quy mô/ rủi ro đặc thù) vào chi phí vốn chủ – giả định tham khảo, cần điều chỉnh theo từng công ty.

Tham số: $r_f$ = 3.0% (lãi suất trái phiếu chính phủ VN 10 năm, làm tròn), $ERP$ = 8.0% (phần bù rủi ro thị trường của thị trường mới nổi như VN), $\beta_U$ = 0.85 (beta ngành bao bì, giả định), tỷ trọng mục tiêu nợ 30% / vốn chủ 70%, $K_d$ = 10% (lãi vay SME), $T$ = 20%.

$$\beta_L = \beta_U \times [1 + (1-T) \times D/E] = 0.85 \times [1 + 0.8 \times (0.30/0.70)] = 0.85 \times 1.3429 = 1.1414$$

$$K_e = r_f + \beta_L \times ERP + Size = 3\% + 1.1414 \times 8\% + 3\% = 3\% + 9.13\% + 3\% = 15.13\%$$

$$WACC = 30\% \times 10\% \times (1-20\%) + 70\% \times 15.13\% = 2.40\% + 10.59\% = \mathbf{12.99\%}$$

#### Bước 3: Dự phóng FCFF 5 năm (triệu VND)

Ví dụ phép tính Y1: Doanh thu = 80,000 × 1.12 = 89,600; EBIT = 89,600 × 10% = 8,960; NOPAT = 8,960 × 0.8 = 7,168; D&A = 3% × 89,600 = 2,688; CAPEX = 4.5% × 89,600 = 4,032; ΔNWC = 18% × (89,600 − 80,000) = 1,728; FCFF = 7,168 + 2,688 − 4,032 − 1,728 = **4,096**.

| Năm | Doanh thu | EBIT | NOPAT | D&A | CAPEX | ΔNWC | FCFF | Hệ số CK (12.99%) | PV(FCFF) |
|-----|-----------|------|-------|-----|-------|------|------|-------------------|----------|
| 1 | 89,600 | 8,960 | 7,168 | 2,688 | 4,032 | 1,728 | 4,096 | 0.8850 | 3,625 |
| 2 | 98,560 | 10,349 | 8,279 | 2,957 | 4,435 | 1,613 | 5,188 | 0.7833 | 4,063 |
| 3 | 106,445 | 11,709 | 9,367 | 3,193 | 4,258 | 1,419 | 6,883 | 0.6932 | 4,772 |
| 4 | 113,896 | 12,529 | 10,023 | 3,417 | 4,556 | 1,341 | 7,543 | 0.6135 | 4,627 |
| 5 | 120,730 | 13,280 | 10,624 | 3,622 | 4,829 | 1,230 | 8,187 | 0.5430 | 4,445 |
| | | | | | | | **Tổng PV** | | **21,532** |

#### Bước 4: Terminal Value với FCFF chuẩn hóa (năm 6)

Tăng trưởng dài hạn $g$ = 4% (thấp hơn tăng trưởng GDP danh nghĩa của Việt Nam). Chuẩn hóa năm 6: Doanh thu = 120,730 × 1.04 = 125,559; NOPAT = 125,559 × 11% × 0.8 = 11,049; D&A = 3% × 125,559 = 3,767; CAPEX = 3.8% × 125,559 = 4,771 (cao hơn D&A để có tăng trưởng); ΔNWC = 18% × (125,559 − 120,730) = 869.

$$FCFF_6 = 11{,}049 + 3{,}767 - 4{,}771 - 869 = 9{,}176$$

$$TV = \frac{9{,}176}{0.12992 - 0.04} = \frac{9{,}176}{0.08992} \approx 102{,}040 \qquad PV(TV) = 102{,}040 \times 0.5430 \approx 55{,}403$$

**Kiểm tra tính hợp lý** bằng $g = RR \times ROIC$: tỷ lệ tái đầu tư $RR = (4{,}771 - 3{,}767 + 869)/11{,}049 = 17.0\%$ → ROIC ngụ ý $= 4\%/17.0\% \approx 23.6\%$ – cao nhưng có thể chấp nhận cho doanh nghiệp đã có nền tảng khách hàng; người định giá thận trọng sẽ thử thêm kịch bản ROIC thấp hơn (biên thấp hơn hoặc capex cao hơn).

#### Bước 5: Từ Enterprise Value sang Equity Value

| Thành phần | Giá trị (triệu VND) |
|-----------|--------------------|
| Tổng PV(FCFF Y1–5) | 21,532 |
| PV(Terminal Value) | 55,403 |
| **Enterprise Value (DCF)** | **76,935** |
| − Nợ vay | (20,000) |
| + Tiền mặt | 5,000 |
| **Equity Value (DCF)** | **61,935** |

- TV chiếm $55{,}403/76{,}935 = 72.0\%$ EV – nằm trong khoảng điển hình 60–80%.
- EV ngụ ý trên EBITDA hiện tại: $76{,}935/10{,}000 = 7.7x$.

#### Bước 6: Bảng độ nhạy (Equity Value, triệu VND)

| | g = 3% | g = 4% | g = 5% |
|-|--------|--------|--------|
| **WACC = 11.99%** | 65,819 | 72,305 | 80,645 |
| **WACC = 12.99%** | 57,047 | **61,935** | 68,048 |
| **WACC = 13.99%** | 49,893 | 53,663 | 58,271 |

→ Khoảng DCF (WACC ±1%, g = 4%): **53,663 – 72,305**. Mức chào 48,000 của bên mua thấp hơn cả đáy bảng độ nhạy.

#### Bước 7: Comps (công ty niêm yết ngành bao bì, số liệu giả định)

| Peer | EV/EBITDA |
|------|-----------|
| Peer A | 7.2x |
| Peer B | 8.1x |
| Peer C | 6.4x |
| Peer D | 9.0x |
| Peer E | 5.9x |
| **Trung vị** | **7.2x** |

Vì Bao Bì Xanh Việt nhỏ hơn, không niêm yết, ta áp **chiết khấu 15%** (DLOM + quy mô) cho multiple: $7.2 \times 0.85 = 6.12x$.

$$EV_{Comps} = 6.12 \times 10{,}000 = 61{,}200 \qquad Equity = 61{,}200 - 15{,}000 = 46{,}200$$

Đối chiếu P/E: trung vị P/E peer 11.0x × Lợi nhuận sau thuế 4,560 = 50,160; sau chiết khấu 15% = 42,636. Khoảng Comps (EV/EBITDA đã chiết khấu, từ peer thấp nhất 5.9x đến cao nhất 9.0x): Equity **35,150 – 61,500**.

#### Bước 8: Precedent Transactions (thương vụ M&A bao bì quy mô vừa/nhỏ, giả định)

| Thương vụ | EV/EBITDA |
|----------|-----------|
| Deal 1 | 6.0x |
| Deal 2 | 6.8x |
| Deal 3 | 7.5x |
| Deal 4 | 8.2x |
| **Trung vị** | **7.15x** |

$$EV_{Precedent} = 7.15 \times 10{,}000 = 71{,}500 \qquad Equity = 71{,}500 - 15{,}000 = 56{,}500$$

Khoảng: **45,000 – 67,000** (từ 6.0x đến 8.2x). Không cần chiết khấu thêm vì thương vụ cũng là công ty tư nhân và đã có phụ trội kiểm soát.

#### Bước 9: Tổng hợp – Football Field và giá trị khuyến nghị

| Phương pháp | Khoảng Equity Value | Điểm giữa | Trọng số | Lý do trọng số |
|-------------|--------------------|-----------|---------|-----------------|
| DCF | 53,663 – 72,305 | 61,935 | 50% | Dựa trên kế hoạch cụ thể, đơn hàng đã ký |
| Trading Comps (đã chiết khấu) | 35,150 – 61,500 | 46,200 | 25% | Peer lớn hơn, chỉ mang tính tham chiếu |
| Precedent | 45,000 – 67,000 | 56,500 | 25% | Sát thực tế M&A, nhưng ít dữ liệu |

$$Equity_{khuyến\,nghị} = 50\% \times 61{,}935 + 25\% \times 46{,}200 + 25\% \times 56{,}500 = 30{,}968 + 11{,}550 + 14{,}125 \approx \mathbf{56{,}643}$$

→ EV tương ứng = 56,643 + 15,000 = 71,643 (≈ **7.2x EBITDA**); giá trị mỗi cổ phần = 56,643 triệu / 1 triệu cổ phần ≈ **56,643 VND/cổ phần**.

```
Equity Value (triệu VND)   35,000     45,000     55,000     65,000     75,000
DCF               (WACC±1%)            ████████████████████████████  (53.7k - 72.3k)
Trading Comps (đã CK 15%)   ██████████████████████████████            (35.2k - 61.5k)
Precedent Txns                     ███████████████████████████        (45.0k - 67.0k)
                                          ▲ khuyến nghị ≈ 56.6k
Mức chào của bên mua = 48.0k  ▲ (thấp hơn giá trị khuyến nghị ~15%)
```

#### Bước 10: Diễn giải kinh doanh và khuyến nghị

- Mức chào **48,000** thấp hơn giá trị khuyến nghị 56,643 khoảng **15.3%**; chỉ cao hơn điểm giữa của Comps đã chiết khấu (46,200) khoảng 3.9% – nghĩa là bên mua đang dựa chủ yếu vào Comps (phương pháp ít có lợi nhất cho bên bán) và chưa tính đến kế hoạch tăng trưởng.
- **Chiến lược đàm phán đề xuất**: giá chào ban đầu ~66–72 tỷ (vùng cao của DCF + Precedent, kèm lập luận về đơn hàng đã ký và synergy cho người mua); mục tiêu thực tế ~57–62 tỷ; mức "walk away" ~**52 tỷ** (gần đáy khoảng DCF 53.7 tỷ trừ một phần thương lượng).
- **Rủi ro cần kiểm soát**: ông Tâm là "key person" – bên mua có thể đòi giữ ông làm tư vấn 1–2 năm, thanh toán một phần theo earn-out (trả sau theo kết quả) – có thể chấp nhận để đổi lấy giá cao hơn.
- **Bài học SME**: (1) Luôn chuẩn hóa EBITDA trước; (2) Dùng ≥ 2 phương pháp; (3) WACC phải có phần bù quy mô; (4) Bảng độ nhạy là công cụ đàm phán – đưa bên mua thấy giá thấp hơn mọi kịch bản hợp lý.

---

## IV. ỨNG DỤNG CHO SME

### 1. Đặc thù định giá SME so với công ty niêm yết

| Đặc điểm | Công ty niêm yết | SME Việt Nam | Hệ quả khi định giá |
|----------|-----------------|--------------|---------------------|
| Dữ liệu | Báo cáo công khai, kiểm toán | Sổ sách chưa chuẩn, trộn chi tiêu cá nhân và công ty | Phải **chuẩn hóa** lợi nhuận (normalization) |
| Giá cổ phiếu | Có giá thị trường hằng ngày | Không có | Chỉ dùng DCF và so sánh gián tiếp |
| Thanh khoản | Cao | Rất thấp | Chiết khấu DLOM 15–30% |
| Phụ thuộc chủ | Thấp | Rất cao (key-person risk) | Chiết khấu hoặc cộng vào $K_e$ |
| Rủi ro | Đa dạng hóa | Tập trung vào 1–3 khách hàng/nhà cung cấp | Phần bù rủi ro đặc thù 2–5% |
| Comps | Peer niêm yết | Ít peer; peer lớn hơn nhiều | Chiết khấu quy mô |
| Dự phóng | Có consensus analyst | Dựa vào kế hoạch của chủ | Kiểm tra bằng đơn hàng, hợp đồng, lịch sử |

### 2. Chuẩn hóa lợi nhuận (Normalization) – bước quan trọng nhất

**Tại sao?** Multiple (và DCF) chỉ có ý nghĩa nếu lợi nhuận phản ánh *khả năng sinh lời bền vững dưới quyền sở hữu mới*. Hai loại điều chỉnh chính:

| Loại điều chỉnh | Ví dụ | Hướng |
|----------------|-------|------|
| Chi phí cá nhân của chủ chạy qua công ty | Xe riêng, du lịch gia đình, điện thoại | Cộng lại EBITDA |
| Lương chủ thấp hơn thị trường | Chủ chỉ nhận 10 triệu/tháng trong khi thuê giám đốc ~40 triệu | Trừ EBITDA |
| Khoản thu/chi bất thường | Thanh lý tài sản, phạt một lần, hợp đồng đột biến | Loại khỏi cả hai chiều |
| Giao dịch bên liên quan giá không thị trường | Thuê mặt bằng của chủ giá thấp/cao bất thường | Điều chỉnh về giá thị trường |

Một số người làm SME dùng khái niệm **SDE (Seller's Discretionary Earnings)** = EBITDA + lương chủ + chi phí cá nhân – áp dụng cho doanh nghiệp rất nhỏ nơi chủ làm việc toàn thời gian.

### 3. Quy tắc ngón tay cái (rules of thumb) và cách dùng thận trọng

Một số ngành SME giao dịch theo multiple "thị trường" phổ biến (tham khảo, **không có nguồn chính thức**, thay đổi theo từng thời điểm và từng thương vụ):

| Loại SME | Multiple thường được nhắc đến | Ghi chú |
|----------|------------------------------|---------|
| Quán ăn/cà phê đơn lẻ | 1.5–3x SDE | Phụ thuộc vị trí, hợp đồng thuê |
| Chuỗi F&B nhỏ (3–10 điểm) | 3–5x EBITDA | Hệ thống vận hành chuẩn hóa tăng multiple |
| Sản xuất nhỏ, ổn định | 4–7x EBITDA | Tài sản và khách hàng ổn định |
| Phân phối/Thương mại | 3–5x EBITDA | Biên thấp, vốn lưu động lớn |
| SaaS/Dịch vụ phần mềm nhỏ | 2–5x doanh thu (ARR) | Tùy tốc độ tăng trưởng, churn |

**Cách dùng đúng**: chỉ dùng làm *kiểm tra chéo* cho DCF, không thay thế DCF.

### 4. Định giá khi gọi vốn (Startup/SME): pre-money, post-money và pha loãng

**Tại sao quan trọng?** Chủ SME khi gọi vốn từ quỹ/angel cần hiểu: định giá cao hơn → nhường ít cổ phần hơn.

$$Post\text{-}money = Pre\text{-}money + Vốn\,đầu\,tư \qquad \%\,nhà\,đầu\,tư\,nhận = \frac{Vốn\,đầu\,tư}{Post\text{-}money}$$

Ví dụ: pre-money = 40 tỷ, quỹ đầu tư 10 tỷ → post-money = 50 tỷ; quỹ nhận 10/50 = **20%**; chủ cũ còn 80%. (Phép tính kiểm tra: 80% × 50 = 40 tỷ = pre-money ✓.)

**VC Method** (cho startup chưa có lợi nhuận): ước tính giá trị thoát (exit) năm thứ 5, chia cho tỷ suất sinh lời mục tiêu (ví dụ 10x–20x với startup giai đoạn sớm) để ra post-money hiện tại – không tin tuyệt đối, chủ yếu để đàm phán.

### 5. Sai lầm thường gặp khi chủ SME tự định giá

| Sai lầm | Hậu quả | Cách tránh |
|---------|---------|------------|
| Định giá theo "giá trị sổ sách" hoặc "tôi đã bỏ bao nhiêu vốn" | Sai bản chất (giá trị = tương lai, không phải quá khứ) | Dùng DCF/multiple |
| Lấy multiple của công ty niêm yết lớn rồi nhân thẳng | Quá cao (không chiết khấu thanh khoản, quy mô) | Chiết khấu 15–30% |
| Lạc quan dự phóng (hockey stick) | Giá trị ảo, mất uy tín khi đàm phán | Dự phóng bám đơn hàng, lịch sử, benchmark |
| Quên trừ nợ vay và các nghĩa vụ ngoài bảng | Định giá vốn chủ quá cao | Lập bảng Equity Bridge đầy đủ |
| Không chuẩn hóa lợi nhuận | Sai số lớn | Làm theo mục IV.2 |
| Chỉ dùng một phương pháp | Không biết mình đúng hay sai | Tối thiểu 2 phương pháp + Football Field |

### 6. Checklist đàm phán khi bán/gọi vốn dựa trên định giá

1. Chuẩn bị 3 kịch bản (thận trọng/cơ sở/lạc quan) và bảng độ nhạy.
2. Chuẩn bị **hồ sơ dữ liệu** (data room): báo cáo tài chính 3 năm, hợp đồng lớn, danh mục khách hàng, sổ phụ ngân hàng.
3. Xác định giá chào ban đầu (vùng cao) – giá mục tiêu – giá rút lui (walk away).
4. Phân biệt rõ **EV** và **Equity** khi thương lượng (bên mua hay nói EV, bạn nhận Equity).
5. Làm rõ điều khoản: earn-out, đảm bảo, cam kết không cạnh tranh, giữ lại cổ phần của chủ.

---

## V. TOOLS & TEMPLATES

### 1. Công cụ và nguồn dữ liệu

| Công cụ/nguồn | Công dụng | Chi phí tham khảo |
|---------------|-----------|-------------------|
| **Excel / Google Sheets** | Xây dựng mô hình DCF, bảng độ nhạy (Data Table) | Có sẵn / miễn phí |
| **Damodaran Online (NYU Stern)** – bảng dữ liệu hằng năm | Beta theo ngành, ERP, multiples theo ngành, cost of capital | Miễn phí |
| **Báo cáo tài chính công bố (HOSE/HNX, CafeF, Vietstock, FiinGroup)** | Dữ liệu peer niêm yết tại VN | Miễn phí – gói trả phí tùy nhà cung cấp |
| **Bloomberg / Capital IQ / Refinitiv** | Dữ liệu Comps & Precedent chuyên nghiệp | Rất đắt (hàng nghìn USD/năm) – thường dùng ở ngân hàng đầu tư |
| **Python (pandas)** | Tự động hóa, mô phỏng Monte Carlo | Miễn phí |
| **Hỏi ý kiến công ty tư vấn/kiểm toán** | Fairness opinion, định giá chính thức | Tùy quy mô thương vụ |

### 2. Cấu trúc file Excel DCF tối thiểu cho SME

```
Sheet 1: Inputs     — giả định (tăng trưởng, biên, capex, NWC, thuế, WACC, g)
Sheet 2: Historical — 3 năm quá khứ đã chuẩn hóa (Normalized EBITDA)
Sheet 3: FCFF       — dự phóng 5 năm: Revenue → EBIT → NOPAT → FCFF
Sheet 4: WACC       — CAPM build-up (rf, ERP, beta relevered, size premium)
Sheet 5: DCF        — chiết khấu, TV, EV → Equity bridge
Sheet 6: Comps      — bảng peer, median, áp dụng chiết khấu
Sheet 7: Sensitivity— Data Table WACC × g
Sheet 8: Football   — tổng hợp, biểu đồ thanh
```

**Công thức Excel gợi ý**:

| Mục đích | Công thức Excel |
|----------|----------------|
| Hệ số chiết khấu | `=1/(1+WACC)^năm` |
| NPV dòng tiền | `=NPV(WACC, FCFF_Y1:FCFF_Y5)` |
| Terminal Value Gordon | `=FCFF_Y5*(1+g)/(WACC-g)` |
| Median multiple | `=MEDIAN(range)` |
| Bảng độ nhạy | `Data → What-If Analysis → Data Table` |
| Beta relevered | `=BetaU*(1+(1-T)*D/E)` |

### 3. Template Football Field (copy-paste)

| Phương pháp | Low | Mid | High | Trọng số |
|-------------|-----|-----|------|---------|
| DCF | | | | 40–60% |
| Trading Comps | | | | 20–30% |
| Precedent | | | | 20–30% |
| **Giá trị khuyến nghị** | | `=SUMPRODUCT(Mid, TrọngSố)` | | 100% |

---

## VI. BÀI TẬP THỰC HÀNH

### Bài 1: Tính FCFF
Một công ty có EBIT = 500 tỷ, thuế 20%, D&A = 100 tỷ, CAPEX = 150 tỷ, ΔNWC = 30 tỷ. Tính FCFF.

*Gợi ý*: NOPAT = 500 × 0.8 = 400; FCFF = 400 + 100 − 150 − 30 = **320 tỷ**.

### Bài 2: Terminal Value
Với FCFF năm 5 = 320 tỷ, WACC = 11%, $g$ = 3%: tính TV và PV(TV) (chiết khấu 5 năm).

*Gợi ý*: TV = 320 × 1.03 / 0.08 = **4,120 tỷ**; PV(TV) = 4,120 / 1.11⁵ ≈ **2,445 tỷ**.

### Bài 3: Equity Bridge
EV = 3,000 tỷ; nợ vay = 800; tiền mặt = 200; cổ đông thiểu số = 100; số cổ phiếu pha loãng 50 triệu. Tính giá trị mỗi cổ phiếu.

*Gợi ý*: Equity = 3,000 − 800 + 200 − 100 = 2,300 tỷ; giá = 2,300 tỷ / 50 triệu = **46,000 VND/cổ phiếu**.

### Bài 4: Comps có chiết khấu
Công ty tư nhân có EBITDA = 250 tỷ; trung vị EV/EBITDA của peer niêm yết = 8x; áp dụng chiết khấu 20% cho multiple; nợ = 400, tiền = 100. Tính Equity Value.

*Gợi ý*: multiple điều chỉnh = 6.4x; EV = 1,600; Equity = 1,600 − 400 + 100 = **1,300 tỷ**.

### Bài 5: Độ nhạy của TV
Giải thích bằng lời tại sao khi WACC giảm từ 11% xuống 10% (g = 3%), TV tăng khoảng 14% (kiểm tra bằng phép tính: mẫu số từ 8% còn 7%).

*Gợi ý*: 1/0.08 = 12.5 và 1/0.07 = 14.29 → tăng 14.3%.

### Bài 6: Mini case SME – chuỗi trà sữa 3 cửa hàng
Chuỗi trà sữa "Mây Xanh" (3 cửa hàng): EBITDA báo cáo = 1,200 triệu; chủ không nhận lương (lương thị trường cho quản lý ~ 240 triệu/năm); nợ vay = 600 triệu; tiền = 200 triệu. Multiple chuỗi F&B nhỏ tham khảo = 3.5x EBITDA.
1. Tính EBITDA chuẩn hóa.
2. Tính EV và Equity Value.
3. Nếu bên mua đề nghị 2,500 triệu, bạn có nên chấp nhận không? Giải thích.

*Gợi ý*: (1) 1,200 − 240 = **960**; (2) EV = 960 × 3.5 = **3,360**; Equity = 3,360 − 600 + 200 = **2,960 triệu**; (3) 2,500 thấp hơn 2,960 khoảng 15.5% – chưa nên chấp nhận ngay, cần thêm DCF/kịch bản để thương lượng.

### Bài 7: Phân tích tình huống
Một công ty có TV chiếm 90% EV trong mô hình DCF. Nêu ít nhất 3 hành động bạn sẽ làm để kiểm tra độ tin cậy của định giá.

*Gợi ý*: (1) Kiểm tra chéo bằng exit multiple; (2) Bảng độ nhạy WACC–g; (3) Kéo dài giai đoạn dự phóng (7–10 năm) hoặc dùng mô hình 3 giai đoạn; (4) Kiểm tra $g = RR \times ROIC$; (5) Đối chiếu Comps.

---

## PHỤ LỤC: CHECKLIST CORPORATE VALUATION TỔNG HỢP

### 1. Checklist rà soát trước khi áp dụng

```
CHUẨN BỊ & CHUẨN HÓA:
□ Xác định mục đích định giá (M&A, gọi vốn, thuế, nội bộ...)?
□ Lợi nhuận quá khứ đã chuẩn hóa (loại chi phí cá nhân, khoản bất thường)?
□ Số liệu đã đối chiếu với thuế, ngân hàng, kiểm toán (nếu có)?

DCF:
□ Revenue projection reasonable (vs historical, market)?
□ Margin assumptions sourced (vs peers)?
□ CAPEX and D&A consistent with growth?
□ Working capital changes included?
□ WACC correctly calculated (market values, CAPM)?
□ Terminal value method chosen and justified?
□ Terminal growth ≤ economy growth?
□ TV as % of total reasonable (50-80%)?
□ Kiểm tra chéo g = RR × ROIC?
□ Sensitivity analysis (WACC, g, margins)?

COMPS:
□ Peer set appropriate (similar size, growth, industry)?
□ Multiples calculated correctly (EV vs Equity)?
□ Medians AND ranges reported?
□ Outliers explained/excluded?
□ Forward vs trailing multiples considered?
□ Adjustments for differences in growth/risk?
□ Chiết khấu quy mô/thanh khoản (DLOM) cho công ty tư nhân?

PRECEDENT TRANSACTIONS:
□ Relevant (same industry, recent)?
□ Control premium included naturally?
□ Market conditions at time of deal considered?
□ Strategic vs financial buyers distinguished?
□ Synergy-driven premium separated?

EQUITY BRIDGE:
□ Đã trừ nợ vay, ưu đãi, cổ đông thiểu số, nợ thuê tài chính?
□ Đã cộng tiền thừa và tài sản phi hoạt động?
□ Dùng số cổ phiếu pha loãng?

SYNTHESIS:
□ "Football field" with all methods plotted?
□ Range makes sense (methods converge)?
□ Key value drivers identified?
□ Upside and downside cases?
□ Final recommendation supported by analysis?
□ Có giá chào / giá mục tiêu / giá rút lui rõ ràng?
```

### 2. Bảng công thức tổng hợp

| Formula | Use |
|---------|-----|
| $EV = \sum \frac{FCFF_t}{(1+WACC)^t} + \frac{TV}{(1+WACC)^n}$ | DCF valuation |
| $FCFF = EBIT(1-T) + D\&A - CAPEX - \Delta NWC$ | Free Cash Flow to Firm |
| $TV = \frac{FCFF_{n+1}}{WACC - g}$ | Terminal Value (Gordon) |
| $TV = EBITDA_n \times Exit\,Multiple$ | Terminal Value (Multiple) |
| $g = RR \times ROIC$, $RR = \frac{CAPEX - D\&A + \Delta NWC}{NOPAT}$ | Kiểm tra tăng trưởng bền vững |
| $Equity = EV - Net\,Debt - Minority - Preferred + Non\text{-}op\,assets$ | Bridge to equity |
| $\beta_L = \beta_U \times [1 + (1-T) \times D/E]$ | Relever beta |
| $K_e = r_f + \beta_L \times ERP + Size\,Premium$ | Chi phí vốn chủ (CAPM + build-up) |
| $WACC = w_d K_d (1-T) + w_e K_e$ | Tỷ lệ chiết khấu |
| $EV/EBITDA_{implied} = EV / EBITDA$ | Multiple calculation |
| $P/E_{implied} = Equity / Net\,Income$ | Equity multiple |
| $Control\,Premium = \frac{Offer - Market}{Market}$ | Phụ trội kiểm soát |
| $Value/Share = Equity / Diluted\,Shares$ | Per-share intrinsic value |
| $Post\text{-}money = Pre\text{-}money + Investment$ | Gọi vốn |

---

*Tài liệu tham khảo: Damodaran "Investment Valuation" 4th Ed; McKinsey "Valuation" 7th Ed; Rosenbaum & Pearl "Investment Banking" 3rd Ed; Koller, Goedhart & Wessels "Valuation"; CFA Level II – Equity Valuation*
