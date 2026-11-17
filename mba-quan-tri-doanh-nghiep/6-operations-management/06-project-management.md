# 06. Quản trị Dự án (Project Management)

> **Mục tiêu**: Giúp chủ SME và người học MBA hiểu bản chất của quản trị dự án (tam giác ràng buộc, WBS, Gantt, CPM/PERT, Crashing, EVM, rủi ro, Agile/Scrum), biết *vì sao* mỗi công thức ra đời và tự tính được lịch trình, xác suất đúng hạn, hiệu suất chi phí của một dự án thực tế.

> File thuộc bộ kiến thức Quản trị Vận hành (Operations Management) - MBA Knowledge Base
> Liên kết: [01-process-design-analysis.md](./01-process-design-analysis.md) | [05-capacity-planning.md](./05-capacity-planning.md) | [07-forecasting.md](./07-forecasting.md)

> **Quy ước nhãn số liệu**: "(giả định minh họa)" = số tự thiết kế để minh họa phép tính; "(ước tính)" = số liệu công khai thường được trích dẫn nhưng tác giả file chưa kiểm chứng được nguồn gốc, người đọc nên đối chiếu trước khi dùng cho mục đích học thuật/chính thức.

---

## I. Khái niệm & Lý thuyết nền tảng

### 1.1. Định nghĩa Dự án và Quản trị Dự án

**Dự án (Project)** là một nỗ lực tạm thời (có thời điểm bắt đầu và kết thúc rõ ràng) nhằm tạo ra một sản phẩm, dịch vụ hoặc kết quả duy nhất, khác biệt với hoạt động vận hành thường xuyên (operations) vốn mang tính lặp lại liên tục.

**Quản trị dự án (Project Management - PM)** là việc áp dụng kiến thức, kỹ năng, công cụ và kỹ thuật vào các hoạt động của dự án nhằm đáp ứng các yêu cầu đã đề ra, trong giới hạn về phạm vi (scope), thời gian (time), chi phí (cost) và chất lượng (quality).

**Vì sao cần một bộ môn riêng cho dự án?** Hoạt động vận hành (ví dụ: pha cà phê mỗi ngày) lặp lại nên có thể tối ưu dần bằng kinh nghiệm. Dự án (ví dụ: fit-out quán cà phê mới) chỉ diễn ra một lần: không có "lần thử trước", mọi sai sót về tiến độ/ngân sách đều phải trả giá thật ngay lập tức. Do đó cần các công cụ *dự báo trước* (CPM/PERT), *đo lường giữa chừng* (EVM) và *kiểm soát thay đổi* thay vì chỉ dựa vào kinh nghiệm.

| Tiêu chí | Dự án (Project) | Vận hành (Operations) |
|---|---|---|
| Tính chất | Tạm thời, có điểm kết thúc | Liên tục, lặp lại |
| Kết quả | Duy nhất (một lần) | Sản phẩm/dịch vụ chuẩn hoá |
| Rủi ro chính | Trễ hạn, vượt ngân sách, sai phạm vi | Biến động chất lượng, công suất |
| Ví dụ | Mở chi nhánh, ra mắt sản phẩm, triển khai ERP | Bán hàng hằng ngày, pha chế, giao hàng |

### 1.2. Nguồn gốc lịch sử của các công cụ (Origin)

Mỗi công cụ trong bài ra đời để giải quyết một "cơn đau" cụ thể của giới quản lý thời đó. Hiểu bối cảnh giúp ta nhớ *bản chất* thay vì học thuộc lòng.

| Công cụ | Ai tạo ra / năm | Bối cảnh & vấn đề cần giải quyết |
|---|---|---|
| Biểu đồ Gantt | Henry Gantt, khoảng 1910-1915 (Hoa Kỳ); trước đó Karol Adamiecki (Ba Lan) có sơ đồ tương tự | Cần nhìn *trực quan* ai làm gì, khi nào trong các xưởng sản xuất, đóng tàu |
| CPM (Critical Path Method) | James Kelley (Remington Rand) và Morgan Walker (DuPont), khoảng 1957 | DuPont cần lập lịch bảo trì nhà máy hoá chất sao cho thời gian dừng máy (mất doanh thu) ngắn nhất; cần biết *việc nào quyết định tổng thời gian* |
| PERT | Hải quân Hoa Kỳ cùng Booz Allen Hamilton và Lockheed, khoảng 1958, cho chương trình tên lửa Polaris | Công việc nghiên cứu - phát triển chưa từng làm, *không thể biết chắc thời gian*, cần mô hình xác suất |
| EVM (Earned Value Management) | Bộ Quốc phòng Hoa Kỳ chuẩn hoá thập niên 1960 (tiêu chí C/SCSC); phương pháp được PMI đưa vào PMBOK | Nhà thầu quốc phòng thường báo "đã chi 50% ngân sách" nhưng không ai biết *đã làm được bao nhiêu % công việc*; cần chỉ số tích hợp tiền - tiến độ - khối lượng |
| PMI và PMBOK | Project Management Institute thành lập 1969; PMBOK Guide xuất bản lần đầu giữa thập niên 1990 | Chuẩn hoá ngôn ngữ và quy trình chung cho nghề quản lý dự án |
| Scrum | Jeff Sutherland và Ken Schwaber giới thiệu chính thức khoảng 1995; ý tưởng "scrum" của Takeuchi và Nonaka (1986) | Dự án phần mềm yêu cầu luôn đổi, Waterfall giao sản phẩm quá muộn mới biết sai |
| Agile Manifesto | 17 nhà phát triển phần mềm, 2001 | Tuyên ngôn ưu tiên con người, sản phẩm chạy được, hợp tác khách hàng, thích ứng thay đổi |

> Lưu ý: các mốc năm trên là mốc thường được trích dẫn trong sách giáo khoa; chênh lệch 1-2 năm giữa các nguồn là bình thường.

### 1.3. Tam giác ràng buộc dự án (Project Triple Constraint / Iron Triangle)

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

**Ví dụ đời thường**: Khách muốn quán cà phê khai trương sớm 10 ngày (Time giảm). Bạn chỉ có 3 lựa chọn: (1) thuê thêm thợ, tăng ca - Cost tăng; (2) bỏ bớt hạng mục như tranh tường, bảng hiệu 3D - Scope giảm; (3) làm ẩu - Quality giảm. Không có lựa chọn "miễn phí".

### 1.4. Vòng đời dự án (Project Life Cycle) theo PMBOK (PMI)

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

### 1.5. Cơ cấu phân chia công việc (Work Breakdown Structure - WBS)

**Vì sao cần WBS?** Lỗi phổ biến nhất của dự án là *bỏ sót công việc* (sau đó phát sinh chi phí) hoặc *giao việc mơ hồ* (không ai chịu trách nhiệm). Không thể ước lượng thời gian, chi phí hay rủi ro cho thứ mà ta chưa liệt kê được. WBS ép người lập kế hoạch chia nhỏ "con voi" thành các gói công việc (work package) đủ nhỏ để ước lượng, giao việc và theo dõi. WBS là nền móng: mọi công cụ sau đó (Gantt, CPM, EVM) đều lấy danh sách công việc từ WBS.

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

**Quy tắc 100% (100% Rule)**: tổng công việc ở mỗi cấp con phải bằng 100% công việc của cấp cha, đảm bảo không bỏ sót và không trùng lặp phạm vi công việc.

**Mẹo thực hành**: một gói công việc tốt thường kéo dài khoảng 8-80 giờ làm việc (quy tắc kinh nghiệm), có một người chịu trách nhiệm, có tiêu chí hoàn thành rõ ràng. Phân rã theo *sản phẩm bàn giao* (deliverable) thay vì theo *động từ hành động* để tránh liệt kê trùng.

### 1.6. Ba phương pháp luận quản trị dự án chính

| Phương pháp | Đặc điểm | Phù hợp |
|---|---|---|
| **Waterfall (Thác nước)** | Tuần tự, từng giai đoạn hoàn thành mới chuyển giai đoạn sau | Dự án có yêu cầu rõ ràng, ít thay đổi (xây dựng, sản xuất) |
| **Agile (Linh hoạt)** | Lặp lại theo chu kỳ ngắn (sprint), phản hồi liên tục, thích ứng thay đổi | Dự án phần mềm, sản phẩm cần đổi mới nhanh, yêu cầu chưa rõ ràng hoàn toàn |
| **Hybrid** | Kết hợp Waterfall cho hoạch định tổng thể + Agile cho triển khai chi tiết | Dự án lớn, phức tạp, cần cả cấu trúc và linh hoạt |

---

## II. Chi tiết từng công cụ và kỹ thuật

### 2.1. Sơ đồ Gantt (Gantt Chart)

**Vấn đề giải quyết**: Bảng danh sách công việc khó cho thấy "tuần này ai đang làm gì, việc nào chồng lên việc nào". Gantt chuyển danh sách đó thành hình ảnh theo trục thời gian để cả người không chuyên (chủ doanh nghiệp, khách hàng) nhìn là hiểu.

Gantt Chart thể hiện các công việc dưới dạng thanh ngang theo trục thời gian, cho thấy thời điểm bắt đầu, kết thúc và mối quan hệ phụ thuộc giữa các công việc.

```
Công việc          T1  T2  T3  T4  T5  T6  T7  T8
Thiết kế UI/UX    ▓▓▓▓▓▓
Phát triển FE           ▓▓▓▓▓▓▓▓
Phát triển BE            ▓▓▓▓▓▓▓▓▓▓
Kiểm thử                          ▓▓▓▓▓
Triển khai                              ▓▓▓
                  └──────────── Milestone: Ra mắt sản phẩm (T8)
```

| Ưu điểm | Hạn chế |
|---|---|
| Trực quan, dễ hiểu cho mọi cấp quản lý, dễ theo dõi tiến độ tổng thể | Không thể hiện rõ công việc nào là "đường găng" quyết định tổng thời gian dự án |
| Dễ lập bằng Excel/Google Sheets/Trello | Khó đọc với dự án hàng trăm công việc phụ thuộc chằng chịt |

**Cách dùng đúng**: Gantt là công cụ *trình bày*, CPM là công cụ *phân tích*. Cách làm tốt: tính CPM trước để biết đường găng, rồi vẽ Gantt và tô màu nổi bật các thanh trên đường găng.

### 2.2. Phương pháp Đường Găng (Critical Path Method - CPM)

**Vì sao ra đời và logic cốt lõi?** Năm 1957, DuPont cần dừng nhà máy để bảo trì với thời gian ngắn nhất (mỗi ngày dừng là mất doanh thu lớn). Câu hỏi then chốt: *trong hàng trăm việc, việc nào mà chỉ cần chậm một ngày là cả dự án chậm một ngày?* Lý lẽ: các việc chạy song song thì việc chậm nhất quyết định thời điểm xong của cả nhóm; vì vậy tổng thời gian dự án chính bằng **chuỗi phụ thuộc dài nhất** từ đầu đến cuối. Chuỗi đó là đường găng; các việc ngoài đường găng có "độ trễ cho phép" (float) vì chúng xong sớm hơn mức cần thiết.

Bất kỳ sự chậm trễ nào trên đường găng đều trực tiếp làm chậm toàn bộ dự án. Do đó nhà quản lý dồn sự chú ý và nguồn lực vào đường găng, còn việc ngoài đường găng thì được linh hoạt.

**Các bước thực hiện CPM**:

1. Liệt kê tất cả công việc, thời gian ước tính, và mối quan hệ phụ thuộc (predecessor).
2. Vẽ sơ đồ mạng lưới (network diagram) thể hiện trình tự công việc.
3. **Forward Pass** (đi xuôi): tính thời gian sớm nhất có thể bắt đầu/kết thúc.
4. **Backward Pass** (đi ngược): tính thời gian muộn nhất có thể bắt đầu/kết thúc mà không làm trễ dự án.
5. Tính độ trễ cho phép (Float/Slack).
6. Xác định đường găng: chuỗi công việc có Float = 0.

**Công thức**:

$$ES_j = \max_{i \in \text{trước } j}(EF_i), \qquad EF_j = ES_j + d_j$$

$$LF_i = \min_{j \in \text{sau } i}(LS_j), \qquad LS_i = LF_i - d_i$$

$$\text{Float}_i = LS_i - ES_i = LF_i - EF_i$$

Trong đó: $d$ là thời lượng công việc; $ES$ (Early Start) là thời điểm bắt đầu sớm nhất; $EF$ (Early Finish) là thời điểm kết thúc sớm nhất; $LS$ (Late Start) và $LF$ (Late Finish) là thời điểm bắt đầu/kết thúc muộn nhất mà dự án không bị trễ.

Giải thích: ES lấy **max** vì một việc chỉ bắt đầu được khi *tất cả* việc trước đã xong (chờ việc chậm nhất). LF lấy **min** vì một việc phải xong kịp trước khi *việc sau nào đến sớm nhất* cần bắt đầu.

#### 2.2.1. Ví dụ từng bước: mạng lưới 5 công việc

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
```

**Bước 1: Forward Pass**

| Việc | ES | EF = ES + d | Ghi chú |
|---|---|---|---|
| A | 0 | 0 + 3 = 3 | Không có việc trước |
| B | 0 | 0 + 5 = 5 | Không có việc trước |
| C | 3 | 3 + 4 = 7 | Chờ A xong |
| D | 5 | 5 + 6 = 11 | Chờ B xong |
| E | max(7, 11) = 11 | 11 + 2 = 13 | Phải chờ cả C và D, D xong muộn hơn |

Tổng thời gian dự án tối thiểu = **13 ngày**.

**Bước 2: Backward Pass** (bắt đầu từ LF của E = 13)

| Việc | LF | LS = LF - d | Float = LS - ES |
|---|---|---|---|
| E | 13 | 11 | 11 - 11 = 0 |
| D | LS của E = 11 | 11 - 6 = 5 | 5 - 5 = 0 |
| C | LS của E = 11 | 11 - 4 = 7 | 7 - 3 = 4 |
| B | LS của D = 5 | 5 - 5 = 0 | 0 - 0 = 0 |
| A | LS của C = 7 | 7 - 3 = 4 | 4 - 0 = 4 |

**Bước 3: Kết luận**: Đường găng là **B → D → E** (Float = 0), dài 5 + 6 + 2 = 13 ngày. Đường còn lại A → C → E dài 3 + 4 + 2 = 9 ngày, vì vậy A và C đều có Float = 13 - 9 = 4 ngày (có thể trễ tối đa 4 ngày mà không ảnh hưởng dự án; lưu ý đây là float *dùng chung* của cả chuỗi A-C, không phải mỗi việc 4 ngày riêng biệt).

**Ý nghĩa kinh doanh**: Nếu quản lý dồn tiền thuê thêm người cho C (để rút ngắn 2 ngày), dự án vẫn xong sau 13 ngày - tiền bị lãng phí. Ngược lại, tiết kiệm 1 ngày ở D sẽ giảm ngay tổng thời gian xuống 12 ngày.

### 2.3. Kỹ thuật đánh giá và xem xét chương trình (PERT)

**Vì sao ra đời?** CPM giả định mỗi công việc có thời gian chắc chắn - hợp lý với bảo trì nhà máy (đã làm nhiều lần). Nhưng với chương trình tên lửa Polaris (1958), nhiều việc chưa ai làm, kỹ sư chỉ nói được "nhanh nhất 4 ngày, thường 6 ngày, tệ nhất 14 ngày". PERT dùng ba ước lượng, rồi lấy trung bình có trọng số.

**Vì sao công thức là $(t_o + 4t_m + t_p)/6$?** PERT giả định thời gian công việc theo phân phối Beta. Ước lượng trung bình xấp xỉ bằng cách cho khả dĩ nhất trọng số 4 và hai đầu mút trọng số 1 mỗi bên (tổng trọng số 6). Còn $\sigma = (t_p - t_o)/6$ dựa trên quan sát rằng gần như toàn bộ phân phối (khoảng ±3σ) nằm giữa mức lạc quan và bi quan, tức khoảng cách này xấp xỉ 6σ.

$$t_e = \frac{t_o + 4t_m + t_p}{6}$$

Trong đó:
- $t_o$ = Thời gian lạc quan (Optimistic time) - nếu mọi thứ diễn ra thuận lợi nhất
- $t_m$ = Thời gian khả dĩ nhất (Most likely time)
- $t_p$ = Thời gian bi quan (Pessimistic time) - nếu gặp nhiều trở ngại nhất

**Độ lệch chuẩn của mỗi công việc** (đo lường độ bất định):

$$\sigma = \frac{t_p - t_o}{6}, \qquad \text{Phương sai} = \sigma^2$$

**Độ lệch chuẩn của toàn dự án** (phương sai cộng dồn trên đường găng, vì các công việc độc lập):

$$\sigma_{project} = \sqrt{\sum \sigma_i^2 \;(\text{các việc trên đường găng})}$$

**Xác suất hoàn thành trước hạn $D$**:

$$z = \frac{D - T_e}{\sigma_{project}}, \qquad P(\text{xong trước } D) = \Phi(z)$$

Trong đó $T_e$ là tổng thời gian kỳ vọng của đường găng, $\Phi(z)$ là hàm phân phối chuẩn tích lũy (tra bảng Z hoặc dùng `NORM.S.DIST(z, TRUE)` trong Excel). Cơ sở: theo định lý giới hạn trung tâm, tổng nhiều thời gian độc lập xấp xỉ phân phối chuẩn.

**Ví dụ**: Một công việc có $t_o = 4$ ngày, $t_m = 6$ ngày, $t_p = 14$ ngày.

$$t_e = \frac{4 + 4(6) + 14}{6} = \frac{4+24+14}{6} = \frac{42}{6} = 7 \text{ ngày}$$

$$\sigma = \frac{14-4}{6} = 1{,}67 \text{ ngày}$$

Nhận xét: $t_e = 7$ lớn hơn $t_m = 6$ vì phân phối lệch phải (kịch bản xấu "kéo dài" nhiều hơn kịch bản tốt "rút ngắn"). Đây là đặc điểm thực tế: việc chậm thường chậm nhiều, việc nhanh chỉ nhanh một chút.

**Hạn chế cần biết**: (1) PERT chỉ tính phương sai đường găng nên đánh giá thấp rủi ro khi có nhiều đường gần găng (hiện tượng "merge bias"); (2) ước lượng ba điểm vẫn chủ quan; (3) giả định độc lập giữa các việc không phải lúc nào cũng đúng. Ví dụ tính đầy đủ nằm ở case SME mục 3.7.

### 2.4. Rút ngắn thời gian dự án: Crashing và Fast-tracking

**Vấn đề giải quyết**: Khách hàng hoặc cơ hội thị trường đòi xong sớm hơn lịch CPM. Hai kỹ thuật chính:

| Kỹ thuật | Bản chất | Chi phí | Rủi ro |
|---|---|---|---|
| **Crashing** | Thêm nguồn lực (nhân công, tăng ca, thiết bị) để rút ngắn thời lượng việc *trên đường găng* | Tăng chi phí trực tiếp | Chi phí tăng, lợi ích giảm dần |
| **Fast-tracking** | Chạy song song những việc vốn nối tiếp (ví dụ bắt đầu thi công khi bản vẽ mới duyệt 70%) | Thường ít tốn tiền trực tiếp | Phải làm lại (rework) nếu việc trước thay đổi |

**Vì sao chỉ crash việc trên đường găng?** Rút ngắn việc ngoài đường găng không giảm tổng thời gian (xem ví dụ C ở mục 2.2.1), nên là chi tiêu vô ích.

$$\text{Chi phí crash mỗi ngày} = \frac{\text{Chi phí crash} - \text{Chi phí bình thường}}{\text{Thời gian bình thường} - \text{Thời gian crash}}$$

Giải thích: đây là *chi phí biên* để mua thêm 1 ngày. So sánh chi phí biên này với lợi ích biên của việc xong sớm (tiền phạt trễ hạn, doanh thu mất đi mỗi ngày chưa khai trương) để quyết định có crash tiếp hay không - cùng logic cận biên (marginal analysis) trong kinh tế học.

**Thuật toán crash tối thiểu chi phí**:
1. Xác định đường găng và chi phí crash/ngày của từng việc trên đường găng.
2. Chọn việc có chi phí/ngày thấp nhất (và còn có thể rút ngắn) để crash 1 ngày.
3. Cập nhật lịch, kiểm tra xem có xuất hiện đường găng song song mới hay không. Nếu có, phải rút ngắn đồng thời trên mọi đường găng.
4. Lặp lại đến khi đạt mục tiêu hoặc khi chi phí crash/ngày vượt lợi ích/ngày.

Ví dụ tính toán đầy đủ: mục 3.7.6 (case SME) và bài tập số 4 (mục VI).

### 2.5. Quản lý giá trị thu được (Earned Value Management - EVM)

**Vì sao ra đời?** Câu hỏi "đã chi 50% ngân sách thì dự án ổn không?" không trả lời được nếu chỉ nhìn tiền chi. Chi 50% mà mới làm xong 30% công việc là thảm họa; chi 50% mà làm xong 70% là rất tốt. EVM giải bằng cách *quy đổi tiến độ công việc thực tế ra tiền* (theo ngân sách kế hoạch), rồi so sánh với kế hoạch và chi phí thực tế - đo được cả chi phí lẫn tiến độ bằng một thước chung là tiền.

**Ba đại lượng nền tảng** (tại một thời điểm báo cáo):

| Đại lượng | Định nghĩa | Câu hỏi trả lời |
|---|---|---|
| PV (Planned Value) | Ngân sách kế hoạch của phần việc *lẽ ra phải xong* đến thời điểm này | Theo kế hoạch, ta nên làm được bao nhiêu? |
| EV (Earned Value) | Ngân sách kế hoạch của phần việc *thực sự đã xong* | Thực tế đã làm được bao nhiêu (tính theo giá trị)? |
| AC (Actual Cost) | Chi phí thực tế đã chi | Ta đã tốn bao nhiêu tiền? |

**Các chỉ số phái sinh**:

$$CV = EV - AC, \qquad SV = EV - PV$$

$$CPI = \frac{EV}{AC}, \qquad SPI = \frac{EV}{PV}$$

| Chỉ số | Ý nghĩa |
|---|---|
| CV (Cost Variance) | Âm: vượt chi phí; Dương: tiết kiệm (đơn vị tiền) |
| SV (Schedule Variance) | Âm: chậm tiến độ; Dương: nhanh hơn kế hoạch (đơn vị tiền) |
| CPI | Mỗi 1 đồng chi tạo ra bao nhiêu đồng giá trị. CPI > 1: tiết kiệm; CPI < 1: vượt ngân sách |
| SPI | Tốc độ thực hiện so với kế hoạch. SPI > 1: nhanh hơn; SPI < 1: chậm |

**Dự báo hoàn thành**:

$$EAC = \frac{BAC}{CPI} \quad (\text{nếu hiệu suất chi phí hiện tại kéo dài đến hết dự án})$$

$$EAC = AC + (BAC - EV) \quad (\text{nếu sai lệch chỉ là sự cố một lần, phần còn lại đúng kế hoạch})$$

$$ETC = EAC - AC, \qquad VAC = BAC - EAC$$

$$TCPI = \frac{BAC - EV}{BAC - AC}$$

Trong đó: BAC (Budget at Completion) là tổng ngân sách kế hoạch cả dự án; EAC (Estimate at Completion) là tổng chi phí dự báo; ETC (Estimate to Complete) là chi phí dự báo còn phải chi; VAC (Variance at Completion) là chênh lệch dự báo; TCPI (To-Complete Performance Index) là hiệu suất cần đạt ở phần việc còn lại để kịp ngân sách BAC (TCPI > 1: phải làm tốt hơn đến nay, khó khăn).

Ví dụ đầy đủ với số liệu: mục 3.7.7 (case SME) và bài tập số 5.

### 2.6. Quản trị rủi ro dự án (Project Risk Management)

**Vấn đề giải quyết**: Dự án luôn có điều bất ngờ. Quản trị rủi ro không loại bỏ bất ngờ mà *nghĩ trước* và *chuẩn bị tiền, thời gian dự phòng* đúng chỗ thay vì xử lý hoảng loạn.

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

**Định lượng bằng Giá trị tiền tệ kỳ vọng (EMV - Expected Monetary Value)**:

$$EMV = P \times I$$

Trong đó $P$ là xác suất xảy ra (0-1) và $I$ là thiệt hại bằng tiền nếu xảy ra. Tổng EMV các rủi ro là cơ sở hợp lý để lập **quỹ dự phòng (contingency reserve)**. Ví dụ: rủi ro "máy nhập khẩu về trễ" xác suất 30%, thiệt hại 45 triệu có EMV = 0,3 x 45 = 13,5 triệu.

**4 chiến lược ứng phó rủi ro (Risk Response Strategies)**:
1. **Né tránh (Avoid)**: thay đổi kế hoạch để loại bỏ hoàn toàn rủi ro.
2. **Giảm thiểu (Mitigate)**: giảm xác suất hoặc tác động của rủi ro.
3. **Chuyển giao (Transfer)**: chuyển rủi ro cho bên thứ ba (bảo hiểm, hợp đồng thầu phụ).
4. **Chấp nhận (Accept)**: chấp nhận rủi ro nếu chi phí xử lý cao hơn tác động tiềm tàng.

### 2.7. Quản lý Agile, Scrum và Kanban

**Vì sao có Agile?** Waterfall giả định ta biết rõ yêu cầu từ đầu. Với phần mềm, sản phẩm số, khách hàng thường chỉ biết mình muốn gì *sau khi nhìn thấy sản phẩm thật*. Giao sản phẩm sau 10 tháng mới biết sai là quá đắt. Agile chia nhỏ thành chu kỳ ngắn, giao bản chạy được mỗi chu kỳ để nhận phản hồi sớm, nên chi phí sai sót nhỏ.

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

**So sánh Scrum vs Kanban**:

| Tiêu chí | Scrum | Kanban |
|---|---|---|
| Nhịp độ | Theo Sprint cố định (time-boxed) | Luồng liên tục (continuous flow) |
| Vai trò | Có vai trò cố định (PO, SM, Team) | Không yêu cầu vai trò cố định |
| Thay đổi trong chu kỳ | Hạn chế thay đổi trong Sprint đang chạy | Có thể thay đổi ưu tiên bất kỳ lúc nào |
| Công cụ trực quan | Sprint Backlog, Burndown Chart | Kanban Board với giới hạn WIP (Work In Progress) |
| Phù hợp | Đội nhóm phát triển sản phẩm có chu kỳ rõ ràng | Đội vận hành/hỗ trợ có luồng công việc liên tục |

**Các chỉ số Agile phổ biến**:

| Chỉ số | Ý nghĩa | Cách sử dụng |
|---|---|---|
| Velocity | Tốc độ hoàn thành công việc trung bình mỗi sprint (story points) | Dự đoán khả năng hoàn thành backlog còn lại |
| Burndown Chart | Biểu đồ công việc còn lại theo thời gian trong sprint | Phát hiện sớm nguy cơ không hoàn thành sprint |
| Burnup Chart | Biểu đồ công việc đã hoàn thành tích luỹ so với tổng phạm vi | Theo dõi thay đổi phạm vi dự án theo thời gian |
| Cycle Time | Thời gian trung bình từ khi bắt đầu đến khi hoàn thành 1 task | Đánh giá hiệu quả luồng công việc (đặc biệt Kanban) |
| Lead Time | Thời gian từ khi yêu cầu được tạo đến khi hoàn thành | Đánh giá tốc độ đáp ứng yêu cầu khách hàng |
| Sprint Goal Achievement Rate | Tỷ lệ % sprint đạt mục tiêu ban đầu | Đánh giá độ chính xác của việc lập kế hoạch sprint |

**Công thức dự báo bằng Velocity**:

$$\text{Số sprint còn lại} = \frac{\text{Story points còn lại trong backlog}}{\text{Velocity trung bình}}$$

### 2.8. So sánh Waterfall vs Agile và ưu nhược điểm của CPM/PERT

| Tiêu chí | Waterfall | Agile |
|---|---|---|
| Yêu cầu dự án | Cần rõ ràng ngay từ đầu | Có thể thay đổi, làm rõ dần |
| Khả năng thích ứng thay đổi | Thấp, chi phí thay đổi cao ở giai đoạn sau | Cao, thay đổi được tích hợp mỗi sprint |
| Khả năng dự đoán ngân sách/thời gian | Cao (rõ ràng từ đầu) | Thấp hơn (linh hoạt theo tiến độ thực tế) |
| Sự tham gia của khách hàng | Chủ yếu đầu và cuối dự án | Liên tục xuyên suốt dự án |
| Rủi ro chính | Phát hiện sai sót muộn, chi phí sửa cao | Có thể thiếu tầm nhìn tổng thể dài hạn nếu quản lý kém |
| Phù hợp | Xây dựng, sản xuất, dự án có quy định pháp lý chặt | Phát triển phần mềm, sản phẩm số, startup |

| Khía cạnh | Ưu điểm | Nhược điểm |
|---|---|---|
| CPM | Xác định rõ đường găng, tập trung nguồn lực đúng chỗ | Giả định thời gian công việc cố định, không xử lý bất định |
| PERT | Xử lý được bất định, tính xác suất hoàn thành | Phức tạp hơn, cần ước lượng 3 kịch bản cho mỗi công việc |
| Cả hai | Cung cấp cơ sở khoa học cho lập lịch và phân bổ nguồn lực | Không phản ánh tốt dự án có phạm vi thay đổi liên tục (phù hợp Agile hơn) |

### 2.9. Quản trị đa dự án: PMO, PPM, AI và làm việc từ xa

#### 2.9.1. Văn phòng quản trị dự án (Project Management Office - PMO)

PMO là bộ phận tập trung hoá trong doanh nghiệp lớn, chịu trách nhiệm chuẩn hoá quy trình quản trị dự án, đào tạo, giám sát và báo cáo hiệu suất tổng thể của danh mục dự án.

| Loại PMO | Mức độ kiểm soát | Vai trò |
|---|---|---|
| Supportive PMO | Thấp | Cung cấp template, tư vấn, đào tạo |
| Controlling PMO | Trung bình | Yêu cầu tuân thủ quy trình, framework chuẩn |
| Directive PMO | Cao | Trực tiếp quản lý dự án, cung cấp Project Manager |

Doanh nghiệp mới bắt đầu chuẩn hoá thường khởi đầu với Supportive PMO, rồi chuyển dần sang Controlling hoặc Directive khi quy mô danh mục dự án tăng lên.

#### 2.9.2. Quản trị danh mục dự án (Project Portfolio Management - PPM)

Với doanh nghiệp triển khai nhiều dự án đồng thời, PPM giúp ưu tiên hoá và phân bổ nguồn lực giữa các dự án dựa trên giá trị chiến lược và rủi ro, thay vì quản lý từng dự án riêng lẻ. Ma trận ưu tiên dựa trên hai trục: Giá trị chiến lược (Strategic Value) và Mức độ khả thi/rủi ro (Feasibility/Risk). Định kỳ (thường hàng quý) cần rà soát để quyết định tiếp tục, tạm dừng hoặc huỷ dự án không còn phù hợp chiến lược, tránh phân tán nguồn lực.

#### 2.9.3. Công nghệ AI hỗ trợ quản trị dự án

Các nền tảng như Monday.com, ClickUp, Microsoft Project đang tích hợp AI để dự đoán rủi ro trễ hạn dựa trên tiến độ lịch sử, đề xuất phân bổ lại nguồn lực và tự tạo báo cáo tiến độ, giảm khối lượng công việc hành chính của Project Manager. Lưu ý: AI hỗ trợ ước lượng, nhưng trách nhiệm quyết định vẫn thuộc về người quản lý.

#### 2.9.4. Quản trị dự án từ xa và phân tán

Xu hướng làm việc từ xa hậu COVID-19 đặt ra thách thức: duy trì giao tiếp hiệu quả, theo dõi tiến độ minh bạch khi nhóm không cùng địa điểm. Thực hành tốt: họp đứng hằng ngày qua video, công cụ cộng tác tài liệu thời gian thực (Google Docs, Notion), văn hoá minh bạch thông tin và giao tiếp bất đồng bộ (asynchronous communication) để giảm phụ thuộc vào việc phải trực tuyến cùng lúc, đặc biệt với nhóm nhiều múi giờ.

---

## III. Case Studies thực tế

> Các case 3.1 đến 3.3 dùng sự kiện công khai; số liệu thực được đánh dấu "(ước tính)" và phần minh họa tính toán dùng số "(giả định minh họa)". Case 3.7 là case SME hoàn toàn tự thiết kế.

### 3.1. Case quốc tế thành công: Boeing 777 - Quản trị dự án phức tạp bằng thiết kế số và nhóm liên chức năng

#### 3.1.1. Bối cảnh

Boeing 777 (phát triển đầu thập niên 1990, chuyến bay đầu tiên năm 1994, vào khai thác thương mại năm 1995) là dự án kỹ thuật cực kỳ phức tạp: phối hợp hàng nghìn kỹ sư và nhiều nhà cung cấp, với số chi tiết thường được nhắc đến ở mức hàng triệu (ước tính). Các dự án máy bay trước đó của Boeing và ngành hàng không nói chung thường chậm tiến độ và phải làm lại nhiều do các chi tiết lắp không khớp khi ráp thử.

#### 3.1.2. Những gì đã làm (theo các tài liệu giảng dạy phổ biến)

- **Thiết kế số toàn phần (paperless design)** bằng phần mềm CAD 3D (hệ thống CATIA): các kỹ sư kiểm tra va chạm giữa chi tiết trên máy tính trước khi chế tạo.
- **Nhóm thiết kế - chế tạo liên chức năng ("Working Together")**: kỹ sư thiết kế, sản xuất, nhà cung cấp và cả hãng hàng không khách hàng ngồi chung nhóm, thay vì chuyển giao tuần tự.
- **Lịch dự án dạng mạng lưới phụ thuộc**: theo dõi liên tục các việc găng để cảnh báo sớm.

#### 3.1.3. Phân tích: vì sao cách làm này hiệu quả? (minh họa bằng chi phí thay đổi)

Quy tắc kinh nghiệm trong kỹ thuật: chi phí sửa lỗi tăng rất nhanh theo giai đoạn phát hiện. Giả sử (giả định minh họa) một lỗi lắp ghép nếu phát hiện lúc thiết kế tốn 1 đơn vị chi phí, lúc chế tạo thử tốn 10 đơn vị, lúc ráp thực tế tốn 100 đơn vị.

| Phát hiện ở giai đoạn | Chi phí tương đối (giả định) | Với 1.000 lỗi tiềm ẩn, nếu phát hiện toàn bộ ở giai đoạn này |
|---|---|---|
| Thiết kế (kiểm tra 3D) | 1 | 1.000 x 1 = 1.000 đơn vị |
| Chế tạo thử | 10 | 1.000 x 10 = 10.000 đơn vị |
| Ráp thực tế | 100 | 1.000 x 100 = 100.000 đơn vị |

Nếu nhờ 3D CAD, giả sử 80% lỗi bị bắt ngay ở giai đoạn thiết kế, 15% ở chế tạo thử, 5% ở ráp thực tế: chi phí = 800 x 1 + 150 x 10 + 50 x 100 = 800 + 1.500 + 5.000 = 7.300 đơn vị, chỉ bằng 7,3% so với kịch bản phát hiện hết ở ráp thực tế (100.000). Đây là lý do cốt lõi: **đầu tư vào giai đoạn hoạch định và kiểm tra sớm có lợi suất cao nhất** (khớp với biểu đồ chi phí thay đổi ở mục 1.4).

#### 3.1.4. Kết quả

Dự án thường được nhắc đến như một ví dụ hiếm hoi về dự án máy bay lớn đạt mốc tiến độ cam kết (so sánh với các trường hợp chậm trễ nghiêm trọng như Boeing 787 ở file 03; thông tin mức ngân sách cụ thể: chưa kiểm chứng).

#### 3.1.5. Bài học cho người quản lý

1. Phát hiện xung đột sớm (ảo hoá, mô phỏng) rẻ hơn gấp nhiều lần so với phát hiện muộn.
2. Phá "tường ngăn" giữa các chức năng giảm số lần chuyển giao có sai sót.
3. Đường găng chỉ có ý nghĩa khi cập nhật liên tục; lịch tĩnh nhanh chóng lỗi thời.

### 3.2. Case Việt Nam lớn: VinFast - Xây dựng nhà máy ô tô thần tốc bằng Fast-tracking và Crashing

#### 3.2.1. Bối cảnh

VinFast xây dựng tổ hợp nhà máy sản xuất ô tô tại Hải Phòng trong khoảng 21 tháng (khởi công 2017, hoàn thành giữa năm 2019, theo thông tin công khai phổ biến), tốc độ được xem là rất nhanh so với thông lệ ngành (thường nhiều năm). Chi tiết ngân sách và lịch nội bộ không được công bố, nên phần phân tích dưới đây dùng **mô hình rút gọn (giả định minh họa)** để làm rõ cơ chế, không phải số liệu thật của VinFast.

#### 3.2.2. Cơ chế áp dụng

Kết hợp hoạch định tổng thể kiểu Waterfall (nhiều ràng buộc pháp lý, kỹ thuật xây dựng) với chạy song song nhiều hạng mục (fast-tracking) và dồn nguồn lực lớn để "crash" các việc găng.

#### 3.2.3. Mô hình tính toán rút gọn (giả định minh họa)

Giả sử dự án gồm 4 hạng mục tuần tự: Thiết kế (6 tháng) - Móng và kết cấu (5 tháng) - Xây dựng nhà xưởng (8 tháng) - Lắp thiết bị (7 tháng).

**Lịch tuần tự (Waterfall thuần)**: 6 + 5 + 8 + 7 = **26 tháng**.

**Lịch fast-tracking**: cho phép chồng lấn: móng bắt đầu khi thiết kế còn 2 tháng cuối; xây dựng bắt đầu khi móng còn 3 tháng cuối; lắp thiết bị bắt đầu khi xây dựng còn 3 tháng cuối.

| Hạng mục | Bắt đầu (tháng) | Thời lượng | Kết thúc (tháng) |
|---|---|---|---|
| Thiết kế | 0 | 6 | 6 |
| Móng và kết cấu | 6 - 2 = 4 | 5 | 9 |
| Xây dựng nhà xưởng | 9 - 3 = 6 | 8 | 14 |
| Lắp thiết bị | 14 - 3 = 11 | 7 | 18 |

Tổng thời gian = **18 tháng**, rút ngắn 26 - 18 = 8 tháng, tức 8/26 = **30,8%**. (Tương đương công thức: 6 + (5-2) + (8-3) + (7-3) = 6 + 3 + 5 + 4 = 18.)

#### 3.2.4. Diễn giải: cái giá phải trả

- Chồng lấn nghĩa là bắt đầu việc sau khi *thông tin chưa hoàn chỉnh*: nếu thiết kế thay đổi, phần móng đã đổ phải sửa (rework).
- Crashing đòi nguồn lực lớn (nhiều đội thi công, tăng ca): chi phí biên tăng. Kỹ thuật này chỉ hợp lý khi *giá trị của việc ra thị trường sớm lớn hơn chi phí tăng thêm* - ví dụ lợi thế tiên phong của một thương hiệu ô tô mới.

#### 3.2.5. Bài học

| Bài học | Giải thích |
|---|---|
| Rút ngắn mạnh cần nguồn lực mạnh | Phù hợp tập đoàn có vốn lớn; SME cần cân nhắc chi phí biên |
| Fast-tracking đòi quản lý giao diện chặt | Mỗi điểm chồng lấn là một điểm rủi ro làm lại |
| Mục tiêu thời gian phải gắn với lợi ích kinh doanh | Nếu ngày sớm không tạo doanh thu, không nên crash |

### 3.3. Case quốc tế thất bại: Hệ thống xử lý hành lý Sân bay Quốc tế Denver

#### 3.3.1. Bối cảnh

Sân bay quốc tế Denver (Hoa Kỳ, thập niên 1990) triển khai hệ thống hành lý tự động quy mô chưa từng có: xe tự hành chở hành lý đi khắp các nhà ga. Dự án thường được trích dẫn là case kinh điển về thất bại quản trị dự án. Theo số liệu hay được nhắc (ước tính): sân bay khai trương trễ khoảng 16 tháng so với kế hoạch (dự kiến cuối 1993, mở đầu 1995) và chi phí phát sinh thêm khoảng 560 triệu USD.

#### 3.3.2. Phân tích nguyên nhân (theo từng kỹ thuật trong bài)

| Nguyên nhân | Công cụ lẽ ra phải dùng | Phân tích |
|---|---|---|
| Phạm vi liên tục mở rộng (scope creep): ví dụ mở rộng hệ thống sang toàn bộ các nhà ga sau khi dự án đã bắt đầu | Quy trình kiểm soát thay đổi (change control) | Mỗi thay đổi lớn đều cần đánh giá tác động đến tiến độ, chi phí trước khi duyệt. Ở đây thay đổi được chấp nhận mà không điều chỉnh lịch |
| Công nghệ tự động hoá chưa từng làm ở quy mô này | Quản trị rủi ro, PERT (ba điểm ước lượng) | Độ bất định rất cao nhưng lịch được lập như việc đã quen thuộc; thời lượng bi quan lẽ ra phải rất xa thời lượng khả dĩ |
| Phối hợp yếu giữa nhà thầu, bên liên quan | Quản lý bên liên quan (stakeholders), họp phối hợp định kỳ | Hệ thống hành lý phải tích hợp với thiết kế nhà ga; thiết kế nhà ga đã xây dựng thì khó sửa |
| Ép tiến độ trong khi chưa kiểm thử | Giai đoạn thử nghiệm trong WBS | Bỏ qua thời gian thử nghiệm tích hợp là tiết kiệm giả |

#### 3.3.3. Minh họa tác động của sự chậm trễ (giả định minh họa)

Báo cáo công khai thường nhắc rằng sân bay mất khoảng 1 triệu USD/ngày chi phí lãi vay và vận hành chưa có doanh thu trong thời gian chậm trễ (ước tính). Với 16 tháng, xấp xỉ 16 x 30 = 480 ngày: 480 x 1 triệu USD ≈ **480 triệu USD**, cùng bậc độ lớn với mức vượt chi phí ~560 triệu USD được trích dẫn. Phép tính cho thấy: **mỗi ngày trễ là một khoản chi phí cố định**, nên chi phí cơ hội của chậm trễ có thể lớn hơn chi phí nguồn lực để tránh nó (liên hệ logic crashing ở mục 2.4).

#### 3.3.4. Bài học

1. Không để phạm vi tự "phình" mà không điều chỉnh lịch và ngân sách tương ứng.
2. Với công nghệ mới, phải dùng thời lượng bi quan và có phương án dự phòng (ví dụ hệ thống hành lý thủ công).
3. Thử nghiệm tích hợp sớm; không ép khai trương khi hệ thống chưa ổn định.

### 3.4. Case SME Việt Nam (khởi nghiệp công nghệ): Chuyển từ Waterfall sang Scrum

> Toàn bộ số liệu trong case này là **giả định minh họa**.

#### 3.4.1. Bối cảnh

Startup công nghệ 15 người tại Hà Nội phát triển ứng dụng đặt đồ ăn. Ban đầu theo Waterfall: kế hoạch 6 tháng, thực tế mất 10 tháng do khách hàng thí điểm liên tục đổi yêu cầu sau khi thấy sản phẩm thật. Mức trễ: (10 - 6)/6 = **66,7%**.

#### 3.4.2. Giải pháp

Chuyển sang Scrum: Sprint 2 tuần; founder là Product Owner làm việc trực tiếp với khách hàng thí điểm; demo cuối mỗi sprint. Product Backlog ban đầu: 200 story points.

#### 3.4.3. Số liệu thực hiện và dự báo bằng Velocity

| Sprint | Story points hoàn thành |
|---|---|
| 1 | 14 |
| 2 | 18 |
| 3 | 21 |
| 4 | 23 |

**Bước 1**: Velocity trung bình 4 sprint đầu = (14 + 18 + 21 + 23)/4 = 76/4 = **19 điểm/sprint**.

**Bước 2**: Backlog còn lại = 200 - 76 = **124 điểm**.

**Bước 3**: Số sprint còn lại = 124/19 = 6,5, làm tròn **7 sprint** (tổng 11 sprint, tức 22 tuần, xấp xỉ 5 tháng).

**Bước 4 (phân tích nhạy)**: velocity đang tăng do đội học việc (14 lên 23). Dùng trung bình 3 sprint gần nhất (18 + 21 + 23)/3 = 20,67 điểm: 124/20,67 = **6,0 sprint**, tức khoảng 10 sprint (20 tuần) tổng. Do đó dự báo hợp lý nằm trong khoảng **10-11 sprint (20-22 tuần)**.

#### 3.4.4. Diễn giải

| Chỉ tiêu | Waterfall (cũ) | Scrum (mới) |
|---|---|---|
| Thời gian | 10 tháng (trễ 66,7%) | Khoảng 5 tháng (dự báo 20-22 tuần) |
| Phản hồi khách hàng | Cuối dự án | Mỗi 2 tuần |
| Lãng phí tính năng không cần | Cao | Thấp (ưu tiên backlog) |

Điều quan trọng: backlog được sắp theo giá trị kinh doanh, nên nhóm có thể ra bản **MVP** (giả sử 80 điểm đầu tiên) rất sớm: sau sprint 4 tích lũy 76 điểm (chưa đủ), sprint 5 (giả sử đạt khoảng 22 điểm) đưa tích lũy lên 98 điểm, tức MVP có thể ra mắt sau 5 sprint (10 tuần) để thu phản hồi thật.

#### 3.4.5. Bài học

1. Scrum không làm dự án "nhanh hơn" về tổng khối lượng, nhưng làm sai lầm lộ ra sớm và giảm lãng phí.
2. Velocity là công cụ *dự báo*, không phải công cụ đánh giá cá nhân hay ép đội nhóm.
3. Ưu tiên backlog theo giá trị giúp ra MVP sớm thay vì chờ 100% sản phẩm.

### 3.5. Case SME Việt Nam (dịch vụ): Công ty tổ chức sự kiện quản lý đa dự án

> Số liệu trong case này là **giả định minh họa**.

#### 3.5.1. Bối cảnh

Công ty tổ chức sự kiện 20 nhân viên quản lý 5-10 sự kiện cùng lúc, mỗi sự kiện có deadline cố định. Trước đây dùng file Excel rời cho từng sự kiện nên xung đột nguồn lực (cùng thiết bị/nhân sự được gán cho 2 sự kiện trùng ngày) không bị phát hiện.

#### 3.5.2. Phân tích nguồn lực (resource histogram)

Công ty có **2 bộ âm thanh - ánh sáng**. Ba sự kiện cần mỗi sự kiện 1 bộ vào các ngày: Sự kiện 1: ngày 10-12; Sự kiện 2: ngày 11-13; Sự kiện 3: ngày 12-14.

| Ngày | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|
| Số bộ cần | 1 | 2 | 3 | 2 | 1 |
| Công suất (2 bộ) | 2 | 2 | 2 | 2 | 2 |
| Chênh lệch | +1 | 0 | **-1** | 0 | +1 |

**Tổng nhu cầu** = 1 + 2 + 3 + 2 + 1 = 9 bộ-ngày; **tổng công suất** = 2 x 5 = 10 bộ-ngày. **Hiệu suất sử dụng** = 9/10 = **90%** - rất cao, rủi ro xung đột lớn. Vấn đề không phải tổng công suất (9 < 10) mà là **sự phân bổ theo thời gian** (ngày 12 cần 3 bộ), điều Excel rời không phát hiện được.

#### 3.5.3. Giải pháp

| Phương án | Mô tả | Kết quả |
|---|---|---|
| 1. San phẳng nguồn lực (resource leveling) | Dời Sự kiện 3 sang ngày 13-15 nếu khâu lắp đặt có float 1 ngày (giả định) | Tải mỗi ngày: 1, 2, 2, 2, 1, 1 (ngày 10 đến 15): tối đa 2, đủ công suất; tổng vẫn 9 bộ-ngày |
| 2. Thuê ngoài 1 bộ trong ngày 12 | Chi phí thuê giả định 3 triệu VNĐ/ngày | Chi phí 3 triệu, giữ nguyên lịch |
| 3. Mua thêm 1 bộ | Đầu tư vốn lớn | Chỉ hợp lý nếu xung đột lặp lại thường xuyên |

Công ty chọn phương án 1 làm mặc định, phương án 2 dự phòng; WBS mẫu cho từng loại sự kiện kết hợp phần mềm đa dự án (Trello, Asana) để thấy tải nguồn lực xuyên suốt.

#### 3.5.4. Bài học

1. Xung đột nguồn lực thường chỉ lộ ra khi cộng dồn nhu cầu theo ngày giữa nhiều dự án.
2. Dùng float của việc không găng để san tải miễn phí trước khi tốn tiền thuê hay mua.
3. Hiệu suất sử dụng trên 85-90% cho thấy cần nguồn lực dự phòng (liên hệ file 05 - hoạch định công suất).

### 3.6. Case Việt Nam (thương mại điện tử): Phối hợp đa nhóm Scrum bằng Scrum of Scrums (minh họa)

> Case này mô tả một **tình huống điển hình, minh họa** về các nền tảng thương mại điện tử Việt Nam vận hành nhiều nhóm sản phẩm; số liệu là giả định, không phải dữ liệu nội bộ của bất kỳ công ty cụ thể nào (kể cả Tiki, nơi tác giả file chưa kiểm chứng được cách tổ chức thực tế).

#### 3.6.1. Bối cảnh

Một sàn thương mại điện tử có nhiều nhóm Scrum song song (thanh toán, logistics, tìm kiếm, khuyến mãi, giao diện). Nhiều tính năng cắt ngang các nhóm; ví dụ tính năng voucher cần cả nhóm thanh toán và nhóm giao diện.

#### 3.6.2. Số liệu giả định và tính toán

- Mỗi quý ra 30 tính năng; 40% có phụ thuộc chéo giữa nhóm: 30 x 40% = **12 tính năng**.
- Trước khi có cơ chế phối hợp: mỗi tính năng phụ thuộc chéo chờ trung bình 1 sprint (2 tuần): 12 x 2 = **24 tính năng-tuần** chờ.
- Sau khi áp dụng Scrum of Scrums (họp đồng bộ liên nhóm hằng tuần, bảng phụ thuộc chung): thời gian chờ giảm còn trung bình 0,5 sprint (1 tuần): 12 x 1 = **12 tính năng-tuần**, giảm 50%.

#### 3.6.3. Cơ chế

- Mỗi nhóm cử đại diện họp Scrum of Scrums hằng tuần: nêu việc nhóm đang chờ nhóm khác, việc nhóm mình cản trở người khác.
- PMO mức Controlling chuẩn hoá cách ước lượng story points và Definition of Done chung để các nhóm "hiểu cùng một ngôn ngữ".

#### 3.6.4. Bài học

1. Phụ thuộc chéo là nguồn trễ hạn chính ở tổ chức nhiều nhóm; phải *nhìn thấy* chúng sớm.
2. Chuẩn hoá tối thiểu (Definition of Done, thang ước lượng) quan trọng hơn thêm quy trình nặng nề.
3. Đo bằng "thời gian chờ" giúp thuyết phục lãnh đạo đầu tư vào phối hợp.

### 3.7. Case SME Việt Nam mới: "Hạnh Phúc Fit-out" thi công quán cà phê 80 m² (giả định minh họa)

> Toàn bộ tên doanh nghiệp, số liệu là **giả định minh họa**. Case tích hợp WBS, PERT, CPM, xác suất đúng hạn, Crashing, rủi ro EMV và EVM.

#### 3.7.1. Bối cảnh

Công ty Hạnh Phúc Fit-out (giả định) nhận thi công trọn gói quán cà phê 80 m² tại TP. Hồ Chí Minh cho khách hàng mở quán. Ngân sách kế hoạch (BAC) **630 triệu VNĐ**. Khách cam kết khai trương vào ngày thứ **42** (kể từ ngày bắt đầu); mỗi ngày khai trương trễ, khách bị mất doanh thu ước tính (giả định) **15 triệu VNĐ/ngày** và đòi công ty bồi thường.

#### 3.7.2. Bước 1: WBS và danh sách công việc

| Mã | Hạng mục | Công việc trước | Ghi chú |
|---|---|---|---|
| A | Thiết kế và duyệt bản vẽ | - | Cần khách duyệt |
| B | Đặt mua và nhận thiết bị (máy espresso, tủ mát) | A | Nhập khẩu |
| C | Thi công phần thô (điện, nước, đập) | A | |
| D | Hoàn thiện (trần, sơn, sàn) | C | |
| E | Nội thất và quầy bar | D | |
| F | Lắp thiết bị và cài POS | B, E | |
| G | Nghiệm thu PCCC và chạy thử | F | |

Ước lượng ba điểm (ngày):

| Việc | $t_o$ | $t_m$ | $t_p$ |
|---|---|---|---|
| A | 4 | 5 | 12 |
| B | 8 | 10 | 18 |
| C | 6 | 8 | 14 |
| D | 7 | 9 | 17 |
| E | 6 | 8 | 10 |
| F | 2 | 3 | 4 |
| G | 2 | 3 | 10 |

#### 3.7.3. Bước 2: Tính thời gian kỳ vọng và phương sai (PERT)

| Việc | $t_e = (t_o + 4t_m + t_p)/6$ | $\sigma = (t_p - t_o)/6$ | Phương sai $\sigma^2$ |
|---|---|---|---|
| A | (4 + 20 + 12)/6 = 36/6 = **6,00** | 8/6 = 1,33 | 1,778 |
| B | (8 + 40 + 18)/6 = 66/6 = **11,00** | 10/6 = 1,67 | 2,778 |
| C | (6 + 32 + 14)/6 = 52/6 = **8,67** | 8/6 = 1,33 | 1,778 |
| D | (7 + 36 + 17)/6 = 60/6 = **10,00** | 10/6 = 1,67 | 2,778 |
| E | (6 + 32 + 10)/6 = 48/6 = **8,00** | 4/6 = 0,67 | 0,444 |
| F | (2 + 12 + 4)/6 = 18/6 = **3,00** | 2/6 = 0,33 | 0,111 |
| G | (2 + 12 + 10)/6 = 24/6 = **4,00** | 8/6 = 1,33 | 1,778 |

#### 3.7.4. Bước 3: CPM (Forward/Backward pass)

```
         ┌──▶ C(8,67) ──▶ D(10) ──▶ E(8) ──┐
A(6) ────┤                                  ├──▶ F(3) ──▶ G(4)
         └──▶ B(11) ────────────────────────┘
```

| Việc | ES | EF | LS | LF | Float |
|---|---|---|---|---|---|
| A | 0 | 6,00 | 0 | 6,00 | 0 |
| B | 6,00 | 17,00 | 21,67 | 32,67 | **15,67** |
| C | 6,00 | 14,67 | 6,00 | 14,67 | 0 |
| D | 14,67 | 24,67 | 14,67 | 24,67 | 0 |
| E | 24,67 | 32,67 | 24,67 | 32,67 | 0 |
| F | 32,67 | 35,67 | 32,67 | 35,67 | 0 |
| G | 35,67 | 39,67 | 35,67 | 39,67 | 0 |

- Đường găng: **A - C - D - E - F - G**, dài 6 + 8,67 + 10 + 8 + 3 + 4 = **39,67 ngày**.
- Đường phụ A - B - F - G dài 6 + 11 + 3 + 4 = 24 ngày; B có float 39,67 - 24 = 15,67 ngày: việc đặt máy rất "thoải mái" về lịch.

**Diễn giải**: lo lắng thường dồn vào máy nhập khẩu (B), nhưng về tiến độ thì chuỗi thi công trong quán mới là điểm quyết định. Chủ thầu nên giám sát chặt C, D, E.

#### 3.7.5. Bước 4: Xác suất kịp hạn 42 ngày

Phương sai đường găng = 1,778 (A) + 1,778 (C) + 2,778 (D) + 0,444 (E) + 0,111 (F) + 1,778 (G) = **8,667**, nên $\sigma_{project} = \sqrt{8{,}667} = 2{,}94$ ngày.

$$z = \frac{42 - 39{,}67}{2{,}94} = 0{,}79 \;\Rightarrow\; \Phi(0{,}79) \approx 78{,}6\%$$

| Hạn cam kết (ngày) | z | Xác suất kịp hạn |
|---|---|---|
| 36 | -1,25 | khoảng 10,7% |
| 40 | 0,11 | khoảng 54,5% |
| 42 | 0,79 | khoảng 78,6% |
| 45 | 1,81 | khoảng 96,5% |

Để đạt độ tin cậy 95%: $T = 39{,}67 + 1{,}645 \times 2{,}94 \approx 44{,}5$ ngày. Vì vậy với hạn 42 ngày công ty có khoảng 21,4% rủi ro trễ; kỳ vọng thiệt hại phạt chỉ là một phần; công ty nên chủ động rút ngắn hoặc thương lượng hạn.

#### 3.7.6. Bước 5: Crashing có lợi cho khai trương sớm

Dùng thời lượng làm tròn (A = 6, B = 11, C = 9, D = 10, E = 8, F = 3, G = 4 ngày; đường găng A-C-D-E-F-G = **40 ngày**).

| Việc găng | Bình thường (ngày / triệu) | Crash (ngày / triệu) | Chi phí crash mỗi ngày | Tối đa rút |
|---|---|---|---|---|
| A | 6 / 40 | 5 / 52 | (52 - 40)/1 = **12** | 1 |
| C | 9 / 90 | 7 / 110 | (110 - 90)/2 = **10** | 2 |
| D | 10 / 120 | 8 / 150 | (150 - 120)/2 = **15** | 2 |
| E | 8 / 150 | 6 / 168 | (168 - 150)/2 = **9** | 2 |
| G | 4 / 30 | 3 / 40 | (40 - 30)/1 = **10** | 1 |

Lợi ích mỗi ngày rút ngắn = 15 triệu (doanh thu khách mất). Ta crash theo thứ tự chi phí thấp nhất và chỉ khi chi phí/ngày nhỏ hơn 15:

1. E: 9 triệu/ngày, rút 2 ngày = 18 triệu.
2. C: 10 triệu/ngày, rút 2 ngày = 20 triệu.
3. G: 10 triệu/ngày, rút 1 ngày = 10 triệu.
4. A: 12 triệu/ngày, rút 1 ngày = 12 triệu.
5. D: 15 triệu/ngày = lợi ích biên: hòa vốn, không crash.

Tổng rút 2 + 2 + 1 + 1 = **6 ngày**, chi phí **18 + 20 + 10 + 12 = 60 triệu**, lợi ích 6 x 15 = **90 triệu**, lợi ròng **30 triệu**. Kiểm tra đường phụ sau crash: A(5) + B(11) + F(3) + G(3) = 22 ngày, vẫn xa 34 ngày, nên **không xuất hiện đường găng mới**. Lịch mới: 40 - 6 = **34 ngày**.

#### 3.7.7. Bước 6: Giám sát EVM tại ngày 25 (theo lịch gốc 40 ngày, chưa crash)

Ngân sách theo hạng mục (triệu VNĐ): A 40, B 180, C 90, D 120, E 150, F 20, G 30; **BAC = 630**.

Theo lịch gốc: A (0-6), B (6-17), C (6-15), D (15-25), E (25-33), F (33-36), G (36-40).

- **PV tại ngày 25**: A, B, C, D lẽ ra đã xong hoàn toàn: 40 + 180 + 90 + 120 = **430**.
- **Thực tế**: A, B, C xong; D mới xong 60%; E chưa bắt đầu. **EV** = 40 + 180 + 90 + 0,6 x 120 = **382**.
- **AC** (chi phí thực tế đã chi, giả định) = **410**.

| Chỉ số | Phép tính | Kết quả | Ý nghĩa |
|---|---|---|---|
| CV | 382 - 410 | **-28 triệu** | Vượt chi phí |
| SV | 382 - 430 | **-48 triệu** | Chậm tiến độ |
| CPI | 382/410 | **0,93** | Mỗi 1 đồng chi chỉ tạo 0,93 đồng giá trị |
| SPI | 382/430 | **0,89** | Chỉ đạt 89% tốc độ kế hoạch |
| EAC (xu hướng CPI kéo dài) | 630/0,9317 | **676,2 triệu** | Dự báo vượt 46,2 triệu |
| EAC (sự cố một lần) | 410 + (630 - 382) | **658 triệu** | Kịch bản lạc quan |
| EAC (CPI x SPI) | 410 + 248/(0,9317 x 0,8884) | **709,6 triệu** | Kịch bản bi quan |
| ETC | 676,2 - 410 | **266,2 triệu** | Còn phải chi |
| VAC | 630 - 676,2 | **-46,2 triệu** | Vượt ngân sách |
| TCPI | (630 - 382)/(630 - 410) = 248/220 | **1,13** | Phải làm tốt hơn mức hiện tại 13% để kịp ngân sách |

Dự báo thời gian: 40/0,8884 = **khoảng 45 ngày** nếu tốc độ hiện tại kéo dài (ước tính thô).

**Diễn giải và hành động**: dự án cùng lúc chậm và vượt chi phí. Việc D (hoàn thiện) làm chậm kéo cả đường găng (D nằm trên đường găng). Hành động: (1) tìm nguyên nhân gốc (thợ thiếu hay vật tư đổi?); (2) crash E hoặc C vì chi phí biên thấp; (3) báo khách sớm về nguy cơ trễ và đàm phán điều chỉnh. Chỉ số TCPI 1,13 cho thấy "tự làm tốt lên 13%" là mục tiêu khó, nên cần xin điều chỉnh ngân sách hoặc cắt phạm vi.

#### 3.7.8. Bước 7: Rủi ro và quỹ dự phòng bằng EMV

| Rủi ro | Xác suất | Thiệt hại (triệu) | EMV = P x I | Ứng phó |
|---|---|---|---|---|
| R1: Máy espresso nhập khẩu về trễ | 30% | 45 | 13,5 | Giảm thiểu: đặt hàng sớm, có phương án thuê máy |
| R2: Khách đổi thiết kế giữa chừng | 40% | 30 | 12,0 | Né tránh/kiểm soát: chốt bản vẽ có chữ ký, change control |
| R3: Nghiệm thu PCCC không đạt lần 1 | 25% | 20 | 5,0 | Giảm thiểu: tư vấn PCCC kiểm tra sớm |
| R4: Thợ chính nghỉ việc | 20% | 15 | 3,0 | Chuyển giao: đội thầu phụ dự phòng |
| **Tổng EMV** | | | **33,5** | |

Quỹ dự phòng khoảng 33,5 triệu, tương đương 33,5/630 = **5,3% BAC**, nằm trong khoảng 5-10% thường dùng cho dự án xây dựng nhỏ (quy tắc kinh nghiệm).

#### 3.7.9. Kết luận và khuyến nghị cho chủ thầu

1. **Tập trung vào đường găng** A-C-D-E-F-G; giám sát B ở mức vừa đủ vì float 15,67 ngày.
2. **Cam kết hạn 42 ngày chỉ có xác suất ~78,6%**: nếu rút ngắn bằng crashing thì kịp hạn gần như chắc chắn (hạn 34 ngày kỳ vọng).
3. **Crash có chọn lọc** (60 triệu cho 6 ngày) hiệu quả hơn tăng ca đồng loạt.
4. **EVM hằng tuần** để phát hiện chậm và vượt sớm; chỉ số CPI 0,93 là chỉ báo cảnh báo.
5. **Quỹ dự phòng 33,5 triệu** (EMV) thay vì "hy vọng không có rủi ro".

### 3.8. Bảng tổng hợp bài học từ các case study

| Case study | Kỹ thuật chính | Bài học chính |
|---|---|---|
| 3.1 Boeing 777 | Thiết kế số, nhóm liên chức năng | Phát hiện lỗi sớm rẻ hơn gấp nhiều lần; đầu tư hoạch định có lợi suất cao |
| 3.2 VinFast | Fast-tracking + Crashing | Rút ngắn mạnh cần nguồn lực mạnh và quản lý giao diện chặt |
| 3.3 Denver Airport (thất bại) | Bài học phản diện | Scope creep, rủi ro công nghệ và thiếu kiểm soát thay đổi gây thiệt hại lớn |
| 3.4 Startup Scrum | Scrum, Velocity | Agile phù hợp khi yêu cầu chưa rõ; velocity giúp dự báo |
| 3.5 Công ty sự kiện | WBS mẫu, resource leveling | Xung đột nguồn lực chỉ lộ khi cộng dồn nhu cầu nhiều dự án |
| 3.6 Đa nhóm Scrum (minh họa) | Scrum of Scrums, PMO | Quản lý phụ thuộc chéo giảm thời gian chờ |
| 3.7 Hạnh Phúc Fit-out (SME mới) | PERT, CPM, Crashing, EVM, EMV | Kết hợp công cụ định lượng giúp cam kết hạn hợp lý và kiểm soát giữa chừng |

---

## IV. Ứng dụng cho SME

### 4.1. Quy trình 8 bước quản trị dự án theo PMBOK

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

### 4.2. Quy mô áp dụng: SME vs Doanh nghiệp lớn

| Thành phần | SME | Doanh nghiệp lớn |
|---|---|---|
| Công cụ lập lịch | Excel/Google Sheets, Trello | MS Project, Primavera P6, Jira Enterprise |
| Phương pháp | Agile đơn giản hoặc Waterfall cơ bản | PMBOK đầy đủ, PMO chuyên trách |
| Quản trị rủi ro | Kinh nghiệm, checklist đơn giản | Ma trận rủi ro định lượng, phần mềm chuyên dụng |
| Nhân sự | Kiêm nhiệm (founder, trưởng nhóm) | Project Manager/PMO chuyên trách, chứng chỉ PMP |
| Đo lường hiệu suất | Theo dõi tiến độ đơn giản | EVM đầy đủ (CPI, SPI), dashboard báo cáo tự động |

### 4.3. Chi phí đầu tư theo giai đoạn phát triển

| Giai đoạn | Công cụ quản trị dự án | Chi phí ước tính (VNĐ) |
|---|---|---|
| Khởi nghiệp | Trello, Google Sheets miễn phí | 0 - 5 triệu/năm |
| Tăng trưởng | Asana, Notion, Jira cơ bản | 20 - 100 triệu/năm |
| Mở rộng | MS Project, Jira Enterprise + PMO nhỏ | 200 triệu - 1 tỷ/năm |
| Doanh nghiệp lớn | Primavera P6, PMO đầy đủ, đào tạo PMP | 1 - 10+ tỷ/năm |

### 4.4. Lộ trình khuyến nghị cho SME

1. Bắt đầu với WBS đơn giản cho mọi dự án, dù nhỏ, để tránh bỏ sót công việc.
2. Áp dụng Gantt Chart cơ bản (Excel/Trello) trước khi đầu tư phần mềm phức tạp.
3. Nếu dự án có yêu cầu rõ ràng, ổn định (xây dựng, sản xuất) thì áp dụng Waterfall cơ bản với CPM.
4. Nếu yêu cầu thay đổi liên tục (phần mềm, sản phẩm số) thì áp dụng Scrum/Agile đơn giản.
5. Khi quản lý nhiều dự án song song, đầu tư công cụ đa dự án để tránh xung đột nguồn lực.
6. Khi dự án có giá trị lớn (từ vài trăm triệu), bắt đầu theo dõi CPI/SPI hằng tuần.

### 4.5. Các sai lầm thường gặp

| Sai lầm | Hậu quả | Cách phòng tránh |
|---|---|---|
| Không xác định rõ đường găng | Tập trung nguồn lực sai chỗ, dự án vẫn trễ | Dùng CPM để xác định và ưu tiên giám sát đường găng |
| Scope creep không kiểm soát | Dự án phình to, trễ hạn, vượt ngân sách | Quy trình kiểm soát thay đổi chặt chẽ |
| Ước lượng thời gian quá lạc quan | Deadline liên tục bị phá vỡ | Dùng PERT 3 kịch bản, học từ dữ liệu lịch sử |
| Áp dụng Waterfall cho dự án yêu cầu chưa rõ | Sản phẩm cuối không đáp ứng nhu cầu | Đánh giá đặc thù để chọn Waterfall/Agile/Hybrid |
| Không quản lý xung đột nguồn lực đa dự án | Phân công trùng lặp, giảm chất lượng | Công cụ đa dự án, xem xét năng lực tổng thể |
| Chỉ theo dõi tiền chi mà không đo EV | Biết "đã chi bao nhiêu" nhưng không biết "đã làm được bao nhiêu" | Dùng EVM tối thiểu (PV, EV, AC) |
| Crash việc ngoài đường găng | Tốn tiền mà không rút ngắn dự án | Luôn kiểm tra float trước khi crash |

---

## V. Tools & Templates

### 5.1. Bảng công cụ phần mềm quản trị dự án

| Công cụ | Chức năng chính | Chi phí ước tính | Phù hợp |
|---|---|---|---|
| Trello | Kanban Board đơn giản | Miễn phí - 5 USD/user/tháng | SME nhỏ, Agile cơ bản |
| Asana, Notion | Quản lý task, timeline cơ bản | Miễn phí - 15 USD/user/tháng | SME vừa |
| Jira | Quản lý Agile/Scrum chuyên sâu | 10-20 USD/user/tháng | Đội phát triển phần mềm |
| Microsoft Project | Gantt Chart, CPM chuyên nghiệp | Vài triệu/license | Dự án xây dựng, kỹ thuật |
| Primavera P6 | Quản lý dự án phức tạp, đa dự án | Hàng chục-trăm triệu | Tập đoàn lớn, dự án hạ tầng |

(Giá tham khảo, thay đổi theo thời điểm và gói; cần kiểm tra lại trên trang nhà cung cấp.)

### 5.2. Template: Bảng tính CPM cơ bản

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
Float = LS - ES (Float = 0 thì nằm trên đường găng)
```

### 5.3. Template: Bảng theo dõi EVM hằng tuần (Excel/Google Sheets)

| Tuần | PV | EV | AC | CV = EV - AC | SV = EV - PV | CPI = EV/AC | SPI = EV/PV | EAC = BAC/CPI | Cảnh báo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | Đỏ nếu CPI hoặc SPI < 0,9 |
| 2 | | | | | | | | | Vàng nếu 0,9 đến 0,95 |

Mẹo: dùng định dạng có điều kiện (conditional formatting) để tô màu cảnh báo; EV tính theo % hoàn thành của từng gói việc nhân ngân sách gói đó.

### 5.4. Sơ đồ quyết định chọn phương pháp luận dự án

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

## VI. Bài tập thực hành

Phần này có đáp án/hướng dẫn giải. Các bài tính toán đã được kiểm chứng bằng Python.

### Bài 1. Xây dựng WBS

Lập WBS ít nhất 3 cấp cho một dự án thực tế (tổ chức sự kiện, ra mắt sản phẩm, xây ứng dụng).

**Hướng dẫn**: cấp 1 là các giai đoạn/sản phẩm bàn giao chính; cấp 2 là hạng mục; cấp 3 là gói công việc 8-80 giờ. Kiểm tra quy tắc 100% (không bỏ sót, không trùng).

### Bài 2. CPM cho dự án 8 công việc

| Việc | Thời gian (ngày) | Phụ thuộc |
|---|---|---|
| A | 3 | - |
| B | 4 | A |
| C | 2 | A |
| D | 5 | B |
| E | 6 | C |
| F | 3 | D, E |
| G | 4 | B |
| H | 2 | F, G |

**Đáp án**:

| Việc | ES | EF | LS | LF | Float |
|---|---|---|---|---|---|
| A | 0 | 3 | 0 | 3 | 0 |
| B | 3 | 7 | 3 | 7 | 0 |
| C | 3 | 5 | 4 | 6 | 1 |
| D | 7 | 12 | 7 | 12 | 0 |
| E | 5 | 11 | 6 | 12 | 1 |
| F | 12 | 15 | 12 | 15 | 0 |
| G | 7 | 11 | 11 | 15 | 4 |
| H | 15 | 17 | 15 | 17 | 0 |

Giải thích: ES của F = max(EF của D = 12, EF của E = 11) = 12; ES của H = max(15, 11) = 15. Đường găng **A - B - D - F - H** = 3 + 4 + 5 + 3 + 2 = **17 ngày**. Float của C và E là 1 ngày (chuỗi A-C-E-F-H = 3 + 2 + 6 + 3 + 2 = 16 ngày, kém 1 ngày), của G là 4 ngày.

### Bài 3. PERT cho 5 công việc

| Việc | $t_o$ | $t_m$ | $t_p$ | $t_e$ | $\sigma$ | $\sigma^2$ |
|---|---|---|---|---|---|---|
| 1 | 2 | 4 | 6 | (2 + 16 + 6)/6 = **4,0** | 4/6 = 0,67 | 0,444 |
| 2 | 3 | 5 | 13 | (3 + 20 + 13)/6 = **6,0** | 10/6 = 1,67 | 2,778 |
| 3 | 1 | 2 | 3 | (1 + 8 + 3)/6 = **2,0** | 2/6 = 0,33 | 0,111 |
| 4 | 6 | 9 | 18 | (6 + 36 + 18)/6 = **10,0** | 12/6 = 2,00 | 4,000 |
| 5 | 4 | 4 | 10 | (4 + 16 + 10)/6 = **5,0** | 6/6 = 1,00 | 1,000 |

Nếu cả 5 việc nối tiếp nhau trên đường găng: $T_e = 4 + 6 + 2 + 10 + 5 = 27$ ngày; phương sai tổng = 0,444 + 2,778 + 0,111 + 4,000 + 1,000 = 8,333, $\sigma = 2{,}89$ ngày. Xác suất xong trong 30 ngày: z = (30 - 27)/2,89 = 1,04, xấp xỉ 85%.

### Bài 4. Crashing: rút ngắn 2 ngày cho dự án Bài 2

Giả định chi phí crash (triệu VNĐ/ngày) trên các việc găng: A 3 (tối đa 1 ngày), B 2 (tối đa 1 ngày), D 1,5 (tối đa 2 ngày), F 4 (tối đa 1 ngày), H 5 (tối đa 1 ngày). Việc E crash 2 triệu/ngày (tối đa 1 ngày).

**Đáp án**:
- Chọn D trước (rẻ nhất, 1,5 triệu/ngày). Crash D 1 ngày thì A-B-D-F-H còn 16 ngày, **trùng** chuỗi A-C-E-F-H (16 ngày): có hai đường găng. Không crash D thêm 1 ngày nữa vì sẽ không giảm tổng (đường kia vẫn 16).
- Để giảm tiếp 1 ngày phải giảm trên **cả hai đường**: hoặc việc chung (A: 3 triệu/ngày), hoặc D + E (1,5 + 2 = 3,5 triệu). Chọn A (3 triệu, rẻ hơn).
- Tổng: D 1 ngày (1,5) + A 1 ngày (3) = **4,5 triệu**, dự án còn **15 ngày** (kiểm tra: A-B-D-F-H = 2 + 4 + 4 + 3 + 2 = 15; A-C-E-F-H = 2 + 2 + 6 + 3 + 2 = 15; A-B-G-H = 2 + 4 + 4 + 2 = 12).

### Bài 5. EVM

Dự án có BAC = 500 triệu. Tại thời điểm đánh giá: PV = 200, EV = 180, AC = 210 (triệu VNĐ).

**Đáp án**:
- CV = 180 - 210 = **-30**; SV = 180 - 200 = **-20**.
- CPI = 180/210 = **0,857**; SPI = 180/200 = **0,90**.
- EAC = 500/0,857 = **583,3 triệu**; VAC = 500 - 583,3 = **-83,3 triệu**.
- Kết luận: dự án vượt chi phí (mỗi 1 đồng chi chỉ tạo 0,857 đồng giá trị) và chậm tiến độ 10%; nếu không cải thiện, vượt ngân sách khoảng 16,7%.

### Bài 6. Velocity và dự báo

Một nhóm Scrum hoàn thành 21, 25, 23, 27, 24 story points ở 5 sprint đầu; backlog còn lại 168 điểm.

**Đáp án**: Velocity trung bình = (21 + 25 + 23 + 27 + 24)/5 = 120/5 = **24 điểm/sprint**; số sprint còn lại = 168/24 = **7 sprint** (nếu sprint 2 tuần, khoảng 14 tuần).

### Bài 7. So sánh Waterfall và Agile

Cho 3 loại dự án: xây nhà, phát triển app, tổ chức hội nghị. Đề xuất phương pháp.

**Gợi ý**: xây nhà là Waterfall (yêu cầu ổn định, quy định pháp lý chặt); phát triển app là Agile/Scrum (yêu cầu thay đổi); tổ chức hội nghị là Hybrid (khung thời gian cố định kiểu Waterfall, nội dung chương trình điều chỉnh linh hoạt).

### Bài 8. Phân tích Denver Airport

Viết phân tích nguyên nhân gốc rễ về quản trị phạm vi và rủi ro cho case mục 3.3.

**Gợi ý**: dùng sơ đồ xương cá hoặc 5 Whys; tách nhóm nguyên nhân thành phạm vi (scope creep), rủi ro công nghệ, phối hợp, ép tiến độ; mỗi nhóm đề xuất một biện pháp phòng ngừa cụ thể bằng công cụ trong bài.

### Bài 9. Ma trận rủi ro

Lập ma trận rủi ro cho một dự án thực tế với tối thiểu 8 rủi ro, phân thành 4 nhóm và đề xuất chiến lược ứng phó.

**Hướng dẫn tính**: gán xác suất P (%) và thiệt hại I (triệu VNĐ) cho từng rủi ro; EMV = P x I; xếp hạng giảm dần; tổng EMV = quỹ dự phòng; chọn một trong 4 chiến lược (né tránh, giảm thiểu, chuyển giao, chấp nhận) cho mỗi rủi ro. Tham khảo mục 3.7.8.

### Bài 10. Xung đột nguồn lực

Thiết kế quy trình quản lý xung đột nguồn lực cho tổ chức nhiều dự án đồng thời.

**Gợi ý**: (1) lập kho nguồn lực chung (resource pool); (2) cộng dồn nhu cầu theo ngày/tuần như bảng ở mục 3.5.2; (3) quy tắc ưu tiên (dự án găng và hạn cứng trước); (4) dùng float để san tải; (5) phương án thuê ngoài; (6) họp phân bổ nguồn lực hằng tuần.

### Bài 11. Scrum of Scrums

Xây dựng mô hình Scrum of Scrums cho tổ chức có 4 nhóm Scrum song song.

**Gợi ý**: mỗi nhóm cử 1 đại diện; họp 2-3 lần/tuần, 15-30 phút; nội dung: (a) nhóm mình đã hoàn thành gì ảnh hưởng nhóm khác, (b) sẽ làm gì tới, (c) đang bị chặn bởi nhóm nào. Dùng bảng phụ thuộc chung và Definition of Done thống nhất.

### Bài 12. Tính toán tổng hợp (EVM + xác suất)

Một đường găng có $T_e = 50$ ngày và tổng phương sai 16 (ngày²). Khách yêu cầu xong sau 54 ngày.

**Đáp án**: $\sigma = \sqrt{16} = 4$; z = (54 - 50)/4 = **1,0**; $\Phi(1) \approx 84{,}1\%$. Vậy xác suất kịp hạn khoảng 84%, còn 16% rủi ro trễ.

---

## PHỤ LỤC: CHECKLIST QUẢN TRỊ DỰ ÁN TỔNG HỢP

### A. Checklist tự đánh giá năng lực quản trị dự án (Project Management Maturity Checklist)

- □ Mọi dự án đều có WBS được lập trước khi bắt đầu triển khai?
- □ Đã xác định rõ đường găng (critical path) cho các dự án có nhiều công việc phụ thuộc?
- □ Có quy trình kiểm soát thay đổi (change control) chính thức để đánh giá tác động trước khi phê duyệt thay đổi phạm vi?
- □ Có công cụ theo dõi tiến độ tập trung khi quản lý nhiều dự án đồng thời?
- □ Đội ngũ được đào tạo cơ bản về sự khác biệt Waterfall và Agile để chọn phương pháp phù hợp?
- □ Có quy trình rút kinh nghiệm (lessons learned) chính thức sau mỗi dự án kết thúc?
- □ Đã dùng ít nhất một chỉ số định lượng (CPI, SPI hoặc Velocity) để đánh giá hiệu suất dự án?
- □ Có ma trận đánh giá rủi ro cập nhật định kỳ trong suốt vòng đời dự án?
- □ Các bên liên quan (stakeholders) chính được xác định và giao tiếp thường xuyên?
- □ Ước lượng thời gian dùng 3 điểm (PERT) cho công việc có độ bất định cao?
- □ Có quỹ dự phòng rủi ro (contingency reserve) tính từ EMV?
- □ Đã kiểm tra float trước khi quyết định crash công việc?

### B. Bảng thuật ngữ (Glossary)

| Thuật ngữ | Giải thích |
|---|---|
| WBS | Work Breakdown Structure - cơ cấu phân chia công việc |
| CPM | Critical Path Method - phương pháp đường găng |
| PERT | Program Evaluation and Review Technique |
| Float/Slack | Độ trễ cho phép của một công việc không nằm trên đường găng |
| Crashing | Rút ngắn thời gian dự án bằng cách tăng nguồn lực |
| Fast-tracking | Chạy song song các công việc thường được lên kế hoạch nối tiếp |
| Scope Creep | Phạm vi dự án mở rộng không kiểm soát |
| EVM | Earned Value Management - quản lý giá trị thu được |
| EMV | Expected Monetary Value - giá trị tiền tệ kỳ vọng của rủi ro |
| Sprint | Chu kỳ lặp ngắn trong Scrum (1-4 tuần) |
| Product Backlog | Danh sách yêu cầu/tính năng được ưu tiên hoá trong Scrum |
| PMO | Project Management Office - văn phòng quản trị dự án tập trung |
| PPM | Project Portfolio Management - quản trị danh mục dự án |
| Velocity | Tốc độ hoàn thành công việc trung bình mỗi sprint |
| Definition of Done | Tiêu chí thống nhất xác định một công việc đã thực sự hoàn thành |

### C. Bảng đo lường KPI dự án

| KPI | Công thức | Mục tiêu tham khảo |
|---|---|---|
| CPI | EV/AC | > 1,0 (tiết kiệm chi phí) |
| SPI | EV/PV | > 1,0 (nhanh hơn kế hoạch) |
| Tỷ lệ hoàn thành đúng hạn | Số dự án đúng hạn / Tổng số dự án | > 90% |
| Tỷ lệ vượt ngân sách | (Chi phí thực tế - Ngân sách) / Ngân sách | < 10% |
| Velocity (Agile) | Số story points hoàn thành mỗi sprint | Ổn định qua các sprint |

### D. Sổ tay rủi ro dự án (Risk Register mẫu)

| Rủi ro | Xác suất | Tác động | Biện pháp giảm thiểu |
|---|---|---|---|
| Yêu cầu khách hàng thay đổi liên tục | Cao | Trung bình | Áp dụng Agile, quy trình change control rõ ràng |
| Thành viên chủ chốt nghỉ việc giữa dự án | Trung bình | Cao | Tài liệu hoá kiến thức, đào tạo chéo (cross-training) |
| Ước lượng thời gian/chi phí sai lệch lớn | Trung bình | Cao | Dùng PERT, tham khảo dữ liệu dự án tương tự |
| Xung đột nguồn lực giữa các dự án | Trung bình | Trung bình | Công cụ đa dự án, họp phân bổ nguồn lực định kỳ |
| Nhà cung cấp/nhà thầu phụ giao chậm | Trung bình | Cao | Hợp đồng ràng buộc SLA, đánh giá NCC trước khi ký |
| Phụ thuộc chéo giữa nhiều nhóm Scrum | Cao | Trung bình | Scrum of Scrums, Definition of Done chung |

### E. Bảng công thức tổng hợp

| Mục tiêu | Công thức |
|---|---|
| Early Finish | $EF = ES + d$, với $ES = \max(EF \text{ các việc trước})$ |
| Late Start | $LS = LF - d$, với $LF = \min(LS \text{ các việc sau})$ |
| Float | $LS - ES$ |
| Thời gian PERT | $t_e = (t_o + 4t_m + t_p)/6$ |
| Độ lệch chuẩn công việc | $\sigma = (t_p - t_o)/6$ |
| Độ lệch chuẩn dự án | $\sqrt{\sum \sigma_i^2}$ (đường găng) |
| Xác suất đúng hạn | $\Phi\left(\dfrac{D - T_e}{\sigma_{project}}\right)$ |
| Chi phí crash mỗi ngày | $(\text{Chi phí crash} - \text{Chi phí thường})/(\text{Thời gian thường} - \text{Thời gian crash})$ |
| CV, SV | $EV - AC$; $EV - PV$ |
| CPI, SPI | $EV/AC$; $EV/PV$ |
| EAC | $BAC/CPI$ hoặc $AC + (BAC - EV)$ |
| TCPI | $(BAC - EV)/(BAC - AC)$ |
| EMV | $P \times I$ |
| Số sprint còn lại | Backlog còn lại / Velocity trung bình |

### F. Ghi chú kết thúc

File này trình bày các công cụ định lượng cốt lõi của quản trị dự án truyền thống (CPM, PERT, EVM) song song với các phương pháp Agile hiện đại (Scrum, Kanban), phản ánh thực tế nhiều doanh nghiệp áp dụng mô hình Hybrid tuỳ đặc thù từng loại dự án. Người đọc nên thực hành xây dựng WBS và sơ đồ CPM cho một dự án thực tế của mình, đồng thời cân nhắc đặc thù dự án (mức độ rõ ràng của yêu cầu, quy định pháp lý, tốc độ thay đổi thị trường) trước khi chọn phương pháp luận.

---

## TÀI LIỆU THAM KHẢO

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
- LinkedIn Learning: "Agile Project Management" - các khóa học thực hành ngắn hạn.
