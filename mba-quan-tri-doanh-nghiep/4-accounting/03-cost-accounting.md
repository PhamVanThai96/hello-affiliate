# Cost Accounting – Kế Toán Chi Phí (ABC, Job Costing, Process Costing)

> **Mục tiêu**: Hiểu rõ **bản chất** và cách vận hành của 3 phương pháp tính giá thành sản phẩm/dịch vụ: Job Order Costing, Process Costing và Activity-Based Costing (ABC) — vì sao chúng ra đời, tính toán từng bước như thế nào, so sánh ưu nhược điểm và ứng dụng cho SME Việt Nam (kèm cách hạch toán theo chế độ kế toán VN, công cụ và giá tham khảo).

---

## I. KHÁI NIỆM & LÝ THUYẾT

### 1. Định nghĩa

**Cost Accounting (Kế toán chi phí)** là nhánh kế toán chuyên về **đo lường, tập hợp, phân bổ và phân tích chi phí** vào sản phẩm, dịch vụ, dự án hoặc bộ phận. Mục tiêu cuối cùng: **biết chính xác mỗi sản phẩm/đơn hàng/khách hàng tốn bao nhiêu tiền** để định giá, kiểm soát chi phí và ra quyết định.

> **"You can't manage what you can't measure."** – thường được gán cho Peter Drucker (cần đối chiếu nguồn trích dẫn gốc).

Hai chữ "giá thành" (Product Cost / Cost of Goods Manufactured) trong tiếng Việt chính là sản phẩm của kế toán chi phí: tổng chi phí sản xuất đã tập hợp được chia cho số lượng sản phẩm hoàn thành.

### 2. Tại sao Kế toán chi phí xuất hiện? — Bối cảnh lịch sử

Kế toán tài chính (Financial Accounting) chỉ cần trả lời cho cơ quan thuế, ngân hàng, cổ đông: "Cả công ty năm nay lãi bao nhiêu?". Nhưng để quản trị, chủ doanh nghiệp cần câu hỏi chi tiết hơn: *"Sản phẩm nào lãi? Đơn hàng nào lỗ? Khách hàng nào đáng giữ?"*. Lịch sử của môn này là lịch sử của việc trả lời ngày càng chính xác những câu hỏi đó:

| Giai đoạn | Bối cảnh | Đóng góp |
|-----------|---------|---------|
| Cuối thế kỷ 18 – 19 (Cách mạng công nghiệp) | Nhà máy thay xưởng thủ công, lần đầu có chi phí cố định lớn (máy móc, nhà xưởng) | Hình thành việc tập hợp chi phí nhân công, nguyên liệu vào sản phẩm (ví dụ các xưởng gốm, dệt, đường sắt ở Anh – Mỹ) |
| Đầu thế kỷ 20 | Sản xuất hàng loạt (Ford, Taylor – quản trị khoa học), sản phẩm đồng nhất | Phát triển **Process Costing** và **Standard Costing** (chi phí tiêu chuẩn) |
| 1920s | DuPont, General Motors cần đo hiệu quả đầu tư theo từng bộ phận | Chi phí gắn với trách nhiệm quản lý và đo lường lợi nhuận |
| 1980s | Tự động hóa tăng mạnh, nhân công trực tiếp chỉ còn 5–10% giá thành, **chi phí gián tiếp (overhead) phình to** | Phương pháp phân bổ overhead theo giờ lao động trở nên sai lệch — Johnson & Kaplan xuất bản *"Relevance Lost: The Rise and Fall of Management Accounting"* (1987) |
| 1988 – 1992 | Cooper & Kaplan phát triển **Activity-Based Costing (ABC)** dựa trên khảo sát các nhà máy Mỹ | ABC ra đời để sửa sai lệch phân bổ overhead |
| 2004 | ABC truyền thống quá tốn công khảo sát | Kaplan & Anderson đề xuất **Time-Driven ABC (TDABC)** |

**Ý nghĩa**: mỗi phương pháp dưới đây là một "lời giải" cho một loại hình sản xuất khác nhau; không có phương pháp nào "tốt nhất" tuyệt đối.

### 3. Tại sao Cost Accounting quan trọng?

| Lý do | Giải thích | Ví dụ |
|-------|-----------|-------|
| **Pricing** (Định giá) | Biết chi phí → định giá hợp lý, biết giá sàn không lỗ | Chi phí 100k → bán 150k (biên 33%) |
| **Profitability** (Lợi nhuận) | Biết sản phẩm/khách hàng nào lãi/lỗ thực sự | SP A lãi 30%, SP B lỗ 5% |
| **Cost Control** (Kiểm soát) | Phát hiện chi phí bất thường | Chi phí NVL tăng 20% → điều tra |
| **Decision Making** (Ra quyết định) | Make-or-Buy, nhận/từ chối đơn đặc biệt, bỏ/giữ sản phẩm | Thuê ngoài nếu chi phí nội bộ cao hơn |
| **Budgeting** (Ngân sách) | Lập ngân sách chính xác | Dự án mới cần bao nhiêu vốn? |
| **Tuân thủ báo cáo** | Giá trị hàng tồn kho & giá vốn trên BCTC phải được xác định theo chuẩn mực | Giá gốc hàng tồn kho (VAS 02) |

### 4. Phân loại chi phí — "bảng chữ cái" của Cost Accounting

Trước khi học các phương pháp, phải thuần thục cách phân loại chi phí, vì mỗi phương pháp chỉ khác nhau ở cách **gom** và **phân bổ** các loại chi phí này.

#### 4.1 Theo chức năng (cách VN dùng cho giá thành)

| Loại chi phí | Tên Anh | Giải thích | TK tham chiếu (TT 200) |
|--------------|---------|-----------|-----------------------|
| NVL trực tiếp | Direct Materials (DM) | Vật liệu cấu thành thực thể sản phẩm, truy nguyên được | 621 |
| Nhân công trực tiếp | Direct Labor (DL) | Lương công nhân trực tiếp làm ra sản phẩm | 622 |
| Chi phí sản xuất chung | Manufacturing Overhead (MOH) | Mọi chi phí sản xuất còn lại: lương quản đốc, khấu hao máy, điện nước xưởng, bảo trì… | 627 |
| Chi phí bán hàng | Selling Expense | Phát sinh khâu tiêu thụ — **không** vào giá thành sản xuất | 641 |
| Chi phí quản lý DN | G&A Expense | Quản lý chung — **không** vào giá thành sản xuất | 642 |

- **Chi phí sản phẩm (Product Cost)** = DM + DL + MOH → nằm trong hàng tồn kho đến khi bán, rồi mới thành giá vốn.
- **Chi phí thời kỳ (Period Cost)** = bán hàng + quản lý → ghi nhận ngay vào kỳ phát sinh.

**Tại sao phân biệt?** Nguyên tắc phù hợp (Matching): chi phí làm ra sản phẩm chưa bán được chưa phải là chi phí của kỳ — nó là tài sản (hàng tồn kho) cho đến khi sản phẩm được bán.

#### 4.2 Theo mối quan hệ với đối tượng tính giá

- **Chi phí trực tiếp (Direct)**: truy nguyên rõ ràng vào một job/sản phẩm (gỗ cho bàn họp).
- **Chi phí gián tiếp (Indirect)**: phục vụ nhiều sản phẩm, phải **phân bổ** (điện xưởng, khấu hao máy). *Toàn bộ cuộc tranh luận Traditional vs ABC xoay quanh cách phân bổ chi phí gián tiếp.*

#### 4.3 Theo ứng xử (Cost Behavior)

| Loại | Đặc điểm | Ví dụ |
|------|---------|-------|
| **Biến phí (Variable)** | Tổng thay đổi tỷ lệ theo sản lượng; trên 1 đơn vị không đổi | NVL, hoa hồng bán hàng |
| **Định phí (Fixed)** | Tổng không đổi trong phạm vi hoạt động liên quan; trên 1 đơn vị giảm khi sản lượng tăng | Thuê xưởng, khấu hao đường thẳng |
| **Hỗn hợp (Mixed)** | Có phần cố định + phần biến đổi | Điện (phí cơ bản + theo kWh) |

Chi tiết cost behavior, CVP và break-even xem `02-managerial-accounting.md` — ở đây chỉ dùng khi cần.

### 5. Dòng chi phí trong doanh nghiệp sản xuất

```
 NVL tồn kho ──► WIP (SP dở dang) ──► Thành phẩm ──► Giá vốn hàng bán
  (TK 152)      (TK 154)             (TK 155)         (TK 632)
                   ▲
   DM (621) ───────┤
   DL (622) ───────┤   Cả 3 loại tập hợp vào TK 154 (kê khai thường xuyên)
   MOH (627) ──────┘   rồi tính giá thành → nhập kho TP
```

Hạch toán cơ bản (kê khai thường xuyên, mô hình chế độ kế toán DN theo Thông tư 200/2014/TT-BTC — **cần xác nhận quy định hiện hành**; DN siêu nhỏ/nhỏ có thể áp dụng Thông tư 133/2016/TT-BTC):

| Nghiệp vụ | Bút toán |
|-----------|---------|
| Xuất NVL dùng cho sản xuất | Nợ 621 / Có 152 |
| Tính lương công nhân sản xuất | Nợ 622 / Có 334 |
| Chi phí SX chung (khấu hao, điện, lương quản đốc…) | Nợ 627 / Có 214, 111, 334… |
| Kết chuyển vào giá thành | Nợ 154 / Có 621, 622, 627 |
| Nhập kho thành phẩm | Nợ 155 / Có 154 |
| Bán hàng: ghi nhận giá vốn | Nợ 632 / Có 155 |

**Nguyên tắc VAS 02 (Hàng tồn kho) ở mức tổng quát — cần xác nhận:**
- Chi phí chế biến tính vào giá thành gồm chi phí trực tiếp và chi phí sản xuất chung biến đổi, cộng chi phí sản xuất chung cố định **phân bổ theo công suất bình thường**.
- Phần chi phí sản xuất chung cố định **vượt/không được phân bổ do sản lượng thấp hơn công suất bình thường** ghi nhận vào giá vốn trong kỳ (không "dồn" vào giá thành khiến hàng tồn kho bị đội giá).
- Hàng tồn kho đo lường theo giá thấp hơn giữa giá gốc và giá trị thuần có thể thực hiện được.
- IFRS (IAS 2) có nguyên tắc tương tự về cấu thành giá gốc hàng tồn kho.

### 6. Sơ đồ tổng quan các phương pháp

```
              COST ACCOUNTING METHODS
                      │
     ┌────────────────┼────────────────┐
     │                │                │
┌────▼────┐     ┌─────▼─────┐    ┌────▼──────┐
│  JOB    │     │  PROCESS  │    │ ACTIVITY  │
│ COSTING │     │  COSTING  │    │  BASED    │
│         │     │           │    │ (ABC)     │
└────┬────┘     └─────┬─────┘    └────┬──────┘
     │                │               │
  Sản phẩm        Sản phẩm        Cách PHÂN BỔ
  đặt riêng       hàng loạt       overhead chính
  unique          identical       xác hơn (có thể
                                  gắn lên Job/Process)
  Xây dựng       Nước giải khát
  In ấn          Xi măng
  Tư vấn         Hóa chất
  Phần mềm       Giấy
```

**Lưu ý quan trọng**: Job Costing và Process Costing trả lời câu hỏi **"gom chi phí theo đối tượng nào?"** (đơn hàng hay công đoạn), còn ABC trả lời câu hỏi **"phân bổ chi phí gián tiếp bằng tiêu thức nào?"**. Hai câu hỏi này độc lập, nên ABC có thể kết hợp với cả Job lẫn Process.

---

## II. CHI TIẾT TỪNG THÀNH PHẦN

### A. Job Order Costing – Tính giá theo đơn đặt hàng

#### 1. Tại sao cần Job Costing?

Khi mỗi sản phẩm khác nhau (một công trình, một lô in, một dự án phần mềm), việc lấy "tổng chi phí chia số lượng" vô nghĩa vì không có "sản phẩm trung bình". Doanh nghiệp cần gom chi phí **riêng cho từng đơn** để (1) báo giá, (2) biết đơn nào lãi/lỗ, (3) rút kinh nghiệm cho đơn sau.

#### 2. Đặc điểm

| Đặc điểm | Chi tiết |
|----------|---------|
| **Sản phẩm** | Đặt riêng, unique, khác nhau |
| **Tracking** | Theo từng job/lô cụ thể |
| **Chứng từ** | Job Cost Sheet (phiếu giá thành) cho mỗi đơn |
| **Chi phí gom** | DM + DL trực tiếp vào job; MOH phân bổ theo tỷ lệ ước tính |

#### 3. Quy trình Job Costing

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ Nhận đơn    │     │ Mở Job Cost │     │ Tập hợp     │
│ đặt hàng    │────►│ Sheet       │────►│ chi phí     │
│ (Job #101)  │     │             │     │             │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                                    ┌──────────┼──────────┐
                              ┌─────▼───┐ ┌────▼────┐ ┌──▼─────┐
                              │Direct   │ │Direct   │ │Mfg     │
                              │Materials│ │Labor    │ │Overhead│
                              │(thực tế)│ │(thực tế)│ │(phân bổ│
                              └─────┬───┘ └────┬────┘ └──┬─────┘
                              ┌─────▼──────────▼──────────▼──────┐
                              │         JOB COST SHEET           │
                              │  Job #101: Bàn gỗ tùy chỉnh      │
                              │  DM: Gỗ sồi 2m³ × 3tr = 6tr      │
                              │  DL: 40h × 80k/h = 3.2tr         │
                              │  MOH: 40h × 60k/h = 2.4tr        │
                              │  Total Job Cost: 11.6 triệu      │
                              └──────────────────────────────────┘
```

#### 4. Predetermined Overhead Rate (POHR) — Tại sao phải "ước tính trước"?

**Vấn đề**: Chi phí chung thực tế chỉ biết đầy đủ khi cuối tháng/quý/năm (hóa đơn điện, khấu hao, lương quản đốc…), nhưng khách hàng cần giá báo ngay và job xong tuần sau phải có giá thành. Hơn nữa, MOH có tính mùa vụ: nếu chia MOH thực tế từng tháng cho khối lượng từng tháng thì tháng thấp điểm (sản lượng ít) sẽ có "giá thành" cao bất thường dù quy trình không đổi.

**Giải pháp**: Dùng tỷ lệ phân bổ ước tính từ đầu kỳ (cả năm) để giá thành ổn định và có sớm:

$$\text{POHR} = \frac{\text{Estimated Total MOH}}{\text{Estimated Total Allocation Base}}$$

**Cách chọn Allocation Base** — nguyên tắc: chọn tiêu thức có **quan hệ nhân quả** nhất với việc phát sinh MOH.

| Base | Công thức | Phù hợp khi |
|------|----------|-------------|
| Direct Labor Hours | MOH / Total DL hours | Sản xuất thâm dụng lao động |
| Machine Hours | MOH / Total machine hours | Thâm dụng máy móc (in ấn, cơ khí CNC) |
| Direct Labor Cost | MOH / Total DL cost | Đơn giản, lương công nhân tương đối đồng đều |
| Units Produced | MOH / Total units | Sản phẩm đồng nhất |

**Phân bổ MOH vào job:**

$$\text{Applied MOH} = \text{POHR} \times \text{Actual Activity (của job hoặc của kỳ)}$$

#### 5. Ví dụ chi tiết từng bước: Xưởng nội thất ABC Furniture (giả định minh họa)

**Bước 1 – Tính POHR đầu năm.** Ngân sách MOH cả năm: 840.000.000 VNĐ; ước tính giờ lao động trực tiếp (DLH) cả năm: 12.000 giờ.

$$\text{POHR} = \frac{840.000.000}{12.000} = 70.000 \text{ VNĐ/DLH}$$

**Bước 2 – Gom chi phí 2 job tháng 3:**

| | Job #201 (Bàn họp 12 chỗ) | Job #202 (Kệ sách custom) |
|---|---------------------------|---------------------------|
| **Direct Materials** | | |
| - Gỗ | 8.000.000 | 3.000.000 |
| - Phụ kiện (ốc vít, keo) | 500.000 | 200.000 |
| **Direct Labor** | | |
| - Thợ mộc (giờ × đơn giá) | 60h × 100k = 6.000.000 | 25h × 100k = 2.500.000 |
| - Thợ sơn | 15h × 80k = 1.200.000 | 8h × 80k = 640.000 |
| **MOH Applied** (70k/DLH) | 75h × 70k = 5.250.000 | 33h × 70k = 2.310.000 |
| **TOTAL JOB COST** | **20.950.000** | **8.650.000** |
| Giá bán | 30.000.000 | 13.000.000 |
| **Gross Profit** | **9.050.000 (30,2%)** | **4.350.000 (33,5%)** |

Phép tính job #201: 8.000.000 + 500.000 + 6.000.000 + 1.200.000 + 5.250.000 = 20.950.000; GP% = 9.050.000/30.000.000 = 30,2%. Job #202: 3.000.000 + 200.000 + 2.500.000 + 640.000 + 2.310.000 = 8.650.000; GP% = 4.350.000/13.000.000 = 33,5%.

**Diễn giải**: Job #202 (nhỏ) có biên lãi gộp cao hơn job #201 dù giá trị thấp hơn — nhưng cần nhớ đây là biên gộp *sau khi phân bổ MOH theo giờ công*; nếu job #202 thực tế tốn nhiều công đoạn chuẩn bị (setup), con số có thể bị "đẹp giả" — chính là vấn đề mà ABC (mục C) giải quyết.

#### 6. Under-applied / Over-applied Overhead — Tại sao xuất hiện và xử lý ra sao?

Vì POHR dựa trên **ước tính**, cuối kỳ MOH phân bổ hiếm khi bằng MOH thực tế. Chênh lệch này gọi là **under/over-applied overhead**.

- **Under-applied**: Applied < Actual → đã "tính thiếu" chi phí vào giá thành → cần **tăng** giá vốn.
- **Over-applied**: Applied > Actual → đã "tính dư" → **giảm** giá vốn.

**Ví dụ tiếp tục (cuối năm, giả định minh họa):** MOH thực tế 852.000.000; giờ lao động trực tiếp thực tế 12.150 giờ.

- Applied MOH = 12.150 × 70.000 = 850.500.000
- Chênh lệch = 852.000.000 − 850.500.000 = **1.500.000 (under-applied)**

**Cách xử lý:**
1. *Nếu không trọng yếu*: điều chỉnh thẳng vào giá vốn: Nợ 632 / Có 627 = 1.500.000.
2. *Nếu trọng yếu*: phân bổ lại theo tỷ lệ số dư cuối kỳ của WIP, Thành phẩm, Giá vốn (giả định tỷ lệ 15% / 25% / 60%): WIP 225.000; Thành phẩm 375.000; Giá vốn 900.000 (cộng lại 1.500.000). Cách này đưa hàng tồn kho gần với giá thực tế hơn.

Theo VAS 02 (cần xác nhận hiện hành), phần MOH cố định không được phân bổ do sản lượng dưới công suất bình thường phải ghi vào giá vốn kỳ đó, không dồn vào hàng tồn kho.

---

### B. Process Costing – Tính giá theo quy trình

#### 1. Tại sao cần Process Costing?

Khi sản xuất ra hàng triệu chai nước mắm giống hệt nhau, không thể và không cần lập phiếu giá thành riêng cho từng chai. Doanh nghiệp tập hợp chi phí **theo từng công đoạn (process/department) trong từng kỳ**, rồi chia cho số **sản lượng quy đổi** của kỳ đó → giá thành đơn vị. Nguồn gốc là các ngành sản xuất liên tục thế kỷ 19–20 (dệt, hóa chất, đường, xi măng).

#### 2. Đặc điểm

| Đặc điểm | Chi tiết |
|----------|---------|
| **Sản phẩm** | Đồng nhất, sản xuất liên tục |
| **Tracking** | Theo department/process |
| **Đơn vị tính** | Equivalent Units (EU – đơn vị tương đương) |
| **Dòng chi phí** | Process 1 → Process 2 → … → Thành phẩm (chi phí công đoạn trước chuyển sang công đoạn sau) |

#### 3. Equivalent Units — Tại sao phải "quy đổi"?

**Vấn đề**: Cuối kỳ còn sản phẩm dở dang (Work-in-Process, WIP). Nếu chỉ chia tổng chi phí cho số thành phẩm, ta dồn cả chi phí của phần dở dang vào thành phẩm → giá thành quá cao. Nếu đếm WIP là 1 sản phẩm đầy đủ → giá thành quá thấp. Giải pháp: quy đổi WIP thành **số sản phẩm hoàn thành tương đương** theo mức độ hoàn thành từng yếu tố chi phí.

$$\text{EU} = \text{Units Completed} + (\text{WIP Ending} \times \text{\% Completion})$$

**Điểm tinh tế (thường bị sai)**: mức độ hoàn thành **khác nhau theo từng loại chi phí**. Nguyên vật liệu thường đưa vào đầu quy trình (100% ngay khi bắt đầu), trong khi nhân công + MOH ("chi phí chế biến" – Conversion Cost) phát sinh dần theo tiến độ. Vì vậy phải tính EU **riêng cho NVL và riêng cho Conversion**.

#### 4. Hai phương pháp: Weighted Average (Bình quân gia quyền) và FIFO

| | Weighted Average (BQGQ) | FIFO |
|---|------------------------|------|
| **Nguyên tắc** | Gộp chi phí WIP đầu kỳ + chi phí phát sinh để tính giá thành bình quân | Tách riêng WIP đầu kỳ; chỉ dùng chi phí **phát sinh trong kỳ** để tính đơn giá của kỳ |
| **EU tính** | EU = Hoàn thành + WIP cuối × %hoàn thành | EU = phần hoàn thiện WIP đầu kỳ + Bắt đầu & hoàn thành trong kỳ + WIP cuối kỳ |
| **Đơn giản** | Dễ hơn | Phức tạp hơn |
| **Chính xác** | Ít chính xác khi giá đầu vào biến động mạnh | Chính xác hơn (đo hiệu quả của kỳ hiện tại) |
| **Phổ biến** | Rất phổ biến, đặc biệt trong SME VN (gần với phương pháp "bình quân" quen thuộc) | Ít phổ biến hơn |

#### 5. Ví dụ chi tiết từng bước: Nhà máy nước mắm — Process 3 (Pha chế), tháng 6 (giả định minh họa)

```
  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
  │ Process 1│    │ Process 2│    │ Process 3│    │ Process 4│
  │ Ngâm ủ   │───►│ Lọc      │───►│ Pha chế  │───►│ Đóng chai│
  │ (6 tháng)│    │          │    │          │    │          │
  └──────────┘    └──────────┘    └──────────┘    └──────────┘
```

**Dữ liệu sản lượng (lít):**

| Chỉ tiêu | Số liệu |
|----------|---------|
| WIP đầu kỳ | 500 lít (NVL 100%, chế biến 80% hoàn thành) |
| Bắt đầu sản xuất trong kỳ | 4.000 lít |
| Hoàn thành & chuyển sang P4 | 3.500 lít |
| WIP cuối kỳ | 1.000 lít (NVL 100%, chế biến 40% hoàn thành) |

*Kiểm tra cân đối số lượng*: đầu vào 500 + 4.000 = 4.500 lít; đầu ra 3.500 + 1.000 = 4.500 lít ✓.

**Dữ liệu chi phí:**

| Chi phí | WIP đầu kỳ | Phát sinh trong kỳ | Tổng |
|---------|-----------|---------------------|------|
| NVL | 10.000.000 | 80.000.000 | 90.000.000 |
| Chế biến (Nhân công + MOH) | 5.200.000 | 53.300.000 | 58.500.000 |
| **Tổng** | 15.200.000 | 133.300.000 | **148.500.000** |

**Phương pháp 1 – Weighted Average:**

*Bước 1 – EU:*
- EU (NVL) = 3.500 + 1.000 × 100% = **4.500**
- EU (Chế biến) = 3.500 + 1.000 × 40% = **3.900**

*Bước 2 – Chi phí/EU (gộp đầu kỳ + phát sinh):*
- NVL: 90.000.000 / 4.500 = **20.000 VNĐ/EU**
- Chế biến: 58.500.000 / 3.900 = **15.000 VNĐ/EU**
- Tổng: **35.000 VNĐ/lít**

*Bước 3 – Phân bổ:*

| | Cách tính | Số tiền |
|---|-----------|--------|
| Thành phẩm chuyển P4 | 3.500 × 35.000 | 122.500.000 |
| WIP cuối – NVL | 1.000 × 20.000 | 20.000.000 |
| WIP cuối – Chế biến | 400 EU × 15.000 | 6.000.000 |
| **Tổng phân bổ** | | **148.500.000** ✓ (= 90.000.000 + 58.500.000) |

**Phương pháp 2 – FIFO (để đối chiếu):**

*Bước 1 – EU:*
- EU (NVL) = 0 (WIP đầu kỳ đã đủ NVL) + (3.500 − 500) bắt đầu & hoàn thành + 1.000 WIP cuối = **4.000**
- EU (Chế biến) = 500 × (100% − 80%) = 100 + 3.000 + 400 = **3.500**

*Bước 2 – Chi phí/EU (chỉ chi phí phát sinh trong kỳ):*
- NVL: 80.000.000 / 4.000 = 20.000
- Chế biến: 53.300.000 / 3.500 = 15.228,57

*Bước 3 – Phân bổ:*
- Thành phẩm = WIP đầu kỳ 15.200.000 + hoàn thiện 100 EU × 15.228,57 + 3.000 × (20.000 + 15.228,57) ≈ **122.408.571**
- WIP cuối = 1.000 × 20.000 + 400 × 15.228,57 ≈ **26.091.429**
- Tổng = 148.500.000 ✓

**So sánh & diễn giải**: Giá thành thành phẩm theo BQGQ là 35.000/lít, theo FIFO ≈ 34.974/lít — chênh lệch rất nhỏ vì chi phí đơn vị giữa các kỳ ít biến động. FIFO chỉ đáng kể khi giá NVL/nhân công biến động mạnh giữa các kỳ. Với SME, **BQGQ thường là đủ**. (Lỗi cũ trong bản gốc: dùng chung 1 cột EU và tính WIP cuối "400 EU × 35.000 = 14 triệu" cho cả NVL — mâu thuẫn với giả định NVL xuất vào đầu quy trình; đã sửa bằng cách tách EU NVL và EU chế biến.)

---

### C. Activity-Based Costing (ABC) – Tính giá theo hoạt động

#### 1. Tại sao ABC ra đời? — Vấn đề của phân bổ truyền thống

Trước thập niên 1980, nhân công trực tiếp là phần lớn giá thành, nên phân bổ overhead theo giờ lao động/giờ máy tạm đủ chính xác. Sau khi tự động hóa, overhead (chuẩn bị máy, kiểm tra chất lượng, hậu cần, thiết kế, phục vụ khách hàng…) chiếm phần lớn giá thành nhưng **không tỷ lệ với số giờ máy hay giờ lao động**. Kết quả: sản phẩm sản xuất **số lượng lớn, đơn giản** bị "gánh" chi phí của sản phẩm **số lượng nhỏ, phức tạp** (trợ giá chéo – cross-subsidization), dẫn đến định giá sai và chọn sai sản phẩm để đẩy mạnh. Robert Kaplan và Robin Cooper (1988) đề xuất ABC với nguyên lý:

> **"Products consume activities, activities consume resources."** – Cooper & Kaplan

Nghĩa là: sản phẩm không "tiêu thụ" overhead trực tiếp; sản phẩm **kích hoạt các hoạt động** (setup, kiểm tra, giao hàng…), và hoạt động mới tiêu thụ nguồn lực. Phân bổ theo hoạt động chính xác hơn.

```
  TRADITIONAL COSTING                    ABC

  Overhead                              Overhead
       │                                     │
       │ (1 base: giờ máy)         ┌────┬────┼────┬────┐
       │                           │    │    │    │
  ┌────▼────┐ ┌────────┐       ┌───▼─┐ ┌▼──┐ ┌▼───┐ ┌▼───┐
  │Product A│ │Product B│       │Setup│ │QC │ │Ship│ │Maint│
  └─────────┘ └────────┘       └──┬──┘ └─┬─┘ └─┬──┘ └──┬──┘
  → chia theo giờ máy              │      │     │       │
                              # setups # tests # orders # hrs
                              Phân bổ theo activity driver thực tế
```

#### 2. Quy trình ABC (5 bước)

```
  Bước 1: Xác định HOẠT ĐỘNG (Activities)
       │   Setup máy, Kiểm tra chất lượng, Giao hàng, Bảo trì
  Bước 2: Gom CHI PHÍ vào từng hoạt động (Activity Cost Pool)
       │   Setup: 150 triệu, QC: 100 triệu, Shipping: 150 triệu...
  Bước 3: Chọn COST DRIVER (tiêu thức gây chi phí)
       │   Setup: số lần setup, QC: số lần kiểm tra, Shipping: số đơn
  Bước 4: Tính ACTIVITY RATE
       │   Rate = Activity Cost Pool / Total Cost Driver
  Bước 5: PHÂN BỔ chi phí cho sản phẩm
           Cost = Activity Rate × Cost Driver mà sản phẩm tiêu thụ
```

**Phân cấp hoạt động (Activity Hierarchy)** — giúp chọn driver:

| Cấp | Phát sinh theo | Ví dụ | Driver |
|-----|----------------|-------|--------|
| Unit-level | Mỗi đơn vị sản phẩm | Điện chạy máy, bảo trì theo giờ máy | Giờ máy |
| Batch-level | Mỗi lô/lần sản xuất | Setup máy, kiểm tra theo lô, xử lý đơn | Số lần setup, số đơn |
| Product-level | Duy trì dòng sản phẩm | Thiết kế mẫu, quản lý công thức | Số mã sản phẩm |
| Facility-level | Duy trì cơ sở | Thuê nhà xưởng, bảo vệ | Thường không phân bổ theo driver |

#### 3. Ví dụ chi tiết: So sánh Traditional vs ABC — Công ty sản xuất bánh (giả định minh họa)

| Thông tin | Bánh A (Hàng loạt) | Bánh B (Đặt riêng) | Tổng |
|----------|-------------------|-------------------|------|
| Sản lượng | 10.000 cái | 2.000 cái | 12.000 |
| Giờ máy | 5.000 h | 1.000 h | 6.000 h |
| Số lần setup | 10 | 40 | 50 |
| Số lần kiểm tra QC | 20 | 60 | 80 |
| Số đơn giao hàng | 50 | 150 | 200 |
| Giá bán / cái | 70.000 | 220.000 | |
| Chi phí trực tiếp (DM + DL) / cái | 30.000 | 45.000 | |

**Tổng MOH: 500 triệu VNĐ.**

**Bước A – Traditional Costing (base: giờ máy):**

$$\text{POHR} = \frac{500.000.000}{6.000} = 83.333 \text{ VNĐ/giờ máy}$$

| | Bánh A | Bánh B |
|---|--------|--------|
| MOH phân bổ | 5.000h × 83.333 = **416,7 triệu** | 1.000h × 83.333 = **83,3 triệu** |
| MOH / cái | **41.667** | **41.667** |

→ Hai sản phẩm có chi phí MOH/cái **bằng nhau** dù B tốn rất nhiều lần setup/QC/giao hàng hơn → không hợp lý.

**Bước B – ABC:**

*Cost pool & driver:*

| Activity | Cost Pool | Cost Driver | Tổng driver | Activity Rate |
|----------|----------|-------------|-------------|---------------|
| Setup máy | 150.000.000 | Số lần setup | 50 | 3.000.000 / lần |
| Kiểm tra QC | 100.000.000 | Số lần kiểm tra | 80 | 1.250.000 / lần |
| Giao hàng | 150.000.000 | Số đơn giao | 200 | 750.000 / đơn |
| Bảo trì máy | 100.000.000 | Giờ máy | 6.000 | 16.667 / giờ |

*Phân bổ:*

| Activity | Bánh A | Bánh B |
|----------|--------|--------|
| Setup | 10 × 3.000.000 = 30.000.000 | 40 × 3.000.000 = 120.000.000 |
| QC | 20 × 1.250.000 = 25.000.000 | 60 × 1.250.000 = 75.000.000 |
| Giao hàng | 50 × 750.000 = 37.500.000 | 150 × 750.000 = 112.500.000 |
| Bảo trì | 5.000 × 16.667 ≈ 83.333.333 | 1.000 × 16.667 ≈ 16.666.667 |
| **Tổng MOH** | **175.833.333** | **324.166.667** |
| **MOH / cái** | **17.583** (÷10.000) | **162.083** (÷2.000) |

*Kiểm tra*: 175.833.333 + 324.166.667 = 500.000.000 ✓.

**Bước C – So sánh MOH/cái:**

| | Traditional | ABC | Chênh lệch |
|---|------------|-----|-----------|
| **Bánh A** | 41.667 | **17.583** | Traditional **cao hơn** ABC 137% |
| **Bánh B** | 41.667 | **162.083** | Traditional **thấp hơn** ABC 74% |

**Bước D – Hệ quả lợi nhuận (đây là điều quan trọng nhất):**

| | Traditional | ABC |
|---|-------------|-----|
| Bánh A: 70.000 − 30.000 − MOH/cái | 70.000 − 30.000 − 41.667 = **−1.667/cái** → lỗ 16,7 triệu | 70.000 − 30.000 − 17.583 = **+22.417/cái** → lãi 224,2 triệu (biên 32,0%) |
| Bánh B: 220.000 − 45.000 − MOH/cái | 220.000 − 45.000 − 41.667 = **+133.333/cái** → lãi 266,7 triệu (biên 60,6%) | 220.000 − 45.000 − 162.083 = **+12.917/cái** → lãi 25,8 triệu (biên 5,9%) |
| **Tổng lợi nhuận** | 250 triệu | 250 triệu |

**Diễn giải**: Tổng lợi nhuận giống nhau (250 triệu) vì tổng MOH vẫn là 500 triệu — ABC không tạo ra tiền, chỉ **phân bổ lại cho đúng**. Nhưng quyết định thay đổi hoàn toàn: theo Traditional, Bánh A "lỗ nhẹ" → có thể bị cắt, Bánh B "siêu lãi" → đẩy mạnh. Theo ABC, Bánh A mới là ngôi sao, còn Bánh B chỉ lãi mỏng 5,9% do tiêu tốn quá nhiều setup/QC/giao hàng. Nếu doanh nghiệp làm theo Traditional (bỏ Bánh A, mở rộng Bánh B) sẽ hủy hoại lợi nhuận. Bánh B thực tế tốn kém gấp ≈ 9,2 lần Bánh A về MOH/cái → cần tăng giá, gom lô sản xuất, hoặc giảm số lần setup.

#### 4. Time-Driven ABC (TDABC)

**Tại sao ra đời?** ABC truyền thống đòi hỏi phỏng vấn nhân viên để ước tính % thời gian cho từng hoạt động — tốn kém, nhanh lỗi thời. Kaplan & Anderson (2004) đơn giản hóa: chỉ cần 2 tham số — (1) **chi phí mỗi phút công suất** của bộ phận, (2) **số phút** mỗi hoạt động cần.

$$\text{Cost per minute} = \frac{\text{Total department cost}}{\text{Practical capacity (minutes)}}$$

$$\text{Activity cost} = \text{Time per activity} \times \text{Cost per minute}$$

*Practical capacity* (công suất thực tế) thường lấy khoảng 80–85% công suất lý thuyết, vì trừ thời gian nghỉ, họp, chờ.

**Ví dụ (giả định minh họa) – Bộ phận xử lý đơn hàng e-commerce:**
- Chi phí bộ phận: 54.000.000 VNĐ/tháng; 5 nhân viên × 20 ngày × 6 giờ thực dụng × 60 phút = 36.000 phút.
- Chi phí mỗi phút = 54.000.000 / 36.000 = **1.500 VNĐ/phút**.

| Hoạt động | Phút/đơn | Chi phí/đơn | Số lượng tháng | Tổng phút |
|-----------|---------|------------|----------------|-----------|
| Xử lý đơn chuẩn | 4 | 6.000 | 4.000 | 16.000 |
| Xử lý đơn tùy chỉnh | 10 | 15.000 | 800 | 8.000 |
| Xử lý đổi trả | 15 | 22.500 | 600 | 9.000 |
| **Tổng** | | | | **33.000** |

- Chi phí đã dùng = 33.000 × 1.500 = 49.500.000; mức sử dụng công suất = 33.000/36.000 = 91,7%.
- **Công suất nhàn rỗi** = (36.000 − 33.000) × 1.500 = **4.500.000** — TDABC cho thấy thẳng chi phí của công suất chưa dùng, thứ ABC truyền thống thường che khuất.
- Mỗi đơn đổi trả tốn 22.500 → đắt gấp 3,75 lần đơn chuẩn (6.000).

---

### D. So sánh 3 phương pháp

| Tiêu chí | Job Order Costing | Process Costing | ABC |
|----------|------------------|----------------|-----|
| **Sản phẩm** | Đặt riêng, unique | Đồng nhất, hàng loạt | Cả hai |
| **Đơn vị tracking** | Từng job/order | Từng department/process | Từng activity |
| **Overhead allocation** | POHR × 1 base | POHR × 1 base | Nhiều activity rate |
| **Độ chính xác** | Trung bình | Thấp nhất khi tính SP riêng lẻ | Cao nhất |
| **Phức tạp** | Trung bình | Thấp | Cao |
| **Chi phí triển khai** | Thấp – TB | Thấp | Cao |
| **Ngành phù hợp** | Xây dựng, in ấn, tư vấn, phần mềm | Thực phẩm, hóa chất, xi măng, dệt may | Đa sản phẩm, overhead cao |
| **Độ dễ cho SME** | Dễ | Dễ | Vừa |
| **Khi nào dùng** | SP khác nhau, chi phí khác nhiều | SP giống nhau, sản xuất liên tục | Cần chính xác overhead |

```
            Sản phẩm của bạn?
                  │
          ┌───────┴───────┐
    Đặt riêng /      Đồng nhất /
    Unique           Hàng loạt
          ▼               ▼
   JOB COSTING      PROCESS COSTING
          └───────┬───────┘
          Overhead chiếm >30%
          tổng chi phí? (ngưỡng tham khảo)
            ┌─────┴─────┐
          Không         Có
            ▼           ▼
     Giữ Traditional   Kết hợp ABC /
                       TDABC cho phần
                       overhead
```

### E. Absorption Costing vs Variable Costing

#### 1. Vấn đề cần giải quyết

Định phí sản xuất chung (khấu hao, thuê xưởng) có được tính vào giá thành sản phẩm hay không? Hai trường phái:

- **Absorption (Full) Costing**: tính cả định phí SX chung vào giá thành sản phẩm — **phương pháp bắt buộc cho báo cáo tài chính** (theo VAS 02/IAS 2, với nguyên tắc phân bổ theo công suất bình thường).
- **Variable (Direct) Costing**: chỉ biến phí vào giá thành; định phí SX chung ghi nhận ngay thành chi phí kỳ — hữu ích cho **quản trị nội bộ** (CVP, quyết định ngắn hạn).

#### 2. Ví dụ từng bước (giả định minh họa)

Biến phí SX 100.000/sp; định phí SX chung 50.000.000/kỳ; sản xuất 1.000 sp; bán 800 sp với giá 250.000.

- Giá thành đơn vị (absorption) = 100.000 + 50.000.000/1.000 = **150.000**
- Lợi nhuận (absorption) = 800 × 250.000 − 800 × 150.000 = **80.000.000**
- Lợi nhuận (variable) = 800 × (250.000 − 100.000) − 50.000.000 = **70.000.000**
- Chênh lệch = 10.000.000 = định phí SX chung nằm trong 200 sp tồn kho (200 × 50.000)

**Diễn giải**: Khi sản xuất > bán, absorption costing "giấu" một phần định phí vào hàng tồn kho nên lợi nhuận cao hơn — có thể bị lợi dụng để "làm đẹp" lợi nhuận bằng cách sản xuất thừa. Đây là lý do kế toán quản trị thường dùng variable costing để đánh giá hiệu quả kinh doanh thực.

### F. Các phương pháp nâng cao

#### 1. Target Costing (Tính giá mục tiêu)

**Tại sao**: Cách tính truyền thống "cost-plus" (chi phí + lợi nhuận → giá bán) có thể dẫn đến giá cao hơn mức thị trường chấp nhận. Toyota và các hãng Nhật Bản phát triển Target Costing để **đảo ngược logic**: giá do thị trường quyết định.

$$\text{Target Cost} = \text{Target Price} - \text{Target Profit}$$

**Ví dụ**: Thị trường chấp nhận giá 300.000, muốn biên lợi nhuận 30% → Target Cost = 300.000 × 70% = 210.000. Nếu chi phí hiện tại 230.000 → "khoảng cách" cần cắt giảm 20.000, thực hiện bằng thiết kế lại sản phẩm (**Value Engineering**) trước khi sản xuất.

#### 2. Kaizen Costing (Cải tiến liên tục)

- Áp dụng **sau** khi sản phẩm đã vào sản xuất, đặt mục tiêu giảm chi phí định kỳ (ví dụ giảm 1–2%/quý).
- Kết hợp Lean Manufacturing; bổ sung cho Target Costing (Target Costing tác động giai đoạn thiết kế, Kaizen Costing giai đoạn sản xuất).

#### 3. Life-Cycle Costing

- Tính chi phí **toàn bộ vòng đời** sản phẩm: R&D → Production → Distribution → After-sales → Disposal.
- Thường được trích dẫn rằng phần lớn (khoảng 70–80%) chi phí vòng đời bị "khóa" ở giai đoạn thiết kế (con số mang tính tham khảo, cần đối chiếu nguồn).

---

## III. CASE STUDIES THỰC TẾ

### 1. Case Study Thành công: Hewlett-Packard (HP) – ABC phơi bày lợi nhuận thật của dòng máy in

#### Bối cảnh

HP là ví dụ kinh điển về ABC trong tài liệu quản trị chi phí (Cooper & Kaplan, và nhiều giáo trình sử dụng). Những năm 1980–1990, HP có nhiều bộ phận sản xuất thiết bị điện tử và máy in. Câu chuyện thường được dùng để minh họa: dưới Traditional Costing (phân bổ overhead theo giờ lao động trực tiếp), dòng sản phẩm đơn giản, số lượng lớn trông "rất lãi", dòng phức tạp trông "kém lãi"; sau ABC, bức tranh đảo ngược.

> **Lưu ý nguồn**: Các số liệu trong tài liệu gốc (ví dụ "lợi nhuận thấp hơn 30%/cao hơn 25%") chưa được kiểm chứng và **cần đối chiếu nguồn** trước khi trích dẫn. Dưới đây là **mô hình minh họa giả định** (không phải số liệu thật của HP) để làm rõ cơ chế.

#### Dữ liệu giả định minh họa

Tổng MOH 600 triệu (đơn vị tiền tệ quy ước). Hai dòng sản phẩm:

| | InkJet (nhỏ, nhiều đơn lẻ) | LaserJet (lớn, ít đơn) | Tổng |
|---|---|---|---|
| Sản lượng | 40.000 | 8.000 | |
| Giờ lao động trực tiếp | 2.000 | 8.000 | 10.000 |
| Giá bán / máy | 20.000 | 100.000 | |
| Chi phí trực tiếp / máy | 8.000 | 30.000 | |
| Số đơn mua NVL | 700 | 300 | 1.000 |
| Số lần kiểm tra chất lượng | 600 | 400 | 1.000 |
| Số yêu cầu bảo hành/hỗ trợ | 1.500 | 500 | 2.000 |
| Số lô giao hàng | 2.000 | 1.000 | 3.000 |

#### Bước 1 – Traditional (base: giờ lao động trực tiếp)

POHR = 600.000.000 / 10.000 = **60.000/giờ**.
- InkJet: 2.000 × 60.000 = 120.000.000 → 3.000/máy
- LaserJet: 8.000 × 60.000 = 480.000.000 → 60.000/máy

#### Bước 2 – ABC

| Activity | Pool | Driver | Rate | InkJet | LaserJet |
|----------|------|--------|------|--------|----------|
| Mua hàng | 100.000.000 | 1.000 đơn | 100.000 | 70.000.000 | 30.000.000 |
| Kiểm tra CL | 150.000.000 | 1.000 lần | 150.000 | 90.000.000 | 60.000.000 |
| Hỗ trợ KH | 200.000.000 | 2.000 yêu cầu | 100.000 | 150.000.000 | 50.000.000 |
| Giao hàng | 150.000.000 | 3.000 lô | 50.000 | 100.000.000 | 50.000.000 |
| **Tổng** | 600.000.000 | | | **410.000.000** | **190.000.000** |
| **MOH/máy** | | | | **10.250** | **23.750** |

#### Bước 3 – So sánh lợi nhuận/máy

| | Traditional | ABC |
|---|---|---|
| InkJet | 20.000 − 8.000 − 3.000 = 9.000 (biên 45%) | 20.000 − 8.000 − 10.250 = **1.750 (biên 8,75%)** |
| LaserJet | 100.000 − 30.000 − 60.000 = 10.000 (biên 10%) | 100.000 − 30.000 − 23.750 = **46.250 (biên 46,25%)** |

Tổng lợi nhuận hai phương pháp đều bằng 440.000.000 (40.000 × 9.000 + 8.000 × 10.000 = 40.000 × 1.750 + 8.000 × 46.250 = 440 triệu) — ABC chỉ phân bổ lại.

#### Diễn giải ý nghĩa kinh doanh

- InkJet chiếm 20% giờ lao động nhưng tiêu thụ 68% overhead (410/600) vì nhiều đơn mua nhỏ, nhiều yêu cầu hỗ trợ, giao hàng lẻ.
- Traditional đánh giá sai: InkJet có vẻ lãi 45% nhưng thực tế chỉ 8,75%.

#### Hành động có thể thực hiện

1. Giảm chi phí hỗ trợ khách hàng của InkJet (thiết kế dễ dùng, hướng dẫn tự phục vụ).
2. Gom đơn mua NVL (mua lô lớn) để giảm số đơn.
3. Tập trung đầu tư vào dòng có lãi thật (LaserJet).
4. Định giá lại thiết bị InkJet hoặc chuyển margin sang vật tư tiêu hao (mô hình "dao cạo – lưỡi dao").

#### Bài học

> ABC phá vỡ ảo tưởng lợi nhuận do trợ giá chéo. **Sản phẩm "đơn giản" chưa chắc rẻ; sản phẩm "phức tạp" chưa chắc đắt nếu quy trình được tối ưu.**

---

### 2. Case Study Thất bại: Chuỗi nhà hàng "TasteVN" – Không biết chi phí thực, mở rộng quá nhanh

#### Bối cảnh

Chuỗi nhà hàng "TasteVN" (tên giả định, tình huống minh họa) có 3 chi nhánh tại TP.HCM. Dựa vào báo cáo tài chính cho thấy "tổng thể có lãi", chủ chuỗi quyết định mở thêm 5 chi nhánh trong 1 năm.

#### Vấn đề: thiếu Cost Accounting chi tiết

| Yếu tố | Biết | Không biết |
|--------|------|-----------|
| Tổng doanh thu | Có | – |
| Tổng chi phí | Có | – |
| Chi phí / món | Không | Food cost % từng món |
| Chi phí / chi nhánh | Không | Lãi/lỗ từng location |
| Chi phí delivery vs dine-in | Không | P&L theo kênh |

#### Bước 1 – P&L từng chi nhánh (giả định minh họa, đơn vị: triệu VNĐ/tháng)

| Chi nhánh | Doanh thu | Food cost | Labor | Rent | Other | Tổng % chi phí | Profit |
|----------|-----------|-----------|-------|------|-------|------|--------|
| Q1 (trung tâm) | 500 | 35% | 25% | 20% | 10% | 90% | **+50 (10%)** |
| Q7 (khu dân cư) | 300 | 33% | 28% | 15% | 12% | 88% | **+36 (12%)** |
| Thủ Đức (mới mở) | 200 | 40% | 30% | 18% | 15% | 103% | **−6 (−3%)** |
| **Tổng** | 1.000 | | | | | | **+80 (8%)** |

Chủ chuỗi chỉ nhìn dòng tổng (+80 triệu, 8%) nên cho rằng mô hình khả thi và nhân rộng.

#### Bước 2 – Phân tích điểm hòa vốn từng chi nhánh

Giả định: food cost là biến phí; labor, rent, other là định phí (đơn giản hóa).

$$\text{BE Revenue} = \frac{\text{Fixed Costs}}{\text{CM ratio}}, \quad \text{CM ratio} = 1 - \text{Food cost \%}$$

| Chi nhánh | Định phí (triệu) | CM ratio | BE Revenue (triệu) | Doanh thu thực | Biên an toàn |
|-----------|------------------|----------|--------------------|-----------------|--------------|
| Q1 | (25%+20%+10%) × 500 = 275 | 65% | 275/0,65 ≈ 423,1 | 500 | 76,9 (15,4%) |
| Q7 | (28%+15%+12%) × 300 = 165 | 67% | 165/0,67 ≈ 246,3 | 300 | 53,7 (17,9%) |
| Thủ Đức | (30%+18%+15%) × 200 = 126 | 60% | 126/0,60 = 210 | 200 | **−10 (−5%)** |

**Diễn giải**: Thủ Đức cần ít nhất 210 triệu/tháng mới hòa vốn nhưng chỉ đạt 200 triệu, thêm food cost cao (40% so với 33–35%) làm CM ratio kém. Nhân bản mô hình ra 5 chi nhánh mới mà chưa biết **chi nhánh mới phải mất bao lâu mới đạt BE** là nhân rộng rủi ro.

#### Bước 3 – Phân tích menu (ABC-lite: theo nhóm món)

| Nhóm món | % Doanh thu | Food cost % | CM % | Verdict |
|----------|------------|-------------|------|---------|
| Món Việt truyền thống | 40% | 28% | 72% | Star – giữ & đẩy mạnh |
| Món Âu fusion | 30% | 45% | 55% | Cần tối ưu NVL/giá |
| Đồ uống | 20% | 18% | 82% | Cash cow |
| Tráng miệng | 10% | 50% | 50% | Xem xét điều chỉnh công thức/giá, **không cắt chỉ vì CM thấp** |

- Food cost bình quân gia quyền = 0,4×28% + 0,3×45% + 0,2×18% + 0,1×50% = 11,2% + 13,5% + 3,6% + 5% = **33,3%**; CM bình quân = 66,7%.
- Nếu giảm food cost món Âu fusion từ 45% xuống 38% (thương lượng NVL, điều chỉnh định lượng): tiết kiệm = 30% × 7% = 2,1% doanh thu → với tổng doanh thu 1.000 triệu/tháng ≈ **21 triệu/tháng** (252 triệu/năm).
- **Điều chỉnh so với bản cũ**: tráng miệng có CM 50% vẫn đóng góp dương cho định phí; chỉ nên cắt nếu chiếm diện tích/nhân công đáng kể hoặc kéo trải nghiệm xấu. Quyết định bỏ món phải dựa trên **chi phí cơ hội và phần định phí tránh được**, không chỉ trên % CM.

#### Hệ quả

- Mở 5 chi nhánh mới; 3 chi nhánh lỗ nặng do mô hình chưa tối ưu và không kiểm soát food cost từng món.
- Phải đóng 2 chi nhánh sau 18 tháng, tổn thất ước tính khoảng 3 tỷ VNĐ (số giả định minh họa).

#### Bài học

> 1. **Biết "tổng thể có lãi" chưa đủ** — cần lãi/lỗ theo chi nhánh, sản phẩm, kênh.
> 2. **Cost Accounting là tiền đề của scaling** — nhân rộng mô hình chưa tối ưu = nhân rộng lỗ.
> 3. **ABC cho F&B**: phân tích food cost + labor + overhead theo nhóm món/kênh.
> 4. **Menu Engineering**: kết hợp popularity × profitability để tối ưu menu.

---

### 3. Case Study SME Việt Nam: Xưởng in bao bì "Hải Long" – Đơn nhỏ nhìn thì lời, tính ABC mới thấy lỗ (giả định minh họa)

#### Bối cảnh

Xưởng in hộp giấy "Hải Long" (tên và số liệu hoàn toàn giả định) ở Bình Dương, 18 nhân sự, 2 máy in offset. Khách hàng gồm doanh nghiệp lớn đặt lô lớn (hàng chục nghìn hộp, 1–2 mẫu) và các shop nhỏ đặt lô vài nghìn hộp, nhiều màu, hay sửa mẫu. Kế toán đang dùng Job Costing, phân bổ MOH theo giờ máy. Chủ xưởng nhận thấy các đơn nhỏ "luôn có biên lợi nhuận đẹp" nên đang ưu tiên nhận đơn nhỏ và khuyến mãi cho shop nhỏ. Cuối năm lợi nhuận lại không như kỳ vọng.

#### Bước 1 – Ngân sách MOH và POHR (kiểu truyền thống)

- MOH ngân sách năm: 960.000.000 VNĐ; giờ máy dự kiến: 4.800 giờ.
- POHR = 960.000.000 / 4.800 = **200.000 VNĐ/giờ máy**.

#### Bước 2 – Hai đơn hàng tiêu biểu

| | Job P-101 (khách lớn) | Job P-102 (shop nhỏ) |
|---|---|---|
| Số lượng | 50.000 hộp | 2.000 hộp |
| Giá bán | 140.000.000 | 14.000.000 |
| NVL trực tiếp (giấy, mực) | 90.000.000 | 6.000.000 |
| Nhân công trực tiếp | 12.000.000 | 3.000.000 |
| Giờ máy | 120 | 12 |
| Số lần setup (chuẩn bị bản in/chỉnh màu) | 4 | 6 |
| Số mẫu thiết kế duyệt | 1 | 3 |
| Số lần giao hàng | 2 | 1 |

#### Bước 3 – Giá thành theo Traditional (giờ máy)

| | P-101 | P-102 |
|---|---|---|
| MOH = giờ máy × 200.000 | 120 × 200.000 = 24.000.000 | 12 × 200.000 = 2.400.000 |
| Giá thành | 90 + 12 + 24 = **126.000.000** | 6 + 3 + 2,4 = **11.400.000** |
| Lợi nhuận | 140 − 126 = **14.000.000 (10,0%)** | 14 − 11,4 = **2.600.000 (18,6%)** |

→ Đơn nhỏ "lãi hơn" (18,6% so với 10%), nên chủ xưởng ưu tiên đơn nhỏ.

#### Bước 4 – Giá thành theo ABC

*Chia MOH 960 triệu thành 4 nhóm hoạt động (giả định phân tích từ sổ sách):*

| Activity | Cost Pool | Driver | Tổng driver | Rate |
|----------|----------|--------|-------------|------|
| Chuẩn bị bản in & chỉnh màu (setup) | 300.000.000 | Số lần setup | 600 | 500.000/lần |
| Thiết kế & duyệt mẫu | 180.000.000 | Số mẫu duyệt | 360 | 500.000/mẫu |
| Vận hành máy (điện, khấu hao, bảo trì) | 330.000.000 | Giờ máy | 4.800 | 68.750/giờ |
| Giao hàng & chăm sóc khách | 150.000.000 | Số lần giao | 1.000 | 150.000/lần |
| **Tổng** | **960.000.000** | | | |

*Phân bổ cho 2 job:*

| Activity | P-101 | P-102 |
|----------|-------|-------|
| Setup | 4 × 500.000 = 2.000.000 | 6 × 500.000 = 3.000.000 |
| Thiết kế | 1 × 500.000 = 500.000 | 3 × 500.000 = 1.500.000 |
| Vận hành máy | 120 × 68.750 = 8.250.000 | 12 × 68.750 = 825.000 |
| Giao hàng | 2 × 150.000 = 300.000 | 1 × 150.000 = 150.000 |
| **MOH (ABC)** | **11.050.000** | **5.475.000** |

| | P-101 | P-102 |
|---|---|---|
| Giá thành ABC | 90 + 12 + 11,05 = **113.050.000** | 6 + 3 + 5,475 = **14.475.000** |
| Lợi nhuận | 140 − 113,05 = **26.950.000 (19,25%)** | 14 − 14,475 = **−475.000 (−3,4%)** |

#### Bước 5 – Diễn giải ý nghĩa kinh doanh

| | Traditional | ABC |
|---|---|---|
| P-101 (lớn) | Lãi 10,0% | Lãi **19,25%** |
| P-102 (nhỏ) | Lãi 18,6% | **Lỗ 3,4%** |

- Đơn nhỏ tiêu tốn **5.475.000** overhead (≈ 39% giá bán) nhưng Traditional chỉ tính 2.400.000 vì chỉ nhìn giờ máy (12 giờ), bỏ qua việc đơn này cần 6 lần setup và 3 mẫu thiết kế.
- Đơn lớn bị Traditional "gánh dư" overhead (24.000.000 so với 11.050.000 thực tế) — nghĩa là xưởng đang **trợ giá chéo**: khách lớn đang trả hộ chi phí phục vụ khách nhỏ. Nếu khách lớn so sánh giá và chuyển sang đối thủ, xưởng mất phần lợi nhuận chính.

#### Bước 6 – Quyết định & tái định giá

Giá tối thiểu để đơn nhỏ đạt biên lãi 15% (theo giá thành ABC 14.475.000):

$$\text{Giá} = \frac{14.475.000}{1 - 15\%} \approx 17.029.412 \text{ VNĐ}$$

→ tăng khoảng **3,03 triệu** (+21,6% so với giá hiện tại 14 triệu). Giải pháp:
1. Áp **phí setup/mẫu thiết kế** riêng (ví dụ 500.000 VNĐ/lần setup và/hoặc mẫu vượt quá 1) thay vì tăng giá hộp.
2. Quy định **số lượng đặt tối thiểu** (MOQ) hoặc giá bậc thang.
3. Gom lô: ghép nhiều đơn nhỏ cùng loại giấy/màu để chia sẻ setup.
4. Chuẩn hóa mẫu thiết kế (template) để giảm công duyệt mẫu.

#### Bước 7 – Xử lý under-applied overhead cuối năm

Cuối năm: MOH thực tế 972.000.000; giờ máy thực tế 4.700.

- MOH phân bổ (Traditional) = 4.700 × 200.000 = 940.000.000
- Under-applied = 972.000.000 − 940.000.000 = **32.000.000**

Nếu coi là không trọng yếu, ghi: Nợ 632 / Có 627 = 32.000.000. Nếu trọng yếu so với lợi nhuận, phân bổ lại theo số dư WIP/thành phẩm/giá vốn. Nguyên nhân under: giờ máy thực tế (4.700) thấp hơn dự kiến (4.800) trong khi định phí không giảm → xưởng chạy dưới công suất. Đây cũng là tín hiệu cho thấy cần thêm đơn có lãi chứ không chỉ "đủ giờ máy".

#### Bài học

> 1. **Biên lãi trên giấy do Traditional Costing có thể đẹp giả** khi phân bổ MOH theo một tiêu thức không phản ánh nguồn gốc phát sinh chi phí.
> 2. **Khách hàng/đơn hàng nhỏ, phức tạp thường là nguồn rò rỉ lợi nhuận** — cần phí dịch vụ hoặc MOQ.
> 3. **Một SME không cần ABC toàn công ty**: chỉ cần 3–4 hoạt động tốn kém nhất, dữ liệu lấy từ phiếu giao việc/Excel là đủ.
> 4. Tổng lợi nhuận không đổi khi đổi phương pháp phân bổ — giá trị nằm ở **quyết định đúng** (giá, mix sản phẩm, khách hàng).

---

## IV. ỨNG DỤNG CHO SME

### 1. Chọn phương pháp theo loại hình SME Việt Nam

| Ngành | Phương pháp phù hợp | Lý do |
|-------|---------------------|-------|
| Xây dựng, nội thất theo đơn | Job Costing | Mỗi công trình/đơn là một job |
| In ấn, bao bì | Job Costing (+ ABC cho overhead) | Mỗi đơn khác nhau, nhiều setup |
| Phát triển phần mềm, agency, tư vấn | Job Costing (theo giờ công dự án) | Mỗi dự án riêng; chi phí chủ yếu là nhân sự |
| Thực phẩm & đồ uống đóng gói | Process Costing | Sản xuất hàng loạt |
| Hóa chất, nhựa, vật liệu xây dựng | Process Costing | Sản xuất liên tục |
| Dệt may, giày da | Process + Job | Hàng loạt + đơn đặt riêng |
| Nhà hàng, cà phê | Food costing theo món + P&L theo chi nhánh/kênh | Biến phí NVL chính, định phí thuê/nhân sự |
| E-commerce, logistics | ABC / TDABC | Cần biết cost per order chi tiết |
| Ngân hàng, bảo hiểm, bệnh viện | ABC | Chi phí gián tiếp lớn |

### 2. Lộ trình áp dụng theo giai đoạn phát triển

```
  Startup ──────► Tăng trưởng ──────► Trưởng thành
     │                │                    │
  Excel đơn giản    Job/Process         ABC (3-5 hoạt động)
  Biến phí/SP       + POHR              + TDABC
  CM/unit           + Budget variance    + Target Costing
  Giá vốn từng món                       + Kaizen Costing
```

### 3. Khi nào KHÔNG nên (hoặc chưa nên) dùng ABC?

| Tình huống | Lý do |
|-----------|-------|
| DN nhỏ, 1–2 sản phẩm | Overhead phân bổ đơn giản, ABC không bổ sung giá trị |
| Overhead < ~10% tổng chi phí (ngưỡng tham khảo) | Chênh lệch Traditional vs ABC không đáng kể |
| Không có dữ liệu hoạt động | Không xác định được cost driver |
| Văn hóa DN kháng cự thay đổi | Triển khai thất bại nếu không có buy-in |

### 4. Lỗi thường gặp (Common mistakes)

| Lỗi | Hậu quả | Cách tránh |
|-----|---------|-----------|
| Phân bổ MOH theo doanh thu hoặc 1 tiêu thức tùy tiện | Sai lệch giá thành, trợ giá chéo | Chọn driver có quan hệ nhân quả |
| Không kiểm tra POHR cuối kỳ (under/over-applied) | Giá vốn sai, lợi nhuận bị bóp méo | Đối chiếu định kỳ; điều chỉnh POHR khi lệch >5% (ngưỡng tham khảo) |
| Dồn toàn bộ MOH vào giá thành dù chạy dưới công suất | Giá thành đội cao, báo giá mất cạnh tranh | Phân bổ theo công suất bình thường; phần dư vào giá vốn |
| Tính EU như nhau cho NVL và chế biến | Sai giá thành WIP | Tách EU theo từng yếu tố chi phí |
| Bỏ sản phẩm dựa trên % margin | Mất đóng góp vào định phí | Xét định phí tránh được và chi phí cơ hội |
| Triển khai ABC quá chi tiết (hàng chục hoạt động) | Tốn công, nhanh lỗi thời | Bắt đầu 3–5 hoạt động lớn nhất; dùng TDABC |
| Mở rộng khi chưa biết P&L từng chi nhánh/sản phẩm | Nhân rộng lỗ | Tính lãi/lỗ và điểm hòa vốn từng đơn vị trước khi scale |

### 5. Gắn với báo cáo tài chính & thuế tại Việt Nam (cần xác nhận hiện hành)

- Hàng tồn kho và giá vốn lập theo VAS 02 / chế độ kế toán DN (Thông tư 200/2014/TT-BTC, hoặc Thông tư 133/2016/TT-BTC cho DN nhỏ và vừa — **cần xác nhận văn bản còn hiệu lực/sửa đổi**).
- Phương pháp tính giá xuất kho (bình quân gia quyền, nhập trước xuất trước, thực tế đích danh) phải áp dụng nhất quán.
- Chi phí được trừ khi tính thuế TNDN có điều kiện về hóa đơn, chứng từ và định mức hợp lý — **cần tham vấn kế toán/thuế**.
- Giá thành quản trị (ABC, TDABC) dùng cho quyết định nội bộ; có thể khác giá thành báo cáo tài chính — cần có bảng đối chiếu.

---

## V. TOOLS & TEMPLATES

### 1. Phần mềm kế toán/quản lý tại Việt Nam (giá mang tính tham khảo — **ước tính, cần xác nhận với nhà cung cấp**)

| Phần mềm | Công dụng liên quan giá thành | Giá tham khảo (ước tính, cần xác nhận) | Phù hợp |
|----------|-------------------------------|-----------------------------------------|---------|
| **MISA SME / MISA AMIS Kế toán** | Tính giá thành sản xuất (theo đơn hàng, công đoạn), phân bổ chi phí chung, hạch toán TK 621/622/627/154 | Khoảng vài triệu đến hơn chục triệu VNĐ/năm tùy gói và số người dùng | SME sản xuất, thương mại |
| **FAST Accounting** | Giá thành sản xuất, kế toán quản trị, nhiều phân hệ | Thường tính theo gói/triển khai, từ vài chục triệu VNĐ (báo giá riêng) | DN vừa |
| **KiotViet / Sapo / iPOS** | Quản lý kho, giá vốn nguyên liệu, công thức (BOM) cho F&B/bán lẻ | Từ khoảng vài trăm nghìn VNĐ/tháng | Cửa hàng, quán cà phê/nhà hàng |
| **Excel / Google Sheets** | Job Cost Sheet, POHR, ABC, TDABC | Miễn phí – Microsoft 365/Google Workspace (trả phí) | Mọi SME |
| **Power BI / Looker Studio** | Dashboard biên lãi theo sản phẩm/khách hàng | Miễn phí – gói trả phí | DN có dữ liệu |

### 2. Template Job Cost Sheet (Excel/Google Sheets)

| Cột | Nội dung |
|-----|---------|
| A | Mã Job, ngày mở/đóng, khách hàng |
| B | NVL: mã vật tư, số lượng, đơn giá, thành tiền |
| C | Nhân công: loại thợ, giờ, đơn giá, thành tiền |
| D | MOH áp dụng = POHR × giờ (hoặc driver) |
| E | Tổng giá thành, giá bán, lãi gộp, % lãi |
| F | So sánh giá báo ban đầu vs giá thành thực tế (chênh lệch) |

### 3. Template ABC cho SME (5 bước trong Sheets)

1. **Sheet "Pools"**: liệt kê hoạt động & chi phí (từ sổ chi tiết).
2. **Sheet "Drivers"**: số lượng driver cho từng sản phẩm/khách hàng.
3. **Sheet "Rates"**: Rate = Pool/Total driver.
4. **Sheet "Allocation"**: ma trận sản phẩm × hoạt động (rate × driver).
5. **Sheet "Compare"**: Traditional vs ABC; kiểm tra tổng phân bổ = tổng MOH.

### 4. Công thức Excel gợi ý

| Mục đích | Công thức |
|----------|----------|
| POHR | `=SUM(MOH_est)/SUM(Base_est)` |
| MOH áp dụng | `=POHR*Actual_Base` |
| Under/Over-applied | `=Actual_MOH - Applied_MOH` (dương = under) |
| Equivalent Units | `=Completed + WIP_end*Pct` |
| Activity rate | `=Pool/Total_Driver` |
| Check phân bổ | `=SUM(Allocated)-SUM(Pools)` (phải = 0) |

---

## VI. BÀI TẬP THỰC HÀNH

### Bài 1 (Cơ bản – POHR và Under/Over-applied)
Xưởng cơ khí ước tính MOH cả năm 480.000.000 và 8.000 giờ lao động trực tiếp. Thực tế: MOH 470.000.000; 7.600 giờ. (a) Tính POHR. (b) MOH áp dụng cả năm. (c) Under hay over-applied bao nhiêu? Bút toán xử lý nếu không trọng yếu?

**Gợi ý đáp số (đã verify):** (a) 480.000.000/8.000 = **60.000/giờ**. (b) 7.600 × 60.000 = **456.000.000**. (c) 470.000.000 − 456.000.000 = **14.000.000 under-applied**; Nợ 632 / Có 627 = 14.000.000.

### Bài 2 (Cơ bản – Process Costing, Weighted Average)
Công đoạn pha trộn: hoàn thành 2.000 đơn vị; WIP cuối 500 đơn vị (NVL 100%, chế biến 60%). Tổng NVL 50.000.000; tổng chế biến 36.800.000 (đã gồm WIP đầu kỳ). Tính EU, giá thành đơn vị, giá trị thành phẩm và WIP cuối.

**Gợi ý đáp số:** EU NVL = 2.000 + 500 = 2.500 → 20.000/EU. EU chế biến = 2.000 + 300 = 2.300 → 16.000/EU. Giá thành đơn vị = **36.000**. Thành phẩm = 2.000 × 36.000 = **72.000.000**. WIP cuối = 500 × 20.000 + 300 × 16.000 = 10.000.000 + 4.800.000 = **14.800.000**. Tổng = 86.800.000 = 50.000.000 + 36.800.000 ✓.

### Bài 3 (Trung bình – ABC cho cửa hàng quà tặng)
Cửa hàng quà tặng có MOH 100.000.000/tháng: đóng gói 40.000.000 (driver: 2.000 gói) và giao hàng 60.000.000 (driver: 1.000 chuyến). Khách sỉ: doanh thu 600 triệu, 300 gói, 100 chuyến. Khách lẻ: doanh thu 400 triệu, 1.700 gói, 900 chuyến. So sánh phân bổ MOH nếu (a) chia theo doanh thu; (b) dùng ABC.

**Gợi ý đáp số:** Rate đóng gói = 20.000/gói; giao hàng = 60.000/chuyến. (a) Theo doanh thu: sỉ 60.000.000, lẻ 40.000.000. (b) ABC: sỉ = 300 × 20.000 + 100 × 60.000 = **12.000.000**; lẻ = 1.700 × 20.000 + 900 × 60.000 = 34.000.000 + 54.000.000 = **88.000.000**; tổng 100.000.000 ✓. Khách lẻ tốn gấp ≈ 7,3 lần dù doanh thu thấp hơn → cần phí giao hàng/mức đơn tối thiểu.

### Bài 4 (Trung bình – TDABC)
Bộ phận CSKH chi phí 54.000.000/tháng, công suất thực tế 36.000 phút. Một cuộc gọi hỗ trợ 6 phút, ticket email 3 phút. Tháng này: 3.000 cuộc gọi và 4.000 email. Tính chi phí/phút, chi phí mỗi loại, mức sử dụng công suất và công suất nhàn rỗi.

**Gợi ý đáp số:** 1.500/phút. Cuộc gọi = 6 × 1.500 = 9.000; email = 3 × 1.500 = 4.500. Thời gian dùng = 3.000×6 + 4.000×3 = 18.000 + 12.000 = 30.000 phút → sử dụng 83,3%; nhàn rỗi 6.000 phút = **9.000.000**.

### Bài 5 (Trung bình – Target Costing)
Giá thị trường chấp nhận 450.000, muốn biên lợi nhuận 25% trên giá bán. Chi phí hiện tại 360.000. Tính target cost và khoảng cách cần cắt giảm.

**Gợi ý đáp số:** Target cost = 450.000 × 75% = **337.500**; khoảng cách = 360.000 − 337.500 = **22.500** (6,25% chi phí hiện tại).

### Bài 6 (Nâng cao – Mini case: Quán/Chuỗi cà phê)
Chuỗi cà phê có chi nhánh với định phí 90 triệu/tháng, giá trung bình 60.000/ly, biến phí 24.000/ly. (a) Điểm hòa vốn (số ly và doanh thu). (b) Nếu bán 2.000 ly/tháng thì lãi/lỗ bao nhiêu? (c) Nếu mở thêm chi nhánh có cùng cấu trúc nhưng bán 2.000 ly/tháng, quyết định có nên nhân rộng?

**Gợi ý đáp số:** CM/ly = 36.000. (a) BE = 90.000.000 / 36.000 = **2.500 ly**, doanh thu = **150.000.000**. (b) 2.000 ly: CM = 72.000.000 − 90.000.000 = **−18.000.000** (lỗ). (c) Không nên nhân rộng nếu chưa chứng minh được chi nhánh đạt ≥ 2.500 ly/tháng — cần cải thiện trước (tăng lưu lượng, giảm định phí) rồi mới scale.

### Bài 7 (Nâng cao – Tự thực hành)
Chọn 5 đơn hàng/sản phẩm gần nhất của doanh nghiệp bạn: (1) lập Job Cost Sheet; (2) tính POHR theo giờ công; (3) chọn 3 hoạt động tốn kém nhất và làm ABC; (4) so sánh biên lãi theo hai cách và đề xuất 2 hành động (tăng giá, đổi mix, giảm setup…).

---

## PHỤ LỤC: CHECKLIST COST ACCOUNTING TỔNG HỢP

```
PHÂN LOẠI & NỀN TẢNG:
□ Đã phân biệt chi phí sản phẩm (DM, DL, MOH) và chi phí thời kỳ (bán hàng, quản lý)?
□ Đã phân loại chi phí trực tiếp / gián tiếp, biến phí / định phí?
□ Biết dòng chi phí: 621/622/627 → 154 → 155 → 632 (kê khai thường xuyên)?
□ Phương pháp tính giá xuất kho áp dụng nhất quán? (cần xác nhận quy định hiện hành)

JOB COSTING:
□ Mỗi đơn có Job Cost Sheet riêng?
□ POHR tính từ ước tính đầu kỳ, base có quan hệ nhân quả với MOH?
□ Đối chiếu MOH áp dụng vs thực tế cuối kỳ (under/over-applied)?
□ Có so sánh giá báo vs giá thành thực tế sau mỗi job?

PROCESS COSTING:
□ Số lượng đầu vào = đầu ra (cân đối đơn vị)?
□ Tính EU riêng cho NVL và chi phí chế biến?
□ Tổng chi phí phân bổ = tổng chi phí tập hợp (kiểm tra cân)?
□ Chọn Weighted Average hay FIFO phù hợp biến động giá?

ABC / TDABC:
□ Overhead chiếm tỷ trọng đủ lớn (ngưỡng tham khảo >30%) để xứng đáng làm ABC?
□ Đã chọn 3–5 hoạt động lớn nhất, driver có dữ liệu thu thập được?
□ Tổng chi phí sau phân bổ ABC = tổng MOH?
□ Đã so sánh Traditional vs ABC và xác định sản phẩm/khách hàng bị trợ giá chéo?
□ Có tính công suất nhàn rỗi (nếu dùng TDABC)?

QUYẾT ĐỊNH:
□ Đã tính điểm hòa vốn từng sản phẩm/chi nhánh trước khi mở rộng?
□ Có phí dịch vụ/MOQ cho đơn nhỏ, phức tạp?
□ Có Target Costing khi thiết kế sản phẩm mới, Kaizen Costing khi đã sản xuất?
□ Quyết định cắt sản phẩm dựa trên chi phí tránh được, không chỉ % margin?
□ Giá thành quản trị đối chiếu được với giá thành báo cáo tài chính?
```

**Công thức tổng hợp:**

| Chỉ tiêu | Công thức |
|----------|----------|
| POHR | Estimated MOH / Estimated Allocation Base |
| MOH áp dụng | POHR × Actual Activity |
| Under/Over-applied | Actual MOH − Applied MOH (dương = under) |
| Equivalent Units (BQGQ) | Units completed + WIP end × %Completion (tính riêng NVL & chế biến) |
| Activity Rate (ABC) | Activity Cost Pool / Total Cost Driver |
| Chi phí/phút (TDABC) | Total department cost / Practical capacity (minutes) |
| Target Cost | Target Price − Target Profit |
| Variable vs Absorption | Chênh lệch lợi nhuận = Δ tồn kho × định phí SX chung/đơn vị |
| BE (số lượng) | Fixed costs / (Price − Variable cost per unit) |

---

*Tài liệu tham khảo: Horngren, Datar & Rajan – "Cost Accounting: A Managerial Emphasis" (16th Ed); Kaplan & Cooper – "Cost and Effect: Using Integrated Cost Systems" (ABC); Kaplan & Anderson – "Time-Driven Activity-Based Costing" (TDABC); Johnson & Kaplan – "Relevance Lost" (1987); Hilton & Platt – "Managerial Accounting: Creating Value in a Dynamic Business Environment"; CMA (IMA) Part 1; CIMA – Management Accounting; VAS 02 – Hàng tồn kho; Thông tư 200/2014/TT-BTC, Thông tư 133/2016/TT-BTC (cần xác nhận hiện hành); Toyota – Target Costing & Kaizen Costing; HP ABC case – Harvard Business Review (cần đối chiếu nguồn)*
