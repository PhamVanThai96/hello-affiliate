# Quality Management (Quản Trị Chất Lượng) – TQM, Six Sigma, Lean Manufacturing

> **Mục tiêu**: Giúp người mới hiểu *bản chất* của ba trụ cột Quản trị Chất lượng hiện đại – Total Quality Management (TQM), Six Sigma và Lean Manufacturing – gồm lý thuyết nền tảng, nguồn gốc lịch sử, công thức thống kê (DPMO, Sigma Level, $C_p$/$C_{pk}$, biểu đồ kiểm soát), case study phân tích từng bước (quốc tế & Việt Nam) và cách áp dụng cho SME.

> **Phạm vi tài liệu**: File 2/9 trong bộ Operations Management. Xây dựng trực tiếp trên nền tảng Process Capability ($C_p$, $C_{pk}$) đã giới thiệu ở file `01-process-design-analysis.md`.

> **Quy ước nhãn số liệu**: "**giả định minh họa**" = số do tài liệu tự thiết kế để dạy cách tính (đã kiểm tra nhất quán bằng Python, không phải dữ liệu thật); "**ước tính/công bố**" = con số lịch sử của công ty/nghiên cứu mà tài liệu chưa kiểm chứng được nguồn gốc, chỉ nên coi là tham khảo.

---

## MỤC LỤC

- **I. Khái niệm & Lý thuyết nền tảng** – định nghĩa chất lượng, lịch sử, 3 trụ cột, chi phí chất lượng (COQ), biến động, FPY/RTY
- **II. Chi tiết từng thành phần** – TQM; Six Sigma (DPMO, $C_p$/$C_{pk}$, biểu đồ kiểm soát, DMAIC, FMEA); Lean (7 Wastes, 5S, Kanban, SMED, Poka-Yoke, Jidoka); so sánh; ưu/nhược điểm
- **III. Case Studies thực tế** – Motorola/GE; Vinamilk; chuỗi trà sữa SME; Toyota; xưởng gỗ SME; **xưởng đóng gói cà phê SME (case mới, giả định minh họa)**
- **IV. Ứng dụng cho SME** – lộ trình, chọn dự án, vai trò Champion, quy mô áp dụng, sai lầm thường gặp
- **V. Tools & Templates**
- **VI. Bài tập thực hành** (kèm đáp án tính toán)
- **PHỤ LỤC: Checklist Quality Management tổng hợp** – thuật ngữ, KPI, công thức tổng hợp, sổ tay rủi ro, checklist
- **Tài liệu tham khảo**

---

## I. KHÁI NIỆM & LÝ THUYẾT NỀN TẢNG

### 1.1. Quality Management là gì?

**Quản trị Chất lượng (Quality Management)** là tập hợp các triết lý, công cụ và phương pháp nhằm đảm bảo sản phẩm/dịch vụ đáp ứng *nhất quán* yêu cầu của khách hàng, đồng thời giảm thiểu lãng phí và biến động (variability) trong quy trình.

**Tại sao cần quản trị chất lượng một cách có hệ thống?** Một ly trà sữa ngon hôm nay chưa chứng minh được gì; khách hàng trung thành chỉ ở lại khi ly thứ 100 vẫn ngon như ly thứ nhất. Vấn đề kinh doanh thực sự không phải "làm ra một sản phẩm tốt" mà là "làm ra hàng nghìn sản phẩm tốt như nhau, ở mọi cửa hàng, mọi ca làm". Quản trị chất lượng là khoa học của **sự nhất quán**.

Ba định nghĩa chất lượng kinh điển cần phân biệt:

| Định nghĩa | Tác giả | Trọng tâm |
|---|---|---|
| **"Fitness for Use" (Phù hợp với mục đích sử dụng)** | Joseph Juran | Chất lượng được đánh giá theo góc nhìn khách hàng, không phải nhà sản xuất |
| **"Conformance to Requirements" (Tuân thủ yêu cầu)** | Philip Crosby | Chất lượng là làm đúng ngay từ đầu (Zero Defects), đo bằng chi phí không tuân thủ |
| **"Degree of Excellence" (Mức độ hoàn hảo)** | W. Edwards Deming | Chất lượng gắn liền với cải tiến liên tục (Continuous Improvement) và giảm biến động thống kê |

> Ghi chú: cách diễn đạt cụ thể của Deming về "chất lượng" thay đổi theo từng tác phẩm; bảng trên là cách tóm lược phổ biến trong giáo trình, không phải trích dẫn nguyên văn.

### 1.2. Lịch sử hình thành – Vì sao có ba trường phái?

Hiểu bối cảnh ra đời giúp nhớ công cụ nào giải quyết vấn đề nào:

| Mốc | Sự kiện | Ý nghĩa |
|---|---|---|
| **1924** | Walter Shewhart (Bell Labs, Mỹ) phát minh **biểu đồ kiểm soát (Control Chart)** | Lần đầu phân biệt được "biến động bình thường" và "biến động bất thường" bằng thống kê |
| **Thập niên 1940** | Sản xuất thời chiến Mỹ dùng kiểm soát chất lượng thống kê | Chất lượng trở thành khoa học ứng dụng |
| **1950** | W. E. Deming được Hiệp hội Khoa học & Kỹ sư Nhật Bản (JUSE) mời giảng; Juran sang Nhật ít năm sau | Nhật Bản tái thiết công nghiệp bằng chất lượng; giải thưởng Deming (1951) ra đời |
| **1950s–1970s** | Toyota (Taiichi Ohno, Shigeo Shingo...) xây dựng Toyota Production System: Kanban, Jidoka, SMED, Poka-Yoke | Nền tảng của **Lean** |
| **1960s** | Kaoru Ishikawa phổ biến Quality Circle và biểu đồ xương cá (Fishbone) tại Nhật | Đưa công cụ chất lượng đến tay công nhân |
| **1979** | Philip Crosby xuất bản *Quality is Free* | Chứng minh chất lượng tốt *tiết kiệm* tiền |
| **1986** | Bill Smith, kỹ sư Motorola, đề xuất **Six Sigma** | Cạnh tranh với hàng điện tử Nhật; Motorola đoạt giải Baldrige 1988 |
| **1987** | Tiêu chuẩn **ISO 9001** ra đời lần đầu | Chuẩn hóa quốc tế hệ thống quản lý chất lượng |
| **1990** | Sách *The Machine That Changed the World* (Womack, Jones, Roos) phổ biến thuật ngữ **Lean** | Phương Tây học hệ thống Toyota |
| **1995** | Jack Welch đưa Six Sigma vào GE | Six Sigma thành phong trào quản trị toàn cầu |

**Mạch tư duy xuyên suốt**: Shewhart/Deming dạy *"đo biến động bằng thống kê"* → Toyota dạy *"loại bỏ lãng phí và để lỗi không đi tiếp"* → Motorola/GE gom lại thành *"chương trình có kỷ luật, có đai, có mục tiêu tài chính"*.

### 1.3. Ba trụ cột của Quality Management hiện đại

```
   BA TRỤ CỘT QUẢN TRỊ CHẤT LƯỢNG
   ══════════════════════════════════════════════════════

   TQM (Total Quality        SIX SIGMA               LEAN MANUFACTURING
   Management)               (Giảm biến động          (Loại bỏ lãng phí)
   – Triết lý toàn diện,     bằng thống kê)
     văn hóa tổ chức         – DMAIC, DPMO,           – 7 Wastes (TIMWOOD)
   – Khách hàng là trung       Cpk, Belt system        – 5S, Kanban, JIT
     tâm                     – Nguồn gốc: Motorola,   – Nguồn gốc: Toyota
   – Nguồn gốc: Deming,        GE                       Production System
     Juran, Crosby (Nhật
     Bản 1950s)

              └──────────────────┬──────────────────┘
                                 ▼
                    Mục tiêu chung: Tối đa hóa giá trị
                    cho khách hàng, tối thiểu hóa lãng
                    phí và biến động trong vận hành
```

**Mối quan hệ giữa 3 trụ cột**: TQM cung cấp **triết lý và văn hóa** (tại sao phải làm), Six Sigma cung cấp **công cụ thống kê để giảm biến động** (làm thế nào để nhất quán), Lean cung cấp **công cụ để loại bỏ lãng phí** (làm thế nào để nhanh và tinh gọn). Nhiều doanh nghiệp hiện đại kết hợp cả ba thành **Lean Six Sigma** – phương pháp phổ biến nhất hiện nay.

### 1.4. Chi phí chất lượng (Cost of Quality – COQ)

**Vấn đề kinh doanh**: Nhiều chủ doanh nghiệp tin "chất lượng cao thì tốn kém". Juran và Crosby phản bác bằng cách *đặt giá* cho chất lượng kém. Khi cộng toàn bộ tiền bị mất vì làm sai (làm lại, bảo hành, mất khách...) và tiền bỏ ra để ngăn sai, người ta thấy: **tiền chi cho phòng ngừa thường rẻ hơn tiền trả cho sửa chữa**. COQ biến một khái niệm mơ hồ ("chất lượng") thành con số tài chính mà CEO hiểu được.

$$\text{Total COQ} = \text{Prevention Cost} + \text{Appraisal Cost} + \text{Internal Failure Cost} + \text{External Failure Cost}$$

Nhóm 1+2 là "chi phí tuân thủ" (chủ động bỏ tiền); nhóm 3+4 là "chi phí không tuân thủ" (mất tiền bị động).

| Loại chi phí | Định nghĩa | Ví dụ |
|---|---|---|
| **Prevention Cost (Chi phí phòng ngừa)** | Chi phí để ngăn lỗi xảy ra ngay từ đầu | Đào tạo nhân viên, thiết kế quy trình chuẩn, bảo trì phòng ngừa máy móc |
| **Appraisal Cost (Chi phí thẩm định)** | Chi phí để phát hiện lỗi trước khi đến tay khách hàng | Kiểm tra chất lượng (QC), test sản phẩm, audit |
| **Internal Failure Cost (Chi phí lỗi nội bộ)** | Chi phí xử lý lỗi phát hiện trước khi giao hàng | Hàng lỗi phải làm lại (rework), phế phẩm (scrap) |
| **External Failure Cost (Chi phí lỗi bên ngoài)** | Chi phí xử lý lỗi khách hàng phát hiện sau khi nhận hàng | Bảo hành, đổi trả, mất uy tín thương hiệu, kiện tụng |

**Quy luật 1-10-100 (Rule of Ten – quy tắc kinh nghiệm, không phải định luật chính xác)**: chi phí xử lý một lỗi tăng khoảng 10 lần ở mỗi giai đoạn muộn hơn. Lý do: lỗi càng đi xa, càng "tích tụ" thêm giá trị đã đầu tư vào nó (nguyên liệu, nhân công, vận chuyển) và càng khó truy nguyên.

*Minh họa (giả định minh họa)*: 100 sản phẩm lỗi, chi phí sửa tại trạm gây lỗi 50.000đ/sản phẩm.
- Phát hiện ngay tại trạm: 100 × 50.000 = **5.000.000đ**
- Phát hiện ở kiểm tra cuối chuyền (×10): 100 × 500.000 = **50.000.000đ**
- Khách hàng phát hiện (×100): 100 × 5.000.000 = **500.000.000đ** (chưa tính mất uy tín)

→ Đây là lý do Deming nhấn mạnh "ngừng phụ thuộc vào kiểm tra hàng loạt" và là cơ sở của Jidoka/Poka-Yoke ở phần Lean.

### 1.5. Biến động (Variability) – Kẻ thù chung của chất lượng

**Vấn đề**: Không có hai sản phẩm nào giống hệt nhau. Câu hỏi quản trị là: sự khác biệt này là *bình thường* của quy trình hay do *một sự cố cụ thể*? Trả lời sai dẫn đến hai sai lầm đắt giá: (a) can thiệp vào quy trình đang ổn (trừng phạt nhân viên oan, chỉnh máy liên tục làm biến động tăng thêm); (b) không can thiệp khi có sự cố thực sự.

Shewhart/Deming phân loại:
- **Nguyên nhân phổ biến (Common causes)**: biến động vốn có của hệ thống (độ ẩm dao động nhẹ, hạt cà phê không đồng đều tuyệt đối). Chỉ giảm được bằng cách **thiết kế lại quy trình**.
- **Nguyên nhân đặc biệt (Special causes)**: sự cố cụ thể (một máy hỏng, một lô nguyên liệu bẩn, một nhân viên mới chưa được đào tạo). Giải quyết bằng cách **tìm và loại bỏ nguyên nhân đó**.

$$\sigma^2_{\text{total}} = \sigma^2_{\text{common causes}} + \sigma^2_{\text{special causes}}$$

(Phương sai tổng bằng tổng phương sai của hai nhóm nguyên nhân, giả định độc lập.)

Deming ước tính khoảng 94% vấn đề chất lượng thuộc về hệ thống (do quản lý chịu trách nhiệm) – đây là **ước tính kinh nghiệm của ông, không phải số liệu thực nghiệm chính xác**. Hàm ý quản trị: nếu quy trình ổn định (in control) mà vẫn có lỗi, việc trừng phạt cá nhân là vô ích; cần thay đổi quy trình. Công cụ để phân biệt hai loại nguyên nhân chính là **biểu đồ kiểm soát (mục 2.2.3)**.

### 1.6. First Pass Yield (FPY) và Rolled Throughput Yield (RTY) – "Nhà máy ẩn"

**Vấn đề**: Tỷ lệ "thành phẩm đạt" cuối chuyền (thường 98–99%) che giấu việc nhiều sản phẩm đã phải *làm lại* ở các bước giữa. Những phần làm lại này tốn tiền nhưng không xuất hiện trong báo cáo – gọi là **"nhà máy ẩn" (Hidden Factory)**.

$$FPY = \frac{\text{Số sản phẩm đạt ngay lần đầu, không rework}}{\text{Tổng số sản phẩm đưa vào}} \qquad RTY = FPY_1 \times FPY_2 \times \dots \times FPY_n$$

RTY là xác suất một sản phẩm đi qua *toàn bộ n bước* mà không cần làm lại lần nào (nhân vì các bước nối tiếp nhau và phải đạt tất cả).

*Ví dụ (giả định minh họa)*: Quy trình 5 bước, mỗi bước FPY = 98%.
- $RTY = 0{,}98^5 = 0{,}9039 \approx 90{,}4\%$ → cứ 100 sản phẩm thì ~9,6 sản phẩm phải làm lại ít nhất một lần dù *mỗi bước trông rất tốt (98%)*.
- Nếu nâng mỗi bước lên 99%: $0{,}99^5 = 0{,}9510 = 95{,}1\%$ → tăng 4,7 điểm phần trăm chỉ nhờ cải thiện 1 điểm ở mỗi bước.

**Bài học**: quy trình càng nhiều bước, mỗi bước cần chất lượng càng cao – nền tảng logic của việc Six Sigma nhắm tới 99,99966%.

---

## II. CHI TIẾT TỪNG THÀNH PHẦN

### 2.1. TOTAL QUALITY MANAGEMENT (TQM)

**Định nghĩa**: TQM là triết lý quản trị toàn diện, coi chất lượng là trách nhiệm của **mọi thành viên trong tổ chức** (không chỉ bộ phận QC), tập trung vào sự hài lòng khách hàng và cải tiến liên tục.

**Tại sao cần TQM?** Trước TQM, chất lượng được coi là việc của phòng kiểm tra cuối chuyền: sản xuất làm ra, QC "bắt lỗi". Cách này đắt (Rule of Ten) và tạo xung đột nội bộ ("lỗi là của QC bỏ sót" hay "của sản xuất làm ẩu?"). TQM chuyển trách nhiệm về nơi tạo ra lỗi: mỗi người là "QC của chính công đoạn mình".

#### 2.1.1. 14 Điểm của Deming (Deming's 14 Points)

Deming đề xuất 14 điểm trong *Out of the Crisis* (1982). Bảng sau liệt kê đủ 14 điểm (diễn đạt tóm lược theo cách hiểu phổ biến):

| # | Nguyên tắc | Ứng dụng thực tế |
|---|---|---|
| 1 | Tạo sự nhất quán về mục đích cải tiến sản phẩm/dịch vụ | Tầm nhìn dài hạn, không chạy theo lợi nhuận ngắn hạn |
| 2 | Chấp nhận triết lý mới: không chấp nhận lỗi, sai sót là chuyện bình thường | Lãnh đạo đặt chuẩn "làm đúng ngay từ đầu" |
| 3 | Ngừng phụ thuộc vào kiểm tra hàng loạt để đạt chất lượng | Xây dựng chất lượng vào quy trình thay vì kiểm tra ở cuối |
| 4 | Không chọn nhà cung cấp chỉ dựa trên giá thấp nhất | Chọn nhà cung cấp theo tổng chi phí & độ ổn định chất lượng |
| 5 | Cải tiến liên tục hệ thống sản xuất và dịch vụ | Kaizen – không có "đủ tốt", luôn có thể cải thiện |
| 6 | Đào tạo tại chỗ (on-the-job training) | Đầu tư đào tạo thay vì chỉ tuyển người "sẵn có kỹ năng" |
| 7 | Thiết lập vai trò lãnh đạo (leadership) | Quản lý là người hỗ trợ, không chỉ giám sát |
| 8 | Loại bỏ nỗi sợ hãi (Drive out fear) | Nhân viên dám báo cáo lỗi/vấn đề mà không sợ bị trừng phạt |
| 9 | Phá bỏ rào cản giữa các phòng ban | Cross-functional collaboration, tránh "silo mentality" |
| 10 | Bỏ khẩu hiệu, lời hô hào không kèm phương pháp | "Zero defects!" không có công cụ thì chỉ gây áp lực |
| 11 | Bỏ định mức số lượng thuần túy (quota) | Quota ép công nhân làm ẩu, tăng lỗi |
| 12 | Loại bỏ rào cản khiến nhân viên không tự hào về công việc | Không đánh giá chỉ bằng chỉ tiêu số lượng |
| 13 | Khuyến khích giáo dục và tự hoàn thiện | Học liên tục là chính sách, không phải phúc lợi |
| 14 | Hành động để đạt được sự chuyển đổi | Cam kết từ lãnh đạo cấp cao là điều kiện tiên quyết |

#### 2.1.2. PDCA Cycle (Plan-Do-Check-Act) – Vòng lặp cải tiến liên tục

**Nguồn gốc**: Shewhart đề xuất chu trình "Specification–Production–Inspection"; Deming phổ biến sang Nhật thập niên 1950 (do đó còn gọi là "Deming Cycle"/"Shewhart Cycle"). **Logic**: cải tiến là *thí nghiệm khoa học nhỏ lặp đi lặp lại*, không phải "cải cách lớn một lần". Thử ở quy mô nhỏ để sai thì rẻ; đo kết quả để biết có hiệu quả thật hay chỉ cảm giác.

```
        ┌─────────────────────────────────────────┐
        │                                         │
        ▼                                         │
    ┌───────┐      ┌───────┐      ┌───────┐   ┌───────┐
    │ PLAN  │  →   │  DO   │  →   │ CHECK │ → │  ACT  │
    │(Lập   │      │(Thực  │      │(Kiểm  │   │(Hành  │
    │ kế    │      │ hiện  │      │ tra   │   │ động  │
    │hoạch) │      │ thử   │      │ kết   │   │ chuẩn │
    │       │      │nghiệm)│      │ quả)  │   │ hóa)  │
    └───────┘      └───────┘      └───────┘   └───────┘
        ▲                                         │
        └─────────────────────────────────────────┘
              (Lặp lại liên tục – Kaizen)
```

- **Plan**: Xác định vấn đề, phân tích nguyên nhân gốc rễ, đề xuất giải pháp
- **Do**: Triển khai thử nghiệm ở quy mô nhỏ (pilot)
- **Check**: Đo lường kết quả, so sánh với mục tiêu ban đầu
- **Act**: Nếu hiệu quả → chuẩn hóa và nhân rộng; nếu không → quay lại Plan với bài học rút ra

#### 2.1.3. 7 Nguyên tắc quản lý chất lượng theo ISO 9001:2015

ISO 9001 là phiên bản chuẩn hóa quốc tế của tư duy TQM (ban hành lần đầu 1987; bản 2015 dùng **7 nguyên tắc**; tài liệu cũ ghi "8 nguyên tắc" nhưng chỉ liệt kê 7 là chưa chính xác – đã sửa):

1. Hướng đến khách hàng (Customer Focus)
2. Vai trò lãnh đạo (Leadership)
3. Sự tham gia của con người (Engagement of People)
4. Tiếp cận theo quy trình (Process Approach)
5. Cải tiến (Improvement)
6. Ra quyết định dựa trên bằng chứng (Evidence-based Decision Making)
7. Quản lý mối quan hệ (Relationship Management)

#### 2.1.4. Bảy công cụ kiểm soát chất lượng (7 QC Tools)

**Tại sao có bộ 7 công cụ?** Ishikawa muốn mọi công nhân, không cần giỏi toán, đều dùng được công cụ thống kê để giải quyết vấn đề. Ông cho rằng phần lớn vấn đề tại xưởng có thể giải quyết chỉ bằng 7 công cụ đơn giản này.

| Công cụ | Công dụng |
|---|---|
| **Check Sheet (Phiếu kiểm tra)** | Thu thập dữ liệu lỗi có hệ thống |
| **Pareto Chart (Biểu đồ Pareto)** | Xếp hạng nguyên nhân theo tần suất, áp dụng quy tắc 80/20 |
| **Cause-and-Effect Diagram / Fishbone / Ishikawa** | Phân tích nguyên nhân gốc rễ theo 6 nhóm (6M: Man, Machine, Material, Method, Measurement, Mother Nature/Environment) |
| **Histogram** | Trực quan hóa phân phối dữ liệu, phát hiện độ lệch |
| **Control Chart (Biểu đồ kiểm soát)** | Theo dõi biến động quy trình theo thời gian, phát hiện "out of control" |
| **Scatter Diagram (Biểu đồ phân tán)** | Xác định mối tương quan giữa hai biến số |
| **Stratification (Phân tầng)** | Phân nhóm dữ liệu theo các yếu tố khác nhau để tìm pattern ẩn |

**Pareto – tại sao hiệu quả?** Vilfredo Pareto (1896) quan sát phần lớn đất đai Ý thuộc về một thiểu số dân cư; Juran áp dụng vào chất lượng, gọi là "vital few vs. trivial many" (số ít nguyên nhân sống còn vs. số nhiều nguyên nhân vụn vặt). Nguồn lực có hạn, nên Pareto chỉ ra 2–3 nguyên nhân đáng xử lý trước. Cách làm: xếp loại lỗi giảm dần theo tần suất → tính % tích lũy $= \frac{\text{tần suất cộng dồn}}{\text{tổng tần suất}} \times 100\%$ → chọn các loại lỗi chiếm khoảng 80% đầu tiên. ("80/20" là quy tắc gần đúng, tỷ lệ thật tùy dữ liệu.)

**Ví dụ Fishbone Diagram cho vấn đề "Tỷ lệ trà sữa bị khách phàn nàn quá ngọt/nhạt không đều"**:

```
                              6M FISHBONE DIAGRAM
   ═══════════════════════════════════════════════════════════════

   MAN (Con người)          MACHINE (Máy móc)
   - Không đong theo         - Máy pha không hiệu
     công thức chuẩn           chỉnh định lượng chính xác
   - Thiếu đào tạo                    │
        │                            │
        └──────────┐      ┌──────────┘
                    ▼      ▼
              [TRÀ SỮA VỊ KHÔNG ĐỒNG NHẤT]
                    ▲      ▲
        ┌──────────┘      └──────────┐
        │                            │
   MATERIAL (Nguyên liệu)     METHOD (Phương pháp)
   - Đường/sữa từ nhiều       - Không có SOP công
     nhà cung cấp khác nhau     thức chuẩn bằng văn bản
```

(Một Fishbone đầy đủ còn có nhánh **Measurement** – dụng cụ đong không chuẩn – và **Environment** – nhiệt độ quầy, thời gian đá tan; ở đây chỉ vẽ 4M cho gọn.)

### 2.2. SIX SIGMA

**Định nghĩa**: Six Sigma là phương pháp cải tiến quy trình dựa trên **thống kê**, nhằm giảm biến động xuống mức cực thấp, với mục tiêu lý tưởng chỉ 3,4 lỗi trên một triệu cơ hội (DPMO – Defects Per Million Opportunities).

**Nguồn gốc**: Bill Smith (kỹ sư Motorola) đề xuất năm 1986, trong bối cảnh Motorola bị hàng điện tử Nhật vượt về chất lượng; Mikel Harry và những người khác góp phần hệ thống hóa. Jack Welch đưa vào GE năm 1995. Chi tiết xem Case 3.1.

**Tại sao dùng "sigma" (σ)?** $\sigma$ là *độ lệch chuẩn* – thước đo mức "phân tán" của dữ liệu quanh trung bình. Sigma Level cho biết: *khoảng cách từ trung bình quy trình đến giới hạn cho phép của khách hàng chứa được bao nhiêu độ lệch chuẩn*. Khoảng cách càng chứa nhiều σ → quy trình có nhiều "biên an toàn" → càng ít lỗi. Đây là cách biến chất lượng thành một con số so sánh được giữa mọi quy trình (đóng gói, giao hàng, hóa đơn...), thay vì mỗi nơi một thước đo.

#### 2.2.1. DPMO, Yield và Sigma Level

| Cấp độ Sigma | DPMO (lỗi/triệu cơ hội) | Tỷ lệ đạt chuẩn (Yield) |
|---|---|---|
| 2σ | 308.537 | 69,1% |
| 3σ | 66.807 | 93,3% |
| 4σ | 6.210 | 99,38% |
| 5σ | 233 | 99,977% |
| **6σ** | **3,4** | **99,99966%** |

**Tại sao 6σ chỉ ứng với 3,4 DPMO chứ không phải 0,002 DPMO?** Nếu quy trình hoàn toàn đúng tâm và phân phối chuẩn, giới hạn cách 6σ chỉ cho khoảng 0,002 lỗi/triệu (hai phía). Nhưng Motorola quan sát thực tế: *qua thời gian dài, trung bình quy trình bị "trôi" (drift)* do mòn máy, đổi lô nguyên liệu, đổi ca... Họ quy ước trôi **1,5σ** để tính theo hướng thận trọng (**Shift 1,5σ**). Khi đó "6σ ngắn hạn" tương đương khoảng cách 4,5σ dài hạn tới giới hạn gần nhất:

$$DPMO_{6\sigma} = \bigl(1-\Phi(6-1{,}5)\bigr)\times 10^6 = \bigl(1-\Phi(4{,}5)\bigr)\times 10^6 \approx 3{,}4$$

với $\Phi$ là hàm phân phối tích lũy chuẩn. Tương tự: 3σ → $(1-\Phi(1{,}5))\times10^6 \approx 66.807$. (Con số 1,5σ là *quy ước thực nghiệm* gây tranh cãi trong giới thống kê; nếu không dùng shift, 3σ hai phía = khoảng 2.700 DPMO.) Toàn bộ bảng trên đã được tính lại bằng Python và khớp.

**Công thức tính DPMO**:

$$DPMO = \frac{\text{Số lỗi}}{\text{Số đơn vị} \times \text{Số cơ hội lỗi/đơn vị}} \times 1.000.000$$

*Tại sao phải nhân "số cơ hội lỗi"?* Để so sánh công bằng: một chiếc áo có 4 điểm có thể lỗi "khó đạt chuẩn" hơn một chiếc ly chỉ có 1 điểm. Chuẩn hóa theo cơ hội giúp so sánh quy trình phức tạp với quy trình đơn giản.

Từ DPMO đổi sang Sigma Level (có shift 1,5):

$$\text{Sigma Level} = \Phi^{-1}\!\left(1-\frac{DPMO}{10^6}\right) + 1{,}5$$

(Trong Excel: `=NORM.S.INV(1-DPMO/1000000)+1.5`.)

**Ví dụ từng bước**: Xưởng may kiểm tra 5.000 áo sơ mi, mỗi áo có 4 điểm có thể lỗi (đường may cổ, tay, thân, khuy), phát hiện 45 lỗi.
1. Tổng cơ hội = 5.000 × 4 = 20.000
2. $DPMO = \frac{45}{20.000} \times 1.000.000 = 2.250$
3. Yield $= 1 - 2.250/10^6 = 99{,}775\%$
4. $\Phi^{-1}(1-0{,}00225) = 2{,}84$ → Sigma Level $= 2{,}84 + 1{,}5 \approx 4{,}34\sigma$ – xưởng đang ở mức khá tốt, nhưng còn xa 6σ.

#### 2.2.2. Chỉ số năng lực quy trình $C_p$ và $C_{pk}$ (Process Capability)

**Vấn đề kinh doanh**: Khách hàng quy định *giới hạn cho phép*: Giới hạn trên (USL – Upper Specification Limit) và Giới hạn dưới (LSL – Lower Specification Limit), ví dụ túi cà phê phải nặng 500–520 g. Câu hỏi: *quy trình hiện tại có đủ khả năng làm ra sản phẩm nằm trong khoảng đó một cách ổn định không?* Chỉ nhìn "hôm nay đạt" là không đủ; cần so sánh "độ rộng cho phép" với "độ rộng thực tế của quy trình".

**Cp – Tiềm năng (nếu quy trình đúng tâm)**:

$$C_p = \frac{USL - LSL}{6\sigma}$$

*Logic*: Với phân phối chuẩn, khoảng $\mu \pm 3\sigma$ chứa 99,73% sản phẩm, nên "độ rộng thực tế" của quy trình là $6\sigma$. $C_p$ là tỷ số *"khoảng cho phép / khoảng thực tế"*. $C_p>1$: khoảng thực tế vừa lọt trong khoảng cho phép; $C_p<1$: chắc chắn có sản phẩm ngoài giới hạn. **Hạn chế**: $C_p$ bỏ qua việc quy trình có bị lệch tâm hay không.

**Cpk – Năng lực thực tế (tính cả độ lệch tâm)**:

$$C_{pk} = \min\!\left(\frac{USL-\mu}{3\sigma},\ \frac{\mu-LSL}{3\sigma}\right)$$

*Logic*: lấy khoảng cách từ trung bình đến giới hạn **gần nhất** (phía "nguy hiểm" nhất), chia cho $3\sigma$ (nửa độ rộng quy trình). $C_{pk}\le C_p$ luôn đúng; $C_{pk}=C_p$ khi quy trình đúng tâm. Nếu $C_p$ cao mà $C_{pk}$ thấp → vấn đề là **lệch tâm** (chỉnh lại trung bình thường dễ hơn giảm biến động). Nếu cả hai đều thấp → vấn đề là **biến động quá lớn**, cần cải tiến quy trình sâu hơn.

| $C_{pk}$ | Đánh giá thường dùng (quy ước tham khảo) |
|---|---|
| < 1,00 | Không đủ năng lực, chắc chắn sinh lỗi |
| 1,00 – 1,33 | Tạm chấp nhận, cần kiểm soát chặt |
| ≥ 1,33 | Đạt yêu cầu của nhiều ngành sản xuất |
| ≥ 1,67 | Rất tốt |
| ≈ 1,50 (z = 4,5 tới giới hạn gần nhất) | Mức "Six Sigma có shift 1,5σ" (3,4 DPMO một phía) |

Mối liên hệ: $z = 3\times C_{pk}$ là khoảng cách (tính bằng σ) tới giới hạn gần nhất; $C_{pk}=1{,}5$ ứng với $z=4{,}5$ → 3,4 DPMO một phía – chính là "Six Sigma có shift 1,5σ". (Ngắn hạn, quy trình đúng tâm với $C_p=2$ có khoảng cách 6σ tới mỗi giới hạn.)

**Ví dụ từng bước** (trục máy, giả định minh họa): đường kính yêu cầu 25,00 ± 0,10 mm → LSL = 24,90; USL = 25,10. Dữ liệu: $\mu = 25{,}02$; $\sigma = 0{,}025$.
1. $C_p = \frac{25{,}10-24{,}90}{6\times0{,}025} = \frac{0{,}20}{0{,}15} = 1{,}333$ → tiềm năng tốt.
2. $\frac{USL-\mu}{3\sigma} = \frac{0{,}08}{0{,}075} = 1{,}067$; $\frac{\mu-LSL}{3\sigma} = \frac{0{,}12}{0{,}075} = 1{,}600$ → $C_{pk} = 1{,}067$.
3. Diễn giải: $C_p$ 1,333 nhưng $C_{pk}$ chỉ 1,067 → quy trình *lệch về phía USL* (trung bình 25,02 thay vì 25,00). Chỉ cần chỉnh máy về tâm là $C_{pk}$ tăng lên 1,333.
4. Tỷ lệ ngoài giới hạn: $z_{USL} = 3{,}2$ → ≈ 687 ppm (phía trên); $z_{LSL}=4{,}8$ → ≈ 0,8 ppm; tổng ≈ 688 ppm. Nếu chỉnh đúng tâm: $2\times(1-\Phi(4)) \approx 63$ ppm.

#### 2.2.3. Biểu đồ kiểm soát (Control Chart) – công cụ thống kê của Shewhart

**Vấn đề**: Làm sao biết biến động hôm nay là "bình thường" hay "có chuyện"? Shewhart (1924) lấy mẫu nhỏ theo thời gian, vẽ trung bình mẫu lên biểu đồ cùng **hai đường giới hạn cách trung tâm ±3σ**. Điểm nằm ngoài giới hạn có xác suất rất thấp (khoảng 0,27% nếu quy trình ổn định) → khả năng cao là có nguyên nhân đặc biệt → đi tìm nguyên nhân. Khác với giới hạn kỹ thuật (USL/LSL do *khách hàng* đặt), giới hạn kiểm soát (UCL/LCL) do *chính dữ liệu quy trình* tạo ra – là "giọng nói của quy trình" (Voice of the Process).

**Biểu đồ $\bar{X}$–R (cho dữ liệu liên tục, mẫu con $n$ sản phẩm)**:

$$UCL_{\bar X} = \bar{\bar X} + A_2\bar R \quad;\quad LCL_{\bar X} = \bar{\bar X} - A_2\bar R \quad;\quad UCL_R = D_4\bar R \quad;\quad LCL_R = D_3\bar R$$

Trong đó: $\bar{\bar X}$ = trung bình của các trung bình mẫu; $\bar R$ = trung bình khoảng biến thiên (max − min) các mẫu; $A_2, D_3, D_4$ là hằng số tra bảng theo cỡ mẫu $n$ (với $A_2 = 3/(d_2\sqrt n)$). Ước lượng độ lệch chuẩn của quy trình: $\hat\sigma = \bar R / d_2$.

| n | 3 | 4 | 5 | 6 |
|---|---|---|---|---|
| $A_2$ | 1,023 | 0,729 | 0,577 | 0,483 |
| $D_3$ | 0 | 0 | 0 | 0 |
| $D_4$ | 2,574 | 2,282 | 2,114 | 2,004 |
| $d_2$ | 1,693 | 2,059 | 2,326 | 2,534 |

**Biểu đồ p (cho tỷ lệ sản phẩm lỗi, dữ liệu đếm)**:

$$UCL_p = \bar p + 3\sqrt{\frac{\bar p(1-\bar p)}{n}} \quad;\quad LCL_p = \max\!\Bigl(0,\ \bar p - 3\sqrt{\frac{\bar p(1-\bar p)}{n}}\Bigr)$$

**Quy tắc phát hiện bất thường** (tham khảo, các tài liệu có biến thể nhỏ): (1) một điểm nằm ngoài UCL/LCL; (2) khoảng 8 điểm liên tiếp cùng nằm một phía đường trung tâm; (3) khoảng 6 điểm liên tiếp tăng hoặc giảm dần. Ví dụ tính trọn vẹn xem **Case 3.6** (X̄–R) và **Case 3.3** (biểu đồ p).

> **Phân biệt dễ nhầm**: *In control* (quy trình ổn định) ≠ *Capable* (đáp ứng yêu cầu khách hàng). Một quy trình có thể ổn định nhưng luôn làm ra hàng không đạt ($C_{pk}<1$); ngược lại có thể đạt yêu cầu hôm nay nhưng không ổn định. Cần **cả hai**: dùng control chart để ổn định trước, rồi mới tính $C_p/C_{pk}$.

#### 2.2.4. Quy trình DMAIC – Xương sống của Six Sigma

**Tại sao DMAIC?** Là phiên bản "khoa học hóa" của PDCA cho các vấn đề *đã có quy trình hiện hữu nhưng kết quả chưa đạt*: buộc đội dự án *đo trước, kết luận sau* – tránh lỗi phổ biến là nhảy thẳng vào "giải pháp" dựa trên cảm tính.

```
   D – Define        M – Measure       A – Analyze       I – Improve       C – Control
   (Xác định)         (Đo lường)        (Phân tích)        (Cải tiến)        (Kiểm soát)
   ─────────         ─────────         ─────────         ─────────         ─────────
   • Xác định vấn    • Thu thập dữ     • Tìm nguyên      • Đề xuất &       • Thiết lập
     đề & phạm vi      liệu hiện         nhân gốc rễ        thử nghiệm        Control Chart
     (dùng SIPOC)      trạng             (5-Why, FMEA,      giải pháp        để duy trì
   • Xác định         • Đánh giá        Fishbone)         • Chọn giải       cải tiến
     "Voice of         độ tin cậy      • Xác định biến      pháp tối ưu    • Chuyển giao
     Customer" (VOC)   phép đo         số đầu vào         • Pilot test       cho Process
   • Lập Project      • Tính Cp/Cpk     ảnh hưởng nhiều   • Đo Cp/Cpk       Owner duy trì
     Charter            hiện tại        nhất (Vital Few)   sau cải tiến
```

**Hệ thống Belt (Đai) trong Six Sigma – Phân cấp chuyên môn** (thời lượng đào tạo mang tính tham khảo, khác nhau theo đơn vị đào tạo):

| Cấp độ | Vai trò | Thời gian đào tạo điển hình |
|---|---|---|
| **White Belt** | Hiểu khái niệm cơ bản, tham gia dự án ở vai trò hỗ trợ | 1 ngày |
| **Yellow Belt** | Tham gia dự án cải tiến trong phạm vi công việc của mình | 2-3 ngày |
| **Green Belt** | Dẫn dắt dự án cải tiến quy mô vừa, làm việc bán thời gian cho dự án | 2 tuần |
| **Black Belt** | Dẫn dắt dự án phức tạp toàn thời gian, đào tạo Green Belt | 4 tuần + dự án thực tế |
| **Master Black Belt** | Cố vấn chiến lược, đào tạo Black Belt, giám sát danh mục dự án toàn công ty | Nhiều năm kinh nghiệm |

#### 2.2.5. FMEA (Failure Mode and Effects Analysis) – Phân tích rủi ro trong giai đoạn Analyze

**Nguồn gốc & tại sao**: FMEA được quân đội Mỹ chuẩn hóa từ thập niên 1940, sau đó NASA và ngành ô tô áp dụng rộng rãi (chi tiết lịch sử tham khảo thêm). Vấn đề: một quy trình có hàng chục kiểu lỗi có thể xảy ra, nguồn lực chỉ đủ xử lý vài cái – xử lý cái nào trước? Chỉ xét "tần suất xảy ra" là chưa đủ (lỗi hiếm nhưng gây chết người vẫn phải ưu tiên), cũng không thể chỉ nhìn "mức nghiêm trọng". FMEA nhân ba yếu tố để một con số phản ánh cả ba:

$$RPN (\text{Risk Priority Number}) = \text{Severity} \times \text{Occurrence} \times \text{Detection}$$

Mỗi yếu tố chấm 1-10: Severity (mức nghiêm trọng nếu lỗi xảy ra), Occurrence (khả năng xảy ra), Detection (khả năng phát hiện trước khi đến tay khách hàng – điểm cao nghĩa là **KHÓ** phát hiện). RPN thang 1–1.000; càng cao ưu tiên càng lớn. (Lưu ý: nhân ba thang thứ tự có hạn chế – hai lỗi khác nhau có thể có cùng RPN; thực tế nên xem riêng các lỗi có Severity ≥ 9 dù RPN thấp.)

**Ví dụ FMEA cho quy trình giao đồ ăn online (giả định minh họa)**:

| Failure Mode | Severity (1-10) | Occurrence (1-10) | Detection (1-10) | RPN |
|---|---|---|---|---|
| Giao sai địa chỉ | 8 | 3 | 2 | 8×3×2 = 48 |
| Đồ ăn nguội khi đến tay khách | 6 | 6 | 7 | 6×6×7 = 252 |
| Thiếu món trong đơn hàng | 7 | 4 | 3 | 7×4×3 = 84 |

→ "Đồ ăn nguội" có RPN cao nhất (252) → ưu tiên xử lý trước (hộp giữ nhiệt, tối ưu tuyến giao). *Chấm lại sau cải tiến*: hộp giữ nhiệt giảm Occurrence 6→3, thêm nhiệt kế kiểm tra giảm Detection 7→4 → RPN mới $= 6\times3\times4 = 72$ (giảm 71%).

### 2.3. LEAN MANUFACTURING

**Định nghĩa**: Lean là triết lý và bộ công cụ nhằm **tối đa hóa giá trị cho khách hàng bằng cách tối thiểu hóa lãng phí (waste/muda)**, có nguồn gốc từ Toyota Production System (đã giới thiệu sơ bộ ở file 01, phần VSM).

**Tại sao Lean ra đời?** Sau chiến tranh, Toyota thiếu vốn, thị trường Nhật nhỏ, không thể sản xuất khối lượng lớn kiểu Ford rồi giữ tồn kho khổng lồ. Taiichi Ohno quan sát: phần lớn thời gian và tiền không tạo giá trị cho khách (chờ đợi, vận chuyển, tồn kho, làm lại). Ông xây hệ thống để chỉ làm *đúng thứ khách cần, đúng lúc cần, đúng số lượng*. Với SME Việt Nam vốn ít, tư duy này đặc biệt phù hợp.

#### 2.3.1. Bảy loại lãng phí (7 Wastes – TIMWOOD)

| Loại lãng phí | Tiếng Việt | Ví dụ trong F&B/bán lẻ | Ví dụ trong sản xuất |
|---|---|---|---|
| **T – Transportation** | Vận chuyển thừa | Nguyên liệu di chuyển qua lại nhiều lần giữa kho và bếp | Bán thành phẩm di chuyển xa giữa các trạm |
| **I – Inventory** | Tồn kho dư thừa | Nguyên liệu tươi tồn quá nhiều gây hư hỏng | Nguyên vật liệu/WIP tồn kho quá mức cần thiết |
| **M – Motion** | Thao tác thừa | Nhân viên phải với/cúi người nhiều lần không cần thiết | Công nhân di chuyển xa để lấy dụng cụ |
| **W – Waiting** | Chờ đợi | Khách chờ order, nhân viên chờ nguyên liệu | Máy chờ nguyên liệu, công nhân chờ máy |
| **O – Overproduction** | Sản xuất thừa | Chuẩn bị quá nhiều món ăn dự phòng bị bỏ đi cuối ngày | Sản xuất vượt nhu cầu, tạo tồn kho thành phẩm dư thừa |
| **O – Overprocessing** | Xử lý thừa | Quy trình phê duyệt qua quá nhiều cấp không cần thiết | Gia công/kiểm tra vượt mức yêu cầu khách hàng |
| **D – Defects** | Lỗi/khuyết tật | Món ăn làm sai phải làm lại | Sản phẩm lỗi phải sửa/loại bỏ |

**Lãng phí thứ 8 (bổ sung hiện đại)**: **Skills/Talent Waste** – lãng phí năng lực, ý tưởng, sự sáng tạo của nhân viên khi tổ chức không tạo cơ hội để họ đóng góp cải tiến.

Overproduction được Ohno coi là "lãng phí gốc" vì nó che giấu và sinh ra nhiều lãng phí khác (tồn kho, vận chuyển, chờ đợi...).

#### 2.3.2. 5S – Nền tảng của môi trường làm việc Lean

**Tại sao 5S đứng đầu?** Môi trường lộn xộn che giấu lãng phí: không thấy được lỗi, mất thời gian tìm dụng cụ (Motion/Waiting), dễ nhầm lẫn (Defects). 5S là cách rẻ nhất (gần như 0đ) để làm cho vấn đề "lộ ra" và tạo kỷ luật nền cho mọi cải tiến sau này.

| S (tiếng Nhật) | S (tiếng Anh) | Tiếng Việt | Hành động cụ thể |
|---|---|---|---|
| Seiri | Sort | Sàng lọc | Loại bỏ vật dụng không cần thiết khỏi khu vực làm việc |
| Seiton | Set in Order | Sắp xếp | Sắp xếp vật dụng cần thiết ở vị trí cố định, dễ lấy nhất |
| Seiso | Shine | Sạch sẽ | Vệ sinh khu vực làm việc thường xuyên, kết hợp kiểm tra |
| Seiketsu | Standardize | Săn sóc (chuẩn hóa) | Chuẩn hóa quy trình 3S trên để duy trì |
| Shitsuke | Sustain | Sẵn sàng/Kỷ luật | Xây dựng thói quen, kỷ luật để duy trì lâu dài |

#### 2.3.3. Kanban và nguyên tắc Pull

**Nguồn gốc & tại sao**: Taiichi Ohno (thập niên 1950) lấy cảm hứng từ cách siêu thị Mỹ chỉ bổ sung hàng khi khách lấy đi. Hệ thống **Push** (sản xuất theo dự báo) dễ sản xuất thừa khi dự báo sai; hệ thống **Pull** (sản xuất khi công đoạn sau "kéo") chỉ làm đúng cái đã tiêu thụ. Thẻ Kanban chính là tín hiệu "kéo".

```
   KANBAN BOARD MẪU CHO QUÁN ĂN NHANH
   ══════════════════════════════════════════════

   [ĐÃ NHẬN ĐƠN]  →  [ĐANG CHẾ BIẾN]  →  [SẴN SÀNG]  →  [ĐÃ GIAO]
   ┌─────────┐       ┌─────────┐        ┌─────────┐    ┌─────────┐
   │ Đơn #12 │       │ Đơn #10 │        │ Đơn #9  │    │ Đơn #8  │
   │ Đơn #11 │       │         │        │         │    │ Đơn #7  │
   └─────────┘       └─────────┘        └─────────┘    └─────────┘

   Giới hạn WIP (Work-In-Progress): Chỉ tối đa 3 đơn được
   "Đang chế biến" cùng lúc → tránh quá tải bếp, đảm bảo
   chất lượng từng món thay vì làm ẩu nhiều món cùng lúc
```

**Công thức số thẻ Kanban** (kinh điển trong sản xuất):

$$k = \frac{D \times L \times (1+\alpha)}{C}$$

Trong đó $D$ = nhu cầu/đơn vị thời gian; $L$ = thời gian bổ sung (từ lúc phát thẻ đến lúc hàng về); $\alpha$ = hệ số an toàn; $C$ = số lượng chứa trong mỗi thùng/khay. *Logic*: lượng cần có trong lúc chờ bổ sung $= D \times L$, cộng đệm an toàn, chia cho dung lượng mỗi thẻ.

*Ví dụ (giả định minh họa)*: quán trà sữa bán 120 phần trân châu/giờ ($D=120$), nấu một mẻ bổ sung mất 0,5 giờ ($L=0{,}5$), đệm an toàn 20% ($\alpha=0{,}2$), mỗi khay chứa 10 phần ($C=10$):

$$k = \frac{120 \times 0{,}5 \times 1{,}2}{10} = 7{,}2 \;\Rightarrow\; \text{làm tròn lên } 8 \text{ khay (thẻ)}$$

**Just-in-Time (JIT)**: Triết lý nhập/sản xuất đúng số lượng, đúng thời điểm cần – không sớm hơn, không nhiều hơn. Phân tích chi tiết hơn ở `04-inventory-management.md`.

#### 2.3.4. SMED (Single-Minute Exchange of Die) – Giảm thời gian chuyển đổi

**Nguồn gốc & tại sao**: Shigeo Shingo (làm việc với Toyota, thập niên 1950–60) giảm thời gian thay khuôn ép từ hàng giờ xuống dưới 10 phút. Vấn đề: thời gian chuyển đổi dài buộc nhà máy chạy **lô lớn** để "đáng công thay khuôn" → tồn kho lớn. Rút ngắn chuyển đổi → chạy lô nhỏ, linh hoạt, ít tồn kho.

$$\text{Setup Time} = \text{Internal Setup (máy phải dừng)} + \text{External Setup (làm được khi máy vẫn chạy)}$$

**Nguyên tắc SMED**: (1) tách bước internal/external; (2) chuyển tối đa bước từ internal sang external; (3) cải tiến chính các bước internal (kẹp nhanh, dụng cụ chuẩn).

*Ví dụ (giả định minh họa)*: Máy đóng gói đổi loại túi mất 60 phút, toàn bộ máy dừng. Phân tích: 25 phút là việc chuẩn bị (lấy túi mới, kiểm dụng cụ, vệ sinh khuôn) làm trước được khi máy vẫn chạy → downtime còn 35 phút. Dùng kẹp nhanh giảm phần internal từ 35 xuống 20 phút → downtime = 20 phút. Giảm $\frac{60-20}{60}=66{,}7\%$. Nếu mỗi ngày đổi loại túi 6 lần, tiết kiệm $6 \times 40 = 240$ phút (4 giờ) máy chạy/ngày.

#### 2.3.5. Poka-Yoke (Chống lỗi/Fool-proofing)

Thiết kế quy trình/công cụ sao cho **không thể xảy ra lỗi về mặt vật lý** (hoặc lỗi bị phát hiện ngay), thay vì chỉ dựa vào sự cẩn thận của con người. Shigeo Shingo hệ thống hóa thập niên 1960 từ nhận định "con người sẽ sai, hãy thiết kế để sai không thể xảy ra". Có hai dạng: **ngăn ngừa** (không cho làm sai) và **cảnh báo** (phát hiện ngay khi sai).

| Ví dụ Poka-Yoke | Ngành áp dụng |
|---|---|
| Cổng thẻ USB chỉ cắm được một chiều | Sản xuất điện tử |
| Máy POS bắt buộc nhập đủ thông tin mới cho phép thanh toán | Bán lẻ/F&B |
| Khuôn đóng gói chỉ vừa khít với đúng loại sản phẩm, không thể nhét sai loại | Đóng gói thực phẩm |
| Checklist bắt buộc tick đủ các bước trước khi xuất kho | Logistics |
| Cân điện tử có ngưỡng định sẵn, đèn xanh/đỏ báo đạt/không đạt | F&B, đóng gói |

#### 2.3.6. Jidoka và Andon

**Jidoka** ("tự động hóa có trí tuệ con người"): máy/quy trình tự dừng khi phát hiện bất thường, để lỗi không trôi xuống công đoạn sau. Nguồn gốc thường được dẫn đến máy dệt tự dừng khi đứt sợi của Sakichi Toyoda (cuối thế kỷ 19). **Andon** là hệ thống tín hiệu (đèn/dây kéo) báo vấn đề. Vận dụng Rule of Ten: dừng chuyền sớm thì rẻ hơn nhiều so với sửa hàng loạt hoặc thu hồi. Xem Case 3.4.

### 2.4. So sánh tổng hợp TQM vs Six Sigma vs Lean

| Tiêu chí | TQM | Six Sigma | Lean Manufacturing |
|---|---|---|---|
| **Trọng tâm chính** | Văn hóa & triết lý toàn diện | Giảm biến động bằng thống kê | Loại bỏ lãng phí, tăng tốc độ |
| **Công cụ đặc trưng** | PDCA, 7 QC Tools, ISO 9001 | DMAIC, FMEA, Control Chart, Cpk | VSM, Kanban, 5S, SMED, Poka-Yoke |
| **Đo lường thành công** | Sự hài lòng khách hàng, văn hóa cải tiến | DPMO, Sigma Level, RPN | Lead Time, %VA, WIP giảm |
| **Đòi hỏi kỹ năng thống kê** | Thấp | Cao (bắt buộc) | Trung bình |
| **Thời gian thấy kết quả** | Dài hạn (thay đổi văn hóa) | Trung hạn (dự án 3-6 tháng) | Có thể thấy nhanh (vài tuần) |
| **Phù hợp nhất với** | Toàn bộ tổ chức, mọi cấp | Quy trình có dữ liệu định lượng nhiều | Quy trình có nhiều lãng phí rõ ràng |

**Lean Six Sigma** – Sự kết hợp phổ biến hiện nay: dùng Lean để nhanh chóng loại bỏ lãng phí rõ ràng (quick wins), sau đó dùng Six Sigma DMAIC cho các vấn đề phức tạp cần phân tích thống kê sâu, tất cả đặt trong khung văn hóa TQM (cam kết lãnh đạo, tham gia toàn bộ nhân viên).

### 2.5. Ưu điểm, nhược điểm và mức độ phù hợp

#### 2.5.1. Ưu điểm theo từng phương pháp

| Phương pháp | Ưu điểm | Giải thích |
|---|---|---|
| **TQM** | Tạo văn hóa cải tiến bền vững | Không phụ thuộc vào một vài chuyên gia, mọi nhân viên đều tham gia |
| **TQM** | Chi phí đầu tư ban đầu thấp | Chủ yếu là thay đổi tư duy/quy trình quản lý, không cần công cụ đắt tiền |
| **Six Sigma** | Độ chính xác cao, dựa trên dữ liệu | Loại bỏ tranh cãi chủ quan, quyết định dựa trên bằng chứng thống kê |
| **Six Sigma** | ROI có thể định lượng rõ ràng | Mỗi dự án DMAIC đều có Project Charter với mục tiêu tài chính cụ thể |
| **Lean** | Thấy kết quả nhanh | Nhiều cải tiến (5S, Kanban) có thể triển khai và thấy hiệu quả trong vài tuần |
| **Lean** | Giảm chi phí vận hành trực tiếp | Giảm tồn kho, giảm thời gian chờ trực tiếp giảm chi phí vốn lưu động |

#### 2.5.2. Nhược điểm & rủi ro

| Phương pháp | Nhược điểm | Cách giảm thiểu |
|---|---|---|
| **TQM** | Kết quả chậm, khó đo lường ROI ngắn hạn | Kết hợp với KPI cụ thể (VD: NPS, tỷ lệ khiếu nại) để có "bằng chứng sớm" |
| **TQM** | Dễ trở thành khẩu hiệu (slogan) không thực chất nếu lãnh đạo không cam kết thật | Lãnh đạo cấp cao phải trực tiếp tham gia Gemba Walk, không chỉ ký duyệt văn bản |
| **Six Sigma** | Đòi hỏi kỹ năng thống kê, chi phí đào tạo Belt cao | SME có thể thuê tư vấn Green/Black Belt theo dự án thay vì đào tạo nội bộ toàn thời gian |
| **Six Sigma** | Có thể trở nên quan liêu, quá nhiều giấy tờ cho vấn đề đơn giản | Chỉ áp dụng DMAIC đầy đủ cho vấn đề phức tạp; vấn đề đơn giản dùng PDCA nhanh |
| **Lean** | Có thể đẩy áp lực quá mức lên nhân viên nếu chỉ tập trung "cắt giảm" mà không đầu tư con người | Cân bằng giữa loại bỏ lãng phí và đầu tư đào tạo/phúc lợi nhân viên |
| **Lean** | Giảm tồn kho quá mức (JIT) có thể gây rủi ro gián đoạn chuỗi cung ứng | Đánh giá rủi ro chuỗi cung ứng trước khi áp dụng JIT triệt để (bài học từ đứt gãy chuỗi cung ứng COVID-19) |

#### 2.5.3. Mức độ phù hợp theo loại vấn đề

| Loại vấn đề | Phương pháp phù hợp nhất | Lý do |
|---|---|---|
| Vấn đề văn hóa, thái độ làm việc | TQM | Cần thay đổi tư duy toàn tổ chức, không phải công cụ kỹ thuật |
| Biến động chất lượng khó xác định nguyên nhân | Six Sigma (DMAIC) | Cần phân tích thống kê sâu để tìm biến số ảnh hưởng thực sự |
| Thời gian chờ/lãng phí rõ ràng, dễ quan sát | Lean | Có thể giải quyết nhanh bằng quan sát trực tiếp, không cần thống kê phức tạp |
| Vấn đề phức tạp, nhiều biến số, cần cả tốc độ lẫn độ chính xác | Lean Six Sigma | Kết hợp tốc độ của Lean với độ chính xác của Six Sigma |

---

## III. CASE STUDIES THỰC TẾ

> Cách đọc: mỗi case gồm **bối cảnh → số liệu → tính toán từng bước → ý nghĩa kinh doanh → bài học**. Case quốc tế/doanh nghiệp lớn dùng số liệu công bố (ghi "ước tính/công bố", chưa kiểm chứng độc lập); các phép tính minh họa là "giả định minh họa" đã kiểm tra bằng Python.

### 3.1. Case Study Quốc tế: Motorola & General Electric – Nguồn gốc Six Sigma

#### Bối cảnh
Giữa thập niên 1980, Motorola mất thị phần vào tay các công ty điện tử Nhật Bản có chất lượng vượt trội. Theo nhiều tài liệu lịch sử quản trị, kỹ sư Bill Smith (1986) nhận ra mối liên hệ: sản phẩm *ít phải sửa trong nhà máy* thì cũng *ít hỏng ở tay khách hàng* – nghĩa là "nhà máy ẩn" (mục 1.6) vừa tốn tiền vừa là tín hiệu rủi ro tới khách hàng. Từ đó Motorola chuyển từ thước đo "phần trăm lỗi" sang "lỗi trên triệu cơ hội" và đặt mục tiêu 6σ. Motorola đoạt giải Chất lượng Quốc gia Malcolm Baldrige năm 1988.

#### Tại sao phải nhắm tới 6σ chứ không dừng ở 3σ? – Phân tích từng bước
Sản phẩm điện tử có hàng trăm linh kiện/mối hàn. Xác suất *cả sản phẩm không lỗi* = xác suất mỗi cơ hội đạt, lũy thừa số cơ hội $n$: $Y = (1-d)^n$, với $d$ = tỷ lệ lỗi mỗi cơ hội (theo bảng DPMO có shift 1,5σ).

Giả sử một sản phẩm có $n=100$ cơ hội lỗi (giả định minh họa):

| Mức Sigma | Yield mỗi cơ hội | Yield cả sản phẩm $= (1-d)^{100}$ | Diễn giải |
|---|---|---|---|
| 3σ | 93,32% | $0{,}9332^{100} \approx 0{,}1\%$ | Gần như *không sản phẩm nào* hoàn hảo |
| 4σ | 99,38% | $0{,}99379^{100} \approx 53{,}6\%$ | Gần một nửa phải sửa |
| 5σ | 99,977% | $\approx 97{,}7\%$ | Còn ~2,3% lỗi |
| 6σ | 99,99966% | $\approx 99{,}97\%$ | Hầu như mọi sản phẩm đều đạt |

**Ý nghĩa kinh doanh**: 99,38% ("4σ") nghe rất tốt nhưng với sản phẩm phức tạp lại có nghĩa là *gần một nửa số sản phẩm phải làm lại*. Đó là lý do tiêu chuẩn "chấp nhận 1–2% lỗi" (kiểu 3–4σ) lỗi thời cho sản phẩm nhiều chi tiết, và là logic nền cho con số 3,4 DPMO.

#### Cách thực hiện
Áp dụng DMAIC cho các quy trình trọng yếu, hệ thống Belt, mục tiêu 6σ cho mọi quy trình. Jack Welch đưa Six Sigma vào GE năm 1995, gắn với đánh giá và thăng tiến của lãnh đạo cấp cao; GE đầu tư lớn vào đào tạo Black Belt/Green Belt.

#### Kết quả (công bố, chưa kiểm chứng độc lập – chỉ mang tính tham khảo)
- Motorola công bố tiết kiệm khoảng **16 tỷ USD** trong giai đoạn 1986–2001 (ước tính theo công bố của công ty).
- GE công bố tiết kiệm hơn **12 tỷ USD** trong 5 năm đầu (1996–2000) (ước tính theo tài liệu thường dẫn; một số nguồn khác đưa ra con số khác). Hãy coi đây là *bậc độ lớn*, không phải số liệu kế toán đã kiểm toán.

#### Bài học & góc nhìn phản biện
1. **Cam kết của lãnh đạo cao nhất** (gắn vào thăng tiến) là điều kiện thành công.
2. **Six Sigma tối ưu hóa quy trình đã có; không tự tạo đột phá.** Một số bài báo thương mại cho rằng áp dụng quá cứng nhắc có thể làm chậm đổi mới ở bộ phận R&D (thường được nhắc là trường hợp 3M thập niên 2000 – thông tin báo chí, còn tranh luận). Cân bằng: dùng Six Sigma cho vận hành, dùng cách tiếp cận linh hoạt hơn cho sáng tạo.
3. Với SME: không cần bê nguyên chương trình tập đoàn; cần **tư duy "đo trước, kết luận sau"** (xem Case 3.5, 3.6).

### 3.2. Case Study Việt Nam (Doanh nghiệp lớn): Vinamilk – ISO 9001, ISO 22000/HACCP và tư duy kiểm soát quy trình

#### Bối cảnh
Vinamilk là doanh nghiệp sữa hàng đầu Việt Nam, vừa phục vụ thị trường nội địa vừa xuất khẩu. Sản phẩm thực phẩm có rủi ro an toàn cao (lỗi nhỏ có thể gây hại sức khỏe), và xuất khẩu đòi hỏi chứng minh bằng chứng nhận quốc tế. *Lưu ý nguồn*: số nhà máy (tài liệu cũ nhắc khoảng 13), số quốc gia xuất khẩu (trên 50) và các chứng nhận cụ thể là **thông tin công bố trước đây, cần người dùng kiểm chứng lại với báo cáo thường niên mới nhất**; phần định lượng dưới đây là **giả định minh họa** để dạy kỹ thuật, không phải số liệu thật của Vinamilk.

#### Cách tiếp cận (điểm mấu chốt của TQM)
1. **Hệ thống quản lý theo chuẩn**: ISO 9001 (quản lý chất lượng), ISO 22000/HACCP (an toàn thực phẩm). HACCP (Hazard Analysis and Critical Control Points – Phân tích mối nguy và Điểm kiểm soát tới hạn) được phát triển thập niên 1960 trong chương trình thực phẩm cho phi hành gia; logic: *không chỉ kiểm tra thành phẩm cuối*, mà **tìm các điểm trong quy trình nơi mối nguy có thể bị kiểm soát (CCP)** và theo dõi liên tục tại đó – đúng tinh thần Deming "xây chất lượng vào quy trình".
2. **Đào tạo và văn hóa**: coi chất lượng là trách nhiệm của mọi người; thưởng/phạt gắn chỉ số chất lượng.

#### Phân tích định lượng minh họa: điểm kiểm soát tới hạn "thanh trùng sữa"
Giả sử quy trình thanh trùng nhanh (HTST) yêu cầu nhiệt độ **tối thiểu 72°C trong 15 giây** (thông số phổ biến trong công nghiệp sữa). Chỉ có **giới hạn dưới** (LSL = 72°C); nhiệt cao hơn không vi phạm an toàn. Với một phía, dùng $C_{pl} = \frac{\mu - LSL}{3\sigma}$.

Giả sử nhiệt độ trung bình cài đặt $\mu = 74{,}0°C$ (giả định minh họa). So sánh hai trường hợp độ ổn định thiết bị:

| Kịch bản | $\sigma$ | $C_{pl}$ | $z=\frac{\mu-LSL}{\sigma}$ | Tỷ lệ dưới 72°C |
|---|---|---|---|---|
| A: thiết bị ổn định | 0,5°C | $\frac{74-72}{3\times0{,}5} = 1{,}333$ | 4,0 | $\Phi(-4)\approx 31{,}7$ ppm |
| B: thiết bị dao động | 1,0°C | $\frac{74-72}{3\times1{,}0} = 0{,}667$ | 2,0 | $\Phi(-2)\approx 22.750$ ppm (2,3%) |

**Ý nghĩa kinh doanh**: Chỉ cần $\sigma$ tăng gấp đôi (0,5→1,0), tỷ lệ không đạt tăng gần **718 lần** ($22.750/31{,}7$). Với thực phẩm, 2,3% là không chấp nhận được → cần cảm biến đo liên tục, hiệu chuẩn định kỳ (Prevention) thay vì chỉ kiểm vi sinh sau (Appraisal).

**Ánh xạ sang chi phí chất lượng (COQ)**:

| Hoạt động | Nhóm COQ |
|---|---|
| Đào tạo HACCP, hiệu chuẩn thiết bị thanh trùng, đánh giá nhà cung cấp sữa tươi | Prevention |
| Xét nghiệm vi sinh lô thành phẩm, audit nội bộ | Appraisal |
| Hủy lô sản phẩm không đạt, xử lý lại | Internal Failure |
| Thu hồi sản phẩm, khiếu nại, mất uy tín thương hiệu | External Failure (đắt nhất, theo Rule of Ten) |

#### Bài học
- **ISO không phải đích đến mà là công cụ duy trì kỷ luật**; tránh "làm ISO để có chứng chỉ".
- Với ngành an toàn cao, ưu tiên **Prevention + kiểm soát quy trình liên tục** vì chi phí External Failure có thể làm sụp đổ thương hiệu.

### 3.3. Case Study SME Việt Nam: Chuỗi trà sữa nhỏ áp dụng 5S và Poka-Yoke (giả định minh họa)

#### Bối cảnh
Chuỗi trà sữa "Trà Hạ Long" (tên giả định) có 3 cửa hàng tại Hà Nội, tổng cộng **9.000 đơn/tháng**. Cùng một công thức nhưng vị khác nhau giữa các cửa hàng, gây phàn nàn từ khách hàng trung thành. Quản lý ghi nhận **12% đơn bị phàn nàn về vị không đồng nhất** (ngọt/nhạt không đều).

#### Bước 1 – Đo lường và định lượng thiệt hại (giả định minh họa)
- Số đơn phàn nàn: $9.000 \times 12\% = 1.080$ đơn/tháng
- Chi phí xử lý mỗi đơn (làm lại ly mới + nguyên liệu + công + voucher xin lỗi): **28.000đ** (giả định)
- Thiệt hại: $1.080 \times 28.000 = 30.240.000$đ/tháng (Internal/External Failure)

#### Bước 2 – Phân tích nguyên nhân bằng Fishbone (xem mục 2.1.4)
Nhóm **Method** (không có công thức định lượng chuẩn bằng văn bản, nhân viên "áng chừng" đường/sữa) và **Man** (nhân viên mới đào tạo chưa kỹ) là hai nhánh chủ yếu; nhánh **Machine/Measurement** (cốc đong có vạch không chính xác, mỗi cửa hàng dùng loại cốc khác nhau) bổ sung thêm.

#### Bước 3 – Giải pháp
1. **5S** tại quầy pha chế: sàng lọc dụng cụ không dùng; sắp xếp nguyên liệu theo thứ tự pha, vị trí cố định; dán nhãn; vệ sinh cuối ca; chuẩn hóa bằng ảnh quầy mẫu; kiểm tra định kỳ hàng tuần.
2. **Poka-Yoke**: thay cốc đong bằng **cân điện tử có mức cân định sẵn** (6 cái, 2 cái/cửa hàng) cho đường, topping; không thể "áng chừng".
3. **Check Sheet** đơn giản: nhân viên tự kiểm trước khi giao.

#### Bước 4 – Kết quả sau 6 tuần và hiệu quả tài chính
- Tỷ lệ phàn nàn giảm **12% → 3%**: $9.000 \times 3\% = 270$ đơn
- Đơn phàn nàn giảm: $1.080 - 270 = 810$ đơn/tháng
- Tiết kiệm: $810 \times 28.000 = 22.680.000$đ/tháng
- Chi phí đầu tư: 6 cân × 500.000đ = 3.000.000đ + vật tư 5S/nhãn/bảng SOP ≈ 1.000.000đ = **4.000.000đ** (giả định)
- Hoàn vốn: $\frac{4.000.000}{22.680.000} \approx 0{,}18$ tháng (khoảng 5 ngày)
- Thời gian đào tạo nhân viên mới rút từ 2 tuần xuống 5 ngày nhờ quy trình chuẩn bằng cân định lượng

#### Bước 5 – Duy trì bằng biểu đồ p (Control Chart cho tỷ lệ)
Mỗi tuần lấy ngẫu nhiên $n=300$ đơn, đếm số đơn bị phàn nàn.
- *Trước cải tiến* $\bar p=0{,}12$: $UCL = 0{,}12+3\sqrt{\frac{0{,}12\times0{,}88}{300}} = 0{,}12+3\times0{,}01876 = 17{,}6\%$; $LCL = 6{,}4\%$.
- *Sau cải tiến* $\bar p=0{,}03$: $\sqrt{\frac{0{,}03\times0{,}97}{300}} = 0{,}00985$ → $UCL = 0{,}03+3\times0{,}00985 = 5{,}95\%$; $LCL = \max(0;\,0{,}03-0{,}0295)\approx 0{,}05\%$ (≈ 0).
- *Diễn giải*: tuần có 22 đơn phàn nàn $= \frac{22}{300} = 7{,}33\%$ > UCL 5,95% → **tín hiệu nguyên nhân đặc biệt** (không phải dao động ngẫu nhiên). Điều tra thấy ca tối ở cửa hàng 2 vừa có nhân viên mới chưa được dùng cân → đào tạo lại, tuần sau về ~3%. Nếu không có biểu đồ kiểm soát, chủ quán dễ vừa mắng cả ba cửa hàng (sai) vừa bỏ lỡ nguyên nhân thật.

#### Bài học
SME không cần Six Sigma phức tạp: **5S + Poka-Yoke chi phí thấp (4 triệu đồng) giảm tổn thất ~22,7 triệu/tháng**. Công cụ thống kê đơn giản (biểu đồ p) giúp giữ thành quả.

### 3.4. Case Study Quốc tế: Toyota – Jidoka, Andon và văn hóa dừng chuyền

#### Bối cảnh
Ngoài JIT, trụ cột thứ hai của Toyota Production System là **Jidoka**. Bất kỳ công nhân nào phát hiện bất thường đều có quyền kích hoạt **Andon** (dây kéo/nút bấm) để báo hiệu và, nếu cần, dừng chuyền; đội trưởng đến xử lý ngay tại chỗ (Genchi Genbutsu – "đi và xem tận nơi").

#### Tại sao dừng chuyền lại rẻ hơn? – Phân tích chi phí (giả định minh họa)
Giả định: biên đóng góp mỗi xe 15 triệu đồng; lỗi xuất hiện tại trạm A; nếu không dừng, **30 xe** tiếp theo mang lỗi trước khi bị phát hiện ở cuối chuyền; chi phí sửa cuối chuyền 2 triệu đồng/xe; nếu lọt tới khách hàng, chi phí xử lý 20 triệu đồng/xe (gấp 10 lần theo Rule of Ten).

| Phương án | Tính toán | Chi phí |
|---|---|---|
| (A) Kéo Andon, dừng chuyền 3 phút (mất 3 xe sản lượng) | $3 \times 15$ triệu | **45 triệu** |
| (B) Cho chạy, phát hiện ở cuối chuyền | $30 \times 2$ triệu | **60 triệu** |
| (C) Lỗi lọt tới khách hàng | $30 \times 20$ triệu | **600 triệu** (chưa tính uy tín) |

**Ý nghĩa**: dừng chuyền "mất sản lượng" thật, nhưng vẫn rẻ nhất, và rẻ hơn rất nhiều so với phương án lỗi lọt tới tay khách. Đây là cơ sở kinh tế cho văn hóa "dừng lại khi có lỗi".

#### Kỹ thuật 5-Why – ví dụ phân tích nguyên nhân gốc
Máy dừng vì cầu chì cháy → *Tại sao cầu chì cháy?* Quá tải → *Tại sao quá tải?* Vòng bi thiếu dầu bôi trơn → *Tại sao thiếu dầu?* Bơm dầu không hoạt động hiệu quả → *Tại sao?* Trục bơm bị mòn → *Tại sao?* Không có bộ lọc nên mạt kim loại lọt vào (**nguyên nhân gốc**). Nếu chỉ thay cầu chì (dừng ở Why #1), sự cố sẽ lặp lại. *Hạn chế của 5-Why*: nguyên nhân gốc thường nhiều nhánh; nên dùng kèm Fishbone và dữ liệu.

#### Kết quả và góc nhìn phản biện
Toyota được nhiều tài liệu đánh giá có chất lượng ô tô thuộc nhóm tốt nhất thế giới trong nhiều thập kỷ (tài liệu này không dẫn số liệu cụ thể). Tuy nhiên hệ thống không bất khả xâm phạm: các đợt thu hồi lớn khoảng 2009–2010 (hàng triệu xe, theo nhiều báo cáo) thường được phân tích là hệ quả của tăng trưởng quá nhanh làm yếu văn hóa chất lượng và kênh phản hồi. Bài học: **văn hóa chất lượng cần duy trì liên tục, không phải thành tựu một lần**.

#### Bài học
Trao quyền cho nhân viên tuyến đầu **báo cáo và dừng lại**, kết hợp phân tích nguyên nhân gốc, tạo chất lượng bền vững hơn kiểm tra cuối chuyền. Áp dụng cho SME dịch vụ: "Andon" có thể là quyền của nhân viên tạm dừng một đơn hàng khi phát hiện sai.

### 3.5. Case Study Việt Nam (Sản xuất SME): Xưởng đồ gỗ nội thất áp dụng DMAIC đơn giản hóa (giả định minh họa)

#### Bối cảnh
Xưởng nội thất gỗ "Gỗ Việt Đồng Nai" (tên giả định), 25 công nhân, sản xuất **1.600 sản phẩm/tháng**. Tỷ lệ hàng lỗi bề mặt sơn (bong tróc, không đều màu) khoảng **15%**, gây thiệt hại lớn.

#### Define – Xác định vấn đề bằng tiền
- Số sản phẩm lỗi sơn: $1.600 \times 15\% = 240$ sản phẩm/tháng
- Chi phí xử lý mỗi sản phẩm lỗi (chà nhám, sơn lại, vật liệu, công): **450.000đ** (giả định)
- Thiệt hại sơn lỗi: $240 \times 450.000 = 108.000.000$đ/tháng, chiếm 60% tổng chi phí lỗi toàn xưởng → tổng chi phí lỗi $= 108/0{,}6 = 180$ triệu đồng/tháng → lỗi sơn là nhóm lớn nhất, đáng làm trước.

#### Measure – Thu thập dữ liệu
Trong 2 tuần kiểm 200 sản phẩm, ghi nhận loại lỗi, ca, công nhân: có **30 sản phẩm lỗi** ($30/200 = 15\%$). Mức Sigma hiện tại (coi mỗi sản phẩm là 1 cơ hội): $DPMO = 150.000$ → $\Phi^{-1}(0{,}85)+1{,}5 \approx 1{,}04+1{,}5 = 2{,}54\sigma$.

#### Analyze – Pareto & phân tầng
*Pareto theo loại lỗi (30 lỗi)*:

| Loại lỗi | Số lỗi | % | % tích lũy |
|---|---|---|---|
| Bong tróc sơn | 14 | 46,7% | 46,7% |
| Không đều màu | 10 | 33,3% | 80,0% |
| Chảy sơn | 4 | 13,3% | 93,3% |
| Bụi bẩn | 2 | 6,7% | 100% |

→ Hai loại lỗi đầu chiếm 80% ("vital few").

*Phân tầng theo ca*: giả sử kiểm 110 sản phẩm ca sáng và 90 sản phẩm ca chiều:

| Ca | Số mẫu | Số lỗi | Tỷ lệ lỗi |
|---|---|---|---|
| Sáng | 110 | 9 | 8,2% |
| Chiều | 90 | 21 | 23,3% |

Ca chiều chiếm $21/30 = 70\%$ số lỗi. *Kiểm định ý nghĩa thống kê* (để chắc đây không phải ngẫu nhiên): $p_1=0{,}0818$, $p_2=0{,}2333$, tỷ lệ gộp $\hat p = 30/200 = 0{,}15$:

$$z = \frac{p_2 - p_1}{\sqrt{\hat p(1-\hat p)\left(\frac{1}{n_1}+\frac{1}{n_2}\right)}} = \frac{0{,}1515}{\sqrt{0{,}15\times0{,}85\times(0{,}00909+0{,}01111)}} = \frac{0{,}1515}{0{,}0507} \approx 2{,}99$$

$z\approx 2{,}99 > 1{,}96$ (p ≈ 0,003) → chênh lệch giữa hai ca có ý nghĩa thống kê. Điều tra: độ ẩm xưởng ca chiều cao hơn (giả định ~82% so với ~68% ca sáng) và một số công nhân chưa quen kỹ thuật phun sơn mới.

#### Improve
Lắp 2 máy hút ẩm cho khu sơn (18 triệu/máy), đào tạo lại kỹ thuật phun theo góc chuẩn (4 triệu), điều chỉnh lịch tránh phun sơn vào giờ ẩm cao nhất. Tổng đầu tư $2\times18+4 = 40$ triệu đồng.

#### Control
Check Sheet hàng ngày ghi độ ẩm và tỷ lệ lỗi; dùng biểu đồ p theo tuần để phát hiện sớm lệch.

#### Kết quả và hiệu quả tài chính
- Tỷ lệ lỗi sơn: 15% → **4%** sau 2 tháng; $1.600\times4\% = 64$ sản phẩm lỗi/tháng
- Giảm: $240 - 64 = 176$ sản phẩm/tháng
- Tiết kiệm: $176\times450.000 = 79.200.000$đ ≈ **80 triệu đồng/tháng**
- Hoàn vốn: $\frac{40}{79{,}2} \approx 0{,}5$ tháng
- Mức Sigma: yield 96% → DPMO 40.000 → $\Phi^{-1}(0{,}96)+1{,}5 \approx 1{,}75+1{,}5 = 3{,}25\sigma$ (từ 2,54σ)

#### Bài học
SME hoàn toàn áp dụng được **tinh thần DMAIC** mà không cần chứng chỉ: dữ liệu có hệ thống + công cụ đơn giản (Pareto, phân tầng, kiểm định tỷ lệ) → tìm đúng nguyên nhân thay vì "đổ lỗi cho thợ sơn". Luôn *kiểm chứng* nghi ngờ bằng số: nếu không có kiểm định, chênh lệch 8% vs 23% với mẫu nhỏ có thể chỉ là may rủi.

### 3.6. Case Study SME mới: Xưởng đóng gói cà phê rang xay "Cao Nguyên Xanh" – Cp/Cpk và biểu đồ kiểm soát (giả định minh họa)

> Toàn bộ tên doanh nghiệp và số liệu của case này do tài liệu tự thiết kế để minh họa kỹ thuật Six Sigma ở quy mô SME; các phép tính đã được kiểm tra lại bằng Python.

#### Bối cảnh
"Cao Nguyên Xanh" là cơ sở rang xay cà phê ở Đắk Lắk, 12 nhân sự, đóng gói **40.000 túi 500 g/tháng** bằng máy đóng gói định lượng vít tải bán tự động. Khách hàng (đại lý, siêu thị) quy định khối lượng tịnh **500–520 g/túi**: LSL = 500 g (thấp hơn là thiếu cân, bị khiếu nại/đổi trả), USL = 520 g (cao hơn là tặng thừa quá mức/phải cân lại); mục tiêu 510 g. Giá cà phê giả định 250.000đ/kg = 250đ/g.

Đội ngũ nhận thấy hai biểu hiện: (1) khách phàn nàn túi thiếu cân; (2) chi phí nguyên liệu cao bất thường vì túi nào cũng "dư cân" – chủ xưởng đang *cài máy cao để tránh thiếu cân*, tức dùng tiền để che giấu biến động.

#### Giai đoạn 1 – Đo lường tình trạng ban đầu (Measure)
Lấy dữ liệu 200 túi: trung bình $\mu = 512{,}5$ g, độ lệch chuẩn $\sigma = 4{,}2$ g.

**Bước 1: Cp**
$$C_p = \frac{520-500}{6\times4{,}2} = \frac{20}{25{,}2} = 0{,}794$$
→ $C_p<1$: *ngay cả khi đúng tâm*, độ rộng thực tế của quy trình (25,2 g) rộng hơn khoảng cho phép (20 g) → chắc chắn có túi ngoài giới hạn. Vấn đề cốt lõi là **biến động quá lớn**.

**Bước 2: Cpk**
$$\frac{USL-\mu}{3\sigma} = \frac{520-512{,}5}{12{,}6} = 0{,}595 \qquad \frac{\mu-LSL}{3\sigma} = \frac{512{,}5-500}{12{,}6} = 0{,}992$$
$$C_{pk} = \min(0{,}595;\ 0{,}992) = 0{,}595$$
→ Quy trình lệch về phía USL (cài cao), nên nguy cơ lớn nhất lại là *vượt 520 g*, không phải thiếu cân.

**Bước 3: Tỷ lệ ngoài giới hạn (giả định phân phối chuẩn)**
- Dưới 500 g: $z=\frac{500-512{,}5}{4{,}2} = -2{,}98$ → ≈ 1.459 ppm
- Trên 520 g: $z=\frac{520-512{,}5}{4{,}2} = 1{,}79$ → ≈ 37.073 ppm
- Tổng ≈ **38.532 DPMO** → $\Phi^{-1}(1-0{,}038532)+1{,}5 \approx 3{,}27\sigma$
- Số túi ngoài giới hạn mỗi tháng: $40.000\times0{,}038532 \approx 1.541$ túi

**Bước 4: Quy đổi thành tiền (giả định)**
- *Chi phí túi ngoài giới hạn* (khiếu nại, đổi trả hoặc bóc ra cân lại): 12.000đ/túi → $1.541\times12.000 \approx 18{,}5$ triệu đồng/tháng.
- *Chi phí dư cân* so với mục tiêu 510 g: $(512{,}5-510)\times250\times40.000 = 25.000.000$đ/tháng (tặng khách miễn phí).
- **Tổng tổn thất ≈ 43,5 triệu đồng/tháng.**

#### Giai đoạn 2 – Phân tích (Analyze)
Phân tầng dữ liệu theo máy, ca và lô nguyên liệu; phát hiện: (a) vít tải mòn khiến lượng cà phê mỗi vòng quay không đều; (b) độ ẩm hạt cà phê dao động theo lô làm tỷ trọng thay đổi; (c) không có quy trình hiệu chuẩn cân kiểm hàng ngày; (d) cài máy cao để bù (nguyên nhân lệch tâm). Dùng Fishbone: Machine – vít tải mòn; Material – độ ẩm; Measurement – cân kiểm lệch; Method – không có SOP hiệu chuẩn.

#### Giai đoạn 3 – Cải tiến (Improve)
1. Thay vít tải và bảo trì phòng ngừa theo lịch (Prevention)
2. Lắp **cảm biến khối lượng (load cell)** ở đầu ra, tự báo đèn đỏ khi ngoài 500–520 g (Poka-Yoke dạng cảnh báo)
3. Đo độ ẩm lô hạt đầu vào, chỉ nhận lô trong dải quy định
4. Hiệu chuẩn cân đầu ca bằng quả cân chuẩn; chỉnh trung bình về mục tiêu 510 g
5. Tổng đầu tư (giả định): **50 triệu đồng** (vít tải mới + load cell + quả cân chuẩn + đào tạo)

#### Giai đoạn 4 – Kiểm soát (Control) bằng biểu đồ $\bar X$–R
Mỗi giờ lấy $n=5$ túi liên tiếp. Dữ liệu 12 mẫu con sau cải tiến (g):

| Mẫu | Giá trị 5 túi | $\bar X$ | R |
|---|---|---|---|
| 1 | 510, 513, 507, 512, 509 | 510,2 | 6 |
| 2 | 511, 508, 514, 509, 512 | 510,8 | 6 |
| 3 | 508, 512, 510, 512, 508 | 510,0 | 4 |
| 4 | 512, 509, 511, 506, 510 | 509,6 | 6 |
| 5 | 510, 513, 508, 511, 509 | 510,2 | 5 |
| 6 | 509, 512, 507, 511, 513 | 510,4 | 6 |
| 7 | 511, 508, 512, 510, 513 | 510,8 | 5 |
| 8 | 510, 513, 509, 508, 512 | 510,4 | 5 |
| 9 | 511, 509, 511, 514, 508 | 510,6 | 6 |
| 10 | 510, 511, 506, 512, 509 | 509,6 | 6 |
| 11 | 516, 518, 515, 519, 517 | 517,0 | 4 |
| 12 | 510, 509, 513, 507, 511 | 510,0 | 6 |

**Bước 1 – Đường giới hạn từ 10 mẫu đầu (giai đoạn thiết lập, quy trình ổn định)**:
- $\bar{\bar X} = \frac{510{,}2+510{,}8+510{,}0+509{,}6+510{,}2+510{,}4+510{,}8+510{,}4+510{,}6+509{,}6}{10} = 510{,}26$ g
- $\bar R = \frac{6+6+4+6+5+6+5+5+6+6}{10} = 5{,}5$ g

**Bước 2 – Giới hạn kiểm soát** (n = 5: $A_2=0{,}577$; $D_4=2{,}114$; $d_2=2{,}326$):
- $UCL_{\bar X} = 510{,}26 + 0{,}577\times5{,}5 = 513{,}43$ g
- $LCL_{\bar X} = 510{,}26 - 0{,}577\times5{,}5 = 507{,}09$ g
- $UCL_R = 2{,}114\times5{,}5 = 11{,}63$ g; $LCL_R = 0$

**Bước 3 – Phát hiện tín hiệu**: Mẫu 11 có $\bar X = 517{,}0 > UCL = 513{,}43$ → **ngoài kiểm soát**, trong khi R = 4 vẫn bình thường (độ phân tán không đổi nhưng *trung bình bị nhảy*). Điều tra: cảm biến đầu ra bị lệch zero sau khi vệ sinh máy. Hiệu chuẩn lại → mẫu 12 trở về 510,0. **Ý nghĩa**: biểu đồ giúp phát hiện sự cố trong vòng 1 giờ thay vì sau khi cả lô hàng đã đóng xong.

**Bước 4 – Ước lượng năng lực sau cải tiến** (dùng 10 mẫu ổn định):
$$\hat\sigma = \frac{\bar R}{d_2} = \frac{5{,}5}{2{,}326} = 2{,}36 \text{ g} \qquad C_p = \frac{20}{6\times2{,}36} = 1{,}41$$
$$\frac{USL-\mu}{3\sigma} = \frac{520-510{,}26}{7{,}09} = 1{,}373 \qquad \frac{\mu-LSL}{3\sigma} = \frac{510{,}26-500}{7{,}09} = 1{,}447 \qquad C_{pk} = \min(1{,}373;\ 1{,}447) = 1{,}37$$
- Tỷ lệ ngoài giới hạn: $z_{USL}=4{,}12$ → ≈ 19 ppm; $z_{LSL}=4{,}34$ → ≈ 7 ppm; tổng ≈ **26 DPMO** → Sigma Level $\approx 5{,}54\sigma$
- Số túi ngoài giới hạn: $40.000\times26/10^6 \approx 1$ túi/tháng (từ 1.541 túi)

#### Giai đoạn 5 – Hiệu quả tài chính

| Chỉ tiêu | Trước | Sau | Thay đổi |
|---|---|---|---|
| Trung bình $\mu$ (g) | 512,5 | 510,26 | −2,24 |
| Độ lệch chuẩn $\sigma$ (g) | 4,2 | 2,36 | −44% |
| $C_p$ | 0,794 | 1,41 | +0,62 |
| $C_{pk}$ | 0,595 | 1,37 | +0,78 |
| DPMO | 38.532 | ≈ 26 | −99,9% |
| Sigma Level | 3,27σ | 5,54σ | +2,27σ |
| Túi ngoài giới hạn/tháng | ≈ 1.541 | ≈ 1 | −1.540 |
| Chi phí túi ngoài giới hạn | ≈ 18,5 triệu | ≈ 0 | −18,5 triệu |
| Chi phí dư cân so với 510 g | 25,0 triệu | $(510{,}26-510)\times250\times40.000 = 2{,}6$ triệu | −22,4 triệu |

- **Tiết kiệm hàng tháng ≈ 18,5 + 22,4 ≈ 40,9 triệu đồng**
- **Hoàn vốn**: $\frac{50}{40{,}9} \approx 1{,}2$ tháng
- *Ý nghĩa kinh doanh*: chất lượng cao hơn **và** chi phí thấp hơn đồng thời – bác bỏ quan niệm "chất lượng tốn tiền". Đây là kết quả của việc *giảm biến động* (σ giảm 44%) nên mới hạ được trung bình về 510 g mà vẫn an toàn. Nếu chỉ hạ trung bình xuống 510 g mà giữ σ = 4,2, tỷ lệ ngoài giới hạn sẽ tăng vọt: $z=\frac{\pm10}{4{,}2}=\pm2{,}38$ → mỗi phía ≈ 8.634 ppm, tổng ≈ 17.268 ppm (≈ 1,7%, tức ~690 túi/tháng) – tệ hơn nhiều so với 26 DPMO.

#### Bài học & khuyến nghị
1. **Dùng $C_p$ và $C_{pk}$ cùng nhau**: $C_p$ báo quy trình có *tiềm năng* không; $C_{pk}$ báo thực tế có *lệch tâm* không. Case này vừa biến động lớn vừa lệch tâm.
2. **Đừng dùng "dư cân" để che biến động**: đó là chi phí ẩn thường xuyên (25 triệu đồng/tháng).
3. **Ổn định trước, năng lực sau**: biểu đồ kiểm soát cho thấy quy trình ổn định (10 mẫu đầu) trước khi tính $C_{pk}$ – nếu không ổn định, $C_{pk}$ không đáng tin.
4. Cần kiểm tra giả định phân phối chuẩn bằng histogram trước khi dùng công thức; cỡ mẫu chỉ là ví dụ.
5. Khuyến nghị tiếp theo: mở rộng sang dòng 250 g và 1 kg; thêm cân kiểm tự động (checkweigher) cuối chuyền khi sản lượng tăng.

### 3.7. Bảng tổng hợp bài học từ 6 case study

| Case study | Quy mô | Phương pháp chính | Kết quả định lượng | Bài học cốt lõi |
|---|---|---|---|---|
| Motorola/GE | Tập đoàn đa quốc gia | Six Sigma, DMAIC, Belt | Yield 100 cơ hội: 4σ ≈ 53,6% vs 6σ ≈ 99,97%; tiết kiệm công bố hàng chục tỷ USD (ước tính) | Cam kết lãnh đạo cao nhất; sản phẩm phức tạp cần 6σ |
| Vinamilk | Tập đoàn lớn | TQM, ISO 9001/22000, HACCP | Minh họa: σ 0,5→1,0 làm tỷ lệ không đạt tăng ~718 lần | ISO là công cụ, ưu tiên Prevention và kiểm soát quy trình |
| Trà sữa SME | 3 cửa hàng | 5S, Poka-Yoke, Fishbone, biểu đồ p | Phàn nàn 12%→3%; tiết kiệm 22,68 triệu/tháng; đầu tư 4 triệu | Công cụ rẻ vẫn hiệu quả cao |
| Toyota | Tập đoàn đa quốc gia | Jidoka, Andon, 5-Why | Minh họa: dừng chuyền 45 triệu vs lọt khách 600 triệu | Trao quyền dừng lại; văn hóa cần duy trì |
| Xưởng gỗ SME | 25 công nhân | DMAIC đơn giản, Pareto, kiểm định tỷ lệ | Lỗi 15%→4%; tiết kiệm ~79,2 triệu/tháng; 2,54σ→3,25σ | Kiểm chứng nghi ngờ bằng dữ liệu |
| Xưởng cà phê SME (mới) | 12 nhân sự | Cp/Cpk, biểu đồ X̄–R, Poka-Yoke | $C_{pk}$ 0,595→1,37; DPMO 38.532→≈26; tiết kiệm ≈ 40,9 triệu/tháng | Giảm biến động trước, rồi mới hạ trung bình |

---

## IV. ỨNG DỤNG CHO SME

### 4.1. Lộ trình triển khai Quality Management cho tổ chức mới bắt đầu

```
GIAI ĐOẠN 1: NỀN TẢNG (Tháng 1-2)
   → Xây dựng văn hóa TQM cơ bản: Cam kết lãnh đạo, đào tạo 7 QC Tools cho quản lý
   → Áp dụng 5S tại các khu vực làm việc chính

GIAI ĐOẠN 2: ĐO LƯỜNG (Tháng 3-4)
   → Thiết lập Check Sheet thu thập dữ liệu lỗi có hệ thống
   → Tính toán Cost of Quality (COQ) hiện tại làm baseline

GIAI ĐOẠN 3: PHÂN TÍCH & CẢI TIẾN (Tháng 5-8)
   → Chọn 1-2 vấn đề ưu tiên cao nhất (Pareto 80/20)
   → Áp dụng PDCA hoặc DMAIC đơn giản hóa tùy độ phức tạp
   → Thử nghiệm giải pháp (Poka-Yoke, SMED, thay đổi quy trình)

GIAI ĐOẠN 4: CHUẨN HÓA & MỞ RỘNG (Tháng 9-12)
   → Chuẩn hóa giải pháp thành công bằng SOP
   → Thiết lập Control Chart để giám sát liên tục
   → Mở rộng phương pháp sang các vấn đề/bộ phận khác
```

### 4.2. Cách chọn dự án cải tiến chất lượng đầu tiên (Project Selection)

**Tại sao cần chấm điểm?** SME nguồn lực ít; chọn sai dự án (quá lớn, thiếu dữ liệu) dễ thất bại và làm đội ngũ mất niềm tin vào phương pháp. Ma trận trọng số buộc ta so sánh các ứng viên theo cùng tiêu chí thay vì chọn theo cảm tính.

| Tiêu chí đánh giá | Câu hỏi cần trả lời | Trọng số khuyến nghị |
|---|---|---|
| Tác động tài chính | Vấn đề này gây thiệt hại bao nhiêu tiền/tháng? | 30% |
| Tác động khách hàng | Vấn đề này ảnh hưởng trực tiếp đến bao nhiêu % khách hàng? | 25% |
| Khả năng thực thi | Có đủ dữ liệu và nguồn lực để giải quyết trong 2-3 tháng không? | 20% |
| Khả năng nhân rộng | Giải pháp có thể áp dụng cho các vấn đề tương tự khác không? | 15% |
| Cam kết của đội ngũ | Đội ngũ liên quan có sẵn sàng tham gia thay đổi không? | 10% |

**Ví dụ chấm điểm (giả định minh họa, thang 1–10)** cho chuỗi trà sữa ở Case 3.3:

| Ứng viên | Tài chính (30%) | Khách hàng (25%) | Thực thi (20%) | Nhân rộng (15%) | Cam kết (10%) | Điểm tổng |
|---|---|---|---|---|---|---|
| A. Vị trà không đồng nhất | 8 | 9 | 8 | 7 | 8 | $0{,}3\times8+0{,}25\times9+0{,}2\times8+0{,}15\times7+0{,}1\times8 = \mathbf{8{,}1}$ |
| B. Giao hàng trễ | 7 | 8 | 4 | 6 | 5 | $2{,}1+2{,}0+0{,}8+0{,}9+0{,}5 = \mathbf{6{,}3}$ |
| C. Lỗi in hóa đơn | 4 | 3 | 9 | 5 | 7 | $1{,}2+0{,}75+1{,}8+0{,}75+0{,}7 = \mathbf{5{,}2}$ |

→ Chọn A làm dự án đầu tiên. **Nguyên tắc**: ưu tiên dự án *dễ đạt thành công nhanh (quick win)* để xây dựng niềm tin, tránh chọn ngay vấn đề quá phức tạp.

### 4.3. Vai trò của Champion và Quality Circle

- **Quality Champion**: Lãnh đạo cấp cao chịu trách nhiệm bảo trợ (sponsor) chương trình chất lượng, phân bổ nguồn lực, tháo gỡ rào cản liên phòng ban
- **Quality Circle (Vòng tròn chất lượng)**: Nhóm nhỏ 5-8 nhân viên tuyến đầu họp định kỳ (VD: 30 phút/tuần) để thảo luận vấn đề chất lượng và đề xuất cải tiến – mô hình phổ biến ở Nhật từ thập niên 1960, giúp khai thác kiến thức thực tế của người trực tiếp làm việc

### 4.4. Quy mô áp dụng – SME vs Doanh nghiệp lớn

| Khía cạnh | SME nhỏ (1-10 nhân viên) | SME vừa (10-50 nhân viên) | Doanh nghiệp lớn (500+ nhân viên) |
|---|---|---|---|
| **Phương pháp phù hợp** | 5S, Poka-Yoke đơn giản, Check Sheet | PDCA, Fishbone, Pareto Chart, biểu đồ kiểm soát cơ bản | Full DMAIC, Six Sigma Belt system, ISO certification |
| **Người thực hiện** | Chủ doanh nghiệp | Quản lý chất lượng kiêm nhiệm | Đội ngũ Quality/Six Sigma chuyên trách |
| **Chi phí đầu tư ban đầu (ước tính)** | Gần như 0 (thay đổi quy trình, mua công cụ đơn giản) | 5-20 triệu đồng (đào tạo cơ bản, công cụ đo lường) | Hàng trăm triệu-hàng tỷ đồng (ISO certification, phần mềm QMS) |
| **Chứng nhận cần thiết** | Không bắt buộc | VSATTP nếu là F&B | ISO 9001/14001/22000, HACCP, chứng nhận xuất khẩu |
| **Tần suất đo lường** | Khi có vấn đề rõ ràng | Hàng tuần/tháng | Liên tục, real-time dashboard |

### 4.5. Khuyến nghị theo giai đoạn phát triển

**SME mới bắt đầu**: Tập trung vào **TQM tinh thần đơn giản** – xây dựng thói quen "làm đúng ngay từ đầu", dùng Check Sheet giấy để ghi nhận lỗi, áp dụng 5S cho khu vực làm việc. Chưa cần đầu tư Six Sigma hay ISO ở giai đoạn này.

**SME chuẩn bị mở rộng/nhượng quyền**: Cần **chuẩn hóa chất lượng bằng văn bản (SOP)**, cân nhắc chứng nhận VSATTP/ISO cơ bản nếu ngành yêu cầu, để đảm bảo chất lượng đồng nhất khi nhân rộng nhiều điểm bán.

**Doanh nghiệp lớn/hướng xuất khẩu**: Cần đầu tư Six Sigma bài bản với đội ngũ Belt chuyên trách, chứng nhận ISO quốc tế, hệ thống QMS (Quality Management System) tích hợp với ERP.

### 4.6. Các lỗi phổ biến khi SME áp dụng Quality Management

| Lỗi phổ biến | Hậu quả | Cách khắc phục |
|---|---|---|
| Cố áp dụng Six Sigma đầy đủ ngay từ đầu (quá phức tạp so với quy mô) | Tốn thời gian, nhân viên không hiểu và không áp dụng được | Bắt đầu với PDCA và 7 QC Tools đơn giản trước |
| Chỉ kiểm tra chất lượng ở khâu cuối, không đầu tư phòng ngừa | Chi phí xử lý lỗi cao (theo Rule of Ten), phát hiện quá muộn | Đầu tư vào Poka-Yoke và đào tạo tại các điểm có nguy cơ lỗi cao |
| Đổ lỗi cho nhân viên khi có vấn đề chất lượng thay vì xem xét hệ thống | Nhân viên sợ hãi, che giấu lỗi thay vì báo cáo (theo nguyên tắc Deming) | Xây dựng văn hóa "an toàn tâm lý" khi báo cáo lỗi, tập trung cải tiến hệ thống |
| Không có dữ liệu định lượng, chỉ dựa vào cảm nhận | Không xác định đúng nguyên nhân gốc rễ, giải pháp sai trọng tâm | Luôn thu thập dữ liệu (Check Sheet) tối thiểu 2 tuần trước khi kết luận |
| Chỉnh máy/chỉnh công thức liên tục mỗi khi thấy một kết quả lệch (tampering) | Làm biến động tăng thêm (Deming) | Dùng biểu đồ kiểm soát để chỉ can thiệp khi có tín hiệu đặc biệt |
| Bù biến động bằng cách "cài dư" (như Case 3.6) | Chi phí ẩn thường xuyên | Giảm σ trước, rồi mới hạ trung bình |

---

## V. TOOLS & TEMPLATES

| Công cụ | Loại | Chi phí (ước tính, cần kiểm tra giá hiện hành) | Phù hợp |
|---|---|---|---|
| **Google Sheets/Excel** | Check Sheet, Pareto Chart, Control Chart cơ bản; hàm `NORM.S.DIST`/`NORM.S.INV` để tính DPMO | Miễn phí | Mọi quy mô |
| **Minitab** | Phần mềm thống kê chuyên dụng cho Six Sigma | ~1.500 USD/năm (ước tính) | Doanh nghiệp vừa/lớn có dự án Six Sigma |
| **SigmaXL (Excel Add-in)** | Công cụ Six Sigma tích hợp Excel | ~500 USD/năm (ước tính) | SME vừa muốn bắt đầu Six Sigma nhẹ |
| **Canva/PowerPoint** | Vẽ Fishbone Diagram, trình bày báo cáo | Miễn phí/chi phí thấp | Mọi quy mô |
| **Trello/Asana** | Quản lý dự án cải tiến chất lượng (PDCA/DMAIC tracking), Kanban board | Miễn phí (bản cơ bản) | SME |
| **Tư vấn ISO 9001 local** | Chứng nhận & tư vấn triển khai | 30-80 triệu đồng (ước tính, tùy quy mô) | SME chuẩn bị xuất khẩu/đấu thầu |

**Công thức Excel hữu ích** (giả sử dữ liệu nằm ở `A2:A201`, LSL ở `E1`, USL ở `E2`):
- Trung bình: `=AVERAGE(A2:A201)`; độ lệch chuẩn mẫu: `=STDEV.S(A2:A201)`
- $C_p$: `=(E2-E1)/(6*STDEV.S(A2:A201))`
- $C_{pk}$: `=MIN((E2-AVERAGE(A2:A201)),(AVERAGE(A2:A201)-E1))/(3*STDEV.S(A2:A201))`
- DPMO từ $C_{pk}$ (hai phía gần đúng): `=(NORM.S.DIST(-(3*Cpk),TRUE))*1000000`
- Sigma Level từ DPMO: `=NORM.S.INV(1-DPMO/1000000)+1.5`

### Template Check Sheet đơn giản (Excel/giấy)

```
┌──────────┬────────────┬─────────────┬────────────┬───────────┐
│  Ngày    │  Ca làm    │  Loại lỗi   │  Số lượng  │  Ghi chú  │
├──────────┼────────────┼─────────────┼────────────┼───────────┤
│ [Điền]   │  Sáng/     │  [Mô tả cụ  │  |||| (đếm │ [Điền]    │
│          │  Chiều/Tối │   thể]      │  vạch)     │           │
└──────────┴────────────┴─────────────┴────────────┴───────────┘
```

### Template Project Charter (DMAIC đơn giản hóa cho SME)

```
1. Tên dự án: ______________________
2. Vấn đề (Problem Statement): ______________________
3. Mục tiêu định lượng (VD: Giảm tỷ lệ lỗi từ X% xuống Y%): ______________________
4. Phạm vi (Scope): ______________________
5. Thành viên tham gia: ______________________
6. Thời gian dự kiến hoàn thành: ______________________
7. Lợi ích tài chính ước tính: ______________________
```

### Template Bảng FMEA

```
┌───────────┬──────────┬────┬────┬────┬─────┬──────────────┬────┬────┬────┬─────────┐
│ Công đoạn │ Failure  │ S  │ O  │ D  │ RPN │ Hành động    │ S' │ O' │ D' │ RPN mới │
│           │ Mode     │    │    │    │     │ khắc phục    │    │    │    │         │
└───────────┴──────────┴────┴────┴────┴─────┴──────────────┴────┴────┴────┴─────────┘
```

---

## VI. BÀI TẬP THỰC HÀNH

> Bài có tính toán kèm đáp án (đã kiểm tra bằng Python); bài định tính kèm hướng dẫn giải.

**Bài 1**: Tính DPMO và Sigma Level cho quy trình đóng gói kiểm tra 2.000 hộp, mỗi hộp có 3 điểm kiểm tra (nhãn, niêm phong, số lượng), phát hiện 30 lỗi.
*Đáp án*: Cơ hội $= 2.000\times3 = 6.000$; $DPMO = \frac{30}{6.000}\times10^6 = 5.000$; yield $= 99{,}5\%$; Sigma $= \Phi^{-1}(0{,}995)+1{,}5 = 2{,}576+1{,}5 \approx 4{,}08\sigma$.

**Bài 2**: Vẽ Fishbone Diagram (6M) cho vấn đề "Khách hàng phàn nàn giao hàng trễ" của một shop online.
*Hướng dẫn*: Man (đóng gói chậm, thiếu nhân sự cao điểm); Machine (máy in vận đơn lỗi); Material (hộp/bao bì thiếu); Method (không có quy trình chốt đơn trước giờ cut-off); Measurement (không đo thời gian xử lý từng khâu); Environment (mưa bão, cao điểm sale). Sau đó dùng Check Sheet thu thập dữ liệu và Pareto để chọn nhánh nguyên nhân chính.

**Bài 3**: Xây dựng bảng FMEA cho quy trình "Pha chế cà phê" với ít nhất 3 Failure Modes, tính RPN và xác định ưu tiên.
*Đáp án mẫu (giả định minh họa)*:

| Failure Mode | S | O | D | RPN |
|---|---|---|---|---|
| Sai tỷ lệ cà phê/nước | 7 | 5 | 6 | 7×5×6 = **210** |
| Nhiệt độ nước không đạt | 5 | 4 | 5 | 5×4×5 = 100 |
| Nhầm đơn (sai món) | 6 | 4 | 4 | 6×4×4 = 96 |
| Cốc/dụng cụ dính bẩn | 9 | 2 | 3 | 9×2×3 = 54 |

Ưu tiên: sai tỷ lệ (210) → Poka-Yoke bằng máy định lượng/cân; sau cải tiến chấm lại O 5→2, D 6→3: RPN mới $= 7\times2\times3 = 42$ (giảm 80%). Lưu ý "cốc dính bẩn" RPN thấp nhưng Severity = 9 vẫn cần giữ quy trình vệ sinh nghiêm ngặt.

**Bài 4**: Áp dụng kỹ thuật 5-Why cho vấn đề "Nhân viên thường xuyên đi trễ".
*Hướng dẫn (ví dụ)*: Vì sao đi trễ? Vì ca bắt đầu 7h mà xe buýt tuyến gần nhất tới 7h05 → Vì sao xếp ca 7h? Vì lịch ca thiết kế theo giờ mở cửa, không theo thực tế di chuyển → Vì sao không điều chỉnh? Vì chưa ai khảo sát nơi ở của nhân viên → ... nguyên nhân gốc: *quy trình xếp ca không dựa trên dữ liệu*, chứ không phải "nhân viên thiếu ý thức". Đáp án đúng cần dừng ở nguyên nhân hệ thống mà quản lý kiểm soát được.

**Bài 5**: Thiết kế một giải pháp Poka-Yoke đơn giản cho một quy trình bạn thấy thường xảy ra lỗi do con người.
*Hướng dẫn*: Xác định lỗi → chọn dạng *ngăn ngừa* (khuôn/đồ gá chỉ lắp đúng một cách) hoặc *cảnh báo* (đèn/âm thanh/checklist bắt buộc) → thử nghiệm 2 tuần → đo tỷ lệ lỗi trước/sau.

**Bài 6**: So sánh Cost of Quality (COQ) của phương án "kiểm tra 100% cuối chuyền" với "đầu tư phòng ngừa" cho một xưởng giả định có doanh thu 10.000 triệu đồng/năm.
*Đáp án (giả định minh họa; đơn vị triệu đồng/năm)*:

| Nhóm chi phí | A: kiểm tra 100% cuối chuyền | B: đầu tư phòng ngừa |
|---|---|---|
| Prevention | 50 | 300 |
| Appraisal | 400 | 200 |
| Internal Failure | 600 | 250 |
| External Failure | 500 | 100 |
| **Tổng COQ** | **1.550** (15,5% doanh thu) | **850** (8,5% doanh thu) |

Phương án B tăng Prevention thêm 250 nhưng tiết kiệm tổng $1.550-850 = 700$ triệu/năm (7,0 điểm phần trăm doanh thu: 15,5% − 8,5%) – chứng minh "phòng ngừa rẻ hơn sửa chữa".

**Bài 7**: Thực hiện 5S cho một không gian làm việc thực tế (bàn làm việc, tủ bếp), chụp ảnh trước/sau. *Hướng dẫn*: đo thời gian tìm một món đồ trước/sau làm số liệu.

**Bài 8**: Lập Project Charter DMAIC đơn giản cho một vấn đề chất lượng bạn từng gặp. *Hướng dẫn*: dùng template mục V; mục tiêu phải có con số và thời hạn.

**Bài 9**: Phân tích Case Toyota Jidoka (3.4) và đề xuất cách áp dụng "Andon Cord" cho một quy trình dịch vụ (call center, nhà hàng). *Hướng dẫn*: ví dụ nhà hàng: bất kỳ nhân viên nào cũng được quyền "giữ món" khi thấy món sai/thiếu; quy ước tín hiệu; quản lý đến xử lý ngay; ghi lại để phân tích 5-Why cuối tuần.

**Bài 10**: Xây dựng Pareto Chart từ dữ liệu lỗi giả định.
*Dữ liệu (400 lỗi, 10 loại)*: 120, 85, 60, 40, 30, 25, 15, 10, 8, 7.
*Đáp án*: % tích lũy lần lượt: 30,0% – 51,3% – 66,3% – 76,3% – 83,8% – 90,0% – 93,8% – 96,3% – 98,3% – 100%. 80% đạt ở loại thứ 5 (tức 50% số loại lỗi chiếm ~84% số lỗi) → với dữ liệu này tỷ lệ "80/20" thực tế là "80/50"; hãy ưu tiên 3–4 loại đầu (chiếm 66–76%).

**Bài 11**: Tấm gỗ dày yêu cầu $20{,}0\pm0{,}5$ mm (LSL = 19,5; USL = 20,5). Dữ liệu: $\mu=20{,}1$; $\sigma=0{,}12$. Tính $C_p$, $C_{pk}$ và tỷ lệ ngoài giới hạn.
*Đáp án*: $C_p = \frac{1{,}0}{6\times0{,}12} = 1{,}389$; $\frac{USL-\mu}{3\sigma} = \frac{0{,}4}{0{,}36} = 1{,}111$; $\frac{\mu-LSL}{3\sigma} = \frac{0{,}6}{0{,}36}=1{,}667$ → $C_{pk}=1{,}111$. $z_{USL} = 3{,}33$ → ≈ 429 ppm; $z_{LSL}=5{,}0$ → ≈ 0,3 ppm. Kết luận: tiềm năng tốt nhưng lệch về phía USL; chỉnh máy về 20,0 sẽ đưa $C_{pk}$ lên 1,389.

**Bài 12**: Biểu đồ $\bar X$–R với $n=4$, từ các mẫu ổn định có $\bar{\bar X} = 50{,}2$ và $\bar R=3{,}0$. Tính giới hạn kiểm soát và $\hat\sigma$.
*Đáp án* ($A_2=0{,}729$; $D_4=2{,}282$; $d_2=2{,}059$): $UCL_{\bar X}=50{,}2+0{,}729\times3 = 52{,}39$; $LCL_{\bar X}=50{,}2-2{,}187 = 48{,}01$; $UCL_R = 2{,}282\times3 = 6{,}85$; $LCL_R=0$; $\hat\sigma = 3/2{,}059 = 1{,}46$.

**Bài 13**: Quy trình 4 bước với FPY lần lượt 97%, 95%, 99%, 98%. Tính RTY và nhận xét.
*Đáp án*: $RTY = 0{,}97\times0{,}95\times0{,}99\times0{,}98 = 0{,}894 = 89{,}4\%$; dù không bước nào dưới 95%, hơn 10% sản phẩm phải làm lại ít nhất một lần; ưu tiên cải tiến bước 2 (95%, thấp nhất).

**Bài 14**: Biểu đồ p: mỗi ngày kiểm $n=200$ đơn, $\bar p = 4\%$. Tính UCL/LCL; ngày có 14 đơn lỗi và ngày có 18 đơn lỗi có ngoài kiểm soát không?
*Đáp án*: $\sqrt{\frac{0{,}04\times0{,}96}{200}} = 0{,}01386$; $UCL = 0{,}04+0{,}0416 = 8{,}16\%$; $LCL = \max(0;\,-0{,}16\%) = 0$. Ngày 14 lỗi $=7\%$ < UCL → **trong kiểm soát** (biến động ngẫu nhiên, không nên truy cứu cá nhân); ngày 18 lỗi $=9\%$ > UCL → **ngoài kiểm soát**, cần điều tra nguyên nhân đặc biệt.

**Bài 15**: Quán bán 60 cốc trà đào/giờ, thời gian bổ sung 0,75 giờ, đệm an toàn 25%, mỗi khay đựng 5 cốc. Tính số thẻ Kanban.
*Đáp án*: $k = \frac{60\times0{,}75\times1{,}25}{5} = 11{,}25$ → làm tròn lên **12 thẻ**.

---

## PHỤ LỤC: CHECKLIST QUALITY MANAGEMENT TỔNG HỢP

### A. Bảng thuật ngữ

| Thuật ngữ | Tiếng Việt | Giải thích |
|---|---|---|
| DPMO | Lỗi trên triệu cơ hội | Chỉ số đo mức độ chất lượng theo Six Sigma |
| Cp / Cpk | Chỉ số năng lực quy trình (Cpk có tính lệch tâm) | Đo mức độ quy trình đáp ứng thông số kỹ thuật |
| USL / LSL | Giới hạn kỹ thuật trên/dưới | Do khách hàng/thiết kế quy định |
| UCL / LCL | Giới hạn kiểm soát trên/dưới | Do dữ liệu quy trình tạo ra (±3σ) |
| DMAIC | Define-Measure-Analyze-Improve-Control | Quy trình 5 bước cải tiến của Six Sigma |
| PDCA | Plan-Do-Check-Act | Vòng cải tiến liên tục của Shewhart/Deming |
| Muda | Lãng phí (tiếng Nhật) | Bất kỳ hoạt động nào không tạo giá trị cho khách hàng |
| Kaizen | Cải tiến liên tục | Triết lý cải tiến từng bước nhỏ |
| Jidoka | Tự động hóa thông minh | Máy móc/quy trình tự dừng khi phát hiện bất thường |
| Andon | Hệ thống báo hiệu trực quan | Đèn/dây kéo báo hiệu vấn đề cần xử lý ngay |
| Poka-Yoke | Chống lỗi | Thiết kế để lỗi không thể xảy ra hoặc bị phát hiện ngay |
| RPN | Số ưu tiên rủi ro | Severity × Occurrence × Detection trong FMEA |
| COQ | Chi phí chất lượng | Tổng chi phí phòng ngừa + thẩm định + lỗi nội bộ + lỗi bên ngoài |
| FPY / RTY | Tỷ lệ đạt lần đầu / Tỷ lệ đạt xuyên suốt | RTY = tích các FPY |
| Gemba | Hiện trường | Nơi công việc thực sự diễn ra |

### B. KPI đo lường chất lượng

| Nhóm KPI | Chỉ số | Công thức |
|---|---|---|
| Chất lượng sản phẩm | First Pass Yield (FPY) | Số SP đạt chuẩn ngay lần đầu / Tổng số SP × 100% |
| Chất lượng sản phẩm | Rolled Throughput Yield (RTY) | $FPY_1\times FPY_2\times\dots\times FPY_n$ |
| Chất lượng dịch vụ | Net Promoter Score (NPS) | % Promoters − % Detractors |
| Chi phí | Cost of Quality (COQ) | Tổng 4 nhóm chi phí chất lượng / Doanh thu × 100% |
| Quy trình | Cpk | $\min\bigl(\frac{USL-\mu}{3\sigma},\frac{\mu-LSL}{3\sigma}\bigr)$ |
| Quy trình | DPMO / Sigma Level | Số lỗi / (Số đơn vị × Số cơ hội) × 10⁶; $\Phi^{-1}(1-DPMO/10^6)+1{,}5$ |
| Rủi ro | RPN | Severity × Occurrence × Detection |

### C. Bảng công thức tổng hợp

| Nội dung | Công thức | Ghi chú |
|---|---|---|
| Tổng COQ | $P + A + IF + EF$ | 4 nhóm chi phí chất lượng |
| DPMO | $\frac{\text{Số lỗi}}{\text{Đơn vị}\times\text{Cơ hội}}\times10^6$ | Chuẩn hóa theo số cơ hội lỗi |
| Sigma Level | $\Phi^{-1}(1-DPMO/10^6)+1{,}5$ | Có shift 1,5σ |
| $C_p$ | $\frac{USL-LSL}{6\sigma}$ | Tiềm năng nếu đúng tâm |
| $C_{pk}$ | $\min\bigl(\frac{USL-\mu}{3\sigma},\frac{\mu-LSL}{3\sigma}\bigr)$ | Năng lực thực tế |
| Giới hạn $\bar X$ | $\bar{\bar X}\pm A_2\bar R$ | n=5: $A_2=0{,}577$ |
| Giới hạn R | $UCL=D_4\bar R$; $LCL=D_3\bar R$ | n=5: $D_4=2{,}114$, $D_3=0$ |
| $\hat\sigma$ từ R | $\bar R/d_2$ | n=5: $d_2=2{,}326$ |
| Giới hạn p | $\bar p\pm3\sqrt{\bar p(1-\bar p)/n}$ | LCL không âm |
| RPN | $S\times O\times D$ | Thang 1–1.000 |
| RTY | $\prod FPY_i$ | Nhà máy ẩn |
| Số thẻ Kanban | $\frac{D\times L\times(1+\alpha)}{C}$ | Làm tròn lên |
| Setup SMED | Internal + External | Chuyển internal → external |

### D. Sổ tay rủi ro

| Rủi ro | Biện pháp giảm thiểu |
|---|---|
| Áp dụng công cụ quá phức tạp so với năng lực đội ngũ | Đào tạo từng bước, bắt đầu từ công cụ đơn giản nhất |
| Chỉ tập trung số liệu, bỏ quên yếu tố con người/văn hóa | Kết hợp TQM (văn hóa) với Six Sigma (công cụ) |
| Giảm tồn kho quá mức theo JIT gây rủi ro gián đoạn cung ứng | Đánh giá rủi ro nhà cung cấp trước khi áp dụng JIT triệt để |
| Tính $C_{pk}$ khi quy trình chưa ổn định hoặc dữ liệu không chuẩn | Dùng biểu đồ kiểm soát/histogram kiểm tra trước |
| Số liệu thu thập thiếu tin cậy (dụng cụ đo sai) | Kiểm tra hệ thống đo lường (Measurement) trước khi phân tích |
| Chương trình chất lượng chỉ là khẩu hiệu | Lãnh đạo tham gia Gemba Walk, gắn KPI chất lượng vào đánh giá |

### E. Checklist trước khi áp dụng

**Nền tảng văn hóa & lãnh đạo**
- □ Lãnh đạo cam kết nguồn lực và trực tiếp tham gia (Champion)
- □ Nhân viên được phép báo lỗi mà không bị trừng phạt
- □ Đã chọn dự án đầu tiên bằng ma trận trọng số, ưu tiên quick win

**Đo lường**
- □ Đã tính COQ hiện tại (baseline) cho 4 nhóm chi phí
- □ Có Check Sheet thu thập dữ liệu lỗi tối thiểu 2 tuần
- □ Dụng cụ đo đã được kiểm tra/hiệu chuẩn
- □ Đã xác định USL/LSL từ nhu cầu khách hàng

**Phân tích**
- □ Có Pareto xác định "vital few"
- □ Đã vẽ Fishbone 6M và kiểm chứng nguyên nhân bằng dữ liệu (không chỉ cảm nhận)
- □ Đã chạy 5-Why đến nguyên nhân hệ thống
- □ Đã tính $C_p$, $C_{pk}$ và so sánh trước/sau cải tiến

**Cải tiến & kiểm soát**
- □ Đã thử nghiệm quy mô nhỏ (pilot) trước khi nhân rộng
- □ Đã triển khai 5S và Poka-Yoke ở các điểm lỗi cao
- □ Đã thiết lập biểu đồ kiểm soát (X̄–R hoặc p) và quy tắc phản ứng khi có tín hiệu
- □ Đã chuẩn hóa bằng SOP và đào tạo
- □ Đã tính hiệu quả tài chính và thời gian hoàn vốn
- □ Có lịch rà soát định kỳ (PDCA), mở rộng sang vấn đề tiếp theo

---

## TÀI LIỆU THAM KHẢO

**Sách nền tảng**: Deming, W.E. – *Out of the Crisis*; Juran, J.M. – *Juran's Quality Handbook*; Crosby, P. – *Quality is Free*; George, M. – *Lean Six Sigma*; Liker, J. – *The Toyota Way*; Womack, J., Jones, D., Roos, D. – *The Machine That Changed the World*; Montgomery, D. – *Introduction to Statistical Quality Control* (cho biểu đồ kiểm soát và $C_p/C_{pk}$).

**Liên kết nội bộ**: [`01-process-design-analysis.md`](./01-process-design-analysis.md) (Process Capability, VSM), [`09-theory-of-constraints.md`](./09-theory-of-constraints.md) (bổ sung góc nhìn về bottleneck).

---

*Tài liệu thuộc bộ Knowledge Base MBA – File 2/9 Operations Management.*
