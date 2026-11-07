# Budgeting & Forecasting – Lập Ngân Sách & Dự Báo

> **Mục tiêu**: Hiểu bản chất và logic của lập ngân sách (Budgeting) và dự báo (Forecasting) — từ Master Budget, Flexible Budget, Zero-Based Budgeting, Rolling Forecast đến các mô hình dự báo định lượng (trung bình di động, san mũ, hồi quy, mùa vụ) và phân tích chênh lệch (Variance Analysis) — để chủ SME Việt Nam tự dựng được ngân sách, dòng tiền 13 tuần và hệ thống cảnh báo sớm cho doanh nghiệp của mình.

> **Quy ước trình bày**: Đơn vị tiền tệ mặc định là **triệu đồng (tr)** trừ khi ghi rõ khác. Số thập phân dùng dấu phẩy, hàng nghìn dùng dấu chấm. Mọi số liệu của doanh nghiệp tự đặt tên trong tài liệu này là **giả định minh họa** (không phải số liệu thật), đã được kiểm tra nhất quán số học bằng Python. Số liệu về công ty thật (Unilever, Sears...) trích từ trí nhớ/nguồn công khai và đều ghi chú **cần đối chiếu nguồn**. Mọi quy định pháp lý/thuế nêu ở mức nguyên tắc và gắn **cần xác nhận hiện hành**.

---

## I. KHÁI NIỆM & LÝ THUYẾT

### 1. Định nghĩa

**Lập ngân sách (Budgeting)** là quá trình **chuyển chiến lược và mục tiêu thành kế hoạch tài chính bằng con số cụ thể** cho một khoảng thời gian (thường 1 năm, chia nhỏ theo quý/tháng): doanh thu dự kiến, chi phí được phép chi, lợi nhuận mục tiêu, dòng tiền và nhu cầu vốn. Ngân sách vừa là **bản đồ** (đi đâu), vừa là **thước đo** (đã đi đến đâu) và vừa là **cam kết** (ai chịu trách nhiệm về con số nào).

**Dự báo (Forecasting)** là quá trình **ước tính kết quả có nhiều khả năng xảy ra nhất** dựa trên dữ liệu lịch sử, xu hướng và các giả định về tương lai. Dự báo trả lời câu hỏi "*nếu mọi thứ tiếp diễn như hiện tại và những thay đổi ta biết trước, chuyện gì sẽ xảy ra?*" — nó không phải là mục tiêu, nên được phép (và nên) cập nhật liên tục khi thực tế thay đổi.

> **"A budget tells your money where to go instead of wondering where it went."** – Dave Ramsey

### 2. Tại sao doanh nghiệp cần cả hai? — Bối cảnh lịch sử

**Ngân sách doanh nghiệp ra đời từ ngân sách nhà nước.** Khái niệm "budget" bắt nguồn từ chính phủ: Đạo luật Ngân sách và Kế toán Hoa Kỳ năm 1921 (Budget and Accounting Act) lần đầu buộc Tổng thống Mỹ phải trình một ngân sách thống nhất lên Quốc hội. Gần như cùng thời, các tập đoàn lớn như General Electric, DuPont và General Motors (những năm 1920) đưa kỹ thuật này vào doanh nghiệp để giải quyết một bài toán cụ thể: *khi công ty lớn lên với nhiều bộ phận, ai đó phải phối hợp để phòng sản xuất không làm ra nhiều hơn mức phòng bán hàng bán được, và phòng mua hàng không mua nguyên liệu vượt quá khả năng chi trả của công ty*. Năm 1922, James O. McKinsey (người sáng lập McKinsey & Company) xuất bản cuốn "Budgetary Control", hệ thống hóa ngân sách thành công cụ kiểm soát quản trị. *(Mốc năm trích từ tài liệu kinh điển về lịch sử kế toán quản trị — cần đối chiếu nguồn nếu trích dẫn học thuật.)*

**Vấn đề của ngân sách cứng nhắc dẫn tới dự báo cuốn chiếu.** Ngân sách năm lập vào quý IV năm trước, nhưng thị trường thay đổi hàng tháng. Từ thập niên 1990, nhiều doanh nghiệp nhận ra: ngân sách lập xong là đã lỗi thời sau 3 tháng, nhưng vẫn bị dùng làm thước đo thưởng phạt — khiến nhà quản lý "chơi" con số thay vì hành động đúng. Phản ứng thứ nhất là **dự báo cuốn chiếu (Rolling Forecast)** — luôn nhìn 12 tháng phía trước thay vì dừng ở 31/12. Phản ứng cực đoan hơn là **Beyond Budgeting** (Jeremy Hope & Robin Fraser, nhóm BBRT thành lập khoảng cuối thập niên 1990) với hình mẫu ngân hàng Thụy Điển Svenska Handelsbanken, nổi tiếng vì từ bỏ ngân sách truyền thống từ thập niên 1970 *(cần đối chiếu nguồn)*.

**Kết luận thực tiễn:** ngân sách và dự báo **không thay thế nhau mà bổ sung nhau** — ngân sách giữ "tính cam kết và trách nhiệm", dự báo giữ "tính cập nhật và thực tế".

### 3. Phân biệt Budget vs Forecast

| Tiêu chí | Budget (Ngân sách) | Forecast (Dự báo) |
|----------|--------------------|-------------------|
| **Trả lời câu hỏi** | "Ta *muốn/cam kết* đạt gì?" | "Ta *nhiều khả năng* đạt gì?" |
| **Mục đích** | Kế hoạch, phân bổ nguồn lực & kiểm soát | Dự đoán & điều chỉnh sớm |
| **Thời gian** | Thường 1 năm, cố định | Liên tục cập nhật (rolling) |
| **Tần suất lập** | 1 lần/năm | Hàng tháng/quý |
| **Phê duyệt** | Cần lãnh đạo phê duyệt (có tính cam kết) | Không nhất thiết |
| **Độ chi tiết** | Rất chi tiết (từng dòng chi phí, từng bộ phận) | Tổng quát hơn (theo yếu tố dẫn dắt – driver) |
| **Linh hoạt** | Cứng (target cố định) | Mềm (điều chỉnh liên tục) |
| **Đánh giá hiệu suất** | Dùng làm chuẩn so sánh (benchmark) | Không dùng để thưởng phạt |

### 4. Vai trò của Budgeting (6 chức năng)

```
┌──────────────────────────────────────────────────┐
│           VAI TRÒ CỦA BUDGETING                  │
│                                                  │
│  ┌─────────────┐  ┌──────────────┐               │
│  │ PLANNING    │  │ COMMUNICATION│               │
│  │ Lập kế hoạch│  │ Truyền thông │               │
│  │ chiến lược  │  │ mục tiêu     │               │
│  └──────┬──────┘  └──────┬───────┘               │
│         │                │                       │
│  ┌──────▼──────┐  ┌──────▼───────┐               │
│  │ COORDINATION│  │ MOTIVATION   │               │
│  │ Phối hợp    │  │ Tạo động lực │               │
│  │ các bộ phận │  │ đạt target   │               │
│  └──────┬──────┘  └──────┬───────┘               │
│         │                │                       │
│  ┌──────▼──────┐  ┌──────▼───────┐               │
│  │ CONTROL     │  │ EVALUATION   │               │
│  │ Kiểm soát   │  │ Đánh giá     │               │
│  │ chi tiêu    │  │ hiệu suất    │               │
│  └─────────────┘  └──────────────┘               │
└──────────────────────────────────────────────────┘
```

| Chức năng | Vấn đề kinh doanh giải quyết | Ví dụ trong SME |
|-----------|-------------------------------|------------------|
| Planning | Biến chiến lược thành hành động có con số | Mục tiêu "mở thêm 1 chi nhánh" thành khoản chi 800tr và 6 tháng dòng tiền |
| Communication | Mọi người biết mục tiêu chung | Trưởng ca biết quán cần bán 55 triệu/ngày mới hòa vốn |
| Coordination | Các bộ phận không "kéo ngược" nhau | Kho không nhập hàng gấp đôi nhu cầu bán |
| Motivation | Mục tiêu rõ ràng kích thích nỗ lực | Thưởng khi vượt ngân sách lợi nhuận |
| Control | Phát hiện chi vượt sớm | Marketing chi 60% ngân sách trong quý I |
| Evaluation | Đánh giá công bằng người quản lý | So thực tế với ngân sách *linh hoạt*, không so với ngân sách tĩnh |

### 5. Bối cảnh Việt Nam: ngân sách thuộc "kế toán quản trị", không phải nghĩa vụ báo cáo

Tại Việt Nam, kế toán được chia thành **kế toán tài chính** (lập báo cáo tài chính cho cơ quan thuế, ngân hàng, cổ đông theo **Chuẩn mực Kế toán Việt Nam – VAS** và chế độ kế toán doanh nghiệp, ví dụ **Thông tư 200/2014/TT-BTC**; doanh nghiệp nhỏ và vừa có thể áp dụng Thông tư 133/2016/TT-BTC) và **kế toán quản trị** (phục vụ nội bộ ra quyết định, Luật Kế toán 2015 cho phép doanh nghiệp tự tổ chức). **Lập ngân sách thuộc kế toán quản trị**: pháp luật không bắt buộc doanh nghiệp tư nhân phải lập ngân sách hay có mẫu biểu cố định, nên chủ SME hoàn toàn tự do thiết kế — nhưng cũng chính vì thế mà dễ bỏ qua.

Ba điểm giao nhau giữa ngân sách nội bộ và quy định kế toán/thuế mà người lập ngân sách cần biết (ở mức nguyên tắc, **cần xác nhận hiện hành** với kế toán trưởng/tư vấn thuế):

1. **Nguyên tắc dồn tích (Accrual)**: Báo cáo kết quả kinh doanh ghi nhận doanh thu/chi phí khi phát sinh, không phải khi thu/chi tiền. Do đó ngân sách lợi nhuận (P&L budget) khác ngân sách tiền mặt (Cash Budget) — sai lầm kinh điển của SME là chỉ nhìn lợi nhuận mà quên tiền (xem mục II.A.5).
2. **Khấu hao TSCĐ**: là chi phí hợp lý nhưng không phải dòng tiền ra; ngân sách cần tách rõ. Mức trích và thời gian khấu hao tối thiểu/tối đa theo quy định kế toán/thuế hiện hành (cần xác nhận).
3. **Chi phí được trừ khi tính thuế TNDN**: chi phí phải có hóa đơn, chứng từ hợp lệ (hóa đơn điện tử) và liên quan đến hoạt động sản xuất kinh doanh. Thuế suất TNDN phổ thông trong tài liệu này giả định **20%** (có thể có chính sách ưu đãi/thuế suất riêng cho doanh nghiệp nhỏ; cần xác nhận hiện hành).

Về **IFRS**: Việt Nam có lộ trình áp dụng chuẩn mực báo cáo tài chính quốc tế (cần xác nhận hiện hành); với SME, chưa bắt buộc, nhưng ngân sách xây dựng theo tư duy dồn tích & bản chất kinh tế (thay vì tư duy thu-chi tiền mặt thuần túy) sẽ dễ chuyển đổi hơn về sau.

### 6. Tại sao ngân sách có thể phản tác dụng? — Mặt tâm lý & hành vi

Chris Argyris (Đại học Harvard, 1952) trong nghiên cứu "The Impact of Budgets on People" là một trong những người đầu tiên chỉ ra: **khi ngân sách bị dùng làm công cụ gây áp lực và thưởng phạt, con người sẽ "chơi" ngân sách thay vì phục vụ mục tiêu thật của công ty.** Các hành vi phổ biến:

| Hành vi | Mô tả | Hậu quả | Cách giảm thiểu |
|---------|-------|---------|-----------------|
| **Budget slack / padding** | Quản lý khai chi phí cao, doanh thu thấp để dễ đạt | Lãng phí có hệ thống | ZBB, benchmark ngoài, thương lượng có dữ liệu |
| **Sandbagging** | Cố tình đặt target thấp để vượt thưởng | Mất cơ hội tăng trưởng | Target dựa trên dữ liệu thị trường |
| **Spend it or lose it** | Cuối năm chi vội cho hết ngân sách kẻo năm sau bị cắt | Chi phí không tạo giá trị | Cho phép chuyển số dư có điều kiện |
| **Ratchet effect** | Vượt target năm nay → năm sau target bị nâng | Người giỏi giấu bớt thành tích | Tách thưởng khỏi mốc ngân sách cứng |
| **Short-termism** | Cắt đào tạo/bảo trì để đạt lợi nhuận quý | Phá hủy giá trị dài hạn | Bổ sung KPI dài hạn (xem Balanced Scorecard) |

**Ngân sách có sự tham gia (participative budgeting)** — nhân viên cấp dưới cùng bàn bạc để đặt con số — giúp tăng cam kết nhưng làm tăng nguy cơ slack; đòi hỏi cấp trên có dữ liệu đối chiếu. Với SME ít cấp bậc, chủ doanh nghiệp là người "kiểm chứng" tốt nhất vì nắm chi tiết vận hành.

---

## II. CHI TIẾT TỪNG THÀNH PHẦN

### A. Master Budget – Ngân sách tổng thể

#### 1. Master Budget là gì và vì sao phải "nối chuỗi"?

**Master Budget** là bộ ngân sách tích hợp, kết nối mọi kế hoạch của doanh nghiệp (bán hàng, sản xuất, mua hàng, nhân công, chi phí chung, đầu tư, tiền mặt) thành **ba báo cáo tài chính dự kiến (pro-forma)**: Kết quả kinh doanh, Bảng cân đối kế toán và Dòng tiền. Chữ "pro-forma" nghĩa là "theo hình thức/dự kiến" — báo cáo mà ta *dựng trước* khi sự việc xảy ra.

**Tại sao phải nối chuỗi thay vì lập từng bảng riêng?** Vì ngân sách các bộ phận *phụ thuộc lẫn nhau*: bộ phận sản xuất không thể quyết định làm bao nhiêu nếu chưa biết bán bao nhiêu; bộ phận mua hàng không thể quyết định nhập bao nhiêu nếu chưa biết sản xuất bao nhiêu; giám đốc tài chính không biết cần vay bao nhiêu nếu chưa biết tiền ra – tiền vào từng quý. Nếu lập rời rạc, kết quả thường là "mâu thuẫn ngầm" — ví dụ kinh doanh đặt chỉ tiêu bán 60.000 chai nhưng nhà máy chỉ đủ công suất làm 50.000, hoặc lãi lớn trên giấy nhưng hết tiền mặt.

**Tại sao bắt đầu từ ngân sách bán hàng?** Trong hầu hết doanh nghiệp, **doanh số là "yếu tố giới hạn" (limiting factor)** — nhu cầu thị trường chứ không phải năng lực sản xuất quyết định quy mô hoạt động. Mọi thứ khác (sản lượng, nguyên liệu, nhân công, tiền thu) là hệ quả của số lượng bán. (Nếu yếu tố giới hạn là công suất máy hay nguồn nguyên liệu khan hiếm — ví dụ nhà máy luôn sản xuất hết công suất vẫn không đủ bán — thì chuỗi sẽ bắt đầu từ chính yếu tố đó.)

```
                    MASTER BUDGET
                         │
          ┌──────────────┼──────────────┐
          │              │              │
   OPERATING         FINANCIAL      CAPITAL
   BUDGET            BUDGET         BUDGET
 (Ngân sách       (Ngân sách       (Ngân sách
  hoạt động)       tài chính)       đầu tư)
          │              │              │
   ┌──────┼──────┐  ┌────┼────┐    ┌────┼────┐
   │      │      │  │    │    │    │         │
Sales  Production Cash Pro-forma CapEx    Project
Budget Budget    Budget  B/S     Budget   Budgets
   │      │         │    P&L
   │   ┌──┼──┐      │
   │   │  │  │      │
  DM  DL MOH Selling & Admin
Budget Budget Budget  Budget
```

#### 2. Quy trình 8 bước

```
  Bước 1: Sales Budget (Ngân sách bán hàng)
  ► Nền tảng – mọi budget khác đều xuất phát từ đây
       │
  Bước 2: Production Budget (Ngân sách sản xuất)
  ► Sản lượng cần SX = Bán + Tồn kho cuối kỳ − Tồn kho đầu kỳ
       │
  Bước 3: Direct Materials Budget (NVL trực tiếp)
       │
  Bước 4: Direct Labor Budget (Nhân công trực tiếp)
       │
  Bước 5: Manufacturing Overhead Budget (Chi phí SX chung)
       │
  Bước 6: Selling & Administrative Budget (Bán hàng & QLDN)
       │
  Bước 7: Cash Budget (Ngân sách tiền mặt)
  ► Tổng hợp thu – chi tiền thực tế, phát hiện nhu cầu vay
       │
  Bước 8: Pro-forma Financial Statements
  ► Báo cáo KQKD + Bảng cân đối kế toán dự kiến
```

#### 3. Ví dụ xuyên suốt: SME sản xuất nước ép "Nước Ép Xanh Việt" (giả định minh họa)

**Bối cảnh giả định:** Xưởng nước ép trái cây đóng chai, bán cho cửa hàng tiện lợi và đại lý. Năm 2026 dự kiến bán 57.000 chai (giá bán 30.000đ/chai), nhu cầu mạnh vào mùa hè (Q2–Q3) và yếu ở Q1, Q4. Dữ liệu cơ bản (tất cả là **giả định để minh họa**):

| Thông số | Giá trị | Ghi chú |
|----------|---------|---------|
| Giá bán | 30.000đ/chai | Cố định cả năm |
| Chính sách tồn kho thành phẩm | 20% nhu cầu bán quý kế tiếp | Đệm an toàn cho đơn hàng đột biến |
| Tồn kho thành phẩm đầu năm | 2.000 chai | Giá vốn biến đổi 11.500đ/chai |
| Dự kiến bán Q1/2027 | 11.000 chai | Dùng tính tồn kho cuối Q4/2026 |
| Định mức NVL | 0,5 lít nước ép nguyên liệu/chai | Giá 10.000đ/lít |
| Chính sách tồn kho NVL | 10% nhu cầu dùng quý kế tiếp | Tồn đầu năm 550 lít (≈ 5,5tr) |
| Nhân công trực tiếp | 5.000đ/chai sản xuất | Lương theo sản phẩm |
| SX chung | Biến phí 1.500đ/chai SX + định phí tiền 60tr/quý + khấu hao 4tr/quý | |
| Bán hàng biến đổi | 4.000đ/chai bán | Vận chuyển, hoa hồng đại lý |
| Bán hàng & QLDN cố định | 80tr/quý | Lương văn phòng, marketing |
| Thu tiền | 90% trong quý, 10% quý sau | Phải thu đầu năm 40tr |
| Chi tiền | Mọi chi phí trả ngay trong quý | Giả định đơn giản hóa |
| Đầu tư | Mua máy 50tr vào Q1 | Chi bằng tiền |
| Tiền đầu năm | 50tr | Vốn góp 250tr, TSCĐ ròng đầu năm 200tr |
| Vay ngắn hạn | Lãi 10%/năm; vay bội số 10tr; giữ tiền tối thiểu 20tr | Trả khi dư tiền |
| Thuế TNDN | 20% (giả định), nộp sang năm sau | Cần xác nhận hiện hành |

**Bước 1 — Ngân sách bán hàng (Sales Budget)**

| Chỉ tiêu | Q1 | Q2 | Q3 | Q4 | Cả năm |
|---|---|---|---|---|---|
| Số chai dự kiến bán | 10.000 | 15.000 | 20.000 | 12.000 | 57.000 |
| Giá bán (đ/chai) | 30.000 | 30.000 | 30.000 | 30.000 | 30.000 |
| **Doanh thu (triệu đồng)** | 300 | 450 | 600 | 360 | 1.710 |

*Diễn giải*: Doanh thu cả năm 1.710tr; riêng Q2 + Q3 chiếm 1.050/1.710 = 61,4% — dấu hiệu tính mùa vụ mạnh, ảnh hưởng đến lượng tiền cần có ở các quý đầu năm.

**Bước 2 — Ngân sách sản xuất (Production Budget)**

*Tại sao công thức là Bán + Tồn cuối − Tồn đầu?* Đây là phương trình cân bằng hàng tồn kho: **Tồn đầu + Sản xuất = Bán + Tồn cuối** → **Sản xuất = Bán + Tồn cuối − Tồn đầu**. Nếu tồn đầu kỳ đã có sẵn một phần hàng thì chỉ cần sản xuất phần thiếu; nếu muốn có đệm an toàn cuối kỳ thì phải sản xuất thêm. Chính sách tồn kho 20% nhu cầu quý sau là giải pháp cân bằng giữa hai rủi ro: tồn quá ít thì hụt hàng khi đơn tăng đột ngột (mất doanh thu), tồn quá nhiều thì chôn vốn và rủi ro hàng hết hạn (nước ép có hạn dùng ngắn).

*Tính tồn cuối kỳ*: Q1 = 20% × 15.000 = 3.000; Q2 = 20% × 20.000 = 4.000; Q3 = 20% × 12.000 = 2.400; Q4 = 20% × 11.000 = 2.200 (11.000 là bán Q1/2027 dự kiến).

| Chỉ tiêu | Q1 | Q2 | Q3 | Q4 | Cả năm |
|---|---|---|---|---|---|
| Dự kiến bán (chai) | 10.000 | 15.000 | 20.000 | 12.000 | 57.000 |
| + Tồn kho TP cuối kỳ mong muốn | 3.000 | 4.000 | 2.400 | 2.200 | 2.200 |
| − Tồn kho TP đầu kỳ | (2.000) | (3.000) | (4.000) | (2.400) | (2.000) |
| **= Sản lượng cần sản xuất (chai)** | 11.000 | 16.000 | 18.400 | 11.800 | 57.200 |

*Diễn giải*: Q3 phải sản xuất 18.400 chai (cao nhất), nhưng Q3 cũng là quý nhu cầu tồn kho thấp nhất (2.400) vì quý Q4 bán chậm lại — chính sách tồn kho "đi theo quý sau" làm đường sản xuất mượt hơn đường bán hàng một chút.

**Bước 3 — Ngân sách nguyên vật liệu trực tiếp (Direct Materials Budget)**

*Logic*: cùng phương trình tồn kho nhưng áp dụng cho nguyên liệu: Cần mua = Cần dùng + Tồn cuối − Tồn đầu. Tồn cuối kỳ = 10% nhu cầu dùng quý sau (Q4 dùng giả định Q1/2027 cần 5.500 lít).

| Chỉ tiêu | Q1 | Q2 | Q3 | Q4 | Cả năm |
|---|---|---|---|---|---|
| Sản lượng cần SX (chai) | 11.000 | 16.000 | 18.400 | 11.800 | 57.200 |
| NVL cần dùng = × 0,5 lít | 5.500 | 8.000 | 9.200 | 5.900 | 28.600 |
| + Tồn NVL cuối kỳ (10% nhu cầu kỳ sau, lít) | 800 | 920 | 590 | 550 | 550 |
| − Tồn NVL đầu kỳ (lít) | (550) | (800) | (920) | (590) | (550) |
| **= NVL cần mua (lít)** | 5.750 | 8.120 | 8.870 | 5.860 | 28.600 |
| **Chi phí mua NVL (triệu đồng, × 10.000đ/lít)** | 57,5 | 81,2 | 88,7 | 58,6 | 286 |

**Bước 4 — Ngân sách nhân công trực tiếp (Direct Labor Budget)**

| Chỉ tiêu | Q1 | Q2 | Q3 | Q4 | Cả năm |
|---|---|---|---|---|---|
| Sản lượng cần SX (chai) | 11.000 | 16.000 | 18.400 | 11.800 | 57.200 |
| **Nhân công trực tiếp (triệu đồng, × 5.000đ/chai)** | 55 | 80 | 92 | 59 | 286 |

**Bước 5 — Ngân sách chi phí sản xuất chung (Manufacturing Overhead Budget)**

*Tại sao tách biến phí/định phí?* Vì chúng hành xử khác nhau khi sản lượng thay đổi: biến phí tăng theo sản lượng (điện chạy máy, vật tư phụ), định phí không đổi trong tầm hoạt động bình thường (thuê xưởng, lương quản đốc). Tách đúng là điều kiện để làm **ngân sách linh hoạt** (mục B.4) và phân tích hòa vốn (mục C).

| Chỉ tiêu | Q1 | Q2 | Q3 | Q4 | Cả năm |
|---|---|---|---|---|---|
| Biến phí SX chung (1.500đ/chai SX) | 16,5 | 24 | 27,6 | 17,7 | 85,8 |
| Định phí SX chung bằng tiền (thuê xưởng, điện cố định, lương quản đốc) | 60 | 60 | 60 | 60 | 240 |
| **Tổng SX chung bằng tiền** | 76,5 | 84 | 87,6 | 77,7 | 325,8 |
| Khấu hao (không dùng tiền) | 4 | 4 | 4 | 4 | 16 |
| **Tổng SX chung (kể cả khấu hao)** | 80,5 | 88 | 91,6 | 81,7 | 341,8 |

**Bước 6 — Ngân sách bán hàng & quản lý doanh nghiệp (Selling & Administrative Budget)**

| Chỉ tiêu | Q1 | Q2 | Q3 | Q4 | Cả năm |
|---|---|---|---|---|---|
| Chi phí bán hàng biến đổi (4.000đ/chai bán: vận chuyển, hoa hồng đại lý) | 40 | 60 | 80 | 48 | 228 |
| Chi phí bán hàng & QLDN cố định (lương văn phòng, marketing) | 80 | 80 | 80 | 80 | 320 |
| **Tổng chi phí bán hàng & QLDN** | 120 | 140 | 160 | 128 | 548 |

**Bước 7 — Ngân sách tiền mặt (Cash Budget)**

*Tại sao cần ngân sách tiền mặt riêng, khi đã có ngân sách lợi nhuận?* Vì **lợi nhuận ≠ tiền mặt**. Doanh nghiệp bán chịu nên tiền về chậm hơn doanh thu; mua máy móc là chi tiền nhưng không phải chi phí tức thời; khấu hao là chi phí nhưng không chi tiền; tồn kho tăng là chi tiền nhưng chưa thành chi phí. Rất nhiều SME có lãi trên sổ sách nhưng **phá sản vì hết tiền** — ngân sách tiền mặt chính là công cụ phát hiện thời điểm "thiếu tiền" *trước khi nó xảy ra*, để kịp vay, thương lượng kỳ hạn thanh toán hoặc hoãn đầu tư.

Lịch thu tiền (90% trong quý, 10% sang quý sau, cộng 40tr phải thu đầu năm):

| Chỉ tiêu | Q1 | Q2 | Q3 | Q4 | Cả năm |
|---|---|---|---|---|---|
| Doanh thu quý | 300 | 450 | 600 | 360 | 1.710 |
| Thu 90% ngay trong quý | 270 | 405 | 540 | 324 | 1.539 |
| Thu 10% doanh thu quý trước | 40 | 30 | 45 | 60 | 175 |
| **Tổng thu tiền bán hàng** | 310 | 435 | 585 | 384 | 1.714 |

Ngân sách tiền mặt tổng hợp (có tính vay ngắn hạn để giữ tối thiểu 20tr):

| Chỉ tiêu | Q1 | Q2 | Q3 | Q4 | Cả năm |
|---|---|---|---|---|---|
| Tiền đầu kỳ | 50 | 21 | 50,3 | 207 | 50 |
| + Thu tiền bán hàng | 310 | 435 | 585 | 384 | 1.714 |
| − Chi mua NVL | (57,5) | (81,2) | (88,7) | (58,6) | (286) |
| − Chi nhân công trực tiếp | (55) | (80) | (92) | (59) | (286) |
| − Chi SX chung bằng tiền | (76,5) | (84) | (87,6) | (77,7) | (325,8) |
| − Chi bán hàng biến đổi | (40) | (60) | (80) | (48) | (228) |
| − Chi bán hàng & QLDN cố định | (80) | (80) | (80) | (80) | (320) |
| − Chi đầu tư máy móc (CapEx) | (50) | 0 | 0 | 0 | (50) |
| − Lãi vay ngắn hạn (10%/năm) | 0 | (0,5) | 0 | 0 | (0,5) |
| **= Tiền trước tài trợ** | 1 | 70,3 | 207 | 267,7 |  |
| + Vay ngắn hạn thêm | 20 | 0 | 0 | 0 | 20 |
| − Trả nợ vay | 0 | (20) | 0 | 0 | (20) |
| **= Tiền cuối kỳ** | 21 | 50,3 | 207 | 267,7 | 267,7 |
| Dư nợ vay cuối kỳ | 20 | 0 | 0 | 0 | 0 |

*Diễn giải*: Q1 là quý "nguy hiểm": tiền đầu kỳ 50 + thu 310 − chi 359 = chỉ còn **1tr**, thấp hơn mức tối thiểu 20tr → phải vay 20tr (làm tròn bội số 10tr). Nguyên nhân: Q1 vừa bán yếu (doanh thu 300tr), vừa phải sản xuất 11.000 chai để dựng tồn kho đón mùa hè, vừa chi mua máy 50tr. Sang Q2 thu tiền cao hơn (435tr) nên trả hết vay. Lãi vay Q2 = 20 × 10% / 4 = 0,5tr. Nếu không lập ngân sách tiền mặt, chủ xưởng sẽ chỉ thấy "năm nay lãi 200tr" và bất ngờ vì Q1 suýt cạn tiền.

**Bước 8 — Báo cáo tài chính dự kiến (Pro-forma)**

*Lưu ý phương pháp:* Để đơn giản và đồng thời phục vụ ra quyết định nội bộ, ví dụ trình bày P&L theo **cách tiếp cận "đảm phí" (variable costing / contribution format)**: chỉ biến phí tính vào giá vốn, mọi định phí sản xuất chung tính vào chi phí kỳ. **Báo cáo tài chính chính thức theo VAS/Thông tư 200 dùng phương pháp phân bổ toàn bộ (absorption costing)**, nghĩa là hàng tồn kho phải mang cả định phí sản xuất chung — kế toán trưởng cần điều chỉnh khi lập báo cáo theo quy định (cần xác nhận hiện hành). Chênh lệch giữa hai phương pháp chỉ xuất hiện khi tồn kho thay đổi (ở đây tồn kho thành phẩm tăng nhẹ 2.000 → 2.200 chai nên chênh lệch nhỏ).

Báo cáo kết quả kinh doanh dự kiến năm:

| Khoản mục | Triệu đồng | % doanh thu |
|---|---|---|
| Doanh thu (57.000 chai × 30.000đ) | 1.710 | 100,0% |
| − Giá vốn biến đổi (57.000 chai × 11.500đ) | (655,5) | 38,3% |
| − Chi phí bán hàng biến đổi | (228) | 13,3% |
| **= Số dư đảm phí (Contribution Margin)** | 826,5 | 48,3% |
| − Định phí SX chung (kể cả khấu hao 16) | (256) | 15,0% |
| − Định phí bán hàng & QLDN | (320) | 18,7% |
| **= Lợi nhuận hoạt động (EBIT)** | 250,5 | 14,6% |
| − Lãi vay | (0,5) | 0,03% |
| **= Lợi nhuận trước thuế (EBT)** | 250 | 14,6% |
| − Thuế TNDN 20% (giả định) | (50) | 2,9% |
| **= Lợi nhuận sau thuế (NI)** | 200 | 11,7% |

Bảng cân đối kế toán dự kiến (đầu năm – cuối năm):

| Khoản mục (triệu đồng) | Đầu năm (1/1) | Cuối năm (31/12) | Thay đổi |
|---|---|---|---|
| Tiền mặt | 50 | 267,7 | 217,7 |
| Phải thu khách hàng | 40 | 36 | -4 |
| Tồn kho NVL (550 lít × 10.000đ) | 5,5 | 5,5 | 0 |
| Tồn kho thành phẩm (giá biến đổi 11.500đ/chai) | 23 | 25,3 | 2,3 |
| TSCĐ ròng (200 + 50 CapEx − 16 khấu hao) | 200 | 234 | 34 |
| **TỔNG TÀI SẢN** | 318,5 | 568,5 | 250 |
| Thuế TNDN phải nộp | 0 | 50 | 50 |
| Vay ngắn hạn | 0 | 0 | 0 |
| Vốn chủ sở hữu (vốn góp 250 + LN giữ lại) | 318,5 | 518,5 | 200 |
| **TỔNG NGUỒN VỐN** | 318,5 | 568,5 | 250 |

Bảng đã **cân**: Tổng tài sản cuối năm 568,5tr = Thuế phải nộp 50 + Vay 0 + Vốn chủ sở hữu 518,5.

**Đối chiếu dòng tiền với lợi nhuận** (tại sao lãi 200tr nhưng tiền chỉ tăng 217,7tr?):

| Bước đối chiếu | Triệu đồng |
|---|---|
| Lợi nhuận sau thuế | 200 |
| + Khấu hao (chi phí không dùng tiền) | 16 |
| + Giảm phải thu (40 → 36) | 4 |
| − Tăng tồn kho thành phẩm (23 → 25,3) | (2,3) |
| + Thuế TNDN chưa nộp (ghi nhận chi phí nhưng chưa chi tiền) | 50 |
| − CapEx | (50) |
| **= Thay đổi tiền thuần** | 217,7 |
| Kiểm tra: tiền cuối 267,7 − tiền đầu 50 | 217,7 |

*Ý nghĩa*: Tiền tăng 217,7tr khớp với chênh lệch giữa tiền cuối kỳ (267,7) và đầu kỳ (50). Lợi nhuận 200 cộng khấu hao 16 (không phải tiền ra), cộng 50 thuế chưa nộp, trừ 50 đầu tư máy... — đây là cách chuyển từ "lợi nhuận" sang "dòng tiền" mà mọi chủ SME cần nắm.

**Điểm hòa vốn năm** của xưởng: Định phí = 240 (SX chung tiền) + 16 (khấu hao) + 320 (bán hàng & QLDN) = 576tr; tỷ lệ số dư đảm phí = 826,5 / 1.710 = 48,3% → Doanh thu hòa vốn = 576 / 0,4833 = **1.191,7tr** (≈ 39.724 chai), tức biên an toàn (margin of safety) = (1.710 − 1.191,7)/1.710 = **30,3%**. Doanh thu có thể sụt tới 30% mà xưởng chưa lỗ hoạt động.

---

### B. Các phương pháp lập ngân sách

#### 1. Bức tranh tổng thể: tại sao có nhiều phương pháp?

Mỗi phương pháp ra đời để chữa một "bệnh" của phương pháp trước: **Incremental** nhanh nhưng tích lũy lãng phí → **ZBB** loại lãng phí nhưng tốn công → **Flexible** sửa lỗi "đánh giá sai khi sản lượng thay đổi" → **Rolling** sửa lỗi "ngân sách lỗi thời" → **Beyond Budgeting** từ bỏ luôn con số cứng.

| Phương pháp | Cách tiếp cận | Ưu điểm | Nhược điểm | Phù hợp |
|-------------|---------------|---------|------------|---------|
| **Incremental** | Ngân sách năm trước ± % | Đơn giản, nhanh | Giữ nguyên bất hợp lý, không tối ưu | DN ổn định, ít cạnh tranh |
| **Zero-Based (ZBB)** | Bắt đầu từ 0, phải giải trình mọi khoản | Loại bỏ lãng phí | Tốn rất nhiều thời gian | Cần cắt giảm/tái cơ cấu |
| **Activity-Based (ABB)** | Ngân sách theo hoạt động và yếu tố dẫn dắt | Chính xác, gắn với đầu ra | Phức tạp, cần hệ thống ABC | DN lớn |
| **Flexible Budget** | Điều chỉnh theo sản lượng thực tế | So sánh công bằng | Phức tạp hơn tĩnh | Sản lượng biến động |
| **Rolling Budget/Forecast** | Luôn có 12 tháng phía trước | Luôn hướng về tương lai | Tốn công cập nhật | Mọi DN muốn thích ứng |
| **Driver-based** | Ngân sách từ yếu tố dẫn dắt (số khách, kg, giờ máy) | Gắn với hành vi kinh doanh thật | Cần dữ liệu driver tốt | SME có số liệu bán hàng |
| **Beyond Budgeting** | Bỏ ngân sách cứng, dùng KPI tương đối & dự báo | Linh hoạt, phi tập trung | Cần văn hóa mạnh, khó kiểm soát | DN đổi mới, văn hóa tin tưởng |

#### 2. Incremental Budgeting – Ngân sách tăng dần

**Logic:** lấy ngân sách (hoặc chi tiêu thực tế) năm trước, cộng/trừ một tỷ lệ phần trăm (thường lạm phát + tăng trưởng). **Tại sao phổ biến?** Vì nhanh, ít tranh cãi, và dựa trên giả định "năm ngoái đã hợp lý". **Nguy hiểm:** sai lầm năm trước được nhân bản mãi; khoản chi vô ích không bao giờ bị hỏi lại; và khi môi trường thay đổi mạnh (như Sears – case III.2) sẽ giữ doanh nghiệp "chết chậm".

#### 3. Zero-Based Budgeting (ZBB) – Ngân sách từ gốc

**Nguồn gốc:** Peter Pyhrr, một kế toán viên của Texas Instruments, đề xuất vào cuối thập niên 1960 – đầu 1970 và công bố trên Harvard Business Review (1970); sau đó được Thống đốc Jimmy Carter áp dụng ở bang Georgia (đầu thập niên 1970) và mang vào chính quyền liên bang Mỹ khi Carter làm Tổng thống (1977) *(cần đối chiếu nguồn)*. Bối cảnh: các phòng ban hỗ trợ (dịch vụ, hành chính) cứ phình ra vì ngân sách tăng dần, không ai chứng minh được giá trị chúng tạo ra.

**Tư tưởng lõi:** "Chi phí không có quyền tồn tại mặc nhiên." Mỗi khoản phải được **biện minh lại từ con số 0**, cạnh tranh với các khoản khác để giành nguồn lực hữu hạn.

```
  Bước 1: Xác định "Decision Units" (đơn vị ra quyết định)
       │   Mỗi bộ phận / dự án / hoạt động
       │
  Bước 2: Tạo "Decision Packages" cho mỗi unit
       │   - Mức tối thiểu (base)
       │   - Mức hiện tại (current)
       │   - Mức tăng cường (enhanced)
       │
  Bước 3: Xếp hạng (Ranking) tất cả decision packages
       │   Theo ROI, độ cấp thiết, chiến lược
       │
  Bước 4: Phân bổ ngân sách từ trên xuống
       │   Package rank cao → duyệt
       │   Package rank thấp → cắt / hoãn
```

**Ví dụ chi tiết – ZBB cho phòng Marketing với trần ngân sách 150tr (số liệu giả định minh họa):**

Bước 1 – Mỗi gói được ước tính **chi phí** và **lợi nhuận gộp kỳ vọng** (do doanh thu tạo thêm × biên lợi nhuận gộp). Bước 2 – Tính tỷ lệ lợi ích/chi phí và xếp hạng. Bước 3 – Cộng dồn đến khi chạm trần.

| Gói | Mô tả | Chi phí (tr) | Lợi nhuận gộp kỳ vọng (tr) | Tỷ lệ lợi ích/chi phí | Xếp hạng | Luỹ kế (tr) | Quyết định (trần 150tr) |
|---|---|---|---|---|---|---|---|
| MKT-1 | SEO cơ bản cho website | 15 | 45 | 3,00 | 1 | 15 | Duyệt |
| MKT-2 | Facebook/Instagram Ads | 40 | 100 | 2,50 | 2 | 55 | Duyệt |
| MKT-3 | Đội content (2 người) | 60 | 135 | 2,25 | 3 | 115 | Duyệt |
| MKT-4 | Hợp tác 5 KOL/KOC nhỏ | 30 | 60 | 2,00 | 4 | 145 | Duyệt |
| MKT-5 | Mở kênh TikTok Ads | 25 | 45 | 1,80 | 5 | 170 | Cắt/hoãn |
| MKT-6 | Billboard ngoài trời | 50 | 60 | 1,20 | 6 | 220 | Cắt/hoãn |

*Diễn giải từng bước*: Cộng dồn 15 + 40 + 60 + 30 = 145tr, còn **5tr** — không đủ cho MKT-5 (25tr) dù tỷ lệ 1,8 vẫn khá hấp dẫn. Có 3 cách xử lý: (a) từ chối MKT-5; (b) cắt "mức tăng cường" của MKT-3 (giảm 1 content creator, tiết kiệm 30tr) để dành cho MKT-5; (c) xin tăng trần ngân sách vì tỷ lệ 1,8 vẫn lớn hơn 1. ZBB buộc cuộc thảo luận diễn ra trên **con số biên (marginal)** chứ không phải "năm ngoái mình chi bao nhiêu". Billboard (tỷ lệ 1,2, tức mỗi đồng chi chỉ tạo 1,2 đồng lợi nhuận gộp — gần như hòa vốn sau khi tính chi phí cơ hội) bị loại là hợp lý.

**Lưu ý:** ZBB không đồng nghĩa với "cắt giảm". Case Unilever (III.1) cho thấy ZBB đúng nghĩa là **phân bổ lại** chi tiêu về nơi tạo giá trị cao.

#### 4. Flexible Budget – Ngân sách linh hoạt

**Vấn đề nó giải quyết:** So sánh thực tế với ngân sách tĩnh (static budget) thường "so táo với cam" khi sản lượng thực khác kế hoạch. Nếu kế hoạch bán 10.000 sản phẩm mà bán được 12.000, chi phí biến đổi chắc chắn tăng — nên không thể kết luận "chi vượt" chỉ vì tổng chi phí cao hơn ngân sách. **Ngân sách linh hoạt tính lại ngân sách cho đúng mức hoạt động thực tế**, rồi mới so sánh.

**Công thức:**

$$\text{Ngân sách linh hoạt} = \text{Biến phí đơn vị} \times \text{Sản lượng thực tế} + \text{Định phí}$$

*Giải thích*: biến phí tỷ lệ thuận sản lượng nên phải nhân lại với sản lượng thực; định phí không đổi trong "tầm hoạt động phù hợp" (relevant range) nên giữ nguyên. Nền tảng của nó là việc phân loại hành vi chi phí (biến phí/định phí) và kế toán giá thành tiêu chuẩn phát triển đầu thế kỷ 20.

**Ví dụ:** ngân sách bán 10.000 SP (giá 50.000đ; biến phí 20.000đ/SP; định phí 150tr), thực tế bán 12.000 SP với doanh thu 580tr, biến phí 260tr, định phí 155tr.

| Khoản mục (triệu đồng) | Ngân sách tĩnh (10.000 SP) | Ngân sách linh hoạt (12.000 SP) | Thực tế (12.000 SP) | Chênh lệch TT − Linh hoạt (B = bất lợi) |
|---|---|---|---|---|
| Doanh thu | 500 | 600 | 580 | (20) B |
| Biến phí | (200) | (240) | (260) | (20) B |
| Định phí | (150) | (150) | (155) | (5) B |
| **Lợi nhuận** | **150** | **210** | **165** | **(45) B** |

*Phân tích từng bước:*
1. **Ngân sách tĩnh**: lợi nhuận = 10.000 × (50.000 − 20.000) − 150tr = 300 − 150 = **150tr**.
2. **Ngân sách linh hoạt tại 12.000 SP**: doanh thu 12.000 × 50.000 = 600tr; biến phí 12.000 × 20.000 = 240tr; định phí 150tr → lợi nhuận = 600 − 240 − 150 = **210tr**.
3. **Thực tế** = 580 − 260 − 155 = **165tr**.
4. So với ngân sách *tĩnh*: 165 − 150 = +15tr ("vượt kế hoạch") — **kết luận sai lệch**.
5. So với ngân sách *linh hoạt*: 165 − 210 = **−45tr (bất lợi)** — đúng bản chất: với sản lượng 12.000, lẽ ra lãi 210tr; đã mất 45tr do giá bán thấp hơn kỳ vọng (580 so với 600: −20tr), biến phí vượt (260 so với 240: −20tr), định phí vượt (155 so với 150: −5tr).

**Bài học:** Ngân sách tĩnh che giấu sự kém hiệu quả bằng sản lượng cao; ngân sách linh hoạt tách bạch "hiệu quả hoạt động" khỏi "hiệu ứng sản lượng". Phần C bên dưới sẽ đi tiếp thành phân tích chênh lệch hoàn chỉnh.

#### 5. Rolling Forecast – Dự báo cuốn chiếu

**Vấn đề nó giải quyết:** Ngân sách năm "co dần" — đến tháng 10 chỉ còn nhìn thấy 3 tháng phía trước, trong khi quyết định tuyển dụng, mua hàng, đàm phán vay cần tầm nhìn 12 tháng. Rolling forecast **luôn duy trì 12 tháng (hoặc 4–6 quý) phía trước**: mỗi khi khép sổ xong một tháng/quý, thêm một kỳ mới vào cuối.

```
  Tháng       1  2  3  4  5  6  7  8  9  10 11 12  1  2  3
              ├──┤──┤──┤──┤──┤──┤──┤──┤──┤──┤──┤──┤
  Ngân sách T1 ════════════════════════════════════════
              Thực tế → → → →  Dự báo → → → → → → →

  Cập nhật T4           ├──┤──┤──┤──┤──┤──┤──┤──┤──┤──┤──┤
                        Thực tế│ ► ► ► ► ► ► ► ► ► ► ► ►
                          Dự báo cập nhật với dữ liệu mới
                          + thêm 3 tháng (T1–T3 năm sau)

  → Luôn có 12 tháng dự báo phía trước
  → Cập nhật hàng quý (hoặc hàng tháng)
```

**Thực hành tốt:** (1) dự báo theo **yếu tố dẫn dắt (driver)** — số khách, số kg, giá nguyên liệu — chứ không chỉ "đoán doanh thu"; (2) dự báo ở mức tổng hợp hơn ngân sách (ít dòng hơn) để cập nhật nhanh; (3) không dùng dự báo để thưởng phạt, để nhà quản lý dám báo tin xấu sớm.

#### 6. Beyond Budgeting & ABB (tóm lược)

- **Activity-Based Budgeting (ABB)**: ngân sách xây từ hoạt động (đặt đơn hàng, giao hàng, xử lý khiếu nại) × số lần × chi phí mỗi lần (cost driver). Phù hợp doanh nghiệp đã có hệ thống tính giá ABC; SME chỉ nên áp dụng cho 1–2 hoạt động tốn kém nhất (ví dụ giao hàng).
- **Beyond Budgeting**: bỏ cam kết con số cứng, thay bằng mục tiêu tương đối (so với đối thủ/kỳ trước), dự báo cuốn chiếu và phân bổ nguồn lực theo nhu cầu. Đòi hỏi niềm tin và minh bạch dữ liệu rất cao; không khuyến nghị cho SME chưa có nền tảng ngân sách cơ bản.

---

### C. Phân tích chênh lệch (Variance Analysis) và điểm hòa vốn

#### 1. Tại sao phải tách chênh lệch thành nhiều nguyên nhân?

Chỉ biết "lợi nhuận thực tế thấp hơn ngân sách 388tr" là chưa đủ để hành động. Câu hỏi quản trị là: **ai chịu trách nhiệm và phải làm gì?** Do giá bán thấp (trách nhiệm của kinh doanh/giá)? Do giá nguyên liệu tăng (mua hàng)? Do sản lượng thấp? Do định phí vượt? **Nguyên tắc kiểm soát được (controllability principle)** trong kế toán trách nhiệm nói: chỉ nên đánh giá nhà quản lý trên những gì họ kiểm soát được — vì vậy phải tách từng nguyên nhân. Kỹ thuật phân tích chênh lệch gắn với kế toán giá thành tiêu chuẩn (standard costing) phát triển mạnh đầu thế kỷ 20.

**Quy ước dấu:** F (Favorable – thuận lợi) khi chênh lệch làm tăng lợi nhuận; U (Unfavorable – bất lợi) khi làm giảm lợi nhuận. Trong bảng ở các mục sau, số dương = thuận lợi, số âm = bất lợi.

#### 2. Khung phân tích 3 tầng

```
 Lợi nhuận thực tế − Lợi nhuận ngân sách TĨNH  = Tổng chênh lệch
                       │
        ┌──────────────┴───────────────┐
        │                              │
 Chênh lệch KHỐI LƯỢNG BÁN        Chênh lệch NGÂN SÁCH LINH HOẠT
 (Linh hoạt − Tĩnh)               (Thực tế − Linh hoạt)
 = Δ sản lượng × CM đơn vị NS            │
 "Bán nhiều/ít hơn kế hoạch"     ┌────────┼─────────┬──────────┐
                                  │        │         │          │
                              Giá bán   Biến phí   Định phí  (chi tiết:
                              (Price)   (Cost/     (Fixed)    giá NVL, lượng NVL,
                                         Efficiency)           giờ công...)
```

**Công thức:**

- Chênh lệch khối lượng bán = (Sản lượng thực − Sản lượng NS) × Số dư đảm phí đơn vị theo ngân sách
- Chênh lệch giá bán = (Giá thực − Giá NS) × Sản lượng thực
- Chênh lệch biến phí = −(Biến phí đơn vị thực − Biến phí đơn vị NS) × Sản lượng thực
- Chênh lệch định phí = −(Định phí thực − Định phí NS)

Ba công thức cuối cộng lại bằng **chênh lệch ngân sách linh hoạt**; cộng thêm chênh lệch khối lượng bán là ra tổng chênh lệch so với ngân sách tĩnh. Một ví dụ số đầy đủ, từng bước, được trình bày ở **Case III.3** (Cà phê rang Cầu Đất Xanh).

#### 3. Điểm hòa vốn và biên an toàn — "phao cứu sinh" của ngân sách

**Vấn đề giải quyết:** Doanh nghiệp cần biết *bán tối thiểu bao nhiêu thì không lỗ* để đặt mục tiêu bán hàng hợp lý và đo "độ dày của lớp đệm" trước biến động.

$$\text{Sản lượng hòa vốn} = \frac{\text{Định phí}}{\text{Giá bán đơn vị} - \text{Biến phí đơn vị}} = \frac{\text{Định phí}}{\text{Số dư đảm phí đơn vị}}$$

$$\text{Biên an toàn (\%)} = \frac{\text{Sản lượng dự kiến} - \text{Sản lượng hòa vốn}}{\text{Sản lượng dự kiến}}$$

*Logic*: mỗi đơn vị bán ra đóng góp một "số dư đảm phí" để trang trải định phí; khi tích lũy đủ bằng định phí là hòa vốn, phần vượt lên là lợi nhuận. Ví dụ ngân sách của xưởng nước ép: biên an toàn 30,3% (mục A.3); trong Case III.3, ngân sách có điểm hòa vốn 15.000 kg (biên an toàn 25%) nhưng thực tế do giá giảm và chi phí tăng, điểm hòa vốn nhảy lên 21.061 kg — biên an toàn chỉ còn 4,3%.

---

### D. Dự báo (Forecasting)

#### 1. Bức tranh tổng quan và tiêu chí chọn phương pháp

```
           PHƯƠNG PHÁP DỰ BÁO
                  │
     ┌────────────┼────────────┐
     │            │            │
  ĐỊNH TÍNH   CHUỖI THỜI GIAN   NHÂN QUẢ
 (Qualitative) (Time Series)    (Causal)
     │            │            │
- Ý kiến         - Trung bình   - Hồi quy
  chuyên gia       di động        (Regression)
- Delphi         - San mũ       - Tương quan
- Khảo sát         (Exp.        - Mô hình
  thị trường       Smoothing)     kinh tế lượng
- Ước tính của   - Phân tích
  đội bán hàng     xu hướng
                 - Mùa vụ
```

| Tình huống | Phương pháp nên dùng | Tại sao |
|------------|----------------------|---------|
| Sản phẩm mới, chưa có dữ liệu | Định tính (khảo sát, Delphi, benchmark) | Không có lịch sử để ngoại suy |
| Doanh số ổn định, ít xu hướng | Trung bình di động, san mũ | Làm mượt nhiễu, đơn giản |
| Có xu hướng + mùa vụ rõ | Chỉ số mùa vụ + xu hướng | Giữ được nhịp lặp lại hàng năm |
| Doanh số phụ thuộc một yếu tố tác động đo được (marketing, giá, thời tiết) | Hồi quy | Mô hình hóa quan hệ nhân quả |
| Dữ liệu ít, biến động bất thường | Kết hợp định lượng + phán đoán | Mô hình đơn giản + trực giác thị trường |

**Delphi** (RAND Corporation, thập niên 1950, cần đối chiếu nguồn): thu thập ý kiến chuyên gia qua nhiều vòng ẩn danh, mỗi vòng chuyên gia nhìn tổng hợp kết quả vòng trước rồi điều chỉnh — để tránh "người nói to thắng" (groupthink). SME có thể dùng phiên bản đơn giản: 3–5 người (bán hàng, vận hành, kế toán) viết riêng dự báo, rồi cùng so sánh và thảo luận chênh lệch.

#### 2. Trung bình di động (Moving Average)

**Vấn đề giải quyết:** Dữ liệu bán hàng hàng tháng luôn có "nhiễu" ngẫu nhiên (một đơn lớn bất thường, một tuần mưa). Nếu lấy đúng số tháng vừa rồi làm dự báo, ta sẽ phản ứng thái quá với nhiễu. **Lấy trung bình của n kỳ gần nhất** làm phẳng nhiễu: nhiễu dương và âm triệt tiêu một phần, còn lại là "mức nền".

$$F_{t+1} = \frac{A_t + A_{t-1} + \dots + A_{t-n+1}}{n}$$

- $F_{t+1}$ = dự báo kỳ tới; $A_t$ = thực tế kỳ $t$; $n$ = số kỳ trung bình.
- **n lớn** → mượt hơn nhưng chậm theo xu hướng thật; **n nhỏ** → nhạy hơn nhưng nhiều nhiễu hơn.
- **Hạn chế:** coi mọi kỳ trong cửa sổ có trọng số bằng nhau; luôn trễ khi dữ liệu có xu hướng tăng/giảm.

**Ví dụ (MA-3)** — doanh thu 6 tháng đầu (triệu đồng) của một cửa hàng (giả định):

| Tháng | Doanh thu thực tế (tr) | Dự báo MA-3 (tr) | Sai số (A − F) |
|---|---|---|---|
| 1 | 100 | – | – |
| 2 | 120 | – | – |
| 3 | 110 | – | – |
| 4 | 130 | 110,00 | 20,00 |
| 5 | 125 | 120,00 | 5,00 |
| 6 | 140 | 121,67 | 18,33 |
| **7** | ? | **131,67** | – |

*Diễn giải từng bước*: Dự báo tháng 4 = (100 + 120 + 110)/3 = 110; thực tế 130 → sai số +20 (dự báo thấp hơn thực tế). Dự báo tháng 5 = (120 + 110 + 130)/3 = 120. Dự báo tháng 6 = (110 + 130 + 125)/3 = 121,67. Tháng 7 = (130 + 125 + 140)/3 = 131,67. Cả ba sai số đều dương → MA **luôn dự báo thấp** vì dữ liệu đang có xu hướng tăng.

#### 3. San mũ (Exponential Smoothing)

**Nguồn gốc & logic:** Robert G. Brown phát triển phương pháp này trong những năm 1950 (bối cảnh: kiểm soát tồn kho cho Hải quân Mỹ) và Charles Holt mở rộng cho dữ liệu có xu hướng (1957); Peter Winters thêm yếu tố mùa vụ (1960) *(cần đối chiếu nguồn)*. Ý tưởng khắc phục điểm yếu của MA: **dữ liệu càng mới càng đáng tin hơn để dự báo, và ta không cần lưu cả cửa sổ n kỳ** — chỉ cần dự báo cũ và thực tế mới nhất.

$$F_{t+1} = \alpha \cdot A_t + (1-\alpha)\cdot F_t$$

- $\alpha$ (0 < α < 1) = hệ số san mũ, quyết định mức độ "tin vào thực tế mới".
- Khai triển: $F_{t+1} = \alpha A_t + \alpha(1-\alpha)A_{t-1} + \alpha(1-\alpha)^2 A_{t-2} + \dots$ → trọng số **giảm theo cấp số nhân** (đó là lý do tên "mũ").
- α cao (0,6–0,9): phản ứng nhanh, thích hợp thị trường biến động; α thấp (0,1–0,3): ổn định, thích hợp nhu cầu bền vững.

**Ví dụ (α = 0,3), cùng dữ liệu trên:**

| Tháng | Thực tế | Dự báo F | Cách tính |
|---|---|---|---|
| 1 | 100 | 100 | Khởi tạo bằng thực tế tháng 1 |
| 2 | 120 | 100,00 | 0,3 × 100 + 0,7 × 100,00 |
| 3 | 110 | 106,00 | 0,3 × 120 + 0,7 × 100,00 |
| 4 | 130 | 107,20 | 0,3 × 110 + 0,7 × 106,00 |
| 5 | 125 | 114,04 | 0,3 × 130 + 0,7 × 107,20 |
| 6 | 140 | 117,33 | 0,3 × 125 + 0,7 × 114,04 |
| **7** | ? | **124,13** | 0,3 × 140 + 0,7 × 117,33 |

*Diễn giải*: Dự báo tháng 3 = 0,3 × 120 + 0,7 × 100 = 106; tháng 4 = 0,3 × 110 + 0,7 × 106 = 107,2; ... tháng 7 = 0,3 × 140 + 0,7 × 117,33 = 124,13.

**Lưu ý quan trọng khi chọn α:** Ở chuỗi này doanh thu tăng đều, α = 0,3 thấp nên dự báo *chậm hơn nhiều* so với thực tế (124 so với MA-3 là 132). Nếu dùng α = 0,7 sai số nhỏ hơn rõ rệt: với dữ liệu trên, MAD tháng 2–6 chỉ khoảng 11,7 so với 16,1 khi α = 0,3 (kiểm tra bằng Python). Với dữ liệu có xu hướng rõ, nên dùng **san mũ có xu hướng của Holt** thay vì san mũ đơn.

#### 4. Chỉ số mùa vụ (Seasonal Index)

**Vấn đề giải quyết:** Nhiều SME F&B, bán lẻ, du lịch có doanh số lặp lại theo mùa; dự báo "bình quân" sẽ đánh giá thấp mùa cao điểm và thừa ở mùa thấp. **Chỉ số mùa vụ** đo "quý này thường cao/thấp hơn mức bình quân bao nhiêu lần".

$$\text{Chỉ số mùa vụ quý } i = \frac{\text{Trung bình các năm của quý } i}{\text{Trung bình chung của mọi quý}}$$

*Ví dụ (xưởng nước ép — số liệu bán 2024 và 2025 là giả định minh họa):*

| Quý | 2024 (chai) | 2025 (chai) | Trung bình 2 năm | Chỉ số mùa vụ = TB quý / TB chung (12.187,5) |
|---|---|---|---|---|
| Q1 | 8.000 | 9.000 | 8.500 | 0,697 |
| Q2 | 12.000 | 13.500 | 12.750 | 1,046 |
| Q3 | 16.500 | 18.000 | 17.250 | 1,415 |
| Q4 | 9.500 | 11.000 | 10.250 | 0,841 |
| **Tổng/TB** | 46.000 | 51.500 | 12.187,5 (TB/quý) | 4,000 |

Dự báo 2026: tốc độ tăng 2025/2024 = 51.500 / 46.000 = 1,1196 (+11,96%); giả sử 2026 tăng cùng tốc độ → tổng 2026 = 51.500 × 1,1196 = 57.658 chai. Chia theo mùa vụ:

| Quý | Dự báo 2026 = (Tổng 2026 / 4) × chỉ số mùa vụ |
|---|---|
| Q1 | 10.053 chai |
| Q2 | 15.080 chai |
| Q3 | 20.402 chai |
| Q4 | 12.123 chai |
| **Cả năm** | 57.658 chai |

*So với ngân sách bán hàng 57.000 chai (A.3)*: dự báo thống kê 57.658 chai chỉ lệch +1,2% so với ngân sách → ngân sách hợp lý; nhưng phân bổ theo quý (10.053; 15.080; 20.402; 12.123) cao hơn đôi chút so với ngân sách (10.000; 15.000; 20.000; 12.000) — hãy xem "chênh nhỏ" này là tín hiệu để kiểm tra chéo chứ không phải sai.

#### 5. Hồi quy tuyến tính (Linear Regression)

**Nguồn gốc & logic:** Phương pháp bình phương tối thiểu (least squares) do Legendre (1805) và Gauss (1809) đưa ra để khớp quỹ đạo thiên văn; Francis Galton (cuối thế kỷ 19) đặt tên "regression" khi nghiên cứu chiều cao cha–con. Trong kinh doanh, hồi quy trả lời: **"nếu thay đổi yếu tố X một đơn vị, Y thường thay đổi bao nhiêu?"** — nghĩa là mô hình nhân quả chứ không chỉ ngoại suy thời gian.

$$Y = a + bX$$

$$b = \frac{n\sum XY - \sum X \sum Y}{n\sum X^2 - (\sum X)^2}, \qquad a = \bar{Y} - b\bar{X}$$

- **b (độ dốc)**: mỗi 1 đơn vị X tăng thì Y tăng trung bình b.
- **a (hệ số chặn)**: giá trị Y "nền" khi X = 0 (cẩn thận ngoại suy ngoài vùng dữ liệu).
- Đường thẳng được chọn sao cho **tổng bình phương khoảng cách** từ các điểm dữ liệu tới đường là nhỏ nhất.

**Ví dụ:** dự báo doanh thu theo chi phí marketing hằng tháng (giả định minh họa):

| Tháng | X: Marketing (tr) | Y: Doanh thu (tr) | X·Y | X² |
|---|---|---|---|---|
| 1 | 20 | 200 | 4000 | 400 |
| 2 | 25 | 240 | 6000 | 625 |
| 3 | 30 | 280 | 8400 | 900 |
| 4 | 22 | 210 | 4620 | 484 |
| 5 | 35 | 320 | 11200 | 1225 |
| 6 | 28 | 260 | 7280 | 784 |
| **Tổng** | **160** | **1510** | **41500** | **4418** |

*Tính từng bước*: n = 6; ΣX = 160; ΣY = 1.510; ΣXY = 41.500; ΣX² = 4.418.
- b = (6 × 41.500 − 160 × 1.510) / (6 × 4.418 − 160²) = (249.000 − 241.600) / (26.508 − 25.600) = 7.400 / 908 = **8,15**.
- X̄ = 160/6 = 26,67; Ȳ = 1.510/6 = 251,67 → a = 251,67 − 8,15 × 26,67 = **34,34**.
- Phương trình: **Y = 34,34 + 8,15 X**. Nếu tháng 7 chi marketing 40tr → Y = 34,34 + 8,15 × 40 = **360,3tr**.
- Hệ số tương quan r ≈ 0,998 (R² ≈ 0,997): mối quan hệ rất chặt trong mẫu 6 tháng này.

*Diễn giải*: mỗi triệu đồng marketing tăng thêm gắn với khoảng 8,15tr doanh thu tăng thêm. **Cảnh báo**: tương quan không phải nhân quả (có thể cả marketing và doanh thu cùng tăng vì mùa cao điểm); mẫu 6 điểm rất nhỏ; ngoại suy quá xa vùng dữ liệu (X từ 20–35) là rủi ro; hiệu ứng bão hòa (chi thêm marketing nhưng doanh thu không tăng tuyến tính). Phiên bản cũ của tài liệu ghi phương trình Y = 20 + 8,5X là **chưa chính xác** (kết quả tính lại như trên).

#### 6. Đo lường độ chính xác dự báo — "dự báo của tôi tốt đến đâu?"

**Vấn đề giải quyết:** Không đo sai số thì không biết nên tin mô hình nào, α nào, hay phải đổi phương pháp. Mỗi chỉ số trả lời một câu hỏi khác nhau:

| Chỉ số | Công thức | Trả lời câu hỏi | Điểm mạnh / yếu |
|--------|-----------|------------------|------------------|
| **MAD** (Mean Absolute Deviation) | $\frac{\sum\|A-F\|}{n}$ | Trung bình dự báo lệch bao nhiêu đơn vị? | Dễ hiểu; không phản ánh độ lớn tương đối |
| **MAPE** (Mean Absolute % Error) | $\frac{1}{n}\sum\left\|\frac{A-F}{A}\right\| \times 100\%$ | Lệch bao nhiêu % so với thực tế? | So sánh được giữa các sản phẩm; lỗi khi A = 0 |
| **MSE** (Mean Squared Error) | $\frac{\sum(A-F)^2}{n}$ | Có sai số lớn đột xuất không? | Phạt nặng sai số lớn; đơn vị bình phương |
| **Tracking Signal** | $\frac{\sum (A-F)}{\text{MAD}}$ | Dự báo có bị lệch một chiều (bias) không? | Nên giữ trong khoảng ±4 (ngưỡng thực hành thường dùng) |

*Tại sao cần Tracking Signal?* MAD có thể nhỏ nhưng nếu sai số cùng chiều (luôn thấp hoặc luôn cao) thì mô hình có **thiên lệch hệ thống** — khác với sai số ngẫu nhiên hai chiều. Tracking signal do Trigg đề xuất (1964, cần đối chiếu nguồn) để cảnh báo điều này.

Áp dụng cho MA-3 và san mũ α = 0,3 ở tháng 4–6 của ví dụ trên:

| Chỉ số (tháng 4-6) | MA-3 | San mũ α = 0,3 |
|---|---|---|
| Sai số từng tháng (A − F) | 20,00 ; 5,00 ; 18,33 | 22,80 ; 10,96 ; 22,67 |
| MAD | 14,44 | 18,81 |
| MAPE | 10,83% | 14,17% |
| MSE | 253,7 | 384,7 |
| Tracking Signal | 3,00 | 3,00 |

*Diễn giải*: MA-3 chính xác hơn (MAD 14,44 so với 18,81; MAPE 10,83% so với 14,17%) cho chuỗi đang tăng. Tracking signal của cả hai đều bằng 3,00 — nghĩa là cả 3 sai số đều dương, tức **cả hai mô hình đều dự báo thấp liên tục**; với chỉ 3 quan sát chưa vượt ngưỡng ±4 nhưng đang tiến sát, báo hiệu cần đổi mô hình (tăng α hoặc dùng mô hình có xu hướng).

---

### E. Ưu nhược điểm của Budgeting và Forecasting

#### 1. Budgeting

| Ưu điểm | Nhược điểm |
|---------|------------|
| Đặt mục tiêu rõ bằng con số | Tốn thời gian lập (3–6 tháng ở DN lớn; 1–3 tuần ở SME) |
| Phối hợp giữa các bộ phận | Nhanh lỗi thời khi môi trường biến động |
| Kiểm soát chi tiêu | Gaming/padding – bộ phận thổi phồng ngân sách |
| Chuẩn so sánh cho variance analysis | Cứng nhắc, khó thích ứng |
| Tạo trách nhiệm giải trình (accountability) | Khuyến khích "spend it or lose it" |
| Buộc lãnh đạo suy nghĩ về tương lai | Tập trung ngắn hạn (1 năm) |

#### 2. Forecasting

| Ưu điểm | Nhược điểm |
|---------|------------|
| Linh hoạt, cập nhật liên tục | Không thay thế được ngân sách cho trách nhiệm giải trình |
| Phản ứng nhanh với thay đổi | Phụ thuộc chất lượng dữ liệu & giả định |
| Hướng về tương lai | "Garbage in, garbage out" |
| Hỗ trợ quyết định ngắn hạn | Không dự đoán được sự kiện "thiên nga đen" |

---

### F. Hoàn cảnh và môi trường áp dụng

#### 1. Theo giai đoạn doanh nghiệp

| Giai đoạn | Cách lập ngân sách | Cách dự báo |
|-----------|--------------------|--------------|
| **Startup (<1 năm)** | Ngân sách tiền mặt 13 tuần | Dự báo cuốn chiếu hàng tháng |
| **Early stage (1–3 năm)** | Ngân sách năm đơn giản | Cuốn chiếu hàng quý |
| **Growth (3–7 năm)** | Master budget + Flexible | Cuốn chiếu hàng tháng + kịch bản |
| **Mature (>7 năm)** | Master budget đầy đủ + chu kỳ ZBB | Cuốn chiếu + driver-based |

#### 2. Theo mức độ biến động

| Biến động | Ngân sách | Dự báo | Tần suất cập nhật |
|-----------|-----------|--------|-------------------|
| **Thấp** (điện nước, FMCG) | Ngân sách tĩnh đủ | Cập nhật quý | Quý |
| **Trung bình** (dịch vụ, bán lẻ) | Ngân sách linh hoạt | Cuốn chiếu tháng | Tháng |
| **Cao** (công nghệ, startup) | Rolling budget hoặc Beyond Budgeting | Hàng tuần/2 tuần | Tuần |

#### 3. Sơ đồ quyết định

```
     DN của bạn ở giai đoạn nào?
              │
     ┌────────┼────────┐
     │                 │
  Startup           Đã ổn định
     │                 │
  Tiền mặt          ┌───┴───┐
  13 tuần           │       │
  + Dự báo         Ổn định  Biến động
  tháng             │       │
                 Ngân sách  Linh hoạt
                 tĩnh       + Cuốn chiếu
                  +           +
                 Dự báo quý  Dự báo tháng
```

---

## III. CASE STUDIES THỰC TẾ

### 1. Case Study Thành công: Unilever – Chuyển đổi bằng Zero-Based Budgeting

> **Ghi chú nguồn dữ liệu**: Các số liệu về Unilever dưới đây tổng hợp từ thông tin công khai và bản cũ của tài liệu; **chưa được kiểm chứng đầy đủ — cần đối chiếu báo cáo thường niên (Annual Report) và công bố của Unilever** trước khi trích dẫn học thuật. Các phép tính "minh họa" là giả định do tài liệu tự đặt.

#### Bối cảnh

Unilever (hàng tiêu dùng nhanh, doanh thu khoảng 50+ tỷ euro/năm) bắt đầu áp dụng ZBB từ khoảng năm 2015 dưới thời CEO Paul Polman và CFO Graeme Pitkethly, trong bối cảnh biên lợi nhuận hoạt động thấp hơn các đối thủ cùng ngành. Đến tháng 2/2017, Kraft Heinz (được hậu thuẫn bởi quỹ 3G Capital – nổi tiếng về văn hóa ZBB cực đoan) công khai đề nghị mua lại Unilever với mức khoảng 143 tỷ USD; đề nghị bị từ chối. Thông điệp chiến lược: *tự chứng minh có thể cải thiện lợi nhuận mà không cần bị mua lại*.

#### Phân tích từng bước

**Bước 1 – Hiểu logic ZBB ở quy mô tập đoàn.** Trong mô hình incremental, chi phí hành chính, du lịch, thuê tư vấn, marketing cứ tăng theo doanh thu. ZBB đặt câu hỏi: *"Nếu hôm nay bắt đầu từ số không, ta có chi khoản này không? Với mức bao nhiêu? Ai chịu trách nhiệm?"*. Unilever chia chi phí thành các "gói" nhỏ với chủ sở hữu rõ ràng, so sánh với chuẩn tốt nhất (best-in-class benchmark) thay vì so với năm trước.

**Bước 2 – Minh họa bằng phép tính (giả định, doanh nghiệp "mini-Unilever"):**

| Thông số giả định | Giá trị |
|-------------------|---------|
| Doanh thu | 1.000 |
| Lợi nhuận hoạt động (biên 15%) | 150 |
| Chi phí hoạt động có thể kiểm soát (marketing, hành chính, tư vấn, du lịch...) | 300 |

- ZBB cắt 10% chi phí kiểm soát được: 10% × 300 = **30** tiết kiệm.
- Tái đầu tư 10 vào các gói marketing có ROI cao hơn.
- Lợi nhuận hoạt động mới = 150 + 30 − 10 = **170** → biên mới = 170 / 1.000 = **17%** (tăng 2 điểm phần trăm).

Với doanh thu thực khoảng 53 tỷ euro, mỗi điểm phần trăm biên lợi nhuận tương đương ~0,53 tỷ euro; tăng khoảng 4 điểm phần trăm tương đương 53 × 0,04 ≈ **2,1 tỷ euro** — cùng bậc độ lớn với con số "tiết kiệm trên 2 tỷ euro" mà bản cũ ghi.

**Bước 3 – Kết quả tóm tắt theo bản cũ (chưa kiểm chứng):**

| Lĩnh vực | Trước ZBB | Sau ZBB | Tiết kiệm (ước tính) |
|----------|-----------|---------|----------------------|
| Marketing | ~7,7 tỷ € (~15% doanh thu) | ~7,1 tỷ € (~14%), hiệu quả hơn | ~600 triệu € |
| Chuỗi cung ứng | Nhiều nhà máy dư thừa | Đóng bớt nhà máy, tối ưu logistics | ~500 triệu € |
| Chi phí chung | Tư vấn, du lịch nhiều | Giảm tư vấn ~30%, du lịch ~40% | ~400 triệu € |
| Mua hàng | Phân tán | Tập trung, đàm phán theo khối lượng | ~500 triệu € |
| **Tổng cộng** | | | **~2.000 triệu € (≈ 2 tỷ €)** |

Kiểm tra số học: 600 + 500 + 400 + 500 = 2.000 triệu €. Biên lợi nhuận hoạt động tăng từ khoảng 15% (2015) lên khoảng 19% (2019) — **cần đối chiếu nguồn** (số cũ ghi 16,4% → 19,1% → 18,4% không nhất quán giữa các định nghĩa "reported" và "underlying").

**Bước 4 – Bốn nguyên tắc ZBB của Unilever:**
1. **Visibility (minh bạch)**: mọi chi phí phải nhìn thấy, không "ẩn" trong ngân sách tổng.
2. **Ownership (chủ sở hữu)**: mỗi khoản có một người chịu trách nhiệm.
3. **Benchmarking**: so với best-in-class, không chỉ năm trước.
4. **Zero-base**: biện minh mọi khoản, không tự động duyệt.

#### Bài học

> ZBB không phải "cắt giảm chi phí" thuần túy mà là **phân bổ lại nguồn lực vào nơi tạo giá trị cao nhất** — tiết kiệm được ở nơi không tạo giá trị để tái đầu tư vào marketing hiệu quả hơn. Tuy nhiên, các phân tích của giới tư vấn thường ghi nhận chi phí có xu hướng "phình" lại sau vài năm nếu thiếu kỷ luật duy trì, và ZBB quá tay có thể làm giảm đầu tư thương hiệu dài hạn (cần đối chiếu nguồn). **Với SME: học tư duy "mỗi khoản phải giải trình" nhưng áp dụng cho 5–7 khoản chi lớn nhất, đừng làm cho toàn bộ chi phí**.

---

### 2. Case Study Thất bại: Sears – Ngân sách cứng nhắc góp phần vào sụp đổ

> **Ghi chú nguồn dữ liệu**: Doanh thu Sears Holdings (khoảng 53 tỷ USD năm 2006, khoảng 16,7 tỷ USD năm 2017) và việc nộp đơn phá sản tháng 10/2018 là thông tin công khai phổ biến; các tỷ lệ về "padding 20–30%", "ngân sách đổi mới 0,5%" và so sánh với Amazon trong bản cũ **chưa kiểm chứng — cần đối chiếu nguồn**. Phép tính mô hình "khóa phân bổ" bên dưới là **giả định minh họa**.

#### Bối cảnh

Sears từng là nhà bán lẻ lớn nhất nước Mỹ, nhưng suy giảm dần từ thập niên 2000 (sáp nhập với Kmart năm 2005 tạo Sears Holdings) và phá sản năm 2018. Nhiều nhà quan sát (cần đối chiếu nguồn) ghi nhận từ khoảng 2008, ban lãnh đạo chia công ty thành hàng chục đơn vị kinh doanh cạnh tranh nhau về nguồn lực — tăng tính "silo" và đấu tranh ngân sách nội bộ.

#### Phân tích từng bước

**Bước 1 – Sức mạnh suy giảm.** Doanh thu giảm từ khoảng 53 tỷ USD (2006) xuống khoảng 16,7 tỷ USD (2017): giảm 1 − 16,7/53 = **68,5%** trong 11 năm, tương đương mức giảm bình quân hằng năm (CAGR) = (16,7/53)^(1/11) − 1 ≈ **−10,0%/năm**. Một công ty thường xuyên mất 10% doanh thu mỗi năm không thể dùng ngân sách "năm trước ± 5%".

**Bước 2 – Năm "bệnh" ngân sách của Sears (theo bản cũ):**

| Yếu tố | Chi tiết | Hệ quả |
|--------|---------|--------|
| **Incremental budgeting** | Ngân sách năm sau = năm trước ± ~5% | Không tái phân bổ sang digital |
| **Ngân sách silo** | Mỗi phòng ban tranh giành ngân sách | Cạnh tranh nội bộ, không hợp tác |
| **Tư duy ngắn hạn** | Ngân sách 1 năm, tối đa hóa thưởng | Cắt R&D, đào tạo, bảo trì cửa hàng |
| **Không có rolling forecast** | Không cập nhật khi thị trường đổi | Amazon/Walmart đổi cuộc chơi, Sears vẫn lập ngân sách kiểu cũ |
| **Văn hóa "chơi" ngân sách** | Quản lý thổi phồng 20–30% (ước tính) | Lãng phí có hệ thống |

**Bước 3 – Mô hình "khóa phân bổ" (giả định minh họa).** Giả sử tỷ trọng thị trường bán lẻ trực tuyến tăng đều từ 5% (2010) lên 21% (2018) (+2 điểm phần trăm/năm), trong khi Sears chỉ tăng ngân sách đầu tư cho kênh digital 5%/năm (tương đối) từ mức khởi điểm 3% tổng đầu tư:

| Năm | Tỷ trọng online của thị trường (giả định) | Tỷ trọng đầu tư digital của Sears (3% × 1,05^t) | Khoảng cách |
|-----|-------------------------------------------|---------------------------------------------------|-------------|
| 2010 | 5% | 3,00% | 2,0 điểm |
| 2012 | 9% | 3,31% | 5,7 điểm |
| 2014 | 13% | 3,65% | 9,4 điểm |
| 2016 | 17% | 4,02% | 13,0 điểm |
| 2018 | 21% | 4,43% | 16,6 điểm |

*Diễn giải*: Mỗi bước tăng ngân sách (5%) đều "hợp lý" khi nhìn riêng, nhưng cộng dồn 8 năm khiến phần đầu tư cho kênh tăng trưởng chỉ bằng ~21% mức thị trường đã dịch chuyển (4,43 / 21). **Đó là cơ chế khóa phân bổ (budget lock-in)**: sai lầm không nằm ở một năm cụ thể mà ở *phương pháp* không bao giờ hỏi lại tỷ trọng.

**Bước 4 – So sánh với doanh nghiệp thích ứng (bản cũ, chưa kiểm chứng):**

| Yếu tố | Sears (2010–2018) | Amazon (cùng thời kỳ) |
|--------|-------------------|------------------------|
| Cách lập ngân sách | Incremental, cứng | Dựa theo yếu tố dẫn dắt, cuốn chiếu |
| Phân bổ vốn đầu tư | Dàn đều cửa hàng | Tập trung AWS, logistics |
| Dự báo | Năm, tĩnh | Gần thời gian thực, dựa trên dữ liệu |
| Phản ứng với thay đổi | Ngân sách duyệt xong không đổi | Cập nhật dự báo theo tuần |
| Chi cho đổi mới | ~0,5% doanh thu (ước tính) | ~12% doanh thu (ước tính) |

#### Bài học

1. **Incremental budgeting trong môi trường bị phá vỡ (disruption) là "chết chậm"** — cần ZBB hoặc ngân sách theo yếu tố dẫn dắt.
2. **Ngân sách phải khớp với chiến lược**: nếu chiến lược là chuyển đổi số mà ngân sách vẫn phân bổ đều cho cửa hàng cũ thì chiến lược chỉ nằm trên giấy.
3. **Rolling forecast là hệ thống cảnh báo sớm**: đợi chu kỳ ngân sách năm sau mới thay đổi là quá chậm.
4. **Văn hóa chống "gaming"**: tách thưởng khỏi mốc ngân sách cứng; khuyến khích báo tin xấu sớm.

---

### 3. Case Study SME Việt Nam: Công ty TNHH Cà phê rang "Cầu Đất Xanh" (giả định minh họa)

> **Tất cả số liệu và tên doanh nghiệp trong case này là giả định để minh họa** (đã kiểm tra bằng Python), không phải doanh nghiệp thật.

#### Bối cảnh

Cầu Đất Xanh là công ty cà phê rang xay tại Đà Lạt, bán buôn cho khoảng 150 quán cà phê/nhà hàng ở TP.HCM, Đà Lạt và bán online. Doanh thu năm 2025 khoảng 18–19 tỷ đồng. Chủ công ty là một kỹ sư rang xay, kế toán thuê ngoài. Đầu năm 2026, chủ công ty đặt ngân sách năm với mục tiêu "tăng doanh số 15%". Đến cuối quý I, báo cáo cho thấy **doanh số vượt kế hoạch 10% nhưng lợi nhuận hoạt động gần như bằng không** — chủ công ty nhờ chuyên gia tư vấn phân tích. Đây là case điển hình của SME "chạy theo doanh số".

#### Bước 1 — Ngân sách gốc được dựng theo yếu tố dẫn dắt (driver-based)

Thay vì lấy 2025 cộng 15%, ngân sách Q1/2026 được dựng từ các yếu tố dẫn dắt:

- **Sản lượng:** 150 quán × 100 kg/quý = 15.000 kg + kênh online & bán lẻ 5.000 kg = **20.000 kg**.
- **Giá bán bình quân:** 250.000đ/kg.
- **Biến phí:** cà phê nhân 110.000 + bao bì 12.000 + nhân công trực tiếp 18.000 + vận chuyển/hoa hồng 20.000 = **160.000đ/kg**.
- **Định phí quý:** 1.350tr (thuê xưởng, lương quản lý, lương văn phòng, marketing, khấu hao...).

Tính lợi nhuận ngân sách:
- Doanh thu = 20.000 × 250.000 = **5.000tr**.
- Tổng biến phí = 20.000 × 160.000 = **3.200tr** → số dư đảm phí = 1.800tr (CM/kg = 90.000đ; 36%).
- Lợi nhuận hoạt động = 1.800 − 1.350 = **450tr** (9%).
- **Điểm hòa vốn** = 1.350tr / 90.000đ = **15.000 kg** → biên an toàn = (20.000 − 15.000)/20.000 = **25%**.

#### Bước 2 — Kết quả thực tế quý I so với ngân sách tĩnh

Doanh số tháng 1–3: 6.800; 7.100; 8.100 kg → **22.000 kg (+10%)**. Nhưng để chốt các đơn lớn, công ty chiết khấu cho nhóm khách buôn → giá bình quân chỉ 238.000đ/kg; đồng thời giá cà phê nhân tăng, chi phí vận chuyển và bao bì cũng tăng.

| Chỉ tiêu Q1/2026 | Ngân sách tĩnh | Thực tế | Chênh lệch |
|---|---|---|---|
| Sản lượng (kg) | 20.000 | 22.000 | +2.000 (+10%) |
| Giá bán (đ/kg) | 250.000 | 238.000 | -12.000 (−4,8%) |
| Biến phí (đ/kg) | 160.000 | 172.000 | +12.000 (+7,5%) |
| Doanh thu (tr) | 5.000 | 5.236 | +236 |
| Tổng biến phí (tr) | 3.200 | 3.784 | +584 |
| Số dư đảm phí (tr) | 1.800 | 1.452 | -348 |
| Định phí (tr) | 1.350 | 1.390 | +40 |
| **Lợi nhuận hoạt động (tr)** | **450** | **62** | **-388** |

*Đọc nhanh*: Lợi nhuận thực tế 62tr so với ngân sách 450tr, thấp hơn **388tr (−86%)** dù sản lượng tăng 10%. Chủ công ty thắc mắc: "Tôi bán nhiều hơn, sao lại lãi ít đi?"

#### Bước 3 — Dựng ngân sách linh hoạt tại sản lượng thực tế 22.000 kg

Ngân sách linh hoạt giữ nguyên **giá bán, biến phí đơn vị và định phí theo kế hoạch** nhưng thay sản lượng bằng thực tế:

- Doanh thu = 22.000 × 250.000 = 5.500tr; Biến phí = 22.000 × 160.000 = 3.520tr; CM = 1.980tr; Định phí 1.350tr → Lợi nhuận = **630tr**.

| Tr đồng | Ngân sách tĩnh (20.000kg) | Ngân sách linh hoạt (22.000kg) | Thực tế (22.000kg) |
|---|---|---|---|
| Doanh thu | 5.000 | 5.500 | 5.236 |
| Biến phí | (3.200) | (3.520) | (3.784) |
| Số dư đảm phí | 1.800 | 1.980 | 1.452 |
| Định phí | (1.350) | (1.350) | (1.390) |
| **Lợi nhuận hoạt động** | **450** | **630** | **62** |

Kết luận quan trọng: *với 22.000 kg lẽ ra phải lãi 630tr*; thực tế chỉ lãi 62tr, tức đã **mất 568tr** do giá, chi phí và định phí chệch kế hoạch — chứ không phải do "bán ít".

#### Bước 4 — Phân tích chênh lệch từng nguyên nhân

- **Khối lượng:** (22.000 − 20.000) × 90.000 = **+180tr (F)** — bán nhiều hơn là điều tốt.
- **Giá bán:** (238.000 − 250.000) × 22.000 = **−264tr (U)**.
- **Biến phí:** chia theo từng thành phần (chênh lệch đơn vị × 22.000 kg):
  - Cà phê nhân: (118.000 − 110.000) = 8.000 × 22.000 = **−176tr**.
  - Bao bì: 1.000 × 22.000 = **−22tr**.
  - Nhân công trực tiếp: 1.000 × 22.000 = **−22tr**.
  - Vận chuyển & hoa hồng: 2.000 × 22.000 = **−44tr**.
  - Tổng biến phí = −264tr (bằng chênh lệch biến phí đơn vị 12.000 × 22.000).
- **Định phí:** 1.350 − 1.390 = **−40tr (U)**.

| Nguyên nhân | Tác động lên lợi nhuận (tr) | Đánh giá |
|---|---|---|
| Khối lượng (SL tăng 2.000 kg × CM ngân sách 90.000đ) | +180 | Thuận lợi (F) |
| Giá bán (−12.000đ × 22.000 kg) | −264 | Bất lợi (U) |
| Nguyên liệu cà phê nhân (8.000đ/kg × 22.000 kg) | −176 | Bất lợi (U) |
| Bao bì (1.000đ/kg × 22.000 kg) | −22 | Bất lợi (U) |
| Nhân công trực tiếp (1.000đ/kg × 22.000 kg) | −22 | Bất lợi (U) |
| Vận chuyển & hoa hồng (2.000đ/kg × 22.000 kg) | −44 | Bất lợi (U) |
| Định phí (1.390 − 1.350) | −40 | Bất lợi (U) |
| **Tổng chênh lệch** | **−388** | (62 − 450) |

Kiểm tra: 180 − 264 − 176 − 22 − 22 − 44 − 40 = **−388** ✓ (khớp 62 − 450).

*Ý nghĩa quản trị:* Hai nguyên nhân lớn nhất là **giảm giá (−264)** và **giá cà phê nhân tăng (−176)**. Giảm giá 12.000đ/kg (−4,8%) có vẻ nhỏ, nhưng vì biên đảm phí chỉ 90.000đ/kg (36%) nên *mỗi 1% giảm giá ăn mất 2,78% số dư đảm phí* (2.500/90.000). Chủ công ty đổi 2.000kg bán thêm (+180tr) lấy việc giảm giá cho toàn bộ 22.000kg (−264tr) — một giao dịch lỗ rõ ràng.

#### Bước 5 — Điểm hòa vốn mới và biên an toàn

- Số dư đảm phí thực tế = 238.000 − 172.000 = **66.000đ/kg** (giảm từ 90.000).
- Điểm hòa vốn thực tế = 1.390tr / 66.000 = **21.061 kg**.
- Biên an toàn = (22.000 − 21.061)/22.000 = **4,3%** (so với 25% ngân sách).

*Diễn giải*: Công ty chỉ còn cách hòa vốn 939kg (khoảng 4% sản lượng). Nếu một khách buôn lớn (chiếm 5% sản lượng) rời đi, công ty lỗ ngay. Biên an toàn là chỉ số cảnh báo sớm mà ngân sách tĩnh không phát hiện được.

#### Bước 6 — Dự báo lại (Reforecast) quý II cho hai kịch bản

**Dự báo sản lượng Q2:** Trung bình tháng Q1 = 22.000/3 = 7.333 kg; tháng 3 = 8.100 kg (có đợt chốt đơn lớn một lần). Lấy điểm giữa = (7.333 + 8.100)/2 = 7.717 kg/tháng → 23.150 kg; làm tròn thận trọng **23.000 kg** (vì tháng 3 có yếu tố khuyến mãi không lặp lại).

- **Kịch bản A – giữ nguyên chính sách:** giá 238.000; biến phí 172.000; định phí 1.390tr → lợi nhuận = 23.000 × 66.000 − 1.390tr = 1.518 − 1.390 = **128tr**.
- **Kịch bản B – hành động điều chỉnh:** (1) chấm dứt chiết khấu rộng rãi, chỉ duy trì giá thấp cho hợp đồng lớn dài hạn → giá bình quân 244.000đ; chấp nhận mất 4% sản lượng (22.080 kg); (2) ký hợp đồng mua kỳ hạn cà phê nhân giá cố định 114.000đ/kg; (3) gom đơn giao hàng, giảm chi phí vận chuyển 2.000đ/kg → biến phí = 114.000 + 13.000 + 19.000 + 20.000 = **166.000đ/kg**.

| Giả định Q2/2026 | Kịch bản A: không đổi | Kịch bản B: hành động điều chỉnh |
|---|---|---|
| Sản lượng (kg) | 23.000 | 22.080 (−4%) |
| Giá bán bình quân (đ/kg) | 238.000 | 244.000 |
| Biến phí (đ/kg) | 172.000 | 166.000 (hợp đồng giá nhân 114.000; cắt ship 2.000) |
| Doanh thu (tr) | 5.474 | 5.387,52 |
| Số dư đảm phí (tr) | 1.518 | 1.722,24 |
| Định phí (tr) | (1.390) | (1.390) |
| **Lợi nhuận hoạt động (tr)** | **128** | **332,24** |

Kịch bản B: CM đơn vị = 244.000 − 166.000 = 78.000đ/kg; lợi nhuận = 22.080 × 78.000 − 1.390tr = 1.722,2 − 1.390 = **332,2tr** — cao gấp 2,6 lần kịch bản A dù bán ít hơn. Điểm hòa vốn mới = 1.390tr / 78.000 = **17.821 kg**, biên an toàn = (22.080 − 17.821)/22.080 = **19,3%**.

#### Bước 7 — Dự báo dòng tiền 13 tuần (tuần 1–13 của quý II)

Lợi nhuận dương không bảo đảm tiền dương. Công ty dự định mua máy rang mới 300tr vào tuần 9 và đang có khoản vay trả 120tr vào tuần 6 và 12.

**Giả định dòng tiền (giả định minh họa):** tiền đầu quý 350tr; mỗi tuần bán 23.000/13 = 1.769 kg × 238.000đ = 421,1tr; 40% thu ngay (online/bán lẻ), 60% thu sau 4 tuần (khách buôn thanh toán 30 ngày; 4 tuần đầu thu từ doanh thu Q1 = 5.236/13 = 402,8tr/tuần × 60% = 241,7tr + 40% × 421,1 = 168,4tr → 410,1tr); biến phí tiền (nhân 118.000 + bao bì 13.000 + vận chuyển 22.000 = 153.000đ/kg) = 270,7tr/tuần; lương công nhân trực tiếp (19.000đ/kg) và định phí tiền (1.300tr/quý, tức 1.390 trừ khấu hao 90) trả theo tháng ở tuần 4, 8, 13.

**Phương án 1 – giữ kế hoạch mua máy 300tr ở tuần 9:**

| Tuần | Tiền đầu | Thu tiền | Biến phí tuần | Lương NV | Định phí | Trả nợ | CapEx | Tiền cuối | Cảnh báo (<150) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 350,0 | 410,1 | (270,7) | 0 | 0 | 0 | 0 | 489,4 |  |
| 2 | 489,4 | 410,1 | (270,7) | 0 | 0 | 0 | 0 | 628,8 |  |
| 3 | 628,8 | 410,1 | (270,7) | 0 | 0 | 0 | 0 | 768,2 |  |
| 4 | 768,2 | 410,1 | (270,7) | (134,5) | (433,3) | 0 | 0 | 339,8 |  |
| 5 | 339,8 | 421,1 | (270,7) | 0 | 0 | 0 | 0 | 490,2 |  |
| 6 | 490,2 | 421,1 | (270,7) | 0 | 0 | (120) | 0 | 520,6 |  |
| 7 | 520,6 | 421,1 | (270,7) | 0 | 0 | 0 | 0 | 671,0 |  |
| 8 | 671,0 | 421,1 | (270,7) | (134,5) | (433,3) | 0 | 0 | 253,5 |  |
| 9 | 253,5 | 421,1 | (270,7) | 0 | 0 | 0 | (300) | **103,9** | CẢNH BÁO |
| 10 | 103,9 | 421,1 | (270,7) | 0 | 0 | 0 | 0 | 254,3 |  |
| 11 | 254,3 | 421,1 | (270,7) | 0 | 0 | 0 | 0 | 404,7 |  |
| 12 | 404,7 | 421,1 | (270,7) | 0 | 0 | (120) | 0 | 435,1 |  |
| 13 | 435,1 | 421,1 | (270,7) | (168,1) | (433,3) | 0 | 0 | **-15,9** | CẢNH BÁO |

**Phát hiện:** Dù lợi nhuận quý dương, **tiền cuối tuần 9 chỉ còn 103,9tr (dưới ngưỡng cảnh báo 150tr) và tuần 13 âm 15,9tr**. Nguyên nhân: kỳ trả lương + định phí dồn vào tuần 4, 8, 13; khoản thu từ khách buôn đến chậm 4 tuần; và 300tr mua máy bơm cạn tiền ngay đúng thời điểm lương tuần 13 sắp đến.

**Phương án 2 – hoãn mua máy sang quý III (hoặc thuê tài chính):**

| Tuần | Tiền đầu | Thu tiền | Biến phí tuần | Lương NV | Định phí | Trả nợ | CapEx | Tiền cuối | Cảnh báo (<150) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 350,0 | 410,1 | (270,7) | 0 | 0 | 0 | 0 | 489,4 |  |
| 2 | 489,4 | 410,1 | (270,7) | 0 | 0 | 0 | 0 | 628,8 |  |
| 3 | 628,8 | 410,1 | (270,7) | 0 | 0 | 0 | 0 | 768,2 |  |
| 4 | 768,2 | 410,1 | (270,7) | (134,5) | (433,3) | 0 | 0 | 339,8 |  |
| 5 | 339,8 | 421,1 | (270,7) | 0 | 0 | 0 | 0 | 490,2 |  |
| 6 | 490,2 | 421,1 | (270,7) | 0 | 0 | (120) | 0 | 520,6 |  |
| 7 | 520,6 | 421,1 | (270,7) | 0 | 0 | 0 | 0 | 671,0 |  |
| 8 | 671,0 | 421,1 | (270,7) | (134,5) | (433,3) | 0 | 0 | 253,5 |  |
| 9 | 253,5 | 421,1 | (270,7) | 0 | 0 | 0 | 0 | 403,9 |  |
| 10 | 403,9 | 421,1 | (270,7) | 0 | 0 | 0 | 0 | 554,3 |  |
| 11 | 554,3 | 421,1 | (270,7) | 0 | 0 | 0 | 0 | 704,7 |  |
| 12 | 704,7 | 421,1 | (270,7) | 0 | 0 | (120) | 0 | 735,1 |  |
| 13 | 735,1 | 421,1 | (270,7) | (168,1) | (433,3) | 0 | 0 | 284,1 |  |

Tiền thấp nhất chỉ giảm xuống 253,5tr (tuần 8) và kết thúc quý với 284,1tr — an toàn trên ngưỡng 150tr suốt cả quý.

#### Bước 8 — Quyết định và bài học

**Hành động chọn (theo khuyến nghị):**
1. Áp dụng Kịch bản B: ngừng chiết khấu đại trà; ký hợp đồng giá cố định nguyên liệu.
2. Hoãn mua máy sang Q3 hoặc thương lượng thuê tài chính để rải chi phí; nếu vẫn cần mua, thương lượng hạn mức vay 300tr trước.
3. Lập dòng tiền 13 tuần cập nhật mỗi thứ Hai; báo động khi tiền cuối tuần dự kiến < 150tr (khoảng 1/3 chi phí tiền cố định hằng tháng).
4. Chuyển đánh giá nhân viên kinh doanh từ "doanh số" sang "số dư đảm phí" (mỗi kg bán ra phải đạt tối thiểu 80.000đ CM).

**Bài học rút ra:**
- **Doanh số cao không đồng nghĩa lợi nhuận cao** — luôn phân tích bằng ngân sách linh hoạt để tách hiệu ứng khối lượng.
- **Biên an toàn** là chỉ số cảnh báo sớm: từ 25% tụt còn 4,3% chỉ sau một quý.
- **Lợi nhuận ≠ dòng tiền** — một quý có lãi vẫn có thể có tuần thiếu tiền nếu dồn khoản chi lớn.
- **Ngân sách theo yếu tố dẫn dắt** (số quán × kg/quý, giá, chi phí/kg) giúp đối chiếu từng yếu tố khi có chênh lệch, thay vì chỉ có một con số "tăng 15%" trừu tượng.

---

## IV. ỨNG DỤNG CHO SME

### 1. Đặc thù lập ngân sách của SME Việt Nam so với công ty lớn

| Yếu tố | Doanh nghiệp lớn | SME Việt Nam | Hệ quả khi lập ngân sách |
|--------|------------------|--------------|---------------------------|
| Nhân sự tài chính | Có phòng FP&A riêng | Chủ DN + 1–2 kế toán (thường thuê ngoài) | Phải dùng mẫu đơn giản, ít dòng |
| Dữ liệu | Hệ thống ERP, dữ liệu lịch sử nhiều năm | Dữ liệu rời rạc (Excel, POS, sổ tay) | Bắt đầu bằng thu thập dữ liệu 12 tháng gần nhất |
| Biến động | Ổn định hơn nhờ đa dạng hóa | Phụ thuộc vài khách hàng/sản phẩm | Cần kịch bản xấu và dòng tiền 13 tuần |
| Nguồn vốn | Đa dạng (trái phiếu, vốn cổ phần) | Chủ yếu vốn tự có + vay ngân hàng | Dòng tiền là ưu tiên số 1 |
| Quyết định | Qua nhiều cấp | Chủ DN quyết nhanh | Ngân sách phải ngắn gọn để chủ đọc và hành động |
| Thuế & hóa đơn | Chuyên nghiệp hóa | Dễ lẫn chi tiêu cá nhân – công ty | Tách bạch tài khoản; ngân sách chi phí hợp lệ (cần xác nhận hiện hành) |

→ **Nguyên tắc cho SME:** ngân sách phải **đủ dùng, không hoàn hảo** — ba ngân sách sống còn là *Bán hàng – Chi phí – Tiền mặt*; mọi thứ khác là bổ sung dần.

### 2. Mẫu ngân sách 1 trang cho SME

```
┌──────────────────────────────────────────────────┐
│     NGÂN SÁCH NĂM 20XX – CÔNG TY ABC             │
│                                                  │
│  I. DOANH THU DỰ KIẾN                            │
│     Sản phẩm A: số lượng × giá = _____           │
│     Sản phẩm B: số lượng × giá = _____           │
│     Dịch vụ:                    _____            │
│     Tổng doanh thu:             _____________    │
│                                                  │
│  II. CHI PHÍ BIẾN ĐỔI                            │
│     NVL: ___% doanh thu =       _____            │
│     Nhân công trực tiếp:        _____            │
│     Hoa hồng bán hàng:          _____            │
│     Vận chuyển:                 _____            │
│     Tổng biến phí:              _____________    │
│                                                  │
│  III. SỐ DƯ ĐẢM PHÍ (CM)        _____________    │
│       CM% =                     _____%           │
│                                                  │
│  IV. CHI PHÍ CỐ ĐỊNH                             │
│     Thuê mặt bằng:              _____            │
│     Lương quản lý:              _____            │
│     Bảo hiểm:                   _____            │
│     Marketing:                  _____            │
│     Phần mềm/IT:                _____            │
│     Khấu hao:                   _____            │
│     Khác:                       _____            │
│     Tổng định phí:              _____________    │
│                                                  │
│  V. LỢI NHUẬN DỰ KIẾN           _____________    │
│     Biên lợi nhuận hoạt động:   _____%           │
│     Điểm hòa vốn (doanh thu):   _____________    │
│                                                  │
│  VI. DÒNG TIỀN                                   │
│     Thu tiền dự kiến:           _____            │
│     Chi tiền dự kiến:           _____            │
│     Dòng tiền thuần:            _____________    │
└──────────────────────────────────────────────────┘
```

**Cách điền nhanh (30–60 phút cho SME nhỏ):** (1) lấy doanh thu thực 12 tháng gần nhất theo sản phẩm/kênh; (2) tách chi phí thành biến phí/định phí (cách tách: chi phí nào thay đổi cùng doanh số thì là biến phí); (3) xác định *yếu tố dẫn dắt* (số khách × giá trị đơn, số kg × giá...) cho năm tới; (4) tính lợi nhuận và điểm hòa vốn; (5) chuyển sang lịch thu – chi tiền để thấy tháng nào căng nhất.

### 3. Quy trình lập ngân sách 6 bước và lịch hàng tháng

| Bước | Hành động | Người thực hiện | Thời gian gợi ý |
|------|-----------|------------------|------------------|
| 1 | Chủ DN đặt mục tiêu tổng (doanh thu, lợi nhuận, tiền mặt tối thiểu) | Chủ DN/CEO | T11 tuần 1 |
| 2 | Các bộ phận lập ngân sách chi tiết theo yếu tố dẫn dắt | Quản lý bộ phận | T11 tuần 2–3 |
| 3 | Kế toán tổng hợp, kiểm tra nhất quán (ngân sách bán – sản xuất – tiền) | Kế toán/CFO | T11 tuần 4 |
| 4 | Họp rà soát, điều chỉnh, thương lượng | CEO + đội ngũ | T12 tuần 1 |
| 5 | Phê duyệt | CEO | T12 tuần 2 |
| 6 | Triển khai và theo dõi hàng tháng | Kế toán | Hàng tháng |

**Lịch theo dõi hàng tháng (chu kỳ "Plan – Do – Check – Act"):**

| Ngày | Việc phải làm | Đầu ra |
|------|---------------|--------|
| Ngày 1–5 | Khép sổ tháng trước | Số liệu thực tế |
| Ngày 6–8 | So sánh thực tế với ngân sách linh hoạt, phân tích chênh lệch | Báo cáo variance 1 trang |
| Ngày 9–10 | Họp 30–45 phút: nguyên nhân, hành động, người phụ trách | Danh sách hành động |
| Ngày 11 | Cập nhật dự báo cuốn chiếu và dòng tiền 13 tuần | Dự báo mới |
| Hằng tuần | Cập nhật dòng tiền 13 tuần | Cảnh báo tiền mặt |

### 4. Dòng tiền 13 tuần (13-Week Cash Flow Forecast) cho startup và SME

**Tại sao 13 tuần?** 13 tuần = 1 quý: đủ ngắn để dự báo chính xác (tuần đầu gần như chắc chắn, tuần 13 còn đoán được), đủ dài để kịp hành động (đàm phán vay, hoãn chi, giục thu nợ). **Xuất xứ:** kỹ thuật này phổ biến trong tái cơ cấu doanh nghiệp (turnaround) tại Mỹ, nơi ngân hàng đòi doanh nghiệp khó khăn báo cáo tiền mặt hàng tuần *(cần đối chiếu nguồn)*; startup và SME dùng lại vì cùng nỗi lo: **hết tiền trước khi hết ngân sách**.

```
  Tuần →          1    2    3    4    5   ...  13
  ────────────────────────────────────────────────
  Tiền đầu tuần   50   42   35   28   31  ...  XX
  + Thu tiền       0   10   25   30   15  ...
  − Trả NCC       (5)  (8)  (20) (15) (12) ...
  − Lương          0    0  (10)   0    0   (10)
  − Thuê           0    0    0  (10)   0    0
  − Khác          (3)  (9)  (2)  (2)  (5)  ...
  ────────────────────────────────────────────────
  Tiền cuối tuần  42   35   28   31   29  ...  XX
  ────────────────────────────────────────────────
  Cảnh báo nếu < 20 triệu → NGUY HIỂM
```

*Kiểm tra số học của bảng mẫu (đơn vị triệu đồng):* Tuần 1: 50 − 5 − 3 = 42; tuần 2: 42 + 10 − 8 − 9 = 35; tuần 3: 35 + 25 − 20 − 10 − 2 = 28; tuần 4: 28 + 30 − 15 − 10 − 2 = 31; tuần 5: 31 + 15 − 12 − 5 = 29.

**Nguyên tắc dùng:** (1) tính theo **tiền thực thu/thực chi theo tuần**, không theo hóa đơn; (2) ngưỡng cảnh báo = số tiền cần để chi lương và các khoản không thể hoãn trong 2–4 tuần tới; (3) cập nhật mỗi tuần: thay dự báo tuần vừa qua bằng thực tế, thêm tuần 14; (4) luôn có "phương án B" cho tuần thiếu tiền (hoãn mua sắm, giục thu nợ, hạn mức vay).

### 5. Bảng ưu tiên triển khai Budgeting & Forecasting cho SME

| # | Hạng mục | Tần suất | Ưu tiên |
|---|----------|----------|---------|
| 1 | Lập ngân sách năm tối thiểu (Bán hàng + Chi phí + Tiền mặt) | Năm | ★★★ |
| 2 | Dòng tiền 13 tuần | Cập nhật hàng tuần | ★★★ |
| 3 | So sánh thực tế với ngân sách hàng tháng (linh hoạt) | Tháng | ★★★ |
| 4 | Cập nhật dự báo cuốn chiếu | Quý (hoặc tháng) | ★★ |
| 5 | Kịch bản (Tốt – Cơ sở – Xấu) và kiểm tra điểm hòa vốn | Năm hoặc khi có biến động | ★★ |
| 6 | Rà soát ZBB cho các khoản chi lớn nhất | Năm | ★ |

### 6. Bảng điều khiển 10 chỉ số cảnh báo hàng tháng

| # | Chỉ số | Công thức | Ngưỡng cảnh báo gợi ý |
|---|--------|-----------|------------------------|
| 1 | Doanh thu thực tế / ngân sách linh hoạt | Thực tế ÷ Ngân sách | < 95% hoặc > 110% |
| 2 | Số dư đảm phí % | CM ÷ Doanh thu | Giảm > 2 điểm so với ngân sách |
| 3 | Chênh lệch giá bán | (Giá thực − Giá NS) × SL | Âm 3 tháng liên tiếp |
| 4 | Chênh lệch giá nguyên liệu | (Giá mua thực − Giá định mức) × SL | > 5% |
| 5 | Định phí thực / ngân sách | | > 105% |
| 6 | Biên an toàn | (SL − SL hòa vốn) ÷ SL | < 15% |
| 7 | Tiền mặt tối thiểu 13 tuần | Min(tiền cuối tuần) | Dưới ngưỡng cảnh báo |
| 8 | Vòng quay phải thu (DSO) | Phải thu ÷ Doanh thu × số ngày | Tăng > 5 ngày so với kế hoạch |
| 9 | Tồn kho (ngày) | Tồn kho ÷ Giá vốn × số ngày | > ngân sách + 10% |
| 10 | MAPE dự báo doanh thu | Xem mục II.D.6 | > 15% |

*(Các ngưỡng là gợi ý khởi điểm; mỗi ngành cần hiệu chỉnh theo dữ liệu lịch sử của chính doanh nghiệp.)*

### 7. Sai lầm thường gặp và cách tránh

| # | Sai lầm | Hậu quả | Cách tránh |
|---|---------|---------|-----------|
| 1 | Lập ngân sách bằng cách "lấy năm ngoái cộng 15%" | Không biết giả định nằm ở đâu | Dựng theo yếu tố dẫn dắt (số khách × giá trị đơn) |
| 2 | Chỉ lập ngân sách lợi nhuận, bỏ ngân sách tiền mặt | Có lãi nhưng hết tiền | Luôn có dòng tiền 13 tuần |
| 3 | So sánh với ngân sách tĩnh khi sản lượng đã đổi | Kết luận sai (như case Cầu Đất Xanh) | Dùng ngân sách linh hoạt |
| 4 | Thưởng theo doanh số, không theo lợi nhuận/CM | Giảm giá, bán lỗ để đạt doanh số | Thưởng theo số dư đảm phí |
| 5 | Ngân sách "đóng đinh" cả năm | Lỗi thời sau quý 1 | Dự báo cuốn chiếu hàng quý |
| 6 | Trộn chi tiêu cá nhân và công ty | Ngân sách vô nghĩa, rủi ro thuế | Tách tài khoản (cần xác nhận hiện hành) |
| 7 | Không tính mùa vụ | Hết tiền ở mùa thấp | Chỉ số mùa vụ + đệm tiền mặt |
| 8 | Lập ngân sách chỉ một mình chủ DN | Thiếu cam kết của người thực hiện | Cho quản lý bộ phận tham gia, chủ DN kiểm chứng |
| 9 | Dự báo nhưng không đo sai số | Không biết mô hình có đáng tin | Theo dõi MAPE, tracking signal |
| 10 | Dùng dự báo lạc quan để "đẹp hồ sơ vay" | Vi phạm covenant | Kiểm tra bằng kịch bản xấu |

### 8. Lộ trình triển khai theo quy mô

| Quy mô | Việc nên làm | Công cụ |
|--------|--------------|---------|
| Hộ kinh doanh/Micro (<5 người) | Sổ thu–chi theo tuần, ngân sách tiền mặt 13 tuần, theo dõi biên lợi nhuận | Google Sheets |
| Nhỏ (5–20 người) | Ngân sách năm 1 trang, variance hàng tháng, dự báo quý | Excel/Sheets + phần mềm kế toán |
| Vừa (20–100 người) | Master budget, ngân sách linh hoạt, cuốn chiếu, ZBB cho chi phí lớn | Phần mềm kế toán/ERP + BI |

---

## V. TOOLS & TEMPLATES

### 1. Phần mềm và công cụ hỗ trợ (giá mang tính tham khảo)

> **Lưu ý về giá**: Mọi mức giá dưới đây là **ước tính tham khảo, cần xác nhận với nhà cung cấp tại thời điểm mua** (giá thay đổi theo gói, số người dùng, khuyến mãi, thuế VAT).

| Nhóm | Công cụ | Công dụng cho ngân sách & dự báo | Giá tham khảo (ước tính, cần xác nhận) | Phù hợp |
|------|---------|----------------------------------|-----------------------------------------|---------|
| Bảng tính | **Google Sheets** | Mô hình ngân sách, dòng tiền 13 tuần, chia sẻ nhiều người | Miễn phí (tài khoản cá nhân); gói doanh nghiệp tính theo người dùng | Mọi SME |
| Bảng tính | **Microsoft Excel (Microsoft 365)** | Mô hình tài chính, Data Table cho kịch bản, hàm FORECAST | Khoảng vài trăm nghìn đồng/người/tháng tùy gói | SME đã quen Excel |
| Kế toán | **MISA (MISA SME, MISA AMIS Kế toán)** | Số liệu thực tế (sổ cái, công nợ, tồn kho) để so sánh với ngân sách; một số gói có báo cáo quản trị | Khoảng vài triệu đến chục triệu đồng/năm tùy gói | SME từ nhỏ đến vừa |
| Kế toán | **Fast Accounting** | Tương tự; mạnh về báo cáo quản trị, nhiều ngành | Khoảng vài triệu đến vài chục triệu đồng/năm hoặc mua bản quyền | SME vừa |
| Bán hàng/POS | **KiotViet, Sapo** | Doanh số thực tế theo sản phẩm/ca/chi nhánh, tồn kho; xuất Excel để đối chiếu | Khoảng vài trăm nghìn đồng/tháng tùy gói và số cửa hàng | Bán lẻ, F&B |
| Báo cáo | **Looker Studio (Google)** | Dashboard variance và dòng tiền từ Sheets | Miễn phí | SME muốn dashboard đơn giản |
| Báo cáo | **Power BI** | BI nâng cao, liên kết nhiều nguồn | Khoảng 10–14 USD/người/tháng cho bản Pro | SME vừa có dữ liệu |
| FP&A chuyên dụng | Anaplan, Adaptive Planning, Planful... | Lập ngân sách và dự báo cho doanh nghiệp lớn | Giá theo báo giá, thường cao | DN lớn (không cần cho SME) |

### 2. Cấu trúc file Excel/Google Sheets gợi ý (5 tab)

```
TAB 1 — INPUTS (chỉ nhập số ở đây, màu xanh):
  - Giá bán, biến phí đơn vị, định phí (theo tháng/quý)
  - Chính sách tồn kho, kỳ thu tiền (% thu ngay, % thu chậm)
  - Tiền đầu kỳ, tiền tối thiểu, lãi vay

TAB 2 — BÁN HÀNG & SẢN XUẤT:
  - Sales Budget → Production Budget → NVL (công thức theo mục II.A)

TAB 3 — CHI PHÍ & P&L:
  - Biến phí, định phí, lợi nhuận, điểm hòa vốn, biên an toàn

TAB 4 — TIỀN MẶT:
  - Lịch thu tiền, lịch chi tiền, dòng tiền 13 tuần
  - Conditional formatting: tô đỏ khi tiền cuối tuần < ngưỡng

TAB 5 — ACTUAL vs BUDGET:
  - Cột: Tĩnh | Linh hoạt | Thực tế | Chênh lệch khối lượng/giá/biến phí/định phí
  - Dashboard: biểu đồ cột chênh lệch, đường dòng tiền
```

**Công thức Excel hữu ích:**

| Mục đích | Công thức (ví dụ) |
|----------|--------------------|
| Trung bình di động 3 kỳ | `=AVERAGE(B2:B4)` kéo xuống |
| San mũ | `=$H$1*B3+(1-$H$1)*C3` (H1 = α) |
| Hồi quy tuyến tính | `=FORECAST.LINEAR(40, Y_range, X_range)`; hệ số: `=SLOPE(Y,X)`, `=INTERCEPT(Y,X)` |
| MAPE | `=SUMPRODUCT(ABS((A-F)/A))/COUNT(A)` |
| Tồn kho cuối kỳ | `=0.2*Bán_kỳ_sau` |
| Điểm hòa vốn | `=Định_phí/(Giá-Biến_phí)` |

### 3. Mẫu báo cáo chênh lệch hàng tháng (1 trang)

| Khoản mục | Ngân sách tĩnh | Ngân sách linh hoạt | Thực tế | Chênh lệch (TT − Linh hoạt) | Nguyên nhân & hành động |
|-----------|----------------|---------------------|---------|------------------------------|-------------------------|
| Sản lượng | | | | | |
| Doanh thu | | | | | |
| Biến phí | | | | | |
| Số dư đảm phí | | | | | |
| Định phí | | | | | |
| Lợi nhuận hoạt động | | | | | |

---

## VI. BÀI TẬP THỰC HÀNH

> Đáp số dưới đây đã được kiểm tra bằng Python; đơn vị triệu đồng (tr) trừ khi ghi khác.

### Bài 1 (Cơ bản — Ngân sách sản xuất)
Một xưởng bánh dự kiến bán 8.000; 10.000; 9.000; 7.000 chiếc trong Q1–Q4; dự kiến bán Q1 năm sau là 8.000 chiếc. Chính sách: tồn kho cuối kỳ = 25% nhu cầu bán quý sau; tồn đầu năm 1.500 chiếc. Tính số chiếc cần sản xuất mỗi quý.

*Đáp số*: Tồn cuối kỳ = 2.500; 2.250; 1.750; 2.000. Sản xuất = **9.000; 9.750; 8.500; 7.250** chiếc.
*(Ví dụ Q1: 8.000 + 2.500 − 1.500 = 9.000.)*

### Bài 2 (Cơ bản — Ngân sách linh hoạt)
Ngân sách tĩnh: bán 5.000 sản phẩm, giá 80.000đ, biến phí 45.000đ/sản phẩm, định phí 120tr. Thực tế: bán 5.600 sản phẩm, doanh thu 436tr, biến phí 266tr, định phí 126tr. (a) Tính lợi nhuận tĩnh, linh hoạt và thực tế. (b) Phân tích chênh lệch.

*Đáp số*: (a) Tĩnh = 5.000 × 35.000 − 120 = **55tr**; Linh hoạt = 5.600 × 35.000 − 120 = **76tr**; Thực tế = 436 − 266 − 126 = **44tr**. (b) Khối lượng **+21tr (F)**; giá bán (436 − 448) = **−12tr**; biến phí (266 − 252) = **−14tr**; định phí **−6tr**. Tổng = 21 − 12 − 14 − 6 = **−11tr** = 44 − 55 ✓. *(Kết luận: bán nhiều hơn nhưng hiệu quả kém đi.)*

### Bài 3 (Trung bình — Dự báo)
Doanh thu 6 tháng: 80; 90; 85; 100; 95; 110 (triệu). Dự báo tháng 7 bằng (a) MA-3, (b) san mũ α = 0,5 với F₁ = 80.

*Đáp số*: (a) (100 + 95 + 110)/3 = **101,67**. (b) F₂ = 80; F₃ = 85; F₄ = 85; F₅ = 92,5; F₆ = 93,75; F₇ = **101,875**.

### Bài 4 (Trung bình — Độ chính xác dự báo)
Thực tế: 100; 120; 110; 130; 125. Dự báo: 105; 115; 118; 122; 128. Tính MAD, MAPE, MSE và Tracking Signal.

*Đáp số*: Sai số (A − F) = −5; +5; −8; +8; −3. **MAD = 5,8; MAPE ≈ 5,0%; MSE = 37,4; Tracking Signal = −3/5,8 ≈ −0,52** (trong ngưỡng ±4, không có thiên lệch rõ).

### Bài 5 (Trung bình — Hồi quy)
Chi phí quảng cáo X (tr): 10; 15; 12; 20; 18. Doanh thu Y (tr): 130; 170; 145; 215; 195. Tìm Y = a + bX và dự báo Y khi X = 25.

*Đáp số*: ΣX = 75; ΣY = 855; ΣXY = 13.400; ΣX² = 1.193; **b ≈ 8,456; a ≈ 44,16**; Y(25) = **255,6tr**.

### Bài 6 (Trung bình — Zero-Based Budgeting)
Ngân sách trần 100tr, các gói (chi phí; lợi nhuận gộp kỳ vọng): A (20; 70), B (35; 80), C (25; 50), D (30; 45), E (15; 40), F (10; 12). Hãy xếp hạng và quyết định.

*Đáp số*: Tỷ lệ lợi ích/chi phí: A 3,50; E 2,67; B 2,29; C 2,00; D 1,50; F 1,20. Cộng dồn: A 20 → E 35 → B 70 → C 95. D (30) vượt trần (125); F (10) cũng vượt (105). **Duyệt A, E, B, C = 95tr; cắt/hoãn D và F; còn dư 5tr.**

### Bài 7 (Nâng cao — Ngân sách tiền mặt)
Doanh thu Q1–Q3: 200; 240; 280. Thu 70% trong quý, 30% quý sau; phải thu đầu năm 60. Chi vận hành: 150; 170; 190; định phí tiền 40/quý; mua máy 80 vào Q2. Tiền đầu năm 30. Tính tiền cuối mỗi quý. Cần vay khi nào, tối thiểu bao nhiêu?

*Đáp số*: Thu tiền: Q1 = 0,7 × 200 + 60 = 200; Q2 = 0,7 × 240 + 0,3 × 200 = 228; Q3 = 0,7 × 280 + 0,3 × 240 = 268. Chi: Q1 = 190; Q2 = 170 + 40 + 80 = 290; Q3 = 230. Tiền cuối: Q1 = **40**; Q2 = 40 + 228 − 290 = **−22**; Q3 = −22 + 268 − 230 = **16**. Cần vay **tối thiểu 22tr** trong Q2 (thực tế nên vay dư để giữ đệm tối thiểu).

### Bài 8 (Nâng cao — Tự thực hành)
Áp dụng toàn bộ quy trình ở Case III.3 cho doanh nghiệp của bạn: (1) dựng ngân sách tháng/quý theo yếu tố dẫn dắt; (2) lập ngân sách linh hoạt; (3) tách chênh lệch khối lượng, giá, biến phí, định phí; (4) tính điểm hòa vốn và biên an toàn; (5) dựng dòng tiền 13 tuần; (6) xác định tuần có tiền thấp nhất và hành động. *(Đáp án mở — hãy tự kiểm tra tổng chênh lệch có khớp với hiệu số lợi nhuận hay không.)*

---

## PHỤ LỤC: CHECKLIST BUDGETING & FORECASTING TỔNG HỢP

### A. Checklist rà soát trước khi áp dụng

```
CHUẨN BỊ DỮ LIỆU:
□ Có doanh thu và chi phí thực 12–24 tháng gần nhất, tách theo sản phẩm/kênh?
□ Đã phân loại chi phí thành biến phí và định phí?
□ Đã xác định các yếu tố dẫn dắt (số khách, kg, giờ máy, giá)?
□ Tách bạch chi tiêu cá nhân và công ty?

LẬP NGÂN SÁCH:
□ Bắt đầu từ ngân sách bán hàng (hoặc yếu tố giới hạn thực tế)?
□ Ngân sách sản xuất/mua hàng/nhân công nối đúng với ngân sách bán hàng?
□ Có ngân sách tiền mặt, không chỉ ngân sách lợi nhuận?
□ Bảng cân đối dự kiến có cân (Tài sản = Nợ phải trả + Vốn chủ)?
□ Dòng tiền dự kiến khớp với thay đổi tiền giữa hai kỳ?
□ Tính điểm hòa vốn và biên an toàn?
□ Có kịch bản Tốt – Cơ sở – Xấu?

THEO DÕI & DỰ BÁO:
□ Hàng tháng so thực tế với ngân sách linh hoạt (không chỉ ngân sách tĩnh)?
□ Tách chênh lệch: khối lượng, giá bán, biến phí, định phí?
□ Có dự báo cuốn chiếu 12 tháng và dòng tiền 13 tuần cập nhật?
□ Đo sai số dự báo (MAPE, tracking signal)?
□ Có ngưỡng cảnh báo tiền mặt tối thiểu?

RỦI RO & VĂN HÓA:
□ Có cơ chế chống slack/sandbagging (benchmark, dữ liệu)?
□ Thưởng gắn với số dư đảm phí/lợi nhuận, không chỉ doanh số?
□ ZBB được áp dụng cho các khoản chi lớn nhất ít nhất mỗi năm một lần?
□ Đã kiểm tra với kế toán về quy định hiện hành (VAS/TT200/TT133, thuế, hóa đơn)?
```

### B. Công thức tổng hợp

| Nhóm | Công thức | Ghi chú |
|------|-----------|---------|
| Sản xuất | $\text{Sản lượng cần SX} = \text{Bán} + \text{Tồn cuối} - \text{Tồn đầu}$ | Phương trình cân bằng tồn kho |
| Mua NVL | $\text{NVL cần mua} = \text{NVL dùng} + \text{Tồn cuối} - \text{Tồn đầu}$ | Cùng logic |
| Hòa vốn | $Q^{*} = \frac{\text{Định phí}}{P - V}$ | Sản lượng hòa vốn |
| Biên an toàn | $\frac{Q - Q^{*}}{Q}$ | % sản lượng có thể giảm trước khi lỗ |
| Ngân sách linh hoạt | $\text{Biến phí đơn vị} \times \text{SL thực} + \text{Định phí}$ | Dùng để so sánh |
| Chênh lệch khối lượng | $(Q_{TT} - Q_{NS}) \times CM_{NS}$ | Hiệu ứng sản lượng |
| Chênh lệch giá bán | $(P_{TT} - P_{NS}) \times Q_{TT}$ | |
| Chênh lệch biến phí | $-(V_{TT} - V_{NS}) \times Q_{TT}$ | |
| Chênh lệch định phí | $-(FC_{TT} - FC_{NS})$ | |
| Trung bình di động | $F_{t+1} = \frac{1}{n}\sum_{i=t-n+1}^{t} A_i$ | |
| San mũ | $F_{t+1} = \alpha A_t + (1-\alpha) F_t$ | α cao → nhạy |
| Hồi quy | $b = \frac{n\sum XY - \sum X\sum Y}{n\sum X^2 - (\sum X)^2}$; $a = \bar{Y} - b\bar{X}$ | |
| Chỉ số mùa vụ | $\text{TB quý } i \div \text{TB chung}$ | Tổng chỉ số = số quý |
| MAD | $\frac{1}{n}\sum \|A - F\|$ | |
| MAPE | $\frac{1}{n}\sum\left\|\frac{A-F}{A}\right\| \times 100\%$ | |
| MSE | $\frac{1}{n}\sum (A-F)^2$ | |
| Tracking Signal | $\frac{\sum (A-F)}{\text{MAD}}$ | Nên trong ±4 |

---

*Tài liệu tham khảo: Garrison, Noreen & Brewer – "Managerial Accounting" Ch. 8–10 (Budgeting); Horngren – "Cost Accounting" Ch. 6 (Master Budget); Pyhrr, Peter – "Zero-Base Budgeting" (Harvard Business Review, 1970); Hope & Fraser – "Beyond Budgeting" (Harvard Business School Press, 2003); Argyris, Chris – "The Impact of Budgets on People" (1952); McKinsey, James O. – "Budgetary Control" (1922); FP&A Body of Knowledge – AFP (Association for Financial Professionals); McKinsey – "The case for Zero-Based Budgeting" (2018); Deloitte – "Rolling Forecasts: A Proactive Approach to Planning"; Luật Kế toán 88/2015/QH13, Thông tư 200/2014/TT-BTC, Thông tư 133/2016/TT-BTC (cần xác nhận hiện hành).*
