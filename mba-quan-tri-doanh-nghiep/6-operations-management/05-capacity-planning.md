# 05. Hoạch định Năng lực (Capacity Planning)

> File thuộc bộ kiến thức Quản trị Vận hành (Operations Management) - MBA Knowledge Base
> Liên kết: [01-process-design-analysis.md](./01-process-design-analysis.md) | [04-inventory-management.md](./04-inventory-management.md) | [06-project-management.md](./06-project-management.md)

---

## I. Tổng quan & Lý thuyết nền tảng

### 1.1. Định nghĩa Năng lực và Hoạch định Năng lực

**Năng lực (Capacity)** là mức sản lượng tối đa mà một hệ thống (nhà máy, dây chuyền, cửa hàng, đội ngũ nhân viên) có thể tạo ra trong một khoảng thời gian nhất định, với các điều kiện vận hành bình thường.

**Hoạch định năng lực (Capacity Planning)** là quá trình xác định năng lực sản xuất/phục vụ cần thiết để đáp ứng nhu cầu hiện tại và tương lai của doanh nghiệp, đồng thời quyết định thời điểm, quy mô và cách thức đầu tư mở rộng (hoặc thu hẹp) năng lực.

Đây là quyết định chiến lược có tác động dài hạn: đầu tư thừa năng lực gây lãng phí vốn, đầu tư thiếu gây mất doanh số và mất khách hàng vào tay đối thủ.

### 1.2. Ba loại năng lực cần phân biệt

| Loại năng lực | Định nghĩa | Ví dụ |
|---|---|---|
| **Năng lực thiết kế (Design Capacity)** | Sản lượng tối đa lý thuyết trong điều kiện lý tưởng | Dây chuyền thiết kế cho 1,000 sản phẩm/ngày |
| **Năng lực hiệu quả (Effective Capacity)** | Sản lượng tối đa thực tế có thể đạt được, trừ đi các yếu tố như bảo trì, thay đổi sản phẩm, nghỉ lễ | 850 sản phẩm/ngày (85% năng lực thiết kế) |
| **Sản lượng thực tế (Actual Output)** | Sản lượng thực sự đạt được, có thể thấp hơn năng lực hiệu quả do sự cố, chất lượng kém, thiếu nguyên liệu | 750 sản phẩm/ngày |

**Công thức các chỉ số hiệu suất**:

$$\text{Hiệu suất (Efficiency)} = \frac{\text{Sản lượng thực tế}}{\text{Năng lực hiệu quả}} \times 100\%$$

$$\text{Mức sử dụng (Utilization)} = \frac{\text{Sản lượng thực tế}}{\text{Năng lực thiết kế}} \times 100\%$$

**Ví dụ**: Với số liệu trên: Hiệu suất = 750/850 = 88.2%; Mức sử dụng = 750/1,000 = 75%.

### 1.3. Đường cong năng lực và điểm hòa vốn (Break-Even Analysis)

Hoạch định năng lực gắn liền chặt chẽ với phân tích điểm hòa vốn để xác định quy mô đầu tư tối ưu:

$$\text{Điểm hòa vốn (Break-Even Point)} = \frac{\text{Chi phí cố định (FC)}}{\text{Giá bán (P)} - \text{Chi phí biến đổi/đơn vị (VC)}}$$

```
Doanh thu/Chi phí (VNĐ)
        │                                    ╱ Doanh thu (Revenue = P × Q)
        │                                  ╱
        │                    Lợi nhuận   ╱
        │                        ▲     ╱
        │                        │   ╱ ← Điểm hòa vốn (Break-even)
        │            ┌───────────╱─────────  Tổng chi phí (TC = FC + VC×Q)
        │            │         ╱
        │      Lỗ    │       ╱
        │            │     ╱
        │  ──────────┴───╱──────────────────  Chi phí cố định (FC)
        │              ╱
        └────────────────────────────────────▶ Sản lượng (Q)
                    Q(hòa vốn)
```

Khi quyết định đầu tư mở rộng năng lực (mua thêm máy móc, mở thêm chi nhánh), doanh nghiệp cần so sánh điểm hòa vốn mới với dự báo nhu cầu để đánh giá tính khả thi tài chính của quyết định.

### 1.4. Chiến lược thời điểm hoạch định năng lực (Capacity Timing Strategies)

Ba chiến lược cơ bản để quyết định thời điểm bổ sung năng lực so với đường tăng trưởng nhu cầu dự báo:

```
Sản lượng
    │                                    ╱ Nhu cầu dự báo (Demand Forecast)
    │                                  ╱
    │        ┌─────────┐            ╱
    │        │         └──────────╱      ← Chiến lược DẪN DẮT (Lead Strategy)
    │  ┌─────┘                  ╱           Xây trước khi nhu cầu tăng
    │  │                      ╱             (rủi ro dư thừa, nhưng không mất khách)
    │  │        ┌────────────┘
    │  │  ┌─────┘                          ← Chiến lược THEO SAU (Lag Strategy)
    │──┘──┘                                  Xây sau khi nhu cầu đã vượt năng lực
    │                                         (rủi ro mất khách, nhưng an toàn vốn)
    │        - - - - - - - - - - - - -      ← Chiến lược TRUNG BÌNH (Match/Average Strategy)
    │                                         Xây theo mức trung bình dự báo,
    └────────────────────────────────▶ Thời gian    chấp nhận thiếu/thừa xen kẽ
```

| Chiến lược | Ưu điểm | Nhược điểm | Phù hợp |
|---|---|---|---|
| **Dẫn dắt (Lead Strategy)** | Không bao giờ mất khách hàng do thiếu năng lực, chiếm lĩnh thị phần trước | Rủi ro dư thừa công suất nếu dự báo sai, chi phí vốn cao | Ngành tăng trưởng nhanh, cạnh tranh giành thị phần |
| **Theo sau (Lag Strategy)** | An toàn tài chính, tránh đầu tư dư thừa | Có thể mất khách hàng, mất cơ hội thị trường | Ngành ổn định, chi phí đầu tư năng lực rất cao |
| **Trung bình (Match Strategy)** | Cân bằng rủi ro tài chính và rủi ro mất khách hàng | Vẫn có giai đoạn thiếu hụt hoặc dư thừa xen kẽ | Đa số doanh nghiệp SME, thị trường tăng trưởng vừa phải |

### 1.5. Hoạch định năng lực tổng hợp (Aggregate Planning)

Aggregate Planning là quá trình hoạch định mức sản lượng, tồn kho, nhân lực trong trung hạn (3-18 tháng) để đáp ứng nhu cầu dao động theo mùa vụ mà không cần thay đổi năng lực cố định (nhà xưởng, máy móc).

**Ba chiến lược cơ bản trong Aggregate Planning**:

1. **Chiến lược đuổi theo (Chase Strategy)**: điều chỉnh nhân lực/sản lượng theo sát biến động nhu cầu (tuyển thêm/cắt giảm lao động thời vụ, tăng ca/giảm giờ làm).
2. **Chiến lược san bằng (Level Strategy)**: duy trì mức sản xuất/nhân lực ổn định, sử dụng tồn kho để hấp thụ biến động nhu cầu (sản xuất nhiều hơn nhu cầu lúc thấp điểm, dự trữ cho lúc cao điểm).
3. **Chiến lược hỗn hợp (Mixed/Hybrid Strategy)**: kết hợp cả hai, ví dụ duy trì lực lượng lao động cơ bản ổn định + thuê lao động thời vụ khi cao điểm + xây dựng tồn kho đệm vừa phải.

| Chiến lược | Ưu điểm | Nhược điểm |
|---|---|---|
| Chase Strategy | Không tốn chi phí tồn kho, linh hoạt theo nhu cầu | Chi phí tuyển dụng/sa thải cao, ảnh hưởng tinh thần nhân viên |
| Level Strategy | Ổn định lực lượng lao động, dễ quản lý chất lượng | Chi phí lưu kho cao, rủi ro tồn kho lỗi thời |
| Mixed Strategy | Cân bằng chi phí và tính linh hoạt | Phức tạp hơn trong hoạch định và điều phối |

---

## II. Phân tích chi tiết các công cụ/kỹ thuật

### 2.1. Lý thuyết ràng buộc và Nút thắt cổ chai (Theory of Constraints - Bottleneck Analysis)

Trong một chuỗi quy trình sản xuất gồm nhiều công đoạn nối tiếp, năng lực tổng thể của toàn hệ thống luôn bị giới hạn bởi công đoạn có năng lực thấp nhất - gọi là **nút thắt cổ chai (Bottleneck)**.

```
Công đoạn 1      Công đoạn 2      Công đoạn 3      Công đoạn 4
(100 SP/giờ) ──▶ (60 SP/giờ) ──▶ (90 SP/giờ) ──▶ (120 SP/giờ)
                      ▲
                 NÚT THẮT CỔ CHAI (Bottleneck)
                 Năng lực toàn hệ thống = 60 SP/giờ
                 (dù các công đoạn khác có năng lực cao hơn)
```

**Nguyên lý quản trị nút thắt cổ chai (theo Eliyahu Goldratt, "The Goal")**:
1. Xác định nút thắt cổ chai của hệ thống.
2. Khai thác tối đa nút thắt cổ chai (không để nó ngừng hoạt động, kể cả giờ nghỉ).
3. Điều chỉnh mọi công đoạn khác phục vụ cho nút thắt cổ chai (không sản xuất vượt quá khả năng xử lý của nút thắt).
4. Nâng cấp năng lực của nút thắt cổ chai (đầu tư máy móc, nhân lực).
5. Lặp lại quy trình - vì khi nút thắt cũ được giải quyết, một nút thắt mới sẽ xuất hiện ở công đoạn khác.

(Chủ đề này được phân tích chuyên sâu hơn trong file [09-theory-of-constraints.md](./09-theory-of-constraints.md).)

### 2.2. Phân tích công suất theo hàng đợi (Queuing Theory / Waiting Line Analysis)

Đối với ngành dịch vụ (nơi năng lực gắn liền với thời gian phục vụ khách hàng), lý thuyết hàng đợi giúp xác định số lượng nhân viên/quầy phục vụ tối ưu để cân bằng giữa chi phí nhân sự và thời gian chờ đợi của khách hàng.

**Công thức cơ bản mô hình M/M/1 (một quầy phục vụ)**:

$$\rho = \frac{\lambda}{\mu}$$

Trong đó:
- $\lambda$ = Tỷ lệ khách đến trung bình (customers/giờ)
- $\mu$ = Tỷ lệ phục vụ trung bình của 1 quầy (customers/giờ)
- $\rho$ = Hệ số sử dụng (Utilization Factor), phải nhỏ hơn 1 để hệ thống ổn định

**Thời gian chờ trung bình trong hàng đợi**:

$$W_q = \frac{\rho}{\mu(1-\rho)} = \frac{\lambda}{\mu(\mu-\lambda)}$$

**Ví dụ**: Một quầy thu ngân siêu thị có tỷ lệ khách đến $\lambda = 30$ khách/giờ, tỷ lệ phục vụ $\mu = 40$ khách/giờ.

$$\rho = 30/40 = 0.75 \quad \Rightarrow \quad W_q = \frac{30}{40(40-30)} = \frac{30}{400} = 0.075 \text{ giờ} \approx 4.5 \text{ phút}$$

Nếu lượng khách tăng lên $\lambda = 38$ khách/giờ (gần bằng năng lực phục vụ), thời gian chờ sẽ tăng vọt phi tuyến tính:

$$W_q = \frac{38}{40(40-38)} = \frac{38}{80} = 0.475 \text{ giờ} \approx 28.5 \text{ phút}$$

Đây là bài học quan trọng: khi mức sử dụng năng lực (utilization) tiến gần 100%, thời gian chờ đợi tăng theo cấp số nhân chứ không tuyến tính - đây là lý do các hệ thống dịch vụ hiệu quả thường không vận hành ở mức 100% công suất mà giữ một khoảng đệm (buffer capacity).

### 2.3. Đường cong học tập (Learning Curve)

Khi một tổ chức/công nhân thực hiện lặp lại một công việc, thời gian hoàn thành giảm dần theo một tỷ lệ có thể dự đoán được - gọi là hiệu ứng đường cong học tập, ảnh hưởng trực tiếp đến năng lực thực tế theo thời gian.

$$T_n = T_1 \times n^{\log_2(r)}$$

Trong đó:
- $T_n$ = Thời gian sản xuất đơn vị thứ $n$
- $T_1$ = Thời gian sản xuất đơn vị đầu tiên
- $r$ = Tỷ lệ học tập (Learning Rate, ví dụ 90% nghĩa là mỗi khi sản lượng tích luỹ tăng gấp đôi, thời gian trung bình giảm còn 90%)

**Ứng dụng**: Khi hoạch định năng lực cho dây chuyền sản xuất mới hoặc nhân viên mới, cần tính đến giai đoạn "làm quen" (ramp-up period) trong 3-6 tháng đầu, năng lực thực tế sẽ thấp hơn năng lực thiết kế đáng kể.

### 2.4. Cân bằng chuyền sản xuất (Line Balancing)

Đối với dây chuyền sản xuất có nhiều trạm làm việc (workstation) nối tiếp, cân bằng chuyền là kỹ thuật phân bổ công việc đồng đều giữa các trạm để tối thiểu hoá thời gian nhàn rỗi (idle time) và tối đa hoá năng lực chuyền.

**Công thức Cycle Time (Nhịp sản xuất) tối thiểu**:

$$C = \frac{\text{Thời gian sản xuất có sẵn mỗi ngày}}{\text{Sản lượng yêu cầu mỗi ngày}}$$

**Số trạm làm việc tối thiểu về lý thuyết**:

$$N_{min} = \frac{\sum t_i}{C}$$

Trong đó $\sum t_i$ là tổng thời gian tất cả các công đoạn.

**Hiệu suất cân bằng chuyền (Balance Efficiency)**:

$$\text{Efficiency} = \frac{\sum t_i}{N_{actual} \times C} \times 100\%$$

### 2.5. Hoạch định yêu cầu năng lực (Capacity Requirements Planning - CRP)

CRP là quá trình xác định chi tiết năng lực cần thiết (theo từng trung tâm làm việc/máy móc) để thực hiện kế hoạch sản xuất chính (Master Production Schedule - MPS), thường được tính toán tự động trong hệ thống ERP/MRP dựa trên định mức thời gian sản xuất (routing) của từng sản phẩm.

---

## III. Ưu điểm & Nhược điểm

### 3.1. Bảng so sánh các chiến lược hoạch định năng lực

| Chiến lược | Ưu điểm | Nhược điểm |
|---|---|---|
| Lead Strategy | Không mất doanh số, chiếm lĩnh thị trường sớm | Rủi ro tài chính cao nếu dự báo sai |
| Lag Strategy | An toàn tài chính, ROI cao hơn khi đầu tư | Mất cơ hội thị trường, khách hàng chuyển sang đối thủ |
| Match Strategy | Cân bằng rủi ro | Đòi hỏi dự báo chính xác và linh hoạt điều chỉnh liên tục |
| Chase (Aggregate) | Chi phí tồn kho thấp | Chi phí biến động nhân sự cao |
| Level (Aggregate) | Ổn định nhân sự, chất lượng | Chi phí tồn kho cao |

### 3.3. So sánh chiến lược năng lực theo góc độ tài chính

| Tiêu chí tài chính | Lead Strategy | Lag Strategy | Match Strategy |
|---|---|---|---|
| Dòng tiền đầu tư ban đầu (CAPEX) | Lớn, trả trước | Nhỏ, trả dần theo nhu cầu | Trung bình, theo giai đoạn |
| Rủi ro tài sản không sử dụng hết (Idle Asset Risk) | Cao | Thấp | Trung bình |
| Chi phí cơ hội (Opportunity Cost) nếu thiếu năng lực | Thấp (hiếm khi thiếu) | Cao (thường xuyên thiếu giai đoạn đầu) | Trung bình |
| Độ nhạy với sai số dự báo | Cao (thiệt hại lớn nếu dự báo sai) | Thấp (ít đầu tư trước) | Trung bình |
| Phù hợp với cấu trúc vốn | Doanh nghiệp có vốn dồi dào, khả năng chịu rủi ro cao | Doanh nghiệp hạn chế vốn, ưu tiên an toàn | Đa số doanh nghiệp có quy mô vừa và tăng trưởng ổn định |

### 3.2. So sánh theo ngành: Sản xuất vs Dịch vụ

| Khía cạnh | Ngành Sản xuất (Manufacturing) | Ngành Dịch vụ (Service) |
|---|---|---|
| Khả năng lưu trữ năng lực dư | Có (qua tồn kho thành phẩm) | Không (dịch vụ không lưu trữ được) |
| Công cụ chính | Line Balancing, Aggregate Planning | Queuing Theory, lịch làm việc linh hoạt |
| Rủi ro chính | Tồn kho dư thừa nếu dự báo sai | Thời gian chờ đợi khách hàng tăng vọt |
| Ví dụ điều chỉnh năng lực | Tăng ca, thuê thêm máy móc | Thuê nhân viên bán thời gian giờ cao điểm |

---

## IV. Case study thực tiễn

### 4.1. Case study quốc tế lớn: Amazon - Hoạch định năng lực kho vận mùa cao điểm

**Bối cảnh**: Amazon phải đối mặt với nhu cầu tăng đột biến gấp 5-10 lần vào mùa mua sắm cuối năm (Black Friday, Cyber Monday, Giáng sinh) so với các tháng bình thường.

**Chiến lược áp dụng**: Amazon sử dụng chiến lược Lead Strategy kết hợp Chase Strategy cho lao động thời vụ - xây dựng trước các trung tâm fulfillment mới nhiều tháng trước mùa cao điểm (Lead), đồng thời tuyển hàng trăm nghìn lao động thời vụ ngắn hạn chỉ trong 2-3 tháng cao điểm (Chase). Amazon cũng đầu tư mạnh vào tự động hoá robot (Kiva robots) để tăng năng lực xử lý mà không phụ thuộc hoàn toàn vào lao động.

**Kết quả**: Khả năng đáp ứng đơn hàng tăng vọt trong mùa cao điểm mà không sụp đổ hệ thống, dù chi phí vận hành mùa cao điểm tăng đáng kể so với các tháng thường.

### 4.2. Case study Việt Nam lớn: Highlands Coffee - Cân bằng năng lực chuỗi cửa hàng

**Bối cảnh**: Highlands Coffee vận hành hàng trăm cửa hàng với nhu cầu khách hàng biến động mạnh theo giờ trong ngày (cao điểm sáng 7-9h, trưa 11-13h, chiều tối 17-19h).

**Giải pháp**: Áp dụng lý thuyết hàng đợi để tính toán số lượng nhân viên pha chế và thu ngân cần thiết theo từng khung giờ, tránh tình trạng khách phải chờ quá lâu vào giờ cao điểm nhưng cũng không dư thừa nhân sự giờ thấp điểm. Xây dựng lịch làm việc ca linh hoạt (shift scheduling) theo dữ liệu lịch sử lượng khách từng khung giờ, từng cửa hàng cụ thể.

**Kết quả**: Cải thiện đáng kể thời gian chờ đợi trung bình của khách trong giờ cao điểm, đồng thời tối ưu chi phí nhân sự tại giờ thấp điểm.

### 4.3. Case study SME Việt Nam: Xưởng may gia công tại Bình Dương mở rộng năng lực

**Bối cảnh**: Xưởng may 150 công nhân nhận được đơn hàng xuất khẩu lớn gấp 3 lần năng lực hiện tại, thời hạn giao hàng chỉ trong 4 tháng.

**Vấn đề**: Chủ xưởng phân vân giữa việc đầu tư mua thêm máy móc và tuyển thêm công nhân (đầu tư dài hạn) hay chỉ tăng ca và thuê gia công lại một phần cho xưởng khác (giải pháp ngắn hạn).

**Phân tích & Giải pháp**: Sử dụng phân tích điểm hòa vốn để đánh giá: nếu đơn hàng lớn này là xu hướng dài hạn (khách hàng cam kết đơn hàng định kỳ), đầu tư máy móc mới có điểm hòa vốn hợp lý trong vòng 18 tháng. Xưởng quyết định đầu tư 40% năng lực mới (mua máy, tuyển thêm công nhân cơ bản) kết hợp thuê gia công ngoài 60% phần vượt trội để đáp ứng đơn hàng gấp mà không rủi ro đầu tư dư thừa nếu đơn hàng không lặp lại.

**Kết quả**: Đáp ứng đúng hạn đơn hàng lớn, đồng thời xây dựng được năng lực nội tại tăng trưởng bền vững cho các đơn hàng tương lai mà không đầu tư quá mức.

### 4.4. Case study quốc tế - thất bại: Ngành hàng không mở rộng năng lực trước khủng hoảng COVID-19

**Bối cảnh**: Nhiều hãng hàng không quốc tế đầu tư mở rộng đội bay và năng lực vận chuyển mạnh mẽ trong giai đoạn 2015-2019 dựa trên dự báo tăng trưởng ngành du lịch liên tục.

**Vấn đề**: Đại dịch COVID-19 năm 2020 khiến nhu cầu di chuyển hàng không sụt giảm đột ngột hơn 90%, trong khi các hãng đã cam kết hợp đồng thuê/mua máy bay dài hạn theo chiến lược Lead Strategy, dẫn đến dư thừa năng lực khổng lồ và thua lỗ nặng nề, nhiều hãng phải tuyên bố phá sản hoặc nhận cứu trợ chính phủ.

**Bài học**: Chiến lược Lead Strategy đầu tư dựa trên dự báo dài hạn có rủi ro rất lớn với các sự kiện gián đoạn không lường trước (black swan events). Đây là lý do các mô hình hoạch định năng lực hiện đại khuyến nghị xây dựng kịch bản dự phòng (scenario planning) và duy trì tính linh hoạt trong hợp đồng đầu tư dài hạn (ví dụ: điều khoản huỷ/hoãn hợp đồng thuê máy bay).

### 4.5. Case study Việt Nam SME - dịch vụ: Phòng khám tư nhân mở rộng năng lực khám bệnh

**Bối cảnh**: Một phòng khám đa khoa tư nhân tại TP.HCM có lượng bệnh nhân tăng trưởng ổn định 20%/năm, hiện tại thường xuyên quá tải vào cuối tuần, bệnh nhân phải chờ 2-3 giờ.

**Giải pháp**: Áp dụng phân tích hàng đợi để tính số lượng bác sĩ cần thiết cho từng khung giờ dựa trên dữ liệu lịch sử lượng bệnh nhân. Thay vì đầu tư mở rộng cơ sở vật chất ngay (chiến lược Lead tốn kém), phòng khám áp dụng chiến lược Match: thuê thêm bác sĩ part-time vào cuối tuần (giờ cao điểm), đồng thời triển khai hệ thống đặt lịch hẹn trước qua ứng dụng để san đều lượng bệnh nhân trong ngày thay vì dồn vào một khung giờ.

**Kết quả**: Thời gian chờ trung bình giảm từ 2-3 giờ xuống dưới 45 phút mà không cần đầu tư mở rộng cơ sở vật chất ngay lập tức, tiết kiệm đáng kể chi phí đầu tư ban đầu.

### 4.6. Bảng tổng hợp bài học từ các case study

| Case study | Chiến lược áp dụng | Bài học chính |
|---|---|---|
| Amazon | Lead + Chase kết hợp | Kết hợp đầu tư dài hạn với lao động linh hoạt cho nhu cầu thời vụ cực đoan |
| Highlands Coffee | Queuing Theory + Shift Scheduling | Lịch làm việc linh hoạt theo dữ liệu giờ cao điểm tối ưu hiệu quả nhân sự |
| Xưởng may Bình Dương | Match Strategy (đầu tư + thuê ngoài) | Đánh giá tính bền vững của đơn hàng trước khi quyết định đầu tư dài hạn |
| Ngành hàng không (thất bại) | Lead Strategy quá mức | Rủi ro của cam kết dài hạn khi không có kế hoạch dự phòng cho sự kiện bất ngờ |
| Phòng khám TP.HCM | Match + công nghệ đặt lịch | Công nghệ (đặt lịch hẹn) có thể thay thế một phần nhu cầu đầu tư năng lực vật lý |
| FPT Software | Bench + đào tạo nội bộ + gig | Năng lực nhân sự tri thức cần vùng đệm và đào tạo liên tục thay vì chỉ tuyển dụng |

---

## V. Phương pháp triển khai từng bước

### 5.1. Quy trình 7 bước hoạch định năng lực

```
Bước 1: Dự báo nhu cầu (Demand Forecasting)
   │  Ngắn hạn, trung hạn, dài hạn - xem file 07-forecasting.md
   ▼
Bước 2: Đánh giá năng lực hiện tại (Current Capacity Assessment)
   │  Đo lường năng lực thiết kế, hiệu quả, sản lượng thực tế
   ▼
Bước 3: Xác định khoảng cách năng lực (Capacity Gap Analysis)
   │  So sánh nhu cầu dự báo với năng lực hiện có theo từng giai đoạn
   ▼
Bước 4: Xác định nút thắt cổ chai (Bottleneck Identification)
   │  Phân tích công đoạn giới hạn năng lực toàn hệ thống
   ▼
Bước 5: Đánh giá các phương án mở rộng (Alternative Evaluation)
   │  So sánh Lead/Lag/Match, phân tích điểm hòa vốn từng phương án
   ▼
Bước 6: Triển khai quyết định đầu tư (Implementation)
   │  Mua máy móc, tuyển dụng, xây dựng cơ sở mới, thuê ngoài
   ▼
Bước 7: Giám sát & Điều chỉnh (Monitoring & Adjustment)
      Theo dõi hiệu suất thực tế, điều chỉnh kế hoạch theo biến động thị trường
```

### 5.2. Bảng các sai lầm thường gặp

| Sai lầm | Hậu quả | Cách phòng tránh |
|---|---|---|
| Chỉ dựa vào dự báo lạc quan để đầu tư | Dư thừa năng lực khi thị trường không như kỳ vọng | Xây dựng kịch bản dự báo (best/base/worst case) |
| Không xác định đúng nút thắt cổ chai | Đầu tư sai chỗ, không cải thiện năng lực tổng thể | Phân tích luồng quy trình kỹ trước khi đầu tư |
| Vận hành ở mức 100% công suất liên tục | Thời gian chờ tăng vọt, không có buffer cho sự cố | Duy trì tỷ lệ sử dụng công suất hợp lý (80-90%) |
| Bỏ qua giai đoạn ramp-up khi mở rộng | Kỳ vọng năng lực đầy đủ ngay lập tức, thất vọng khi thực tế thấp hơn | Tính đến đường cong học tập trong kế hoạch |
| Không có kế hoạch dự phòng khi cam kết dài hạn | Thiệt hại nặng khi có sự kiện bất ngờ (như COVID-19) | Đàm phán điều khoản linh hoạt, kịch bản ứng phó rủi ro |

---

## VI. Quy mô áp dụng – SME vs Doanh nghiệp lớn

### 6.1. Bảng so sánh mức độ áp dụng

| Thành phần | SME | Doanh nghiệp lớn |
|---|---|---|
| Dự báo nhu cầu | Kinh nghiệm, dữ liệu lịch sử đơn giản | Mô hình thống kê/AI phức tạp, đa kịch bản |
| Chiến lược năng lực | Chủ yếu Match/Lag do hạn chế vốn | Có thể áp dụng Lead Strategy nhờ tiềm lực tài chính |
| Công cụ phân tích | Excel, ước lượng thủ công | Phần mềm mô phỏng (simulation), APS (Advanced Planning System) |
| Linh hoạt điều chỉnh | Nhanh, ít ràng buộc hợp đồng dài hạn | Chậm hơn do cam kết đầu tư/hợp đồng lớn |
| Rủi ro chính | Thiếu vốn đầu tư khi cơ hội đến | Rủi ro dư thừa năng lực khi dự báo sai |

### 6.2. Chi phí đầu tư theo giai đoạn phát triển

| Giai đoạn | Hoạt động hoạch định năng lực | Chi phí ước tính (VNĐ) |
|---|---|---|
| Khởi nghiệp | Ước lượng thủ công, thuê ngoài linh hoạt | 0 - 50 triệu |
| Tăng trưởng | Đầu tư máy móc/nhân sự cơ bản theo Match Strategy | 200 triệu - 2 tỷ |
| Mở rộng | Xây dựng cơ sở mới, đầu tư tự động hoá một phần | 5 - 30 tỷ |
| Doanh nghiệp lớn | Đầu tư nhà máy/trung tâm phân phối quy mô lớn, tự động hoá cao | 50 - hàng nghìn tỷ |

### 6.3. Lộ trình khuyến nghị cho SME

1. Bắt đầu với việc đo lường chính xác năng lực hiện tại (thiết kế, hiệu quả, thực tế).
2. Áp dụng phân tích điểm hòa vốn đơn giản trước khi quyết định đầu tư mở rộng.
3. Ưu tiên chiến lược Match/Lag để giảm rủi ro tài chính, chỉ áp dụng Lead khi có cam kết đơn hàng dài hạn rõ ràng.
4. Tận dụng thuê ngoài (outsourcing) một phần năng lực trong giai đoạn nhu cầu tăng đột biến chưa rõ tính bền vững.
5. Khi quy mô đủ lớn, đầu tư công cụ mô phỏng/dự báo nâng cao để tối ưu hoá quyết định đầu tư năng lực.

### 6.4. Bảng kiểm tự đánh giá năng lực doanh nghiệp (Capacity Self-Assessment Checklist)

Trước khi tiến hành hoạch định năng lực bài bản, doanh nghiệp (đặc biệt SME) nên tự đánh giá theo bảng kiểm nhanh dưới đây:

- [ ] Đã đo lường được năng lực thiết kế và năng lực hiệu quả hiện tại của quy trình cốt lõi?
- [ ] Đã xác định rõ nút thắt cổ chai (bottleneck) trong hệ thống hiện tại?
- [ ] Có dữ liệu lịch sử về nhu cầu để dự báo tương đối tin cậy?
- [ ] Đã tính toán điểm hòa vốn cho các phương án đầu tư mở rộng đang cân nhắc?
- [ ] Có phương án dự phòng (thuê ngoài, lao động linh hoạt) cho trường hợp nhu cầu tăng đột biến ngắn hạn?
- [ ] Đã đánh giá rủi ro của các cam kết đầu tư/hợp đồng dài hạn trước các sự kiện bất ngờ?
- [ ] Đã xác định tỷ lệ dự phòng năng lực (capacity cushion) phù hợp với đặc thù ngành?
- [ ] Đã cân nhắc đầy đủ giữa sở hữu tài sản và thuê ngoài linh hoạt cho từng loại năng lực?
- [ ] Đội ngũ quản lý đã hiểu rõ khái niệm nút thắt cổ chai và cách quản trị nó theo Lý thuyết ràng buộc?
- [ ] Có kế hoạch giám sát và điều chỉnh định kỳ (ít nhất hàng quý) cho kế hoạch năng lực đã thiết lập?
- [ ] Đã trao đổi với bộ phận tài chính về tác động dòng tiền của các phương án đầu tư năng lực?
- [ ] Đã xây dựng ít nhất một kịch bản dự phòng cho trường hợp nhu cầu sụt giảm bất ngờ?

---

## VII. Công cụ & Templates hỗ trợ

### 7.1. Bảng công cụ phần mềm hỗ trợ hoạch định năng lực

| Công cụ | Chức năng | Chi phí ước tính | Phù hợp |
|---|---|---|---|
| Excel với công thức Break-even/Queuing | Phân tích cơ bản | Miễn phí | SME nhỏ |
| Arena, Simul8 (Simulation Software) | Mô phỏng dòng chảy quy trình phức tạp | 50-200 triệu/license | SME vừa, tư vấn |
| SAP APO/IBP, Oracle Demantra | Hoạch định năng lực tích hợp ERP | Hàng tỷ/năm | Doanh nghiệp lớn |
| Google Sheets + Power BI | Theo dõi KPI năng lực trực quan | Miễn phí - vài triệu/tháng | Mọi quy mô |

### 7.2. Template: Bảng tính điểm hòa vốn cho quyết định đầu tư năng lực

```
Phương án đầu tư: _______________
Chi phí cố định tăng thêm (FC): _______________ VNĐ/năm
Giá bán trung bình (P): _______________ VNĐ/đơn vị
Chi phí biến đổi/đơn vị (VC): _______________ VNĐ/đơn vị

Điểm hòa vốn (Q hòa vốn) = FC / (P - VC) = _______________ đơn vị/năm

Dự báo nhu cầu năm 1: _______  Năm 2: _______  Năm 3: _______
So sánh với điểm hòa vốn → Quyết định: [ ] Đầu tư  [ ] Không đầu tư  [ ] Đầu tư từng phần
```

### 7.3. Sơ đồ quyết định chiến lược thời điểm đầu tư năng lực

```
                    Bắt đầu
                       │
        Nhu cầu thị trường có tăng trưởng ổn định, dự báo tin cậy cao?
                /                          \
              Có                          Không/Biến động cao
               │                              │
   Đối thủ đang mở rộng nhanh?         CHIẾN LƯỢC LAG/MATCH
      /            \                   (Chờ tín hiệu rõ ràng,
    Có             Không                 thuê ngoài linh hoạt)
     │                │
CHIẾN LƯỢC LEAD    CHIẾN LƯỢC MATCH
(Đầu tư trước để    (Đầu tư theo dự báo
 giữ thị phần)       trung bình, điều
                     chỉnh dần)
```

---

## VIII. Bài tập thực hành

1. Tính năng lực thiết kế, năng lực hiệu quả và hiệu suất/mức sử dụng cho một quy trình sản xuất/dịch vụ thực tế bạn quen thuộc.
2. Xây dựng phân tích điểm hòa vốn cho một quyết định đầu tư mở rộng năng lực giả định (mua máy mới, mở chi nhánh).
3. Áp dụng mô hình hàng đợi M/M/1 để tính thời gian chờ đợi trung bình cho một quầy dịch vụ (ngân hàng, siêu thị, phòng khám) với dữ liệu tự thu thập hoặc giả định hợp lý.
4. So sánh 3 chiến lược Lead/Lag/Match cho một tình huống kinh doanh cụ thể, đề xuất chiến lược phù hợp nhất kèm lý do.
5. Xác định nút thắt cổ chai (bottleneck) trong một quy trình sản xuất/dịch vụ gồm ít nhất 4 công đoạn, đề xuất giải pháp nâng cao năng lực nút thắt.
6. Xây dựng kế hoạch Aggregate Planning theo Chase, Level, và Mixed Strategy cho một doanh nghiệp có nhu cầu theo mùa (may mặc, thực phẩm, du lịch), so sánh chi phí giữa 3 chiến lược.
7. Tính đường cong học tập cho một công việc lặp lại, dự đoán thời gian hoàn thành đơn vị thứ 50 và thứ 100 dựa trên thời gian đơn vị đầu tiên và tỷ lệ học tập giả định.
8. Nghiên cứu case ngành hàng không thời COVID-19, phân tích bài học về rủi ro của chiến lược Lead Strategy quá mức.
9. Thiết kế lịch làm việc ca linh hoạt (shift scheduling) cho một cửa hàng/quán ăn dựa trên dữ liệu lượng khách theo giờ giả định.
10. Đề xuất lộ trình hoạch định năng lực cho một SME giả định đang tăng trưởng 30%/năm trong 3 năm tới, bao gồm chi phí đầu tư ước tính theo từng giai đoạn.
11. So sánh chi phí và rủi ro giữa phương án sở hữu tài sản (own capacity) và thuê ngoài linh hoạt (outsource/flexible capacity) cho một quyết định mở rộng cụ thể.
12. Tính tỷ lệ dự phòng năng lực (capacity cushion) hiện tại của một tổ chức bạn quen thuộc, so sánh với mức khuyến nghị theo ngành và đề xuất điều chỉnh nếu cần.
13. Thiết kế mô hình mô phỏng Monte Carlo đơn giản (bằng Excel) để đánh giá xác suất thành công của một quyết định đầu tư năng lực dưới điều kiện nhu cầu bất định.

---

## IX. Phụ lục

### 9.1. Bảng thuật ngữ (Glossary)

| Thuật ngữ | Giải thích |
|---|---|
| Design Capacity | Năng lực thiết kế - sản lượng tối đa lý thuyết |
| Effective Capacity | Năng lực hiệu quả - sản lượng tối đa thực tế khả thi |
| Utilization | Mức sử dụng năng lực so với năng lực thiết kế |
| Bottleneck | Nút thắt cổ chai - công đoạn giới hạn năng lực toàn hệ thống |
| Lead/Lag/Match Strategy | Ba chiến lược thời điểm đầu tư năng lực |
| Aggregate Planning | Hoạch định tổng hợp sản lượng/nhân lực trung hạn |
| Queuing Theory | Lý thuyết hàng đợi - phân tích thời gian chờ đợi dịch vụ |
| Learning Curve | Đường cong học tập - giảm thời gian sản xuất theo kinh nghiệm tích luỹ |
| Line Balancing | Cân bằng chuyền sản xuất |
| CRP | Capacity Requirements Planning - hoạch định yêu cầu năng lực chi tiết |
| Capacity Cushion | Tỷ lệ năng lực dự phòng chưa sử dụng, duy trì có chủ đích |
| Gig Economy | Nền kinh tế lao động linh hoạt theo nhu cầu, không cố định dài hạn |
| Monte Carlo Simulation | Phương pháp mô phỏng xác suất dựa trên hàng nghìn kịch bản ngẫu nhiên |
| M/M/c | Mô hình hàng đợi với c quầy phục vụ song song |

### 9.2. Bảng đo lường KPI năng lực

| KPI | Công thức | Mục tiêu tham khảo |
|---|---|---|
| Hiệu suất (Efficiency) | Sản lượng thực tế / Năng lực hiệu quả | > 85% |
| Mức sử dụng (Utilization) | Sản lượng thực tế / Năng lực thiết kế | 75-90% (tránh 100% liên tục) |
| Thời gian ngừng máy (Downtime %) | Thời gian ngừng / Tổng thời gian vận hành | < 10% |
| Thời gian chờ đợi trung bình (dịch vụ) | Theo mô hình hàng đợi | Theo chuẩn ngành/kỳ vọng khách hàng |
| Tỷ lệ tăng trưởng năng lực (Capacity Growth Rate) | (Năng lực mới - Năng lực cũ) / Năng lực cũ | Theo kế hoạch chiến lược |

### 9.3. Sổ tay rủi ro hoạch định năng lực (Risk Register mẫu)

| Rủi ro | Xác suất | Tác động | Biện pháp giảm thiểu |
|---|---|---|---|
| Dự báo nhu cầu sai lệch lớn dẫn đến đầu tư dư thừa | Trung bình | Cao | Kịch bản dự báo đa chiều, đầu tư theo giai đoạn |
| Sự kiện bất khả kháng làm sụp đổ nhu cầu (như COVID-19) | Thấp | Rất cao | Điều khoản hợp đồng linh hoạt, kế hoạch BCP |
| Nút thắt cổ chai mới xuất hiện sau khi giải quyết cái cũ | Cao | Trung bình | Giám sát liên tục toàn bộ chuỗi quy trình |
| Thiếu lao động có kỹ năng khi mở rộng nhanh | Trung bình | Trung bình | Kế hoạch đào tạo trước, tính đến đường cong học tập |
| Phụ thuộc quá mức vào đối tác thuê ngoài năng lực | Trung bình | Trung bình | Đa dạng hoá đối tác, hợp đồng dịch vụ rõ ràng về SLA |
| Đầu tư công nghệ tự động hoá không phù hợp quy mô | Thấp | Cao | Đánh giá kỹ ROI và quy mô tối thiểu hiệu quả trước đầu tư |

### 9.4. Bảng tham chiếu nhanh các công thức cốt lõi

| Mục tiêu | Công thức |
|---|---|
| Hiệu suất | $\text{Efficiency} = \text{Sản lượng thực tế}/\text{Năng lực hiệu quả}$ |
| Mức sử dụng | $\text{Utilization} = \text{Sản lượng thực tế}/\text{Năng lực thiết kế}$ |
| Điểm hòa vốn | $Q^* = FC/(P-VC)$ |
| Hệ số sử dụng hàng đợi | $\rho = \lambda/\mu$ |
| Thời gian chờ M/M/1 | $W_q = \lambda/[\mu(\mu-\lambda)]$ |
| Đường cong học tập | $T_n = T_1 \times n^{\log_2(r)}$ |
| Capacity Cushion | $100\% - \text{Utilization Rate}$ |

### 9.5. Ghi chú kết thúc file

File này kết hợp giữa lý thuyết định lượng (Break-even Analysis, Queuing Theory, Learning Curve, Line Balancing) và các chiến lược định tính (Lead/Lag/Match Strategy) để cung cấp bức tranh toàn diện về hoạch định năng lực. Người đọc nên lưu ý rằng hoạch định năng lực không chỉ là bài toán kỹ thuật mà còn là quyết định chiến lược cấp cao, đòi hỏi sự phối hợp giữa bộ phận vận hành, tài chính và chiến lược kinh doanh tổng thể của doanh nghiệp. Phần phụ lục bổ sung về năng lực linh hoạt (flexible capacity, gig economy) phản ánh xu hướng chuyển dịch quan trọng trong tư duy quản trị năng lực hiện đại, đặc biệt phù hợp với bối cảnh kinh doanh biến động nhanh tại Việt Nam.

---

## X. Tài liệu tham khảo

### Sách tham khảo
1. Slack, N., Brandon-Jones, A., & Johnston, R. (2016). *Operations Management*. Pearson.
2. Goldratt, E. M. (1984). *The Goal: A Process of Ongoing Improvement*. North River Press.
3. Chase, R. B., Jacobs, F. R., & Aquilano, N. J. (2014). *Operations and Supply Chain Management*. McGraw-Hill.
4. Hillier, F. S. & Lieberman, G. J. (2014). *Introduction to Operations Research* (chương về Queuing Theory).
5. Heizer, J., Render, B., & Munson, C. (2020). *Operations Management: Sustainability and Supply Chain Management*. Pearson.

### Liên kết nội bộ (Internal Cross-links)
- [01-process-design-analysis.md](./01-process-design-analysis.md) - Little's Law và nền tảng phân tích quy trình liên quan đến năng lực.
- [04-inventory-management.md](./04-inventory-management.md) - Chiến lược Level trong Aggregate Planning gắn liền với tồn kho đệm.
- [06-project-management.md](./06-project-management.md) - Hoạch định nguồn lực dự án liên quan đến năng lực đội ngũ.
- [07-forecasting.md](./07-forecasting.md) - Dự báo nhu cầu là bước đầu tiên bắt buộc trong quy trình hoạch định năng lực.
- [09-theory-of-constraints.md](./09-theory-of-constraints.md) - Phân tích chuyên sâu về nút thắt cổ chai và Lý thuyết ràng buộc.

### Nguồn học trực tuyến
- ASCM CPIM - chứng chỉ về hoạch định sản xuất và năng lực.
- Coursera: "Operations Management" - University of Pennsylvania (Wharton).
- MIT OpenCourseWare: "Operations Management" - tài liệu mở về Queuing Theory và Capacity Planning.

---

## Phụ lục bổ sung: Hoạch định năng lực trong bối cảnh chuyển đổi số

### A.1. Mô hình hàng đợi đa quầy (M/M/c) và ứng dụng thực tế

Trong thực tế, hầu hết hệ thống dịch vụ có nhiều quầy phục vụ song song (c quầy) thay vì chỉ 1 quầy như mô hình M/M/1 cơ bản. Mô hình M/M/c phức tạp hơn về mặt toán học nhưng nguyên lý cốt lõi tương tự: hệ số sử dụng năng lực tổng thể là

$$\rho = \frac{\lambda}{c \times \mu}$$

Trong đó $c$ là số quầy phục vụ song song. Khi $\rho$ tiến gần 1 (tức tổng năng lực phục vụ gần bằng nhu cầu), thời gian chờ đợi tăng phi tuyến tính tương tự mô hình đơn quầy, nhưng việc có nhiều quầy giúp giảm biến động ngẫu nhiên tốt hơn (một quầy tạm ngừng không làm sụp đổ toàn hệ thống).

**Ứng dụng thực tế**: Các trung tâm chăm sóc khách hàng (call center), quầy thu ngân siêu thị, cửa khẩu sân bay đều áp dụng mô hình M/M/c để xác định số lượng nhân viên/quầy tối ưu theo từng khung giờ trong ngày, cân bằng giữa chi phí nhân sự và trải nghiệm khách hàng.

### A.2. Năng lực linh hoạt và Nền kinh tế chia sẻ (Flexible Capacity & Gig Economy)

Xu hướng hiện đại trong hoạch định năng lực là chuyển từ đầu tư tài sản cố định (fixed asset) sang mô hình năng lực linh hoạt, đặc biệt phổ biến trong ngành logistics và dịch vụ:

| Mô hình | Mô tả | Ví dụ |
|---|---|---|
| Gig Economy Labor | Thuê lao động tự do theo nhu cầu thời điểm | Grab, ShopeeFood thuê tài xế đối tác thay vì nhân viên cố định |
| Cloud Kitchen | Thuê bếp trung tâm dùng chung, không đầu tư mặt bằng riêng | Các thương hiệu F&B mới ra mắt thử nghiệm thị trường |
| Warehouse-as-a-Service | Thuê không gian kho theo nhu cầu thời điểm (mùa cao điểm) | Amazon FBA, các dịch vụ fulfillment bên thứ ba tại Việt Nam |
| Cloud Computing (IaaS) | Thuê năng lực tính toán theo nhu cầu thay vì đầu tư server | AWS, Google Cloud - mở rộng/thu hẹp năng lực tính toán tức thời |

**Lợi ích chính**: Giảm rủi ro đầu tư dư thừa năng lực cố định, chuyển chi phí cố định (Fixed Cost) thành chi phí biến đổi (Variable Cost), tăng khả năng thích ứng nhanh với biến động thị trường - đặc biệt quan trọng với SME có nguồn vốn hạn chế.

**Hạn chế**: Chi phí trên mỗi đơn vị thường cao hơn so với đầu tư sở hữu trực tiếp về dài hạn, phụ thuộc vào bên thứ ba nên có rủi ro về kiểm soát chất lượng và tính sẵn có.

### A.3. Mô phỏng Monte Carlo trong hoạch định năng lực dưới điều kiện bất định

Đối với các quyết định đầu tư năng lực có mức độ bất định cao (nhu cầu thị trường mới, sản phẩm mới chưa có dữ liệu lịch sử), phương pháp mô phỏng Monte Carlo giúp đánh giá xác suất thành công của các phương án đầu tư bằng cách chạy hàng nghìn kịch bản ngẫu nhiên dựa trên phân phối xác suất của các biến đầu vào (nhu cầu, giá bán, chi phí).

**Quy trình cơ bản**:
1. Xác định các biến bất định chính (nhu cầu, giá, chi phí vận hành) và phân phối xác suất của chúng.
2. Chạy mô phỏng hàng nghìn lần với các giá trị ngẫu nhiên rút từ phân phối đã xác định.
3. Tổng hợp kết quả thành phân phối xác suất của lợi nhuận/ROI cho mỗi phương án đầu tư.
4. So sánh xác suất đạt mục tiêu tài chính giữa các phương án để ra quyết định.

Phương pháp này phổ biến trong các doanh nghiệp lớn khi quyết định đầu tư nhà máy mới, mở rộng dây chuyền sản xuất quy mô lớn, nơi sai lầm dự báo có thể gây thiệt hại hàng trăm tỷ đồng.

### A.4. Hoạch định năng lực và tính bền vững (Sustainability trong Capacity Planning)

Xu hướng ESG cũng ảnh hưởng đến quyết định hoạch định năng lực hiện đại:

- **Hiệu quả năng lượng**: đầu tư máy móc mới cần cân nhắc mức tiêu thụ năng lượng/đơn vị sản phẩm, không chỉ công suất tối đa.
- **Khả năng tái sử dụng/tái cấu hình**: thiết kế dây chuyền có thể điều chỉnh linh hoạt giữa các dòng sản phẩm khác nhau (flexible manufacturing system) giúp giảm lãng phí đầu tư khi nhu cầu sản phẩm thay đổi.
- **Quy mô tối thiểu hiệu quả (Minimum Efficient Scale)**: cân nhắc quy mô đầu tư đủ lớn để đạt hiệu quả kinh tế theo quy mô (economies of scale) nhưng không quá lớn gây lãng phí tài nguyên nếu nhu cầu không đạt kỳ vọng.

### A.5. Bảng so sánh nhanh sở hữu tài sản (Own) vs Thuê ngoài năng lực (Outsource/Rent)

| Tiêu chí | Sở hữu (Own Capacity) | Thuê ngoài (Outsource/Flexible) |
|---|---|---|
| Chi phí cố định | Cao (đầu tư ban đầu lớn) | Thấp (chuyển thành chi phí biến đổi) |
| Kiểm soát chất lượng | Cao, trực tiếp quản lý | Phụ thuộc năng lực đối tác |
| Tính linh hoạt | Thấp, khó điều chỉnh nhanh | Cao, dễ tăng/giảm theo nhu cầu |
| Phù hợp | Nhu cầu ổn định, dài hạn, chiến lược cốt lõi | Nhu cầu biến động, thời vụ, không phải năng lực cốt lõi |
| Rủi ro | Dư thừa/thiếu hụt khi dự báo sai | Phụ thuộc đối tác, rủi ro nguồn cung dịch vụ |

### A.6. Case study bổ sung: FPT Software - Hoạch định năng lực nhân sự công nghệ

**Bối cảnh**: FPT Software là doanh nghiệp gia công phần mềm lớn tại Việt Nam, năng lực cốt lõi của doanh nghiệp chính là đội ngũ kỹ sư phần mềm - một dạng "năng lực" đặc thù khác với năng lực máy móc trong sản xuất truyền thống.

**Thách thức**: Nhu cầu dự án từ khách hàng quốc tế biến động liên tục, một dự án lớn có thể cần huy động 200-300 kỹ sư trong vài tháng, trong khi việc tuyển dụng và đào tạo kỹ sư mới đạt năng lực đầy đủ cần thời gian dài (đường cong học tập kéo dài nhiều tháng đối với kỹ sư mới).

**Giải pháp áp dụng**:
- Xây dựng "bench" (đội ngũ nhân sự dự phòng chưa phân bổ dự án cụ thể) làm vùng đệm năng lực, tương tự khái niệm Safety Stock trong quản trị tồn kho.
- Áp dụng mô hình đào tạo nội bộ liên tục (FPT University, FPT Academy) để rút ngắn đường cong học tập cho kỹ sư mới.
- Hợp tác với mạng lưới đối tác/freelancer bên ngoài để xử lý các đợt tăng đột biến ngắn hạn mà không cần tuyển dụng chính thức ngay (tương tự mô hình gig economy).
- Dự báo nhu cầu nhân sự dựa trên pipeline hợp đồng ký kết và xác suất chốt hợp đồng mới.

**Kết quả**: Duy trì tỷ lệ sử dụng nhân sự (utilization rate) ở mức tối ưu, tránh tình trạng vừa thiếu nhân sự cho dự án gấp vừa dư thừa nhân sự nhàn rỗi ở bộ phận khác - một bài toán hoạch định năng lực đặc thù của ngành dịch vụ tri thức (knowledge-based services).

### A.7. Chỉ số năng lực dự phòng chiến lược (Strategic Capacity Cushion)

Nhiều doanh nghiệp chủ động duy trì một tỷ lệ năng lực dự phòng (capacity cushion) thay vì vận hành ở mức tối đa, nhằm ứng phó với biến động nhu cầu bất ngờ hoặc cơ hội kinh doanh đột xuất:

$$\text{Capacity Cushion} = 100\% - \text{Utilization Rate}$$

| Ngành | Tỷ lệ dự phòng năng lực điển hình | Lý do |
|---|---|---|
| Bệnh viện/cấp cứu | 30-40% | Phải sẵn sàng ứng phó ca cấp cứu bất ngờ |
| Sản xuất hàng tiêu dùng ổn định | 10-15% | Nhu cầu dự báo tương đối chính xác |
| Trung tâm dữ liệu (Data Center) | 20-30% | Đảm bảo hiệu suất khi có đợt tải đột biến |
| Ngành thời trang/theo mùa | 25-35% | Biến động nhu cầu cao theo mùa và xu hướng |

Việc xác định tỷ lệ dự phòng năng lực phù hợp là một quyết định chiến lược quan trọng, cân bằng giữa chi phí duy trì năng lực nhàn rỗi và rủi ro không đáp ứng được nhu cầu đột biến hoặc cơ hội kinh doanh mới.
