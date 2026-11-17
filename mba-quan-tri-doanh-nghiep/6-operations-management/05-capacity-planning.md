# 05. Hoạch định Năng lực (Capacity Planning)

> **Mục tiêu**: Hiểu bản chất của "năng lực" (capacity), biết đo lường nó bằng các chỉ số định lượng (hiệu suất, mức sử dụng, điểm hòa vốn, hàng đợi, đường cong học tập), và biết ra quyết định **đầu tư bao nhiêu, khi nào, theo cách nào** (xây trước, xây sau, thuê ngoài hay chờ) với dữ liệu và phép tính cụ thể thay vì cảm tính.

> File thuộc bộ kiến thức Quản trị Vận hành (Operations Management) - MBA Knowledge Base
> Liên kết: [01-process-design-analysis.md](./01-process-design-analysis.md) | [04-inventory-management.md](./04-inventory-management.md) | [06-project-management.md](./06-project-management.md)

**Quy ước số liệu trong file**: các số liệu gắn nhãn "giả định minh họa" do tác giả tự thiết kế để làm rõ cách tính, KHÔNG phải số liệu thật của doanh nghiệp được nhắc tên. Các con số của công ty thật (Amazon, Highlands Coffee, FPT Software, các hãng hàng không) chỉ mang tính mô tả định tính hoặc "ước tính/minh họa".

---

## MỤC LỤC

- I. Khái niệm & Lý thuyết nền tảng (định nghĩa, 3 loại năng lực, break-even, Lead/Lag/Match, Aggregate Planning)
- II. Chi tiết từng công cụ/kỹ thuật (Nút thắt cổ chai, hàng đợi M/M/1 và M/M/c, đường cong học tập, cân bằng chuyền, CRP, Aggregate Planning có tính toán, năng lực dự phòng, sở hữu vs thuê ngoài, cây quyết định, Monte Carlo, ESG, ưu/nhược điểm)
- III. Case Studies thực tế (Amazon, Highlands Coffee, xưởng may Bình Dương, ngành hàng không, phòng khám TP.HCM, FPT Software, SME mới: Cà phê Đất Đỏ, bảng tổng hợp)
- IV. Ứng dụng cho SME (quy trình 7 bước, sai lầm thường gặp, SME vs doanh nghiệp lớn, lộ trình, sổ tay rủi ro)
- V. Tools & Templates
- VI. Bài tập thực hành (kèm đáp án)
- PHỤ LỤC: Checklist Hoạch định Năng lực tổng hợp (checklist, KPI, thuật ngữ, công thức tổng hợp)
- Tài liệu tham khảo

---

## I. Khái niệm & Lý thuyết nền tảng

### 1.1. Định nghĩa Năng lực và Hoạch định Năng lực

**Năng lực (Capacity)** là mức sản lượng tối đa mà một hệ thống (nhà máy, dây chuyền, cửa hàng, đội ngũ nhân viên) có thể tạo ra trong một khoảng thời gian nhất định, với các điều kiện vận hành bình thường.

**Hoạch định năng lực (Capacity Planning)** là quá trình xác định năng lực sản xuất/phục vụ cần thiết để đáp ứng nhu cầu hiện tại và tương lai của doanh nghiệp, đồng thời quyết định thời điểm, quy mô và cách thức đầu tư mở rộng (hoặc thu hẹp) năng lực.

Đây là quyết định chiến lược có tác động dài hạn: đầu tư thừa năng lực gây lãng phí vốn, đầu tư thiếu gây mất doanh số và mất khách hàng vào tay đối thủ.

**Tại sao hoạch định năng lực lại khó và quan trọng?** Có ba đặc điểm khiến nó khác với các quyết định vận hành hằng ngày:

1. **Năng lực đến theo "từng bậc" (lumpy)**: bạn không thể mua 0.3 cái lò nướng hay thuê 0.5 bác sĩ cố định. Năng lực tăng theo từng bước lớn, nên mỗi lần đầu tư thường "thừa" một chút so với nhu cầu ngay lúc đó.
2. **Độ trễ (lead time)**: từ lúc ra quyết định đến lúc năng lực hoạt động được (xây xưởng, nhập máy, tuyển và đào tạo người) mất vài tuần đến vài năm. Trong khoảng đó nhu cầu có thể đã khác.
3. **Khó đảo ngược (irreversibility)**: máy móc, mặt bằng đã mua rất khó bán lại nguyên giá. Sai lầm kéo dài nhiều năm dưới dạng khấu hao và chi phí cố định.

**Nguồn gốc**: Vấn đề năng lực xuất hiện cùng nền sản xuất công nghiệp. Dây chuyền lắp ráp của Henry Ford (Highland Park, 1913) buộc các nhà quản lý lần đầu phải cân đối năng lực giữa các công đoạn nối tiếp. Sau đó các nhánh của khoa học quản trị lần lượt bổ sung công cụ: lý thuyết hàng đợi (A. K. Erlang, 1909, bài toán tổng đài điện thoại), đường cong học tập (T. P. Wright, 1936, ngành chế tạo máy bay), hoạch định tổng hợp (Holt, Modigliani, Muth, Simon, giữa thập niên 1950), và Lý thuyết ràng buộc (E. Goldratt, 1984). File này tổng hợp các công cụ đó thành một bộ để trả lời trọn vẹn câu hỏi: "Tôi cần bao nhiêu năng lực, khi nào, và nên có nó bằng cách nào?"

### 1.2. Ba loại năng lực cần phân biệt

**Tại sao phải phân biệt?** Nhiều chủ doanh nghiệp nói "máy tôi chạy 1,000 sản phẩm/ngày" nhưng thực tế chưa bao giờ đạt. Lý do là họ trộn lẫn ba khái niệm khác nhau. Mỗi loại trả lời một câu hỏi khác nhau: thiết kế cho biết "trần lý thuyết", năng lực hiệu quả cho biết "trần thực tế có thể duy trì", sản lượng thực tế cho biết "ta đang làm được bao nhiêu".

| Loại năng lực | Định nghĩa | Ví dụ |
|---|---|---|
| **Năng lực thiết kế (Design Capacity)** | Sản lượng tối đa lý thuyết trong điều kiện lý tưởng | Dây chuyền thiết kế cho 1,000 sản phẩm/ngày |
| **Năng lực hiệu quả (Effective Capacity)** | Sản lượng tối đa thực tế có thể đạt được, trừ đi các yếu tố như bảo trì, thay đổi sản phẩm, nghỉ lễ | 850 sản phẩm/ngày (85% năng lực thiết kế) |
| **Sản lượng thực tế (Actual Output)** | Sản lượng thực sự đạt được, có thể thấp hơn năng lực hiệu quả do sự cố, chất lượng kém, thiếu nguyên liệu | 750 sản phẩm/ngày |

**Hai chỉ số hiệu suất** (khoảng cách giữa 3 loại năng lực trên cho ta hai "thước đo"):

$$\text{Hiệu suất (Efficiency)} = \frac{\text{Sản lượng thực tế}}{\text{Năng lực hiệu quả}} \times 100\%$$

$$\text{Mức sử dụng (Utilization)} = \frac{\text{Sản lượng thực tế}}{\text{Năng lực thiết kế}} \times 100\%$$

**Logic đằng sau hai công thức**:
- **Hiệu suất** lấy *năng lực hiệu quả* làm mẫu số, tức là so sánh với mức "hợp lý đạt được". Chỉ số này đo **việc quản lý vận hành tốt đến đâu**: sự cố, phế phẩm, thiếu nguyên liệu, thao tác chậm đều kéo nó xuống. Nó trả lời "chúng ta có đang làm tốt trong giới hạn thực tế không?"
- **Mức sử dụng** lấy *năng lực thiết kế* làm mẫu số, tức là so với mức "tối đa trên giấy". Chỉ số này đo **mức độ khai thác tài sản đã đầu tư**. Nó trả lời "đồng vốn đã bỏ vào máy móc đang được dùng đến mức nào?"
- Khoảng cách giữa năng lực thiết kế và hiệu quả (15% trong ví dụ) là phần **không thể tránh** (bảo trì, nghỉ lễ, đổi mẫu); khoảng cách giữa hiệu quả và thực tế (100 sản phẩm) là phần **có thể cải thiện** bằng quản lý. Vì vậy chủ doanh nghiệp nên tập trung vào Hiệu suất khi muốn cải tiến vận hành, và nhìn Mức sử dụng khi cân nhắc có nên đầu tư thêm hay không.

**Ví dụ từng bước** (số liệu ở bảng trên):

| Bước | Phép tính | Kết quả |
|---|---|---|
| 1 | Năng lực hiệu quả / thiết kế = 850 / 1,000 | 85% |
| 2 | Hiệu suất = 750 / 850 | 88.2% |
| 3 | Mức sử dụng = 750 / 1,000 | 75.0% |

Diễn giải: dây chuyền đang vận hành tốt (hiệu suất 88.2%, vượt mốc tham khảo 85%), nhưng chỉ khai thác 75% tài sản thiết kế. Trước khi đầu tư dây chuyền mới, nên hỏi: "Có thể bán thêm 100 sản phẩm/ngày (đến mức hiệu quả 850) mà không cần chi vốn không?" Nếu nhu cầu thực sự vượt 850, mới đến lượt đầu tư.

### 1.3. Đường cong năng lực và điểm hòa vốn (Break-Even Analysis)

**Vấn đề kinh doanh cần giải quyết**: Mở rộng năng lực luôn kéo theo **chi phí cố định (Fixed Cost - FC)** mới (khấu hao máy, lương quản lý, tiền thuê mặt bằng...) không phụ thuộc bạn bán được bao nhiêu. Câu hỏi sống còn: "Phải bán tối thiểu bao nhiêu thì khoản chi phí cố định này được bù đắp?" Phân tích điểm hòa vốn trả lời câu hỏi đó. Nó được dùng rộng rãi trong kế toán quản trị từ đầu thế kỷ 20 vì cực kỳ đơn giản và buộc người ra quyết định phải tách bạch chi phí cố định với chi phí biến đổi.

**Logic của công thức**: mỗi đơn vị bán ra đóng góp một phần "lợi nhuận góp" (Contribution Margin = P - VC) để trang trải chi phí cố định. Cần bán đủ bao nhiêu đơn vị để tổng phần góp bằng FC? Chia FC cho phần góp mỗi đơn vị.

$$Q^* = \frac{FC}{P - VC}$$

Trong đó:
- $Q^*$ = sản lượng hòa vốn (Break-Even Point), đơn vị sản phẩm
- $FC$ = tổng chi phí cố định trong kỳ (VNĐ)
- $P$ = giá bán mỗi đơn vị (VNĐ)
- $VC$ = chi phí biến đổi mỗi đơn vị (VNĐ)
- $P - VC$ = lợi nhuận góp trên mỗi đơn vị (Contribution Margin)

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

**Ví dụ từng bước** (giả định minh họa: một cơ sở sản xuất bánh mua thêm lò nướng công nghiệp):

| Bước | Nội dung | Kết quả |
|---|---|---|
| 1 | Chi phí cố định tăng thêm: khấu hao + nhân công cơ bản + bảo trì | FC = 360 triệu/năm |
| 2 | Giá bán P = 120,000 VNĐ/đơn vị; chi phí biến đổi VC = 70,000 VNĐ/đơn vị | P - VC = 50,000 VNĐ |
| 3 | Q* = 360,000,000 / 50,000 | **7,200 đơn vị/năm** |
| 4 | Năng lực của lò mới = 9,000 đơn vị/năm. Tỷ lệ công suất tại điểm hòa vốn = 7,200 / 9,000 | **80%** |
| 5 | Nếu nhu cầu thực tế là 8,400: biên an toàn = (8,400 - 7,200)/8,400 | **14.3%** |
| 6 | Lợi nhuận tại 8,400 = (8,400 - 7,200) x 50,000 | **60 triệu/năm** |

**Diễn giải kinh doanh**: bước 4 mới là điểm đáng lo. Lò mới phải chạy ít nhất 80% công suất mới hòa vốn, nghĩa là chỉ cần nhu cầu thấp hơn dự báo khoảng 14% là dự án bắt đầu lỗ. Một dự án "hòa vốn ở 80% công suất" là dự án rủi ro cao, đặc biệt với SME ít vốn. Quy tắc kinh nghiệm: điểm hòa vốn nên nằm dưới khoảng 60-70% năng lực, hoặc phải có đơn hàng cam kết bù lại.

Khi quyết định đầu tư mở rộng năng lực (mua thêm máy móc, mở thêm chi nhánh), doanh nghiệp cần so sánh điểm hòa vốn mới với dự báo nhu cầu để đánh giá tính khả thi tài chính của quyết định.

**Giới hạn của công cụ**: break-even là phân tích "tĩnh" (một mức giá, một mức chi phí, không có giá trị thời gian của tiền). Với quyết định lớn, phải kết hợp với NPV/dòng tiền chiết khấu (xem mục 2.10 và [3-financial/01-time-value-of-money.md](../3-financial/01-time-value-of-money.md)).

### 1.4. Chiến lược thời điểm hoạch định năng lực (Capacity Timing Strategies)

**Vấn đề**: Nhu cầu tăng liên tục nhưng năng lực tăng theo bậc thang. Câu hỏi là "bậc thang" nên đặt **trước**, **sau** hay **ngang** đường nhu cầu?

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

**Logic lựa chọn**: ba chiến lược thực chất là ba mức "khẩu vị rủi ro" khác nhau trước hai loại sai lầm. Lead chọn tránh **chi phí cơ hội** (mất khách) và chấp nhận **chi phí tài sản nhàn rỗi**. Lag làm ngược lại. Câu trả lời đúng phụ thuộc vào cái nào đắt hơn trong ngành của bạn: nếu mất một khách hàng là mất vĩnh viễn (thị trường winner-takes-most, sản phẩm có hiệu ứng mạng) thì Lead hợp lý; nếu khách hàng sẵn sàng chờ hoặc tài sản rất đắt, hãy Lag.

### 1.5. Hoạch định năng lực tổng hợp (Aggregate Planning)

Aggregate Planning là quá trình hoạch định mức sản lượng, tồn kho, nhân lực trong trung hạn (3-18 tháng) để đáp ứng nhu cầu dao động theo mùa vụ mà không cần thay đổi năng lực cố định (nhà xưởng, máy móc). Phương pháp này được hệ thống hóa bởi nhóm Holt, Modigliani, Muth và Simon vào giữa thập niên 1950 (mô hình "quy tắc quyết định tuyến tính" cho một nhà máy sơn), với ý tưởng: thay vì lập kế hoạch cho từng sản phẩm, hãy gộp thành một "đơn vị tổng hợp" rồi tối ưu tổng chi phí của ba đòn bẩy: nhân lực, tăng ca, tồn kho.

**Ba chiến lược cơ bản trong Aggregate Planning**:

1. **Chiến lược đuổi theo (Chase Strategy)**: điều chỉnh nhân lực/sản lượng theo sát biến động nhu cầu (tuyển thêm/cắt giảm lao động thời vụ, tăng ca/giảm giờ làm).
2. **Chiến lược san bằng (Level Strategy)**: duy trì mức sản xuất/nhân lực ổn định, sử dụng tồn kho để hấp thụ biến động nhu cầu (sản xuất nhiều hơn nhu cầu lúc thấp điểm, dự trữ cho lúc cao điểm).
3. **Chiến lược hỗn hợp (Mixed/Hybrid Strategy)**: kết hợp cả hai, ví dụ duy trì lực lượng lao động cơ bản ổn định + thuê lao động thời vụ khi cao điểm + xây dựng tồn kho đệm vừa phải.

| Chiến lược | Ưu điểm | Nhược điểm |
|---|---|---|
| Chase Strategy | Không tốn chi phí tồn kho, linh hoạt theo nhu cầu | Chi phí tuyển dụng/sa thải cao, ảnh hưởng tinh thần nhân viên |
| Level Strategy | Ổn định lực lượng lao động, dễ quản lý chất lượng | Chi phí lưu kho cao, rủi ro tồn kho lỗi thời |
| Mixed Strategy | Cân bằng chi phí và tính linh hoạt | Phức tạp hơn trong hoạch định và điều phối |

Ví dụ tính toán chi tiết ba chiến lược nằm ở mục 2.7.

### 1.6. Bản đồ công cụ: vấn đề nào dùng công cụ nào?

| Câu hỏi của nhà quản lý | Công cụ phù hợp | Mục |
|---|---|---|
| Hệ thống của tôi thực sự làm tối đa được bao nhiêu? | 3 loại năng lực, Hiệu suất, Mức sử dụng | 1.2 |
| Đầu tư thêm có đáng không? Bán bao nhiêu thì hòa vốn? | Break-even, NPV, cây quyết định | 1.3, 2.10 |
| Nên đầu tư trước, sau hay song hành với nhu cầu? | Lead/Lag/Match | 1.4 |
| Cải thiện chỗ nào thì năng lực toàn hệ thống tăng? | Nút thắt cổ chai (TOC) | 2.1 |
| Cần bao nhiêu nhân viên/quầy để khách không phải chờ lâu? | Hàng đợi M/M/1, M/M/c | 2.2, 2.3 |
| Nhân viên/chuyền mới bao lâu thì đạt năng suất? | Đường cong học tập | 2.4 |
| Chia việc đều giữa các trạm thế nào? | Cân bằng chuyền | 2.5 |
| Nhu cầu mùa vụ: tuyển, tăng ca hay tích trữ? | Aggregate Planning | 1.5, 2.7 |
| Nên chừa bao nhiêu % năng lực dự phòng? | Capacity Cushion | 2.8 |
| Tự đầu tư hay thuê ngoài? | So sánh Own vs Outsource | 2.9 |
| Nhu cầu quá bất định, xác suất thành công là bao nhiêu? | Monte Carlo | 2.11 |

---

## II. Chi tiết từng công cụ/kỹ thuật

### 2.1. Lý thuyết ràng buộc và Nút thắt cổ chai (Theory of Constraints - Bottleneck Analysis)

**Vấn đề kinh doanh**: Nhiều doanh nghiệp đầu tư vào công đoạn "dễ thấy" nhất (máy mới, người mới) nhưng sản lượng toàn xưởng không tăng. Nguyên nhân: họ đầu tư sai chỗ. Trong chuỗi nối tiếp, sản lượng chung bằng sản lượng của công đoạn chậm nhất, giống như một sợi xích chỉ bền bằng mắt xích yếu nhất. Eliyahu Goldratt (nhà vật lý người Israel) phổ biến ý tưởng này trong tiểu thuyết quản trị "The Goal" (1984), sau đó phát triển thành Lý thuyết ràng buộc (Theory of Constraints - TOC).

Trong một chuỗi quy trình sản xuất gồm nhiều công đoạn nối tiếp, năng lực tổng thể của toàn hệ thống luôn bị giới hạn bởi công đoạn có năng lực thấp nhất - gọi là **nút thắt cổ chai (Bottleneck)**.

```
Công đoạn 1      Công đoạn 2      Công đoạn 3      Công đoạn 4
(100 SP/giờ) ──▶ (60 SP/giờ) ──▶ (90 SP/giờ) ──▶ (120 SP/giờ)
                      ▲
                 NÚT THẮT CỔ CHAI (Bottleneck)
                 Năng lực toàn hệ thống = 60 SP/giờ
                 (dù các công đoạn khác có năng lực cao hơn)
```

**Hệ quả quan trọng**:
- Một giờ ngừng máy ở nút thắt = mất một giờ sản lượng của **cả hệ thống**. Một giờ ngừng máy ở công đoạn khác thường không mất gì (còn dư năng lực).
- Tăng năng lực ở công đoạn không phải nút thắt = **không tạo thêm một đơn vị sản lượng nào**, chỉ tốn tiền.
- Khi nâng nút thắt cũ, nút thắt **chuyển sang** công đoạn chậm kế tiếp. Ví dụ trên: nâng công đoạn 2 từ 60 lên 120 SP/giờ thì hệ thống chỉ lên 90 SP/giờ (công đoạn 3 trở thành nút thắt mới), tức tăng 50% thay vì 100%.

**Nguyên lý quản trị nút thắt cổ chai (theo Eliyahu Goldratt, "The Goal")** - "5 bước tập trung":
1. Xác định nút thắt cổ chai của hệ thống.
2. Khai thác tối đa nút thắt cổ chai (không để nó ngừng hoạt động, kể cả giờ nghỉ).
3. Điều chỉnh mọi công đoạn khác phục vụ cho nút thắt cổ chai (không sản xuất vượt quá khả năng xử lý của nút thắt).
4. Nâng cấp năng lực của nút thắt cổ chai (đầu tư máy móc, nhân lực).
5. Lặp lại quy trình - vì khi nút thắt cũ được giải quyết, một nút thắt mới sẽ xuất hiện ở công đoạn khác.

(Chủ đề này được phân tích chuyên sâu hơn trong file [09-theory-of-constraints.md](./09-theory-of-constraints.md).)

### 2.2. Phân tích công suất theo hàng đợi - mô hình M/M/1 (Queuing Theory / Waiting Line Analysis)

**Vấn đề kinh doanh**: Trong dịch vụ, năng lực **không thể lưu kho**: quầy thu ngân nhàn rỗi lúc 3 giờ chiều không "để dành" được cho giờ cao điểm. Khách đến ngẫu nhiên, thời gian phục vụ cũng ngẫu nhiên, nên dù năng lực trung bình lớn hơn nhu cầu trung bình, hàng đợi vẫn xuất hiện (khách đến dồn, ca phục vụ lâu). Câu hỏi: cần bao nhiêu năng lực để thời gian chờ ở mức khách chấp nhận được, mà không lãng phí nhân sự?

**Nguồn gốc**: A. K. Erlang, kỹ sư người Đan Mạch của Công ty Điện thoại Copenhagen, công bố những kết quả đầu tiên vào năm 1909 khi nghiên cứu cần bao nhiêu đường dây tổng đài để cuộc gọi không bị nghẽn. Về sau lý thuyết hàng đợi lan sang ngân hàng, bệnh viện, siêu thị, trung tâm dữ liệu. Ký hiệu "M/M/1" (ký hiệu Kendall) nghĩa là: khách đến theo quá trình ngẫu nhiên Poisson (M = Markovian), thời gian phục vụ phân phối mũ (M), có 1 quầy phục vụ.

**Công thức cơ bản mô hình M/M/1 (một quầy phục vụ)**:

$$\rho = \frac{\lambda}{\mu}$$

Trong đó:
- $\lambda$ = Tỷ lệ khách đến trung bình (customers/giờ)
- $\mu$ = Tỷ lệ phục vụ trung bình của 1 quầy (customers/giờ)
- $\rho$ = Hệ số sử dụng (Utilization Factor), phải nhỏ hơn 1 để hệ thống ổn định

**Thời gian chờ trung bình trong hàng đợi**:

$$W_q = \frac{\rho}{\mu(1-\rho)} = \frac{\lambda}{\mu(\mu-\lambda)}$$

**Các chỉ số khác của M/M/1**:

$$L_q = \frac{\lambda^2}{\mu(\mu-\lambda)} \qquad L_s = \frac{\lambda}{\mu-\lambda} \qquad W = W_q + \frac{1}{\mu} = \frac{1}{\mu-\lambda}$$

với $L_q$ = số khách trung bình đang xếp hàng, $L_s$ = số khách trung bình trong hệ thống (cả đang được phục vụ), $W$ = tổng thời gian trung bình khách ở trong hệ thống. Chúng liên hệ với nhau qua **Định luật Little** ($L = \lambda W$, xem [01-process-design-analysis.md](./01-process-design-analysis.md)).

**Tại sao $W_q$ có mẫu số $(1-\rho)$?** Đây là chỗ cốt lõi cần hiểu. Khi $\rho$ gần 1, phần năng lực "dư" để xả hàng đợi $(\mu-\lambda)$ gần bằng 0. Mỗi nhóm khách đến dồn sẽ để lại hàng đợi mà hệ thống rất lâu mới "dọn" xong, vì chỉ có rất ít năng lực dư. Vì vậy thời gian chờ tỷ lệ nghịch với **phần năng lực dư** $(\mu - \lambda)$, không phải tỷ lệ với $\rho$.

**Ví dụ từng bước**: quầy thu ngân siêu thị có $\lambda = 30$ khách/giờ, $\mu = 40$ khách/giờ (tức 1.5 phút/khách).

| Bước | Phép tính | Kết quả |
|---|---|---|
| 1 | $\rho = 30/40$ | 0.75 (quầy bận 75% thời gian) |
| 2 | $W_q = 30 / [40 \times (40-30)] = 30/400$ | 0.075 giờ = **4.5 phút** |
| 3 | $L_q = 30^2 / [40 \times 10] = 900/400$ | 2.25 khách xếp hàng |
| 4 | $W = 1/(40-30)$ | 0.1 giờ = 6 phút trong hệ thống |
| 5 | Kiểm tra Little: $L_q = \lambda W_q = 30 \times 0.075$ | 2.25 (khớp bước 3) |

**Cảnh báo phi tuyến**: bảng dưới giữ $\mu = 40$ và tăng dần $\lambda$:

| $\lambda$ (khách/giờ) | $\rho$ | $W_q$ (phút) | $L_q$ (khách) |
|---|---|---|---|
| 30 | 75.0% | 4.5 | 2.25 |
| 34 | 85.0% | 8.5 | 4.82 |
| 36 | 90.0% | 13.5 | 8.10 |
| 38 | 95.0% | 28.5 | 18.05 |
| 39 | 97.5% | 58.5 | 38.03 |

Nhu cầu tăng từ 30 lên 38 (chỉ +27%) nhưng thời gian chờ tăng từ 4.5 lên 28.5 phút (gấp 6.3 lần). Đây là lý do các hệ thống dịch vụ hiệu quả thường không vận hành ở 100% công suất mà giữ khoảng đệm (buffer capacity). Lưu ý chính xác về mặt toán học: thời gian chờ tăng **theo dạng hyperbol** (tiến ra vô cực khi $\rho \to 1$), không phải "theo cấp số nhân", nhưng hệ quả thực tế là như nhau: ở vùng trên 85-90%, mỗi vài phần trăm tăng thêm đều làm thời gian chờ tăng rất mạnh.

### 2.3. Mô hình hàng đợi đa quầy M/M/c và ứng dụng thực tế

**Vấn đề**: Thực tế hầu hết hệ thống dịch vụ có nhiều quầy phục vụ song song ($c$ quầy) cùng chia một hàng đợi chung (ngân hàng, sân bay, call center). Mô hình M/M/c phức tạp hơn nhưng giải quyết đúng câu hỏi quản trị: "Với lượng khách này, cần mở **bao nhiêu quầy** để thời gian chờ nằm trong mục tiêu?"

Hệ số sử dụng tổng thể:

$$\rho = \frac{\lambda}{c \times \mu}$$

Trong đó $c$ là số quầy phục vụ song song và điều kiện ổn định là $\rho < 1$. Với $a = \lambda/\mu$ (tải trọng, đơn vị "Erlang"), **xác suất khách phải chờ** theo công thức **Erlang C**:

$$P_w = \frac{\dfrac{a^c}{c!\,(1-\rho)}}{\displaystyle\sum_{k=0}^{c-1}\frac{a^k}{k!} + \frac{a^c}{c!\,(1-\rho)}} \qquad\qquad W_q = \frac{P_w}{c\mu - \lambda}$$

**Giải thích**: tử số là "xác suất mọi quầy đều đang bận" (khi đó khách mới phải xếp hàng); $W_q = P_w/(c\mu-\lambda)$ cho thấy thời gian chờ trung bình bằng xác suất phải chờ nhân với thời gian xả hàng của phần năng lực dư ($c\mu - \lambda$). Công thức này do Erlang xây dựng cho tổng đài điện thoại (nên tên gọi Erlang C), và đến nay vẫn là chuẩn để hoạch định nhân lực call center.

**Tại sao thêm quầy hiệu quả hơn tăng tốc từng quầy?** Hàng chung cho nhiều quầy giúp "gộp" (pooling) biến động ngẫu nhiên: một ca phục vụ lâu ở quầy 1 không làm cả hàng đứng yên vì quầy 2, 3 vẫn xử lý tiếp. Vì vậy với cùng $\rho$, hệ thống nhiều quầy chờ ít hơn hệ thống một quầy. Ngoài ra một quầy tạm ngừng không làm sụp đổ toàn hệ thống.

**Ví dụ từng bước** (giả định minh họa, 1 điểm bán đồ uống giờ cao điểm): $\lambda = 120$ khách/giờ, mỗi nhân viên pha chế phục vụ $\mu = 30$ khách/giờ (2 phút/khách).

| $c$ (số nhân viên) | $\rho = 120/(30c)$ | $P_w$ (xác suất chờ) | $W_q$ (phút) | Nhận xét |
|---|---|---|---|---|
| 4 | 100% | - | vô hạn | Không ổn định, hàng đợi tăng mãi |
| 5 | 80.0% | 55.4% | 1.11 | Chấp nhận được nhưng hơn nửa số khách phải chờ |
| 6 | 66.7% | 28.5% | 0.28 | Tốt |
| 7 | 57.1% | 13.5% | 0.09 | Rất tốt, nhưng dư người |

Hai bài học: (1) với $c = 4$ dù "năng lực trung bình bằng nhu cầu trung bình", hệ thống vẫn sụp đổ, vì không có năng lực dư để xả hàng; (2) hiệu ích biên giảm dần: từ 5 lên 6 nhân viên giảm chờ 0.83 phút, từ 6 lên 7 chỉ giảm 0.19 phút. Mục tiêu hợp lý là điểm dừng ở nơi thời gian chờ đạt chuẩn dịch vụ (ví dụ dưới 1 phút) chứ không phải tối đa hóa số quầy.

**Ứng dụng thực tế**: các trung tâm chăm sóc khách hàng (call center), quầy thu ngân siêu thị, quầy thủ tục sân bay đều áp dụng M/M/c để xác định số nhân viên/quầy theo từng khung giờ trong ngày.

### 2.4. Đường cong học tập (Learning Curve)

**Vấn đề kinh doanh**: Khi mở rộng năng lực (xưởng mới, chuyền mới, nhân viên mới), năng lực **thực tế** ban đầu thấp hơn năng lực thiết kế rất nhiều và tăng dần theo kinh nghiệm. Nếu bỏ qua điều này, kế hoạch giao hàng sẽ trễ và kế hoạch dòng tiền sẽ sai.

**Nguồn gốc**: Theodore P. Wright (kỹ sư hàng không, Curtiss-Wright) công bố năm 1936 sau khi quan sát chi phí lao động để sản xuất máy bay giảm theo quy luật ổn định mỗi khi sản lượng tích lũy tăng gấp đôi. Về sau quy luật được xác nhận rộng rãi trong chế tạo, đóng tàu, bán dẫn, và dịch vụ.

**Logic**: mỗi lần sản lượng tích lũy **gấp đôi**, thời gian (hoặc chi phí) của một đơn vị giảm còn $r$ lần (ví dụ $r = 90\%$ = "đường cong 90%"). Hàm lũy thừa đảm bảo tính chất đó:

$$T_n = T_1 \times n^{\log_2(r)}$$

Trong đó:
- $T_n$ = Thời gian sản xuất đơn vị thứ $n$ (mô hình đơn vị - "unit model" của Crawford; mô hình gốc của Wright áp dụng cho thời gian *trung bình tích lũy*, hai mô hình cho kết quả hơi khác nhau)
- $T_1$ = Thời gian sản xuất đơn vị đầu tiên
- $r$ = Tỷ lệ học tập (Learning Rate): khi sản lượng tích lũy tăng gấp đôi, thời gian của đơn vị thứ $2n$ bằng $r$ lần thời gian đơn vị thứ $n$
- $\log_2(r)$ = số mũ học tập (luôn âm, vì $r<1$)

**Ví dụ từng bước**: $T_1 = 10$ giờ, $r = 90\%$ (giả định minh họa).

| Bước | Phép tính | Kết quả |
|---|---|---|
| 1 | Số mũ: $b = \log_2(0.9) = \ln 0.9 / \ln 2$ | -0.1520 |
| 2 | Đơn vị thứ 2: $10 \times 2^{-0.152}$ | 9.00 giờ (= 90% của 10) |
| 3 | Đơn vị thứ 4: $10 \times 4^{-0.152}$ | 8.10 giờ (= 90% của 9.00) |
| 4 | Đơn vị thứ 8 | 7.29 giờ |
| 5 | Đơn vị thứ 50: $10 \times 50^{-0.152}$ | 5.52 giờ |
| 6 | Đơn vị thứ 100: $10 \times 100^{-0.152}$ | 4.97 giờ |
| 7 | Tổng giờ làm 50 đơn vị đầu (cộng dồn) | 321.4 giờ (trung bình 6.43 giờ/đv) |
| 8 | Tổng giờ làm 100 đơn vị đầu (cộng dồn) | 581.4 giờ (trung bình 5.81 giờ/đv) |

**Diễn giải**: đơn vị thứ 100 chỉ mất khoảng một nửa thời gian của đơn vị thứ nhất. Nếu lập kế hoạch năng lực bằng $T_1$ cho cả 100 đơn vị, ta ước tính 1,000 giờ - gấp 1.7 lần so với thực tế 581 giờ. Ngược lại, nếu dùng $T_{100}$ cho giai đoạn đầu, ta sẽ ước tính sai nghiêm trọng khả năng giao hàng 3-6 tháng đầu.

**Ứng dụng**: khi hoạch định năng lực cho dây chuyền sản xuất mới hoặc nhân viên mới, cần tính đến giai đoạn "làm quen" (ramp-up period) trong 3-6 tháng đầu, năng lực thực tế sẽ thấp hơn năng lực thiết kế đáng kể. Đào tạo bài bản, tài liệu hướng dẫn chuẩn (SOP) và kèm cặp (mentoring) giúp đường cong dốc hơn (r nhỏ hơn).

### 2.5. Cân bằng chuyền sản xuất (Line Balancing)

**Vấn đề kinh doanh**: Trên dây chuyền gồm nhiều trạm nối tiếp, trạm chậm nhất quyết định nhịp của cả chuyền (đúng nguyên lý nút thắt). Nếu việc chia không đều, các trạm nhanh sẽ chờ - đó là thời gian nhàn rỗi (idle time) - tức lãng phí lao động đã trả lương. Cân bằng chuyền là kỹ thuật chia công việc đều giữa các trạm để tối thiểu hóa lãng phí đó. Nó ra đời cùng dây chuyền lắp ráp ở nhà máy Ford (đầu thế kỷ 20) và được hệ thống hóa thành thuật toán trong các thập niên 1950-1960.

**Công thức Cycle Time (Nhịp sản xuất) tối đa cho phép**:

$$C = \frac{\text{Thời gian sản xuất có sẵn mỗi ngày}}{\text{Sản lượng yêu cầu mỗi ngày}}$$

*Giải thích*: để giao đủ sản lượng mục tiêu, mỗi trạm không được mất quá $C$ phút cho mỗi sản phẩm.

**Số trạm làm việc tối thiểu về lý thuyết**:

$$N_{min} = \left\lceil \frac{\sum t_i}{C} \right\rceil$$

Trong đó $\sum t_i$ là tổng thời gian tất cả các công đoạn, làm tròn lên số nguyên (không thể có 2.33 trạm).

**Hiệu suất cân bằng chuyền (Balance Efficiency)**:

$$\text{Efficiency} = \frac{\sum t_i}{N_{actual} \times C} \times 100\%$$

*Giải thích*: tử số là tổng việc thực sự có, mẫu số là tổng "thời gian được trả lương" của tất cả các trạm. Phần còn lại là thời gian nhàn rỗi.

**Ví dụ từng bước** (giả định minh họa: lắp ráp 1 sản phẩm gồm 8 công việc A-H tuần tự, thời gian lần lượt 0.8; 0.6; 0.9; 0.5; 0.7; 1.1; 0.6; 0.4 phút; làm việc 480 phút/ngày, yêu cầu 200 sản phẩm/ngày):

| Bước | Phép tính | Kết quả |
|---|---|---|
| 1 | $\sum t_i = 0.8+0.6+0.9+0.5+0.7+1.1+0.6+0.4$ | 5.6 phút |
| 2 | $C = 480/200$ | 2.4 phút |
| 3 | $N_{min} = \lceil 5.6/2.4 \rceil = \lceil 2.33 \rceil$ | 3 trạm |
| 4 | Cách chia 1 (xếp tham lam, nhồi đầy trạm 1 trước): T1 = A+B+C = 2.3; T2 = D+E+F = 2.3; T3 = G+H = 1.0 | Trạm chậm nhất 2.3 phút |
| 5 | Hiệu suất so với nhịp 2.4: $5.6/(3 \times 2.4)$ | 77.8% |
| 6 | Cách chia 2 (cân hơn): T1 = A+B = 1.4; T2 = C+D+E = 2.1; T3 = F+G+H = 2.1 | Trạm chậm nhất 2.1 phút |
| 7 | Hiệu suất thực: $5.6/(3 \times 2.1)$ | **88.9%** |
| 8 | Sản lượng tối đa/ngày: $480/2.1$ | 228.6 sản phẩm (vượt yêu cầu 200) |

Nếu yêu cầu tăng lên 240 sản phẩm/ngày: $C = 2.0$ phút, $N_{min} = \lceil 5.6/2.0 \rceil = \lceil 2.8 \rceil = 3$ trạm. Nhưng không thể chia 8 việc tuần tự này thành 3 nhóm liên tiếp mà nhóm nào cũng $\le 2.0$ phút, nên phải dùng **4 trạm**: T1 = A+B (1.4), T2 = C+D (1.4), T3 = E+F (1.8), T4 = G+H (1.0), hiệu suất $= 5.6/(4 \times 2.0) = 70\%$. Bài học: $N_{min}$ lý thuyết chỉ là cận dưới, thực tế còn bị ràng buộc bởi thứ tự công việc (precedence) và kích thước từng công việc; muốn đạt hiệu suất cao hơn cần chia nhỏ công việc F (1.1 phút) hoặc dùng thêm công nhân ở trạm đó.

### 2.6. Hoạch định yêu cầu năng lực (Capacity Requirements Planning - CRP)

**Vấn đề**: Sau khi có Lịch sản xuất chính (Master Production Schedule - MPS) và kế hoạch vật tư (MRP), cần kiểm tra xem từng trung tâm làm việc/máy móc có đủ giờ máy, giờ công để thực hiện không. CRP chính là bước "kiểm tra khả thi" đó.

CRP là quá trình xác định chi tiết năng lực cần thiết (theo từng trung tâm làm việc/máy móc) để thực hiện MPS, thường được tính toán tự động trong hệ thống ERP/MRP dựa trên định mức thời gian sản xuất (routing) của từng sản phẩm.

$$\text{Giờ cần tại trung tâm } k = \sum_{j} \left( \text{Số lượng sản phẩm } j \times \text{Định mức giờ/đơn vị tại } k \right)$$

**Ví dụ** (giả định minh họa): tháng tới cần làm 1,000 sản phẩm A (0.30 giờ máy cắt/đv) và 600 sản phẩm B (0.50 giờ máy cắt/đv). Giờ máy cắt cần $= 1{,}000 \times 0.30 + 600 \times 0.50 = 600$ giờ. Nếu máy cắt có 2 máy $\times$ 200 giờ hiệu quả/tháng $= 400$ giờ, thiếu 200 giờ: phải tăng ca, thuê ngoài, hoặc dời đơn hàng. Cũng như TOC, CRP buộc nhà quản lý nhìn vào trung tâm bị quá tải thay vì năng lực trung bình toàn xưởng.

### 2.7. Aggregate Planning có tính toán: so sánh Chase, Level và Mixed

**Vấn đề kinh doanh**: Nhu cầu dao động theo mùa, nhưng nhà xưởng không thể co giãn. Có ba "đòn bẩy" để hấp thụ biến động: (1) thay đổi số nhân công (tuyển/sa thải), (2) thay đổi giờ làm (tăng ca), (3) dùng tồn kho (sản xuất trước, bán sau). Mỗi đòn bẩy có chi phí riêng; Aggregate Planning là bài toán chọn tổ hợp rẻ nhất.

**Ví dụ từng bước** (giả định minh họa: xưởng sản xuất 6 tháng đầu năm, đơn vị sản phẩm quy đổi):

| Tháng | T1 | T2 | T3 | T4 | T5 | T6 | Tổng |
|---|---|---|---|---|---|---|---|
| Nhu cầu (đơn vị) | 400 | 500 | 700 | 900 | 800 | 600 | 3,900 |

Giả định chi phí: sản xuất giờ chuẩn 50,000 VNĐ/đv; sản xuất tăng ca 75,000 VNĐ/đv (tối đa 200 đv tăng ca/tháng); lưu kho 2,000 VNĐ/đv/tháng; tuyển mới 4 triệu VNĐ/người; sa thải 3 triệu VNĐ/người; năng suất 20 đv/người/tháng; hiện có 20 người; tồn kho đầu kỳ 100 đv.

**Phương án 1 - Chase (sản xuất đúng bằng nhu cầu, thay đổi nhân lực)**

| Bước | Tính toán | Kết quả |
|---|---|---|
| 1 | Số người cần mỗi tháng = nhu cầu / 20 | 20, 25, 35, 45, 40, 30 |
| 2 | Tuyển mới (T2: +5, T3: +10, T4: +10) | 25 người x 4 triệu = 100 triệu |
| 3 | Sa thải (T5: -5, T6: -10) | 15 người x 3 triệu = 45 triệu |
| 4 | Chi phí sản xuất: 3,900 x 50,000 | 195 triệu |
| 5 | Tồn kho: giả định không có | 0 |
| **Tổng** | 195 + 100 + 45 | **340 triệu** |

**Phương án 2 - Level (sản xuất đều 650 đv/tháng, dùng tồn kho)**

| Tháng | T1 | T2 | T3 | T4 | T5 | T6 |
|---|---|---|---|---|---|---|
| Sản xuất | 650 | 650 | 650 | 650 | 650 | 650 |
| Tồn kho cuối tháng (= tồn đầu + SX - nhu cầu) | 350 | 500 | 450 | 200 | 50 | 100 |

Chi phí sản xuất 3,900 x 50,000 = 195 triệu; tổng tồn kho-tháng = 350+500+450+200+50+100 = 1,650 đv-tháng, chi phí lưu kho 1,650 x 2,000 = 3.3 triệu. **Tổng = 198.3 triệu.** Tồn kho không âm ở mọi tháng nên kế hoạch khả thi.

**Phương án 3 - Mixed (nền ổn định 600 đv/tháng + tăng ca khi đỉnh)**

| Tháng | T1 | T2 | T3 | T4 | T5 | T6 |
|---|---|---|---|---|---|---|
| Sản xuất chuẩn | 600 | 600 | 600 | 600 | 600 | 600 |
| Tăng ca | 0 | 0 | 0 | 0 | 200 | 0 |
| Tồn kho cuối tháng | 300 | 400 | 300 | 0 | 0 | 0 |

Chi phí: giờ chuẩn 3,600 x 50,000 = 180 triệu; tăng ca 200 x 75,000 = 15 triệu; lưu kho 1,000 đv-tháng x 2,000 = 2 triệu. **Tổng = 197 triệu.**

**Diễn giải**: Chase đắt nhất (340 triệu) vì chi phí tuyển/sa thải chiếm 43% tổng chi phí biến động (145/340) - và chưa tính tổn thất tinh thần, đào tạo lại, đường cong học tập của người mới. Level và Mixed gần như ngang nhau (198.3 so với 197.0 triệu), Mixed linh hoạt hơn vì không bị khóa vào mức tồn kho cao. Kết luận này phụ thuộc vào chi phí lưu kho: nếu hàng dễ hỏng/lỗi thời (thực phẩm tươi, thời trang), chi phí lưu kho cao làm Level kém hấp dẫn, và ngược lại. *Lưu ý*: các chi phí lao động ở trên đã giản lược (tính theo sản lượng, bỏ qua chi phí nhàn rỗi và lương cố định).

### 2.8. Năng lực dự phòng chiến lược (Capacity Cushion)

**Vấn đề**: Vì sao không vận hành 100% công suất cho "hiệu quả"? Phần 2.2 đã cho câu trả lời: thời gian chờ tiến ra vô cực khi $\rho \to 1$. Trong sản xuất cũng vậy: không có đệm thì mọi sự cố, đơn hàng gấp, hay đột biến nhu cầu đều gây trễ hoặc mất khách. Năng lực dự phòng là khoản "bảo hiểm" mua bằng tài sản nhàn rỗi, tương tự tồn kho an toàn (Safety Stock) trong quản trị tồn kho ([04-inventory-management.md](./04-inventory-management.md)).

$$\text{Capacity Cushion} = 100\% - \text{Utilization Rate}$$

Ví dụ: nếu mức sử dụng năng lực 85% thì cushion là 15%.

| Ngành | Tỷ lệ dự phòng năng lực điển hình (tham khảo, ước tính) | Lý do |
|---|---|---|
| Bệnh viện/cấp cứu | 30-40% | Phải sẵn sàng ứng phó ca cấp cứu bất ngờ |
| Sản xuất hàng tiêu dùng ổn định | 10-15% | Nhu cầu dự báo tương đối chính xác |
| Trung tâm dữ liệu (Data Center) | 20-30% | Đảm bảo hiệu suất khi có đợt tải đột biến |
| Ngành thời trang/theo mùa | 25-35% | Biến động nhu cầu cao theo mùa và xu hướng |

**Khi nào cushion lớn hợp lý?** Khi (1) nhu cầu biến động mạnh, (2) hậu quả thiếu năng lực nặng (mạng người, mất khách vĩnh viễn), (3) năng lực khó bổ sung nhanh. **Khi nào nên nhỏ?** Khi nhu cầu ổn định, sản phẩm lưu kho được, hoặc có thể thuê ngoài nhanh. Việc xác định tỷ lệ phù hợp là một quyết định chiến lược cân bằng giữa chi phí nhàn rỗi và rủi ro mất cơ hội.

### 2.9. Sở hữu năng lực vs Thuê ngoài và năng lực linh hoạt (Flexible Capacity & Gig Economy)

**Vấn đề**: Xu hướng hiện đại trong hoạch định năng lực là chuyển từ đầu tư tài sản cố định (fixed asset) sang mô hình năng lực linh hoạt, đặc biệt phổ biến trong logistics và dịch vụ. Về bản chất, đó là cách **chuyển chi phí cố định thành chi phí biến đổi**, giảm rủi ro dự báo sai.

| Mô hình | Mô tả | Ví dụ |
|---|---|---|
| Gig Economy Labor | Thuê lao động tự do theo nhu cầu thời điểm | Grab, ShopeeFood thuê tài xế đối tác thay vì nhân viên cố định |
| Cloud Kitchen | Thuê bếp trung tâm dùng chung, không đầu tư mặt bằng riêng | Các thương hiệu F&B mới ra mắt thử nghiệm thị trường |
| Warehouse-as-a-Service | Thuê không gian kho theo nhu cầu thời điểm (mùa cao điểm) | Amazon FBA, các dịch vụ fulfillment bên thứ ba tại Việt Nam |
| Cloud Computing (IaaS) | Thuê năng lực tính toán theo nhu cầu thay vì đầu tư server | AWS, Google Cloud - mở rộng/thu hẹp năng lực tính toán tức thời |

| Tiêu chí | Sở hữu (Own Capacity) | Thuê ngoài (Outsource/Flexible) |
|---|---|---|
| Chi phí cố định | Cao (đầu tư ban đầu lớn) | Thấp (chuyển thành chi phí biến đổi) |
| Kiểm soát chất lượng | Cao, trực tiếp quản lý | Phụ thuộc năng lực đối tác |
| Tính linh hoạt | Thấp, khó điều chỉnh nhanh | Cao, dễ tăng/giảm theo nhu cầu |
| Phù hợp | Nhu cầu ổn định, dài hạn, chiến lược cốt lõi | Nhu cầu biến động, thời vụ, không phải năng lực cốt lõi |
| Rủi ro | Dư thừa/thiếu hụt khi dự báo sai | Phụ thuộc đối tác, rủi ro nguồn cung dịch vụ |

**Điểm hòa vốn giữa tự làm và thuê ngoài**: nếu tự làm có chi phí cố định $FC_{own}$ và chi phí biến đổi $VC_{own}$, còn thuê ngoài không có chi phí cố định nhưng chi phí biến đổi $VC_{out}$ cao hơn, thì khối lượng hòa vốn là:

$$Q^*_{own/out} = \frac{FC_{own}}{VC_{out} - VC_{own}}$$

**Ví dụ**: $FC_{own} = 480$ triệu/năm, $VC_{own} = 40{,}000$ VNĐ, $VC_{out} = 52{,}000$ VNĐ. Chênh lệch $52{,}000 - 40{,}000 = 12{,}000$ VNĐ/đv. $Q^* = 480{,}000{,}000 / 12{,}000 = 40{,}000$ đơn vị/năm. Cần dự báo nhu cầu bền vững trên 40,000 đv/năm mới nên tự đầu tư; dưới mức đó, thuê ngoài rẻ hơn. Đây chính là phép tính cốt lõi của "Lead hay Lag" đối với SME: khối lượng dự báo càng bất định, thuê ngoài càng đáng giá.

**Hạn chế của thuê ngoài**: chi phí trên mỗi đơn vị thường cao hơn so với đầu tư sở hữu trực tiếp về dài hạn, phụ thuộc vào bên thứ ba nên có rủi ro kiểm soát chất lượng và tính sẵn có.

### 2.10. Cây quyết định và Giá trị kỳ vọng (Decision Tree & EMV/NPV)

**Vấn đề kinh doanh**: Quyết định năng lực là quyết định **dưới bất định**: ta chọn phương án trước khi biết nhu cầu thực. Cây quyết định (Decision Tree) liệt kê các phương án, các kịch bản nhu cầu xảy ra sau đó với xác suất, và lợi ích ở từng nhánh, rồi tính **Giá trị kỳ vọng (Expected Monetary Value - EMV)**. Phương pháp được hệ thống hóa trong lý thuyết quyết định (Howard Raiffa, Harvard, thập niên 1960).

$$EMV = \sum_{i} p_i \times V_i$$

Trong đó $p_i$ là xác suất kịch bản $i$ ($\sum p_i = 1$) và $V_i$ là lợi ích của phương án trong kịch bản đó. Khi dòng tiền kéo dài nhiều năm, $V_i$ phải là giá trị hiện tại ròng (NPV) chứ không phải tổng tiền cộng thẳng (lý do: một đồng hôm nay có giá trị hơn một đồng sau 5 năm, xem [3-financial/01-time-value-of-money.md](../3-financial/01-time-value-of-money.md)).

**Ví dụ minh họa** (giả định minh họa; lợi ích tính bằng triệu VNĐ, đã quy NPV):

| Phương án | Nhu cầu cao (p = 0.4) | Nhu cầu thấp (p = 0.6) | EMV |
|---|---|---|---|
| A. Đầu tư máy mới | +600 | -200 | 0.4 x 600 + 0.6 x (-200) = **120** |
| B. Thuê ngoài | +250 | +50 | 0.4 x 250 + 0.6 x 50 = **130** |

```
                          ┌── Nhu cầu cao (0.4) ──▶ +600
        ┌── A. Đầu tư ────┤
        │                 └── Nhu cầu thấp (0.6) ─▶ -200      EMV(A) = 120
 ───[Quyết định]
        │                 ┌── Nhu cầu cao (0.4) ──▶ +250
        └── B. Thuê ngoài ┤
                          └── Nhu cầu thấp (0.6) ─▶ +50       EMV(B) = 130
```

**Diễn giải**: dù A có tiềm năng lãi lớn nhất (+600), EMV của B lại cao hơn (130 so với 120) và không có kịch bản lỗ. Bài học thường gặp: **EMV không phản ánh rủi ro**. Người ra quyết định phải xem thêm kịch bản xấu nhất và khả năng chịu lỗ của doanh nghiệp. Case 7 trong mục III dùng chính công cụ này, mở rộng thêm khái niệm **quyền chọn chờ đợi (option to wait)**: trả giá nhỏ để có thêm thông tin trước khi cam kết vốn lớn.

### 2.11. Mô phỏng Monte Carlo trong hoạch định năng lực dưới điều kiện bất định

**Vấn đề**: Cây quyết định chỉ có vài kịch bản rời rạc (cao/trung/thấp). Thực tế nhu cầu có thể là bất kỳ giá trị nào trong một khoảng. Mô phỏng Monte Carlo (đặt tên theo sòng bạc Monte Carlo; do Ulam, von Neumann, Metropolis phát triển trong dự án Manhattan, thập niên 1940) chạy hàng nghìn kịch bản ngẫu nhiên rút từ phân phối xác suất của các biến đầu vào, từ đó cho ra **phân phối** kết quả (không chỉ một con số trung bình).

**Quy trình cơ bản**:
1. Xác định các biến bất định chính (nhu cầu, giá, chi phí vận hành) và phân phối xác suất của chúng (thường dùng phân phối tam giác: giá trị thấp nhất, khả dĩ nhất, cao nhất, vì dễ ước lượng từ kinh nghiệm).
2. Chạy mô phỏng hàng nghìn lần với các giá trị ngẫu nhiên rút từ phân phối đã xác định.
3. Tổng hợp kết quả thành phân phối xác suất của lợi nhuận/ROI cho mỗi phương án đầu tư.
4. So sánh xác suất đạt mục tiêu tài chính (ví dụ P(NPV < 0)) giữa các phương án để ra quyết định.

Phương pháp này phổ biến trong các doanh nghiệp lớn khi quyết định đầu tư nhà máy mới, mở rộng dây chuyền quy mô lớn, nơi sai lầm dự báo có thể gây thiệt hại hàng trăm tỷ đồng. SME có thể làm bằng Excel/Google Sheets (xem mục 5.4). Kết quả minh họa cho một SME nằm ở Case 7.

### 2.12. Hoạch định năng lực và tính bền vững (Sustainability)

Xu hướng ESG cũng ảnh hưởng đến quyết định hoạch định năng lực hiện đại:

- **Hiệu quả năng lượng**: đầu tư máy móc mới cần cân nhắc mức tiêu thụ năng lượng/đơn vị sản phẩm, không chỉ công suất tối đa.
- **Khả năng tái sử dụng/tái cấu hình**: thiết kế dây chuyền có thể điều chỉnh linh hoạt giữa các dòng sản phẩm khác nhau (flexible manufacturing system) giúp giảm lãng phí đầu tư khi nhu cầu sản phẩm thay đổi.
- **Quy mô tối thiểu hiệu quả (Minimum Efficient Scale)**: cân nhắc quy mô đầu tư đủ lớn để đạt hiệu quả kinh tế theo quy mô (economies of scale) nhưng không quá lớn gây lãng phí tài nguyên nếu nhu cầu không đạt kỳ vọng.

### 2.13. Ưu điểm và nhược điểm của các chiến lược hoạch định năng lực

#### 2.13.1. Bảng so sánh theo góc độ tài chính

| Tiêu chí tài chính | Lead Strategy | Lag Strategy | Match Strategy |
|---|---|---|---|
| Dòng tiền đầu tư ban đầu (CAPEX) | Lớn, trả trước | Nhỏ, trả dần theo nhu cầu | Trung bình, theo giai đoạn |
| Rủi ro tài sản không sử dụng hết (Idle Asset Risk) | Cao | Thấp | Trung bình |
| Chi phí cơ hội (Opportunity Cost) nếu thiếu năng lực | Thấp (hiếm khi thiếu) | Cao (thường xuyên thiếu giai đoạn đầu) | Trung bình |
| Độ nhạy với sai số dự báo | Cao (thiệt hại lớn nếu dự báo sai) | Thấp (ít đầu tư trước) | Trung bình |
| Phù hợp với cấu trúc vốn | Doanh nghiệp có vốn dồi dào, khả năng chịu rủi ro cao | Doanh nghiệp hạn chế vốn, ưu tiên an toàn | Đa số doanh nghiệp có quy mô vừa và tăng trưởng ổn định |

Ưu/nhược điểm cốt lõi của Lead/Lag/Match đã được nêu ở bảng mục 1.4 và của Chase/Level/Mixed ở mục 1.5, nên không lặp lại ở đây.

#### 2.13.2. So sánh theo ngành: Sản xuất vs Dịch vụ

| Khía cạnh | Ngành Sản xuất (Manufacturing) | Ngành Dịch vụ (Service) |
|---|---|---|
| Khả năng lưu trữ năng lực dư | Có (qua tồn kho thành phẩm) | Không (dịch vụ không lưu trữ được) |
| Công cụ chính | Line Balancing, Aggregate Planning | Queuing Theory, lịch làm việc linh hoạt |
| Rủi ro chính | Tồn kho dư thừa nếu dự báo sai | Thời gian chờ đợi khách hàng tăng vọt |
| Ví dụ điều chỉnh năng lực | Tăng ca, thuê thêm máy móc | Thuê nhân viên bán thời gian giờ cao điểm |

---

## III. Case Studies thực tế

> Nguyên tắc đọc: mỗi case dưới đây đi từ bối cảnh, đến số liệu, đến từng bước tính, đến diễn giải và bài học. Với các công ty thật, phần định tính dựa trên thông tin công khai; mọi con số tính toán là "giả định minh họa" do tác giả thiết kế để làm rõ phương pháp, không phải số liệu thực của doanh nghiệp.

### 1. Case quốc tế thành công: Amazon - Hoạch định năng lực kho vận mùa cao điểm

#### Case 1.1 - Bối cảnh
Amazon phải đối mặt với nhu cầu tăng đột biến (theo mô tả công khai, nhiều lần so với các tháng thường) vào mùa mua sắm cuối năm (Black Friday, Cyber Monday, Giáng sinh). Vấn đề: lượng đơn tăng nhiều lần chỉ trong vài tuần, nhưng nhà kho, robot và đội ngũ không thể co giãn tức thời.

#### Case 1.2 - Chiến lược áp dụng (theo mô tả công khai)
Amazon kết hợp Lead Strategy (xây trước các trung tâm fulfillment mới nhiều tháng trước mùa cao điểm) với Chase Strategy cho lao động (tuyển lao động thời vụ ngắn hạn trong 2-3 tháng cao điểm), đồng thời đầu tư tự động hóa bằng robot (hệ thống Kiva, mua lại năm 2012) để tăng năng lực xử lý mà không phụ thuộc hoàn toàn vào lao động.

#### Case 1.3 - Mô hình tính toán minh họa (trung tâm giả định, KHÔNG phải số liệu Amazon)
Giả định một trung tâm fulfillment: ngày thường 100,000 đơn/ngày; cao điểm gấp 5 lần = 500,000 đơn/ngày kéo dài 90 ngày; mỗi nhân viên xử lý 100 đơn/ngày; lương 500,000 VNĐ/ngày; lao động thời vụ 550,000 VNĐ/ngày kèm 3 triệu VNĐ chi phí tuyển và đào tạo mỗi người.

| Bước | Phép tính | Kết quả |
|---|---|---|
| 1 | Nhân sự ngày thường = 100,000 / 100 | 1,000 người |
| 2 | Nhân sự cao điểm = 500,000 / 100 | 5,000 người |
| 3 | Nhân sự cần thêm | 4,000 người |
| 4a | **Level** (thuê cố định cả năm, 275 ngày thấp điểm bị nhàn rỗi): 4,000 x 500,000 x 275 | **550 tỷ VNĐ** chi phí nhàn rỗi |
| 4b | **Chase** (thuê thời vụ 90 ngày): 4,000 x (550,000 x 90 + 3,000,000) = 4,000 x 52,500,000 | **210 tỷ VNĐ** |
| 5 | **Chase + robot** (năng suất tăng lên 160 đơn/người/ngày): nhân sự cao điểm 500,000/160 = 3,125; ngày thường 100,000/160 = 625; cần thêm 2,500 người; chi phí 2,500 x 52,500,000 | **131.25 tỷ VNĐ** |
| 6 | Tiết kiệm mỗi mùa nhờ robot = 210 - 131.25 | **78.75 tỷ VNĐ** |

#### Case 1.4 - Diễn giải kinh doanh
- Level (giữ đội ngũ đủ cho đỉnh cả năm) đắt gấp 2.6 lần Chase (550/210) vì phải trả lương cho người nhàn rỗi 275 ngày. Chase hợp lý khi lao động thời vụ sẵn có và đào tạo nhanh.
- Chase vẫn có chi phí ẩn: chất lượng, an toàn lao động, đào tạo (đường cong học tập, mục 2.4). Vì vậy Amazon bổ sung tự động hóa để tăng năng suất mỗi người, thu hẹp chênh lệch giữa đỉnh và đáy.
- Robot là khoản đầu tư năng lực cố định: chỉ đáng khi khoản tiết kiệm mỗi mùa (78.75 tỷ trong mô hình giả định) bù được chi phí đầu tư trong vài mùa.

#### Case 1.5 - Bài học
Không có chiến lược "thuần" cho nhu cầu cực đoan: phải **kết hợp** đầu tư dài hạn (Lead: nền tảng cố định, tự động hóa) với năng lực linh hoạt (Chase: lao động thời vụ). SME có thể học theo tinh thần đó ở quy mô nhỏ: thuê gói thầu fulfillment ngoài vào mùa cao điểm.

### 2. Case Việt Nam lớn: Highlands Coffee - Cân bằng năng lực chuỗi cửa hàng

#### Case 2.1 - Bối cảnh
Highlands Coffee vận hành hàng trăm cửa hàng với nhu cầu biến động mạnh theo giờ (cao điểm sáng 7-9h, trưa 11-13h, chiều tối 17-19h). Về định tính: chuỗi dùng dữ liệu lượng khách theo khung giờ để xếp ca linh hoạt (shift scheduling), tránh để khách chờ quá lâu giờ cao điểm nhưng không thừa người giờ thấp điểm. Phần tính toán dưới đây là mô hình giả định cho một cửa hàng minh họa, không phải dữ liệu nội bộ của Highlands.

#### Case 2.2 - Số liệu giả định
Cửa hàng mở 16 giờ/ngày (6 giờ cao điểm + 10 giờ thấp điểm). Cao điểm: $\lambda = 120$ khách/giờ; thấp điểm: $\lambda = 45$ khách/giờ. Mỗi nhân viên pha chế phục vụ $\mu = 30$ khách/giờ. Chi phí nhân viên 30,000 VNĐ/giờ. Mục tiêu dịch vụ: thời gian chờ $W_q \le 1$ phút.

#### Case 2.3 - Từng bước tính toán (dùng công thức Erlang C, mục 2.3)

| Khung giờ | $\lambda$ | Số nhân viên $c$ | $\rho$ | $P_w$ | $W_q$ (phút) | Đạt mục tiêu? |
|---|---|---|---|---|---|---|
| Cao điểm | 120 | 4 | 100% | - | vô hạn | Không (sụp đổ) |
| Cao điểm | 120 | 5 | 80.0% | 55.4% | 1.11 | Không (vừa vượt 1 phút) |
| Cao điểm | 120 | 6 | 66.7% | 28.5% | 0.28 | Có |
| Thấp điểm | 45 | 2 | 75.0% | 64.3% | 2.57 | Không |
| Thấp điểm | 45 | 3 | 50.0% | 23.7% | 0.32 | Có |
| Thấp điểm | 45 | 4 | 37.5% | 7.5% | 0.06 | Có nhưng dư |

Lịch tối ưu: **6 nhân viên** giờ cao điểm, **3 nhân viên** giờ thấp điểm.

| So sánh chi phí | Giờ công/ngày | Chi phí/ngày |
|---|---|---|
| Lịch cố định 6 người cả ngày: 6 x 16 | 96 giờ | 2,880,000 VNĐ |
| Lịch linh hoạt: 6 x 6 + 3 x 10 | 66 giờ | 1,980,000 VNĐ |
| Tiết kiệm: 96 - 66 = 30 giờ x 30,000 | 30 giờ | **900,000 VNĐ/ngày**, tức 328.5 triệu VNĐ/năm cho một cửa hàng |

#### Case 2.4 - Diễn giải kinh doanh
- Lịch cố định 4 người (rẻ nhất, 64 giờ) thất bại ở cao điểm vì $\rho = 1$; không có năng lực dư để xả hàng đợi.
- Lịch linh hoạt giữ cùng chất lượng dịch vụ như lịch "6 người cố định" nhưng giảm 31% giờ công (30/96).
- Nhân với số cửa hàng, khoản tiết kiệm có ý nghĩa chiến lược. Nhưng cần cân nhắc: ca ngắn và chia nhỏ ảnh hưởng đến tuyển dụng và giữ chân nhân viên (nhiều người cần thu nhập ổn định).

#### Case 2.5 - Bài học
Với dịch vụ không lưu kho được, đồ thị nhu cầu theo giờ chính là đầu vào của bài toán năng lực. Quy trình chuẩn: đo $\lambda$ theo khung giờ, đặt mục tiêu chờ, dùng Erlang C để tìm $c$ nhỏ nhất đạt mục tiêu cho từng khung.

### 3. Case SME Việt Nam: Xưởng may gia công Bình Dương mở rộng năng lực

> Toàn bộ số liệu trong case này là giả định minh họa. (Bản gốc của file mô tả đơn hàng "gấp 3 lần năng lực"; để các con số tự nhất quán, case được viết lại với đơn hàng gấp 2 lần năng lực hiện tại, tức cần thêm 100% năng lực.)

#### Case 3.1 - Bối cảnh
Xưởng may 150 công nhân, năng suất 10 áo/người/ngày, tức năng lực **1,500 áo/ngày** (làm việc 26 ngày/tháng). Khách hàng xuất khẩu đặt đơn **3,000 áo/ngày** trong 4 tháng đầu, và phía khách đưa ra khả năng ký tiếp hợp đồng định kỳ 24 tháng nếu chất lượng tốt (chưa ký, xác suất chưa rõ). Chủ xưởng phân vân giữa đầu tư dài hạn và giải pháp ngắn hạn.

#### Case 3.2 - Số liệu giả định

| Hạng mục | Giá trị |
|---|---|
| Giá nhận gia công P | 50,000 VNĐ/áo |
| Chi phí biến đổi tự may (VC in-house) | 40,000 VNĐ/áo, lợi nhuận góp 10,000 |
| Chi phí giao thầu phụ (VC outsource) | 48,000 VNĐ/áo, lợi nhuận góp 2,000 |
| Đầu tư cho 60 công nhân + 60 máy + thiết bị | 2,000 triệu VNĐ; bán lại sau cùng 40% |
| Chi phí cố định tăng thêm (quản lý chuyền, điện, bảo trì...) | 50 triệu/tháng |
| Tỷ suất chiết khấu | 1%/tháng |

#### Case 3.3 - Từng bước tính toán

**Bước 1 - Khoảng cách năng lực**: nhu cầu 3,000 - năng lực 1,500 = 1,500 áo/ngày thiếu = 39,000 áo/tháng (x 26 ngày).

**Bước 2 - Ba phương án**:
- **X**: giao thầu phụ toàn bộ 1,500 áo/ngày (không đầu tư).
- **Y (xưởng chọn)**: tự may 40% (600 áo/ngày = 15,600 áo/tháng, cần thêm 60 công nhân vì 600/10 = 60) + giao thầu phụ 60% (900 áo/ngày = 23,400 áo/tháng).
- **Z**: tự may toàn bộ 1,500 áo/ngày: thêm 150 công nhân, đầu tư 5,000 triệu, chi phí cố định 125 triệu/tháng.

**Bước 3 - Lợi nhuận hàng tháng**:

| Phương án | Công thức | Lợi nhuận/tháng |
|---|---|---|
| X | 39,000 áo x 2,000 | 78.0 triệu |
| Y (tự may) | 15,600 x 10,000 - 50 triệu = 156 - 50 | 106.0 triệu |
| Y (thầu phụ) | 23,400 x 2,000 | 46.8 triệu |
| **Y tổng** | 106.0 + 46.8 | **152.8 triệu** |
| Z | 39,000 x 10,000 - 125 triệu = 390 - 125 | 265.0 triệu |

**Bước 4 - Điểm hòa vốn riêng cho phần tự may của Y**: $Q^* = 50{,}000{,}000 / 10{,}000 = 5{,}000$ áo/tháng, tức 192 áo/ngày, bằng 32% năng lực 15,600 áo/tháng. Hòa vốn hoạt động thấp, nhưng điều đó chưa hoàn vốn đầu tư 2 tỷ. Hoàn vốn giản đơn nếu chỉ tính phần tự may: $2{,}000 / 106 = 18.9$ tháng (khớp với kỳ vọng "khoảng 18 tháng" của bản gốc).

**Bước 5 - So sánh giá trị hiện tại ròng theo thời gian kéo dài đơn hàng** (triệu VNĐ; NPV = dòng tiền hàng tháng chiết khấu 1%/tháng - đầu tư + 40% giá trị thu hồi chiết khấu về hiện tại):

| Thời gian đơn hàng kéo dài | X (thầu phụ) | Y (hỗn hợp) | Z (tự may hết) |
|---|---|---|---|
| 4 tháng (đơn một lần) | **304.4** | -635.0 | -2,044.0 |
| 12 tháng | **877.9** | 429.7 | -242.5 |
| 24 tháng | 1,657.0 | 1,876.0 | **2,204.6** |
| 36 tháng | 2,348.4 | 3,159.6 | **4,376.3** |
| 48 tháng | 2,962.0 | 4,298.6 | **6,303.6** |

Điểm giao: Y vượt X từ tháng thứ 20; Z vượt Y từ tháng thứ 20.

#### Case 3.4 - Diễn giải kinh doanh
1. Nếu đơn hàng chỉ kéo dài 4 tháng, giao thầu phụ toàn bộ (X) thắng rõ: đầu tư máy móc bị lỗ -635 triệu vì chưa kịp thu hồi vốn. Đây chính là lý do "chỉ dựa vào đơn lớn một lần để mua máy" là sai lầm kinh điển.
2. Nếu đơn hàng kéo dài từ 20 tháng trở lên, có tài sản tự sở hữu thắng, vì lợi nhuận góp tự may (10,000/áo) gấp 5 lần thầu phụ (2,000/áo).
3. Z thắng Y về lâu dài, nhưng cần 5 tỷ, vượt khả năng huy động của xưởng (giả định chỉ vay được tối đa khoảng 2-2.5 tỷ). Y là phương án nằm trong giới hạn vốn, và cũng là **Match Strategy**: đầu tư một phần, linh hoạt phần còn lại.
4. Với hợp đồng 24 tháng, lợi thế của Y so với X chỉ là 219 triệu (1,876.0 - 1,657.0), tương đối mỏng. Vì vậy quyết định phụ thuộc vào độ chắc chắn của hợp đồng định kỳ; nên yêu cầu khách cam kết tối thiểu (take-or-pay) hoặc đặt cọc trước khi đầu tư.

#### Case 3.5 - Bài học và khuyến nghị
- Quyết định giữa tự đầu tư và thuê ngoài phải dựa trên **thời gian kéo dài của nhu cầu**, không phải quy mô đơn hàng. Điểm quyết định ở đây là 20 tháng.
- Đàm phán cam kết dài hạn trước khi đầu tư (giảm rủi ro Lead).
- Theo dõi kỹ năng chất lượng của thầu phụ (rủi ro giao trễ, lỗi), vì bản chất thầu phụ là chuyển chi phí cố định sang biến đổi nhưng không chuyển được trách nhiệm với khách hàng cuối.
- Theo dõi đường cong học tập: 60 công nhân mới sẽ không đạt 10 áo/người/ngày ngay từ tháng đầu (mục 2.4); kế hoạch nên giả định ramp-up 2-3 tháng.

### 4. Case quốc tế thất bại: Ngành hàng không mở rộng năng lực trước khủng hoảng COVID-19

#### Case 4.1 - Bối cảnh
Nhiều hãng hàng không quốc tế đầu tư mở rộng đội bay và năng lực vận chuyển mạnh mẽ trong giai đoạn 2015-2019 dựa trên dự báo tăng trưởng liên tục của ngành du lịch. Đại dịch COVID-19 năm 2020 khiến nhu cầu di chuyển hàng không sụt giảm đột ngột (theo nhiều báo cáo công khai, mức giảm lên tới hơn 90% ở thời điểm thấp nhất), trong khi các hãng đã cam kết hợp đồng thuê/mua máy bay dài hạn (Lead Strategy), dẫn đến dư thừa năng lực lớn; nhiều hãng phải tuyên bố phá sản hoặc nhận cứu trợ chính phủ.

#### Case 4.2 - Mô hình tính toán minh họa (hãng giả định, đơn vị tương đối, KHÔNG phải số liệu một hãng cụ thể)
Giả định doanh thu bình thường = 1,000 đơn vị; chi phí cố định (thuê/khấu hao máy bay, bảo hiểm, lương cố định) = 400; chi phí biến đổi theo chuyến bay (nhiên liệu, phí sân bay, phục vụ) = 450. Lợi nhuận bình thường = 1,000 - 400 - 450 = **150**.

| Bước | Tình huống | Phép tính | Kết quả |
|---|---|---|---|
| 1 | Nhu cầu giảm 90%, cắt chuyến tương ứng: doanh thu 100, chi phí biến đổi 45 | 100 - 400 - 45 | **-345** (lỗ) |
| 2 | Doanh thu hòa vốn của cấu trúc chi phí gốc: tỷ lệ chi phí biến đổi 450/1,000 = 0.45; $400/(1-0.45)$ | 727.3, tức 72.7% doanh thu bình thường | Chỉ cần mất hơn 27% nhu cầu là lỗ |
| 3 | Cấu trúc linh hoạt hơn: chia 400 chi phí cố định thành 200 cố định thật + 200 cắt giảm được (hợp đồng thuê linh hoạt, lương theo chuyến). Lợi nhuận bình thường vẫn 1,000 - 200 - 200 - 450 = 150 | - | 150 |
| 4 | Nhu cầu giảm 90% với cấu trúc linh hoạt: chi phí linh hoạt cắt còn 20 | 100 - 45 - 20 - 200 | **-165** |
| 5 | Doanh thu hòa vốn cấu trúc linh hoạt: $200/(1 - 0.45 - 0.20) = 200/0.35$ | 571.4, tức 57.1% doanh thu bình thường | Chịu được mất đến 43% nhu cầu |

#### Case 4.3 - Diễn giải kinh doanh
Cùng một mức sụt giảm nhu cầu 90%, hãng có cấu trúc linh hoạt lỗ chỉ bằng 48% hãng cứng (165/345), và điểm hòa vốn giảm từ 72.7% xuống 57.1% doanh thu bình thường. Đòn bẩy hoạt động (operating leverage) cao (chi phí cố định lớn) khuếch đại cả lãi lẫn lỗ: đó là điểm cốt lõi của Lead Strategy với tài sản đắt, khó đảo ngược.

#### Case 4.4 - Bài học
Chiến lược Lead đầu tư dựa trên dự báo dài hạn có rủi ro rất lớn với các sự kiện gián đoạn (black swan). Các mô hình hoạch định năng lực hiện đại khuyến nghị: xây dựng kịch bản (scenario planning, xem [1-strategic/07-scenario-planning.md](../1-strategic/07-scenario-planning.md)), kiểm tra độ chịu đựng (stress test) điểm hòa vốn, và duy trì tính linh hoạt trong hợp đồng dài hạn (điều khoản hủy/hoãn, thuê ngắn hạn).

### 5. Case Việt Nam SME - dịch vụ: Phòng khám tư nhân mở rộng năng lực khám bệnh

> Số liệu giả định minh họa.

#### Case 5.1 - Bối cảnh
Một phòng khám đa khoa tư nhân tại TP.HCM có lượng bệnh nhân tăng trưởng ổn định 20%/năm, thường xuyên quá tải vào cuối tuần, bệnh nhân phải chờ 2-3 giờ. Phòng khám cân nhắc mở rộng cơ sở vật chất (Lead, tốn kém) hay giải pháp rẻ hơn.

#### Case 5.2 - Số liệu giả định
Khung khám sáng cuối tuần 8 giờ; mỗi bác sĩ khám 6 bệnh nhân/giờ ($\mu = 6$, tức 10 phút/ca); đang có 3 bác sĩ; bệnh nhân đến trung bình $\lambda = 22$ người/giờ (đa phần đến không hẹn, dồn vào buổi sáng).

#### Case 5.3 - Từng bước tính toán

| Bước | Phép tính | Kết quả |
|---|---|---|
| 1 | Năng lực phục vụ: $3 \times 6$ | 18 bệnh nhân/giờ |
| 2 | Hệ số sử dụng: $\rho = 22/18$ | 1.22 (> 1: không ổn định) |
| 3 | Bệnh nhân tồn lại mỗi giờ: $22 - 18$ | 4 người/giờ |
| 4 | Sau 8 giờ: $4 \times 8$ | 32 bệnh nhân còn trong hàng |
| 5 | Thời gian chờ của người đến cuối: $32/18$ | 1.78 giờ (khoảng 107 phút) |

Kết quả khớp với trải nghiệm thực tế "chờ 2-3 giờ" (cộng thêm thời gian khám và thủ tục).

**Giải pháp 1 - Thêm bác sĩ bán thời gian cuối tuần ($c = 4$)**: $\rho = 22/24 = 91.7\%$; xác suất phải chờ $P_w = 82.2\%$; $W_q = 24.7$ phút. Ổn định nhưng chờ vẫn lâu.

**Giải pháp 2 - Thêm hệ thống đặt lịch hẹn** để dời bớt bệnh nhân sang khung giờ ít người: giả định giảm $\lambda$ đỉnh từ 22 xuống 18 người/giờ.
- Với $c = 4$: $\rho = 18/24 = 75\%$; $P_w = 50.9\%$; $W_q = 5.1$ phút.

| Phương án | $c$ | $\lambda$ | $\rho$ | $W_q$ |
|---|---|---|---|---|
| Hiện tại | 3 | 22 | 122% | không ổn định (~1.8 giờ cuối buổi) |
| Thêm bác sĩ | 4 | 22 | 91.7% | 24.7 phút |
| Thêm bác sĩ + đặt lịch | 4 | 18 | 75.0% | 5.1 phút |
| Mở rộng cơ sở (Lead): nâng lên 5 phòng khám/bác sĩ | 5 | 22 | 73.3% | 3.2 phút |

#### Case 5.4 - Diễn giải kinh doanh
- Chiến lược Match (thuê bác sĩ bán thời gian đúng giờ cao điểm + đặt lịch) giảm thời gian chờ từ khoảng 1.8 giờ xuống dưới 10 phút (kết quả thực tế thấp hơn mô hình vì còn thời gian đăng ký, thanh toán), mà không cần đầu tư xây thêm phòng khám.
- Mở rộng cơ sở (c = 5) chỉ cải thiện thêm khoảng 2 phút so với phương án kết hợp nhưng phải bỏ vốn lớn. Công nghệ đặt lịch đóng vai trò "điều tiết nhu cầu" thay thế một phần năng lực vật lý.
- Tuy nhiên với tăng trưởng 20%/năm, $\lambda$ sẽ tăng: sau 2 năm $\lambda \approx 18 \times 1.44 = 25.9$ (vượt 24 = năng lực $c=4$). Đây là tín hiệu cần chuẩn bị bước tăng năng lực tiếp theo, không nên đợi đến khi quá tải rồi mới hành động.

#### Case 5.5 - Bài học
Trước khi đầu tư năng lực vật lý, hãy xem có thể **điều tiết nhu cầu** (đặt lịch, giá khác theo khung giờ) hoặc **mua năng lực linh hoạt** (nhân sự bán thời gian) trước không. Và dùng $\rho$ để phát hiện hệ thống "sắp vỡ" từ trước: khi $\rho$ vượt 85% là lúc cần hành động.

### 6. Case bổ sung: FPT Software - Hoạch định năng lực nhân sự công nghệ

> Phần định tính dựa trên mô tả chung về mô hình dịch vụ phần mềm; số liệu định lượng là giả định minh họa, không phải số liệu nội bộ của FPT Software.

#### Case 6.1 - Bối cảnh
FPT Software là doanh nghiệp gia công phần mềm lớn tại Việt Nam; "năng lực" cốt lõi chính là đội ngũ kỹ sư, khác với năng lực máy móc. Nhu cầu dự án của khách hàng quốc tế biến động liên tục: một dự án lớn có thể cần huy động hàng trăm kỹ sư trong vài tháng, trong khi tuyển và đào tạo kỹ sư mới đạt năng lực đầy đủ mất nhiều tháng (đường cong học tập kéo dài).

#### Case 6.2 - Giải pháp áp dụng (mô tả định tính)
- Xây dựng "bench" (nhân sự dự phòng chưa phân bổ dự án) làm vùng đệm năng lực, tương tự Safety Stock trong quản trị tồn kho.
- Đào tạo nội bộ liên tục (FPT University, FPT Academy) để rút ngắn đường cong học tập.
- Hợp tác mạng lưới đối tác/freelancer xử lý đợt tăng đột biến ngắn hạn (mô hình gig economy, mục 2.9).
- Dự báo nhu cầu nhân sự dựa trên pipeline hợp đồng và xác suất chốt hợp đồng.

#### Case 6.3 - Mô hình tính toán minh họa (giả định)
Giả định tổng 6,000 kỹ sư; chi phí trung bình 25 triệu VNĐ/kỹ sư/tháng; mục tiêu tỷ lệ sử dụng (utilization rate) 82%.

| Bước | Phép tính | Kết quả |
|---|---|---|
| 1 | Kỹ sư tính được tiền (billable): $6{,}000 \times 82\%$ | 4,920 người |
| 2 | Bench: $6{,}000 \times 18\%$ (cushion = 100% - 82%) | 1,080 người |
| 3 | Mỗi 1 điểm % utilization tăng thêm = 60 người chuyển từ bench sang billable | 60 người |
| 4 | Chi phí bench tương ứng: $60 \times 25$ triệu $\times$ 12 tháng | 18 tỷ VNĐ/năm |

#### Case 6.4 - Diễn giải kinh doanh
Bench 18% có vẻ "lãng phí" nhưng chính là khoản bảo hiểm để nhận được dự án gấp mà không phải tuyển ồ ạt (và đào tạo kéo dài). Mỗi điểm % utilization được cải thiện (ví dụ bằng đào tạo chéo để bench có thể điều sang nhiều loại dự án) tiết kiệm 18 tỷ VNĐ/năm trong mô hình này; nhưng đẩy utilization quá cao (ví dụ trên 90%) sẽ không còn khả năng đáp ứng dự án gấp và dễ kiệt sức nhân sự.

#### Case 6.5 - Bài học
Với dịch vụ tri thức, "tài sản" là con người; cushion, đào tạo (rút ngắn đường cong học tập) và mạng lưới đối tác (năng lực linh hoạt) là ba đòn bẩy tương ứng với tồn kho an toàn, ramp-up và thuê ngoài trong sản xuất.

### 7. Case SME Việt Nam mới: Cà phê rang xay "Đất Đỏ" - Hoạch định năng lực rang xay

> **Toàn bộ nhân vật, tên doanh nghiệp và số liệu trong case này là GIẢ ĐỊNH MINH HỌA** do tác giả thiết kế để thực hành toàn bộ chuỗi kỹ thuật của bài (đo năng lực, nút thắt, khoảng cách, break-even, cây quyết định, Monte Carlo). Mọi con số đã được kiểm tra lại bằng tính toán.

#### Case 7.1 - Bối cảnh
"Cà phê Đất Đỏ" là xưởng rang xay đóng gói cà phê bột quy mô nhỏ tại Đắk Lắk, bán sỉ cho quán và đại lý, đang nhận lời mời từ một chuỗi quán ở TP.HCM đặt hàng thêm. Chủ xưởng đứng trước đề nghị mua thêm một máy rang mới. Xưởng làm việc 1 ca/ngày, 8 giờ, 26 ngày/tháng. Sản lượng thực tế hiện tại 7,000 kg/tháng.

#### Case 7.2 - Số liệu đầu vào (giả định minh họa)

| Công đoạn | Năng lực (kg/giờ) |
|---|---|
| 1. Sàng, phân loại nhân xanh | 120 |
| 2. Rang | 45 |
| 3. Xay | 90 |
| 4. Đóng gói | 60 |
| 5. Dán nhãn, đóng thùng | 100 |

Giá bán trung bình 220,000 VNĐ/kg; chi phí biến đổi 180,000 VNĐ/kg (lợi nhuận góp 40,000 VNĐ/kg, đã quy đổi để dùng trong mô hình). Năng lực hiệu quả bằng 85% năng lực thiết kế (do bảo trì, vệ sinh, đổi mẻ). Máy rang mới: công suất 20 kg/giờ, vốn đầu tư 480 triệu VNĐ, khấu hao 5 năm, chi phí cố định hoạt động thêm 90 triệu/năm (nhân công, điện, bảo trì). Tỷ suất chiết khấu 12%/năm, thời hạn phân tích 5 năm.

Dự báo nhu cầu 12 tháng tới (kg/tháng), ba kịch bản: Cao 10,000 (xác suất 0.3); Trung bình 8,800 (0.5); Thấp 7,500 (0.2).

#### Case 7.3 - Bước 1 - Đo năng lực hiện tại và tìm nút thắt

| Công đoạn | kg/giờ | Năng lực thiết kế kg/tháng ($\times 8 \times 26 = 208$ giờ) |
|---|---|---|
| Sàng | 120 | 24,960 |
| **Rang** | **45** | **9,360 (nút thắt)** |
| Xay | 90 | 18,720 |
| Đóng gói | 60 | 12,480 |
| Dán nhãn | 100 | 20,800 |

- Năng lực thiết kế hệ thống = công đoạn thấp nhất = 9,360 kg/tháng.
- Năng lực hiệu quả = $9{,}360 \times 85\% = 7{,}956$ kg/tháng.
- Hiệu suất = $7{,}000 / 7{,}956 = 88.0\%$; Mức sử dụng = $7{,}000 / 9{,}360 = 74.8\%$.

Diễn giải: xưởng đang vận hành khá tốt (hiệu suất 88%) và chỉ còn dư khoảng 956 kg/tháng ở mức hiệu quả (7,956 - 7,000). Chỉ cần nhu cầu tăng 14% là hết chỗ. Không nên đầu tư thêm vào sàng, xay hay dán nhãn vì chúng còn dư năng lực 2-3 lần.

#### Case 7.4 - Bước 2 - Khoảng cách năng lực theo kịch bản

| Kịch bản | Nhu cầu (kg/tháng) | Năng lực hiệu quả hiện tại | Phần thiếu (kg/tháng) |
|---|---|---|---|
| Cao (0.3) | 10,000 | 7,956 | 2,044 |
| Trung bình (0.5) | 8,800 | 7,956 | 844 |
| Thấp (0.2) | 7,500 | 7,956 | 0 (đủ năng lực) |

#### Case 7.5 - Bước 3 - Nút thắt dịch chuyển khi thêm máy rang
Thêm máy rang 20 kg/giờ: công đoạn rang thành $45 + 20 = 65$ kg/giờ (13,520 kg/tháng). Nút thắt mới là **đóng gói** (60 kg/giờ). Năng lực thiết kế hệ thống tăng từ 9,360 lên $60 \times 208 = 12{,}480$ kg/tháng (tăng 33%, không phải 44% như phép cộng rang cho thấy); năng lực hiệu quả mới $= 12{,}480 \times 85\% = 10{,}608$ kg/tháng. Nghĩa là máy rang mới chỉ phát huy tối đa nếu đóng gói không bị nghẽn; nhu cầu Cao (10,000) vẫn nằm trong 10,608, nên không cần mua thêm máy đóng gói ngay, nhưng đã gần chạm trần mới.

Như vậy phần bán thêm được tối đa nhờ máy mới (kg/tháng): Cao: $\min(10{,}000; 10{,}608) - 7{,}956 = 2{,}044$; Trung bình: 844; Thấp: 0.

#### Case 7.6 - Bước 4 - Điểm hòa vốn của máy rang mới

| Chỉ số | Công thức | Kết quả |
|---|---|---|
| Khấu hao/năm | 480 / 5 | 96 triệu |
| Chi phí cố định kế toán/năm | 90 + 96 | 186 triệu |
| Sản lượng hòa vốn kế toán | 186,000,000 / 40,000 | 4,650 kg/năm = 387.5 kg/tháng |
| Sản lượng hòa vốn tiền mặt (không khấu hao) | 90,000,000 / 40,000 | 2,250 kg/năm |

So với phần bán thêm: kịch bản Trung bình bán thêm 844 x 12 = 10,128 kg/năm, gấp 2.2 lần mức hòa vốn kế toán; kịch bản Thấp bán thêm 0 kg, tức lỗ toàn bộ chi phí cố định. Hòa vốn ở mức thấp là tín hiệu tốt, nhưng cần nhu cầu thực sự vượt năng lực hiện tại.

#### Case 7.7 - Bước 5 - Cây quyết định với NPV (5 năm, 12%/năm)
Hệ số hiện tại hóa niên kim 5 năm: $\sum_{t=1}^{5} 1/1.12^t = 3.6048$.

Ba phương án: **A** mua máy rang mới (vốn 480 triệu, chi phí cố định 90 triệu/năm, lợi nhuận góp 40,000 VNĐ/kg); **B** thuê rang gia công bên ngoài phần vượt (không đầu tư, chi phí biến đổi cao hơn 20,000 VNĐ/kg, nên lợi nhuận góp chỉ 20,000 VNĐ/kg); **C** không làm gì (0).

| Kịch bản (xác suất) | Bán thêm/năm (kg) | A: dòng tiền ròng/năm (triệu) | NPV A (triệu) | B: dòng tiền/năm (triệu) | NPV B (triệu) |
|---|---|---|---|---|---|
| Cao (0.3) | 24,528 | 24,528 x 40,000 - 90 = **891.1** | 891.1 x 3.6048 - 480 = **2,732.3** | 24,528 x 20,000 = 490.6 | 490.6 x 3.6048 = **1,768.4** |
| Trung bình (0.5) | 10,128 | 10,128 x 40,000 - 90 = **315.1** | 315.1 x 3.6048 - 480 = **655.9** | 10,128 x 20,000 = 202.6 | **730.2** |
| Thấp (0.2) | 0 | -90 | -90 x 3.6048 - 480 = **-804.4** | 0 | **0** |
| **EMV (NPV kỳ vọng)** | | | **986.8** | | **895.6** |

Tính EMV của A: $0.3 \times 2{,}732.3 + 0.5 \times 655.9 + 0.2 \times (-804.4) = 819.7 + 328.0 - 160.9 = 986.8$ triệu. EMV của B: $0.3 \times 1{,}768.4 + 0.5 \times 730.2 + 0 = 530.5 + 365.1 = 895.6$ triệu.

```
                          ┌── Cao (0.3) ──────▶ NPV +2,732.3
        ┌── A. Mua máy ───┼── Trung bình (0.5) ▶ NPV +655.9       EMV(A) = 986.8
        │                 └── Thấp (0.2) ─────▶ NPV -804.4
 ───[Quyết định]
        │                 ┌── Cao (0.3) ──────▶ NPV +1,768.4
        ├── B. Thuê ngoài ┼── Trung bình (0.5) ▶ NPV +730.2       EMV(B) = 895.6
        │                 └── Thấp (0.2) ─────▶ NPV 0
        └── C. Không làm ─────────────────────▶ NPV 0             EMV(C) = 0
```

**Phương án D - "quyền chọn chờ đợi" (staged)**: năm đầu thuê rang gia công (B) để quan sát nhu cầu thật; cuối năm 1, nếu nhu cầu là Cao hoặc Trung bình thì mới mua máy (vốn bỏ ra ở cuối năm 1) và hưởng phương án A trong 4 năm còn lại; nếu Thấp thì tiếp tục không đầu tư. Giả định nhu cầu đã được "lộ diện" sau một năm và giá máy không đổi.
- Cao: $490.6/1.12 + \sum_{t=2}^{5}(891.1)/1.12^t - 480/1.12 = 2{,}426.1$ triệu.
- Trung bình: $202.6/1.12 + \sum_{t=2}^{5}(315.1)/1.12^t - 480/1.12 = 606.9$ triệu.
- Thấp: 0 (không mất vốn).
- **EMV(D)** = $0.3 \times 2{,}426.1 + 0.5 \times 606.9 + 0.2 \times 0 = 727.8 + 303.5 = 1{,}031.3$ triệu.

| Phương án | EMV (triệu VNĐ) | NPV xấu nhất (triệu VNĐ) | Vốn phải bỏ ra ngay |
|---|---|---|---|
| A. Mua máy ngay | 986.8 | **-804.4** | 480 |
| B. Thuê ngoài | 895.6 | 0 | 0 |
| C. Không làm | 0 | 0 | 0 |
| D. Thuê ngoài rồi quyết định | **1,031.3** | 0 | 0 |

#### Case 7.8 - Bước 6 - Mô phỏng Monte Carlo
Thay ba kịch bản rời rạc bằng phân phối tam giác cho nhu cầu hàng tháng: thấp nhất 7,000, khả dĩ nhất 8,800, cao nhất 11,000 kg/tháng (trung bình $(7{,}000 + 8{,}800 + 11{,}000)/3 = 8{,}933$). Chạy 10,000 lần (seed ngẫu nhiên = 42; mỗi lần: bán thêm = $\max(0, \min(\text{nhu cầu}; 10{,}608) - 7{,}956) \times 12$; tính NPV 5 năm cho A và B như bước 5):

| Chỉ số | A. Mua máy | B. Thuê ngoài |
|---|---|---|
| NPV trung bình | 951 triệu | 878 triệu |
| Xác suất NPV < 0 | **27.7%** | 0% |
| Phân vị 5% (kịch bản xấu nhất trong 20) | -804 triệu | 0 |

(Kết quả có thể chênh nhẹ giữa các lần chạy với seed khác.)

#### Case 7.9 - Diễn giải kinh doanh và khuyến nghị
1. **Đừng mua máy vì "gần quá tải"**: A có EMV cao hơn B 91 triệu (986.8 so với 895.6) nhưng 20% khả năng lỗ 804 triệu và xác suất lỗ khoảng 28% trong mô phỏng. Với xưởng nhỏ, một khoản lỗ 804 triệu có thể gây nguy hiểm cho dòng tiền.
2. **Thuê gia công (B) có EMV thấp hơn không nhiều nhưng không có rủi ro lỗ**, và chuyển chi phí cố định thành chi phí biến đổi.
3. **Phương án D (quan sát 1 năm rồi quyết) thắng cả về kỳ vọng lẫn rủi ro** (1,031.3 triệu, không có kịch bản lỗ), vì chi phí của việc chờ (mất 20,000 VNĐ/kg trên phần bán thêm trong năm đầu) nhỏ hơn giá trị của thông tin thu được. Đây là ứng dụng của "quyền chọn thực" (real option).
4. Cần kiểm soát chất lượng với xưởng rang gia công (hương vị là tài sản thương hiệu), có hợp đồng SLA rõ ràng.
5. Điều kiện kích hoạt mua máy: hai quý liên tiếp nhu cầu vượt 8,500 kg/tháng, hoặc có hợp đồng cam kết sản lượng tối thiểu từ khách hàng. Nếu mua máy rang, đồng thời lập kế hoạch nâng cấp công đoạn đóng gói (nút thắt tiếp theo).

#### Case 7.10 - Bài học
Trình tự chuẩn: đo năng lực (3 loại), tìm nút thắt, định lượng khoảng cách theo kịch bản, tính hòa vốn, so sánh phương án bằng EMV/NPV, đánh giá rủi ro (kịch bản xấu nhất, Monte Carlo), rồi cân nhắc phương án "chờ có chủ đích". Không công cụ nào đơn lẻ đủ để ra quyết định.

### 8. Bảng tổng hợp bài học từ các case study

| Case study | Chiến lược/công cụ áp dụng | Bài học chính |
|---|---|---|
| Amazon (mô hình minh họa) | Lead + Chase + tự động hóa | Kết hợp đầu tư dài hạn với lao động linh hoạt cho nhu cầu thời vụ cực đoan; Level đắt gấp 2.6 lần Chase trong mô hình |
| Highlands Coffee (mô hình minh họa) | Erlang C + Shift Scheduling | Xếp ca theo giờ cao/thấp điểm tiết kiệm 31% giờ công mà vẫn đạt chuẩn chờ <= 1 phút |
| Xưởng may Bình Dương | Match (đầu tư 40% + thầu phụ 60%), NPV theo thời gian đơn hàng | Điểm quyết định là đơn hàng kéo dài bao lâu (từ 20 tháng thì tự đầu tư thắng), không phải đơn hàng lớn cỡ nào |
| Ngành hàng không (thất bại) | Lead Strategy quá mức, đòn bẩy hoạt động cao | Chi phí cố định cứng khuếch đại thua lỗ; cấu trúc linh hoạt giảm lỗ còn 48% và hạ điểm hòa vốn từ 72.7% xuống 57.1% |
| Phòng khám TP.HCM | Match + đặt lịch hẹn + M/M/c | Điều tiết nhu cầu bằng công nghệ thay thế một phần đầu tư vật lý; chờ giảm từ khoảng 1.8 giờ xuống 5.1 phút |
| FPT Software (mô hình minh họa) | Bench + đào tạo nội bộ + gig | Năng lực nhân sự tri thức cần vùng đệm (cushion) và đào tạo liên tục thay vì chỉ tuyển dụng |
| Cà phê Đất Đỏ (SME mới) | Nút thắt, Break-even, Decision Tree, Monte Carlo, Real Option | Đừng đầu tư vì "gần quá tải": thuê ngoài trước, đo nhu cầu, rồi mới quyết định (EMV 1,031 triệu, không có kịch bản lỗ) |

---

## IV. Ứng dụng cho SME

### 4.1. Quy trình 7 bước hoạch định năng lực

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
   │  So sánh Lead/Lag/Match, phân tích điểm hòa vốn, EMV/NPV từng phương án
   ▼
Bước 6: Triển khai quyết định đầu tư (Implementation)
   │  Mua máy móc, tuyển dụng, xây dựng cơ sở mới, thuê ngoài
   ▼
Bước 7: Giám sát & Điều chỉnh (Monitoring & Adjustment)
      Theo dõi hiệu suất thực tế, điều chỉnh kế hoạch theo biến động thị trường
```

| Bước | Dữ liệu cần thu thập | Đầu ra | Công cụ/Mục tham chiếu |
|---|---|---|---|
| 1 | Doanh số 12-24 tháng, đơn hàng đã chốt | Dự báo 3 kịch bản (cao/trung/thấp) có xác suất | Excel; file 07 |
| 2 | Giờ chạy máy, sản lượng, sự cố | Năng lực thiết kế/hiệu quả/thực tế, Hiệu suất, Mức sử dụng | 1.2 |
| 3 | Kết quả bước 1 và 2 | Khoảng thiếu (kg, SP, giờ) theo từng kịch bản | Case 7, bước 2 |
| 4 | Năng lực từng công đoạn | Công đoạn nút thắt và nút thắt kế tiếp | 2.1 |
| 5 | Chi phí cố định/biến đổi mỗi phương án | Q*, EMV, NPV, kịch bản xấu nhất | 1.3, 2.9, 2.10 |
| 6 | Hợp đồng, tiến độ | Kế hoạch triển khai, ramp-up | 2.4 |
| 7 | KPI hằng tháng | Cập nhật dự báo, kích hoạt bước đầu tư tiếp theo | Phụ lục |

### 4.2. Bảng các sai lầm thường gặp

| Sai lầm | Hậu quả | Cách phòng tránh |
|---|---|---|
| Chỉ dựa vào dự báo lạc quan để đầu tư | Dư thừa năng lực khi thị trường không như kỳ vọng | Xây dựng kịch bản dự báo (best/base/worst case), tính EMV và NPV xấu nhất |
| Không xác định đúng nút thắt cổ chai | Đầu tư sai chỗ, không cải thiện năng lực tổng thể | Phân tích luồng quy trình kỹ trước khi đầu tư |
| Vận hành ở mức 100% công suất liên tục | Thời gian chờ tăng vọt, không có buffer cho sự cố | Duy trì tỷ lệ sử dụng công suất hợp lý (75-90%, tùy ngành) |
| Bỏ qua giai đoạn ramp-up khi mở rộng | Kỳ vọng năng lực đầy đủ ngay lập tức, thất vọng khi thực tế thấp hơn | Tính đến đường cong học tập trong kế hoạch |
| Không có kế hoạch dự phòng khi cam kết dài hạn | Thiệt hại nặng khi có sự kiện bất ngờ (như COVID-19) | Đàm phán điều khoản linh hoạt, kịch bản ứng phó rủi ro |
| Đầu tư vì một đơn hàng lớn duy nhất | Không đủ thời gian thu hồi vốn (xem Case 3: đơn 4 tháng, đầu tư lỗ 635 triệu) | Tính điểm giao theo số tháng đơn hàng kéo dài; yêu cầu cam kết dài hạn |
| Chỉ nhìn giá trị kỳ vọng (EMV), bỏ qua kịch bản xấu | Phá sản vì một kịch bản xấu dù EMV dương | Luôn báo cáo kịch bản xấu nhất và xác suất lỗ |
| Quên rằng nút thắt dịch chuyển sau khi nâng cấp | Mua máy mới nhưng sản lượng không tăng như tính | Tính lại năng lực toàn hệ thống sau mỗi lần nâng công đoạn (Case 7, bước 3) |

### 4.3. Quy mô áp dụng: SME vs Doanh nghiệp lớn

| Thành phần | SME | Doanh nghiệp lớn |
|---|---|---|
| Dự báo nhu cầu | Kinh nghiệm, dữ liệu lịch sử đơn giản | Mô hình thống kê/AI phức tạp, đa kịch bản |
| Chiến lược năng lực | Chủ yếu Match/Lag do hạn chế vốn | Có thể áp dụng Lead Strategy nhờ tiềm lực tài chính |
| Công cụ phân tích | Excel, ước lượng thủ công | Phần mềm mô phỏng (simulation), APS (Advanced Planning System) |
| Linh hoạt điều chỉnh | Nhanh, ít ràng buộc hợp đồng dài hạn | Chậm hơn do cam kết đầu tư/hợp đồng lớn |
| Rủi ro chính | Thiếu vốn đầu tư khi cơ hội đến | Rủi ro dư thừa năng lực khi dự báo sai |

### 4.4. Chi phí đầu tư theo giai đoạn phát triển

| Giai đoạn | Hoạt động hoạch định năng lực | Chi phí ước tính (VNĐ) |
|---|---|---|
| Khởi nghiệp | Ước lượng thủ công, thuê ngoài linh hoạt | 0 - 50 triệu |
| Tăng trưởng | Đầu tư máy móc/nhân sự cơ bản theo Match Strategy | 200 triệu - 2 tỷ |
| Mở rộng | Xây dựng cơ sở mới, đầu tư tự động hóa một phần | 5 - 30 tỷ |
| Doanh nghiệp lớn | Đầu tư nhà máy/trung tâm phân phối quy mô lớn, tự động hóa cao | 50 - hàng nghìn tỷ |

(Khoảng giá trị mang tính tham khảo, thay đổi theo ngành.)

### 4.5. Lộ trình khuyến nghị cho SME

1. Bắt đầu với việc đo lường chính xác năng lực hiện tại (thiết kế, hiệu quả, thực tế).
2. Áp dụng phân tích điểm hòa vốn đơn giản trước khi quyết định đầu tư mở rộng.
3. Ưu tiên chiến lược Match/Lag để giảm rủi ro tài chính, chỉ áp dụng Lead khi có cam kết đơn hàng dài hạn rõ ràng.
4. Tận dụng thuê ngoài (outsourcing) một phần năng lực trong giai đoạn nhu cầu tăng đột biến chưa rõ tính bền vững; coi thuê ngoài là "quyền chọn chờ đợi" (Case 7).
5. Khi quy mô đủ lớn, đầu tư công cụ mô phỏng/dự báo nâng cao để tối ưu hóa quyết định đầu tư năng lực.

### 4.6. Sơ đồ quyết định chiến lược thời điểm đầu tư năng lực

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

## V. Tools & Templates

### 5.1. Bảng công cụ phần mềm hỗ trợ hoạch định năng lực

| Công cụ | Chức năng | Chi phí ước tính | Phù hợp |
|---|---|---|---|
| Excel với công thức Break-even/Queuing | Phân tích cơ bản | Miễn phí | SME nhỏ |
| Arena, Simul8 (Simulation Software) | Mô phỏng dòng chảy quy trình phức tạp | 50-200 triệu/license | SME vừa, tư vấn |
| SAP APO/IBP, Oracle Demantra | Hoạch định năng lực tích hợp ERP | Hàng tỷ/năm | Doanh nghiệp lớn |
| Google Sheets + Power BI | Theo dõi KPI năng lực trực quan | Miễn phí - vài triệu/tháng | Mọi quy mô |

(Chi phí là ước tính tham khảo, cần kiểm tra lại báo giá hiện hành.)

### 5.2. Template: Bảng tính điểm hòa vốn cho quyết định đầu tư năng lực

```
Phương án đầu tư: _______________
Chi phí cố định tăng thêm (FC): _______________ VNĐ/năm
Giá bán trung bình (P): _______________ VNĐ/đơn vị
Chi phí biến đổi/đơn vị (VC): _______________ VNĐ/đơn vị

Điểm hòa vốn (Q hòa vốn) = FC / (P - VC) = _______________ đơn vị/năm

Dự báo nhu cầu năm 1: _______  Năm 2: _______  Năm 3: _______
So sánh với điểm hòa vốn → Quyết định: [ ] Đầu tư  [ ] Không đầu tư  [ ] Đầu tư từng phần
```

### 5.3. Template: Bảng đánh giá năng lực hiện tại

| Công đoạn | Năng lực/giờ | Giờ/ngày x ngày/tháng | Thiết kế/tháng | Hiệu quả (%) | Hiệu quả/tháng | Thực tế/tháng | Hiệu suất | Mức sử dụng |
|---|---|---|---|---|---|---|---|---|
| (điền) | a | b | c = a x b | d | e = c x d | f | f / e | f / c |

Công đoạn có "Thiết kế/tháng" nhỏ nhất = nút thắt; năng lực hệ thống = giá trị đó.

### 5.4. Công thức Excel/Google Sheets hữu ích

| Mục đích | Công thức mẫu |
|---|---|
| Điểm hòa vốn | `=FC/(P-VC)` |
| Đường cong học tập (đơn vị thứ n) | `=T1*n^(LOG(r,2))` với r là 0.9 chẳng hạn |
| Thời gian chờ M/M/1 (giờ) | `=lambda/(mu*(mu-lambda))` |
| Xác suất chờ Erlang C (a = lambda/mu, c quầy) | `=(POISSON.DIST(c,a,FALSE)/(1-a/c))/((POISSON.DIST(c,a,FALSE)/(1-a/c))+POISSON.DIST(c-1,a,TRUE))` |
| Thời gian chờ M/M/c (giờ) | `=Pw/(c*mu-lambda)` |
| NPV niên kim | `=-CAPEX+PV(rate,n,-NetCashflow)` hoặc `=NPV(rate, dòng tiền năm 1..n) - CAPEX` |
| Nhu cầu tam giác ngẫu nhiên (a thấp nhất, m khả dĩ nhất, b cao nhất; u = RAND() đặt ở ô riêng) | `=IF(u<(m-a)/(b-a), a+SQRT(u*(b-a)*(m-a)), b-SQRT((1-u)*(b-a)*(b-m)))` |

Gợi ý Monte Carlo trong Excel: tạo 1,000 dòng, mỗi dòng rút một nhu cầu ngẫu nhiên và tính NPV; dùng `=COUNTIF(cột NPV,"<0")/1000` để tính xác suất lỗ.

---

## VI. Bài tập thực hành

> Các bài có số liệu bên dưới đều kèm đáp án đã kiểm tra tính toán. Làm bài trước, xem đáp án sau.

**Bài 1 - Ba loại năng lực.** Một xưởng bánh có năng lực thiết kế 1,500 bánh/ngày, năng lực hiệu quả 1,200 bánh/ngày, sản lượng thực tế 1,000 bánh/ngày. Tính Hiệu suất, Mức sử dụng. Nên cải thiện vận hành hay đầu tư thêm lò?
*Đáp án*: Hiệu suất = 1,000/1,200 = 83.3%; Mức sử dụng = 1,000/1,500 = 66.7%; năng lực hiệu quả/thiết kế = 80%. Còn dư 200 bánh/ngày ở mức hiệu quả, và mức sử dụng chỉ 66.7%, nên cải thiện vận hành (nâng hiệu suất lên khoảng 90%+) trước khi đầu tư.

**Bài 2 - Điểm hòa vốn.** Mở rộng cần chi phí cố định 600 triệu/năm; giá bán 150,000 VNĐ; chi phí biến đổi 90,000 VNĐ; năng lực mới 15,000 đv/năm; dự báo bán thêm 13,000 đv. Tính điểm hòa vốn, tỷ lệ công suất tại hòa vốn và lợi nhuận.
*Đáp án*: $Q^* = 600{,}000{,}000 / 60{,}000 = 10{,}000$ đv/năm (833 đv/tháng); chiếm $10{,}000 / 15{,}000 = 66.7\%$ công suất; lợi nhuận $= (13{,}000 - 10{,}000) \times 60{,}000 = 180$ triệu/năm.

**Bài 3 - Hàng đợi M/M/1.** Quầy tư vấn có $\lambda = 24$ khách/giờ, $\mu = 30$ khách/giờ. Tính $\rho$, $W_q$, $L_q$, $W$. Nếu $\lambda$ tăng lên 28, $W_q$ là bao nhiêu?
*Đáp án*: $\rho = 0.8$; $W_q = 24/(30 \times 6) = 0.1333$ giờ = 8 phút; $L_q = 24^2/(30 \times 6) = 3.2$ khách; $W = 1/(30-24) = 10$ phút. Với $\lambda = 28$: $W_q = 28/(30 \times 2) = 0.467$ giờ = 28 phút (nhu cầu tăng 17% làm thời gian chờ tăng 3.5 lần).

**Bài 4 - Hàng đợi M/M/c.** Một quán có $\lambda = 90$ khách/giờ, mỗi nhân viên $\mu = 30$ khách/giờ. Cần bao nhiêu nhân viên để $W_q \le 1$ phút?
*Đáp án*: $c = 3$ → $\rho = 1$, không ổn định. $c = 4$ → $\rho = 75\%$, $P_w = 50.9\%$, $W_q = 0.509/(120-90) = 0.0170$ giờ = 1.02 phút (hơi vượt). $c = 5$ → $\rho = 60\%$, $P_w = 23.6\%$, $W_q = 0.236/(150-90) = 0.0039$ giờ = 0.24 phút. Chọn $c = 5$ (hoặc 4 nếu chấp nhận 1.02 phút).

**Bài 5 - So sánh Lead/Lag/Match.** Chọn một tình huống kinh doanh (quán cà phê muốn mở chi nhánh, xưởng nhận đơn mới...), lập bảng so sánh ba chiến lược theo CAPEX, rủi ro nhàn rỗi, chi phí cơ hội, rồi đề xuất kèm lý do.
*Hướng dẫn*: dùng bảng ở mục 2.13.1; SME ít vốn và nhu cầu bất định thường chọn Match/Lag. Nên tính EMV (mục 2.10) cho ít nhất ba kịch bản để chứng minh lựa chọn.

**Bài 6 - Nút thắt cổ chai.** Quy trình 4 công đoạn nối tiếp có năng lực 80, 50, 70, 90 sản phẩm/giờ; làm việc 8 giờ/ngày; năng lực hiệu quả 85% năng lực thiết kế. Xác định nút thắt, năng lực thiết kế/hiệu quả của hệ thống; nếu nâng công đoạn 2 lên 75 sản phẩm/giờ thì kết quả ra sao?
*Đáp án*: Nút thắt = công đoạn 2 (50/giờ) → thiết kế $50 \times 8 = 400$ sp/ngày; hiệu quả $400 \times 85\% = 340$ sp/ngày. Nâng công đoạn 2 lên 75: nút thắt chuyển sang công đoạn 3 (70/giờ) → thiết kế $70 \times 8 = 560$ sp/ngày (tăng 40%, không phải 50% như mức tăng của công đoạn 2).

**Bài 7 - Aggregate Planning.** Dùng số liệu mục 2.7 nhưng giả định chi phí lưu kho tăng lên 20,000 VNĐ/đv/tháng (hàng tươi, dễ hỏng). Phương án nào rẻ nhất?
*Đáp án*: Chase = 340 triệu (không đổi, không có tồn kho). Level = 195 + 1,650 x 20,000 / 1,000,000 = 195 + 33 = **228 triệu**. Mixed = 180 + 15 + 1,000 x 20,000/1,000,000 = 180 + 15 + 20 = **215 triệu**. Mixed rẻ nhất; Level vẫn rẻ hơn Chase nhưng đã đắt hơn Mixed vì chi phí lưu kho tăng.

**Bài 8 - Đường cong học tập.** $T_1 = 20$ giờ, tỷ lệ học tập 85%. Dự đoán thời gian đơn vị thứ 50 và thứ 100.
*Đáp án*: $b = \log_2 0.85 = -0.2345$; $T_{50} = 20 \times 50^{-0.2345} = 7.99$ giờ; $T_{100} = 20 \times 100^{-0.2345} = 6.79$ giờ (đúng bằng 85% của $T_{50}$).

**Bài 9 - Hàng không và đòn bẩy hoạt động.** Dùng mô hình mục III, Case 4. Tính doanh thu hòa vốn khi chi phí cố định 400, chi phí biến đổi bằng 45% doanh thu. Nếu chuyển một nửa chi phí cố định thành chi phí cắt giảm được (200 cố định + 200 linh hoạt, linh hoạt tương đương 20% doanh thu bình thường) thì sao?
*Đáp án*: $400/(1 - 0.45) = 727.3$ (72.7% doanh thu bình thường). Cấu trúc linh hoạt: $200/(1 - 0.45 - 0.20) = 571.4$ (57.1%). Khi doanh thu chỉ còn 100: lỗ lần lượt -345 và -165.

**Bài 10 - Lịch ca linh hoạt.** Quán trà sữa có giờ cao điểm $\lambda = 60$ đơn/giờ, thấp điểm $\lambda = 20$ đơn/giờ; mỗi người pha chế $\mu = 20$ đơn/giờ; mục tiêu $W_q \le 1.6$ phút ở cao điểm và $\le 1$ phút thấp điểm. Cần mấy người mỗi khung?
*Đáp án*: Cao điểm: $c = 3$ → $\rho = 1$ (không ổn định); $c = 4$ → $W_q = 1.53$ phút (đạt chuẩn 1.6); $c = 5$ → 0.35 phút. Chọn $c = 4$ (hoặc 5 nếu muốn chờ thấp hơn). Thấp điểm: $c = 2$ → $\rho = 50\%$, $W_q = 1.0$ phút (đúng ngưỡng); $c = 3$ → 0.14 phút. Lịch gợi ý 4 người cao điểm, 2 người thấp điểm.

**Bài 11 - Sở hữu vs thuê ngoài.** $FC_{own} = 480$ triệu/năm, $VC_{own} = 40{,}000$, $VC_{out} = 52{,}000$ VNĐ/đv. Tính $Q^*$; so sánh chi phí tại 30,000 và 50,000 đv/năm.
*Đáp án*: $Q^* = 480{,}000{,}000/12{,}000 = 40{,}000$ đv. Tại 30,000: tự làm $= 480 + 30{,}000 \times 40{,}000/10^6 = 1{,}680$ triệu; thuê ngoài $= 30{,}000 \times 52{,}000/10^6 = 1{,}560$ triệu → thuê ngoài rẻ hơn 120 triệu. Tại 50,000: tự làm = 480 + 2,000 = 2,480 triệu; thuê ngoài = 2,600 triệu → tự làm rẻ hơn 120 triệu.

**Bài 12 - Capacity Cushion.** Nhà máy bao bì ổn định có mức sử dụng 92%. So sánh với mức tham khảo 10-15%; cần tăng năng lực bao nhiêu để mức sử dụng về 90% hoặc 85%?
*Đáp án*: Cushion = 100% - 92% = 8%, thấp hơn 10-15%. Năng lực cần tăng: để về 90%: $92/90 = 1.022$, tức +2.2%; để về 85%: $92/85 = 1.082$, tức +8.2% (so với năng lực hiện có).

**Bài 13 - Cây quyết định và Monte Carlo.** (a) Tính EMV cho hai phương án ở mục 2.10. (b) Dùng công thức tam giác ở mục 5.4 và số liệu Case 7 để tự chạy Monte Carlo 1,000 dòng trong Excel; ước lượng xác suất NPV < 0 của phương án mua máy.
*Đáp án*: (a) EMV(A) = 0.4 x 600 + 0.6 x (-200) = 120 triệu; EMV(B) = 0.4 x 250 + 0.6 x 50 = 130 triệu → chọn B nếu chỉ xét EMV và rủi ro. (b) Kết quả mong đợi khoảng 25-30% (kết quả trong file mục 7.8 là 27.7% với 10,000 lần chạy); mỗi lần chạy Excel sẽ chênh nhẹ vì RAND() thay đổi.

**Bài 14 - Cân bằng chuyền.** Quy trình có tổng thời gian công việc 8.4 phút; làm việc 480 phút/ngày; yêu cầu 160 sản phẩm/ngày. Tính nhịp, số trạm tối thiểu, hiệu suất nếu dùng 3 trạm.
*Đáp án*: $C = 480/160 = 3$ phút; $N_{min} = \lceil 8.4/3 \rceil = \lceil 2.8 \rceil = 3$; hiệu suất $= 8.4/(3 \times 3) = 93.3\%$ (nếu chia được để trạm nào cũng không quá 3 phút).

**Bài 15 - Tình huống tổng hợp (thảo luận).** Nghiên cứu một SME giả định tăng trưởng 30%/năm trong 3 năm: đề xuất lộ trình hoạch định năng lực (khi nào Lag, khi nào Match, khi nào Lead), chi phí đầu tư ước tính theo từng giai đoạn (tham khảo mục 4.4), và nêu 3 chỉ số cảnh báo sớm để kích hoạt bước đầu tư kế tiếp. Ngoài ra, thiết kế một lịch làm việc ca linh hoạt cho một cửa hàng/quán ăn dựa trên số liệu lượng khách theo giờ giả định.

---

## PHỤ LỤC: CHECKLIST HOẠCH ĐỊNH NĂNG LỰC TỔNG HỢP

### A. Checklist tự đánh giá năng lực doanh nghiệp (Capacity Self-Assessment)

Trước khi tiến hành hoạch định năng lực bài bản, doanh nghiệp (đặc biệt SME) nên tự đánh giá:

- □ Đã đo lường được năng lực thiết kế và năng lực hiệu quả hiện tại của quy trình cốt lõi?
- □ Đã tính Hiệu suất và Mức sử dụng, và biết rõ khoảng cách "không tránh được" và "cải thiện được"?
- □ Đã xác định rõ nút thắt cổ chai (bottleneck) trong hệ thống hiện tại, và biết nút thắt kế tiếp là gì?
- □ Có dữ liệu lịch sử về nhu cầu để dự báo tương đối tin cậy, và đã xây dựng ít nhất ba kịch bản (cao/trung/thấp) có xác suất?
- □ Đã tính toán điểm hòa vốn cho các phương án đầu tư mở rộng đang cân nhắc, và so sánh với năng lực mới (hòa vốn ở bao nhiêu % công suất)?
- □ Đã tính EMV/NPV và xem xét kịch bản xấu nhất của từng phương án?
- □ Có phương án dự phòng (thuê ngoài, lao động linh hoạt) cho trường hợp nhu cầu tăng đột biến ngắn hạn?
- □ Đã đánh giá rủi ro của các cam kết đầu tư/hợp đồng dài hạn trước các sự kiện bất ngờ?
- □ Đã xác định tỷ lệ dự phòng năng lực (capacity cushion) phù hợp với đặc thù ngành?
- □ Đã cân nhắc đầy đủ giữa sở hữu tài sản và thuê ngoài linh hoạt cho từng loại năng lực (điểm hòa vốn giữa tự làm và thuê ngoài)?
- □ Đội ngũ quản lý đã hiểu rõ khái niệm nút thắt cổ chai và cách quản trị nó theo Lý thuyết ràng buộc?
- □ Với dịch vụ: đã đo $\lambda$ theo khung giờ và xác định số quầy/nhân viên để thời gian chờ đạt chuẩn?
- □ Đã tính đến giai đoạn ramp-up (đường cong học tập) của người/máy mới trong kế hoạch giao hàng?
- □ Có kế hoạch giám sát và điều chỉnh định kỳ (ít nhất hàng quý) cho kế hoạch năng lực đã thiết lập?
- □ Đã trao đổi với bộ phận tài chính về tác động dòng tiền của các phương án đầu tư năng lực?
- □ Đã xây dựng ít nhất một kịch bản dự phòng cho trường hợp nhu cầu sụt giảm bất ngờ?

### B. Bảng đo lường KPI năng lực

| KPI | Công thức | Mục tiêu tham khảo |
|---|---|---|
| Hiệu suất (Efficiency) | Sản lượng thực tế / Năng lực hiệu quả | > 85% |
| Mức sử dụng (Utilization) | Sản lượng thực tế / Năng lực thiết kế | 75-90% (tránh 100% liên tục) |
| Thời gian ngừng máy (Downtime %) | Thời gian ngừng / Tổng thời gian vận hành | < 10% |
| Thời gian chờ đợi trung bình (dịch vụ) | Theo mô hình hàng đợi | Theo chuẩn ngành/kỳ vọng khách hàng |
| Tỷ lệ tăng trưởng năng lực (Capacity Growth Rate) | (Năng lực mới - Năng lực cũ) / Năng lực cũ | Theo kế hoạch chiến lược |

### C. Bảng công thức tổng hợp

| Mục tiêu | Công thức |
|---|---|
| Hiệu suất | $\text{Efficiency} = \text{Sản lượng thực tế}/\text{Năng lực hiệu quả}$ |
| Mức sử dụng | $\text{Utilization} = \text{Sản lượng thực tế}/\text{Năng lực thiết kế}$ |
| Điểm hòa vốn | $Q^* = FC/(P-VC)$ |
| Hòa vốn tự làm vs thuê ngoài | $Q^* = FC_{own}/(VC_{out}-VC_{own})$ |
| Hệ số sử dụng hàng đợi | $\rho = \lambda/\mu$ (M/M/1); $\rho = \lambda/(c\mu)$ (M/M/c) |
| Thời gian chờ M/M/1 | $W_q = \lambda/[\mu(\mu-\lambda)]$ |
| Thời gian chờ M/M/c | $W_q = P_w/(c\mu-\lambda)$ ($P_w$ theo Erlang C) |
| Đường cong học tập | $T_n = T_1 \times n^{\log_2(r)}$ |
| Nhịp chuyền | $C = \text{Thời gian có sẵn}/\text{Sản lượng yêu cầu}$ |
| Số trạm tối thiểu | $N_{min} = \lceil \sum t_i / C \rceil$ |
| Hiệu suất cân bằng chuyền | $\sum t_i / (N \times C)$ |
| Giá trị kỳ vọng | $EMV = \sum p_i V_i$ |
| Capacity Cushion | $100\% - \text{Utilization Rate}$ |

### D. Sổ tay rủi ro hoạch định năng lực (Risk Register mẫu)

| Rủi ro | Xác suất | Tác động | Biện pháp giảm thiểu |
|---|---|---|---|
| Dự báo nhu cầu sai lệch lớn dẫn đến đầu tư dư thừa | Trung bình | Cao | Kịch bản dự báo đa chiều, đầu tư theo giai đoạn |
| Sự kiện bất khả kháng làm sụp đổ nhu cầu (như COVID-19) | Thấp | Rất cao | Điều khoản hợp đồng linh hoạt, kế hoạch BCP |
| Nút thắt cổ chai mới xuất hiện sau khi giải quyết cái cũ | Cao | Trung bình | Giám sát liên tục toàn bộ chuỗi quy trình |
| Thiếu lao động có kỹ năng khi mở rộng nhanh | Trung bình | Trung bình | Kế hoạch đào tạo trước, tính đến đường cong học tập |
| Phụ thuộc quá mức vào đối tác thuê ngoài năng lực | Trung bình | Trung bình | Đa dạng hóa đối tác, hợp đồng dịch vụ rõ ràng về SLA |
| Đầu tư công nghệ tự động hóa không phù hợp quy mô | Thấp | Cao | Đánh giá kỹ ROI và quy mô tối thiểu hiệu quả trước đầu tư |

### E. Bảng thuật ngữ (Glossary)

| Thuật ngữ | Giải thích |
|---|---|
| Design Capacity | Năng lực thiết kế - sản lượng tối đa lý thuyết |
| Effective Capacity | Năng lực hiệu quả - sản lượng tối đa thực tế khả thi |
| Utilization | Mức sử dụng năng lực so với năng lực thiết kế |
| Bottleneck | Nút thắt cổ chai - công đoạn giới hạn năng lực toàn hệ thống |
| Lead/Lag/Match Strategy | Ba chiến lược thời điểm đầu tư năng lực |
| Aggregate Planning | Hoạch định tổng hợp sản lượng/nhân lực trung hạn |
| Chase/Level/Mixed | Ba chiến lược Aggregate Planning |
| Queuing Theory | Lý thuyết hàng đợi - phân tích thời gian chờ đợi dịch vụ |
| Learning Curve | Đường cong học tập - giảm thời gian sản xuất theo kinh nghiệm tích lũy |
| Line Balancing | Cân bằng chuyền sản xuất |
| CRP | Capacity Requirements Planning - hoạch định yêu cầu năng lực chi tiết |
| Capacity Cushion | Tỷ lệ năng lực dự phòng chưa sử dụng, duy trì có chủ đích |
| Gig Economy | Nền kinh tế lao động linh hoạt theo nhu cầu, không cố định dài hạn |
| Monte Carlo Simulation | Phương pháp mô phỏng xác suất dựa trên hàng nghìn kịch bản ngẫu nhiên |
| M/M/c | Mô hình hàng đợi với c quầy phục vụ song song |
| Erlang C | Công thức xác suất khách phải chờ trong mô hình M/M/c |
| EMV | Expected Monetary Value - giá trị tiền tệ kỳ vọng |
| Real Option | Quyền chọn thực: giá trị của việc chờ thêm thông tin trước khi đầu tư |

### F. Ghi chú kết thúc

File này kết hợp lý thuyết định lượng (Break-even Analysis, Queuing Theory, Learning Curve, Line Balancing, Decision Tree) và các chiến lược định tính (Lead/Lag/Match Strategy) để cung cấp bức tranh toàn diện về hoạch định năng lực. Hoạch định năng lực không chỉ là bài toán kỹ thuật mà còn là quyết định chiến lược cấp cao, đòi hỏi sự phối hợp giữa bộ phận vận hành, tài chính và chiến lược kinh doanh. Xu hướng năng lực linh hoạt (flexible capacity, gig economy) là chuyển dịch quan trọng trong tư duy quản trị năng lực hiện đại, đặc biệt phù hợp với bối cảnh kinh doanh biến động nhanh tại Việt Nam.

---

## TÀI LIỆU THAM KHẢO

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
