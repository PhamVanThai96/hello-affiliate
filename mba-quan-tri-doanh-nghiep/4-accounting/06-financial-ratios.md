# Financial Ratios – Các Tỷ Số Tài Chính

> **Mục tiêu**: Hiểu bản chất (không chỉ công thức) của các tỷ số tài chính quan trọng nhất — Thanh khoản, Hiệu quả, Đòn bẩy, Lợi nhuận — nhìn từ góc độ **kế toán** (số liệu đến từ đâu trên BCTC theo VAS, chính sách kế toán làm méo tỷ số thế nào), kèm DuPont, red flags, case study từng bước và ứng dụng cho SME Việt Nam.

> **Liên hệ file khác**: File [`3-financial-management/05-financial-statement-analysis.md`](../3-financial-management/05-financial-statement-analysis.md) trình bày tỷ số trong bức tranh phân tích BCTC tổng thể (đọc 3 báo cáo, Quality of Earnings, Enron, Apple, Bách Hóa Xanh, "Làn Gió Mới Coffee"). File này **không lặp lại** các case đó mà tập trung vào: (1) **từ mã số/tài khoản kế toán đến tỷ số**, (2) **chính sách kế toán ảnh hưởng tỷ số**, (3) bộ case riêng (Apple dưới góc nhìn vòng quay vốn lưu động, Evergrande dưới góc nhìn đòn bẩy/thanh khoản, và một SME phân phối Việt Nam: "tăng trưởng đốt tiền").

---

## I. KHÁI NIỆM & LÝ THUYẾT

### 1. Định nghĩa

**Financial Ratios (Tỷ số tài chính)** là các **chỉ số định lượng** được tính bằng cách lấy một khoản mục trên BCTC chia cho một khoản mục khác (hoặc cho cùng khoản mục ở kỳ khác), dùng để **đánh giá sức khỏe tài chính, hiệu quả hoạt động và rủi ro** của doanh nghiệp.

> **"Ratios are like a doctor's vital signs – they tell you quickly if the patient is healthy, sick, or critical."**

Tỷ số là **ngôn ngữ chung** biến những con số tuyệt đối khó so sánh (công ty A lãi 500 triệu, công ty B lãi 5 tỷ) thành những con số tương đối so sánh được (A lãi 10% doanh thu, B lãi 3% doanh thu).

### 2. Tại sao phải dùng "tỷ số" mà không nhìn con số tuyệt đối? — Bối cảnh lịch sử

**Vấn đề kinh doanh cần giải quyết**: Một con số tuyệt đối không nói lên điều gì nếu không có "thước đo". Lãi 1 tỷ đồng là tốt hay xấu? Phụ thuộc vào việc bỏ ra bao nhiêu vốn, doanh thu bao nhiêu, đối thủ lãi bao nhiêu. Tỷ số chuẩn hóa mọi thứ về cùng một thang đo.

**Nguồn gốc lịch sử** (nên hiểu để thấy tỷ số không phải "trò chơi con số" mà sinh ra từ nhu cầu thực tế):

| Mốc | Sự kiện | Ý nghĩa |
|---|---|---|
| Cuối thế kỷ 19 (Mỹ) | Ngân hàng bắt đầu yêu cầu doanh nghiệp xin vay cung cấp bảng cân đối; **Current Ratio** (thường dùng ngưỡng "2:1") ra đời để trả lời câu hỏi "tài sản ngắn hạn có gấp đôi nợ ngắn hạn không?" | Tỷ số đầu tiên phục vụ **chủ nợ**, vì chủ nợ cần biết mình có được trả lại không |
| 1919 | **Alexander Wall** công bố nghiên cứu về hệ thống phân tích tỷ số (thường gọi là "credit barometrics"), đề xuất dùng nhiều tỷ số cùng lúc thay vì chỉ một | Chuyển từ "một con số" sang "một hệ thống tỷ số" |
| Thập niên 1910–1920 | **DuPont** (tập đoàn hóa chất Mỹ) — mà người gắn liền nhất là **Donaldson Brown**, nhân sự tài chính của DuPont — xây hệ thống tách ROE thành các thành phần để quản lý các bộ phận sau khi DuPont sáp nhập/kiểm soát General Motors | Cho phép biết ROE cao đến từ **biên lợi nhuận, vòng quay hay đòn bẩy** — mỗi thứ do một bộ phận quản lý chịu trách nhiệm |
| Thế kỷ 20 | Chuẩn hóa chuẩn mực kế toán (GAAP, IFRS, VAS) → BCTC đủ nhất quán để tỷ số so sánh được giữa các doanh nghiệp | Tỷ số chỉ có nghĩa khi **cách lập BCTC nhất quán** → đây là điểm giao giữa kế toán và phân tích |

*(Các mốc năm/người ở trên là kiến thức lịch sử phổ biến trong giáo trình, nên đối chiếu thêm nguồn khi trích dẫn chính thức.)*

### 3. Góc nhìn kế toán: Tỷ số là "đầu ra" của hệ thống kế toán

Một sai lầm phổ biến của người mới: coi tỷ số là phép toán độc lập với kế toán. Thực ra **mọi tỷ số đều phụ thuộc vào cách ghi sổ**:

```
Chứng từ → Sổ nhật ký/Sổ cái (TK) → Bảng cân đối phát sinh → BCTC → Tỷ số
   ▲                                                           │
   └──────  Chính sách kế toán (FIFO/BQGQ, khấu hao,           │
            dự phòng, ghi nhận doanh thu...) tác động ──────────┘
```

Do đó: (1) muốn tỷ số đúng thì sổ sách phải đúng và cắt kỳ đúng; (2) khi so sánh giữa hai doanh nghiệp phải kiểm tra **chính sách kế toán có giống nhau không**; (3) tỷ số tốt trên BCTC "làm đẹp" là tỷ số vô nghĩa.

#### Bảng ánh xạ: Số liệu tỷ số nằm ở đâu trên BCTC theo VAS (Thông tư 200/2014/TT-BTC)

| Thành phần dùng trong tỷ số | Vị trí trên BCTC | Mã số tham khảo* | Tài khoản kế toán (TT200) thường liên quan |
|---|---|---|---|
| Tài sản ngắn hạn (Current Assets) | Bảng CĐKT (B01-DN) | 100 | TK 111, 112, 121, 131, 141, 151–156... |
| Tiền & tương đương tiền (Cash) | B01-DN | 110 | TK 111, 112, 113 |
| Phải thu ngắn hạn (AR) | B01-DN | 130 | TK 131 (và 136, 138 khi liên quan) |
| Hàng tồn kho (Inventory) | B01-DN | 140 | TK 151–158 (trừ dự phòng TK 2294) |
| Tổng tài sản | B01-DN | 270 | — |
| Nợ phải trả (Total Liabilities) | B01-DN | 300 | TK 331, 333, 334, 338, 341... |
| Nợ ngắn hạn (Current Liabilities) | B01-DN | 310 | — |
| Vốn chủ sở hữu (Equity) | B01-DN | 400 | TK 411, 421... |
| Doanh thu thuần | KQKD (B02-DN) | 10 (từ 01 trừ giảm trừ 02) | TK 511 |
| Giá vốn hàng bán (COGS) | B02-DN | 11 | TK 632 |
| Lợi nhuận gộp | B02-DN | 20 | — |
| Chi phí lãi vay | B02-DN | 23 (nằm trong chi phí tài chính, mã 22) | TK 635 |
| Lợi nhuận trước thuế (EBT) | B02-DN | 50 | — |
| Lợi nhuận sau thuế (Net Income) | B02-DN | 60 | — |

*\*Mã số và tài khoản chỉ để định hướng, **cần đối chiếu mẫu biểu và hướng dẫn hiện hành**; doanh nghiệp nhỏ/siêu nhỏ có thể áp dụng chế độ kế toán khác (ví dụ Thông tư 133/2016/TT-BTC) với mẫu biểu khác — cần xác nhận hiện hành.*

**EBIT trên BCTC theo VAS** không có sẵn một dòng riêng: thường tính **EBIT = Lợi nhuận trước thuế (mã 50) + Chi phí lãi vay (mã 23)**. Nếu có thu nhập/chi phí khác bất thường, nên loại ra để EBIT phản ánh hoạt động cốt lõi.

### 4. Sử dụng tỷ số theo đối tượng

| Đối tượng | Dùng tỷ số để | Tỷ số quan tâm |
|----------|--------------|----------------|
| **Nhà đầu tư** | Quyết định mua/bán | ROE, P/E, EPS, Dividend Yield |
| **Ngân hàng/Chủ nợ** | Quyết định cho vay | D/E, Interest Coverage, Current Ratio |
| **Nhà quản lý** | Đánh giá, cải thiện | ROA, Inventory Turnover, Operating Margin |
| **Nhà cung cấp** | Quyết định cấp hạn mức công nợ | Quick Ratio, DPO của khách hàng |
| **Cơ quan thuế/Kiểm toán** | Rà soát bất thường | Gross Margin so với ngành, tỷ lệ chi phí/doanh thu (cần xác nhận phạm vi áp dụng hiện hành) |
| **Đối thủ** | Benchmarking | Mọi tỷ số |

### 5. Sơ đồ tổng quan 4 nhóm tỷ số

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

Bốn nhóm này tương ứng bốn câu hỏi của chủ doanh nghiệp: *Có trả được nợ gần không? (Liquidity) – Có dùng tài sản/vốn lưu động hiệu quả không? (Efficiency) – Có vay quá mức không? (Leverage) – Có kiếm được tiền xứng đáng không? (Profitability)*.

### 6. Quy ước tính toán dùng xuyên suốt tài liệu

| Quy ước | Nội dung | Tại sao |
|---|---|---|
| Số ngày trong năm | **365 ngày** (một số tài liệu dùng 360) | Phải nhất quán giữa các kỳ khi so sánh |
| Số dư **bình quân** vs **cuối kỳ** | Về lý thuyết, tử số là **dòng chảy** (doanh thu, lợi nhuận — phát sinh cả kỳ) nên mẫu số nên là **số dư bình quân** (đầu kỳ + cuối kỳ)/2. Trong các case SME bên dưới, để dễ theo dõi từng bước, dùng **số dư cuối kỳ** và ghi rõ | Tử số là dòng chảy cả năm, mẫu số là "ảnh chụp" một thời điểm → nếu doanh nghiệp tăng trưởng nhanh, số cuối kỳ làm tỷ số **thấp hơn thực tế** (AR/HTK lớn hơn mức bình quân cả năm) hoặc ngược lại; dùng bình quân giảm méo |
| Chiều của tỷ số | Tỷ số **lợi nhuận/vòng quay**: cao thường tốt; tỷ số **đòn bẩy**: cao thường rủi ro; tỷ số **DSO/DIO/CCC**: thấp thường tốt | Tránh đọc nhầm chiều |
| Benchmark | So sánh **cùng ngành, cùng quy mô, cùng chính sách kế toán** | Tỷ số tuyệt đối vô nghĩa nếu thiếu "thước đo" |

---

## II. CHI TIẾT TỪNG THÀNH PHẦN

### A. NHÓM 1: LIQUIDITY RATIOS (TỶ SỐ THANH KHOẢN)

#### 1. Mục đích và nguồn gốc ý tưởng

**Vấn đề giải quyết**: Doanh nghiệp có lãi trên giấy vẫn có thể phá sản vì **không có tiền trả nợ đúng hạn** (lãi kế toán ≠ tiền mặt). Nhóm này trả lời: *"Trong 12 tháng tới (hoặc chu kỳ kinh doanh), tài sản có thể chuyển thành tiền có đủ để trả các khoản nợ đến hạn không?"*

**Logic xây dựng**: Chia tài sản theo **mức độ dễ chuyển thành tiền** (tính thanh khoản), rồi so với nghĩa vụ phải trả sớm. Ba tỷ số = ba mức độ "khắt khe" khác nhau về tài sản nào được tính.

#### 2. Current Ratio (Tỷ số thanh toán hiện hành)

$$\text{Current Ratio} = \frac{\text{Current Assets}}{\text{Current Liabilities}}$$

**Tại sao lại thế**: Tử số là mọi tài sản dự kiến chuyển thành tiền trong ≤ 12 tháng (hoặc 1 chu kỳ), mẫu số là mọi khoản nợ đến hạn trong cùng kỳ. Tỷ số lớn hơn 1 nghĩa là về nguyên tắc, nếu mọi tài sản ngắn hạn thanh lý đúng giá trị sổ sách thì đủ trả nợ ngắn hạn. Ngưỡng "2:1" cổ điển có từ yêu cầu của các ngân hàng Mỹ đầu thế kỷ 20 — tạo "đệm an toàn" cho trường hợp tài sản bán không được giá sổ sách.

| Giá trị | Ý nghĩa |
|---------|---------|
| < 1.0 | **Nguy hiểm** – Không đủ tài sản ngắn hạn cover nợ ngắn hạn |
| 1.0 - 1.5 | **Cảnh báo** – Vừa đủ, rủi ro nếu có biến động |
| 1.5 - 3.0 | **Khỏe mạnh** – Đủ khả năng thanh toán |
| > 3.0 | **Quá cao** – Có thể giữ quá nhiều tiền/tồn kho/phải thu, sử dụng tài sản chưa hiệu quả |

**Hạn chế**: Tử số bao gồm **hàng tồn kho** (có thể khó bán nhanh, hoặc bán phải giảm giá) và **phải thu** (có thể thu chậm). → Cần Quick Ratio.

**Góc nhìn kế toán**: Current Ratio có thể bị "làm đẹp" cuối kỳ (window dressing): trả bớt nợ ngắn hạn ngay trước ngày khóa sổ để tỷ số cao lên, rồi vay lại ngay đầu kỳ sau. Ví dụ: CA = 200, CL = 100 → CR = 2.0; dùng 50 tiền trả nợ → CA = 150, CL = 50 → CR = 3.0. Hoặc phân loại nợ ngắn hạn thành dài hạn (tái cơ cấu hợp đồng vay). Phải xem thuyết minh để biết bản chất.

#### 3. Quick Ratio / Acid-Test Ratio (Tỷ số thanh toán nhanh)

$$\text{Quick Ratio} = \frac{\text{Current Assets} - \text{Inventory}}{\text{Current Liabilities}} \quad \text{hoặc} \quad \frac{\text{Cash} + \text{Short-term Investments} + \text{AR}}{\text{Current Liabilities}}$$

**Tại sao loại hàng tồn kho?** Tên "Acid-Test" xuất phát từ phép thử axit của thợ vàng thời xưa — kiểm tra xem vàng thật hay giả. Cũng vậy, Quick Ratio là "phép thử khắt khe" để xem thanh khoản có thật không. Hàng tồn kho bị loại vì: (1) là tài sản **khó chuyển thành tiền nhất** trong nhóm tài sản ngắn hạn (phải tìm khách, có thể phải giảm giá sâu, có thể lỗi mốt/hết hạn); (2) giá trị ghi sổ là **giá gốc**, không phải giá có thể thu về khi bán gấp; (3) trong khủng hoảng, hàng tồn kho là thứ bị "đóng băng" đầu tiên. Do đó Quick Ratio trả lời: *"Nếu không bán thêm được một món hàng nào, doanh nghiệp có trả được nợ ngắn hạn không?"*

| Giá trị | Ý nghĩa |
|---------|---------|
| < 0.5 | **Nguy hiểm** – Phụ thuộc bán tồn kho để trả nợ |
| 0.5 - 1.0 | **Chấp nhận được** – Hơi tight |
| 1.0 - 2.0 | **Tốt** – Thanh khoản vững |
| > 2.0 | **Rất tốt** nhưng có thể giữ quá nhiều tiền mặt |

#### 4. Cash Ratio (Tỷ số tiền mặt)

$$\text{Cash Ratio} = \frac{\text{Cash} + \text{Cash Equivalents}}{\text{Current Liabilities}}$$

**Tại sao**: Là phép thử khắt khe nhất, chỉ tính tiền (mã 110) — trả lời "nếu **ngày mai** chủ nợ đồng loạt đòi, doanh nghiệp có trả được bao nhiêu phần?". Không doanh nghiệp bình thường nào để Cash Ratio = 1 (giữ quá nhiều tiền nhàn rỗi là lãng phí cơ hội), nhưng **Cash Ratio < 0.1** là tín hiệu rất mong manh. Chủ nợ ngân hàng thường quan tâm khi doanh nghiệp có nhiều khoản vay đến hạn cùng lúc.

#### 5. So sánh 3 Liquidity Ratios

```
  Strict ◄──────────────────────────────── Lenient

  Cash Ratio    <    Quick Ratio    <    Current Ratio
  (Only cash)        (No inventory)      (All current assets)

  Ví dụ:
  Current Assets:  Tiền: 100   AR: 200   Inventory: 300   Total: 600
  Current Liab:    400

  Cash Ratio:     100/400       = 0.25  → Rất mỏng
  Quick Ratio:    (100+200)/400 = 0.75  → Tạm được
  Current Ratio:  600/400       = 1.50  → Nhìn có vẻ ổn
```

**Ví dụ thực tế – So sánh 2 công ty (giả định minh họa):**

| | Công ty A (Bán lẻ) | Công ty B (SaaS) |
|---|-------------------|-----------------|
| Tiền | 50 triệu | 300 triệu |
| Phải thu (AR) | 100 triệu | 200 triệu |
| Tồn kho | 400 triệu | 0 |
| Current Assets | 550 triệu | 500 triệu |
| Current Liabilities | 300 triệu | 250 triệu |
| **Current Ratio** | 550/300 = **1.83** | 500/250 = **2.00** |
| **Quick Ratio** | (50+100)/300 = **0.50** | (300+200)/250 = **2.00** |
| **Insight** | CR đẹp nhưng QR thấp → phụ thuộc bán hàng tồn kho | Cả hai đều tốt, thanh khoản thực sự mạnh |

---

### B. NHÓM 2: EFFICIENCY RATIOS (TỶ SỐ HIỆU QUẢ)

#### 1. Mục đích và nguồn gốc ý tưởng

**Vấn đề giải quyết**: Hai doanh nghiệp cùng doanh thu có thể cần lượng vốn rất khác nhau để vận hành. Doanh nghiệp nào biến vốn thành doanh thu nhanh hơn thì cần ít vốn hơn, ít phải vay hơn. Nhóm này đo **tốc độ quay vòng** của từng loại tài sản (hàng, công nợ, tài sản tổng thể).

**Logic chung của mọi "vòng quay"**: Lấy một **dòng chảy** (doanh thu hoặc giá vốn trong cả kỳ) chia cho một **số dư** (tồn kho, phải thu...) = "số lần số dư đó được thay mới trong kỳ". Rồi lấy 365 chia cho số lần đó = "số ngày một đồng vốn nằm lại ở khoản mục đó". Chuyển sang ngày giúp nhà quản lý dễ hình dung ("hàng nằm kho 46 ngày") và cộng/trừ được (CCC).

#### 2. Inventory Turnover (Vòng quay hàng tồn kho) và DIO

$$\text{Inventory Turnover} = \frac{\text{COGS}}{\text{Average Inventory}}, \qquad \text{DIO} = \frac{365}{\text{Inventory Turnover}}$$

**Tại sao dùng COGS (giá vốn) mà không dùng doanh thu?** Vì hàng tồn kho được ghi sổ theo **giá vốn**; chia doanh thu (có chứa lãi) cho tồn kho (giá vốn) sẽ so sánh hai thứ khác "thước đo" và làm vòng quay bị thổi phồng theo biên lợi nhuận. Dùng COGS giữ tử và mẫu cùng cơ sở giá gốc.

| Ngành | Turnover tốt | DIO tốt | Ghi chú |
|-------|-------------|---------|---------|
| FMCG (tiêu dùng nhanh) | 8-12x | 30-45 ngày | Nhanh – SP có hạn sử dụng |
| Thời trang | 4-6x | 60-90 ngày | Theo mùa |
| Điện tử | 6-10x | 35-60 ngày | Mất giá nhanh |
| Nội thất | 2-4x | 90-180 ngày | Chậm hơn |
| Xây dựng | 1-3x | 120-365 ngày | Rất chậm |

*(Khoảng giá trị mang tính tham khảo chung, cần đối chiếu số liệu ngành thực tế khi áp dụng.)*

**Ví dụ từng bước**: COGS = 2.000 triệu/năm, tồn kho bình quân = 400 triệu.

$$\text{Turnover} = \frac{2.000}{400} = 5{,}0 \text{ lần/năm}, \quad \text{DIO} = \frac{365}{5{,}0} = 73 \text{ ngày}$$

→ Hàng nằm trung bình 73 ngày trước khi bán. Ngành thời trang: chấp nhận được; FMCG: **quá chậm**.

**Góc nhìn kế toán**: DIO phụ thuộc vào **phương pháp tính giá xuất kho** (FIFO, bình quân gia quyền…) và **dự phòng giảm giá hàng tồn kho** — xem mục F.

#### 3. Accounts Receivable Turnover (Vòng quay phải thu) và DSO

$$\text{AR Turnover} = \frac{\text{Net Credit Sales}}{\text{Average AR}}, \qquad \text{DSO} = \frac{365}{\text{AR Turnover}}$$

**Tại sao**: DSO cho biết "trung bình bán xong bao lâu thì thu được tiền". Tử số lý tưởng là **doanh thu bán chịu thuần**; vì doanh nghiệp thường không tách riêng, thực hành dùng doanh thu thuần (có thể tính cả doanh thu thu tiền ngay → làm DSO thấp hơn thực tế). Người phân tích cẩn thận chỉ dùng doanh thu bán chịu nếu có số liệu.

| DSO | Ý nghĩa (cần so với điều khoản bán hàng của doanh nghiệp) |
|-----|---------|
| < 30 ngày | Xuất sắc – thu tiền nhanh |
| 30-45 ngày | Tốt |
| 45-60 ngày | Trung bình |
| 60-90 ngày | Cần cải thiện |
| > 90 ngày | Nguy hiểm – rủi ro nợ xấu cao |

**Nguyên tắc đọc**: So DSO thực tế với **hạn thanh toán cho khách**. Nếu điều khoản là 30 ngày mà DSO = 45 → khách đang trả chậm trung bình 15 ngày.

**Góc nhìn kế toán**: Rủi ro AR không chỉ ở thu chậm mà ở **không thu được** → cần lập dự phòng phải thu khó đòi (TK 2293 theo TT200 — cần xác nhận hiện hành). Nếu AR quá hạn lâu mà không trích dự phòng, tỷ số DSO và lợi nhuận đều "đẹp giả".

#### 4. Accounts Payable Turnover (Vòng quay phải trả) và DPO

$$\text{AP Turnover} = \frac{\text{COGS (hoặc Purchases)}}{\text{Average AP}}, \qquad \text{DPO} = \frac{365}{\text{AP Turnover}}$$

**Tại sao**: DPO là "số ngày doanh nghiệp giữ tiền của nhà cung cấp". DPO cao = **được nhà cung cấp tài trợ vốn lưu động miễn phí** → tốt cho dòng tiền, nhưng nếu kéo quá dài (vượt điều khoản) sẽ mất uy tín, bị siết hàng, mất chiết khấu thanh toán sớm. Lưu ý: tử số lý tưởng là **giá trị mua vào** (Purchases) vì AP phát sinh từ mua hàng chứ không phải từ giá xuất bán; dùng COGS là xấp xỉ chấp nhận được khi tồn kho ổn định.

#### 5. Cash Conversion Cycle (CCC – Chu kỳ chuyển đổi tiền mặt)

$$\boxed{\text{CCC} = \text{DIO} + \text{DSO} - \text{DPO}}$$

**Tại sao công thức là "cộng, cộng, trừ"?** Hãy đi theo chuỗi sự kiện của một đồng vốn: (1) trả tiền mua hàng (hoặc hết thời hạn nợ nhà cung cấp); (2) hàng nằm kho DIO ngày; (3) bán chịu, chờ khách trả DSO ngày; (4) khách trả tiền. Thời gian **doanh nghiệp tự bỏ vốn** từ lúc bắt đầu bỏ tiền ra đến lúc tiền thu về = DIO + DSO (chuỗi "tiền bị kẹt"). Nhưng trong thời gian đó doanh nghiệp **chưa phải trả** nhà cung cấp DPO ngày (nhà cung cấp tài trợ) → trừ đi. Phần còn lại là số ngày doanh nghiệp phải **tự tìm vốn** (vốn chủ hoặc vay). Khái niệm này do giới học thuật và thực hành quản trị vốn lưu động phát triển rộng rãi từ cuối thế kỷ 20 *(nên đối chiếu nguồn về nguồn gốc chính xác khi trích dẫn)*.

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
| < 0 (Negative CCC) | **Tuyệt vời** – Nhận tiền TRƯỚC khi trả (mô hình kiểu Dell, Amazon) |
| 0 - 30 ngày | Rất tốt |
| 30 - 60 ngày | Bình thường |
| 60 - 90 ngày | Cần tối ưu |
| > 90 ngày | Quá dài – vốn lưu động bị "đóng băng" |

**Quy đổi ra tiền**: Mỗi ngày CCC rút ngắn giải phóng lượng tiền bằng **giá vốn (hoặc doanh thu) bình quân một ngày**. Ví dụ doanh thu 24.000 triệu/năm → doanh thu/ngày ≈ 65,75 triệu → giảm 8 ngày DSO giải phóng ≈ 526 triệu. Đây là cách biến tỷ số thành **quyết định tiền thật**.

#### 6. Total Asset Turnover (Vòng quay tổng tài sản)

$$\text{Asset Turnover} = \frac{\text{Revenue}}{\text{Average Total Assets}}$$

**Tại sao**: Đo "mỗi đồng tài sản tạo ra bao nhiêu đồng doanh thu". Doanh nghiệp bán lẻ giá rẻ có thể lãi mỏng trên mỗi đồng doanh thu nhưng vòng quay tài sản rất cao; khách sạn/bất động sản thì ngược lại. Đây là một trong **3 trụ cột của DuPont** (mục E).

| Ngành | Asset Turnover | Ghi chú |
|-------|---------|---------|
| Bán lẻ | 2.0 - 3.0 | Ít tài sản cố định, doanh thu cao |
| FMCG | 1.0 - 2.0 | Nhà máy + distribution |
| Sản xuất nặng | 0.3 - 0.8 | Nhiều TSCĐ |
| Tech/SaaS | 0.5 - 1.0 | Tài sản vô hình cao |
| Bất động sản | 0.1 - 0.3 | Tài sản rất lớn |

**Góc nhìn kế toán**: Tài sản được ghi theo **giá gốc trừ khấu hao** (VAS) → tài sản cũ, đã khấu hao nhiều làm Asset Turnover **cao lên một cách giả tạo** so với công ty mới đầu tư tài sản mới. Vì vậy so sánh Asset Turnover giữa công ty có tuổi tài sản khác nhau cần thận trọng.

---

### C. NHÓM 3: LEVERAGE RATIOS (TỶ SỐ ĐÒN BẨY)

#### 1. Mục đích và nguồn gốc ý tưởng

**Vấn đề giải quyết**: Nợ vay là "con dao hai lưỡi": làm tăng lợi nhuận cho chủ sở hữu khi kinh doanh tốt, nhưng lãi và gốc phải trả bất kể kinh doanh tốt hay xấu. Nhóm này trả lời: *"Doanh nghiệp đang gánh bao nhiêu nghĩa vụ trả nợ so với nguồn lực, và có đủ lợi nhuận để trả lãi không?"* Phân tích sâu hơn về cơ cấu vốn tối ưu xem [`3-financial-management/04-capital-structure.md`](../3-financial-management/04-capital-structure.md).

#### 2. Debt-to-Equity Ratio (D/E)

$$\text{D/E Ratio} = \frac{\text{Total Liabilities}}{\text{Total Equity}}$$

**Tại sao**: So sánh "tiền của người ngoài" với "tiền của chủ". Chủ nợ nhìn vào đây để thấy **đệm vốn chủ** bảo vệ họ đến đâu: D/E = 1 nghĩa là 1 đồng vốn chủ đệm cho 1 đồng nợ. Lưu ý: có hai cách định nghĩa phổ biến — **tổng nợ phải trả / vốn chủ** (dùng trong tài liệu này) hoặc **chỉ nợ vay có lãi / vốn chủ**; cần ghi rõ định nghĩa khi so sánh.

| D/E | Ý nghĩa |
|-----|---------|
| < 0.5 | **Bảo thủ** – Ít nợ, rủi ro thấp, có thể chưa tối ưu đòn bẩy |
| 0.5 - 1.5 | **Cân bằng** – Sử dụng đòn bẩy hợp lý |
| 1.5 - 3.0 | **Aggressive** – Nhiều nợ, rủi ro cao, có thể tối ưu ROE |
| > 3.0 | **Nguy hiểm** – Rủi ro phá sản cao nếu kinh doanh suy giảm |

D/E khác nhau lớn giữa các ngành:

| Ngành | D/E tham khảo | Lý do |
|-------|---------------|-------|
| Utilities (điện nước) | 1.5 - 3.0 | Dòng tiền ổn định, tài sản có thể thế chấp |
| BĐS | 2.0 - 5.0 | Đòn bẩy bằng BĐS thế chấp |
| Tech | 0.0 - 0.5 | Cash-rich, ít cần vay |
| Bán lẻ | 0.5 - 1.5 | Vừa phải |
| Ngân hàng | 8.0 - 15.0 | Đặc thù ngành (tiền gửi = nợ phải trả) |

#### 3. Debt Ratio (Tỷ số nợ)

$$\text{Debt Ratio} = \frac{\text{Total Liabilities}}{\text{Total Assets}} = 1 - \text{Equity Ratio}$$

**Tại sao**: Cùng thông tin với D/E nhưng ở dạng "% tài sản được tài trợ bằng nợ" — dễ hiểu hơn với người không quen khái niệm D/E. Debt Ratio > 50% → tài sản chủ yếu tài trợ bằng nợ. Liên hệ: $\text{D/E} = \frac{\text{Debt Ratio}}{1 - \text{Debt Ratio}}$ (ví dụ Debt Ratio 56,85% → D/E = 0,5685/0,4315 ≈ 1,32).

**Góc nhìn kế toán — nợ "ngầm" ngoài bảng**: Hợp đồng thuê tài chính/thuê hoạt động dài hạn, bảo lãnh vay cho bên liên quan, cam kết ngoài bảng... có thể không nằm trong Nợ phải trả nhưng là nghĩa vụ thực. Theo IFRS 16, hầu hết hợp đồng thuê phải ghi lên bảng cân đối, còn VAS ít chặt chẽ hơn (cần xác nhận hiện hành) → D/E theo VAS có thể **thấp hơn thực chất** nếu doanh nghiệp thuê nhiều (cửa hàng, nhà xưởng).

#### 4. Interest Coverage Ratio / Times Interest Earned (ICR)

$$\text{Interest Coverage} = \frac{\text{EBIT}}{\text{Interest Expense}}$$

**Tại sao dùng EBIT, trước thuế và trước lãi?** Lãi vay được trả **từ lợi nhuận trước khi** có lãi vay và thuế (lãi vay là chi phí được trừ trước thuế). Vì vậy câu hỏi đúng là: *"Lợi nhuận hoạt động cốt lõi gấp bao nhiêu lần lãi phải trả?"* — ICR càng cao, "đệm" chống suy giảm lợi nhuận càng dày. Nếu ICR = 5 thì EBIT có thể giảm đến 80% mà vẫn đủ trả lãi.

| ICR | Ý nghĩa |
|-----|---------|
| < 1.0 | **Rất nguy** – Không đủ lợi nhuận trả lãi vay |
| 1.0 - 1.5 | **Nguy hiểm** – Chỉ vừa đủ, không có room |
| 1.5 - 3.0 | **Chấp nhận** – Cần cẩn thận |
| 3.0 - 6.0 | **Tốt** – Dư sức trả lãi |
| > 6.0 | **Rất tốt** – Hoặc ít nợ |

**Ví dụ**: EBIT = 500 triệu, lãi vay = 100 triệu → ICR = 500/100 = 5,0x → EBIT giảm tối đa còn 100 (giảm 80%) vẫn đủ trả lãi.

**Hạn chế quan trọng**: ICR chỉ xét **lãi**, không xét **trả gốc**; doanh nghiệp có ICR đẹp vẫn có thể vỡ nợ nếu gốc nợ đến hạn lớn. Do đó ngân hàng còn dùng thêm **DSCR** (xem phụ lục công thức): $\text{DSCR} = \frac{\text{Dòng tiền khả dụng để trả nợ}}{\text{Gốc + Lãi phải trả trong kỳ}}$.

#### 5. Equity Multiplier (Hệ số vốn chủ sở hữu)

$$\text{Equity Multiplier} = \frac{\text{Total Assets}}{\text{Total Equity}} = 1 + \text{D/E Ratio}$$

**Tại sao**: Cho biết "mỗi 1 đồng vốn chủ chống đỡ bao nhiêu đồng tài sản". Đây là thành phần "đòn bẩy" trong DuPont. Chứng minh nhanh: Tài sản = Nợ + Vốn chủ → Tài sản/Vốn chủ = Nợ/Vốn chủ + 1.

---

### D. NHÓM 4: PROFITABILITY RATIOS (TỶ SỐ LỢI NHUẬN)

#### 1. Mục đích và nguồn gốc ý tưởng

**Vấn đề giải quyết**: Kiếm 1 tỷ đồng lợi nhuận là nhiều hay ít? Phải so với doanh thu (biên lợi nhuận), với tài sản (ROA), và với vốn chủ bỏ ra (ROE). Mỗi mẫu số trả lời một câu hỏi khác nhau, vì vậy cần cả bộ chứ không dùng một tỷ số.

#### 2. Gross Margin (Biên lợi nhuận gộp)

$$\text{Gross Margin} = \frac{\text{Revenue} - \text{COGS}}{\text{Revenue}} \times 100\%$$

**Tại sao**: Đo "phần doanh thu còn lại sau khi trả chi phí trực tiếp tạo ra hàng bán". Đây là thước đo **sức mạnh định giá** và **hiệu quả sản xuất/mua hàng**. Biên gộp giảm = giá bán giảm hoặc giá vốn tăng nhanh hơn.

| Ngành | Gross Margin tham khảo | Ghi chú |
|-------|------------------------|---------|
| SaaS/Software | 70-90% | Chi phí biên gần 0 |
| Dược phẩm | 60-80% | R&D cao nhưng SX rẻ |
| Thời trang | 50-65% | Markup cao |
| F&B (nhà hàng) | 60-70% | Food cost 30-40% |
| Bán lẻ | 25-40% | Margin mỏng, volume lớn |
| Phân phối hàng tiêu dùng | 10-20% | Margin mỏng, vòng quay nhanh |
| Xây dựng | 10-20% | Chi phí NVL & nhân công cao |

**Góc nhìn kế toán**: Biên gộp **phụ thuộc cách phân loại chi phí** — cùng một khoản có thể xếp vào giá vốn (TK 632) hoặc chi phí bán hàng (TK 641), làm biên gộp khác nhau mà lợi nhuận ròng không đổi. Ví dụ: nhà hàng xếp lương đầu bếp vào giá vốn thì biên gộp thấp hơn nhà hàng xếp vào chi phí QLDN. Khi so sánh biên gộp giữa hai doanh nghiệp, phải kiểm tra cách phân loại.

#### 3. Operating Margin và EBITDA Margin

$$\text{Operating Margin} = \frac{\text{EBIT}}{\text{Revenue}}, \qquad \text{EBITDA Margin} = \frac{\text{EBIT} + \text{Depreciation \& Amortization}}{\text{Revenue}}$$

**Tại sao**: Operating Margin phản ánh hiệu quả **hoạt động kinh doanh cốt lõi** (trước cấu trúc vốn và thuế) — cho phép so sánh hai công ty vay nợ khác nhau. EBITDA Margin loại thêm khấu hao (khoản chi phí **không dùng tiền** trong kỳ và phụ thuộc chính sách khấu hao) để thấy khả năng tạo dòng tiền hoạt động thô và so sánh công ty có chính sách khấu hao khác nhau. **Cẩn thận**: EBITDA bỏ qua nhu cầu tái đầu tư tài sản — doanh nghiệp nhiều tài sản (nhà hàng, sản xuất) không nên coi EBITDA như tiền thật có thể chi tự do.

#### 4. Net Profit Margin (Biên lợi nhuận ròng)

$$\text{Net Margin} = \frac{\text{Net Income}}{\text{Revenue}} \times 100\%$$

**Tại sao**: "Bottom line" — cuối cùng giữ lại bao nhiêu từ mỗi đồng doanh thu sau **mọi** chi phí, lãi vay và thuế. Biên ròng của một số ngành (phân phối, bán lẻ) chỉ vài %; biên 3% không "tệ" nếu vòng quay nhanh (xem DuPont).

#### 5. Return on Equity (ROE)

$$\boxed{\text{ROE} = \frac{\text{Net Income}}{\text{Average Equity}} \times 100\%}$$

**Tại sao**: ROE là thước đo từ góc nhìn **chủ sở hữu**: "mỗi đồng vốn tôi bỏ vào kiếm được bao nhiêu". Phải đạt ít nhất cao hơn lãi suất gửi tiết kiệm/chi phí cơ hội vốn chủ, nếu không chủ doanh nghiệp bỏ tiền ngân hàng còn hơn.

| ROE | Ý nghĩa |
|-----|---------|
| < 5% | Yếu – thấp hơn gửi tiết kiệm |
| 5-10% | Trung bình |
| 10-20% | Tốt |
| 20-30% | Rất tốt |
| > 30% | Xuất sắc (hoặc leverage rất cao) |

**ROE cao có thể do 3 nguyên nhân rất khác nhau:**
1. Kinh doanh thật sự hiệu quả → **Tốt**
2. Sử dụng nợ nhiều (leverage) → **Rủi ro cao**
3. Vốn chủ thấp do lỗ lũy kế hoặc mua lại cổ phiếu/chia cổ tức lớn → **Cần phân tích thêm**

→ Cần phân tích bằng **DuPont** để hiểu rõ (mục E).

#### 6. Return on Assets (ROA)

$$\text{ROA} = \frac{\text{Net Income}}{\text{Average Total Assets}} \times 100\%$$

**Tại sao**: Đo hiệu quả sử dụng **tài sản** bất kể tài sản được tài trợ bằng nợ hay vốn chủ → phù hợp để đánh giá **năng lực quản lý** (nhà quản lý tạo lợi nhuận từ tài sản được giao). (Một số tài liệu hiệu chỉnh tử số thành $\text{NI} + \text{Lãi vay}\times(1-T)$ để loại ảnh hưởng của cách tài trợ — cần nêu rõ định nghĩa khi so sánh.)

| | ROE | ROA |
|---|-----|-----|
| Tử số | Net Income | Net Income |
| Mẫu số | Equity only | Total Assets |
| Ảnh hưởng leverage | Có – đòn bẩy tăng ROE | Ít – độc lập cấu trúc vốn |
| Phù hợp | Đánh giá cho chủ sở hữu | Đánh giá hiệu quả quản lý |

---

### E. DUPONT ANALYSIS – PHÂN TÍCH DUPONT

#### 1. Nguồn gốc & tại sao cần tách ROE?

DuPont là tập đoàn hóa chất Mỹ; trong những năm 1910–1920, nhân sự tài chính của công ty (gắn với tên **Donaldson Brown**) xây dựng hệ thống tách ROE thành các thành phần để lãnh đạo biết **bộ phận nào chịu trách nhiệm** khi ROE biến động (ví dụ: bán hàng chịu trách nhiệm biên lợi nhuận, vận hành chịu trách nhiệm vòng quay, tài chính chịu trách nhiệm đòn bẩy) *(chi tiết lịch sử nên đối chiếu thêm nguồn)*.

**Vấn đề**: Con số ROE 20% không cho biết nó "tốt" hay "xấu" vì có thể đến từ ba cách rất khác nhau: bán sản phẩm đắt (biên cao), bán nhanh (vòng quay cao), hoặc vay nhiều (đòn bẩy cao). Hai công ty cùng ROE 20% có thể rủi ro hoàn toàn khác nhau. DuPont "mổ xẻ" ROE để chỉ ra nguồn gốc.

#### 2. DuPont 3 thành phần

$$\boxed{\text{ROE} = \underbrace{\frac{\text{Net Income}}{\text{Revenue}}}_{\text{Net Margin}} \times \underbrace{\frac{\text{Revenue}}{\text{Assets}}}_{\text{Asset Turnover}} \times \underbrace{\frac{\text{Assets}}{\text{Equity}}}_{\text{Equity Multiplier}}}$$

Đây là một **đồng nhất thức đại số**: Doanh thu và Tài sản "triệt tiêu" khi nhân ba phân số, còn lại $\text{NI}/\text{Equity}$ = ROE. Nghĩa của nó: ROE = **Khả năng sinh lời** × **Hiệu quả dùng tài sản** × **Đòn bẩy tài chính**.

```
                      ROE
                       │
          ┌────────────┼────────────┐
          │            │            │
     Net Margin   Asset Turnover  Equity Multiplier
     (Lợi nhuận)  (Hiệu quả)     (Đòn bẩy)
          │            │            │
     Net Income     Revenue      Assets
     ──────────    ─────────    ─────────
      Revenue       Assets       Equity
```

#### 3. Ví dụ so sánh 2 mô hình (giả định minh họa)

| Component | Công ty X (Luxury) | Công ty Y (Bán lẻ giá rẻ) |
|-----------|-------------------|--------------------------|
| **Net Margin** | 15% | 3% |
| **Asset Turnover** | 0.8x | 3.0x |
| **Equity Multiplier** | 1.5x | 2.5x |
| **ROE** | 15% × 0.8 × 1.5 = **18%** | 3% × 3.0 × 2.5 = **22,5%** |

- **X**: ROE đến từ **biên cao** (sản phẩm premium), đòn bẩy thấp, rủi ro thấp.
- **Y**: ROE đến từ **vòng quay cao** + **đòn bẩy cao** — ROE cao hơn nhưng nhạy cảm với suy thoái hơn.

#### 4. DuPont 5 thành phần (mở rộng)

$$\text{ROE} = \underbrace{\frac{\text{NI}}{\text{EBT}}}_{\text{Tax Burden}} \times \underbrace{\frac{\text{EBT}}{\text{EBIT}}}_{\text{Interest Burden}} \times \underbrace{\frac{\text{EBIT}}{\text{Revenue}}}_{\text{Operating Margin}} \times \underbrace{\frac{\text{Revenue}}{\text{Assets}}}_{\text{Asset Turnover}} \times \underbrace{\frac{\text{Assets}}{\text{Equity}}}_{\text{Equity Multiplier}}$$

**Tại sao tách thêm**: 3 thành phần gộp cả thuế và lãi vay vào "Net Margin". 5 thành phần tách riêng: **gánh nặng thuế** (NI/EBT: ví dụ thuế 20% → 0,8) và **gánh nặng lãi vay** (EBT/EBIT: lãi vay "ăn" bao nhiêu % EBIT). Nhờ đó phân biệt được: ROE tăng là do kinh doanh cốt lõi tốt lên (Operating Margin ↑) hay chỉ do thuế/lãi vay giảm. Một Interest Burden thấp (ví dụ 0,5) = nửa lợi nhuận hoạt động bị lãi vay nuốt.

---

### F. CHÍNH SÁCH KẾ TOÁN ẢNH HƯỞNG TỶ SỐ NHƯ THẾ NÀO

Đây là điểm đặc thù của góc nhìn kế toán: **cùng một hoạt động kinh doanh, hai chính sách kế toán khác nhau cho hai bộ tỷ số khác nhau**.

| Chính sách kế toán | Ảnh hưởng chính | Tỷ số bị tác động |
|---|---|---|
| Phương pháp tính giá xuất kho (FIFO, bình quân gia quyền, đích danh; VAS 02 không cho LIFO — cần xác nhận hiện hành) | Giá vốn, tồn kho cuối kỳ, lợi nhuận | Gross Margin, Current Ratio, DIO, Inventory Turnover |
| Phương pháp khấu hao (đường thẳng, số dư giảm dần…) và thời gian hữu dụng ước tính | Chi phí khấu hao, giá trị TSCĐ ròng | Operating Margin, ROA, Asset Turnover |
| Dự phòng phải thu khó đòi/giảm giá hàng tồn kho | Giá trị AR, HTK, lợi nhuận | Current Ratio, DSO, DIO, Net Margin |
| Thời điểm ghi nhận doanh thu (cut-off) | Doanh thu, AR, lợi nhuận | Gần như mọi tỷ số |
| Vốn hóa vs ghi nhận ngay chi phí (ví dụ chi phí sửa chữa lớn) | Chi phí kỳ, tài sản | Margin, ROA, Asset Turnover |
| Phân loại nợ ngắn hạn/dài hạn | Nợ ngắn hạn | Current Ratio, Quick Ratio |

#### Ví dụ: FIFO vs Bình quân gia quyền (giả định minh họa, đơn vị nghìn đồng, giá tăng)

Dữ liệu: Tồn đầu 100 sản phẩm, giá 10/sp. Nhập thêm 100 sp, giá 12/sp. Bán 120 sp, giá bán 20/sp. Doanh thu = 120 × 20 = 2.400.

| | FIFO | Bình quân gia quyền |
|---|---|---|
| Cách tính giá vốn | 100 × 10 + 20 × 12 = 1.240 | 120 × [(100×10 + 100×12)/200] = 120 × 11 = 1.320 |
| Lợi nhuận gộp | 2.400 − 1.240 = 1.160 | 2.400 − 1.320 = 1.080 |
| **Gross Margin** | 1.160/2.400 = **48,3%** | 1.080/2.400 = **45,0%** |
| Tồn kho cuối kỳ | 2.200 − 1.240 = 960 | 2.200 − 1.320 = 880 |

**Giải thích**: Khi giá nhập tăng, FIFO xuất hàng cũ (rẻ) trước nên giá vốn thấp, biên gộp cao hơn và tồn kho cuối kỳ (hàng mới, đắt) lớn hơn. Hai công ty đồng nhất về kinh doanh nhưng chọn chính sách khác nhau sẽ có Gross Margin chênh 3,3 điểm %. **Hệ quả**: Không so sánh Gross Margin/Current Ratio giữa hai doanh nghiệp mà không kiểm tra chính sách giá xuất kho trong thuyết minh BCTC. Đồng thời, đổi chính sách phải thuyết minh và áp dụng nhất quán (nguyên tắc nhất quán của kế toán).

---

### G. RED FLAGS & WARNING SIGNS

#### 1. Dấu hiệu cảnh báo trong tỷ số

| Mức | Tỷ số | Ngưỡng ví dụ | Ý nghĩa |
|----------|-------|--------|---------|
| Đỏ | Current Ratio < 1.0 | Giảm 3 quý liên tiếp | Sắp mất khả năng thanh toán |
| Đỏ | D/E tăng nhanh | +50% trong 1 năm | Vay nợ quá mức |
| Đỏ | Interest Coverage < 1.5 | Và đang giảm | Không đủ trả lãi |
| Vàng | DIO tăng nhanh | +30% so với cùng kỳ | Hàng tồn kho ứ đọng |
| Vàng | DSO tăng | > 90 ngày hoặc tăng nhanh hơn doanh thu | Khách chậm trả, nợ xấu, hoặc ghi nhận doanh thu sớm |
| Vàng | Gross Margin giảm | −5 điểm % YoY | Mất pricing power hoặc NVL tăng |
| Vàng | ROE tăng do EM tăng | EM tăng nhưng Net Margin không đổi/giảm | "Đẹp mặt nhưng rỗng ruột" |
| Vàng | CFO < Net Income | 3+ kỳ liên tiếp | Chất lượng lợi nhuận thấp |

*(Các ngưỡng là quy tắc kinh nghiệm, không phải quy định pháp lý.)*

#### 2. Sơ đồ cảnh báo: doanh nghiệp "trông có vẻ khỏe"

```
  Revenue: ↑ 20%    ← Tốt!
  Net Income: ↑ 25% ← Rất tốt!

  NHƯNG nhìn kỹ ratios:
  DSO: 45 → 85 ngày       ← Ghi doanh thu nhưng chưa thu được tiền?
  DIO: 30 → 55 ngày       ← Hàng bán không chạy?
  Current Ratio: 2.0 → 1.2 ← Thanh khoản giảm nhanh
  CFO: +100tr → -50tr      ← Cash flow ÂM dù profit DƯƠNG

  → Có thể DN đang ghi nhận doanh thu quá sớm hoặc bán chịu quá nhiều
     → rủi ro nợ xấu và thiếu tiền
```

**Nguyên tắc quan trọng**: Không dựa vào một tỷ số đơn lẻ; tìm **sự phân kỳ** giữa các tỷ số (lợi nhuận tăng nhưng tiền giảm; doanh thu tăng nhưng DSO tăng nhanh hơn). Xem thêm Quality of Earnings Checklist ở file 05.

---

### H. ƯU VÀ NHƯỢC ĐIỂM CỦA PHÂN TÍCH TỶ SỐ

| Ưu điểm | Chi tiết |
|---------|---------|
| **Đơn giản** | Dễ tính từ BCTC có sẵn |
| **So sánh được** | Benchmark với ngành, đối thủ, qua các năm |
| **Snapshot nhanh** | "Health check" tài chính trong vài phút |
| **Ngôn ngữ chung** | Giữa chủ doanh nghiệp, kế toán, ngân hàng, nhà đầu tư |
| **Cảnh báo sớm** | Phát hiện xu hướng xấu sớm |

| Nhược điểm | Chi tiết |
|-----------|---------|
| **Dựa trên quá khứ** | Không dự báo tương lai |
| **Phụ thuộc chất lượng kế toán** | BCTC bị "làm đẹp" hoặc sổ sách sai → tỷ số sai |
| **Phụ thuộc chính sách kế toán** | Xem mục F; VAS vs IFRS khác biệt |
| **Chỉ so sánh cùng ngành** | Cross-industry vô nghĩa |
| **Một thời điểm** | Cần xu hướng, không chỉ 1 mốc; số cuối kỳ có tính mùa vụ |
| **Không thấy phi tài chính** | Khách hàng hài lòng, đổi mới, văn hóa |
| **Thiên lệch quy mô** | DN nhỏ/lớn có đặc điểm khác nhau |

---

### I. HOÀN CẢNH VÀ MÔI TRƯỜNG ÁP DỤNG

#### 1. Theo mục đích sử dụng

| Mục đích | Tỷ số quan trọng nhất | Vì sao |
|----------|----------------------|--------|
| **Xin vay ngân hàng** | Current Ratio, D/E, ICR, DSO | Ngân hàng quan tâm khả năng trả nợ |
| **Gọi vốn đầu tư** | ROE, tăng trưởng doanh thu, Net Margin | Nhà đầu tư quan tâm lợi suất và tăng trưởng |
| **Quản lý nội bộ** | Gross Margin, CCC, Asset Turnover | Tối ưu vận hành |
| **Mua bán DN (M&A)** | EV/EBITDA, ROA, DuPont | Đánh giá giá trị và hiệu quả |
| **Đánh giá đối thủ** | Tất cả, benchmarking | So sánh vị thế |

#### 2. Theo giai đoạn doanh nghiệp

```
  Startup     →  Growth      →  Maturity    →  Decline
  │               │               │               │
  Burn Rate      Revenue         Net Margin      Cash Ratio
  Runway         Growth%         ROE/ROA         D/E
  CAC/LTV        Gross Margin    DuPont          ICR
  CCC            CCC             CCC             Thanh lý
                                 Dividend        (liquidation)
                                 Payout          ratios
```

**Burn Rate và Runway** (đặc thù startup, khi chưa có lợi nhuận): $\text{Burn Rate} = $ tiền mặt tiêu hao ròng mỗi tháng; $\text{Runway} = \frac{\text{Tiền mặt hiện có}}{\text{Burn Rate}}$. Ví dụ: tiền mặt 480 triệu, burn 60 triệu/tháng → runway = 480/60 = **8 tháng**. Tại sao: với startup lỗ, Current Ratio chưa đủ nói lên "còn sống được bao lâu"; runway trả lời trực tiếp.

---

## III. CASE STUDIES THỰC TẾ

> **Lưu ý về nguồn số liệu**: Số liệu doanh nghiệp thật (Apple, Evergrande) dưới đây là số **làm tròn/xấp xỉ**, **cần đối chiếu nguồn gốc (10-K, báo cáo thường niên)** trước khi dùng cho mục đích chính thức. Số liệu công ty "Phân phối Thực phẩm Hải Long" là **giả định minh họa** do tác giả tự thiết kế, đã kiểm tra nhất quán về số học.

### 1. Case Study Thành công: Apple Inc. – Vòng quay vốn lưu động và ROE 150%+ nhìn từ góc độ kế toán

*(Case Apple dưới góc nhìn DuPont/mua lại cổ phiếu đã có ở file 05; ở đây tập trung vào **các tỷ số liên quan đến vốn lưu động và thanh khoản**, và sửa các sai số thường gặp khi trích dẫn.)*

#### Bối cảnh

Apple là doanh nghiệp có mô hình "ít tài sản, thuê ngoài sản xuất, bán lẻ trực tiếp". Câu hỏi: Tại sao Apple có Current Ratio dưới 1.0 nhưng không hề có rủi ro thanh khoản?

#### Số liệu FY2023 (xấp xỉ, USD tỷ — cần đối chiếu 10-K)

| Khoản mục | Giá trị |
|---|---|
| Doanh thu | 383,3 |
| Giá vốn hàng bán | 214,1 |
| Lợi nhuận ròng | 97,0 |
| Tài sản ngắn hạn | 143,6 |
| Nợ ngắn hạn | 145,3 |
| Tổng tài sản | 352,6 |
| Tổng nợ phải trả | 290,4 |
| Vốn chủ sở hữu | 62,1 |
| Hàng tồn kho | 6,3 |
| Phải thu | 29,5 |
| Phải trả nhà cung cấp | 62,6 |

#### Bước 1: Tính thanh khoản

$$\text{Current Ratio} = \frac{143{,}6}{145{,}3} \approx 0{,}99$$

Dưới 1.0 → theo quy tắc cổ điển là "cảnh báo". Nhưng nhìn cấu trúc nợ ngắn hạn: phần lớn là **phải trả nhà cung cấp** (62,6) — khoản nợ hoạt động mà Apple dùng như nguồn vốn vì được trả chậm; kèm với dòng tiền hoạt động rất lớn (hàng chục tỷ USD mỗi quý, cần đối chiếu) và các khoản đầu tư tài chính dễ thanh khoản.

#### Bước 2: Tính chu kỳ chuyển đổi tiền mặt (dùng số cuối kỳ)

$$\text{DIO} = \frac{6{,}3}{214{,}1} \times 365 \approx 10{,}8 \text{ ngày}$$

$$\text{DSO} = \frac{29{,}5}{383{,}3} \times 365 \approx 28{,}1 \text{ ngày}$$

$$\text{DPO} = \frac{62{,}6}{214{,}1} \times 365 \approx 106{,}7 \text{ ngày}$$

$$\text{CCC} = 10{,}8 + 28{,}1 - 106{,}7 \approx -67{,}8 \text{ ngày}$$

*(Phiên bản cũ của file ghi DIO ≈ 9, DPO ≈ 97, CCC ≈ −60; con số phụ thuộc vào việc dùng số cuối kỳ hay bình quân và nguồn dữ liệu — hãy luôn ghi rõ cách tính.)*

#### Bước 3: Diễn giải ý nghĩa kinh doanh

```
  Hàng nằm kho:         ~11 ngày  (thuê ngoài sản xuất, nhập đúng lúc)
  Chờ khách trả tiền:   ~28 ngày  (nhiều bán lẻ/thanh toán thẻ)
  Chờ trả nhà cung cấp: ~107 ngày (Apple có sức mạnh đàm phán)

  CCC âm ≈ -68 ngày → Nhận tiền từ khách trước khi trả nhà cung cấp
  ≈ 2 tháng → nhà cung cấp "cho vay không lãi" để Apple hoạt động
```

#### Bước 4: Tính đòn bẩy, ROE và đối chiếu sai số cũ

$$\text{Net Margin} = \frac{97{,}0}{383{,}3} = 25{,}3\%, \quad \text{Asset Turnover} = \frac{383{,}3}{352{,}6} = 1{,}087, \quad \text{EM} = \frac{352{,}6}{62{,}1} = 5{,}67$$

$$\text{ROE} = 25{,}3\% \times 1{,}087 \times 5{,}67 \approx 156\%$$

$$\text{D/E} = \frac{290{,}4}{62{,}1} \approx 4{,}67 \text{ (tổng nợ phải trả/vốn chủ)}$$

**Lỗi số liệu cũ đã sửa**: bản cũ ghi Asset Turnover 1,16 → ROE ~166% (mâu thuẫn với "ROE 160%+" ở bảng trên) và D/E "~2,0" (con số đó gần với nợ vay có lãi/vốn chủ chứ không phải tổng nợ phải trả/vốn chủ). Khi tính cùng định nghĩa như bảng trên, D/E ≈ 4,67; dùng số bình quân vốn chủ thì ROE còn cao hơn (~172%).

#### Bước 5: Vì sao ROE 156% nhưng không "nguy hiểm"?

Vốn chủ (62,1) thấp một phần do Apple **chủ động mua lại cổ phiếu quỹ** lớn nhiều năm và trả cổ tức → làm giảm vốn chủ → tăng EM. Giả định minh họa: nếu vốn chủ là 150 thay vì 62,1 thì $\text{ROE} = 97{,}0/150 \approx 64{,}7\%$ — vẫn rất cao. Đòn bẩy cao nhưng đi cùng biên lợi nhuận 25%, dòng tiền khổng lồ → khác hẳn doanh nghiệp "ROE cao do vay nợ để sống".

#### Bài học

> 1. **Current Ratio < 1 không tự động là nguy hiểm** — phải xem *bản chất* nợ ngắn hạn và dòng tiền hoạt động.
> 2. **CCC âm là đỉnh cao quản trị vốn lưu động** — dựa trên sức mạnh đàm phán, không sao chép máy móc cho SME.
> 3. **Phải ghi rõ cách tính** (cuối kỳ/bình quân, định nghĩa D/E) vì chênh lệch định nghĩa tạo ra các con số rất khác nhau.
> 4. **Bài học cho SME**: không thể sao chép CCC âm, nhưng có thể học tư duy "biến nhà cung cấp thành nguồn vốn" bằng cách thương lượng DPO hợp lý.

---

### 2. Case Study Thất bại: Evergrande – Đòn bẩy và thanh khoản mất kiểm soát

#### Bối cảnh

China Evergrande Group là một trong những tập đoàn bất động sản lớn nhất Trung Quốc, nợ phải trả hơn 300 tỷ USD (cần đối chiếu nguồn), rơi vào vỡ nợ từ năm 2021; Tòa án Hồng Kông ra lệnh thanh lý công ty vào tháng 1/2024 *(cần đối chiếu nguồn)*. Chính sách **"Ba lằn ranh đỏ" (Three Red Lines)** do cơ quan quản lý Trung Quốc ban hành khoảng năm 2020 dùng ba tỷ số để giới hạn đòn bẩy của nhà phát triển bất động sản.

> **Lưu ý**: Phần dưới đây dùng **bộ số giả định mô phỏng một nhà phát triển BĐS vay nợ cao** (đơn vị: tỷ NDT) để minh họa cách các tỷ số cảnh báo; **không phải số liệu báo cáo thực của Evergrande**. Bảng "D/E 7,8x", "DIO 1.200+ ngày" trong phiên bản cũ của file không có nguồn kiểm chứng nên đã được thay thế.

#### Bước 1: Số liệu giả định (tỷ NDT)

| Khoản mục | Giá trị |
|---|---|
| Tổng tài sản | 2.500 |
| Tổng nợ phải trả | 2.100 |
| Trong đó: tiền nhận trước của khách mua nhà (advance receipts) | 300 |
| Nợ vay có lãi | 700 |
| Nợ vay ngắn hạn | 360 |
| Tiền mặt | 130 |
| Vốn chủ sở hữu | 2.500 − 2.100 = 400 |
| Tài sản ngắn hạn (chủ yếu dự án dở dang) | 1.500 |
| Nợ ngắn hạn | 1.700 |
| Hàng tồn kho (dự án BĐS) | 1.300 |
| Giá vốn hàng bán | 400 |
| EBIT / Lãi vay | 120 / 160 |

#### Bước 2: Tính các tỷ số đòn bẩy và thanh khoản

$$\text{D/E} = \frac{2.100}{400} = 5{,}25 \quad\text{(cảnh báo đỏ so với ngưỡng 3.0)}$$

$$\text{Current Ratio} = \frac{1.500}{1.700} = 0{,}88 \quad\text{(< 1)}$$

$$\text{Cash Ratio} = \frac{130}{1.700} = 0{,}076 \quad\text{(rất mỏng)}$$

$$\text{ICR} = \frac{120}{160} = 0{,}75 \quad\text{(không đủ trả lãi)}$$

$$\text{DIO} = \frac{1.300}{400} \times 365 \approx 1.186 \text{ ngày} \quad\text{(hàng tồn đã "đóng băng")}$$

#### Bước 3: Kiểm tra theo "Ba lằn ranh đỏ" (diễn đạt ở mức nguyên tắc, cần đối chiếu quy định gốc)

| Lằn ranh | Quy tắc | Tính toán | Kết quả |
|---|---|---|---|
| 1 | (Nợ phải trả − tiền nhận trước)/Tài sản ≤ 70% | (2.100 − 300)/2.500 = **72,0%** | Vi phạm |
| 2 | Nợ ròng/Vốn chủ ≤ 100% | (700 − 130)/400 = **142,5%** | Vi phạm |
| 3 | Tiền/Nợ ngắn hạn ≥ 1,0 | 130/360 = **0,36** | Vi phạm |

*(Lưu ý: phiên bản cũ của file ghi lằn ranh 1 là "D/E < 1.0" — không chính xác; quy tắc đúng liên quan đến tỷ lệ nợ/tài sản đã loại trừ tiền nhận trước.)*

#### Bước 4: Diễn giải cơ chế sụp đổ

```
  Vay → Mua đất → Xây → Bán nhà trước (pre-sale) → Vay thêm
   ▲                                              │
   └──────────── Vòng lặp tăng đòn bẩy ───────────┘

  Khi chính sách siết nợ + thị trường BĐS đi xuống:
  - Không vay mới được → không trả nổi nợ cũ (thanh khoản âm)
  - Doanh thu pre-sale giảm → thiếu tiền hoàn thành dự án
  - Dự án dở dang → khách không nhận được nhà → ngừng trả góp
  - Nhà thầu/nhà cung cấp không được trả → domino
```

Kế toán nhìn vào đâu để thấy sớm? (1) Cash Ratio và Cash/Nợ ngắn hạn thấp liên tục; (2) ICR < 1 nghĩa là phải vay mới để trả lãi cũ; (3) DIO của dự án kéo dài hơn nhiều năm; (4) **tiền nhận trước của khách** được ghi là nợ (không phải doanh thu) cho đến khi bàn giao — đây là nghĩa vụ giao nhà, không thể "trả" bằng tiền khi dự án dở dang.

#### Bài học

> 1. **Không một tỷ số riêng lẻ nào cảnh báo hết** — bộ tỷ số đòn bẩy + thanh khoản + hiệu quả phải đồng thời xấu.
> 2. **ICR < 1** nghĩa là đang vay để trả lãi — "bẫy" cực nguy hiểm.
> 3. **Đòn bẩy trong ngành chu kỳ (BĐS)** khuếch đại cả hai chiều.
> 4. **"Too big to fail" không phải quy luật.**
> 5. **Cho SME**: tỷ số cảnh báo cũng đúng với doanh nghiệp nhỏ; khác biệt là SME thường không có "cơ quan quản lý đặt lằn ranh đỏ" nên phải tự đặt lằn ranh (ví dụ: ICR tối thiểu, Cash Ratio tối thiểu).

---

### 3. Case Study SME: Công ty TNHH Phân phối Thực phẩm Hải Long – "Tăng trưởng 33%, lợi nhuận tăng 33%, nhưng tiền mặt cạn" (giả định minh họa)

#### Bối cảnh

Hải Long (giả định) là nhà phân phối hàng thực phẩm khô và gia vị cho tạp hóa/siêu thị mini tại TP.HCM. Năm N-1 doanh thu 18.000 triệu VNĐ. Sang năm N, chủ doanh nghiệp mở thêm 1 tuyến giao hàng và chấp nhận bán chịu dài hơn để chiếm thị phần; doanh thu tăng lên 24.000 triệu (+33,3%), lợi nhuận ròng cũng tăng 33,3%. Chủ doanh nghiệp vui mừng, nhưng cuối năm kế toán trưởng báo "quỹ tiền mặt còn rất ít và ngân hàng nhắc hạn mức vay". Hãy dùng tỷ số để lý giải.

Đơn vị: **triệu VNĐ**; thuế TNDN giả định 20% (cần xác nhận hiện hành); dùng **số dư cuối kỳ**, 365 ngày.

#### Bước 1: Báo cáo kết quả kinh doanh

| Khoản mục | N-1 | N |
|---|---|---|
| Doanh thu thuần | 18.000 | 24.000 |
| Giá vốn hàng bán | 15.120 | 20.400 |
| **Lợi nhuận gộp** | 2.880 | 3.600 |
| Chi phí bán hàng & QLDN (gồm khấu hao 250 / 300) | 1.980 | 2.400 |
| **EBIT** | 900 | 1.200 |
| Chi phí lãi vay | 180 | 240 |
| **Lợi nhuận trước thuế** | 720 | 960 |
| Thuế TNDN (20%) | 144 | 192 |
| **Lợi nhuận sau thuế** | 576 | 768 |

#### Bước 2: Bảng cân đối kế toán

| Khoản mục | N-1 | N |
|---|---|---|
| Tiền mặt | 900 | 268 |
| Phải thu khách hàng | 1.800 | 2.900 |
| Hàng tồn kho | 1.700 | 2.600 |
| Tài sản ngắn hạn khác | 100 | 100 |
| **Tài sản ngắn hạn** | **4.500** | **5.868** |
| TSCĐ ròng | 2.000 | 2.400 |
| **TỔNG TÀI SẢN** | **6.500** | **8.268** |
| Phải trả nhà cung cấp | 1.100 | 1.500 |
| Vay ngắn hạn | 700 | 1.600 |
| Nợ ngắn hạn khác | 300 | 400 |
| **Nợ ngắn hạn** | **2.100** | **3.500** |
| Vay dài hạn | 1.400 | 1.200 |
| **Nợ phải trả** | **3.500** | **4.700** |
| Vốn góp | 2.000 | 2.000 |
| Lợi nhuận chưa phân phối | 1.000 | 1.568 |
| **Vốn chủ sở hữu** | **3.000** | **3.568** |
| **TỔNG NGUỒN VỐN** | **6.500** | **8.268** |

**Kiểm tra cân đối**: N-1: 3.500 + 3.000 = 6.500 ✓. N: 4.700 + 3.568 = 8.268 ✓. Lợi nhuận chưa phân phối N = 1.000 + 768 − cổ tức 200 = 1.568 ✓. TSCĐ ròng N = 2.000 + đầu tư mới 700 − khấu hao 300 = 2.400 ✓.

#### Bước 3: Báo cáo lưu chuyển tiền tệ (phương pháp gián tiếp, năm N)

| Khoản mục | Số tiền |
|---|---|
| Lợi nhuận sau thuế | 768 |
| + Khấu hao | 300 |
| − Tăng phải thu (2.900 − 1.800) | −1.100 |
| − Tăng hàng tồn kho (2.600 − 1.700) | −900 |
| + Tăng phải trả nhà cung cấp (1.500 − 1.100) | +400 |
| + Tăng nợ ngắn hạn khác (400 − 300) | +100 |
| **Lưu chuyển tiền thuần từ HĐKD (CFO)** | **−432** |
| Chi mua TSCĐ | −700 |
| **Lưu chuyển tiền thuần từ đầu tư (CFI)** | **−700** |
| Tăng vay ngắn hạn (1.600 − 700) | +900 |
| Trả bớt vay dài hạn (1.200 − 1.400) | −200 |
| Chi trả cổ tức | −200 |
| **Lưu chuyển tiền thuần từ tài chính (CFF)** | **+500** |
| **Tăng/giảm tiền thuần** | −432 − 700 + 500 = **−632** |
| Tiền đầu kỳ | 900 |
| **Tiền cuối kỳ** | 900 − 632 = **268** ✓ (khớp bảng cân đối) |

*(Quy ước: chi phí lãi vay đã nằm trong lợi nhuận nên nằm trong CFO; VAS cho phép trình bày lãi vay đã trả ở CFO hoặc CFF tùy chính sách — cần xác nhận hiện hành.)*

#### Bước 4: Tính toàn bộ tỷ số

**Nhóm Thanh khoản**

| Tỷ số | Công thức | N-1 | N |
|---|---|---|---|
| Current Ratio | 4.500/2.100 ; 5.868/3.500 | **2,14** | **1,68** |
| Quick Ratio | (900+1.800)/2.100 ; (268+2.900)/3.500 | **1,29** | **0,91** |
| Cash Ratio | 900/2.100 ; 268/3.500 | **0,43** | **0,08** |

**Nhóm Hiệu quả**

| Tỷ số | Công thức (ngày) | N-1 | N |
|---|---|---|---|
| DIO | 1.700/15.120×365 ; 2.600/20.400×365 | **41,0** | **46,5** |
| DSO | 1.800/18.000×365 ; 2.900/24.000×365 | **36,5** | **44,1** |
| DPO | 1.100/15.120×365 ; 1.500/20.400×365 | **26,6** | **26,8** |
| **CCC** | DIO + DSO − DPO | **51,0** | **63,8** |
| Asset Turnover | 18.000/6.500 ; 24.000/8.268 | **2,77** | **2,90** |

**Nhóm Đòn bẩy**

| Tỷ số | Công thức | N-1 | N |
|---|---|---|---|
| D/E | 3.500/3.000 ; 4.700/3.568 | **1,17** | **1,32** |
| Debt Ratio | 3.500/6.500 ; 4.700/8.268 | **53,8%** | **56,8%** |
| ICR | 900/180 ; 1.200/240 | **5,0x** | **5,0x** |
| Equity Multiplier | 6.500/3.000 ; 8.268/3.568 | **2,17** | **2,32** |

**Nhóm Lợi nhuận**

| Tỷ số | Công thức | N-1 | N |
|---|---|---|---|
| Gross Margin | 2.880/18.000 ; 3.600/24.000 | **16,0%** | **15,0%** |
| Operating Margin | 900/18.000 ; 1.200/24.000 | **5,0%** | **5,0%** |
| Net Margin | 576/18.000 ; 768/24.000 | **3,2%** | **3,2%** |
| ROA | 576/6.500 ; 768/8.268 | **8,9%** | **9,3%** |
| ROE | 576/3.000 ; 768/3.568 | **19,2%** | **21,5%** |

#### Bước 5: DuPont 3 và 5 thành phần cho năm N

$$\text{ROE}_N = 3{,}2\% \times 2{,}90 \times 2{,}32 \approx 21{,}5\% \quad\text{(N-1: } 3{,}2\% \times 2{,}77 \times 2{,}17 \approx 19{,}2\%)$$

$$\text{DuPont 5}: \quad 0{,}8 \times 0{,}8 \times 5{,}0\% \times 2{,}90 \times 2{,}32 \approx 21{,}5\%$$

Trong đó Tax Burden = 768/960 = 0,8; Interest Burden = 960/1.200 = 0,8. **Diễn giải**: ROE tăng từ 19,2% lên 21,5% (+2,3 điểm %) nhưng Net Margin **không đổi** (3,2%) và Operating Margin không đổi. ROE tăng nhờ hai thứ: Asset Turnover nhích lên (2,77 → 2,90) và **Equity Multiplier tăng (2,17 → 2,32) — tức đòn bẩy**. Biên gộp thực ra **giảm** (16,0% → 15,0%): để tăng doanh số, công ty đã nhường giá/chiết khấu.

#### Bước 6: Chẩn đoán — chuyện gì thực sự đã xảy ra?

1. **Tăng trưởng đã "nuốt" tiền**: Phải thu +61,1% (1.800 → 2.900), tồn kho +52,9% (1.700 → 2.600), trong khi doanh thu chỉ +33,3% và phải trả NCC +36,4%. Vốn lưu động hoạt động (Phải thu + Tồn kho − Phải trả) tăng từ 1.800 + 1.700 − 1.100 = **2.400** lên 2.900 + 2.600 − 1.500 = **4.000** (+1.600).
2. **CCC kéo dài 12,8 ngày** (51,0 → 63,8): DSO +7,6 ngày (nới bán chịu), DIO +5,5 ngày (tồn kho dày để không đứt hàng).
3. **Lợi nhuận kế toán 768 nhưng CFO = −432**: chênh lệch 1.200 chủ yếu do vốn lưu động. Dòng tiền tự do (CFO + CFI) = −432 − 700 = **−1.132**, được bù bằng vay ngắn hạn thêm 900 và tiêu hết 632 tiền mặt.
4. **Cơ cấu nợ xấu đi**: vay ngắn hạn 700 → 1.600 để tài trợ tài sản (vốn lưu động và đầu tư TSCĐ 700 — **vay ngắn hạn để đầu tư dài hạn** là sai nguyên tắc "khớp kỳ hạn"). Cash Ratio 0,43 → 0,08; Quick Ratio xuống dưới 1,0.
5. **ICR 5,0x vẫn "đẹp"** — lý do chủ doanh nghiệp chưa thấy báo động. Nhưng ICR chỉ đo lãi trên lợi nhuận kế toán, không đo khả năng trả **gốc** (1.600 vay ngắn hạn sắp đáo hạn) bằng tiền.

#### Bước 7: Khuyến nghị hành động và lượng hóa

Doanh thu bình quân/ngày = 24.000/365 ≈ 65,75; giá vốn bình quân/ngày = 20.400/365 ≈ 55,89 (triệu).

| Hành động | Mục tiêu | Tiền giải phóng ước tính |
|---|---|---|
| Siết thu hồi công nợ, đưa DSO về 36,5 ngày (mức N-1) | −7,6 ngày | 65,75 × 7,6 ≈ **500** |
| Giảm tồn kho dư thừa (SKU chậm), đưa DIO về 41,0 ngày | −5,5 ngày | 55,89 × 5,5 ≈ **306** |
| Thương lượng DPO lên 35 ngày (đổi lại thanh toán đúng hẹn) | +8,2 ngày | 55,89 × 8,2 ≈ **456** |
| **Tổng** | CCC còn 36,5 + 41,0 − 35,0 = **42,5 ngày** | ≈ **1.263** |

Số tiền giải phóng ≈ 1.263 đủ để trả bớt vay ngắn hạn 900 bổ sung năm N và khôi phục đệm tiền mặt. Đồng thời: chuyển phần vay ngắn hạn tài trợ TSCĐ sang vay trung/dài hạn; đặt chính sách tín dụng khách hàng (hạn mức, chiết khấu thanh toán sớm, phạt chậm); lập dự báo dòng tiền 13 tuần.

#### Bài học

> 1. **Lợi nhuận tăng ≠ tiền tăng**: tăng trưởng nhanh cần vốn lưu động; phải đọc song song CFO.
> 2. **ROE tăng không phải lúc nào cũng tốt** — ở đây ROE tăng nhờ đòn bẩy, không nhờ biên lợi nhuận.
> 3. **ICR đẹp nhưng Cash Ratio gần 0** — một tỷ số tốt không bù được một tỷ số xấu ở nhóm khác.
> 4. **CCC là kim chỉ nam cho doanh nghiệp phân phối**; mỗi ngày CCC = một lượng tiền cụ thể.
> 5. **Giữ nhất quán giữa kế toán và quản trị**: chỉ cần kế toán lập BCTC tháng đúng hạn, chủ doanh nghiệp đã thấy cảnh báo này sớm hơn nhiều.

---

## IV. ỨNG DỤNG CHO SME

### 1. Top 10 tỷ số SME cần theo dõi

| # | Tỷ số | Vì sao quan trọng | Tần suất kiểm tra |
|---|-------|-------------------|----------------|
| 1 | **Gross Margin** | Sản phẩm/giá bán còn đủ "ăn" không? | Tháng |
| 2 | **Net Margin** | Cuối cùng giữ lại bao nhiêu? | Tháng |
| 3 | **Current Ratio & Quick Ratio** | Có trả được nợ ngắn hạn không? | Tháng |
| 4 | **CCC (DIO + DSO − DPO)** | Tiền quay vòng nhanh không? | Quý (tháng với phân phối/bán lẻ) |
| 5 | **D/E Ratio** | Nợ có quá nhiều không? | Quý |
| 6 | **Burn Rate & Runway** | Bao lâu nữa hết tiền? (startup) | Tuần/Tháng |
| 7 | **Revenue Growth** | Đang tăng trưởng không? Có đi kèm tăng vốn lưu động không? | Tháng |
| 8 | **DSO** | Khách trả tiền nhanh không? | Tháng |
| 9 | **ROE** (kèm DuPont) | Có xứng đáng vốn chủ bỏ ra? | Quý |
| 10 | **Operating Margin & ICR** | Hoạt động cốt lõi hiệu quả? Có đủ trả lãi? | Tháng/Quý |

### 2. Dashboard tỷ số mẫu

```
┌──────────────────────────────────────────────────────┐
│     FINANCIAL HEALTH DASHBOARD – THÁNG XX/20XX       │
│     Công ty: _______________                         │
│                                                      │
│  PROFITABILITY           │  LIQUIDITY                │
│  Gross Margin:  ___%     │  Current Ratio:  ___      │
│  Net Margin:    ___%     │  Quick Ratio:    ___      │
│  ROE:           ___%     │  Cash Ratio:     ___      │
│  ROA:           ___%     │                           │
│                          │  LEVERAGE                 │
│  EFFICIENCY              │  D/E Ratio:      ___      │
│  Inv Turnover:  ___x     │  Interest Cov:   ___x     │
│  DSO:           ___ days │                           │
│  DPO:           ___ days │  GROWTH                   │
│  CCC:           ___ days │  Revenue Growth:  ___% YoY│
│  Asset Turnover: ___x    │  Profit Growth:   ___% YoY│
│                                                      │
│  XANH = Tốt   VÀNG = Theo dõi   ĐỎ = Cần hành động   │
└──────────────────────────────────────────────────────┘
```

### 3. Quy trình để tỷ số đáng tin trong SME (góc nhìn kế toán)

| Bước | Việc cần làm | Tại sao |
|---|---|---|
| 1 | Đóng sổ tháng đúng hạn, đối chiếu công nợ, kiểm kê kho định kỳ | Tỷ số sai nếu sổ sai |
| 2 | Cắt kỳ đúng (ghi nhận doanh thu/chi phí đúng kỳ) | Tránh méo DSO/Margin |
| 3 | Trích lập dự phòng theo quy định khi có cơ sở (cần xác nhận hiện hành) | Tránh AR/HTK bị thổi phồng |
| 4 | Ghi rõ chính sách kế toán và giữ nhất quán | Để so sánh kỳ này với kỳ trước |
| 5 | Dùng số **quản trị** (tháng) bên cạnh BCTC thuế | Số thuế phục vụ tuân thủ, số quản trị phục vụ ra quyết định |

### 4. Benchmark tham khảo cho một số loại hình SME (ước lượng, cần đối chiếu số liệu ngành thực tế)

| Loại hình | Gross Margin | Net Margin | CCC điển hình | Lưu ý |
|---|---|---|---|---|
| Quán cà phê/F&B | 60-70% | 5-12% | Gần 0 hoặc âm (thu tiền ngay, trả NCC chịu) | Khảo hạn thuê mặt bằng, khấu hao |
| Bán lẻ | 25-40% | 2-6% | 30-60 ngày | Tồn kho là rủi ro chính |
| Phân phối | 10-20% | 1-4% | 40-80 ngày | Công nợ và vốn lưu động quyết định |
| Dịch vụ/Agency | 40-70% | 10-20% | 30-60 ngày | DSO quan trọng |
| Sản xuất nhỏ | 20-35% | 3-8% | 60-120 ngày | Cả HTK và công nợ |

### 5. Sai lầm thường gặp

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| Chỉ nhìn một tỷ số (thường là lợi nhuận) | Bỏ sót rủi ro tiền mặt | Xem đủ 4 nhóm + CFO |
| So sánh với ngành khác | Kết luận sai | Chỉ benchmark cùng ngành/quy mô |
| Dùng số một thời điểm cuối năm | Bị ảnh hưởng mùa vụ/window dressing | Dùng bình quân, xem xu hướng |
| Bỏ qua chính sách kế toán khác nhau | So sánh khập khiễng | Đọc thuyết minh |
| Không ghi rõ công thức | Mỗi người tính mỗi kiểu | Chuẩn hóa công thức trong 1 file |
| Tin ICR mà bỏ quên trả gốc | Vỡ nợ vì gốc đến hạn | Thêm DSCR/lịch trả nợ |
| Tối ưu ROE bằng vay thêm | Rủi ro tăng | Xem DuPont, luôn kèm ICR/Cash Ratio |

### 6. Tần suất & phân công

| Việc | Ai làm | Tần suất |
|---|---|---|
| Nhập liệu, đóng sổ | Kế toán | Hàng ngày/tháng |
| Tính bộ tỷ số cốt lõi (dashboard) | Kế toán trưởng/kế toán tổng hợp | Tháng |
| Phân tích DuPont, so sánh ngành, kiến nghị | Chủ DN + kế toán trưởng | Quý |
| Soát xét độc lập | Kiểm toán/tư vấn thuế (nếu cần) | Năm |

---

## V. TOOLS & TEMPLATES

### 1. Phần mềm kế toán/quản lý hỗ trợ tính tỷ số cho SME Việt Nam

| Phần mềm | Chi phí tham khảo (ước tính, cần xác nhận với nhà cung cấp) | Phù hợp |
|---|---|---|
| **Excel / Google Sheets** | Miễn phí (Google) / có sẵn (Excel) | SME rất nhỏ, linh hoạt, tự dựng dashboard |
| **MISA SME / MISA AMIS Kế toán** | ~3-8 triệu VNĐ/năm (ước tính) | SME cần tuân thủ chuẩn mực VN, xuất BCTC & báo cáo thuế |
| **Fast Accounting** | ~5-10 triệu VNĐ/năm (ước tính) | Giao dịch nhiều, quản lý kho/công nợ chi tiết |
| **KiotViet** | ~3-6 triệu VNĐ/năm tùy gói (ước tính) | Bán lẻ/F&B; theo dõi tồn kho, doanh thu, công nợ cơ bản |
| **Sapo** | ~4-10 triệu VNĐ/năm tùy gói (ước tính) | Bán lẻ đa kênh, quản lý đơn hàng |
| **Looker Studio / Power BI Desktop** | Miễn phí hoặc chi phí thấp (cần xác nhận) | Dựng dashboard trực quan từ Google Sheets/Excel |

Danh mục đầy đủ công cụ theo loại hình xem [`cong-cu-quan-tri-doanh-nghiep-sme.md`](../cong-cu-quan-tri-doanh-nghiep-sme.md).

**Lưu ý chọn công cụ**: Phần mềm kế toán xuất được BCTC nhưng thường không tính sẵn bộ tỷ số — chủ SME nên xuất bảng cân đối/KQKD hàng tháng ra Excel rồi dùng template dưới đây. Ưu tiên phần mềm cho phép xuất theo chuẩn mẫu biểu VAS.

### 2. Template Excel/Google Sheets tính tỷ số hàng tháng

```
TAB 1 — INPUT_BS (Bảng cân đối): cột Tháng 1..12
  Hàng: Tiền (mã 110), Phải thu (130), Tồn kho (140), TS ngắn hạn (100),
        Tổng tài sản (270), Nợ ngắn hạn (310), Nợ phải trả (300),
        Vốn chủ (400), Phải trả NCC
TAB 2 — INPUT_PL (KQKD): cột Tháng 1..12
  Hàng: Doanh thu thuần, Giá vốn, Lợi nhuận gộp, Chi phí lãi vay,
        EBT (mã 50), LNST (mã 60), Khấu hao
TAB 3 — RATIOS: công thức tự động
TAB 4 — DASHBOARD: biểu đồ xu hướng + tô màu cảnh báo
TAB 5 — NOTES: ghi chính sách kế toán, thay đổi bất thường
```

**Công thức Excel mẫu** (giả sử BS ở `INPUT_BS`, PL ở `INPUT_PL`, cột C = tháng hiện tại):

| Tỷ số | Công thức Excel |
|---|---|
| Current Ratio | `=INPUT_BS!C4/INPUT_BS!C6` (TS ngắn hạn / Nợ ngắn hạn) |
| Quick Ratio | `=(INPUT_BS!C2+INPUT_BS!C3)/INPUT_BS!C6` |
| DSO (số liệu tháng, quy đổi theo 30 ngày) | `=INPUT_BS!C3/INPUT_PL!C2*30` |
| DIO | `=INPUT_BS!C4/INPUT_PL!C3*30` |
| CCC | `=DSO+DIO-DPO` |
| D/E | `=INPUT_BS!C7/INPUT_BS!C8` |
| ROE (quy năm hóa tháng) | `=INPUT_PL!C7*12/INPUT_BS!C8` |
| Cảnh báo | `=IF(C10<1,"ĐỎ",IF(C10<1.5,"VÀNG","XANH"))` |

*(Các ô tham chiếu chỉ minh họa; nên dùng tên vùng (named range) để tránh sai khi chèn hàng. Với số liệu tháng, tính DSO/DIO bằng doanh thu/giá vốn tháng nhân 30, hoặc dùng luỹ kế 12 tháng gần nhất × 365 để tránh biến động mùa vụ.)*

---

## VI. BÀI TẬP THỰC HÀNH

### Bài 1 (Cơ bản — Tính tỷ số đơn lẻ)
Một cửa hàng có tài sản ngắn hạn = 450 triệu, hàng tồn kho = 200 triệu, nợ ngắn hạn = 300 triệu. Tính Current Ratio và Quick Ratio, nhận xét.

> *Gợi ý đáp số*: CR = 450/300 = 1,5; QR = (450 − 200)/300 = 0,83. CR ở mức tốt nhưng QR dưới 1 → thanh khoản phụ thuộc vào bán hết tồn kho.

### Bài 2 (Cơ bản — Hiểu bản chất công thức)
Giải thích bằng lời của bạn: (a) Tại sao Quick Ratio loại hàng tồn kho? (b) Tại sao ICR dùng EBIT thay vì lợi nhuận ròng? (c) Tại sao Inventory Turnover dùng giá vốn thay vì doanh thu?

> *Gợi ý*: (a) HTK khó chuyển thành tiền nhất, giá sổ sách là giá gốc; (b) lãi vay được trả từ lợi nhuận trước lãi và thuế; (c) cùng cơ sở giá gốc với giá trị tồn kho.

### Bài 3 (Trung bình — DuPont)
Công ty có Net Margin 4%, Asset Turnover 2,5x, Tổng tài sản 2.000 triệu, Vốn chủ 1.000 triệu. Tính Equity Multiplier, Doanh thu, Lợi nhuận ròng, ROE.

> *Gợi ý đáp số*: EM = 2.000/1.000 = 2,0; Doanh thu = 2,5 × 2.000 = 5.000; NI = 4% × 5.000 = 200; ROE = 4% × 2,5 × 2,0 = 20% (kiểm tra: 200/1.000 = 20%).

### Bài 4 (Trung bình — Cash Conversion Cycle)
DN phân phối có DIO = 45, DSO = 30, DPO = 20 ngày; giá vốn 7.300 triệu/năm. Tính CCC. Nếu thương lượng DPO lên 50 ngày, CCC mới là bao nhiêu và giải phóng bao nhiêu tiền?

> *Gợi ý đáp số*: CCC = 45 + 30 − 20 = 55 ngày. DPO = 50 → CCC = 25 ngày (giảm 30 ngày). Giá vốn/ngày = 7.300/365 = 20 triệu → giải phóng ≈ 30 × 20 = 600 triệu.

### Bài 5 (Trung bình — Chính sách kế toán)
Dùng dữ liệu mục II.F nhưng giả định giá nhập thứ hai giảm xuống 8/sp (tồn đầu 100 sp × 10; nhập 100 sp × 8; bán 120 sp × 20). Tính giá vốn, Gross Margin theo FIFO và bình quân gia quyền. Chính sách nào cho biên gộp cao hơn khi giá giảm?

> *Gợi ý đáp số*: FIFO: giá vốn = 100×10 + 20×8 = 1.160; lợi nhuận gộp = 2.400 − 1.160 = 1.240; Gross Margin = 51,7%. Bình quân: đơn giá = (1.000 + 800)/200 = 9; giá vốn = 120 × 9 = 1.080; lợi nhuận gộp = 1.320; Gross Margin = 55,0%. Khi giá giảm, bình quân gia quyền cho biên gộp cao hơn (ngược chiều so với khi giá tăng).

### Bài 6 (Nâng cao — Phát hiện red flags)
Công ty Y (giả định, tỷ VNĐ):

| Chỉ tiêu | Năm 1 | Năm 2 | Năm 3 |
|---|---|---|---|
| Doanh thu | 100 | 130 | 170 |
| Lợi nhuận ròng | 10 | 15 | 22 |
| Dòng tiền từ HĐKD (CFO) | 9 | 8 | 3 |
| Phải thu (AR) | 15 | 28 | 55 |
| Hàng tồn kho | 10 | 12 | 14 |

Yêu cầu: (a) Tính tăng trưởng Doanh thu, Lợi nhuận, AR; (b) DSO và tỷ lệ CFO/Lợi nhuận mỗi năm; (c) Chỉ ra red flag nghiêm trọng nhất và giả thuyết.

> *Gợi ý đáp số*: (a) Doanh thu +30,0% rồi +30,8%; Lợi nhuận +50,0% rồi +46,7%; AR +86,7% rồi +96,4%. (b) DSO = AR/Doanh thu × 365: 54,8 → 78,6 → 118,1 ngày. CFO/LNST = 0,90 → 0,53 → 0,14. (c) Red flag lớn nhất: AR tăng nhanh gấp 2-3 lần doanh thu, DSO tăng gấp đôi và CFO tụt khi lợi nhuận tăng → khả năng bán chịu mạnh/ghi nhận doanh thu sớm; cần rà soát cut-off, dự phòng phải thu, đối chiếu công nợ.

### Bài 7 (Nâng cao — Đòn bẩy)
Công ty có EBIT = 600 triệu, lãi vay = 400 triệu. Tính ICR. Nếu EBIT giảm 30% thì ICR bằng bao nhiêu? Nhận xét.

> *Gợi ý đáp số*: ICR = 600/400 = 1,5. EBIT mới = 420 → ICR = 420/400 = 1,05. Chỉ giảm 30% EBIT là gần như không đủ trả lãi → rất nhạy cảm.

### Bài 8 (Nâng cao — Case SME)
Với dữ liệu Hải Long (mục III.3): (a) Tính Net Working Capital (TS ngắn hạn − Nợ ngắn hạn) hai năm; (b) Giải thích vì sao NWC gần như không đổi nhưng thanh khoản xấu đi rõ rệt; (c) Đề xuất 3 hành động.

> *Gợi ý đáp số*: (a) N-1: 4.500 − 2.100 = 2.400; N: 5.868 − 3.500 = 2.368. (b) NWC gần như giữ nguyên nhưng cấu trúc đổi: tiền giảm từ 900 xuống 268, phải thu/tồn kho tăng (khó chuyển thành tiền hơn), nợ vay ngắn hạn tăng → Quick/Cash Ratio giảm mạnh. (c) Siết DSO, giảm tồn kho chậm, vay dài hạn thay vay ngắn hạn cho đầu tư TSCĐ.

### Bài 9 (Thực hành thực tế)
Lấy BCTC (hoặc số liệu quản trị) của chính doanh nghiệp bạn 2 năm liên tiếp. Làm đủ các bước như mục III.3: kiểm tra cân đối, lập Cash Flow gián tiếp, tính 4 nhóm tỷ số, DuPont, rà soát red flags, viết 3 hành động cho quý tới. Nêu rõ chính sách kế toán đang dùng.

---

## PHỤ LỤC: CHECKLIST TỶ SỐ TÀI CHÍNH TỔNG HỢP

### 1. Checklist trước khi tính tỷ số (độ tin cậy số liệu)

```
□ Bảng cân đối kế toán đã cân (Tài sản = Nguồn vốn)?
□ Lợi nhuận sau thuế khớp giữa KQKD và Vốn chủ (lợi nhuận chưa phân phối)?
□ Tiền cuối kỳ trên LCTT khớp với tiền trên Bảng cân đối?
□ Công nợ phải thu/phải trả đã đối chiếu với đối tác?
□ Hàng tồn kho đã kiểm kê và so với sổ?
□ Đã trích lập dự phòng cần thiết (phải thu khó đòi, giảm giá HTK) theo quy định hiện hành?
□ Doanh thu/chi phí ghi nhận đúng kỳ (cut-off)?
□ Chính sách kế toán (giá xuất kho, khấu hao) nhất quán so với kỳ trước? Có thay đổi thì đã thuyết minh?
□ Số liệu có thể so sánh với kỳ trước/đối thủ (cùng đơn vị, cùng định nghĩa)?
```

### 2. Checklist phân tích tỷ số

```
□ Đã tính đủ 4 nhóm: Liquidity, Efficiency, Leverage, Profitability?
□ So sánh YoY (cùng kỳ năm trước) và MoM/QoQ (kỳ trước)?
□ Benchmark với ngành (nếu có dữ liệu), cùng quy mô?
□ Đã phân rã DuPont để biết ROE đến từ đâu (margin/vòng quay/đòn bẩy)?
□ Đã tính CCC và quy đổi ra số tiền giải phóng được?
□ Đã đối chiếu CFO với Lợi nhuận ròng?
□ Đã check red flags (DSO, DIO, Current Ratio, ICR, Cash Ratio)?
□ Đã kiểm tra ảnh hưởng của chính sách kế toán (FIFO/BQGQ, khấu hao, dự phòng)?
□ Có cân nhắc nợ ngoài bảng (thuê dài hạn, bảo lãnh)?
□ Ghi action items cho tỷ số xấu, có chủ trách nhiệm và hạn?
□ Cập nhật dự báo dòng tiền nếu xu hướng thay đổi?
```

### 3. Công thức tổng hợp

| Nhóm | Tỷ số | Công thức |
|---|---|---|
| **Liquidity** | Current Ratio | $\frac{\text{CA}}{\text{CL}}$ |
| | Quick Ratio | $\frac{\text{CA} - \text{Inventory}}{\text{CL}}$ |
| | Cash Ratio | $\frac{\text{Cash}}{\text{CL}}$ |
| **Efficiency** | Inventory Turnover / DIO | $\frac{\text{COGS}}{\text{Avg Inv}}$ ; $\frac{365}{\text{Turnover}}$ |
| | AR Turnover / DSO | $\frac{\text{Net Credit Sales}}{\text{Avg AR}}$ ; $\frac{365}{\text{Turnover}}$ |
| | AP Turnover / DPO | $\frac{\text{COGS (hoặc Purchases)}}{\text{Avg AP}}$ ; $\frac{365}{\text{Turnover}}$ |
| | CCC | $\text{DIO} + \text{DSO} - \text{DPO}$ |
| | Asset Turnover | $\frac{\text{Revenue}}{\text{Avg Total Assets}}$ |
| **Leverage** | D/E | $\frac{\text{Total Liabilities}}{\text{Equity}}$ |
| | Debt Ratio | $\frac{\text{Total Liabilities}}{\text{Total Assets}}$ |
| | ICR | $\frac{\text{EBIT}}{\text{Interest}}$ |
| | Equity Multiplier | $\frac{\text{Total Assets}}{\text{Equity}} = 1 + \text{D/E}$ |
| | DSCR | $\frac{\text{Dòng tiền khả dụng trả nợ}}{\text{Gốc + Lãi}}$ |
| **Profitability** | Gross Margin | $\frac{\text{Revenue} - \text{COGS}}{\text{Revenue}}$ |
| | Operating Margin | $\frac{\text{EBIT}}{\text{Revenue}}$ |
| | EBITDA Margin | $\frac{\text{EBIT} + \text{D\&A}}{\text{Revenue}}$ |
| | Net Margin | $\frac{\text{NI}}{\text{Revenue}}$ |
| | ROE | $\frac{\text{NI}}{\text{Avg Equity}}$ |
| | ROA | $\frac{\text{NI}}{\text{Avg Total Assets}}$ |
| **DuPont 3** | ROE | $\text{Net Margin} \times \text{Asset Turnover} \times \text{Equity Multiplier}$ |
| **DuPont 5** | ROE | $\text{Tax Burden} \times \text{Interest Burden} \times \text{Op. Margin} \times \text{AT} \times \text{EM}$ |
| **Startup** | Runway | $\frac{\text{Tiền mặt}}{\text{Burn Rate/tháng}}$ |

### 4. Lưu ý pháp lý/chuẩn mực (cần xác nhận hiện hành)

```
□ Chế độ kế toán áp dụng (Thông tư 200/2014/TT-BTC hay chế độ cho DN nhỏ và siêu nhỏ) — cần xác nhận hiện hành
□ Mẫu biểu BCTC và mã số theo chế độ đang áp dụng — cần đối chiếu
□ Thuế suất TNDN và các quy định khấu trừ chi phí (ví dụ trần chi phí lãi vay) — cần xác nhận hiện hành
□ Nếu gọi vốn nước ngoài/niêm yết: chuẩn bị đối chiếu VAS ↔ IFRS (thuê tài sản, ghi nhận doanh thu, công cụ tài chính)
```

---

*Tài liệu tham khảo: Brealey, Myers & Allen – "Principles of Corporate Finance"; Palepu, Healy & Peek – "Business Analysis & Valuation"; Damodaran – "The Little Book of Valuation" và dữ liệu ngành NYU; CFA Institute – Level I: Financial Reporting and Analysis; Kieso, Weygandt – "Intermediate Accounting"; McKinsey – "Valuation"; Thông tư 200/2014/TT-BTC và VAS (cần đối chiếu văn bản hiện hành)*
