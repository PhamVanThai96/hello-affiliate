# 09. Lý thuyết Ràng buộc (Theory of Constraints - TOC)

> **Mục tiêu**: Hiểu bản chất TOC - mọi hệ thống bị giới hạn bởi một (vài) điểm nghẽn - và biết cách tập trung 100% nguồn lực vào đúng điểm đó (5 bước tập trung, Drum-Buffer-Rope, Throughput Accounting, Buffer Management, CCPM) để tăng dòng tiền, giảm tồn kho và tránh đầu tư sai chỗ, đặc biệt phù hợp SME Việt Nam vốn ít.

## MỤC LỤC

- **I. Khái niệm & Lý thuyết**: 1.1 Định nghĩa & nguồn gốc - 1.2 Vấn đề TOC giải quyết (tối ưu cục bộ, mắt xích yếu nhất) - 1.3 Mục tiêu & ba chỉ số T, I, OE - 1.4 Phân loại ràng buộc - 1.5 Chín quy tắc OPT - 1.6 Bản đồ tổng quan các công cụ TOC
- **II. Chi tiết từng thành phần**: 2.1 Năm bước tập trung - 2.2 Throughput Accounting & T/CU - 2.3 Drum-Buffer-Rope - 2.4 Buffer Management - 2.5 CCPM - 2.6 Thinking Processes (CRT, Evaporating Cloud, FRT) - 2.7 OEE - 2.8 Replenishment & Dynamic Buffer Management - 2.9 Ưu điểm & Nhược điểm - 2.10 TOC so với Lean, Six Sigma
- **III. Case Studies thực tế**: 3.1 - 3.14 (quốc tế, Việt Nam, thất bại, SME mới: xưởng inox, bảng tổng hợp)
- **IV. Ứng dụng cho SME**: quy trình triển khai, SME vs doanh nghiệp lớn, chi phí, lộ trình, rủi ro, sai lầm, vai trò lãnh đạo, dịch vụ/bán lẻ
- **V. Tools & Templates**: công cụ, phần mềm, template, Excel
- **VI. Bài tập thực hành**: 10 bài + đáp án
- **PHỤ LỤC: CHECKLIST TOC TỔNG HỢP**: checklist, công thức, thuật ngữ, KPI, sổ tay rủi ro, mức trưởng thành, tự kiểm tra
- **TÀI LIỆU THAM KHẢO**

> **Lưu ý về số liệu**: toàn bộ số liệu định lượng trong các ví dụ và case study (trừ khi ghi rõ khác) là **giả định minh họa** do tác giả thiết kế để dạy phương pháp, đã được kiểm tra tính nhất quán bằng tính toán. Các case của doanh nghiệp quốc tế (Ford, Boeing, Amazon) chỉ mô tả **bối cảnh/nguyên lý được thảo luận phổ biến**, không phải số liệu công bố chính thức; con số trong đó là minh họa.

---

## I. Khái niệm & Lý thuyết

### 1.1. Định nghĩa và nguồn gốc của Lý thuyết Ràng buộc

**Lý thuyết Ràng buộc (Theory of Constraints - TOC)** là một triết lý quản trị và hệ phương pháp cải tiến dựa trên một quan sát rất đơn giản: *mọi hệ thống (nhà máy, chuỗi cung ứng, dự án, phòng khám, thậm chí cả doanh nghiệp) luôn bị giới hạn bởi ít nhất một "ràng buộc" (Constraint/Bottleneck)*. Ràng buộc quyết định mức đầu ra tối đa của cả hệ thống, giống như sợi xích chỉ chịu được lực bằng mắt xích yếu nhất.

**Nguồn gốc (Origin)**:

| Mốc | Sự kiện (theo các nguồn phổ biến, cần đối chiếu khi trích dẫn học thuật) |
|---|---|
| Cuối thập niên 1970 | Eliyahu M. Goldratt, nhà vật lý người Israel, cùng cộng sự phát triển phần mềm lập lịch sản xuất **OPT (Optimized Production Technology)**. Ông nhận thấy các nhà máy dù có phần mềm MRP vẫn trễ đơn hàng và tồn kho cao vì lịch sản xuất không tính đến công đoạn "cổ chai" |
| 1984 | Xuất bản tiểu thuyết kinh doanh **"The Goal"** (Goldratt & Jeff Cox). Nhân vật Alex Rogo, giám đốc một nhà máy sắp bị đóng cửa, học cách tìm "Herbie" (cậu bé đi chậm nhất trong đoàn đi bộ - hình ảnh ẩn dụ cho ràng buộc). Cách kể chuyện khiến TOC lan rộng từ phòng kỹ thuật ra toàn bộ giới quản lý |
| 1990 | *The Haystack Syndrome* - nền tảng thông tin/đo lường và lập lịch Drum-Buffer-Rope |
| 1994 | *It's Not Luck* - các công cụ tư duy logic (Thinking Processes) |
| 1997 | *Critical Chain* - áp dụng TOC cho quản trị dự án |
| Sau đó | Mở rộng sang chuỗi cung ứng (Replenishment), bán hàng, marketing, y tế, giáo dục |

**Tại sao Goldratt viết tiểu thuyết thay vì sách giáo khoa?** Vì ông muốn người đọc *tự khám phá* ra nguyên lý qua các tình huống, thay vì học thuộc. Thông điệp của "The Goal" là: những gì ta tưởng là "hiệu quả" (máy nào cũng chạy kín, nhân viên nào cũng bận) lại chính là nguyên nhân làm nhà máy lỗ.

Nguyên lý này mở rộng khái niệm "điểm nghẽn" (Bottleneck) đã giới thiệu ở File 05 - Hoạch định năng lực (Mục 2.1) thành một hệ phương pháp toàn diện: không chỉ *tìm* điểm nghẽn mà còn *quản trị cả hệ thống xoay quanh nó*.

### 1.2. Vấn đề kinh doanh TOC giải quyết: tối ưu cục bộ và mắt xích yếu nhất

**Vấn đề**: Quản trị truyền thống chia doanh nghiệp thành các bộ phận, giao cho mỗi bộ phận chỉ tiêu "hiệu suất" riêng (máy chạy bao nhiêu % thời gian, nhân công làm ra bao nhiêu sản phẩm). Giả định ngầm: *nếu mỗi bộ phận tối ưu thì cả hệ thống tối ưu*. Đây là **tối ưu cục bộ (Local Optimum)**. TOC chỉ ra giả định này **sai** trong hệ thống có phụ thuộc lẫn nhau (công đoạn sau cần đầu ra của công đoạn trước): đầu ra của cả hệ thống không bao giờ vượt quá đầu ra của công đoạn chậm nhất.

**Nguyên tắc "mắt xích yếu nhất" (Weakest Link)**: sức mạnh của sợi xích = mắt xích yếu nhất. Gia cố mắt xích đã mạnh không làm xích mạnh hơn; chỉ gia cố đúng mắt xích yếu nhất mới nâng được toàn hệ thống. Đây là nền tảng triết lý cho 5 bước tập trung.

**Ví dụ minh họa step-by-step** (giả định minh họa): dây chuyền 4 công đoạn A -> B -> C -> D, năng lực (sản phẩm/giờ) và nhu cầu thị trường 80 sản phẩm/giờ:

| Công đoạn | Năng lực (sp/giờ) | Dòng chảy thực tế (sp/giờ) | Tỷ lệ sử dụng |
|---|---|---|---|
| A | 120 | 75 | 75/120 = 62,5% |
| B | 90 | 75 | 75/90 = 83,3% |
| C | 75 | 75 | 75/75 = 100% (ràng buộc) |
| D | 100 | 75 | 75/100 = 75% |

- **Bước 1 - Xác định đầu ra hệ thống**: Đầu ra = min(120, 90, 75, 100) = **75 sp/giờ** (nhỏ hơn nhu cầu 80 => C là ràng buộc).
- **Bước 2 - Điều gì xảy ra nếu "ai cũng chạy hết công suất"?** A làm 120 nhưng B chỉ nhận 90 => tồn đọng trước B: 120 - 90 = 30 sp/giờ. B làm 90 nhưng C chỉ nhận 75 => tồn đọng trước C: 90 - 75 = 15 sp/giờ. Sau 1 ca 8 giờ: tồn trước B = 30 x 8 = 240, tồn trước C = 15 x 8 = 120, tổng **360 bán thành phẩm** nằm chờ - mà đầu ra vẫn chỉ 75 sp/giờ.
- **Bước 3 - Ý nghĩa kinh doanh**: 360 sp/ca là tiền nguyên liệu chết (Inventory), tốn kho bãi, dễ hỏng, che giấu lỗi, kéo dài lead time - mà không bán thêm được cái nào. Chỉ số "hiệu suất máy A = 100%" ở đây là con số **gây hại**.

### 1.3. Mục tiêu của tổ chức và ba chỉ số tài chính (T, I, OE)

**Tại sao cần bộ chỉ số mới?** Kế toán chi phí truyền thống (Cost Accounting) hình thành từ đầu thế kỷ 20, khi nhân công trực tiếp là khoản chi lớn nhất và biến đổi theo sản lượng. Nó phân bổ mọi chi phí (kể cả gián tiếp) lên từng sản phẩm để tính "giá thành đơn vị", từ đó khuyến khích "làm nhiều hơn để chia nhỏ chi phí cố định". Goldratt cho rằng điều này dẫn tới sản xuất thừa và quyết định sai. Ông định nghĩa lại bằng 3 con số trả lời đúng câu hỏi "doanh nghiệp có đang kiếm tiền không?".

Goldratt định nghĩa mục tiêu (Goal) của doanh nghiệp vì lợi nhuận là **"kiếm tiền, bây giờ và trong tương lai"** (making money, now and in the future). Ba chỉ số:

- **Throughput (T)**: tốc độ hệ thống tạo ra tiền **thông qua bán hàng** = Doanh thu bán hàng - Chi phí hoàn toàn biến đổi (chủ yếu nguyên vật liệu trực tiếp, hoa hồng, cước vận chuyển theo đơn). Lưu ý: hàng chưa bán **không** tạo T, dù đã sản xuất xong.
- **Inventory/Investment (I)**: toàn bộ tiền hệ thống bị "chôn" vào những thứ dự định bán ra (nguyên vật liệu, bán thành phẩm, thành phẩm, máy móc, nhà xưởng).
- **Operating Expense (OE)**: toàn bộ tiền chi ra để biến Inventory thành Throughput (lương, điện nước, thuê mặt bằng, khấu hao...).

$$NP = T - OE, \qquad ROI = \frac{T - OE}{I}$$

Trong đó $NP$ là lợi nhuận ròng (Net Profit); $ROI$ là tỷ suất hoàn vốn trên vốn bị chôn trong hệ thống. Hai chỉ số phụ thường dùng: Năng suất $= T / OE$ (mỗi đồng chi vận hành tạo bao nhiêu đồng Throughput) và Vòng quay đầu tư $= T / I$.

**Thứ tự ưu tiên của TOC: T > I > OE.** Lý do: giảm OE hay I chỉ có giới hạn (không thể cắt chi phí xuống dưới 0), còn tăng T về lý thuyết không có trần (trong giới hạn thị trường).

**Ví dụ step-by-step - xưởng may "giả định minh họa"** (đơn vị: triệu VNĐ/tháng):

| Khoản | Giá trị | Cách tính |
|---|---|---|
| Doanh thu bán hàng | 1.200 | Số liệu cho trước |
| Nguyên vật liệu trực tiếp (vải, chỉ, khuy) | 480 | Hoàn toàn biến đổi theo đơn hàng |
| **Throughput (T)** | **720** | 1.200 - 480 |
| OE: lương 300 + điện nước 60 + khấu hao 80 + thuê xưởng 100 + khác 60 | **600** | Cộng các khoản |
| **Lợi nhuận ròng (NP)** | **120** | 720 - 600 |
| Inventory (I): vải, bán thành phẩm, thành phẩm, máy móc | 3.000 | Số liệu cho trước |
| **ROI (theo tháng)** | **4%** | 120 / 3.000 (tương đương khoảng 48%/năm nếu giữ nguyên) |
| Năng suất T/OE | 1,2 | 720 / 600 |
| Vòng quay T/I | 0,24 | 720 / 3.000 |

**So sánh 3 đòn bẩy (giả định mỗi đòn cải thiện 10%)**:

- Tăng T 10%: T = 792 => NP = 192 (+60%).
- Giảm OE 10%: OE = 540 => NP = 180 (+50%).
- Giảm I 10% (I = 2.700): ROI = 120/2.700 = 4,44% (tăng từ 4% lên 4,44%) và giải phóng 300 triệu tiền mặt.

**Diễn giải**: một cải thiện T 10% hiệu quả hơn giảm OE 10%, và quan trọng hơn, T là đòn bẩy duy nhất không bị chặn trên. Nhưng chỉ tăng T được khi **ràng buộc** được giải phóng - đó là lý do cần phần còn lại của TOC.

### 1.4. Phân loại ràng buộc (Types of Constraints)

```
┌───────────────────────────────────────────────────────────┐
│  1. RÀNG BUỘC VẬT LÝ (Physical Constraint)                  │
│     Máy móc, nhân lực, nguyên vật liệu không đủ              │
├───────────────────────────────────────────────────────────┤
│  2. RÀNG BUỘC THỊ TRƯỜNG (Market Constraint)                 │
│     Nhu cầu thị trường thấp hơn năng lực sản xuất             │
├───────────────────────────────────────────────────────────┤
│  3. RÀNG BUỘC CHÍNH SÁCH (Policy Constraint)                 │
│     Quy định/quy trình nội bộ lỗi thời cản trở hiệu suất       │
├───────────────────────────────────────────────────────────┤
│  4. RÀNG BUỘC NGUỒN LỰC (Resource Constraint)                │
│     Thiếu nhân sự có kỹ năng, thiếu vốn đầu tư                │
└───────────────────────────────────────────────────────────┘
```

**Tại sao phân loại?** Mỗi loại cần cách xử lý khác nhau: ràng buộc vật lý/nguồn lực xử lý bằng 5 bước tập trung; ràng buộc thị trường cần chiến lược bán hàng/giá (xem case 3.9); ràng buộc chính sách cần công cụ tư duy (CRT, Evaporating Cloud). Thực tế, **ràng buộc chính sách là loại phổ biến và khó thấy nhất** (ví dụ: "mọi máy phải đạt hiệu suất 90%", "đơn hàng nhỏ phải đợi gộp lô"), vì nó nằm trong thói quen chứ không nằm trên sàn xưởng.

### 1.5. Chín quy tắc OPT (Nguyên lý nền tảng của lập lịch theo ràng buộc)

Từ thời OPT, Goldratt tổng hợp 9 quy tắc (tóm tắt):

1. Cân bằng **dòng chảy**, không cân bằng năng lực.
2. Mức sử dụng của công đoạn không phải ràng buộc được quyết định bởi ràng buộc, không phải bởi năng lực riêng của nó.
3. "Sử dụng" (Utilization) và "kích hoạt" (Activation) không đồng nghĩa: máy chạy không có nghĩa là đang tạo giá trị.
4. **Một giờ mất ở ràng buộc là một giờ mất của cả hệ thống.**
5. Một giờ tiết kiệm ở công đoạn không phải ràng buộc chỉ là ảo giác (không tăng đầu ra).
6. Ràng buộc chi phối cả Throughput lẫn Inventory.
7. Lô chuyển (Transfer batch) không nhất thiết bằng lô sản xuất (Process batch).
8. Lô sản xuất nên biến đổi, không cố định.
9. Lịch phải được lập bằng cách xem xét **đồng thời** mọi ràng buộc; lead time là kết quả của lịch, không phải đầu vào cố định.

### 1.6. Bản đồ tổng quan các công cụ TOC

```
                         MỤC TIÊU: Kiếm tiền (T tăng, I giảm, OE giảm)
                                         │
        ┌────────────────────┬───────────┴────────────┬─────────────────────┐
        ▼                    ▼                        ▼                     ▼
  ĐO LƯỜNG             LẬP LỊCH & ĐỒNG BỘ       DỰ ÁN & CHUỖI CUNG ỨNG   TƯ DUY LOGIC
  Throughput           5 bước tập trung          CCPM (Project Buffer)    Current Reality Tree
  Accounting           Drum-Buffer-Rope          Replenishment            Evaporating Cloud
  (T, I, OE, T/CU)     Buffer Management         Dynamic Buffer Mgmt      Future Reality Tree
```

---

## II. Chi tiết từng thành phần

### 2.1. Quy trình 5 bước tập trung của TOC (Five Focusing Steps)

**Tại sao cần 5 bước, và tại sao đúng thứ tự này?** Cải tiến không có định hướng thường dàn trải. 5 bước ép doanh nghiệp đi từ **rẻ nhất, nhanh nhất** (Exploit, Subordinate) đến **đắt nhất** (Elevate), và đảm bảo không dừng lại (Repeat). Thứ tự quan trọng vì Elevate là bước tốn tiền; nếu bỏ qua Exploit, doanh nghiệp có thể bỏ ra hàng tỷ để mua cái mà một lịch trình tốt cho ra miễn phí.

1. **Identify (Xác định)**: tìm ràng buộc - công đoạn có năng lực nhỏ nhất so với nhu cầu, hoặc nơi tồn đọng hàng chờ lớn nhất. Dấu hiệu nhận biết: hàng chờ dài **trước** nó, công đoạn **sau** nó thường nhàn rỗi, tăng ca thường xuyên.
2. **Exploit (Khai thác)**: lấy tối đa từ ràng buộc hiện có mà **không** đầu tư thêm: không để ràng buộc đói việc, không để nó làm hàng lỗi, không để nó chạy sản phẩm có T/CU thấp khi còn đơn hàng có T/CU cao hơn, giảm thời gian chuyển đổi, nghỉ trưa luân phiên để máy không dừng.
3. **Subordinate (Phụ thuộc hoá)**: mọi công đoạn khác phải phục vụ nhịp độ ràng buộc: không sản xuất vượt ràng buộc, chấp nhận nhàn rỗi có chủ đích, bảo vệ ràng buộc bằng buffer.
4. **Elevate (Nâng cấp)**: chỉ khi 2 bước trên chưa đủ đáp ứng nhu cầu mới đầu tư (máy mới, ca mới, nhân sự mới, thuê ngoài) - và phải tính ROI.
5. **Repeat (Lặp lại)**: khi ràng buộc cũ được "phá", ràng buộc mới xuất hiện ở nơi khác (có thể là thị trường). Quay lại bước 1; cảnh giác với **quán tính (Inertia)** - các quy tắc/chính sách thiết lập cho ràng buộc cũ có thể trở thành ràng buộc chính sách mới.

**Ví dụ tiếp nối từ dây chuyền A-B-C-D (mục 1.2), giả định T = 40.000 VNĐ/sản phẩm**:

- **Identify**: C (75 sp/giờ) là ràng buộc vì nhỏ hơn nhu cầu 80 sp/giờ.
- **Exploit**: giảm thời gian dừng máy C (nghỉ trưa luân phiên, chuẩn bị sẵn nguyên liệu) nâng C từ 75 lên 82 sp/giờ => đầu ra hệ thống = min(120; 90; 82; 100; nhu cầu 80) = **80 sp/giờ**. Tăng 5 sp/giờ => $\Delta T = 5 \times 40.000 = 200.000$ VNĐ/giờ $= 200.000 \times 8 \times 26 = 41{,}6$ triệu VNĐ/tháng, chi phí gần như bằng 0.
- **Subordinate**: A chỉ phát liệu 80 sp/giờ (Rope), không chạy 120. Tồn kho bán thành phẩm giảm từ 360 sp/ca về mức buffer đã định.
- **Elevate?** Không cần. Nhu cầu 80 sp/giờ đã được đáp ứng; mua thêm máy C là lãng phí.
- **Repeat**: ràng buộc mới là **thị trường** (nhu cầu 80 sp/giờ); hành động tiếp theo thuộc về bán hàng/marketing chứ không phải sản xuất.

### 2.2. Throughput Accounting (Kế toán Throughput)

**Vấn đề nó giải quyết**: khi có nhiều sản phẩm dùng chung một ràng buộc, nên ưu tiên sản phẩm nào? Cost Accounting trả lời "sản phẩm có biên lợi nhuận gộp/đơn vị cao nhất", nhưng đó là trả lời **sai**, vì nguồn lực khan hiếm không phải là "đơn vị sản phẩm" mà là **thời gian của ràng buộc**.

**Logic**: nếu ràng buộc chỉ có 2.400 phút/tuần, thì mỗi phút là một "tài nguyên khan hiếm" cần được dùng để tạo nhiều Throughput nhất. Do đó đo lường đúng là Throughput **trên mỗi đơn vị ràng buộc** (Throughput per Constraint Unit - T/CU), tương tự như một cửa hàng tính "doanh thu trên mỗi mét vuông kệ" thay vì "lãi trên mỗi món hàng". Khái niệm "Throughput Accounting" thường gắn với Goldratt và các tác giả Galloway & Waldron (cuối thập niên 1980) khi họ hệ thống hoá thành phương pháp kế toán quản trị.

$$T/CU = \frac{\text{Giá bán} - \text{Chi phí NVL trực tiếp (hoàn toàn biến đổi)}}{\text{Thời gian xử lý tại ràng buộc (phút)}}$$

Biến số: Giá bán (VNĐ/sp); Chi phí NVL trực tiếp (VNĐ/sp); Thời gian tại ràng buộc (phút/sp). Đơn vị kết quả: VNĐ/phút ràng buộc.

**Bảng so sánh Cost Accounting vs Throughput Accounting**:

| Tiêu chí | Cost Accounting | Throughput Accounting |
|---|---|---|
| Đơn vị phân tích | Giá thành đơn vị (phân bổ nhân công, chi phí chung) | T, I, OE của cả hệ thống |
| Nhân công trực tiếp | Coi là chi phí biến đổi | Thường là OE (trả lương cố định dù sản lượng đổi) |
| Quyết định product mix | Theo lãi gộp/đơn vị hoặc % lãi gộp | Theo T/CU (VNĐ/phút ràng buộc) |
| Hành vi khuyến khích | Chạy máy tối đa để "chia" chi phí cố định | Chỉ chạy khi tạo T; chấp nhận nhàn rỗi ở công đoạn không phải ràng buộc |
| Tồn kho | Là tài sản (tăng lợi nhuận kế toán khi tồn tăng) | Là gánh nặng (I tăng làm ROI giảm) |

**Ví dụ step-by-step - quyết định product mix** (xem phân tích đầy đủ ở case 3.13). Ba sản phẩm dùng chung máy cắt laser (ràng buộc, 2.400 phút/tuần):

| Sản phẩm | Giá bán (k VNĐ) | NVL (k) | T = giá - NVL (k) | Biên T/giá | Phút laser | T/CU (k/phút) |
|---|---|---|---|---|---|---|
| Bàn sơ chế | 2.000 | 800 | 1.200 | 60% | 45 | 1.200/45 = 26,67 |
| Kệ úp chén | 800 | 360 | 440 | 55% | 10 | 440/10 = 44,0 |
| Chậu rửa | 1.200 | 600 | 600 | 50% | 20 | 600/20 = 30,0 |

Theo Cost Accounting, "Bàn" đứng đầu (T/đơn vị cao nhất 1.200k và % lãi cao nhất 60%). Theo Throughput Accounting, "Bàn" đứng **cuối** (26,67 k/phút). Kệ (T/CU = 44) rồi Chậu (30) rồi Bàn (26,67). Đây chính là nghịch lý mà TOC làm rõ.

### 2.3. Drum-Buffer-Rope (DBR)

**Vấn đề nó giải quyết**: nếu mọi công đoạn tự lập lịch ("đẩy" - Push), công đoạn nhanh sẽ tràn hàng sang công đoạn chậm. DBR là cơ chế **"kéo có kiểm soát"** quanh ràng buộc, đơn giản hơn MRP vì chỉ cần lập lịch chi tiết cho **một** điểm (ràng buộc) rồi cho các công đoạn khác đi theo.

- **Drum (Trống)**: lịch trình của ràng buộc - nhịp trống mà cả hệ thống đi theo. Lịch này quyết định sản phẩm nào, lô nào, vào lúc nào.
- **Buffer (Bộ đệm)**: vùng bảo vệ **bằng thời gian** (không phải bằng tồn kho tuỳ tiện) đặt trước ràng buộc để nó không bao giờ đói việc vì biến động ở công đoạn trước. Có thể có 3 loại: *Constraint Buffer* (trước ràng buộc), *Shipping Buffer* (trước khâu giao hàng, bảo vệ ngày giao cam kết), *Assembly Buffer* (trước điểm lắp ráp gặp các nhánh sản phẩm khi nhánh chứa ràng buộc phải gặp nhánh khác).
- **Rope (Dây thừng)**: tín hiệu phát nguyên liệu vào hệ thống theo đúng nhịp ràng buộc, giữ cho tổng "hàng đang làm dở" (WIP) ổn định.

```
Nguyên liệu vào (Rope điều tiết theo nhịp độ Drum)
        │
        ▼
  [Công đoạn 1] → [Công đoạn 2] → [BUFFER] → [DRUM - Ràng buộc] → [Công đoạn 4] → Thành phẩm
                                     ▲              │
                                     └── nhịp độ hệ thống đồng bộ theo đây ──┘
```

**Cách xác định kích thước buffer**: một cách khởi đầu thông dụng (hướng dẫn tham khảo, không phải quy luật tuyệt đối) là lấy khoảng **50% lead time hiện tại** của đoạn từ lúc phát liệu đến ràng buộc, sau đó điều chỉnh theo dữ liệu Buffer Management (mục 2.4). Lý do: lead time hiện tại bị kéo dài chủ yếu do thời gian hàng nằm chờ, nên có thể rút khoảng một nửa mà vẫn bảo vệ ràng buộc.

**Liên hệ với Định luật Little (Little's Law)**: $WIP = T_h \times LT$, trong đó $T_h$ là tốc độ đầu ra (đơn vị/ngày), $LT$ là lead time (ngày). Nếu giữ $T_h$ cố định (do ràng buộc quyết định) mà giảm WIP thì lead time giảm tương ứng: $LT = WIP / T_h$. Ví dụ ở case 3.2: WIP 160 tấn, đầu ra 12 tấn/ngày => LT chờ = 13,3 ngày; WIP giảm còn 18 tấn => LT chờ 1,5 ngày.

### 2.4. Buffer Management (Quản lý bộ đệm)

**Vấn đề nó giải quyết**: thay vì theo dõi tiến độ từng công đoạn (rối và dễ gây "chữa cháy" không cần thiết), chỉ cần theo dõi **mức tiêu hao buffer** của từng lệnh sản xuất - một chỉ số duy nhất cho biết lệnh nào cần hành động.

TOC chia buffer thành 3 vùng theo đèn giao thông (mỗi vùng khoảng 1/3):

| Vùng | % buffer đã tiêu hao (Buffer Penetration) | Ý nghĩa | Hành động |
|---|---|---|---|
| Xanh | 0% - 33% | An toàn | Không can thiệp |
| Vàng | 33% - 66% | Cảnh báo | Lên kế hoạch xử lý, xác định nguyên nhân |
| Đỏ | 66% - 100% | Nguy hiểm | Hành động khẩn cấp ngay (đẩy nguyên liệu, tăng nhân lực) |

$$\text{Buffer Penetration} = \frac{\text{Thời gian buffer đã tiêu hao}}{\text{Tổng thời gian buffer}} \times 100\%$$

**Ví dụ step-by-step**: buffer của một đơn hàng là 3 ngày. Sau 0,6 ngày đơn chưa đến ràng buộc: 0,6/3 = 20% (Xanh). Với đơn khác tiêu hao 1,5 ngày: 1,5/3 = 50% (Vàng). Đơn thứ ba 2,4 ngày: 2,4/3 = 80% (Đỏ - ưu tiên xử lý ngay). **Giá trị lớn nhất của phương pháp**: dữ liệu tiêu hao buffer tích luỹ sau vài tuần cho biết **nguyên nhân gốc** gây tiêu hao buffer nhiều nhất (thiếu NVL, hỏng máy, thiếu người...) để quản lý ưu tiên cải tiến (Pareto).

### 2.5. Critical Chain Project Management (CCPM)

**Vấn đề nó giải quyết**: dự án thường trễ dù từng người đều ước lượng "an toàn". Lý do là **hành vi**: (1) mỗi người cộng thêm thời gian dự phòng ẩn vào ước lượng của mình; (2) **Student Syndrome**: có dư thời gian nên trì hoãn đến sát hạn mới bắt đầu; (3) **Parkinson's Law**: công việc giãn ra lấp đầy thời gian được cấp; (4) thời gian tiết kiệm ở nhiệm vụ trước bị "lãng phí" vì nhiệm vụ sau không bắt đầu sớm; (5) đa nhiệm (multitasking) làm mọi việc chậm lại.

**Giải pháp của Goldratt (*Critical Chain*, 1997)**: bóc bỏ dự phòng ẩn ở từng nhiệm vụ (ước lượng khoảng 50% khả năng hoàn thành), gom thành một **Project Buffer** chung đặt cuối **chuỗi tới hạn (Critical Chain)** - chuỗi nhiệm vụ dài nhất tính cả ràng buộc về **nguồn lực** (khác CPM ở File 06 chỉ xét ràng buộc trình tự logic). Đồng thời đặt **Feeding Buffer** ở các nhánh phụ nối vào chuỗi tới hạn.

**Ví dụ step-by-step**: chuỗi 5 nhiệm vụ, người thực hiện ước lượng "an toàn" (ngày): 10, 8, 12, 6, 14.

- Tổng ước lượng an toàn: 10 + 8 + 12 + 6 + 14 = **50 ngày**.
- Ước lượng tích cực (cắt 50%): 5 + 4 + 6 + 3 + 7 = **25 ngày**.
- Project Buffer (quy tắc 50% của chuỗi đã cắt): 25 x 50% = **12,5 ngày** => thời hạn dự án = 25 + 12,5 = **37,5 ngày** (ngắn hơn 50 ngày an toàn ban đầu 25%).
- Cách tính chặt chẽ hơn bằng căn bậc hai tổng bình phương (Root Sum of Squares): phần cắt của từng nhiệm vụ là 5, 4, 6, 3, 7 => buffer = $\sqrt{5^2 + 4^2 + 6^2 + 3^2 + 7^2} = \sqrt{135} \approx 11{,}6$ ngày. Lý do: các rủi ro ngẫu nhiên của từng nhiệm vụ không xảy ra cùng lúc nên buffer tổng không cần bằng tổng cộng đơn thuần.
- **Giám sát**: nếu đến một thời điểm đã dùng 7 ngày buffer: 7/12,5 = 56% => vùng Vàng. Không giám sát "mỗi nhiệm vụ có đúng hạn riêng không" mà giám sát mức tiêu hao Project Buffer, tương tự Buffer Management.

### 2.6. Các công cụ tư duy logic (Thinking Processes)

Ba công cụ này (từ *It's Not Luck*, 1994) giải quyết ba câu hỏi: **Thay đổi cái gì? Thay đổi thành cái gì? Thay đổi bằng cách nào?**

#### 2.6.1. Current Reality Tree (CRT - Sơ đồ hiện thực hiện tại)

Truy ngược từ các **hiệu ứng không mong muốn (Undesirable Effects - UDE)** quan sát được (ví dụ: giao hàng trễ, tồn kho cao, nhân viên bận mà vẫn lỗ) theo chuỗi nhân-quả để tìm **nguyên nhân gốc rễ**, thường là một ràng buộc chính sách. Ví dụ: UDE "đơn hàng nhỏ bị trễ" <- "lô sản xuất tối thiểu 500 cái" <- chính sách "chạy lô lớn để giảm chi phí đơn vị" (nguyên nhân gốc).

#### 2.6.2. Evaporating Cloud (Đám mây bốc hơi - Conflict Resolution Diagram)

Giải quyết mâu thuẫn tưởng như không thể (ví dụ: "cần giảm chi phí" mâu thuẫn "cần tăng chất lượng") bằng cách làm lộ **giả định ngầm** sai ở mỗi mũi tên nhân-quả, rồi phá vỡ giả định đó để "đám mây" tan đi. Cấu trúc 5 ô: Mục tiêu chung (A) <- Nhu cầu B và Nhu cầu C <- Hành động D và Hành động D' (mâu thuẫn nhau).

#### 2.6.3. Future Reality Tree (FRT - Sơ đồ hiện thực tương lai)

Kiểm chứng logic giải pháp **trước khi** triển khai: dự đoán hiệu ứng mong muốn (Desirable Effects), và tìm các nhánh tiêu cực (Negative Branches) có thể phát sinh để xử lý trước.

### 2.7. Chỉ số hiệu suất OEE và mối liên hệ với phân tích ràng buộc

**Tại sao OEE?** OEE (Overall Equipment Effectiveness) đo lường hiệu quả thực của thiết bị bằng cách tách thất thoát thành 3 nhóm. Với TOC, OEE chỉ đáng đo **tại ràng buộc** (vì một giờ mất ở ràng buộc là mất của cả hệ thống); đo OEE ở máy không phải ràng buộc chỉ khuyến khích chạy thừa.

$$OEE = A \times P \times Q$$

- $A$ (Availability) = Thời gian chạy thực / Thời gian kế hoạch (trừ dừng máy, chuyển đổi).
- $P$ (Performance) = Sản lượng thực / Sản lượng lý tưởng trong thời gian chạy (trừ chạy chậm).
- $Q$ (Quality) = Số sản phẩm đạt / Tổng sản phẩm làm ra.

**Ví dụ step-by-step**: ca 480 phút, dừng máy 48 phút => chạy thực 432 phút, $A = 432/480 = 90\%$. Tốc độ lý tưởng 1 sp/phút => lý tưởng 432 sp, thực làm 367 sp, $P = 367/432 = 85\%$. Đạt 360 sp, $Q = 360/367 = 98\%$. $OEE = 0{,}90 \times 0{,}85 \times 0{,}98 \approx 75\%$ (tính từ số thực: 360/480 = 75%). **Diễn giải**: 25% công suất lý thuyết của ràng buộc bị mất; ưu tiên là cải thiện P (15% mất) và A (10% mất) - chính là phạm vi của bước Exploit.

### 2.8. Replenishment (Bổ sung hàng) và Dynamic Buffer Management (DBM)

**Vấn đề**: trong chuỗi bán lẻ, dự báo cho từng điểm bán thường sai, dẫn đến vừa hết hàng ở nơi này vừa dư ở nơi khác. Goldratt mở rộng TOC sang chuỗi cung ứng bằng **Replenishment Solution**: giữ buffer tập trung ở kho trung tâm (nơi gộp biến động nên cần ít hàng hơn) và bổ sung cho từng điểm bán **theo mức tiêu thụ thực tế** thay vì theo dự báo.

**Dynamic Buffer Management (DBM)**: kích thước buffer điều chỉnh theo dữ liệu: nếu tồn kho điểm bán liên tiếp rơi vào vùng Đỏ => tăng buffer (khoảng 1/3); nếu liên tục ở vùng Xanh cả một chu kỳ bổ sung => giảm buffer. Với dữ liệu thời gian thực, phần mềm làm tự động; trước đây dựa kinh nghiệm cố định.

### 2.9. Ưu điểm & Nhược điểm của TOC

| Khía cạnh | Ưu điểm | Nhược điểm |
|---|---|---|
| Tốc độ cải tiến | Tập trung nguồn lực vào đúng điểm nghẽn, cải thiện nhanh trong thời gian ngắn | Có thể bỏ qua các vấn đề nhỏ ở bộ phận không phải ràng buộc |
| Chi phí đầu tư | Bước Exploit/Subordinate không cần đầu tư thêm, chi phí thấp | Bước Elevate có thể đòi hỏi đầu tư lớn nếu ràng buộc là vật lý |
| Tính đơn giản | Dễ hiểu, dễ truyền đạt cho toàn bộ nhân viên (qua "The Goal") | Throughput Accounting đòi hỏi thay đổi tư duy kế toán truyền thống |
| Khả năng áp dụng | Áp dụng được cho sản xuất, dự án, chuỗi cung ứng, thậm chí bán hàng | Hiệu quả giảm nếu ràng buộc thay đổi liên tục, khó xác định rõ ràng |
| Văn hoá | Chấm dứt "chạy đua bận rộn" vô nghĩa | Gặp phản đối khi yêu cầu bộ phận "nhàn rỗi có chủ đích" |

### 2.10. So sánh TOC với Lean và Six Sigma

| Tiêu chí | TOC | Lean | Six Sigma |
|---|---|---|---|
| Trọng tâm | Ràng buộc/điểm nghẽn của hệ thống | Loại bỏ lãng phí (Muda) toàn bộ quy trình | Giảm biến động, lỗi (Defects) |
| Cách tiếp cận | Tập trung 100% nguồn lực vào ràng buộc | Cải tiến toàn diện mọi công đoạn | Phân tích thống kê nguyên nhân gốc rễ |
| Tốc độ thấy kết quả | Nhanh (tập trung vào 1 điểm) | Trung bình (cần thay đổi văn hoá rộng) | Chậm hơn (cần thu thập dữ liệu, phân tích sâu) |
| Rủi ro | Bỏ sót vấn đề ở nơi không phải ràng buộc | Có thể tối ưu cục bộ không cần thiết nếu không xác định ràng buộc trước | Có thể tốn thời gian phân tích cho vấn đề không quan trọng |

**Khi nào ưu tiên TOC trước?** Doanh nghiệp nên áp dụng TOC **trước** để chọn đúng điểm cần cải tiến, sau đó dùng Lean (giảm lãng phí) hoặc Six Sigma (giảm biến động) **tại điểm đó**. Cách kết hợp này đôi khi gọi là **TLS (TOC-Lean-Six Sigma)**: TOC trả lời "cải tiến *ở đâu* trước", Lean/Six Sigma trả lời "cải tiến *bằng cách nào*". Ví dụ: ràng buộc là máy in; dùng Lean (SMED) giảm thời gian chuyển đổi và Six Sigma giảm tỷ lệ in lỗi - đúng tại máy in thay vì rải khắp xưởng.

---


## III. Case Studies thực tế

> Các case dưới đây dùng số liệu **giả định minh họa** (xem lưu ý đầu file) để người đọc thực hành từng bước tính toán. Tên doanh nghiệp Việt Nam là tên hư cấu trừ khi ghi khác.

### 3.1. Case quốc tế: Ford Motor - dây chuyền lắp ráp và máy sơn (minh họa)

#### Bối cảnh

Ví dụ này dựa trên một kiểu tình huống thường được thảo luận khi giảng dạy TOC trong ngành ô tô: nhà máy lắp ráp liên tục đầu tư thêm máy ở nhiều công đoạn nhưng sản lượng ra cuối dây chuyền không tăng. *Con số bên dưới là minh họa, không phải số liệu công bố của Ford.* Dây chuyền 5 công đoạn, nhu cầu 50 xe/giờ:

| Công đoạn | Dập | Hàn | **Sơn** | Lắp ráp | Kiểm tra |
|---|---|---|---|---|---|
| Năng lực (xe/giờ) | 70 | 60 | **42** | 55 | 65 |

#### Phân tích từng bước

1. **Identify**: đầu ra hệ thống = min(70, 60, 42, 55, 65) = **42 xe/giờ** < nhu cầu 50 => sơn là ràng buộc. Ban quản lý ban đầu nghi ngờ khâu hàn/lắp ráp (nơi nhìn thấy "bận rộn" nhất), nhưng dữ liệu cho thấy hàng chờ nằm **trước máy sơn**.
2. **Chi phí của tối ưu cục bộ**: nếu dập chạy 70, hàn chạy 60 mà sơn chỉ 42: tồn đọng trước hàn = 70 - 60 = 10 xe/giờ, trước sơn = 60 - 42 = 18 xe/giờ; mỗi ca 8 giờ tích luỹ (10 + 18) x 8 = **224 xe dở dang**. Với giả định mỗi xe dở dang chiếm 2.500 USD vốn, tồn kho tăng thêm 224 x 2.500 = **560.000 USD/ca** mà đầu ra không tăng.
3. **Exploit**: giảm thời gian đổi màu và dừng máy sơn, nâng sơn từ 42 lên 46 xe/giờ (+4 xe/giờ). Với T giả định 4.000 USD/xe: $\Delta T = 4 \times 8 \times 4.000 = 128.000$ USD/ca, không cần mua thêm máy.
4. **Subordinate - DBR**: Drum = máy sơn (46 xe/giờ). Rope: phát thân xe vào dây chuyền với tốc độ 46 xe/giờ thay vì 70. Buffer: 2 giờ trước máy sơn = 2 x 46 = **92 xe** thay vì tăng vô hạn 224 xe/ca. Dập và hàn "nhàn rỗi" theo kế hoạch: tỷ lệ sử dụng dập = 46/70 = 65,7%, hàn = 46/60 = 76,7%.
5. **Repeat**: sơn đã 46, nhu cầu 50 => vẫn thiếu 4 xe/giờ, hàn (60) và lắp ráp (55) chưa phải ràng buộc, nên nếu còn nhu cầu mới cân nhắc **Elevate** (thêm ca sơn, thêm buồng sơn). Ràng buộc kế tiếp có thể là lắp ráp (55).

#### Ý nghĩa kinh doanh và bài học

- Cải thiện đầu ra đến từ **đúng một điểm**; các khoản đầu tư rải rác ở hàn/lắp ráp trước đó không làm tăng xe ra khỏi nhà máy.
- DBR biến "224 xe dở dang tăng mỗi ca" thành "92 xe cố định" - giải phóng vốn và rút ngắn lead time.
- Bài học: luôn tìm **nơi hàng chờ tích tụ** trước khi duyệt ngân sách đầu tư.

### 3.2. Case Việt Nam lớn: Nhà máy dệt may - ràng buộc ở công đoạn nhuộm (minh họa, không nêu tên doanh nghiệp)

#### Bối cảnh

Nhà máy dệt-nhuộm-may quy mô lớn, công đoạn nhuộm vải là điểm nghẽn, dệt và may dư năng lực. *Số liệu là giả định minh họa*:

| Công đoạn | Dệt | **Nhuộm** | May |
|---|---|---|---|
| Năng lực (tấn vải/ngày) | 20 | **12** | 16 |

Dệt vẫn chạy 20 tấn/ngày vì chỉ tiêu "hiệu suất máy dệt 95%" gắn với thưởng quản đốc.

#### Phân tích từng bước

1. **Identify**: đầu ra hệ thống = min(20, 12, 16) = **12 tấn/ngày**; ràng buộc là nhuộm.
2. **Tồn kho chờ nhuộm khi dệt chạy hết công suất**: mỗi ngày tích luỹ 20 - 12 = 8 tấn. Sau 20 ngày làm việc: 8 x 20 = **160 tấn vải mộc** chờ nhuộm.
3. **Lead time chờ** (Định luật Little, mục 2.3): $LT = WIP / T_h = 160 / 12 \approx 13{,}3$ ngày - đơn hàng nằm chờ hơn 2 tuần trước khi vào nhuộm.
4. **Subordinate - DBR**: Drum = nhuộm (12 tấn/ngày). Rope: dệt chỉ phát đúng 12 tấn/ngày. Buffer: 1,5 ngày công việc trước nhuộm = 1,5 x 12 = **18 tấn**. Lead time chờ còn 18/12 = **1,5 ngày**.
5. **Hiệu quả tài chính** (giả định giá trị vải mộc 60 triệu VNĐ/tấn, lãi vay 11%/năm):
   - WIP giảm: 160 - 18 = 142 tấn => giải phóng vốn 142 x 60 = **8.520 triệu VNĐ (~8,5 tỷ)**.
   - Tiết kiệm lãi vay: 8.520 x 11% = **~937 triệu VNĐ/năm**.
   - Thêm lợi ích chưa định lượng: giảm điện/nhân công tăng ca ở dệt, giảm vải mộc hư hỏng khi tồn lâu.
6. **Elevate/Repeat**: nếu nhu cầu > 12 tấn/ngày, mới đánh giá mở thêm ca nhuộm hoặc thuê nhuộm ngoài; ràng buộc tiếp theo sẽ là may (16 tấn/ngày).

#### Bài học

Dệt "cố ý chạy chậm" xuống 12 tấn/ngày làm **chỉ số hiệu suất cục bộ của dệt giảm** nhưng **tiền của cả doanh nghiệp tăng**. Bài học quản trị: phải đổi chỉ tiêu thưởng của quản đốc dệt từ "hiệu suất máy" sang "giao đủ đúng nhịp cho nhuộm".

### 3.3. Case SME Việt Nam: Xưởng in ấn tại TP.HCM - Exploit máy in offset cũ (giả định minh họa)

#### Bối cảnh

Xưởng in nhỏ có 1 máy in offset đời cũ là ràng buộc; các công đoạn cắt, gia công sau in đều dư năng lực. Máy làm việc 480 phút/ca, 22 ngày/tháng, trung bình 8 đơn/ngày. Chi phí vận hành (OE) cố định 340 triệu VNĐ/tháng. Throughput giả định **60.000 VNĐ mỗi phút máy in thực sự chạy** (T/CU).

Chủ xưởng đang nghĩ đến mua máy in mới (hàng tỷ đồng) - vượt khả năng tài chính.

#### Phân tích từng bước

1. **Xem máy in dùng thời gian vào việc gì** (đo 2 tuần):

| Hạng mục (phút/ngày) | Trước | Sau Exploit |
|---|---|---|
| Chuyển đổi khuôn/giấy/mực (8 đơn) | 8 x 20 = 160 | 8 x 12 = 96 |
| Chờ vật tư, chờ duyệt mẫu | 20 | 15 |
| **Thời gian in thực** | 480 - 160 - 20 = **300** | 480 - 96 - 15 = **369** |

2. **Các hành động Exploit**: gộp đơn cùng loại giấy/mực để giảm số lần đổi; chuẩn bị khuôn/giấy sẵn trong lúc máy đang chạy đơn trước (chuyển thao tác "ngoại" ra ngoài thời gian máy dừng - tinh thần SMED); duyệt mẫu trước khi tới giờ in; nghỉ trưa luân phiên.
3. **Tăng năng lực thực**: $369/300 - 1 = 23\%$ (tăng khoảng 23%, nằm trong khoảng 20-25%).
4. **Tính tác động tài chính**:
   - T trước: $300 \times 60.000 \times 22 = 396$ triệu VNĐ/tháng.
   - T sau: $369 \times 60.000 \times 22 = 487{,}08$ triệu VNĐ/tháng (+91,08 triệu).
   - NP trước = 396 - 340 = **56 triệu**; NP sau = 487,08 - 340 = **147,08 triệu** (tăng khoảng 163%).
5. **Vì sao lợi nhuận tăng gần 163% khi T chỉ tăng 23%?** Vì OE gần như cố định (lương, thuê xưởng không đổi); phần T tăng thêm chảy gần như toàn bộ xuống lợi nhuận (điều kiện: có đủ đơn hàng).
6. **Subordinate**: công đoạn cắt/gia công sau in chỉ nhận việc theo nhịp ra của máy in; không ép chạy trước.

#### Bài học

- 91 triệu VNĐ/tháng thêm T mà **chi phí đầu tư gần 0**: chỉ cần số liệu quan sát và sắp lịch.
- Chỉ sau khi Exploit đã hết dư địa (thời gian chuyển đổi, chờ vật tư không còn giảm được) và đơn hàng vẫn dư thì mới tính Elevate (máy mới/ca 2).

### 3.4. Case thất bại: Doanh nghiệp đồ gỗ đầu tư CNC khi chưa xác định đúng ràng buộc (giả định minh họa)

#### Bối cảnh

Nhà máy đồ gỗ nội thất có sản lượng thấp; ban lãnh đạo thấy "cắt gỗ" là khâu "cũ nhất" nên mua dây chuyền CNC mới 3,2 tỷ VNĐ mà không đo năng lực từng công đoạn.

| Công đoạn (bộ/ngày) | Cắt | Lắp ráp | **Sơn - hoàn thiện** | Đóng gói |
|---|---|---|---|---|
| Năng lực trước đầu tư | 120 | 150 | **90** | 140 |

Giả định: T = 1,2 triệu VNĐ/bộ; 26 ngày/tháng; OE hiện tại 2.100 triệu/tháng; Inventory 12.000 triệu; nhu cầu thị trường >= 120 bộ/ngày.

#### Phân tích từng bước

1. **Tình trạng trước đầu tư**: đầu ra = min(120, 150, 90, 140) = **90 bộ/ngày**; $T = 90 \times 1{,}2 \times 26 = 2.808$ triệu/tháng; $NP = 2.808 - 2.100 = 708$ triệu; $ROI = 708/12.000 = 5{,}9\%$/tháng.
2. **Sau khi lắp CNC** (năng lực cắt 120 -> 200): đầu ra = min(200, 150, 90, 140) = **90 bộ/ngày** (không đổi). $\Delta T = 0$.
3. **Chi phí phát sinh**: khấu hao 5 năm = 3.200/60 = 53,3 triệu/tháng + bảo trì/điện 10 triệu => OE mới = 2.100 + 53,3 + 10 = **2.163,3 triệu**. $NP = 2.808 - 2.163{,}3 = 644{,}7$ triệu (giảm 63,3 triệu). Inventory = 12.000 + 3.200 = 15.200 => $ROI = 644{,}7/15.200 = 4{,}24\%$ (giảm từ 5,9%).
4. **Tác động ngầm**: nếu không có Rope, bộ phận cắt "nhàn rỗi" sẽ cắt nhiều hơn 110 bộ/ngày so với sơn (200 - 90) => tồn kho bán thành phẩm chờ sơn phình to.
5. **Phương án đúng (nếu đã xác định ràng buộc)**: đầu tư buồng sơn thứ hai 900 triệu, năng lực sơn 90 -> 130 bộ/ngày. Đầu ra mới = min(120, 150, 130, 140) = **120 bộ/ngày** (ràng buộc dịch sang khâu cắt). $T = 120 \times 1{,}2 \times 26 = 3.744$ triệu (+936 triệu). OE tăng = khấu hao 900/60 = 15 + vận hành 40 = 55 triệu. $NP = 3.744 - 2.155 = 1.589$ triệu (tăng 881 triệu so với ban đầu). **Thời gian hoàn vốn** $= 900/881 \approx 1{,}02$ tháng (giả định nhu cầu >= 120 bộ/ngày và đủ nguyên liệu).

| Chỉ tiêu | Hiện trạng | Đầu tư CNC (sai chỗ) | Đầu tư buồng sơn (đúng chỗ) |
|---|---|---|---|
| Đầu ra (bộ/ngày) | 90 | 90 | 120 |
| Throughput (triệu/tháng) | 2.808 | 2.808 | 3.744 |
| OE (triệu/tháng) | 2.100 | 2.163,3 | 2.155 |
| Lợi nhuận NP (triệu/tháng) | 708 | 644,7 | 1.589 |

#### Bài học

- Ba lỗi: quyết định theo cảm tính ("máy cũ nhất"), không đo năng lực từng công đoạn, nhảy thẳng vào Elevate.
- Quy trình đúng: vẽ dòng chảy -> đo năng lực thực -> quan sát nơi hàng chờ tích tụ -> chỉ duyệt đầu tư cho ràng buộc, kèm tính $\Delta T$ và hoàn vốn.
- Kết quả sau khi sửa: ràng buộc dịch chuyển sang khâu cắt - đúng nguyên lý Repeat; lúc đó CNC (nếu có) mới có ý nghĩa.

### 3.5. Case SME dịch vụ: Phòng khám đa khoa - ràng buộc ở máy xét nghiệm (giả định minh họa)

#### Bối cảnh

Phòng khám có nhiều bác sĩ, thời gian chờ của bệnh nhân rất dài dù bác sĩ rảnh. Chỉ có 1 máy xét nghiệm, 6 phút/mẫu => năng lực **10 mẫu/giờ**, 8 giờ/ngày = 80 mẫu/ngày. Dòng bệnh nhân cần xét nghiệm: giờ cao điểm 3 giờ đầu ca (bác sĩ cùng khám buổi sáng) 16 mẫu/giờ; 5 giờ còn lại 6 mẫu/giờ. Tổng 3 x 16 + 5 x 6 = **78 mẫu/ngày** (< 80 năng lực).

#### Phân tích từng bước

1. **Identify**: tổng năng lực (80) đủ tổng nhu cầu (78) nhưng **phân bố theo giờ** làm máy xét nghiệm quá tải cục bộ: cao điểm đến 16 mẫu/giờ so với 10 mẫu/giờ.
2. **Hàng chờ tích luỹ giờ cao điểm**: (16 - 10) x 3 = **18 mẫu** tồn đọng cuối giờ cao điểm. Bệnh nhân đến cuối giờ cao điểm chờ 18/10 = 1,8 giờ = **108 phút**. Mô hình dòng chảy cho thời gian chờ trung bình của bệnh nhân đến trong giờ cao điểm khoảng **52 phút** (tăng tuyến tính từ 0 lên 108 phút).
3. **Subordinate**: xếp lịch khám/hẹn để dòng bệnh nhân gửi xét nghiệm đều đặn 78/8 = **9,75 mẫu/giờ** (< 10). Bác sĩ có thể nhàn rỗi một phần; khám theo lịch hẹn khung giờ, đẩy bệnh nhân không cần xét nghiệm gấp vào giờ cao điểm.
4. **Kết quả**: theo mô hình dòng chảy hàng chờ ≈ 0; trong thực tế còn biến động ngẫu nhiên nên đặt buffer nhỏ (ví dụ 3 mẫu ≈ 18 phút) - giảm thời gian chờ trung bình từ **~52 phút xuống dưới ~10-18 phút** mà không mua thêm máy.
5. **Exploit thêm**: chuẩn bị ống/nhãn trước, ưu tiên mẫu cấp cứu, dùng thời gian nhàn rỗi của máy để xử lý loạt mẫu theo lô.
6. **Elevate** (nếu bệnh nhân tăng): mua thêm máy; lúc đó tính $\Delta T$ từ số bệnh nhân bổ sung.

#### Bài học

Ràng buộc trong dịch vụ thường không nằm ở **tổng** năng lực mà ở **phân bố thời gian** của tải. Điều chỉnh lịch (miễn phí) là giải pháp đầu tiên.

### 3.6. Case quốc tế: Boeing - CCPM trong quản trị dự án (minh họa)

#### Bối cảnh

CCPM được các tổ chức hàng không-vũ trụ và phát triển sản phẩm phức tạp thảo luận như cách giải quyết tình trạng dự án luôn trễ (không có số liệu công bố chính thức được kiểm chứng trong tài liệu này). Ví dụ minh họa: chuỗi tới hạn gồm 4 nhiệm vụ, ước lượng an toàn của người thực hiện (ngày): 20, 16, 24, 12.

#### Phân tích từng bước

1. **Ước lượng an toàn truyền thống**: 20 + 16 + 24 + 12 = **72 ngày**.
2. **Cắt ước lượng ở mức 50%**: 10 + 8 + 12 + 6 = **36 ngày** (phần cắt: 10, 8, 12, 6).
3. **Project Buffer**: quy tắc 50% => 36 x 50% = **18 ngày**; (cách RSS: $\sqrt{10^2+8^2+12^2+6^2} = \sqrt{344} \approx 18{,}5$ ngày - gần như trùng).
4. **Lịch dự án mới**: 36 + 18 = **54 ngày**, rút ngắn $(72-54)/72 = 25\%$.
5. **Giám sát**: sau 3 nhiệm vụ đầu (kế hoạch 10 + 8 + 12 = 30 ngày) thực tế dùng 38 ngày => buffer tiêu hao 8/18 = **44% (Vàng)**: bắt đầu lập kế hoạch xử lý; nếu 12/18 = 67% (Đỏ) phải hành động ngay.
6. **Giải quyết hành vi**: không còn mốc hạn cứng cho từng nhiệm vụ => giảm Student Syndrome; "báo cáo sớm, bàn giao ngay" (kiểu chạy tiếp sức - relay race) => nhiệm vụ nào xong sớm thì người kế tiếp bắt đầu ngay, không lãng phí thời gian tiết kiệm; giảm đa nhiệm vì tập trung hoàn thành từng việc.

#### Bài học

Dự án nên được quản trị bằng **mức tiêu hao buffer chung**, không phải bằng việc ép từng nhiệm vụ đúng hạn riêng. Rủi ro: nếu văn hoá vẫn phạt người "báo trễ" thì họ lại giấu dự phòng như cũ.

### 3.7. Case Việt Nam: Chuỗi nhà hàng ở Hà Nội - bếp trưởng là ràng buộc (giả định minh họa)

#### Bối cảnh

Chuỗi 3 chi nhánh, giờ cao điểm 11:00-13:30 (150 phút) khách chờ món lâu dù đủ bàn và phục vụ. Món đặc biệt (giá bán 185.000 VNĐ, NVL 78.000 VNĐ => **T = 107.000 VNĐ/món**) chỉ do bếp trưởng hoàn thiện. Nhu cầu món đặc biệt trong cao điểm: 55 món/chi nhánh/ngày.

#### Phân tích từng bước

1. **Identify**: mỗi món chiếm bếp trưởng 4 phút (sơ chế 1,5 + nêm nấu 1,5 + trình bày 1) => năng lực = 150/4 = **37,5 món**/cao điểm < nhu cầu 55. Phần chờ chính nằm ở "phiếu món đặc biệt" trước bếp trưởng.
2. **Exploit**: chuyển sơ chế (1,5 phút) sang phụ bếp làm sẵn trước giờ cao điểm; chuyển trình bày (1 phút) cho người khác theo chuẩn mẫu => bếp trưởng còn 2,5 phút/món. Năng lực mới = 150/2,5 = **60 món** (> nhu cầu 55).
3. **Đầu ra thực** = min(60; nhu cầu 55) = 55 món. $\Delta T$ mỗi ngày = (55 - 37,5) x 107.000 = 17,5 x 107.000 = **1.872.500 VNĐ/ngày**; x 30 ngày = **56,175 triệu VNĐ/tháng**/chi nhánh.
4. **Chi phí**: thêm 1 phụ bếp 8 triệu/tháng. Ròng = 56,175 - 8 = **48,175 triệu/tháng**/chi nhánh; cả 3 chi nhánh ≈ **144,5 triệu/tháng**.
5. **Subordinate**: phục vụ không "đẩy" quá nhiều phiếu món đặc biệt vào bếp; nhập phiếu theo nhịp, khuyến nghị món khác khi bếp trưởng gần đầy.
6. **Elevate** (chưa cần): không thuê bếp trưởng thứ hai.
7. **Repeat**: ràng buộc chuyển sang **thị trường** (nhu cầu 55 món) hoặc khu vực khác (số bàn).

#### Bài học

Với ràng buộc là **người có kỹ năng hiếm**, Exploit nghĩa là dồn việc không cần kỹ năng đó ra khỏi tay họ. Chi phí hiệu quả hơn nhiều so với tuyển bếp trưởng thứ hai.

### 3.8. Case quốc tế: Trung tâm hoàn tất đơn hàng kiểu Amazon - trạm đóng gói (minh họa)

#### Bối cảnh

Trong mùa cao điểm, trạm đóng gói thành ràng buộc của một trung tâm hoàn tất đơn hàng quy mô lớn. *Số liệu là minh họa, không phải số liệu công bố của Amazon.* Năng lực (đơn/giờ): lấy hàng (picking) 1.200, phân loại (sorting) 1.100, **đóng gói 800** (16 trạm x 50 đơn/giờ), nhu cầu 1.000 đơn/giờ.

#### Phân tích từng bước

1. **Identify**: đầu ra = min(1.200; 1.100; 800) = 800 đơn/giờ < nhu cầu 1.000 => đóng gói là ràng buộc. Thiếu 200 đơn/giờ.
2. **Exploit**: chuẩn hoá kích thước hộp, in sẵn nhãn tự động => mỗi trạm từ 50 lên 58 đơn/giờ. Năng lực = 16 x 58 = **928 đơn/giờ** (+16%).
3. **Subordinate**: nếu picking vẫn chạy 1.200, hàng tích trước trạm đóng gói 1.200 - 928 = 272 đơn/giờ => ca 10 giờ tồn 2.720 đơn dở dang. Áp dụng Rope: phát lệnh lấy hàng đúng 928 đơn/giờ; giữ buffer đơn đã sẵn sàng ở mức ~1 giờ.
4. **Còn thiếu**: nhu cầu 1.000 - 928 = 72 đơn/giờ => mới xét **Elevate** (thêm trạm: cần 72/58 ≈ 1,24 => thêm 2 trạm lên 18 trạm x 58 = 1.044 > 1.000).
5. Sau Elevate: ràng buộc mới có thể là sorting (1.100) hoặc nhu cầu; Repeat.

#### Bài học

Mùa cao điểm thể hiện rõ giá trị **Subordinate**: không "chạy nhanh" khâu lấy hàng mà kết quả là đống hàng chờ đóng gói.

### 3.9. Case Việt Nam: Doanh nghiệp bao bì carton ở Bình Dương - ràng buộc thị trường (giả định minh họa)

#### Bối cảnh

Nhà máy sản xuất carton, công suất 1.500 nghìn m²/tháng nhưng chỉ bán 960 nghìn m² (sử dụng 64%). Giá bán 9.000 VNĐ/m², NVL 6.300 VNĐ/m² => T = **2.700 VNĐ/m²**. OE 2.200 triệu/tháng. Chủ doanh nghiệp định mua máy sóng mới 4,5 tỷ để "tăng năng lực".

#### Phân tích từng bước

1. **Identify**: sản xuất chỉ dùng 64% => công suất không phải ràng buộc. Ràng buộc là **khả năng bán hàng** (đội sales mỏng).
2. **Hiện trạng**: $T = 960.000 \times 2.700 = 2.592$ triệu/tháng; $NP = 2.592 - 2.200 = 392$ triệu.
3. **Phương án A - mua máy mới 4,5 tỷ**: $\Delta T = 0$ (không có thêm đơn), OE tăng khấu hao - **lãng phí**.
4. **Phương án B - đầu tư vào bán hàng** (giả định): tuyển 3 sales (15 triệu/tháng/người) + đào tạo/công cụ 10 triệu/tháng => OE tăng 55 triệu/tháng. Mỗi sales mới đưa thêm 90 nghìn m²/tháng => thêm 270 nghìn m²; để mở thị phần, giảm giá 2% cho khối lượng mới: giá mới 9.000 x 0,98 = 8.820 => T mới/m² = 8.820 - 6.300 = **2.520 VNĐ**.
5. **Tính kết quả B**: $\Delta T = 270.000 \times 2.520 = 680{,}4$ triệu/tháng; $\Delta NP = 680{,}4 - 55 = 625{,}4$ triệu; NP mới = 392 + 625,4 = **1.017,4 triệu/tháng** (gấp ~2,6 lần). Sản lượng 960 + 270 = 1.230 nghìn m² => sử dụng công suất 82%.
6. **Repeat**: khi công suất sử dụng tiến gần 100% (~1.500), ràng buộc quay lại vật lý => lúc đó mới xét Elevate.

#### Bài học

Phân biệt ràng buộc thị trường và ràng buộc vật lý. Ràng buộc thị trường khó nhận ra vì nó nằm **ngoài** nhà máy và thường bị che bởi nhận định "mình chưa đủ máy".

### 3.10. Case Việt Nam: Công ty logistics - ràng buộc ở bốc xếp tại kho (giả định minh họa)

#### Bối cảnh

Kho trung tâm có 3 bến bốc xếp (dock), mỗi bến làm việc 13 giờ = 780 phút/ngày. Mỗi lượt xe chiếm bến 60 phút (bốc 45 + chờ/đổi xe 15). Đội xe đủ cho 50 chuyến/ngày. Cước 3,1 triệu/chuyến, chi phí biến đổi (nhiên liệu, phí cầu đường) 0,7 triệu => **T = 2,4 triệu VNĐ/chuyến**.

#### Phân tích từng bước

1. **Identify**: năng lực bến = 3 x 780/60 = **39 chuyến/ngày** < năng lực đội xe 50 => bến bốc xếp là ràng buộc (không phải số xe).
2. **Exploit**: đặt lịch hẹn từng xe, bốc theo tuyến ưu tiên, chuẩn bị sẵn pallet trong lúc xe trước đang bốc => thời gian chiếm bến giảm từ 60 xuống 52 phút.
3. **Năng lực mới** = 3 x 780/52 = **45 chuyến/ngày** (+6 chuyến, +15,4%).
4. **Tác động**: $\Delta T = 6 \times 2{,}4 \times 26 = 374{,}4$ triệu/tháng, không mua thêm xe hay thuê thêm người bốc.
5. **Repeat**: 45 gần với năng lực đội xe 50 => ràng buộc kế tiếp có thể là đội xe; cân nhắc Elevate lúc đó.

#### Bài học

Nếu mua thêm xe ở trạng thái ban đầu, chi phí tăng mà số chuyến vẫn bị chặn ở 39 vì cổng kho.

### 3.11. Case Việt Nam: Nhà máy linh kiện điện tử Bắc Ninh - ràng buộc ở QC cuối dây chuyền (giả định minh họa)

#### Bối cảnh

Công đoạn kiểm tra chất lượng (QC) cuối dây chuyền là ràng buộc vì thiếu nhân viên QC được đào tạo. 6 người, kiểm 100% mọi sản phẩm, 90 giây/sản phẩm; lắp ráp phía trước dư năng lực (320 sp/giờ).

#### Phân tích từng bước

1. **Năng lực QC trước**: mỗi người 3.600/90 = 40 sp/giờ; 6 người = **240 sp/giờ** (ràng buộc, thấp hơn lắp ráp 320).
2. **Exploit 1 - kiểm theo rủi ro**: phân loại lỗi; 80% sản phẩm thuộc nhóm lỗi nghiêm trọng kiểm 100% (90 giây), 20% thuộc nhóm lỗi nhẹ lấy mẫu 50% (trung bình 45 giây). Thời gian bình quân = 0,8 x 90 + 0,2 x 45 = 72 + 9 = **81 giây/sản phẩm**.
3. **Exploit 2 - đào tạo chéo**: 2 nhân viên lắp ráp (dư năng lực) hỗ trợ QC 4/8 giờ cao điểm => nhân lực bình quân = 6 + 2 x (4/8) = **7 người**.
4. **Năng lực mới** = 7 x 3.600/81 = **311,1 sp/giờ**. Tăng $311{,}1/240 - 1 = 29{,}6\%$ (khoảng 30%).
5. **Subordinate/Repeat**: 311 gần với lắp ráp 320 => ràng buộc sắp chuyển về lắp ráp; cần kế hoạch tuyển dụng dài hạn khi nhu cầu tăng thêm.

#### Bài học và lưu ý rủi ro

Giảm kiểm tra nhẹ cần dữ liệu tỷ lệ lỗi và thoả thuận với khách hàng; nếu chất lượng giảm, chi phí hàng trả về sẽ vượt phần lợi (xem File 02 - Quản trị chất lượng).

### 3.12. Case Việt Nam: Chuỗi cửa hàng tiện lợi - Replenishment (giả định minh họa)

#### Bối cảnh

Chuỗi 40 cửa hàng gặp tình trạng vừa hết hàng ở cửa hàng này vừa dư ở cửa hàng khác với cùng một mặt hàng. Hiện tại: tỷ lệ hết hàng 8,5%, tồn kho trung bình 14 ngày bán. Doanh thu 20 triệu/cửa hàng/ngày (tổng 800 triệu/ngày), giá vốn 15 triệu/cửa hàng/ngày (tổng 600 triệu/ngày), T ≈ 25% doanh thu.

#### Phân tích từng bước

1. **Thiết lập buffer cho một mặt hàng** (nước suối 500ml): tiêu thụ trung bình 18 chai/ngày/cửa hàng, thời gian bổ sung từ kho trung tâm 1 ngày. Buffer ban đầu = 18 x 1 x hệ số an toàn 2 = **36 chai**.
2. **Chia vùng**: Xanh >= 24 chai (2/3 buffer), Vàng 12-24, Đỏ < 12 chai.
3. **Bổ sung theo tiêu thụ thực tế**: mỗi ngày gửi lượng đúng bằng đã bán hôm trước để đưa tồn về mức 36 (thay vì đặt theo dự báo).
4. **Dynamic Buffer Management**: nhu cầu tăng lên 27 chai/ngày làm cửa hàng 2 chu kỳ liên tiếp rơi vào vùng Đỏ => tăng buffer khoảng 1/3: 36 x 4/3 = **48 chai** (phù hợp mức cần ~ 27 x 1 x 2 = 54). Ngược lại, nếu cả chu kỳ ở vùng Xanh thì giảm buffer.
5. **Kết quả sau 6 tháng** (giả định): hết hàng giảm 8,5% -> 3,2%; tồn kho từ 14 ngày xuống 9 ngày bán.
6. **Tính giá trị**:
   - Giảm tồn kho: giá vốn 600 triệu/ngày x (14 - 9) = **3.000 triệu (3 tỷ)** vốn được giải phóng; lãi vay 11% => tiết kiệm **330 triệu/năm**.
   - Doanh thu thu hồi (giả định 40% cầu hết hàng bị mất hẳn): (8,5% - 3,2%) x 40% = 2,12% doanh thu => 800 x 2,12% = 16,96 triệu/ngày; T ≈ 25% => ~4,24 triệu/ngày ≈ **1.548 triệu/năm**.

#### Bài học

Nguyên lý TOC trong chuỗi cung ứng: gom buffer ở nơi biến động nhỏ hơn (kho trung tâm), bổ sung theo tiêu thụ thực, điều chỉnh buffer bằng dữ liệu thay vì đoán.

### 3.13. Case SME Việt Nam mới: Xưởng inox "Thành Phát" (Biên Hòa) - tối ưu product mix quanh máy laser (giả định minh họa)

> Case SME bổ sung áp dụng đầy đủ Throughput Accounting, T/CU, 5 bước, DBR và Elevate. Tên doanh nghiệp và số liệu hoàn toàn hư cấu.

#### Bối cảnh

Xưởng gia công inox 45 nhân sự, sản xuất 3 sản phẩm: **Kệ úp chén**, **Chậu rửa 2 hố**, **Bàn sơ chế bếp công nghiệp**. Chủ xưởng thường xuyên tăng ca, đơn hàng trễ, nhưng lợi nhuận thấp. Ông ưu tiên làm "Bàn sơ chế" vì "lãi gộp cao nhất" (60%).

Máy cắt laser duy nhất là công đoạn ai cũng phải qua. Năng lực mỗi tuần (phút): **laser 2.400** (1 máy x 40 giờ), chấn gấp 2.400, hàn 4.800, đánh bóng 9.600. OE xưởng **55.000 nghìn VNĐ/tuần (55 triệu)**.

| Sản phẩm | Giá bán (k) | NVL (k) | Laser (phút) | Chấn (phút) | Hàn (phút) | Đánh bóng (phút) | Nhu cầu tối đa/tuần |
|---|---|---|---|---|---|---|---|
| Kệ úp chén | 800 | 360 | 10 | 5 | 8 | 15 | 100 |
| Chậu rửa | 1.200 | 600 | 20 | 10 | 15 | 30 | 80 |
| Bàn sơ chế | 2.000 | 800 | 45 | 15 | 20 | 40 | 60 |

#### Phân tích từng bước

1. **Identify - nạp tải nếu làm đủ nhu cầu**:
   - Laser: 100 x 10 + 80 x 20 + 60 x 45 = 1.000 + 1.600 + 2.700 = **5.300 phút** / 2.400 = **220,8%** (ràng buộc).
   - Chấn: 500 + 800 + 900 = 2.200 / 2.400 = 91,7% (gần ngưỡng, cần theo dõi).
   - Hàn: 800 + 1.200 + 1.200 = 3.200 / 4.800 = 66,7%.
   - Đánh bóng: 1.500 + 2.400 + 2.400 = 6.300 / 9.600 = 65,6%.
   => Laser chiếm tới hơn 2 lần năng lực: không thể làm hết đơn; phải chọn sản phẩm.
2. **Tính T và T/CU** (T = giá - NVL):
   - Kệ: 800 - 360 = 440k; T/CU = 440/10 = **44,0 k/phút**.
   - Chậu: 1.200 - 600 = 600k; T/CU = 600/20 = **30,0 k/phút**.
   - Bàn: 2.000 - 800 = 1.200k; T/CU = 1.200/45 = **26,67 k/phút**.
3. **Phương án truyền thống (theo lãi gộp lớn nhất)** - ưu tiên Bàn, rồi Kệ, rồi Chậu: Bàn 53 chiếc x 45 = 2.385 phút; còn 15 phút => 1 Kệ (10 phút). $T = 53 \times 1.200 + 1 \times 440 = 64.040$ k (≈ **64,04 triệu**/tuần). $NP = 64{,}04 - 55 = 9{,}04$ triệu/tuần.
4. **Phương án TOC (theo T/CU giảm dần)** - ưu tiên Kệ -> Chậu -> Bàn:
   - Kệ: làm hết nhu cầu 100 chiếc x 10 = 1.000 phút; còn 1.400 phút.
   - Chậu: 1.400/20 = 70 chiếc (nhu cầu 80, làm 70) = 1.400 phút; còn 0.
   - Bàn: 0 chiếc.
   - $T = 100 \times 440 + 70 \times 600 = 44.000 + 42.000 = 86.000$ k (**86 triệu**/tuần). $NP = 86 - 55 = 31$ triệu/tuần.
5. **So sánh**: TOC cho T cao hơn 86,0 - 64,04 = **21,96 triệu/tuần**; NP gấp 31/9,04 ≈ **3,4 lần**; mỗi tháng (4 tuần) NP = 124 triệu so với ~36,2 triệu.
6. **Kiểm tra "Subordinate" - công đoạn khác có chịu nổi mix TOC không?** Tải mix (100 Kệ, 70 Chậu): Laser 1.000 + 1.400 = 2.400 (100%); Chấn 500 + 700 = 1.200 (50%); Hàn 800 + 1.050 = 1.850 (38,5%); Đánh bóng 1.500 + 2.100 = 3.600 (37,5%). Hàn và đánh bóng nhàn rỗi nhiều => đúng với dự kiến "nhàn rỗi có chủ đích"; không ép họ chạy thêm.
7. **DBR - lịch Drum**: laser chạy theo kế hoạch tuần: ưu tiên 100 Kệ, 70 Chậu (có thể xếp xen kẽ để giao hàng đều). **Constraint buffer** = 1 ngày công việc đã sẵn sàng trước laser = 2.400/5 = **480 phút laser**; chia vùng: Xanh >= 320 phút việc chờ, Vàng 160-320, Đỏ < 160. **Rope**: phát tấm inox và bản vẽ cho laser theo đúng lịch Drum, không phát sớm hơn 1 ngày.
8. **Exploit cụ thể**: lồng cắt (nesting) tối ưu tấm để giảm phế liệu; cho laser chạy giờ nghỉ trưa; tách việc nạp/dỡ tấm cho người phụ; kiểm tra chất lượng bản vẽ **trước** laser để không cắt lỗi.
9. **Elevate - mua laser thứ hai**: giả định giá 600 triệu, nhân công vận hành thêm 3,5 triệu/tuần, năng lực laser 4.800 phút/tuần. Với 4.800 phút: Kệ 100 (1.000), Chậu 80 (1.600), Bàn: (4.800 - 2.600)/45 = 48,9 => 48 chiếc (2.160); tổng laser 4.760 (99,2%). $T = 100 \times 440 + 80 \times 600 + 48 \times 1.200 = 44.000 + 48.000 + 57.600 = 149.600$ k (≈ **149,6 triệu**/tuần). Kiểm tra: chấn 500 + 800 + 720 = 2.020/2.400 = 84,2%; hàn 800 + 1.200 + 960 = 2.960/4.800 = 61,7%; đánh bóng 1.500 + 2.400 + 1.920 = 5.820/9.600 = 60,6% => đều ổn. $\Delta T = 149{,}6 - 86 = 63{,}6$ triệu/tuần; trừ OE tăng 3,5 => ròng **60,1 triệu/tuần** => hoàn vốn 600/60,1 ≈ **10 tuần**.
10. **Repeat**: sau khi có laser 2, tải chấn gấp lên 84% - ràng buộc kế tiếp có thể là chấn hoặc thị trường (Bàn còn 12 chiếc nhu cầu chưa đáp ứng).

#### Ý nghĩa kinh doanh và bài học

- Quyết định theo "% lãi gộp cao nhất" làm xưởng **mất 22 triệu/tuần**, tương đương hơn 87 triệu/tháng.
- Không dừng việc nhận đơn "Bàn": có thể **tăng giá Bàn** cho đến khi T/CU của Bàn vượt Chậu (cần T > 30 x 45 = 1.350k, tức giá >= 2.150k nếu NVL không đổi) hoặc chỉ nhận khi laser còn rảnh.
- Elevate chỉ sau khi tối ưu mix (miễn phí): và chỉ sau khi tính hoàn vốn.
- **Cảnh báo**: Throughput Accounting chỉ hợp lý khi ràng buộc thực sự là laser; nếu khách hàng chiến lược cần cả 3 sản phẩm, cần cân nhắc yếu tố quan hệ/giá trị dài hạn, không chỉ T/CU.

### 3.14. Bảng tổng hợp case study

| Case | Bước TOC chính | Kết quả định lượng (minh họa) | Bài học chính |
|---|---|---|---|
| 3.1 Ford (dây chuyền sơn) | Identify + DBR | 42 -> 46 xe/giờ; WIP chốt 92 xe thay vì +224/ca | Xác định đúng ràng buộc trước khi hành động |
| 3.2 Dệt may VN | Subordinate | WIP 160 -> 18 tấn; ~8,5 tỷ vốn giải phóng | Giảm tốc công đoạn không phải ràng buộc để tối ưu hệ thống |
| 3.3 Xưởng in TP.HCM | Exploit | Năng lực +23%; NP 56 -> 147 triệu | SME cải thiện không cần đầu tư lớn |
| 3.4 Đồ gỗ (thất bại) | Bỏ qua Identify | NP giảm 708 -> 645 triệu; buồng sơn: 1.589 triệu | Đầu tư sai chỗ nếu không xác định ràng buộc |
| 3.5 Phòng khám | Subordinate | Chờ TB ~52 phút -> dưới ~18 phút | Ràng buộc có thể nằm ở phân bố tải theo giờ |
| 3.6 Boeing CCPM | CCPM | 72 -> 54 ngày | Gom dự phòng thành Project Buffer chung |
| 3.7 Chuỗi nhà hàng | Exploit | +144,5 triệu/tháng (3 chi nhánh) | Giải phóng người có kỹ năng hiếm khỏi việc phụ |
| 3.8 Trung tâm hoàn tất đơn hàng | Exploit + Subordinate | 800 -> 928 đơn/giờ | Đồng bộ dòng chảy theo trạm đóng gói |
| 3.9 Bao bì Bình Dương | Identify (thị trường) | NP 392 -> 1.017 triệu | Ràng buộc có thể là thị trường |
| 3.10 Logistics | Exploit | 39 -> 45 chuyến/ngày | Tối ưu khâu bốc xếp thay vì mua thêm xe |
| 3.11 Linh kiện Bắc Ninh | Exploit | QC +29,6% | Kiểm tra theo rủi ro, đào tạo chéo |
| 3.12 Cửa hàng tiện lợi | Replenishment/DBM | Tồn 14 -> 9 ngày; OOS 8,5% -> 3,2% | Bổ sung theo tiêu thụ thực |
| 3.13 Xưởng inox Thành Phát | Cả 5 bước + T/CU | T 64,04 -> 86 triệu/tuần; hoàn vốn laser 2: ~10 tuần | Product mix theo T/CU, không theo % lãi gộp |

---


## IV. Ứng dụng cho SME

### 4.1. Quy trình triển khai TOC từng bước trong thực tế

**Tại sao cần quy trình?** TOC rất đơn giản về ý tưởng nhưng dễ sai ở thực thi: nhiều doanh nghiệp "biết" nguyên lý mà vẫn nhảy thẳng đến mua máy. Quy trình dưới đây ép đi từ dữ liệu đến hành động.

1. **Vẽ sơ đồ dòng chảy (Process Flow)** và thu thập dữ liệu năng lực thực tế từng công đoạn (không dùng công suất danh nghĩa trên catalogue).
2. **So sánh năng lực với nhu cầu** để xác định ràng buộc (Identify): dùng bảng ở mục 5.2; kiểm chứng bằng việc quan sát nơi hàng chờ tích tụ.
3. **Phân tích lãng phí năng lực tại ràng buộc** (dừng máy, chờ nguyên liệu, chuyển đổi, lỗi chất lượng) và loại bỏ (Exploit).
4. **Đồng bộ toàn hệ thống** theo nhịp ràng buộc, thiết lập Drum-Buffer-Rope, chấp nhận nhàn rỗi ở công đoạn khác (Subordinate).
5. **Đánh giá Elevate** nếu vẫn thiếu: tính $\Delta T$, chi phí, thời gian hoàn vốn (ví dụ case 3.4 và 3.13).
6. **Lặp lại** (Repeat): tìm ràng buộc mới, cảnh giác với quán tính (Inertia): chính sách cũ có thể trở thành ràng buộc.

### 4.2. SME và doanh nghiệp lớn: khác biệt mức độ áp dụng

| Tiêu chí | SME | Doanh nghiệp lớn |
|---|---|---|
| Công cụ sử dụng | Quan sát trực tiếp, bảng tính đơn giản | Phần mềm hoạch định sản xuất tích hợp TOC (APS) |
| Trọng tâm áp dụng | Chủ yếu bước Exploit (tối ưu miễn phí) | Toàn bộ 5 bước bao gồm Elevate (đầu tư lớn) |
| Yêu cầu chuyên môn | Có thể tự thực hiện dựa trên nguyên tắc cơ bản | Cần đội ngũ chuyên trách phân tích và triển khai |
| Lợi thế riêng | Ít tầng quản lý, thay đổi nhanh | Dữ liệu và nguồn lực đầu tư lớn |

### 4.3. Chi phí đầu tư theo giai đoạn

| Giai đoạn | Hoạt động | Chi phí ước tính (VNĐ) |
|---|---|---|
| Khởi đầu | Xác định ràng buộc bằng quan sát, dữ liệu cơ bản | Miễn phí |
| Tăng trưởng | Đào tạo nhân viên về TOC, tối ưu hoá lịch trình | 5-20 triệu (đào tạo, tư vấn) |
| Mở rộng/Doanh nghiệp lớn | Đầu tư phần mềm APS, nâng cấp ràng buộc (Elevate) | Hàng trăm triệu đến hàng tỷ đồng |

*(Chi phí là ước tính tham khảo, cần cập nhật theo báo giá thực tế.)*

### 4.4. Lộ trình khuyến nghị cho SME

1. Vẽ sơ đồ dòng chảy sản xuất/dịch vụ đơn giản, quan sát công đoạn nào thường xuyên "tắc" nhất.
2. Áp dụng Exploit trước: giảm thời gian chết, tối ưu lịch trình tại công đoạn ràng buộc.
3. Điều chỉnh các công đoạn khác phục vụ nhịp ràng buộc, chấp nhận nhàn rỗi ở nơi không phải ràng buộc.
4. Đo kết quả (sản lượng, lead time, T, NP) trước khi cân nhắc đầu tư lớn.
5. Khi đã tối ưu hết mức miễn phí mà vẫn thiếu, mới nâng cấp ràng buộc.

### 4.5. So sánh rủi ro tài chính giữa các chiến lược xử lý ràng buộc

| Chiến lược | Vốn đầu tư | Rủi ro nếu sai | Thời gian thấy kết quả |
|---|---|---|---|
| Exploit (tối ưu miễn phí) | Rất thấp | Thấp | Nhanh (vài tuần) |
| Subordinate (đồng bộ hoá hệ thống) | Thấp | Thấp - trung bình (phản ứng từ nhân viên) | Nhanh - trung bình |
| Elevate (đầu tư nâng cấp) | Cao - rất cao | Cao (nếu xác định sai ràng buộc) | Chậm (vài tháng đến vài năm) |

**Minh họa** (lấy từ case 3.4): đầu tư sai chỗ 3,2 tỷ làm NP giảm 63,3 triệu/tháng; đầu tư đúng chỗ 900 triệu hoàn vốn khoảng 1 tháng. Khoảng cách giữa hai kết cục chỉ là bước Identify.

### 4.6. Các sai lầm thường gặp khi triển khai TOC

| Sai lầm | Hậu quả | Cách phòng tránh |
|---|---|---|
| Xác định ràng buộc theo cảm tính thay vì dữ liệu | Đầu tư/cải tiến sai chỗ | Thu thập dữ liệu năng lực thực tế từng công đoạn |
| Nhảy thẳng đến Elevate, bỏ qua Exploit | Tốn kém không cần thiết | Luôn thử Exploit trước, ghi lại hiệu quả |
| Không đồng bộ các bộ phận khác theo ràng buộc | Tồn kho tăng ở công đoạn không phải ràng buộc | Áp dụng nghiêm túc Subordinate, đổi chỉ tiêu thưởng |
| Dừng sau khi giải quyết một ràng buộc | Bỏ lỡ cải tiến liên tục | Đưa vòng lặp 5 bước vào họp vận hành định kỳ |
| Bỏ qua ràng buộc thị trường/chính sách | Đầu tư năng lực thừa | Đối chiếu công suất sử dụng với doanh số (case 3.9) |
| Đo OEE/hiệu suất ở mọi máy | Khuyến khích chạy thừa | Chỉ đo và thưởng theo ràng buộc và Throughput toàn hệ thống |

### 4.7. Vai trò của lãnh đạo và văn hoá doanh nghiệp

Thách thức lớn nhất khi triển khai TOC là thay đổi **tư duy đo lường hiệu suất**: thay vì đánh giá từng bộ phận theo tỷ lệ sử dụng máy/nhân công tối đa (local efficiency), lãnh đạo phải truyền thông rõ: mục tiêu là tối đa hoá Throughput toàn hệ thống; một số bộ phận **nhàn rỗi có chủ đích** là bình thường và cần thiết. Doanh nghiệp duy trì TOC lâu dài thường có cam kết rõ ràng của lãnh đạo cấp cao trong việc bảo vệ nguyên lý này trước áp lực đo lường truyền thống từ các phòng ban riêng lẻ.

**Gợi ý hành động cho chủ SME**: (1) đổi chỉ tiêu thưởng quản đốc từ "hiệu suất máy" sang "giao đúng nhịp"; (2) giải thích bằng ví dụ của chính xưởng (ví dụ tồn kho chờ trước ràng buộc); (3) cho nhân viên không ở ràng buộc tham gia hỗ trợ ràng buộc (đào tạo chéo).

### 4.8. TOC trong ngành dịch vụ và bán lẻ

TOC ra đời từ sản xuất nhưng áp dụng tốt cho dịch vụ: trong ngân hàng, ràng buộc có thể là quầy xử lý hồ sơ vay phức tạp; trong bệnh viện/phòng khám là phòng mổ hoặc máy chẩn đoán hình ảnh (xem case 3.5); trong bán lẻ là khâu thanh toán vào giờ cao điểm; trong nhà hàng là bếp trưởng/quầy bar (case 3.7). 5 bước áp dụng tương tự: xác định khâu giới hạn năng lực phục vụ, tối ưu hoá miễn phí trước, rồi mới mở rộng.

### 4.9. Dấu hiệu doanh nghiệp sẵn sàng chuyển từ SME lên áp dụng TOC toàn diện

- Ràng buộc đã dịch chuyển nhiều lần trong năm và khó theo dõi thủ công bằng bảng tính.
- Chuỗi cung ứng mở rộng ra nhiều kho/điểm bán, cần Replenishment Solution tự động.
- Số dự án chạy song song tăng cao, cần phần mềm CCPM chuyên dụng.
- Ban lãnh đạo chấp nhận đầu tư ngân sách cho phần mềm APS/mô phỏng.

### 4.10. Chi phí ẩn của quản lý truyền thống và tính bền vững

| Loại chi phí ẩn | Quản lý truyền thống (tối ưu cục bộ) | Quản lý theo TOC |
|---|---|---|
| Tồn kho bán thành phẩm dư thừa | Cao (các công đoạn chạy hết công suất không đồng bộ) | Thấp (đồng bộ theo nhịp ràng buộc) |
| Chi phí tăng ca không cần thiết | Cao (tăng ca ở công đoạn không phải ràng buộc) | Thấp (chỉ tăng ca tại đúng ràng buộc khi cần) |
| Chi phí cơ hội do đầu tư sai chỗ | Cao (đầu tư dàn trải) | Thấp (tập trung vào ràng buộc đã xác định đúng) |

Góc nhìn bền vững: khi tập trung vào đúng ràng buộc, doanh nghiệp tránh được đầu tư dàn trải, lãng phí vốn, năng lượng, nguyên vật liệu vào các công đoạn không thực sự cần thiết - đây cũng là cách sử dụng tài nguyên hiệu quả hơn.

---

## V. Tools & Templates

### 5.1. Bảng công cụ hỗ trợ triển khai TOC

| Công cụ | Loại | Chi phí (ước tính, cần cập nhật) | Phù hợp |
|---|---|---|---|
| Excel/Google Sheets theo dõi năng lực, T/CU | Thủ công | Miễn phí | SME |
| Phần mềm CCPM chuyên dụng (ví dụ Realization/Concerto) | Chuyên dụng | Hàng chục triệu VNĐ/năm | Doanh nghiệp vừa, quản trị nhiều dự án |
| Phần mềm APS (ví dụ SAP APO/Oracle APS) | Hệ thống hoạch định lớn, tích hợp chuỗi cung ứng | Hàng trăm triệu đến hàng tỷ VNĐ | Doanh nghiệp lớn |
| Phần mềm mô phỏng (Simul8, FlexSim) | Mô phỏng dòng chảy | Hàng chục triệu VNĐ/năm | Doanh nghiệp vừa và lớn |

**Sơ đồ chọn công cụ theo quy mô**:

```
Doanh nghiệp cần công cụ TOC?
        │
        ├── Quy mô nhỏ, ngân sách hạn chế ──► Excel/Google Sheets tự xây dựng
        │
        ├── Quy mô vừa, cần quản trị dự án ──► Phần mềm CCPM chuyên dụng (Realization...)
        │
        └── Quy mô lớn, chuỗi cung ứng phức tạp ──► Hệ thống APS tích hợp toàn diện
```

**TOC và chuyển đổi số**: các phần mềm APS hiện đại tích hợp thuật toán TOC để tự động xác định ràng buộc và đề xuất lịch theo thời gian thực, và hỗ trợ DBM (mục 2.8), giảm công sức phân tích thủ công so với bảng tính.

### 5.2. Template bảng phân tích năng lực xác định ràng buộc

| Công đoạn | Năng lực tối đa (đơn vị/giờ) | Nhu cầu thực tế (đơn vị/giờ) | Tỷ lệ sử dụng (%) | Là ràng buộc? |
|---|---|---|---|---|
| Công đoạn 1 | ___ | ___ | ___ | ___ |
| Công đoạn 2 | ___ | ___ | ___ | ___ |
| Công đoạn 3 | ___ | ___ | ___ | ___ |

**Ví dụ đã điền** (dây chuyền mục 1.2, nhu cầu 80 sp/giờ): A 120 -> 62,5% -> Không; B 90 -> 83,3% -> Không; **C 75 -> 100% -> Có**; D 100 -> 75% -> Không. Công thức tỷ lệ sử dụng: $\text{Dòng chảy thực tế} / \text{Năng lực tối đa}$.

### 5.3. Template báo cáo Buffer Management hàng ngày

| Ngày | Đơn hàng | % Buffer đã tiêu hao | Vùng (Xanh/Vàng/Đỏ) | Hành động cần thực hiện |
|---|---|---|---|---|
| ___ | ___ | ___ | ___ | ___ |

**Ví dụ đã điền** (buffer mỗi đơn = 3 ngày):

| Đơn hàng | Buffer tiêu hao (ngày) | % tiêu hao | Vùng | Hành động |
|---|---|---|---|---|
| DH-101 | 0,6 | 20% | Xanh | Không can thiệp |
| DH-102 | 1,5 | 50% | Vàng | Tìm nguyên nhân, chuẩn bị phương án |
| DH-103 | 2,4 | 80% | Đỏ | Ưu tiên ngay: đẩy nguyên liệu, tăng nhân lực |
| DH-104 | 3,3 | 110% | Vượt buffer | Báo khách hàng, ghi nhận nguyên nhân |

Bảng giúp theo dõi từng đơn hàng theo mức tiêu hao buffer thay vì theo tiến độ cố định; khi vào vùng Đỏ (trên 66%) cần can thiệp ngay.

### 5.4. Mẫu Excel tính T/CU và product mix

Bố cục (dòng 2 trở đi mỗi dòng là một sản phẩm):

| Cột | Nội dung | Công thức ví dụ (dòng 2) |
|---|---|---|
| A | Sản phẩm | |
| B | Giá bán | |
| C | NVL hoàn toàn biến đổi | |
| D | Thời gian ràng buộc (phút/sp) | |
| E | Nhu cầu tối đa/kỳ | |
| F | T = giá - NVL | `=B2-C2` |
| G | T/CU | `=F2/D2` |
| H | Thứ hạng | `=RANK(G2,$G$2:$G$4,0)` |
| I | Số lượng sản xuất | Với sản phẩm hạng 1: `=MIN(E2,ROUNDDOWN($K$1/D2,0))`; hạng 2: `=MIN(E3,ROUNDDOWN(($K$1-SUMPRODUCT(...))/D3,0))` |
| J | Tổng T | `=I2*F2` |

Ô `K1` chứa tổng phút ràng buộc/kỳ. Sắp xếp bảng theo cột T/CU giảm dần trước khi phân bổ để công thức phân bổ nối tiếp dễ viết (phút còn lại = tổng phút trừ phút đã dùng của các sản phẩm đứng trên). Dòng cuối: $NP = \sum J - OE$. Luôn thêm bảng kiểm tải cho các công đoạn khác (như bước 6 của case 3.13) để đảm bảo chúng không vượt 100%.

---

## VI. Bài tập thực hành

### 6.1. Đề bài

1. **Xác định ràng buộc**: dây chuyền 4 công đoạn: Cắt 60, Hàn 45, Sơn 38, Đóng gói 50 (sp/giờ); nhu cầu 48 sp/giờ. (a) Ràng buộc? (b) Tỷ lệ sử dụng mỗi công đoạn khi dòng chảy bằng đầu ra hệ thống? (c) Nếu Exploit nâng Sơn lên 44 thì đầu ra và ràng buộc mới?
2. **Product mix**: ba sản phẩm dùng chung một ràng buộc 900 phút/tuần. X: giá 500k, NVL 200k, 15 phút, nhu cầu 30. Y: giá 420k, NVL 150k, 10 phút, nhu cầu 40. Z: giá 300k, NVL 60k, 6 phút, nhu cầu 50. (a) Tính T/CU và thứ tự ưu tiên. (b) Số lượng mỗi sản phẩm và tổng T. (c) So sánh với cách ưu tiên theo T/đơn vị lớn nhất.
3. **T, I, OE**: Doanh thu 2.000 triệu, NVL trực tiếp 800 triệu, OE 900 triệu, Inventory 3.600 triệu (đơn vị tháng). Tính T, NP, ROI, T/OE, T/I. Nếu giảm OE 10% hoặc tăng T 10%, NP tăng bao nhiêu %?
4. **Exploit hay Elevate?**: ràng buộc tạo T 150 triệu/tháng. Exploit giảm 10% thời gian dừng máy (cho thêm 10% T hiện có), chi phí một lần 2 triệu. Elevate mua máy 800 triệu nâng năng lực 20% (T thêm 20%), OE tăng 5 triệu/tháng. Tính hoàn vốn mỗi phương án và đề xuất thứ tự.
5. **OEE**: ca 480 phút, dừng máy 60 phút, tốc độ lý tưởng 1,2 sp/phút, thực làm 441 sp, đạt 427 sp. Tính A, P, Q, OEE và nêu ưu tiên cải thiện.
6. **CCPM**: chuỗi 5 nhiệm vụ, ước lượng an toàn (ngày) 8, 6, 10, 12, 4. Tính lịch dự án theo quy tắc 50%, buffer theo RSS, và vùng buffer nếu chuỗi thực tế chạy 24 ngày so với kế hoạch cắt 50%.
7. **Buffer Management**: buffer mỗi đơn 4 ngày; ba đơn đã tiêu hao 1; 2,2; 3,4 ngày. Phân loại vùng và đề xuất hành động.
8. **Little's Law**: WIP trước ràng buộc 90 tấn, ràng buộc xử lý 15 tấn/ngày. Tính lead time chờ; nếu giảm WIP còn 30 tấn thì sao?
9. **Ràng buộc thị trường**: công suất 10.000 sp/tháng, bán 7.000, T 50.000 VNĐ/sp, OE 280 triệu. (A) Mua máy 900 triệu tăng công suất 30%. (B) Tuyển 2 sales tổng 40 triệu/tháng, mỗi người thêm 1.200 sp/tháng. Tính NP hiện tại và sau mỗi phương án.
10. **Tư duy logic**: (a) Xây Current Reality Tree đơn giản cho vấn đề "nhân viên thường xuyên trễ deadline"; (b) viết Evaporating Cloud cho mâu thuẫn "giảm chi phí" và "tăng chất lượng dịch vụ".

### 6.2. Đáp án và hướng dẫn giải

**Bài 1**: (a) Đầu ra = min(60, 45, 38, 50) = 38 < nhu cầu 48 => **Sơn** là ràng buộc. (b) Cắt 38/60 = 63,3%; Hàn 38/45 = 84,4%; Sơn 38/38 = 100%; Đóng gói 38/50 = 76%. (c) Sơn 44 => đầu ra = min(60, 45, 44, 50) = 44 (vẫn < 48), Sơn vẫn là ràng buộc; nếu tiếp tục nâng Sơn lên 45+ thì **Hàn (45)** là ràng buộc kế tiếp.

**Bài 2**: (a) T: X = 300k, Y = 270k, Z = 240k. T/CU: X = 300/15 = 20; Y = 270/10 = 27; Z = 240/6 = 40 => thứ tự **Z, Y, X**. (b) Z: 50 x 6 = 300 phút; Y: 40 x 10 = 400 phút (tổng 700); còn 200 phút => X: 200/15 = 13,3 => 13 sp (195 phút). $T = 50 \times 240 + 40 \times 270 + 13 \times 300 = 12.000 + 10.800 + 3.900 = 26.700$k. (c) Theo T/đơn vị (X, Y, Z): X 30 x 15 = 450 phút; Y 40 x 10 = 400 (tổng 850); còn 50 phút => Z 8 sp (48 phút). $T = 30 \times 300 + 40 \times 270 + 8 \times 240 = 9.000 + 10.800 + 1.920 = 21.720$k. Chênh lệch **4.980k** (~23%) nghiêng về cách T/CU.

**Bài 3**: T = 2.000 - 800 = 1.200; NP = 1.200 - 900 = 300; ROI = 300/3.600 = 8,33%/tháng; T/OE = 1,33; T/I = 0,333. Giảm OE 10% (còn 810): NP = 390 (+30%). Tăng T 10% (1.320): NP = 420 (+40%). (Tăng T hiệu quả hơn.)

**Bài 4**: Exploit: +10% x 150 = +15 triệu/tháng; hoàn vốn = 2/15 = 0,13 tháng (~4 ngày). Elevate: +20% x 150 = 30; trừ OE 5 => 25 triệu/tháng; hoàn vốn = 800/25 = **32 tháng**. Thứ tự: Exploit trước (gần như miễn phí); chỉ Elevate khi vẫn thiếu năng lực và nhu cầu đã được xác nhận (nên tính cả khi sau Exploit).

**Bài 5**: Thời gian chạy = 480 - 60 = 420 => A = 420/480 = 87,5%. Lý tưởng = 420 x 1,2 = 504 sp; P = 441/504 = 87,5%. Q = 427/441 = 96,8%. OEE = 0,875 x 0,875 x 0,968 = **74,1%** (kiểm tra: 427/(480 x 1,2) = 427/576 = 74,1%). Ưu tiên: A và P đều mất 12,5%; xử lý dừng máy (chuyển đổi, chờ liệu) và chạy chậm trước; Q mất 3,2%.

**Bài 6**: Tổng an toàn 40 ngày; cắt 50%: 4, 3, 5, 6, 2 = 20 ngày; Project Buffer 50% = 10 ngày => lịch **30 ngày** (giảm 25% so với 40). RSS = $\sqrt{4^2+3^2+5^2+6^2+2^2} = \sqrt{90} \approx 9{,}5$ ngày. Chuỗi thực tế 24 ngày => tiêu hao 24 - 20 = 4 ngày => 4/10 = 40% => **Vàng**. (Nếu 27 ngày: 7/10 = 70% => Đỏ.)

**Bài 7**: 1/4 = 25% Xanh (không can thiệp); 2,2/4 = 55% Vàng (tìm nguyên nhân, chuẩn bị phương án); 3,4/4 = 85% Đỏ (hành động ngay).

**Bài 8**: $LT = 90/15 = 6$ ngày. WIP 30 => $LT = 30/15 = 2$ ngày (giảm 4 ngày; đầu ra vẫn 15 tấn/ngày nhờ ràng buộc không đổi).

**Bài 9**: Hiện tại T = 7.000 x 50.000 = 350 triệu; NP = 350 - 280 = **70 triệu**. (A) công suất sẵn dư 3.000 sp (sử dụng 70%): tăng thêm công suất không thêm đơn => $\Delta T = 0$, OE tăng khấu hao => NP giảm. (B) thêm 2 x 1.200 = 2.400 sp => $\Delta T = 2.400 \times 50.000 = 120$ triệu; $\Delta NP = 120 - 40 = 80$ => NP = **150 triệu** (gấp ~2,14 lần); sử dụng công suất (7.000 + 2.400)/10.000 = 94%.

**Bài 10**: Hướng dẫn CRT: UDE "trễ deadline" <- "thường nhận việc đột xuất" <- "không có quy tắc ưu tiên" và "đa nhiệm" <- nguyên nhân gốc: chính sách "ai cũng phải đáp ứng mọi yêu cầu ngay". Evaporating Cloud: Mục tiêu chung "dịch vụ bền vững có lợi nhuận"; Nhu cầu B "giữ chi phí thấp" - Hành động D "cắt giảm người"; Nhu cầu C "chất lượng cao" - Hành động D' "tăng nhân sự/đào tạo"; giả định sai cần xét: "chất lượng chỉ đến từ thêm người" - có thể phá vỡ bằng chuẩn hoá quy trình tại khâu ràng buộc (Exploit) để vừa giảm chi phí vừa tăng chất lượng.

---

## PHỤ LỤC: CHECKLIST TOC TỔNG HỢP

### Checklist chuẩn bị và triển khai TOC

**Chuẩn bị**
- □ Đã có dữ liệu năng lực thực tế (không phải công suất danh nghĩa) của từng công đoạn?
- □ Lãnh đạo cấp cao cam kết bảo vệ nguyên lý "nhàn rỗi có chủ đích"?
- □ Đã lên kế hoạch truyền thông thay đổi tư duy đo lường hiệu suất (đổi chỉ tiêu thưởng)?
- □ Đã chọn công cụ theo dõi Buffer Management phù hợp quy mô?

**Triển khai**
- □ Đã xác định ràng buộc bằng dữ liệu, kiểm chứng bằng nơi hàng chờ tích tụ (Identify)?
- □ Đã phân loại ràng buộc: vật lý, thị trường, chính sách, nguồn lực?
- □ Đã thử tối ưu hoá miễn phí (Exploit) trước khi cân nhắc đầu tư (Elevate)?
- □ Đã xếp ưu tiên sản phẩm theo T/CU khi nhiều sản phẩm dùng chung ràng buộc?
- □ Đã kiểm tra tải các công đoạn khác sau khi đổi product mix?
- □ Đã thiết lập Drum (lịch ràng buộc), Buffer và Rope (nhịp phát liệu)?
- □ Đã truyền thông lý do các bộ phận không phải ràng buộc giảm tốc?
- □ Đã thiết lập giám sát mức tiêu hao buffer thay vì giám sát từng công đoạn riêng lẻ?
- □ Đã tính $\Delta T$, chi phí, hoàn vốn trước mọi khoản Elevate?
- □ Đã lên kế hoạch lặp lại 5 bước định kỳ (Repeat) và theo dõi ràng buộc chính sách do quán tính?

### Công thức tổng hợp

| Công thức | Ý nghĩa |
|---|---|
| $T = \text{Doanh thu} - \text{Chi phí hoàn toàn biến đổi (NVL trực tiếp)}$ | Throughput |
| $NP = T - OE$ | Lợi nhuận ròng |
| $ROI = \dfrac{T - OE}{I}$ | Tỷ suất hoàn vốn |
| Năng suất $= T/OE$; Vòng quay $= T/I$ | Hiệu quả dùng chi phí và vốn |
| $T/CU = \dfrac{\text{Giá bán} - \text{NVL}}{\text{Phút tại ràng buộc}}$ | Căn cứ ưu tiên product mix |
| Tỷ lệ sử dụng $= \dfrac{\text{Dòng chảy thực tế}}{\text{Năng lực tối đa}}$ | Nhận diện ràng buộc (gần 100%) |
| $WIP = T_h \times LT$ | Định luật Little |
| $\text{Buffer Penetration} = \dfrac{\text{Buffer đã tiêu hao}}{\text{Tổng buffer}}$ | Xanh < 33%, Vàng 33-66%, Đỏ > 66% |
| Project Buffer $\approx 50\% \times$ chuỗi đã cắt, hoặc $\sqrt{\sum d_i^2}$ | CCPM |
| $OEE = A \times P \times Q$ | Hiệu suất thiết bị (đo tại ràng buộc) |
| Hoàn vốn $= \dfrac{\text{Vốn đầu tư}}{\Delta T - \Delta OE}$ | Đánh giá Elevate |

### Bảng thuật ngữ (Glossary)

| Thuật ngữ | Giải thích |
|---|---|
| Constraint/Bottleneck | Ràng buộc/điểm nghẽn giới hạn năng lực toàn hệ thống |
| Throughput (T) | Tốc độ hệ thống tạo ra tiền qua bán hàng |
| Inventory/Investment (I) | Tổng tiền đầu tư vào những thứ dự định bán ra |
| Operating Expense (OE) | Chi phí biến Inventory thành Throughput |
| Drum-Buffer-Rope (DBR) | Phương pháp lập lịch sản xuất dựa trên nhịp ràng buộc |
| Five Focusing Steps | Identify - Exploit - Subordinate - Elevate - Repeat |
| Throughput Accounting | Kế toán quản trị tập trung vào Throughput |
| T/CU | Throughput trên mỗi đơn vị (phút) ràng buộc |
| Critical Chain (CCPM) | Quản trị dự án theo TOC, gom buffer thành Project Buffer |
| Current Reality Tree | Công cụ truy tìm nguyên nhân gốc rễ |
| Evaporating Cloud | Công cụ giải quyết xung đột bằng phá vỡ giả định sai |
| Future Reality Tree | Công cụ kiểm chứng logic giải pháp trước khi triển khai |
| OEE | Overall Equipment Effectiveness - hiệu suất tổng thể thiết bị |
| Local Optimum | Tối ưu cục bộ, không đồng nghĩa tối ưu toàn hệ thống |
| Replenishment Solution | Bổ sung hàng dựa trên tiêu thụ thực tế theo TOC |
| DBM | Dynamic Buffer Management - điều chỉnh buffer theo dữ liệu |
| TLS (TOC-Lean-Six Sigma) | Kết hợp TOC chọn ưu tiên và Lean/Six Sigma thực thi cải tiến |
| Market Constraint | Ràng buộc thị trường - nhu cầu không đủ lấp đầy năng lực |
| Policy Constraint | Ràng buộc chính sách - quy định nội bộ vô tình giới hạn năng lực |
| Resource Constraint | Ràng buộc nguồn lực - thiếu nhân sự, máy móc, vật tư |
| Student Syndrome | Trì hoãn công việc đến sát hạn chót mới bắt đầu |
| Parkinson's Law | Công việc luôn giãn ra để lấp đầy thời gian được cấp |

### Bảng đo lường KPI TOC

| KPI | Công thức/Ý nghĩa | Mục tiêu tham khảo |
|---|---|---|
| Throughput | Doanh thu - Chi phí NVL trực tiếp | Tối đa hoá liên tục |
| Ràng buộc Utilization | Thời gian ràng buộc hoạt động thực tế / Thời gian có sẵn | Gần 100% |
| Buffer Penetration | % buffer đã tiêu hao so với kế hoạch | Tránh vào vùng Đỏ |
| Lead Time | Thời gian từ đặt hàng đến giao hàng | Giảm liên tục |
| OEE tại ràng buộc | Availability x Performance x Quality | > 85% (benchmark tham khảo) |
| Tỷ lệ đáp ứng đơn hàng đúng hạn | Số đơn giao đúng hạn / Tổng số đơn | > 95% |

### Sổ tay rủi ro TOC (Risk Register mẫu)

| Rủi ro | Xác suất | Tác động | Biện pháp giảm thiểu |
|---|---|---|---|
| Xác định sai ràng buộc | Trung bình | Cao | Thu thập dữ liệu năng lực thực tế trước khi kết luận |
| Ràng buộc dịch chuyển (đặc biệt sang thị trường) | Cao | Trung bình | Lặp lại 5 bước liên tục |
| Nhân viên phản đối giảm tốc công đoạn không phải ràng buộc | Trung bình | Trung bình | Truyền thông logic Subordinate, đổi chỉ tiêu thưởng |
| Elevate quá sớm khi chưa khai thác hết Exploit | Trung bình | Cao | Đánh giá đầy đủ Exploit trước khi đề xuất đầu tư |
| Thiếu cải tiến liên tục sau ràng buộc ban đầu | Cao | Trung bình | Đưa vòng lặp TOC vào họp vận hành định kỳ |

### Bảng tự đánh giá mức độ trưởng thành TOC

| Mức độ | Mô tả |
|---|---|
| Cấp 1 - Nhận thức | Hiểu khái niệm TOC nhưng chưa áp dụng có hệ thống |
| Cấp 2 - Áp dụng đơn lẻ | Đã xác định ràng buộc và Exploit tại một vài điểm |
| Cấp 3 - Hệ thống hoá | Áp dụng đầy đủ 5 bước và Buffer Management thường xuyên |
| Cấp 4 - Văn hoá tổ chức | TOC là tư duy mặc định trong mọi quyết định vận hành và đầu tư |

### Câu hỏi tự kiểm tra nhanh

1. Ba chỉ số T, I, OE khác kế toán chi phí truyền thống như thế nào?
2. Vì sao Exploit phải làm trước Elevate?
3. Drum-Buffer-Rope đồng bộ hoá hệ thống như thế nào?
4. Vì sao "dừng lại sau khi giải quyết một ràng buộc" là sai lầm?
5. TOC, Lean và Six Sigma kết hợp với nhau như thế nào?

### Mối quan hệ với các chủ đề Quản trị Vận hành khác và hướng nghiên cứu mở rộng

TOC là khung tư duy tổng hợp: thiết kế quy trình (file 01) xác định dòng chảy; quản trị chất lượng (file 02) bảo đảm ràng buộc không bị lãng phí vì lỗi; chuỗi cung ứng (file 03) và tồn kho (file 04) kết nối qua Replenishment và Buffer Management; hoạch định năng lực (file 05) qua Bottleneck Analysis; quản trị dự án (file 06) qua Critical Chain; dự báo (file 07) cho ràng buộc thị trường; bố trí mặt bằng (file 08) tối ưu dòng chảy vật lý quanh ràng buộc. Hướng mở rộng: Quản trị rủi ro chuỗi cung ứng toàn cầu, Chuyển đổi số trong vận hành, Quản trị vận hành bền vững.

---

## TÀI LIỆU THAM KHẢO

### Sách tham khảo
1. Goldratt, E. M. & Cox, J. (1984). *The Goal: A Process of Ongoing Improvement*. North River Press.
2. Goldratt, E. M. (1997). *Critical Chain*. North River Press.
3. Dettmer, H. W. (1997). *Goldratt's Theory of Constraints: A Systems Approach to Continuous Improvement*. ASQ Quality Press.
4. Schragenheim, E. & Dettmer, H. W. (2000). *Manufacturing at Warp Speed*. CRC Press.
5. Goldratt, E. M. (1990). *The Haystack Syndrome: Sifting Information Out of the Data Ocean*. North River Press.
6. Cox, J. F. & Schleier, J. G. (2010). *Theory of Constraints Handbook*. McGraw-Hill.
7. Goldratt, E. M. (1994). *It's Not Luck*. North River Press - phần mở rộng của Evaporating Cloud và Current Reality Tree.
8. Woeppel, M. J. (2000). *Manufacturer's Guide to Implementing the Theory of Constraints*. CRC Press.

### Nguồn tài liệu trực tuyến bổ sung
1. Trang chủ Theory of Constraints Institute (tocinstitute.org) - tài liệu và chứng chỉ chuyên sâu về TOC.
2. Cộng đồng Goldratt Marketing Group - các bài viết phân tích case study TOC thực tế từ nhiều ngành.

### Liên kết nội bộ
- [05-capacity-planning.md](./05-capacity-planning.md) - Khái niệm Bottleneck Analysis được mở rộng chi tiết trong file này.
- [06-project-management.md](./06-project-management.md) - CPM/PERT là nền tảng để hiểu Critical Chain Project Management.
- [01-process-design-analysis.md](./01-process-design-analysis.md) - Phân tích dòng chảy quy trình là bước đầu để xác định ràng buộc.
- [03-supply-chain-management.md](./03-supply-chain-management.md) - Replenishment Solution là ứng dụng TOC trong chuỗi cung ứng.
- [04-inventory-management.md](./04-inventory-management.md) - Buffer Management liên quan trực tiếp đến quản trị tồn kho bảo vệ.

*Tài liệu tham khảo: Goldratt & Cox (1984), Goldratt (1990, 1994, 1997), Dettmer (1997), Schragenheim & Dettmer (2000), Cox & Schleier (2010), Woeppel (2000). File này là file cuối trong 9 nội dung cốt lõi của bộ tài liệu Quản trị Vận hành.*
