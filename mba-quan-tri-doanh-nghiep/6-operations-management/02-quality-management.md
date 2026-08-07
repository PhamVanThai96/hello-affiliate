# Quality Management (Quản Trị Chất Lượng) – TQM, Six Sigma, Lean Manufacturing

> **Mục tiêu**: Phân tích chuyên sâu ba trụ cột lớn của Quản trị Chất lượng hiện đại – Total Quality Management (TQM), Six Sigma, và Lean Manufacturing – bao gồm lý thuyết nền tảng, công cụ thực hành, ưu-nhược điểm, case study thực tiễn (quốc tế & Việt Nam), và hướng dẫn áp dụng theo quy mô doanh nghiệp.

> **Phạm vi tài liệu**: File 2/9 trong bộ Operations Management. Xây dựng trực tiếp trên nền tảng Process Capability ($C_p$, $C_{pk}$) đã giới thiệu ở file `01-process-design-analysis.md`.

---

## MỤC LỤC

1. Tổng quan & Lý thuyết nền tảng
2. Phân tích chi tiết TQM, Six Sigma, Lean Manufacturing
3. Ưu điểm & Nhược điểm
4. Case study thực tiễn
5. Phương pháp triển khai từng bước
6. Quy mô áp dụng – SME vs Doanh nghiệp lớn
7. Công cụ & Templates hỗ trợ
8. Bài tập thực hành
9. Phụ lục – Thuật ngữ, KPI, sổ tay rủi ro
10. Tài liệu tham khảo

---

## I. TỔNG QUAN & LÝ THUYẾT NỀN TẢNG

### 1.1. Quality Management là gì?

**Quản trị Chất lượng (Quality Management)** là tập hợp các triết lý, công cụ, và phương pháp nhằm đảm bảo sản phẩm/dịch vụ đáp ứng nhất quán yêu cầu của khách hàng, đồng thời giảm thiểu lãng phí và biến động (variability) trong quy trình sản xuất/cung ứng.

Ba định nghĩa chất lượng kinh điển cần phân biệt:

| Định nghĩa | Tác giả | Trọng tâm |
|---|---|---|
| **"Fitness for Use" (Phù hợp với mục đích sử dụng)** | Joseph Juran | Chất lượng được đánh giá theo góc nhìn khách hàng, không phải nhà sản xuất |
| **"Conformance to Requirements" (Tuân thủ yêu cầu)** | Philip Crosby | Chất lượng là làm đúng ngay từ đầu (Zero Defects), đo bằng chi phí không tuân thủ |
| **"Degree of Excellence" (Mức độ hoàn hảo)** | W. Edwards Deming | Chất lượng gắn liền với cải tiến liên tục (Continuous Improvement) và giảm biến động thống kê |

### 1.2. Ba trụ cột của Quality Management hiện đại

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

### 1.3. Chi phí chất lượng (Cost of Quality – COQ)

Một trong những đóng góp quan trọng nhất của Juran là định lượng chi phí chất lượng thành 4 nhóm:

$$\text{Total COQ} = \text{Prevention Cost} + \text{Appraisal Cost} + \text{Internal Failure Cost} + \text{External Failure Cost}$$

| Loại chi phí | Định nghĩa | Ví dụ |
|---|---|---|
| **Prevention Cost (Chi phí phòng ngừa)** | Chi phí để ngăn lỗi xảy ra ngay từ đầu | Đào tạo nhân viên, thiết kế quy trình chuẩn, bảo trì phòng ngừa máy móc |
| **Appraisal Cost (Chi phí thẩm định)** | Chi phí để phát hiện lỗi trước khi đến tay khách hàng | Kiểm tra chất lượng (QC), test sản phẩm, audit |
| **Internal Failure Cost (Chi phí lỗi nội bộ)** | Chi phí xử lý lỗi phát hiện trước khi giao hàng | Hàng lỗi phải làm lại (rework), phế phẩm (scrap) |
| **External Failure Cost (Chi phí lỗi bên ngoài)** | Chi phí xử lý lỗi khách hàng phát hiện sau khi nhận hàng | Bảo hành, đổi trả, mất uy tín thương hiệu, kiện tụng |

**Quy luật 1-10-100 (Rule of Ten)**: Chi phí xử lý một lỗi tăng theo cấp số nhân (khoảng 10 lần) ở mỗi giai đoạn muộn hơn trong chuỗi giá trị – lỗi phát hiện ở khâu thiết kế có chi phí sửa là 1 đơn vị, phát hiện ở khâu sản xuất là ~10 đơn vị, phát hiện sau khi khách hàng đã nhận hàng có thể lên tới ~100 đơn vị (bao gồm chi phí uy tín, mất khách hàng). Đây là lý do các phương pháp hiện đại (Six Sigma, Lean) đều nhấn mạnh "phòng ngừa" hơn "phát hiện".

### 1.4. Biến động (Variability) – Kẻ thù chung của chất lượng

Theo Deming, hầu hết vấn đề chất lượng (94%, theo ước tính của ông) xuất phát từ **nguyên nhân hệ thống (common causes)** – biến động vốn có trong thiết kế quy trình – chứ không phải từ **nguyên nhân đặc biệt (special causes)** – lỗi cá nhân của một công nhân cụ thể. Đây là nền tảng triết lý quan trọng: **đổ lỗi cho nhân viên thường sai hướng**; cần cải tiến hệ thống/quy trình.

$$\sigma^2_{\text{total}} = \sigma^2_{\text{common causes}} + \sigma^2_{\text{special causes}}$$

**Ý nghĩa quản trị**: Nếu một quy trình chỉ có biến động do nguyên nhân hệ thống (statistically stable/in control), việc trừng phạt cá nhân công nhân khi có lỗi là vô ích – cần thay đổi thiết kế quy trình. Chỉ khi có "nguyên nhân đặc biệt" rõ ràng (VD: một máy cụ thể bị hỏng, một công nhân cụ thể chưa được đào tạo) thì can thiệp cá nhân mới có ý nghĩa.

---

## II. PHÂN TÍCH CHI TIẾT TQM, SIX SIGMA, LEAN MANUFACTURING

### 2.1. TOTAL QUALITY MANAGEMENT (TQM)

**Định nghĩa**: TQM là triết lý quản trị toàn diện, coi chất lượng là trách nhiệm của **mọi thành viên trong tổ chức** (không chỉ bộ phận QC), tập trung vào sự hài lòng khách hàng và cải tiến liên tục.

**14 Điểm của Deming (Deming's 14 Points)** – trích lược các điểm quan trọng nhất áp dụng cho doanh nghiệp hiện đại:

| # | Nguyên tắc | Ứng dụng thực tế |
|---|---|---|
| 1 | Tạo sự nhất quán về mục đích cải tiến sản phẩm/dịch vụ | Tầm nhìn dài hạn, không chạy theo lợi nhuận ngắn hạn |
| 3 | Ngừng phụ thuộc vào kiểm tra hàng loạt để đạt chất lượng | Xây dựng chất lượng vào quy trình thay vì kiểm tra ở cuối |
| 5 | Cải tiến liên tục hệ thống sản xuất và dịch vụ | Kaizen – không có "đủ tốt", luôn có thể cải thiện |
| 6 | Đào tạo tại chỗ (on-the-job training) | Đầu tư đào tạo thay vì chỉ tuyển người "sẵn có kỹ năng" |
| 8 | Loại bỏ nỗi sợ hãi (Drive out fear) | Nhân viên dám báo cáo lỗi/vấn đề mà không sợ bị trừng phạt |
| 9 | Phá bỏ rào cản giữa các phòng ban | Cross-functional collaboration, tránh "silo mentality" |
| 12 | Loại bỏ rào cản khiến nhân viên tự hào về công việc | Không đánh giá bằng chỉ tiêu số lượng đơn thuần (quota) gây áp lực làm ẩu |
| 14 | Hành động để đạt được sự chuyển đổi | Cam kết từ lãnh đạo cấp cao (top management commitment) là điều kiện tiên quyết |

**PDCA Cycle (Plan-Do-Check-Act) – Vòng lặp cải tiến liên tục của Deming**:

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

**8 Nguyên tắc quản lý chất lượng theo ISO 9001** (phiên bản hiện đại hóa của TQM, được chuẩn hóa quốc tế):

1. Hướng đến khách hàng (Customer Focus)
2. Vai trò lãnh đạo (Leadership)
3. Sự tham gia của con người (Engagement of People)
4. Tiếp cận theo quy trình (Process Approach)
5. Cải tiến (Improvement)
6. Ra quyết định dựa trên bằng chứng (Evidence-based Decision Making)
7. Quản lý mối quan hệ (Relationship Management)

**Công cụ 7 QC Tools (7 công cụ kiểm soát chất lượng cơ bản)** – nền tảng thực hành TQM:

| Công cụ | Công dụng |
|---|---|
| **Check Sheet (Phiếu kiểm tra)** | Thu thập dữ liệu lỗi có hệ thống |
| **Pareto Chart (Biểu đồ Pareto)** | Xếp hạng nguyên nhân theo tần suất, áp dụng quy tắc 80/20 |
| **Cause-and-Effect Diagram / Fishbone / Ishikawa** | Phân tích nguyên nhân gốc rễ theo 6 nhóm (6M: Man, Machine, Material, Method, Measurement, Mother Nature/Environment) |
| **Histogram** | Trực quan hóa phân phối dữ liệu, phát hiện độ lệch |
| **Control Chart (Biểu đồ kiểm soát)** | Theo dõi biến động quy trình theo thời gian, phát hiện "out of control" |
| **Scatter Diagram (Biểu đồ phân tán)** | Xác định mối tương quan giữa hai biến số |
| **Stratification (Phân tầng)** | Phân nhóm dữ liệu theo các yếu tố khác nhau để tìm pattern ẩn |

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

### 2.2. SIX SIGMA

**Định nghĩa**: Six Sigma là phương pháp cải tiến quy trình dựa trên **thống kê**, nhằm giảm biến động (variability) xuống mức cực thấp, với mục tiêu lý tưởng chỉ 3,4 lỗi trên một triệu cơ hội (DPMO – Defects Per Million Opportunities).

**Nguồn gốc**: Phát triển bởi Motorola (1986, kỹ sư Bill Smith), phổ biến rộng rãi nhờ Jack Welch tại General Electric (GE) thập niên 1990, tiết kiệm cho GE hơn 12 tỷ USD trong 5 năm đầu áp dụng.

**Ý nghĩa con số "Six Sigma"**: $\sigma$ (sigma) là độ lệch chuẩn. "Six Sigma" nghĩa là giới hạn thông số kỹ thuật (specification limits) cách xa trung bình quy trình tới 6 lần độ lệch chuẩn, tạo ra xác suất lỗi cực thấp:

| Cấp độ Sigma | DPMO (lỗi/triệu cơ hội) | Tỷ lệ đạt chuẩn (Yield) |
|---|---|---|
| 2σ | 308.537 | 69,1% |
| 3σ | 66.807 | 93,3% |
| 4σ | 6.210 | 99,38% |
| 5σ | 233 | 99,977% |
| **6σ** | **3,4** | **99,99966%** |

**Công thức tính DPMO**:

$$DPMO = \frac{\text{Số lỗi}}{\text{Số đơn vị} \times \text{Số cơ hội lỗi/đơn vị}} \times 1.000.000$$

**Ví dụ tính toán**: Một xưởng may kiểm tra 5.000 áo sơ mi, mỗi áo có 4 điểm có thể lỗi (đường may cổ, tay, thân, khuy), phát hiện 45 lỗi:

$$DPMO = \frac{45}{5.000 \times 4} \times 1.000.000 = 2.250 \text{ lỗi/triệu cơ hội} \approx \text{4,3σ}$$

**Quy trình DMAIC – Xương sống của Six Sigma**:

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

**Hệ thống Belt (Đai) trong Six Sigma – Phân cấp chuyên môn**:

| Cấp độ | Vai trò | Thời gian đào tạo điển hình |
|---|---|---|
| **White Belt** | Hiểu khái niệm cơ bản, tham gia dự án ở vai trò hỗ trợ | 1 ngày |
| **Yellow Belt** | Tham gia dự án cải tiến trong phạm vi công việc của mình | 2-3 ngày |
| **Green Belt** | Dẫn dắt dự án cải tiến quy mô vừa, làm việc bán thời gian cho dự án | 2 tuần |
| **Black Belt** | Dẫn dắt dự án phức tạp toàn thời gian, đào tạo Green Belt | 4 tuần + dự án thực tế |
| **Master Black Belt** | Cố vấn chiến lược, đào tạo Black Belt, giám sát danh mục dự án toàn công ty | Nhiều năm kinh nghiệm |

**FMEA (Failure Mode and Effects Analysis) – Công cụ phân tích rủi ro trong Analyze phase**:

$$RPN (\text{Risk Priority Number}) = \text{Severity} \times \text{Occurrence} \times \text{Detection}$$

Trong đó mỗi yếu tố được chấm điểm 1-10: Severity (mức độ nghiêm trọng nếu lỗi xảy ra), Occurrence (khả năng xảy ra), Detection (khả năng phát hiện trước khi đến tay khách hàng – điểm cao nghĩa là KHÓ phát hiện). RPN càng cao, mức độ ưu tiên xử lý càng lớn.

**Ví dụ FMEA cho quy trình giao đồ ăn online**:

| Failure Mode | Severity (1-10) | Occurrence (1-10) | Detection (1-10) | RPN |
|---|---|---|---|---|
| Giao sai địa chỉ | 8 | 3 | 2 | 48 |
| Đồ ăn nguội khi đến tay khách | 6 | 6 | 7 | 252 |
| Thiếu món trong đơn hàng | 7 | 4 | 3 | 84 |

→ "Đồ ăn nguội" có RPN cao nhất (252) → cần ưu tiên xử lý trước (VD: đầu tư hộp giữ nhiệt, tối ưu route giao hàng).

### 2.3. LEAN MANUFACTURING

**Định nghĩa**: Lean là triết lý và bộ công cụ nhằm **tối đa hóa giá trị cho khách hàng bằng cách tối thiểu hóa lãng phí (waste/muda)**, có nguồn gốc từ Toyota Production System (đã giới thiệu sơ bộ ở file 01, phần VSM).

**7 Loại Lãng phí kinh điển (7 Wastes – TIMWOOD)** – mở rộng chi tiết hơn so với file 01:

| Loại lãng phí | Tiếng Việt | Ví dụ trong F&B/bán lẻ | Ví dụ trong sản xuất |
|---|---|---|---|
| **T – Transportation** | Vận chuyển thừa | Nguyên liệu di chuyển qua lại nhiều lần giữa kho và bếp | Bán thành phẩm di chuyển xa giữa các trạm |
| **I – Inventory** | Tồn kho dư thừa | Nguyên liệu tươi tồn quá nhiều gây hư hỏng | Nguyên vật liệu/WIP tồn kho quá mức cần thiết |
| **M – Motion** | Thao tác thừa | Nhân viên phải với/cúi người nhiều lần không cần thiết | Công nhân di chuyển xa để lấy dụng cụ |
| **W – Waiting** | Chờ đợi | Khách chờ order, nhân viên chờ nguyên liệu | Máy chờ nguyên liệu, công nhân chờ máy |
| **O – Overproduction** | Sản xuất thừa | Chuẩn bị quá nhiều món ăn dự phòng bị bỏ đi cuối ngày | Sản xuất vượt nhu cầu, tạo tồn kho thành phẩm dư thừa |
| **O – Overprocessing** | Xử lý thừa | Quy trình phê duyệt qua quá nhiều cấp không cần thiết | Gia công/kiểm tra vượt mức yêu cầu khách hàng |
| **D – Defects** | Lỗi/khuyết tật | Món ăn làm sai phải làm lại | Sản phẩm lỗi phải sửa/loại bỏ |

**Lãng phí thứ 8 (bổ sung hiện đại)**: **Skills/Talent Waste** – lãng phí năng lực, ý tưởng, sự sáng tạo của nhân viên khi tổ chức không tạo cơ hội để họ đóng góp cải tiến (VD: nhân viên tuyến đầu biết rõ vấn đề nhưng không có kênh phản hồi).

**5S – Nền tảng của môi trường làm việc Lean**:

| S (tiếng Nhật) | S (tiếng Anh) | Tiếng Việt | Hành động cụ thể |
|---|---|---|---|
| Seiri | Sort | Sàng lọc | Loại bỏ vật dụng không cần thiết khỏi khu vực làm việc |
| Seiton | Set in Order | Sắp xếp | Sắp xếp vật dụng cần thiết ở vị trí cố định, dễ lấy nhất |
| Seiso | Shine | Sạch sẽ | Vệ sinh khu vực làm việc thường xuyên, kết hợp kiểm tra |
| Seiketsu | Standardize | Săn sóc | Chuẩn hóa quy trình 3S trên để duy trì |
| Shitsuke | Sustain | Sẵn sàng/Kỷ luật | Xây dựng thói quen, kỷ luật để duy trì lâu dài |

**Kanban System (Hệ thống thẻ bài)**: Cơ chế trực quan để kiểm soát dòng chảy công việc theo nguyên tắc **Pull** (kéo theo nhu cầu thực tế) thay vì **Push** (đẩy theo kế hoạch dự báo).

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

**Just-in-Time (JIT)**: Triết lý sản xuất/nhập hàng đúng số lượng, đúng thời điểm cần thiết – không sớm hơn, không nhiều hơn. Sẽ được phân tích chi tiết hơn trong file `04-inventory-management.md` (phần so sánh với EOQ và Safety Stock).

**SMED (Single-Minute Exchange of Die) – Giảm thời gian chuyển đổi**:

Kỹ thuật giảm thời gian chuyển đổi giữa các lô sản xuất khác nhau (setup time), giúp doanh nghiệp có thể sản xuất lô nhỏ linh hoạt (small batch) mà không mất hiệu quả kinh tế theo quy mô.

$$\text{Setup Time} = \text{Internal Setup (máy phải dừng)} + \text{External Setup (có thể làm khi máy vẫn chạy)}$$

**Nguyên tắc SMED**: Chuyển tối đa các bước từ Internal Setup sang External Setup (chuẩn bị trước khi dừng máy), giúp giảm thời gian dừng máy thực tế.

**Poka-Yoke (Chống lỗi/Fool-proofing)**: Thiết kế quy trình/công cụ sao cho **không thể xảy ra lỗi về mặt vật lý**, thay vì chỉ dựa vào sự cẩn thận của con người.

| Ví dụ Poka-Yoke | Ngành áp dụng |
|---|---|
| Cổng thẻ USB chỉ cắm được một chiều | Sản xuất điện tử |
| Máy POS bắt buộc nhập đủ thông tin mới cho phép thanh toán | Bán lẻ/F&B |
| Khuôn đóng gói chỉ vừa khít với đúng loại sản phẩm, không thể nhét sai loại | Đóng gói thực phẩm |
| Checklist bắt buộc tick đủ các bước trước khi xuất kho | Logistics |

### 2.4. So sánh tổng hợp TQM vs Six Sigma vs Lean

| Tiêu chí | TQM | Six Sigma | Lean Manufacturing |
|---|---|---|---|
| **Trọng tâm chính** | Văn hóa & triết lý toàn diện | Giảm biến động bằng thống kê | Loại bỏ lãng phí, tăng tốc độ |
| **Công cụ đặc trưng** | PDCA, 7 QC Tools, ISO 9001 | DMAIC, FMEA, Control Chart, Cpk | VSM, Kanban, 5S, SMED, Poka-Yoke |
| **Đo lường thành công** | Sự hài lòng khách hàng, văn hóa cải tiến | DPMO, Sigma Level, RPN | Lead Time, %VA, WIP giảm |
| **Đòi hỏi kỹ năng thống kê** | Thấp | Cao (bắt buộc) | Trung bình |
| **Thời gian thấy kết quả** | Dài hạn (thay đổi văn hóa) | Trung hạn (dự án 3-6 tháng) | Có thể thấy nhanh (vài tuần) |
| **Phù hợp nhất với** | Toàn bộ tổ chức, mọi cấp | Quy trình có dữ liệu định lượng nhiều | Quy trình có nhiều lãng phí rõ ràng |

**Lean Six Sigma** – Sự kết hợp phổ biến hiện nay: Dùng Lean để nhanh chóng loại bỏ lãng phí rõ ràng (quick wins), sau đó dùng Six Sigma DMAIC cho các vấn đề phức tạp cần phân tích thống kê sâu, tất cả đặt trong khung văn hóa TQM (cam kết lãnh đạo, tham gia toàn bộ nhân viên).

---

## III. ƯU ĐIỂM & NHƯỢC ĐIỂM

### 3.1. Bảng ưu điểm chi tiết theo từng phương pháp

| Phương pháp | Ưu điểm | Giải thích |
|---|---|---|
| **TQM** | Tạo văn hóa cải tiến bền vững | Không phụ thuộc vào một vài chuyên gia, mọi nhân viên đều tham gia |
| **TQM** | Chi phí đầu tư ban đầu thấp | Chủ yếu là thay đổi tư duy/quy trình quản lý, không cần công cụ đắt tiền |
| **Six Sigma** | Độ chính xác cao, dựa trên dữ liệu | Loại bỏ tranh cãi chủ quan, quyết định dựa trên bằng chứng thống kê |
| **Six Sigma** | ROI có thể định lượng rõ ràng | Mỗi dự án DMAIC đều có Project Charter với mục tiêu tài chính cụ thể |
| **Lean** | Thấy kết quả nhanh | Nhiều cải tiến (5S, Kanban) có thể triển khai và thấy hiệu quả trong vài tuần |
| **Lean** | Giảm chi phí vận hành trực tiếp | Giảm tồn kho, giảm thời gian chờ trực tiếp giảm chi phí vốn lưu động |

### 3.2. Bảng nhược điểm & rủi ro chi tiết

| Phương pháp | Nhược điểm | Cách giảm thiểu |
|---|---|---|
| **TQM** | Kết quả chậm, khó đo lường ROI ngắn hạn | Kết hợp với KPI cụ thể (VD: NPS, tỷ lệ khiếu nại) để có "bằng chứng sớm" |
| **TQM** | Dễ trở thành khẩu hiệu (slogan) không thực chất nếu lãnh đạo không cam kết thật | Lãnh đạo cấp cao phải trực tiếp tham gia Gemba Walk, không chỉ ký duyệt văn bản |
| **Six Sigma** | Đòi hỏi kỹ năng thống kê, chi phí đào tạo Belt cao | SME có thể thuê tư vấn Green/Black Belt theo dự án thay vì đào tạo nội bộ toàn thời gian |
| **Six Sigma** | Có thể trở nên quan liêu, quá nhiều giấy tờ (paperwork) cho vấn đề đơn giản | Chỉ áp dụng DMAIC đầy đủ cho vấn đề phức tạp; vấn đề đơn giản dùng PDCA nhanh |
| **Lean** | Có thể đẩy áp lực quá mức lên nhân viên nếu chỉ tập trung "cắt giảm" mà không đầu tư con người | Cân bằng giữa loại bỏ lãng phí và đầu tư đào tạo/phúc lợi nhân viên |
| **Lean** | Giảm tồn kho quá mức (JIT) có thể gây rủi ro gián đoạn chuỗi cung ứng | Đánh giá rủi ro chuỗi cung ứng trước khi áp dụng JIT triệt để (bài học từ đứt gãy chuỗi cung ứng COVID-19) |

### 3.3. So sánh mức độ phù hợp theo loại hình vấn đề

| Loại vấn đề | Phương pháp phù hợp nhất | Lý do |
|---|---|---|
| Vấn đề văn hóa, thái độ làm việc | TQM | Cần thay đổi tư duy toàn tổ chức, không phải công cụ kỹ thuật |
| Biến động chất lượng khó xác định nguyên nhân | Six Sigma (DMAIC) | Cần phân tích thống kê sâu để tìm biến số ảnh hưởng thực sự |
| Thời gian chờ/lãng phí rõ ràng, dễ quan sát | Lean | Có thể giải quyết nhanh bằng quan sát trực tiếp, không cần thống kê phức tạp |
| Vấn đề phức tạp, nhiều biến số, cần cả tốc độ lẫn độ chính xác | Lean Six Sigma | Kết hợp tốc độ của Lean với độ chính xác của Six Sigma |

---

## IV. CASE STUDY THỰC TIỄN

### 4.1. Case Study Quốc tế: Motorola & General Electric – Nguồn gốc Six Sigma

**Bối cảnh**: Giữa thập niên 1980, Motorola đối mặt với sự cạnh tranh khốc liệt từ các công ty điện tử Nhật Bản có chất lượng vượt trội. Kỹ sư Bill Smith phát triển phương pháp Six Sigma để giải quyết vấn đề tỷ lệ lỗi cao trong sản xuất.

**Cách thực hiện**: Motorola áp dụng DMAIC nghiêm ngặt cho toàn bộ dây chuyền sản xuất, đào tạo đội ngũ Black Belt chuyên trách, đặt mục tiêu táo bạo "6 Sigma quality" cho mọi quy trình. Jack Welch sau đó đưa Six Sigma vào GE năm 1995, biến nó thành chương trình bắt buộc cho mọi lãnh đạo cấp cao muốn thăng tiến.

**Kết quả định lượng**: Motorola tiết kiệm ước tính 16 tỷ USD trong giai đoạn 1986-2001 nhờ Six Sigma; GE tiết kiệm hơn 12 tỷ USD trong 5 năm đầu (1996-2000), tỷ lệ lỗi giảm đáng kể trên toàn bộ dòng sản phẩm từ máy bay động cơ đến thiết bị y tế.

**Bài học rút ra**: Six Sigma hiệu quả nhất khi có **cam kết từ lãnh đạo cao nhất** (Jack Welch đích thân yêu cầu mọi lãnh đạo phải đạt Green Belt) và được tích hợp vào hệ thống đánh giá hiệu suất/thăng tiến, không chỉ là chương trình đào tạo riêng lẻ.

### 4.2. Case Study Việt Nam (Doanh nghiệp lớn): Vinamilk – Áp dụng ISO 9001 & TQM

**Bối cảnh**: Để cạnh tranh trên thị trường quốc tế và đáp ứng yêu cầu xuất khẩu, Vinamilk cần chứng minh hệ thống quản lý chất lượng đạt chuẩn quốc tế.

**Cách thực hiện**: Vinamilk áp dụng ISO 9001 (hệ thống quản lý chất lượng), ISO 22000/HACCP (an toàn thực phẩm) trên toàn bộ 13 nhà máy, xây dựng văn hóa "chất lượng là trách nhiệm của mọi người" thông qua chương trình đào tạo nội bộ liên tục và hệ thống thưởng/phạt gắn với chỉ số chất lượng.

**Kết quả**: Đạt chứng nhận xuất khẩu sang hơn 50 quốc gia, tỷ lệ sản phẩm lỗi duy trì cực thấp dù sản xuất hàng tỷ sản phẩm/năm, xây dựng được niềm tin thương hiệu bền vững trong hơn 3 thập kỷ.

**Bài học rút ra**: Đối với doanh nghiệp lớn hướng đến thị trường quốc tế, **chứng nhận ISO không phải là đích đến mà là công cụ** để duy trì kỷ luật quản lý chất lượng liên tục – cần tránh tình trạng "làm ISO cho có chứng chỉ" mà không thực sự thay đổi văn hóa vận hành.

### 4.3. Case Study SME Việt Nam: Chuỗi trà sữa nhỏ áp dụng 5S và Poka-Yoke

**Bối cảnh**: Một chuỗi trà sữa 3 cửa hàng tại Hà Nội gặp vấn đề: mỗi cửa hàng pha chế cùng một công thức nhưng vị khác nhau, gây phàn nàn từ khách hàng trung thành.

**Phân tích bằng Fishbone Diagram**: Nhóm quản lý xác định nguyên nhân chính từ nhóm "Method" (không có công thức định lượng chuẩn bằng cân điện tử) và "Man" (nhân viên mới chưa được đào tạo kỹ).

**Giải pháp triển khai**:
1. Áp dụng **5S** tại quầy pha chế: Sàng lọc bớt dụng cụ không dùng đến, sắp xếp nguyên liệu theo thứ tự sử dụng, dán nhãn rõ ràng
2. Áp dụng **Poka-Yoke**: Thay cốc đong bằng cân điện tử có mức cân định sẵn cho từng loại topping/đường, nhân viên không thể "áng chừng" theo cảm tính
3. Xây dựng **Check Sheet** đơn giản để nhân viên tự kiểm tra trước khi giao đồ uống cho khách

**Kết quả sau 6 tuần**: Tỷ lệ phàn nàn về vị không đồng nhất giảm từ 12%/tổng đơn xuống còn 3%; thời gian đào tạo nhân viên mới rút ngắn từ 2 tuần xuống 5 ngày nhờ có quy trình chuẩn rõ ràng bằng cân định lượng thay vì "cảm nhận".

**Bài học rút ra**: SME không cần Six Sigma phức tạp để cải thiện chất lượng đáng kể – **5S + Poka-Yoke đơn giản, chi phí thấp** (mua vài cái cân điện tử ~500.000đ/cái) có thể giải quyết hiệu quả vấn đề biến động chất lượng do thao tác con người.

### 4.4. Case Study Quốc tế (Dịch vụ quy mô lớn): Toyota – Jidoka và văn hóa dừng chuyền

**Bối cảnh**: Ngoài JIT, trụ cột thứ hai của Toyota Production System là **Jidoka** ("tự động hóa có trí tuệ con người") – bất kỳ công nhân nào phát hiện lỗi đều có quyền kéo dây (Andon Cord) để dừng toàn bộ dây chuyền.

**Cách thực hiện**: Toyota trao quyền cho mọi công nhân dừng chuyền khi phát hiện bất thường, thay vì để lỗi trôi qua và tích lũy đến cuối dây chuyền mới phát hiện. Mỗi lần dừng chuyền, đội trưởng và kỹ sư phải đến giải quyết ngay tại chỗ (Genchi Genbutsu), tìm nguyên nhân gốc rễ bằng kỹ thuật **5-Why**.

**Ví dụ kỹ thuật 5-Why**: Máy dừng vì cầu chì cháy → Tại sao cầu chì cháy? Quá tải → Tại sao quá tải? Vòng bi thiếu dầu bôi trơn → Tại sao thiếu dầu? Bơm dầu không hoạt động hiệu quả → Tại sao? Trục bơm bị mòn → Tại sao? Không có bộ lọc nên mạt kim loại lọt vào (nguyên nhân gốc rễ thực sự, không phải "cầu chì cháy").

**Kết quả**: Toyota có tỷ lệ lỗi trên xe thấp nhất ngành ô tô toàn cầu trong nhiều thập kỷ liên tiếp, dù trao quyền dừng chuyền cho hàng nghìn công nhân (một quyết định mà nhiều hãng xe khác coi là "rủi ro" làm giảm năng suất).

**Bài học rút ra**: Trao quyền cho nhân viên tuyến đầu **báo cáo và dừng lại khi phát hiện vấn đề**, kết hợp phân tích nguyên nhân gốc rễ triệt để (5-Why), tạo ra chất lượng bền vững hơn nhiều so với việc chỉ kiểm tra chất lượng ở cuối dây chuyền.

### 4.5. Case Study Việt Nam (Sản xuất SME): Xưởng sản xuất đồ gỗ nội thất áp dụng Six Sigma đơn giản hóa

**Bối cảnh**: Một xưởng sản xuất đồ gỗ nội thất quy mô 25 công nhân tại Đồng Nai gặp tỷ lệ hàng lỗi bề mặt sơn (bong tróc, không đều màu) khoảng 15%, gây thiệt hại lớn về nguyên liệu và thời gian.

**Áp dụng DMAIC đơn giản hóa (không cần Black Belt chuyên nghiệp)**:
- **Define**: Xác định vấn đề "lỗi bề mặt sơn" là vấn đề tài chính lớn nhất (chiếm 60% tổng chi phí lỗi)
- **Measure**: Thu thập dữ liệu 200 sản phẩm trong 2 tuần, ghi nhận loại lỗi, thời điểm, ca làm việc, người thực hiện
- **Analyze**: Dùng Pareto Chart phát hiện 70% lỗi tập trung vào ca chiều (khi độ ẩm không khí trong xưởng cao hơn) và ở một số công nhân cụ thể chưa quen kỹ thuật phun sơn mới
- **Improve**: Lắp máy hút ẩm cho khu vực sơn, đào tạo lại kỹ thuật phun sơn theo góc độ chuẩn, điều chỉnh lịch làm việc để tránh sơn vào giờ ẩm cao nhất trong ngày
- **Control**: Thiết lập Check Sheet hàng ngày ghi nhận độ ẩm và tỷ lệ lỗi để theo dõi xu hướng

**Kết quả**: Tỷ lệ lỗi bề mặt sơn giảm từ 15% xuống còn 4% sau 2 tháng, tiết kiệm ước tính 80 triệu đồng/tháng chi phí nguyên liệu và nhân công làm lại.

**Bài học rút ra**: SME sản xuất hoàn toàn có thể áp dụng **tinh thần DMAIC** (không cần chứng chỉ Six Sigma chính thức) – chỉ cần thu thập dữ liệu có hệ thống và phân tích bằng công cụ đơn giản (Pareto Chart, Check Sheet) đã đủ để tìm ra nguyên nhân gốc rễ và giải quyết hiệu quả.

### 4.6. Bảng tổng hợp bài học từ 5 case study

| Case study | Quy mô | Phương pháp chính | Bài học cốt lõi |
|---|---|---|---|
| Motorola/GE | Tập đoàn đa quốc gia | Six Sigma, DMAIC, Belt system | Cam kết lãnh đạo cao nhất là điều kiện tiên quyết để Six Sigma thành công |
| Vinamilk | Tập đoàn lớn, đa nhà máy | TQM, ISO 9001/22000 | Chứng nhận quốc tế là công cụ duy trì kỷ luật, không phải đích đến cuối cùng |
| Chuỗi trà sữa SME | SME nhỏ (3 cửa hàng) | 5S, Poka-Yoke, Fishbone | Công cụ đơn giản, chi phí thấp vẫn giải quyết hiệu quả vấn đề biến động chất lượng |
| Toyota | Tập đoàn đa quốc gia | Jidoka, Andon, 5-Why | Trao quyền nhân viên tuyến đầu dừng lại khi phát hiện lỗi tạo chất lượng bền vững |
| Xưởng gỗ SME | SME sản xuất (25 công nhân) | DMAIC đơn giản hóa | SME có thể áp dụng tinh thần Six Sigma mà không cần chứng chỉ chính thức |

---

## V. PHƯƠNG PHÁP TRIỂN KHAI TỪNG BƯỚC

### 5.1. Lộ trình triển khai Quality Management cho tổ chức mới bắt đầu

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

### 5.2. Cách chọn dự án cải tiến chất lượng đầu tiên (Project Selection)

| Tiêu chí đánh giá | Câu hỏi cần trả lời | Trọng số khuyến nghị |
|---|---|---|
| Tác động tài chính | Vấn đề này gây thiệt hại bao nhiêu tiền/tháng? | 30% |
| Tác động khách hàng | Vấn đề này ảnh hưởng trực tiếp đến bao nhiêu % khách hàng? | 25% |
| Khả năng thực thi | Có đủ dữ liệu và nguồn lực để giải quyết trong 2-3 tháng không? | 20% |
| Khả năng nhân rộng | Giải pháp có thể áp dụng cho các vấn đề tương tự khác không? | 15% |
| Cam kết của đội ngũ | Đội ngũ liên quan có sẵn sàng tham gia thay đổi không? | 10% |

**Nguyên tắc quan trọng**: Chọn dự án đầu tiên **dễ đạt thành công nhanh (quick win)** để xây dựng niềm tin vào phương pháp, tránh chọn ngay vấn đề quá phức tạp có thể thất bại và làm mất động lực của toàn đội ngũ.

### 5.3. Vai trò của Champion và Quality Circle

- **Quality Champion**: Lãnh đạo cấp cao chịu trách nhiệm bảo trợ (sponsor) cho chương trình chất lượng, phân bổ nguồn lực, tháo gỡ rào cản liên phòng ban
- **Quality Circle (Vòng tròn chất lượng)**: Nhóm nhỏ 5-8 nhân viên tuyến đầu họp định kỳ (VD: 30 phút/tuần) để thảo luận vấn đề chất lượng gặp phải và đề xuất cải tiến – mô hình có nguồn gốc từ Nhật Bản, giúp khai thác kiến thức thực tế của người trực tiếp làm việc

---

## VI. QUY MÔ ÁP DỤNG – SME VS DOANH NGHIỆP LỚN

### 6.1. Bảng so sánh cách tiếp cận theo quy mô

| Khía cạnh | SME nhỏ (1-10 nhân viên) | SME vừa (10-50 nhân viên) | Doanh nghiệp lớn (500+ nhân viên) |
|---|---|---|---|
| **Phương pháp phù hợp** | 5S, Poka-Yoke đơn giản, Check Sheet | PDCA, Fishbone, Pareto Chart | Full DMAIC, Six Sigma Belt system, ISO certification |
| **Người thực hiện** | Chủ doanh nghiệp | Quản lý chất lượng kiêm nhiệm | Đội ngũ Quality/Six Sigma chuyên trách |
| **Chi phí đầu tư ban đầu** | Gần như 0 (thay đổi quy trình, mua công cụ đơn giản) | 5-20 triệu đồng (đào tạo cơ bản, công cụ đo lường) | Hàng trăm triệu-hàng tỷ đồng (ISO certification, phần mềm QMS) |
| **Chứng nhận cần thiết** | Không bắt buộc | VSATTP nếu là F&B | ISO 9001/14001/22000, HACCP, chứng nhận xuất khẩu |
| **Tần suất đo lường** | Khi có vấn đề rõ ràng | Hàng tuần/tháng | Liên tục, real-time dashboard |

### 6.2. Khuyến nghị theo giai đoạn phát triển

**SME mới bắt đầu**: Tập trung vào **TQM tinh thần đơn giản** – xây dựng thói quen "làm đúng ngay từ đầu", dùng Check Sheet giấy để ghi nhận lỗi, áp dụng 5S cho khu vực làm việc. Chưa cần đầu tư Six Sigma hay ISO ở giai đoạn này.

**SME chuẩn bị mở rộng/nhượng quyền**: Đây là giai đoạn cần **chuẩn hóa chất lượng bằng văn bản (SOP)** và có thể cân nhắc chứng nhận VSATTP/ISO cơ bản nếu ngành yêu cầu, để đảm bảo chất lượng đồng nhất khi nhân rộng ra nhiều điểm bán.

**Doanh nghiệp lớn/hướng xuất khẩu**: Bắt buộc đầu tư Six Sigma bài bản với đội ngũ Belt chuyên trách, chứng nhận ISO quốc tế, và hệ thống QMS (Quality Management System) tích hợp với ERP.

### 6.3. Các lỗi phổ biến khi SME áp dụng Quality Management

| Lỗi phổ biến | Hậu quả | Cách khắc phục |
|---|---|---|
| Cố áp dụng Six Sigma đầy đủ ngay từ đầu (quá phức tạp so với quy mô) | Tốn thời gian, nhân viên không hiểu và không áp dụng được | Bắt đầu với PDCA và 7 QC Tools đơn giản trước |
| Chỉ kiểm tra chất lượng ở khâu cuối, không đầu tư phòng ngừa | Chi phí xử lý lỗi cao (theo Rule of Ten), phát hiện quá muộn | Đầu tư vào Poka-Yoke và đào tạo tại các điểm có nguy cơ lỗi cao |
| Đổ lỗi cho nhân viên khi có vấn đề chất lượng thay vì xem xét hệ thống | Nhân viên sợ hãi, che giấu lỗi thay vì báo cáo (theo nguyên tắc Deming) | Xây dựng văn hóa "an toàn tâm lý" khi báo cáo lỗi, tập trung cải tiến hệ thống |
| Không có dữ liệu định lượng, chỉ dựa vào cảm nhận | Không xác định đúng nguyên nhân gốc rễ, giải pháp sai trọng tâm | Luôn thu thập dữ liệu (Check Sheet) tối thiểu 2 tuần trước khi kết luận |

---

## VII. CÔNG CỤ & TEMPLATES HỖ TRỢ

| Công cụ | Loại | Chi phí | Phù hợp |
|---|---|---|---|
| **Google Sheets/Excel** | Check Sheet, Pareto Chart, Control Chart cơ bản | Miễn phí | Mọi quy mô |
| **Minitab** | Phần mềm thống kê chuyên dụng cho Six Sigma | ~1.500 USD/năm (bản quyền) | Doanh nghiệp vừa/lớn có dự án Six Sigma |
| **SigmaXL (Excel Add-in)** | Công cụ Six Sigma tích hợp Excel | ~500 USD/năm | SME vừa muốn bắt đầu Six Sigma nhẹ |
| **Canva/PowerPoint** | Vẽ Fishbone Diagram, trình bày báo cáo | Miễn phí/chi phí thấp | Mọi quy mô |
| **Trello/Asana** | Quản lý dự án cải tiến chất lượng (PDCA/DMAIC tracking) | Miễn phí (bản cơ bản) | SME |
| **Tư vấn ISO 9001 local** | Chứng nhận & tư vấn triển khai | 30-80 triệu đồng (tùy quy mô) | SME chuẩn bị xuất khẩu/đấu thầu |

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

---

## VIII. BÀI TẬP THỰC HÀNH

**Bài 1**: Tính DPMO và Sigma Level cho một quy trình đóng gói kiểm tra 2.000 hộp, mỗi hộp có 3 điểm kiểm tra (nhãn, niêm phong, số lượng), phát hiện 30 lỗi.

**Bài 2**: Vẽ Fishbone Diagram (6M) cho vấn đề "Khách hàng phàn nàn giao hàng trễ" của một shop online.

**Bài 3**: Xây dựng bảng FMEA cho quy trình "Pha chế cà phê" với ít nhất 3 Failure Modes, tính RPN và xác định ưu tiên xử lý.

**Bài 4**: Áp dụng kỹ thuật 5-Why cho vấn đề "Nhân viên thường xuyên đi trễ" – tìm ra nguyên nhân gốc rễ thực sự.

**Bài 5**: Thiết kế một giải pháp Poka-Yoke đơn giản cho một quy trình bạn quan sát thấy thường xuyên xảy ra lỗi do con người.

**Bài 6**: So sánh Cost of Quality (COQ) của phương án "kiểm tra chất lượng 100% ở cuối chuyền" với phương án "đầu tư đào tạo phòng ngừa lỗi từ đầu" cho một xưởng sản xuất giả định.

**Bài 7**: Thực hiện 5S cho một không gian làm việc thực tế của bạn (bàn làm việc, tủ bếp), chụp ảnh trước/sau.

**Bài 8**: Lập Project Charter DMAIC đơn giản cho một vấn đề chất lượng bạn từng gặp trong công việc/cuộc sống.

**Bài 9**: Phân tích case study Toyota Jidoka (Mục 4.4) và đề xuất cách áp dụng nguyên tắc "Andon Cord" (quyền dừng lại khi phát hiện lỗi) cho một quy trình dịch vụ (VD: call center, nhà hàng).

**Bài 10**: Xây dựng Pareto Chart từ dữ liệu lỗi giả định (10 loại lỗi với tần suất khác nhau), xác định 20% nguyên nhân gây ra 80% vấn đề.

---

## IX. PHỤ LỤC – THUẬT NGỮ, KPI, SỔ TAY RỦI RO

### 9.1. Bảng thuật ngữ

| Thuật ngữ | Tiếng Việt | Giải thích |
|---|---|---|
| DPMO | Lỗi trên triệu cơ hội | Chỉ số đo mức độ chất lượng theo Six Sigma |
| Cpk | Chỉ số năng lực quy trình (có tính lệch tâm) | Đo mức độ quy trình đáp ứng thông số kỹ thuật |
| DMAIC | Define-Measure-Analyze-Improve-Control | Quy trình 5 bước cải tiến của Six Sigma |
| Muda | Lãng phí (tiếng Nhật) | Bất kỳ hoạt động nào không tạo giá trị cho khách hàng |
| Kaizen | Cải tiến liên tục | Triết lý cải tiến từng bước nhỏ |
| Jidoka | Tự động hóa thông minh | Máy móc/quy trình tự dừng khi phát hiện bất thường |
| Andon | Hệ thống báo hiệu trực quan | Đèn/dây kéo báo hiệu vấn đề cần xử lý ngay |
| RPN | Số ưu tiên rủi ro | Severity × Occurrence × Detection trong FMEA |
| COQ | Chi phí chất lượng | Tổng chi phí phòng ngừa + thẩm định + lỗi nội bộ + lỗi bên ngoài |

### 9.2. KPI đo lường chất lượng

| Nhóm KPI | Chỉ số | Công thức |
|---|---|---|
| Chất lượng sản phẩm | First Pass Yield (FPY) | Số SP đạt chuẩn ngay lần đầu / Tổng số SP × 100% |
| Chất lượng dịch vụ | Net Promoter Score (NPS) | % Promoters - % Detractors |
| Chi phí | Cost of Quality (COQ) | Tổng 4 nhóm chi phí chất lượng / Doanh thu × 100% |
| Quy trình | Cpk | (USL-Mean)/3σ hoặc (Mean-LSL)/3σ, lấy giá trị nhỏ hơn |

### 9.3. Sổ tay rủi ro

| Rủi ro | Biện pháp giảm thiểu |
|---|---|
| Áp dụng công cụ quá phức tạp so với năng lực đội ngũ | Đào tạo từng bước, bắt đầu từ công cụ đơn giản nhất |
| Chỉ tập trung số liệu, bỏ quên yếu tố con người/văn hóa | Kết hợp TQM (văn hóa) với Six Sigma (công cụ) |
| Giảm tồn kho quá mức theo JIT gây rủi ro gián đoạn cung ứng | Đánh giá rủi ro nhà cung cấp trước khi áp dụng JIT triệt để |

---

## X. TÀI LIỆU THAM KHẢO

**Sách nền tảng**: Deming, W.E. – *Out of the Crisis*; Juran, J.M. – *Juran's Quality Handbook*; Crosby, P. – *Quality is Free*; George, M. – *Lean Six Sigma*; Liker, J. – *The Toyota Way*.

**Liên kết nội bộ**: [`01-process-design-analysis.md`](./01-process-design-analysis.md) (Process Capability, VSM), [`09-theory-of-constraints.md`](./09-theory-of-constraints.md) (bổ sung góc nhìn về bottleneck).

---

*Tài liệu thuộc bộ Knowledge Base MBA – File 2/9 Operations Management.*
