# 06. Quản trị Dự án (Project Management)

> File thuộc bộ kiến thức Quản trị Vận hành (Operations Management) - MBA Knowledge Base
> Liên kết: [01-process-design-analysis.md](./01-process-design-analysis.md) | [05-capacity-planning.md](./05-capacity-planning.md) | [07-forecasting.md](./07-forecasting.md)

---

## I. Tổng quan & Lý thuyết nền tảng

### 1.1. Định nghĩa Dự án và Quản trị Dự án

**Dự án (Project)** là một nỗ lực tạm thời (có thời điểm bắt đầu và kết thúc rõ ràng) nhằm tạo ra một sản phẩm, dịch vụ hoặc kết quả duy nhất, khác biệt với hoạt động vận hành thường xuyên (operations) vốn mang tính lặp lại liên tục.

**Quản trị dự án (Project Management - PM)** là việc áp dụng kiến thức, kỹ năng, công cụ và kỹ thuật vào các hoạt động của dự án nhằm đáp ứng các yêu cầu đã đề ra, trong giới hạn về phạm vi (scope), thời gian (time), chi phí (cost) và chất lượng (quality).

### 1.2. Tam giác ràng buộc dự án (Project Triple Constraint / Iron Triangle)

```
                    PHẠM VI (Scope)
                         ╱╲
                        ╱  ╲
                       ╱    ╲
                      ╱      ╲
                     ╱ CHẤT   ╲
                    ╱ LƯỢNG    ╲
                   ╱ (Quality)  ╲
                  ╱──────────────╲
        THỜI GIAN                  CHI PHÍ
        (Time)  ◀──── đánh đổi ────▶ (Cost)
```

Ba yếu tố Phạm vi - Thời gian - Chi phí luôn ràng buộc lẫn nhau, với Chất lượng ở trung tâm chịu ảnh hưởng bởi cả ba. Thay đổi một yếu tố (ví dụ rút ngắn thời gian) thường buộc phải đánh đổi ở yếu tố khác (tăng chi phí hoặc giảm phạm vi). Đây là nguyên lý nền tảng mà mọi quyết định quản trị dự án phải cân nhắc.

### 1.3. Vòng đời dự án (Project Life Cycle) theo PMBOK (PMI)

```
Giai đoạn 1        Giai đoạn 2         Giai đoạn 3        Giai đoạn 4
Khởi tạo      ──▶  Hoạch định    ──▶  Thực thi &     ──▶  Kết thúc
(Initiating)       (Planning)         Giám sát            (Closing)
                                      (Executing &
                                       Monitoring/
                                       Controlling)

- Xác định mục    - Lập kế hoạch    - Triển khai công   - Nghiệm thu
  tiêu, phạm vi     chi tiết          việc theo kế         bàn giao
- Xác định các    - Phân bổ nguồn    hoạch               - Đánh giá bài
  bên liên quan     lực             - Theo dõi tiến        học kinh
  (stakeholders)  - Xây dựng lịch     độ, chi phí,          nghiệm
- Phê duyệt dự      trình (Gantt,     chất lượng          - Giải phóng
  án (Project       CPM/PERT)       - Quản lý rủi ro,       nguồn lực
  Charter)        - Hoạch định        thay đổi
                    ngân sách, rủi
                    ro, chất lượng
```

Mức độ ảnh hưởng của các bên liên quan và rủi ro thường cao nhất ở giai đoạn đầu và giảm dần, trong khi chi phí thay đổi (cost of change) tăng dần theo tiến độ dự án - đây là lý do quản trị rủi ro và hoạch định kỹ lưỡng ở giai đoạn đầu có giá trị đặc biệt quan trọng.

### 1.4. Cơ cấu phân chia công việc (Work Breakdown Structure - WBS)

WBS là kỹ thuật phân rã dự án thành các gói công việc (work package) nhỏ hơn, dễ quản lý, ước lượng và giao trách nhiệm hơn.

```
                        DỰ ÁN XÂY DỰNG WEBSITE
                                │
        ┌───────────────┬───────┴───────┬───────────────┐
        ▼               ▼               ▼               ▼
   1. Thiết kế    2. Phát triển    3. Kiểm thử      4. Triển khai
     (Design)      (Development)    (Testing)        (Deployment)
        │               │               │               │
   1.1 UI/UX       2.1 Frontend    3.1 Unit Test    4.1 Deploy Server
   1.2 Wireframe   2.2 Backend     3.2 UAT          4.2 Đào tạo user
   1.3 Prototype   2.3 Database    3.3 Bug Fix       4.3 Go-live
```

Nguyên tắc "Quy tắc 100%" (100% Rule): tổng công việc ở mỗi cấp con phải bằng 100% công việc của cấp cha, đảm bảo không bỏ sót và không trùng lặp phạm vi công việc.

### 1.5. Ba phương pháp luận quản trị dự án chính

| Phương pháp | Đặc điểm | Phù hợp |
|---|---|---|
| **Waterfall (Thác nước)** | Tuần tự, từng giai đoạn hoàn thành mới chuyển giai đoạn sau | Dự án có yêu cầu rõ ràng, ít thay đổi (xây dựng, sản xuất) |
| **Agile (Linh hoạt)** | Lặp lại theo chu kỳ ngắn (sprint), phản hồi liên tục, thích ứng thay đổi | Dự án phần mềm, sản phẩm cần đổi mới nhanh, yêu cầu chưa rõ ràng hoàn toàn |
| **Hybrid** | Kết hợp Waterfall cho hoạch định tổng thể + Agile cho triển khai chi tiết | Dự án lớn, phức tạp, cần cả cấu trúc và linh hoạt |

---

## II. Phân tích chi tiết các công cụ/kỹ thuật

### 2.1. Sơ đồ Gantt (Gantt Chart)

Gantt Chart là công cụ trực quan hoá lịch trình dự án phổ biến nhất, thể hiện các công việc dưới dạng thanh ngang theo trục thời gian, cho thấy thời điểm bắt đầu, kết thúc và mối quan hệ phụ thuộc giữa các công việc.

```
Công việc          T1  T2  T3  T4  T5  T6  T7  T8
Thiết kế UI/UX    ▓▓▓▓▓▓
Phát triển FE           ▓▓▓▓▓▓▓▓
Phát triển BE            ▓▓▓▓▓▓▓▓▓▓
Kiểm thử                          ▓▓▓▓▓
Triển khai                              ▓▓▓
                  └──────────── Milestone: Ra mắt sản phẩm (T8)
```

**Ưu điểm**: Trực quan, dễ hiểu cho mọi cấp quản lý, dễ dàng theo dõi tiến độ tổng thể.
**Hạn chế**: Không thể hiện rõ ràng công việc nào là "đường găng" (critical path) quyết định tổng thời gian dự án, khó thể hiện các dự án phức tạp với hàng trăm công việc phụ thuộc chằng chịt.

### 2.2. Phương pháp Đường Găng (Critical Path Method - CPM)

CPM là kỹ thuật xác định chuỗi các công việc dài nhất (đường găng - critical path) quyết định tổng thời gian tối thiểu để hoàn thành dự án. Bất kỳ sự chậm trễ nào trên đường găng đều trực tiếp làm chậm toàn bộ dự án.

**Các bước thực hiện CPM**:

1. Liệt kê tất cả công việc, thời gian ước tính, và mối quan hệ phụ thuộc (predecessor).
2. Vẽ sơ đồ mạng lưới (network diagram) thể hiện trình tự công việc.
3. Tính toán thời gian sớm nhất có thể bắt đầu/kết thúc (Forward Pass - ES, EF).
4. Tính toán thời gian muộn nhất có thể bắt đầu/kết thúc mà không trễ dự án (Backward Pass - LS, LF).
5. Tính độ trễ cho phép (Float/Slack) = LS - ES (hoặc LF - EF).
6. Xác định đường găng: chuỗi công việc có Float = 0.

**Ví dụ minh hoạ mạng lưới CPM đơn giản**:

```
Công việc  Thời gian(ngày)  Phụ thuộc
   A            3              -
   B            5              -
   C            4              A
   D            6              B
   E            2              C, D

Sơ đồ mạng:
   A(3) ──▶ C(4) ──┐
                    ├──▶ E(2)
   B(5) ──▶ D(6) ──┘

Đường 1: A → C → E = 3+4+2 = 9 ngày
Đường 2: B → D → E = 5+6+2 = 13 ngày  ← ĐƯỜNG GĂNG (dài nhất)

Tổng thời gian dự án tối thiểu = 13 ngày
Float của A = 13 - 9 = 4 ngày (có thể trễ tối đa 4 ngày mà không ảnh hưởng dự án)
Float của B, D = 0 ngày (nằm trên đường găng, không được phép trễ)
```

### 2.3. Kỹ thuật đánh giá và xem xét chương trình (PERT - Program Evaluation and Review Technique)

PERT mở rộng CPM bằng cách xử lý sự bất định trong ước lượng thời gian, sử dụng ba ước lượng thay vì một ước lượng cố định:

$$t_e = \frac{t_o + 4t_m + t_p}{6}$$

Trong đó:
- $t_o$ = Thời gian lạc quan (Optimistic time) - nếu mọi thứ diễn ra thuận lợi nhất
- $t_m$ = Thời gian khả dĩ nhất (Most likely time)
- $t_p$ = Thời gian bi quan (Pessimistic time) - nếu gặp nhiều trở ngại nhất

**Độ lệch chuẩn của mỗi công việc** (đo lường độ bất định):

$$\sigma = \frac{t_p - t_o}{6}$$

**Độ lệch chuẩn của toàn dự án** (tổng phương sai các công việc trên đường găng):

$$\sigma_{project} = \sqrt{\sum \sigma_i^2 \text{ (trên đường găng)}}$$

**Ứng dụng**: PERT cho phép tính xác suất hoàn thành dự án trước một thời hạn cụ thể bằng phân phối chuẩn, hữu ích cho các dự án nghiên cứu, phát triển sản phẩm mới có độ bất định cao về thời gian thực hiện.

**Ví dụ**: Một công việc có $t_o = 4$ ngày, $t_m = 6$ ngày, $t_p = 14$ ngày.

$$t_e = \frac{4 + 4(6) + 14}{6} = \frac{4+24+14}{6} = \frac{42}{6} = 7 \text{ ngày}$$

$$\sigma = \frac{14-4}{6} = 1.67 \text{ ngày}$$

### 2.4. Rút ngắn thời gian dự án (Crashing)

Khi cần rút ngắn thời gian dự án (do yêu cầu khách hàng, cơ hội thị trường), kỹ thuật Crashing giúp xác định công việc nào trên đường găng nên được đẩy nhanh với chi phí thấp nhất.

$$\text{Chi phí crash mỗi ngày} = \frac{\text{Chi phí crash} - \text{Chi phí bình thường}}{\text{Thời gian bình thường} - \text{Thời gian crash}}$$

**Nguyên tắc**: Luôn ưu tiên crash công việc trên đường găng có chi phí/ngày rút ngắn thấp nhất trước. Sau khi crash, cần kiểm tra lại xem đường găng có thay đổi hay không (có thể xuất hiện đường găng mới sau khi rút ngắn đường găng cũ).

### 2.5. Quản lý Agile và Scrum Framework

**Scrum** là framework Agile phổ biến nhất, tổ chức công việc theo các chu kỳ lặp ngắn gọi là Sprint (thường 1-4 tuần).

**Các vai trò chính trong Scrum**:

| Vai trò | Trách nhiệm |
|---|---|
| Product Owner | Định nghĩa và ưu tiên hoá Product Backlog (danh sách yêu cầu/tính năng) |
| Scrum Master | Hỗ trợ nhóm tuân thủ quy trình Scrum, loại bỏ trở ngại (impediments) |
| Development Team | Thực hiện công việc, tự tổ chức để hoàn thành Sprint Backlog |

**Chu trình Sprint**:

```
Sprint Planning ──▶ Daily Scrum ──▶ Sprint Review ──▶ Sprint Retrospective
(Lập kế hoạch      (Họp đứng 15    (Demo sản phẩm    (Rút kinh nghiệm,
 sprint, chọn        phút mỗi        cho stakeholder)   cải tiến quy
 backlog items)      ngày)                              trình cho sprint
                                                          tiếp theo)
        └──────────────── Lặp lại mỗi 1-4 tuần ─────────────────┘
```

**So sánh Scrum vs Kanban** (hai framework Agile phổ biến):

| Tiêu chí | Scrum | Kanban |
|---|---|---|
| Nhịp độ | Theo Sprint cố định (time-boxed) | Luồng liên tục (continuous flow) |
| Vai trò | Có vai trò cố định (PO, SM, Team) | Không yêu cầu vai trò cố định |
| Thay đổi trong chu kỳ | Hạn chế thay đổi trong Sprint đang chạy | Có thể thay đổi ưu tiên bất kỳ lúc nào |
| Công cụ trực quan | Sprint Backlog, Burndown Chart | Kanban Board với giới hạn WIP (Work In Progress) |
| Phù hợp | Đội nhóm phát triển sản phẩm có chu kỳ rõ ràng | Đội vận hành/hỗ trợ có luồng công việc liên tục |

### 2.6. Quản trị rủi ro dự án (Project Risk Management)

**Ma trận đánh giá rủi ro (Probability-Impact Matrix)**:

```
Tác động
   Cao   │  Giám sát chặt     │  Ưu tiên xử lý ngay
         │  (Monitor)          │  (High Priority)
         │────────────────────┼──────────────────────
   Thấp  │  Chấp nhận          │  Lập kế hoạch dự phòng
         │  (Accept)           │  (Contingency Plan)
         └────────────────────┴──────────────────────
              Thấp                    Cao
                   Xác suất xảy ra
```

**4 chiến lược ứng phó rủi ro (Risk Response Strategies)**:
1. **Né tránh (Avoid)**: thay đổi kế hoạch để loại bỏ hoàn toàn rủi ro.
2. **Giảm thiểu (Mitigate)**: giảm xác suất hoặc tác động của rủi ro.
3. **Chuyển giao (Transfer)**: chuyển rủi ro cho bên thứ ba (bảo hiểm, hợp đồng thầu phụ).
4. **Chấp nhận (Accept)**: chấp nhận rủi ro nếu chi phí xử lý cao hơn tác động tiềm tàng.

---

## III. Ưu điểm & Nhược điểm

### 3.1. Bảng so sánh Waterfall vs Agile

| Tiêu chí | Waterfall | Agile |
|---|---|---|
| Yêu cầu dự án | Cần rõ ràng ngay từ đầu | Có thể thay đổi, làm rõ dần |
| Khả năng thích ứng thay đổi | Thấp, chi phí thay đổi cao ở giai đoạn sau | Cao, thay đổi được tích hợp mỗi sprint |
| Khả năng dự đoán ngân sách/thời gian | Cao (rõ ràng từ đầu) | Thấp hơn (linh hoạt theo tiến độ thực tế) |
| Sự tham gia của khách hàng | Chủ yếu đầu và cuối dự án | Liên tục xuyên suốt dự án |
| Rủi ro chính | Phát hiện sai sót muộn, chi phí sửa cao | Có thể thiếu tầm nhìn tổng thể dài hạn nếu quản lý kém |
| Phù hợp | Xây dựng, sản xuất, dự án có quy định pháp lý chặt | Phát triển phần mềm, sản phẩm số, startup |

### 3.2. Bảng ưu nhược điểm CPM/PERT

| Khía cạnh | Ưu điểm | Nhược điểm |
|---|---|---|
| CPM | Xác định rõ đường găng, tập trung nguồn lực đúng chỗ | Giả định thời gian công việc cố định, không xử lý bất định |
| PERT | Xử lý được bất định, tính xác suất hoàn thành | Phức tạp hơn, cần ước lượng 3 kịch bản cho mỗi công việc |
| Cả hai | Cung cấp cơ sở khoa học cho lập lịch và phân bổ nguồn lực | Không phản ánh tốt các dự án có phạm vi thay đổi liên tục (phù hợp Agile hơn) |

---

## IV. Case study thực tiễn

### 4.1. Case study quốc tế lớn: Boeing 777 - Ứng dụng CPM/PERT trong dự án phát triển máy bay

**Bối cảnh**: Dự án phát triển Boeing 777 (thập niên 1990) là một trong những dự án kỹ thuật phức tạp nhất, với hàng triệu công việc liên quan, đòi hỏi phối hợp giữa hàng nghìn kỹ sư và nhà cung cấp.

**Ứng dụng**: Boeing sử dụng hệ thống CPM/PERT quy mô lớn kết hợp công nghệ CAD 3D (thiết kế không giấy - paperless design) để quản lý mối phụ thuộc giữa hàng nghìn công việc thiết kế, thử nghiệm, sản xuất. Đường găng được cập nhật liên tục để xác định các rủi ro trễ tiến độ then chốt.

**Kết quả**: Dự án hoàn thành đúng tiến độ và ngân sách - một thành tựu hiếm có trong ngành hàng không vốn nổi tiếng với các dự án bị trễ hạn nghiêm trọng (như trường hợp Boeing 787 đã phân tích ở file 03).

### 4.2. Case study Việt Nam lớn: VinFast - Quản trị dự án xây dựng nhà máy ô tô thần tốc

**Bối cảnh**: VinFast xây dựng nhà máy sản xuất ô tô tại Hải Phòng chỉ trong 21 tháng (2017-2019), một tốc độ được xem là kỷ lục trong ngành công nghiệp ô tô toàn cầu (thông thường mất 3-5 năm).

**Phương pháp áp dụng**: Kết hợp phương pháp Waterfall cho hoạch định tổng thể (do có nhiều ràng buộc pháp lý, kỹ thuật xây dựng) với việc chạy song song nhiều hạng mục công việc thay vì tuần tự (fast-tracking) - một kỹ thuật rút ngắn thời gian dự án bằng cách thực hiện đồng thời các công việc thường được lên kế hoạch nối tiếp nhau. Đầu tư nguồn lực khổng lồ để "crash" các công việc trên đường găng.

**Kết quả**: Hoàn thành nhà máy đúng cam kết, dù đánh đổi bằng chi phí đầu tư rất lớn - minh chứng điển hình cho việc áp dụng kỹ thuật Crashing và Fast-tracking ở quy mô công nghiệp lớn.

### 4.3. Case study SME Việt Nam: Startup công nghệ áp dụng Scrum phát triển ứng dụng di động

**Bối cảnh**: Một startup công nghệ 15 người tại Hà Nội phát triển ứng dụng đặt đồ ăn, ban đầu áp dụng mô hình Waterfall truyền thống nhưng liên tục trễ hạn do yêu cầu khách hàng thay đổi liên tục sau khi thấy sản phẩm thực tế.

**Giải pháp**: Chuyển đổi sang Scrum với Sprint 2 tuần, Product Owner là founder trực tiếp làm việc với khách hàng thí điểm để thu thập phản hồi liên tục, demo sản phẩm cuối mỗi sprint để điều chỉnh hướng phát triển kịp thời thay vì chờ đến khi hoàn thành toàn bộ mới phát hiện sai lệch.

**Kết quả**: Thời gian đưa sản phẩm ra thị trường (Time-to-Market) giảm đáng kể, đội nhóm phản ứng nhanh hơn với phản hồi thị trường thực tế, giảm lãng phí phát triển các tính năng không cần thiết.

### 4.4. Case study quốc tế - thất bại: Dự án Denver International Airport Baggage System

**Bối cảnh**: Hệ thống xử lý hành lý tự động tại sân bay quốc tế Denver (thập niên 1990) là một trong những case study kinh điển về thất bại quản trị dự án được giảng dạy rộng rãi trong các chương trình MBA.

**Vấn đề phát sinh**:
- Phạm vi dự án liên tục mở rộng (scope creep) mà không đánh giá đầy đủ tác động đến thời gian/chi phí.
- Công nghệ tự động hoá phức tạp chưa từng được triển khai ở quy mô tương tự, độ bất định kỹ thuật cao nhưng không được quản trị rủi ro đầy đủ.
- Thiếu sự phối hợp giữa các nhà thầu và bên liên quan.
- Dự án bị trễ 16 tháng, đội chi phí thêm hơn 560 triệu USD so với ngân sách ban đầu.

**Bài học**: Đây là minh chứng điển hình cho hậu quả của việc quản trị phạm vi kém (scope creep), đánh giá rủi ro công nghệ không đầy đủ, và thiếu quy trình kiểm soát thay đổi (change control) chặt chẽ trong các dự án có độ phức tạp kỹ thuật cao.

### 4.5. Case study Việt Nam SME - dịch vụ: Công ty tổ chức sự kiện quản lý dự án đa nhiệm

**Bối cảnh**: Một công ty tổ chức sự kiện quy mô 20 nhân viên thường xuyên phải quản lý 5-10 sự kiện cùng lúc (hội nghị doanh nghiệp, đám cưới, ra mắt sản phẩm), mỗi sự kiện có deadline cố định không thể trễ.

**Vấn đề**: Trước đây quản lý bằng file Excel rời rạc cho từng sự kiện, dẫn đến xung đột nguồn lực (cùng một nhân viên/thiết bị được phân công cho 2 sự kiện trùng thời gian) mà không phát hiện kịp thời.

**Giải pháp**: Áp dụng WBS chi tiết cho mỗi loại sự kiện (template chuẩn hoá), sử dụng phần mềm quản lý dự án đa dự án (Trello, Asana) để theo dõi tổng thể nguồn lực (nhân sự, thiết bị) được phân bổ xuyên suốt tất cả sự kiện đang diễn ra, xác định trước các điểm xung đột nguồn lực (resource conflict) để điều chỉnh kịp thời.

**Kết quả**: Giảm đáng kể tình trạng xung đột nguồn lực gây ảnh hưởng chất lượng sự kiện, cải thiện khả năng nhận thêm dự án mới nhờ có cái nhìn tổng thể rõ ràng về năng lực khả dụng.

### 4.6. Bảng tổng hợp bài học từ các case study

| Case study | Phương pháp áp dụng | Bài học chính |
|---|---|---|
| Boeing 777 | CPM/PERT + CAD 3D | Hệ thống quản trị đường găng quy mô lớn giúp hoàn thành dự án phức tạp đúng hạn |
| VinFast | Fast-tracking + Crashing | Chạy song song công việc và đầu tư mạnh có thể rút ngắn đáng kể thời gian dự án |
| Startup ứng dụng đặt đồ ăn | Chuyển đổi Waterfall sang Scrum | Agile phù hợp hơn khi yêu cầu khách hàng chưa rõ ràng, cần phản hồi liên tục |
| Denver Airport (thất bại) | (Bài học từ thất bại quản trị phạm vi) | Scope creep và thiếu quản trị rủi ro công nghệ gây thiệt hại nghiêm trọng |
| Công ty tổ chức sự kiện | WBS + phần mềm đa dự án | Quản lý nguồn lực xuyên suốt nhiều dự án đồng thời cần công cụ tổng thể, không rời rạc |

---

## V. Phương pháp triển khai từng bước

### 5.1. Quy trình 8 bước quản trị dự án theo PMBOK

```
Bước 1: Khởi tạo dự án (Project Charter)
   │  Xác định mục tiêu, phạm vi, các bên liên quan chính
   ▼
Bước 2: Xây dựng WBS
   │  Phân rã công việc thành các gói quản lý được
   ▼
Bước 3: Ước lượng thời gian & chi phí
   │  Sử dụng dữ liệu lịch sử, ý kiến chuyên gia, PERT nếu cần
   ▼
Bước 4: Xây dựng lịch trình (CPM/Gantt)
   │  Xác định đường găng, các mốc quan trọng (milestones)
   ▼
Bước 5: Hoạch định rủi ro & nguồn lực
   │  Ma trận rủi ro, phân bổ nhân sự/thiết bị
   ▼
Bước 6: Thực thi & Giám sát (Execute & Monitor)
   │  Theo dõi tiến độ thực tế so với kế hoạch (Earned Value Management)
   ▼
Bước 7: Quản lý thay đổi (Change Control)
   │  Đánh giá tác động mọi thay đổi phạm vi/yêu cầu trước khi phê duyệt
   ▼
Bước 8: Kết thúc & Rút kinh nghiệm (Closing & Lessons Learned)
      Nghiệm thu, đánh giá bài học kinh nghiệm cho dự án tương lai
```

### 5.2. Quản lý giá trị thu được (Earned Value Management - EVM)

EVM là kỹ thuật tích hợp đo lường phạm vi, thời gian và chi phí để đánh giá hiệu suất dự án một cách khách quan:

| Chỉ số | Công thức | Ý nghĩa |
|---|---|---|
| PV (Planned Value) | Giá trị kế hoạch tại thời điểm đánh giá | Ngân sách dự kiến đã hoàn thành theo kế hoạch |
| EV (Earned Value) | Giá trị công việc thực sự hoàn thành | Ngân sách tương ứng với công việc đã thực sự làm |
| AC (Actual Cost) | Chi phí thực tế đã chi | Số tiền thực sự đã bỏ ra |
| CPI (Cost Performance Index) | $EV/AC$ | CPI > 1: tiết kiệm chi phí; CPI < 1: vượt ngân sách |
| SPI (Schedule Performance Index) | $EV/PV$ | SPI > 1: nhanh hơn kế hoạch; SPI < 1: chậm tiến độ |

### 5.3. Bảng các sai lầm thường gặp

| Sai lầm | Hậu quả | Cách phòng tránh |
|---|---|---|
| Không xác định rõ đường găng | Tập trung nguồn lực sai chỗ, dự án vẫn trễ dù các việc khác đúng hạn | Sử dụng CPM để xác định và ưu tiên giám sát đường găng |
| Scope creep không kiểm soát | Dự án phình to, trễ hạn, vượt ngân sách nghiêm trọng | Quy trình kiểm soát thay đổi (change control) chặt chẽ |
| Ước lượng thời gian quá lạc quan | Deadline liên tục bị phá vỡ, mất uy tín với khách hàng | Sử dụng PERT với 3 kịch bản, học từ dữ liệu lịch sử |
| Áp dụng Waterfall cho dự án có yêu cầu chưa rõ ràng | Sản phẩm cuối không đáp ứng nhu cầu thực tế | Đánh giá đặc thù dự án để chọn Waterfall/Agile/Hybrid phù hợp |
| Không quản lý xung đột nguồn lực đa dự án | Nhân sự/thiết bị bị phân công trùng lặp, giảm chất lượng | Sử dụng công cụ quản lý đa dự án, xem xét năng lực tổng thể |

---

## VI. Quy mô áp dụng – SME vs Doanh nghiệp lớn

### 6.1. Bảng so sánh mức độ áp dụng

| Thành phần | SME | Doanh nghiệp lớn |
|---|---|---|
| Công cụ lập lịch | Excel/Google Sheets, Trello | MS Project, Primavera P6, Jira Enterprise |
| Phương pháp | Agile đơn giản hoặc Waterfall cơ bản | PMBOK đầy đủ, PMO (Project Management Office) chuyên trách |
| Quản trị rủi ro | Kinh nghiệm, checklist đơn giản | Ma trận rủi ro định lượng, phần mềm quản trị rủi ro chuyên dụng |
| Nhân sự | Kiêm nhiệm (founder, trưởng nhóm) | Project Manager/PMO chuyên trách, chứng chỉ PMP |
| Đo lường hiệu suất | Theo dõi tiến độ đơn giản | EVM đầy đủ (CPI, SPI), dashboard báo cáo tự động |

### 6.2. Chi phí đầu tư theo giai đoạn phát triển

| Giai đoạn | Công cụ quản trị dự án | Chi phí ước tính (VNĐ) |
|---|---|---|
| Khởi nghiệp | Trello, Google Sheets miễn phí | 0 - 5 triệu/năm |
| Tăng trưởng | Asana, Notion, Jira cơ bản | 20 - 100 triệu/năm |
| Mở rộng | MS Project, Jira Enterprise + PMO nhỏ | 200 triệu - 1 tỷ/năm |
| Doanh nghiệp lớn | Primavera P6, PMO đầy đủ, đào tạo PMP | 1 - 10+ tỷ/năm |

### 6.3. Lộ trình khuyến nghị cho SME

1. Bắt đầu với WBS đơn giản cho mọi dự án, dù nhỏ, để tránh bỏ sót công việc.
2. Áp dụng Gantt Chart cơ bản (Excel/Trello) trước khi đầu tư phần mềm phức tạp.
3. Nếu dự án có yêu cầu rõ ràng, ổn định (xây dựng, sản xuất) → áp dụng Waterfall cơ bản với CPM.
4. Nếu dự án có yêu cầu thay đổi liên tục (phần mềm, sản phẩm số) → áp dụng Scrum/Agile đơn giản.
5. Khi quản lý nhiều dự án song song, đầu tư công cụ quản lý đa dự án để tránh xung đột nguồn lực.

### 6.4. Bảng kiểm tự đánh giá năng lực quản trị dự án (Project Management Maturity Checklist)

- [ ] Mọi dự án đều có WBS được lập trước khi bắt đầu triển khai?
- [ ] Đã xác định rõ đường găng (critical path) cho các dự án có nhiều công việc phụ thuộc?
- [ ] Có quy trình kiểm soát thay đổi (change control) chính thức để đánh giá tác động trước khi phê duyệt thay đổi phạm vi?
- [ ] Có công cụ theo dõi tiến độ tập trung khi quản lý nhiều dự án đồng thời?
- [ ] Đội ngũ đã được đào tạo cơ bản về sự khác biệt giữa Waterfall và Agile để chọn phương pháp phù hợp?
- [ ] Có quy trình rút kinh nghiệm (lessons learned) chính thức sau mỗi dự án kết thúc?
- [ ] Đã sử dụng ít nhất một chỉ số định lượng (CPI, SPI, hoặc Velocity) để đánh giá hiệu suất dự án?
- [ ] Có ma trận đánh giá rủi ro được cập nhật định kỳ trong suốt vòng đời dự án?
- [ ] Các bên liên quan (stakeholders) chính đã được xác định và giao tiếp thường xuyên trong suốt dự án?

---

## VII. Công cụ & Templates hỗ trợ

### 7.1. Bảng công cụ phần mềm quản trị dự án

| Công cụ | Chức năng chính | Chi phí ước tính | Phù hợp |
|---|---|---|---|
| Trello | Kanban Board đơn giản | Miễn phí - 5 USD/user/tháng | SME nhỏ, Agile cơ bản |
| Asana, Notion | Quản lý task, timeline cơ bản | Miễn phí - 15 USD/user/tháng | SME vừa |
| Jira | Quản lý Agile/Scrum chuyên sâu | 10-20 USD/user/tháng | Đội phát triển phần mềm |
| Microsoft Project | Gantt Chart, CPM chuyên nghiệp | Vài triệu/license | Dự án xây dựng, kỹ thuật |
| Primavera P6 | Quản lý dự án phức tạp, đa dự án | Hàng chục-trăm triệu | Tập đoàn lớn, dự án hạ tầng |

### 7.2. Template: Bảng tính CPM cơ bản

```
Công việc | Thời gian | Phụ thuộc | ES | EF | LS | LF | Float | Đường găng?
----------|-----------|-----------|----|----|----|----|-------|------------
   A      |           |           |    |    |    |    |       |
   B      |           |           |    |    |    |    |       |
   C      |           |           |    |    |    |    |       |

ES (Early Start) = Max(EF của các công việc trước)
EF (Early Finish) = ES + Thời gian
LF (Late Finish) = Min(LS của các công việc sau)
LS (Late Start) = LF - Thời gian
Float = LS - ES (Float = 0 → nằm trên đường găng)
```

### 7.3. Sơ đồ quyết định chọn phương pháp luận dự án

```
                    Bắt đầu
                       │
        Yêu cầu dự án đã rõ ràng, ít khả năng thay đổi?
                /                          \
              Có                          Không
               │                              │
    Dự án có quy định pháp lý/kỹ         AGILE/SCRUM
    thuật chặt chẽ (xây dựng, y tế)?     (Sprint ngắn, phản
          /            \                  hồi liên tục)
        Có             Không
         │                │
    WATERFALL         HYBRID
    (CPM/PERT,        (Waterfall cho khung
     Gantt Chart)      tổng thể + Agile cho
                       triển khai chi tiết)
```

---

## VIII. Bài tập thực hành

1. Xây dựng WBS chi tiết cho một dự án thực tế (tổ chức sự kiện, ra mắt sản phẩm, xây dựng ứng dụng) với ít nhất 3 cấp phân rã.
2. Vẽ sơ đồ mạng CPM cho một dự án có ít nhất 8 công việc với các mối quan hệ phụ thuộc, xác định đường găng và tổng thời gian dự án.
3. Tính PERT ($t_e$, $\sigma$) cho 5 công việc với 3 ước lượng lạc quan/khả dĩ/bi quan tự giả định.
4. Áp dụng kỹ thuật Crashing để rút ngắn 2 ngày cho dự án ở bài tập 2, xác định công việc nào nên crash để chi phí tăng thêm là thấp nhất.
5. So sánh Waterfall và Agile cho 3 loại dự án khác nhau (xây nhà, phát triển app, tổ chức hội nghị), giải thích phương pháp phù hợp cho từng loại.
6. Thiết kế một Sprint Backlog mẫu cho 1 sprint 2 tuần của một dự án phần mềm giả định.
7. Tính CPI và SPI cho một dự án giả định với dữ liệu PV, EV, AC tự cho, giải thích tình trạng dự án đang vượt/dưới ngân sách và tiến độ.
8. Nghiên cứu case Denver Airport Baggage System, viết phân tích nguyên nhân gốc rễ về quản trị phạm vi và rủi ro.
9. Xây dựng ma trận đánh giá rủi ro cho một dự án thực tế với tối thiểu 8 rủi ro, phân loại theo 4 nhóm và đề xuất chiến lược ứng phó.
10. Thiết kế quy trình quản lý xung đột nguồn lực cho một tổ chức quản lý nhiều dự án đồng thời (như case công ty tổ chức sự kiện).
11. Xây dựng mô hình "Scrum of Scrums" cho một tổ chức giả định có 4 nhóm Scrum song song, xác định tần suất và nội dung họp đồng bộ liên nhóm.
12. Tính Velocity trung bình của một nhóm Scrum giả định qua 5 sprint, dự đoán số sprint còn lại cần thiết để hoàn thành backlog còn lại.

---

## IX. Phụ lục

### 9.1. Bảng thuật ngữ (Glossary)

| Thuật ngữ | Giải thích |
|---|---|
| WBS | Work Breakdown Structure - cơ cấu phân chia công việc |
| CPM | Critical Path Method - phương pháp đường găng |
| PERT | Program Evaluation and Review Technique |
| Float/Slack | Độ trễ cho phép của một công việc không nằm trên đường găng |
| Crashing | Kỹ thuật rút ngắn thời gian dự án bằng cách tăng nguồn lực |
| Fast-tracking | Chạy song song các công việc thường được lên kế hoạch nối tiếp |
| Scope Creep | Hiện tượng phạm vi dự án mở rộng không kiểm soát |
| EVM | Earned Value Management - quản lý giá trị thu được |
| Sprint | Chu kỳ lặp ngắn trong Scrum (1-4 tuần) |
| Product Backlog | Danh sách yêu cầu/tính năng được ưu tiên hoá trong Scrum |
| PMO | Project Management Office - văn phòng quản trị dự án tập trung |
| PPM | Project Portfolio Management - quản trị danh mục dự án |
| Velocity | Tốc độ hoàn thành công việc trung bình mỗi sprint |
| Definition of Done | Tiêu chí thống nhất để xác định một công việc đã thực sự hoàn thành |

### 9.2. Bảng đo lường KPI dự án

| KPI | Công thức | Mục tiêu tham khảo |
|---|---|---|
| CPI (Cost Performance Index) | EV/AC | > 1.0 (tiết kiệm chi phí) |
| SPI (Schedule Performance Index) | EV/PV | > 1.0 (nhanh hơn kế hoạch) |
| Tỷ lệ hoàn thành đúng hạn (On-time completion %) | Số dự án đúng hạn / Tổng số dự án | > 90% |
| Tỷ lệ vượt ngân sách (Budget Overrun %) | (Chi phí thực tế - Ngân sách) / Ngân sách | < 10% |
| Velocity (Agile) | Số story points hoàn thành mỗi sprint | Ổn định qua các sprint |

### 9.3. Sổ tay rủi ro dự án (Risk Register mẫu)

| Rủi ro | Xác suất | Tác động | Biện pháp giảm thiểu |
|---|---|---|---|
| Yêu cầu khách hàng thay đổi liên tục | Cao | Trung bình | Áp dụng Agile, quy trình change control rõ ràng |
| Thành viên chủ chốt nghỉ việc giữa dự án | Trung bình | Cao | Tài liệu hoá kiến thức, đào tạo chéo (cross-training) |
| Ước lượng thời gian/chi phí sai lệch lớn | Trung bình | Cao | Sử dụng PERT, tham khảo dữ liệu dự án tương tự trước đó |
| Xung đột nguồn lực giữa các dự án | Trung bình | Trung bình | Công cụ quản lý đa dự án, họp phân bổ nguồn lực định kỳ |
| Nhà cung cấp/nhà thầu phụ giao chậm | Trung bình | Cao | Hợp đồng ràng buộc SLA, đánh giá NCC trước khi ký kết |
| Phụ thuộc chéo giữa nhiều nhóm Scrum song song | Cao | Trung bình | Áp dụng mô hình Scrum of Scrums, xác định Definition of Done chung |

### 9.4. Bảng tham chiếu nhanh các công thức cốt lõi

| Mục tiêu | Công thức |
|---|---|
| Thời gian PERT | $t_e = (t_o + 4t_m + t_p)/6$ |
| Độ lệch chuẩn công việc | $\sigma = (t_p - t_o)/6$ |
| Chi phí crash mỗi ngày | $(\text{Chi phí crash} - \text{Chi phí thường})/(\text{Thời gian thường} - \text{Thời gian crash})$ |
| CPI | $EV/AC$ |
| SPI | $EV/PV$ |

---

## X. Tài liệu tham khảo

### Sách tham khảo
1. Project Management Institute (2021). *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*. PMI.
2. Kerzner, H. (2017). *Project Management: A Systems Approach to Planning, Scheduling, and Controlling*. Wiley.
3. Schwaber, K. & Sutherland, J. (2020). *The Scrum Guide*. Scrum.org.
4. Meredith, J. R. & Mantel, S. J. (2017). *Project Management: A Managerial Approach*. Wiley.
5. Goldratt, E. M. (1997). *Critical Chain*. North River Press.

### Liên kết nội bộ (Internal Cross-links)
- [01-process-design-analysis.md](./01-process-design-analysis.md) - RACI Matrix và các công cụ quy trình liên quan đến dự án.
- [05-capacity-planning.md](./05-capacity-planning.md) - Hoạch định nguồn lực gắn với quản trị dự án đa nhiệm.
- [07-forecasting.md](./07-forecasting.md) - Ước lượng thời gian/chi phí dự án dựa trên kỹ thuật dự báo.
- [09-theory-of-constraints.md](./09-theory-of-constraints.md) - Nguyên lý nút thắt cổ chai cũng áp dụng cho quản lý đa dự án (Critical Chain Project Management).

### Nguồn học trực tuyến
- PMI (Project Management Institute) - chứng chỉ PMP, CAPM.
- Scrum.org, Scrum Alliance - chứng chỉ CSM (Certified ScrumMaster).
- Coursera: "Project Management Principles and Practices" - University of California, Irvine.
- LinkedIn Learning: "Agile Project Management" - các khoá học thực hành ngắn hạn.

---

## Phụ lục bổ sung: Quản trị dự án trong bối cảnh chuyển đổi số và đa dự án

### A.1. Văn phòng quản trị dự án (Project Management Office - PMO)

PMO là bộ phận tập trung hoá trong doanh nghiệp lớn, chịu trách nhiệm chuẩn hoá quy trình quản trị dự án, đào tạo, giám sát và báo cáo hiệu suất tổng thể của danh mục dự án (project portfolio).

| Loại PMO | Mức độ kiểm soát | Vai trò |
|---|---|---|
| Supportive PMO | Thấp | Cung cấp template, tư vấn, đào tạo |
| Controlling PMO | Trung bình | Yêu cầu tuân thủ quy trình, framework chuẩn |
| Directive PMO | Cao | Trực tiếp quản lý dự án, cung cấp Project Manager |

Việc lựa chọn loại PMO phù hợp phụ thuộc vào văn hoá tổ chức và mức độ trưởng thành trong quản trị dự án - doanh nghiệp mới bắt đầu chuẩn hoá thường khởi đầu với Supportive PMO trước khi chuyển dần sang Controlling hoặc Directive khi quy mô danh mục dự án tăng lên.

### A.2. Quản trị danh mục dự án (Project Portfolio Management - PPM)

Đối với doanh nghiệp lớn triển khai nhiều dự án đồng thời, PPM giúp ưu tiên hoá và phân bổ nguồn lực giữa các dự án dựa trên giá trị chiến lược và rủi ro, thay vì quản lý từng dự án riêng lẻ. Ma trận ưu tiên hoá danh mục dự án thường dựa trên hai trục: Giá trị chiến lược (Strategic Value) và Mức độ khả thi/rủi ro (Feasibility/Risk).

Doanh nghiệp cần định kỳ (thường hàng quý) rà soát lại toàn bộ danh mục dự án đang triển khai để quyết định tiếp tục đầu tư, tạm dừng, hoặc huỷ bỏ các dự án không còn phù hợp với chiến lược tổng thể, tránh tình trạng phân tán nguồn lực cho quá nhiều dự án có giá trị chiến lược thấp.

### A.3. Công nghệ AI hỗ trợ quản trị dự án hiện đại

Các nền tảng quản trị dự án hiện đại (Monday.com, ClickUp, Microsoft Project) đang tích hợp AI để tự động dự đoán rủi ro trễ hạn dựa trên tiến độ lịch sử, đề xuất phân bổ lại nguồn lực tối ưu, và tự động tạo báo cáo tiến độ, giảm đáng kể khối lượng công việc hành chính của Project Manager.

### A.4. Quản trị dự án từ xa và phân tán (Remote/Distributed Project Management)

Xu hướng làm việc từ xa hậu COVID-19 đặt ra thách thức mới cho quản trị dự án: duy trì giao tiếp hiệu quả, theo dõi tiến độ minh bạch khi nhóm không cùng địa điểm. Các thực hành tốt bao gồm: họp đứng hàng ngày qua video call, công cụ cộng tác tài liệu thời gian thực (Google Docs, Notion), và văn hoá minh bạch thông tin (asynchronous communication) để giảm phụ thuộc vào việc phải trực tuyến cùng lúc, đặc biệt quan trọng với các đội nhóm phân tán nhiều múi giờ.

### A.5. Case study bổ sung: Tiki - Quản trị dự án đa nhóm trong phát triển sản phẩm thương mại điện tử

**Bối cảnh**: Tiki là một trong những sàn thương mại điện tử lớn tại Việt Nam, vận hành hàng chục nhóm phát triển sản phẩm song song (nhóm thanh toán, nhóm logistics, nhóm tìm kiếm, nhóm khuyến mãi), mỗi nhóm áp dụng Scrum riêng nhưng phải phối hợp chặt chẽ với nhau.

**Thách thức**: Các tính năng thường phụ thuộc chéo giữa nhiều nhóm (ví dụ: tính năng khuyến mãi mới cần cả nhóm thanh toán và nhóm giao diện người dùng cùng triển khai), gây khó khăn trong việc đồng bộ tiến độ giữa các Sprint của từng nhóm.

**Giải pháp áp dụng**: Áp dụng mô hình "Scrum of Scrums" - mỗi nhóm Scrum cử đại diện tham gia họp đồng bộ liên nhóm hàng tuần để phát hiện sớm các phụ thuộc chéo và xung đột tiến độ. Xây dựng PMO ở mức Controlling để chuẩn hoá quy trình ước lượng story points và định nghĩa "hoàn thành" (Definition of Done) chung giữa các nhóm.

**Kết quả**: Cải thiện đáng kể khả năng phối hợp liên nhóm, giảm tình trạng tính năng bị trễ do chờ đợi nhóm khác hoàn thành phần phụ thuộc.

### A.6. Bảng so sánh nhanh các chỉ số Agile phổ biến

| Chỉ số | Ý nghĩa | Cách sử dụng |
|---|---|---|
| Velocity | Tốc độ hoàn thành công việc trung bình mỗi sprint (story points) | Dự đoán khả năng hoàn thành backlog còn lại |
| Burndown Chart | Biểu đồ thể hiện công việc còn lại theo thời gian trong sprint | Phát hiện sớm nguy cơ không hoàn thành sprint |
| Burnup Chart | Biểu đồ thể hiện công việc đã hoàn thành tích luỹ so với tổng phạm vi | Theo dõi thay đổi phạm vi dự án theo thời gian |
| Cycle Time | Thời gian trung bình từ khi bắt đầu đến khi hoàn thành 1 task | Đánh giá hiệu quả luồng công việc (đặc biệt trong Kanban) |
| Lead Time | Thời gian từ khi yêu cầu được tạo đến khi hoàn thành | Đánh giá tốc độ đáp ứng yêu cầu khách hàng tổng thể |
| Sprint Goal Achievement Rate | Tỷ lệ % sprint đạt được mục tiêu đề ra ban đầu | Đánh giá độ chính xác của việc lập kế hoạch sprint |

### A.7. Ghi chú kết thúc file

File này trình bày các công cụ định lượng cốt lõi của quản trị dự án truyền thống (CPM, PERT, EVM) song song với các phương pháp Agile hiện đại (Scrum, Kanban), phản ánh thực tế rằng nhiều doanh nghiệp hiện nay áp dụng mô hình Hybrid tuỳ theo đặc thù từng loại dự án. Người đọc nên thực hành xây dựng WBS và sơ đồ CPM cho một dự án thực tế của mình để hiểu sâu hơn cách áp dụng lý thuyết vào thực tiễn, đồng thời cân nhắc kỹ đặc thù dự án (mức độ rõ ràng của yêu cầu, quy định pháp lý, tốc độ thay đổi thị trường) trước khi lựa chọn phương pháp luận phù hợp.
