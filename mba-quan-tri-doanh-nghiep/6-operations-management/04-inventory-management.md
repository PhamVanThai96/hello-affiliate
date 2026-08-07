# 04. Quản trị Tồn kho (Inventory Management)

> File thuộc bộ kiến thức Quản trị Vận hành (Operations Management) - MBA Knowledge Base
> Liên kết: [01-process-design-analysis.md](./01-process-design-analysis.md) | [03-supply-chain-management.md](./03-supply-chain-management.md) | [05-capacity-planning.md](./05-capacity-planning.md)

---

## I. Tổng quan & Lý thuyết nền tảng

### 1.1. Định nghĩa và vai trò của tồn kho

**Tồn kho (Inventory)** là toàn bộ nguyên vật liệu, bán thành phẩm, thành phẩm mà doanh nghiệp lưu giữ để phục vụ sản xuất hoặc bán hàng trong tương lai. Tồn kho là một khoản đầu tư (vốn lưu động bị "đóng băng"), do đó quản trị tồn kho là bài toán cân bằng giữa chi phí lưu giữ và khả năng đáp ứng nhu cầu khách hàng.

**Bốn loại tồn kho chính theo mục đích**:

| Loại tồn kho | Mục đích | Ví dụ |
|---|---|---|
| Tồn kho chu kỳ (Cycle Stock) | Đáp ứng nhu cầu bình thường giữa 2 lần đặt hàng | Hàng đặt định kỳ hàng tuần |
| Tồn kho an toàn (Safety Stock) | Phòng ngừa biến động nhu cầu hoặc lead time | Dự trữ thêm 20% so với nhu cầu dự báo |
| Tồn kho theo mùa (Seasonal Stock) | Đáp ứng nhu cầu tăng đột biến theo mùa vụ | Bánh trung thu, hàng Tết |
| Tồn kho trong chuyển (Pipeline/Transit Stock) | Hàng đang vận chuyển giữa các mắt xích | Hàng trên tàu biển từ Trung Quốc về Việt Nam |

### 1.2. Chi phí liên quan đến tồn kho

Ra quyết định tồn kho tối ưu đòi hỏi hiểu rõ 3 nhóm chi phí đối lập:

1. **Chi phí đặt hàng (Ordering Cost - S)**: chi phí phát sinh mỗi lần đặt hàng, không phụ thuộc số lượng đặt (chi phí hành chính, vận chuyển cố định, kiểm tra nhận hàng). Đặt hàng ít lần với số lượng lớn giúp giảm tổng chi phí đặt hàng.
2. **Chi phí lưu kho (Holding/Carrying Cost - H)**: chi phí phát sinh khi giữ hàng trong kho, bao gồm chi phí vốn (cơ hội), kho bãi, bảo hiểm, hao hụt/lỗi thời. Thường tính theo tỷ lệ % giá trị hàng tồn/năm (thường 15-30%/năm).
3. **Chi phí thiếu hàng (Stockout/Shortage Cost)**: chi phí phát sinh khi hết hàng - mất doanh số, mất khách hàng, chi phí đặt hàng khẩn cấp.

```
Tổng chi phí tồn kho (Total Cost)
        │
        │      Chi phí lưu kho (Holding Cost)
        │              ╱
        │            ╱     ← tăng theo Q (số lượng đặt hàng)
        │          ╱
        │  ─────────────────  Tổng chi phí (Total Cost)
        │        ╲                (hình chữ U, có điểm cực tiểu)
        │          ╲
        │            ╲    Chi phí đặt hàng (Ordering Cost)
        │              ╲   ← giảm theo Q
        │                ╲___________
        └────────────────────────────────▶ Q (Số lượng đặt hàng)
                    Q* (EOQ - điểm tối ưu)
```

### 1.3. Mô hình EOQ (Economic Order Quantity) - Ford W. Harris, 1913

EOQ là công thức kinh điển xác định số lượng đặt hàng tối ưu giúp tối thiểu hoá tổng chi phí tồn kho (chi phí đặt hàng + chi phí lưu kho).

**Công thức EOQ**:

$$EOQ = Q^* = \sqrt{\frac{2DS}{H}}$$

Trong đó:
- $D$ = Nhu cầu hàng năm (Annual Demand, đơn vị/năm)
- $S$ = Chi phí đặt hàng mỗi lần (Ordering Cost per order)
- $H$ = Chi phí lưu kho mỗi đơn vị mỗi năm (Holding Cost per unit per year)

**Số lần đặt hàng tối ưu mỗi năm**:

$$N^* = \frac{D}{Q^*}$$

**Chu kỳ đặt hàng tối ưu (ngày)**:

$$T^* = \frac{\text{Số ngày làm việc trong năm}}{N^*}$$

**Tổng chi phí tối ưu (Total Annual Cost)**:

$$TC^* = \sqrt{2DSH}$$

**Ví dụ minh hoạ**: Một cửa hàng bán lẻ có nhu cầu $D = 12,000$ đơn vị/năm, chi phí đặt hàng $S = 500,000$ VNĐ/lần, chi phí lưu kho $H = 20,000$ VNĐ/đơn vị/năm.

$$EOQ = \sqrt{\frac{2 \times 12,000 \times 500,000}{20,000}} = \sqrt{600,000,000} \approx 775 \text{ đơn vị}$$

Số lần đặt hàng tối ưu: $N^* = 12,000 / 775 \approx 15.5$ lần/năm (khoảng mỗi 23 ngày đặt hàng một lần nếu làm việc 360 ngày/năm).

### 1.4. Điểm đặt hàng lại (Reorder Point - ROP) và Tồn kho an toàn (Safety Stock)

**Điểm đặt hàng lại (ROP)** là mức tồn kho mà khi chạm tới, doanh nghiệp phải đặt hàng ngay để tránh hết hàng trước khi lô hàng mới về.

$$ROP = d \times L + SS$$

Trong đó:
- $d$ = Nhu cầu trung bình mỗi ngày (Average daily demand)
- $L$ = Thời gian giao hàng (Lead Time, tính bằng ngày)
- $SS$ = Tồn kho an toàn (Safety Stock)

**Công thức tính tồn kho an toàn khi nhu cầu biến động (giả định phân phối chuẩn)**:

$$SS = Z \times \sigma_d \times \sqrt{L}$$

Trong đó:
- $Z$ = Hệ số mức độ tin cậy (Service Level Z-score), ví dụ Z=1.65 cho mức phục vụ 95%, Z=2.33 cho 99%
- $\sigma_d$ = Độ lệch chuẩn của nhu cầu hàng ngày
- $L$ = Lead time (ngày)

**Bảng hệ số Z theo mức độ phục vụ (Service Level)**:

| Mức độ phục vụ (Service Level) | Hệ số Z |
|---|---|
| 90% | 1.28 |
| 95% | 1.65 |
| 97.5% | 1.96 |
| 99% | 2.33 |
| 99.9% | 3.09 |

**Ví dụ**: Nhu cầu trung bình ngày $d = 40$ đơn vị, độ lệch chuẩn $\sigma_d = 8$, lead time $L = 9$ ngày, mức phục vụ mong muốn 95% ($Z=1.65$).

$$SS = 1.65 \times 8 \times \sqrt{9} = 1.65 \times 8 \times 3 = 39.6 \approx 40 \text{ đơn vị}$$

$$ROP = 40 \times 9 + 40 = 360 + 40 = 400 \text{ đơn vị}$$

### 1.5. Phân loại ABC (ABC Analysis - dựa trên nguyên lý Pareto 80/20)

Phân loại ABC giúp doanh nghiệp tập trung nguồn lực quản trị vào nhóm hàng hoá quan trọng nhất thay vì đối xử đồng đều với toàn bộ danh mục.

| Nhóm | % số lượng mặt hàng (SKU) | % giá trị tồn kho | Mức độ kiểm soát |
|---|---|---|---|
| **A** | 10-20% | 70-80% | Kiểm soát chặt chẽ, kiểm kê thường xuyên, dự báo chính xác cao |
| **B** | 20-30% | 15-25% | Kiểm soát trung bình, kiểm kê định kỳ |
| **C** | 50-70% | 5-10% | Kiểm soát đơn giản, đặt hàng số lượng lớn ít lần |

```
% Giá trị tồn kho tích luỹ
100% │                                    ●───●───●  (Nhóm C: nhiều SKU,
     │                          ●───●───●              giá trị thấp)
 90% │                    ●───●
     │              ●───●        Nhóm B
 80% │        ●───●
     │      ●
     │    ●
     │  ●     Nhóm A (ít SKU, giá trị cao)
     │●
   0%└──────────────────────────────────────▶ % Số lượng SKU
      10%        30%              100%
```

### 1.6. Hệ thống kiểm soát tồn kho: Liên tục (Continuous Review) vs Định kỳ (Periodic Review)

| Tiêu chí | Hệ thống liên tục (Q-system, s,Q) | Hệ thống định kỳ (P-system, s,S) |
|---|---|---|
| Cách theo dõi | Theo dõi tồn kho liên tục theo thời gian thực | Kiểm tra tồn kho theo chu kỳ cố định (VD: mỗi tuần) |
| Thời điểm đặt hàng | Khi tồn kho chạm ROP | Vào thời điểm kiểm tra định kỳ |
| Số lượng đặt hàng | Cố định (EOQ) | Biến đổi (đặt đủ để đạt mức tồn kho mục tiêu S) |
| Yêu cầu hệ thống | Cần hệ thống theo dõi thời gian thực (POS, mã vạch) | Đơn giản hơn, phù hợp kiểm kê thủ công |
| Tồn kho an toàn cần thiết | Thấp hơn (do phát hiện thiếu hàng sớm hơn) | Cao hơn (do có độ trễ giữa các lần kiểm tra) |
| Phù hợp | Hàng giá trị cao, nhu cầu ổn định, có hệ thống IT | SME, hàng giá trị thấp, kiểm kê thủ công |

---

## II. Phân tích chi tiết các công cụ/kỹ thuật

### 2.1. Just-In-Time (JIT) - Hệ thống sản xuất tinh gọn của Toyota

JIT là triết lý quản trị tồn kho nhằm giảm thiểu tồn kho xuống mức tối thiểu bằng cách chỉ sản xuất/nhận hàng đúng số lượng, đúng thời điểm cần thiết, dựa trên hệ thống kéo (Pull System) thay vì đẩy (Push System).

**Nguyên lý cốt lõi**:
- **Kanban**: thẻ tín hiệu (vật lý hoặc điện tử) ra lệnh sản xuất/bổ sung chỉ khi công đoạn sau tiêu thụ hết hàng của công đoạn trước.
- **Heijunka (San bằng sản xuất)**: san đều khối lượng và chủng loại sản xuất để tránh biến động đột ngột.
- **Quan hệ đối tác chặt chẽ với NCC**: giao hàng nhiều lần trong ngày, số lượng nhỏ, độ tin cậy giao hàng gần như tuyệt đối.

**Điều kiện tiên quyết để áp dụng JIT thành công**:
1. Nhu cầu ổn định và dự báo được.
2. Nhà cung cấp đáng tin cậy, khoảng cách địa lý gần hoặc hệ thống logistics rất hiệu quả.
3. Chất lượng sản phẩm ổn định (không có JIT nếu tỷ lệ lỗi cao, vì không có tồn kho đệm để bù đắp).
4. Văn hoá cải tiến liên tục (Kaizen) trong toàn tổ chức.

**Rủi ro của JIT**: Đại dịch COVID-19 và tình trạng đứt gãy chuỗi cung ứng toàn cầu 2020-2022 đã phơi bày điểm yếu của JIT thuần tuý - không có tồn kho đệm khiến nhiều doanh nghiệp (đặc biệt ngành ô tô, bán dẫn) phải dừng sản xuất khi nguồn cung gián đoạn. Xu hướng hậu COVID chuyển sang mô hình "Just-In-Case" (JIC) có chọn lọc cho các linh kiện quan trọng.

### 2.2. Mô hình chiết khấu theo số lượng (Quantity Discount Model)

Khi nhà cung cấp áp dụng chiết khấu theo số lượng đặt hàng, công thức EOQ cơ bản cần điều chỉnh để tính tổng chi phí (bao gồm cả chi phí mua hàng) ở mỗi mức giá:

$$TC = \frac{D}{Q} \times S + \frac{Q}{2} \times H + D \times P$$

Trong đó $P$ là đơn giá mua tại mức chiết khấu tương ứng. Quy trình: (1) tính EOQ tại mỗi mức giá, (2) kiểm tra tính khả thi (EOQ có nằm trong khoảng số lượng được chiết khấu không), (3) so sánh tổng chi phí giữa các phương án khả thi để chọn Q tối ưu.

### 2.3. Mô hình EOQ khi có thiếu hàng có kế hoạch (Planned Backorder Model)

Trong một số ngành cho phép khách hàng chấp nhận chờ đợi (backorder), công thức EOQ mở rộng cho phép tính toán mức thiếu hụt tối ưu (b) để giảm thêm chi phí lưu kho, đánh đổi với chi phí thiếu hàng (backorder cost). Đây là mô hình nâng cao thường dùng trong các ngành công nghiệp có sản phẩm đặt hàng theo yêu cầu (make-to-order).

### 2.4. Kiểm kê tồn kho theo chu kỳ (Cycle Counting)

Thay vì kiểm kê toàn bộ kho một lần mỗi năm (tốn thời gian, gây gián đoạn hoạt động), Cycle Counting chia nhỏ việc kiểm kê theo chu kỳ liên tục trong năm, ưu tiên tần suất cao hơn cho nhóm hàng A:

| Nhóm ABC | Tần suất kiểm kê khuyến nghị |
|---|---|
| A | Hàng tháng hoặc hàng tuần |
| B | Hàng quý |
| C | Nửa năm hoặc hàng năm |

### 2.5. Chỉ số vòng quay tồn kho (Inventory Turnover) và Số ngày tồn kho (Days of Inventory)

$$\text{Vòng quay tồn kho} = \frac{\text{Giá vốn hàng bán (COGS)}}{\text{Tồn kho bình quân}}$$

$$\text{Số ngày tồn kho (DIO)} = \frac{365}{\text{Vòng quay tồn kho}}$$

Vòng quay tồn kho càng cao (số ngày tồn kho càng thấp) thể hiện hiệu quả sử dụng vốn lưu động càng tốt, nhưng cần cân đối với rủi ro thiếu hàng. Chỉ số này thường được đối chiếu (benchmark) với trung bình ngành.

### 2.6. Mô hình người bán báo (Newsvendor Model) cho sản phẩm có vòng đời ngắn

Mô hình Newsvendor giải quyết bài toán tồn kho cho các sản phẩm chỉ bán được trong một chu kỳ duy nhất (single-period), không thể tái đặt hàng khi hết mùa - ví dụ báo giấy, bánh trung thu, thời trang theo mùa, vé sự kiện.

**Công thức mức phục vụ tối ưu (Critical Ratio - CR)**:

$$CR = \frac{C_u}{C_u + C_o}$$

Trong đó:
- $C_u$ = Chi phí thiếu hàng (Underage Cost) - lợi nhuận biên mất đi khi thiếu 1 đơn vị hàng bán
- $C_o$ = Chi phí thừa hàng (Overage Cost) - chi phí phát sinh khi thừa 1 đơn vị hàng không bán được (phải thanh lý lỗ)

Từ tỷ lệ $CR$, tra bảng phân phối chuẩn (hoặc phân phối nhu cầu thực tế) để xác định số lượng đặt hàng tối ưu $Q^*$ tương ứng với phân vị $CR$ của phân phối nhu cầu.

**Ví dụ minh hoạ**: Một cửa hàng bánh trung thu có giá bán 150,000 VNĐ/hộp, giá vốn 90,000 VNĐ/hộp, giá thanh lý cuối mùa chỉ còn 40,000 VNĐ/hộp.

- $C_u = 150,000 - 90,000 = 60,000$ VNĐ (lợi nhuận mất đi nếu thiếu hàng)
- $C_o = 90,000 - 40,000 = 50,000$ VNĐ (lỗ nếu thừa hàng phải thanh lý)

$$CR = \frac{60,000}{60,000 + 50,000} = \frac{60,000}{110,000} \approx 0.545$$

Điều này có nghĩa doanh nghiệp nên đặt hàng ở mức đủ để đáp ứng khoảng 54.5% khả năng xảy ra của phân phối nhu cầu - nếu nhu cầu tuân theo phân phối chuẩn với trung bình 1,000 hộp và độ lệch chuẩn 200 hộp, tra bảng Z tương ứng phân vị 0.545 (Z ≈ 0.11), ta có $Q^* = 1,000 + 0.11 \times 200 \approx 1,022$ hộp.

**Ứng dụng thực tế**: Mô hình này đặc biệt quan trọng với các ngành hàng thời vụ tại Việt Nam như bánh trung thu, mứt Tết, hàng thời trang theo mùa, hoa dịp lễ - nơi quyết định số lượng đặt hàng ban đầu gần như không thể điều chỉnh sau đó.

---

## III. Ưu điểm & Nhược điểm

### 3.1. Bảng ưu nhược điểm các chiến lược tồn kho

| Chiến lược | Ưu điểm | Nhược điểm |
|---|---|---|
| Tồn kho cao (High Inventory) | Đáp ứng nhanh nhu cầu đột biến, ít rủi ro thiếu hàng | Vốn lưu động bị đóng băng lớn, chi phí lưu kho cao, rủi ro lỗi thời |
| JIT/Tồn kho thấp | Giảm chi phí vốn, giảm lãng phí, tăng vòng quay | Rủi ro gián đoạn cao khi chuỗi cung ứng bất ổn |
| Phân loại ABC | Tập trung nguồn lực hiệu quả vào SKU quan trọng | Cần dữ liệu lịch sử đủ tốt để phân loại chính xác |
| Hệ thống liên tục (Continuous Review) | Phát hiện thiếu hàng sớm, tồn kho an toàn thấp hơn | Đòi hỏi đầu tư hệ thống IT theo dõi thời gian thực |
| Hệ thống định kỳ (Periodic Review) | Đơn giản, dễ triển khai thủ công | Cần tồn kho an toàn cao hơn, độ trễ phát hiện vấn đề |

### 3.2. So sánh chi phí ẩn của tồn kho quá cao vs quá thấp

| Hậu quả | Tồn kho quá cao (Overstock) | Tồn kho quá thấp (Understock) |
|---|---|---|
| Chi phí tài chính | Vốn lưu động bị chôn, tăng chi phí lãi vay | Không tận dụng được chiết khấu số lượng lớn |
| Rủi ro | Hàng lỗi thời, hết hạn, giảm giá thanh lý | Mất doanh số, mất khách hàng, chi phí đặt hàng khẩn cấp |
| Không gian | Cần kho bãi lớn hơn, tăng chi phí thuê/vận hành kho | Không tận dụng hết công suất kho hiện có |
| Ảnh hưởng thương hiệu | Không đáng kể trực tiếp | Nghiêm trọng - mất uy tín "luôn có hàng" |

---

## IV. Case study thực tiễn

### 4.1. Case study quốc tế lớn: Toyota - Hệ thống Kanban và JIT

**Bối cảnh**: Toyota Production System (TPS) phát triển từ thập niên 1950 bởi Taiichi Ohno, với mục tiêu loại bỏ 7 loại lãng phí (muda), trong đó tồn kho dư thừa là một trong những lãng phí lớn nhất.

**Triển khai**: Hệ thống Kanban vật lý (thẻ giấy) điều phối sản xuất giữa các công đoạn, chỉ sản xuất khi có tín hiệu tiêu thụ từ công đoạn sau. Nhà cung cấp giao hàng nhiều lần/ngày ngay tại dây chuyền lắp ráp (line-side delivery), gần như không cần kho trung gian.

**Kết quả**: Vòng quay tồn kho của Toyota thuộc nhóm cao nhất ngành ô tô toàn cầu, giảm đáng kể vốn lưu động bị chôn trong tồn kho so với các đối thủ. Tuy nhiên, sự cố động đất Nhật Bản 2011 và khủng hoảng chip bán dẫn 2021 đã buộc Toyota phải điều chỉnh chiến lược, xây dựng tồn kho đệm chiến lược cho các linh kiện bán dẫn quan trọng (chiến lược học từ trận động đất 2011 giúp Toyota ứng phó khủng hoảng chip 2021 tốt hơn nhiều đối thủ).

### 4.2. Case study Việt Nam lớn: Vinamilk - Quản trị tồn kho nguyên liệu sữa

**Bối cảnh**: Vinamilk cần quản trị tồn kho nguyên liệu sữa tươi (dễ hư hỏng, cần chuỗi lạnh) và sữa bột nhập khẩu (thời gian vận chuyển dài từ New Zealand, Mỹ, châu Âu).

**Giải pháp**: Áp dụng phân loại ABC cho hàng nghìn SKU nguyên vật liệu và bao bì, tập trung kiểm soát chặt nhóm A (sữa bột nguyên liệu, bao bì chính). Xây dựng hệ thống hoạch định nguồn lực doanh nghiệp (ERP) tích hợp dự báo nhu cầu sản xuất với kế hoạch nhập khẩu nguyên liệu (do lead time nhập khẩu 45-60 ngày, cần tồn kho an toàn được tính toán kỹ dựa trên độ biến động nhu cầu và thời gian vận chuyển).

**Kết quả**: Duy trì tỷ lệ đáp ứng đơn hàng cao trong khi tối ưu vốn lưu động, đồng thời giảm thiểu rủi ro hết nguyên liệu sản xuất do biến động chuỗi cung ứng quốc tế.

### 4.3. Case study SME Việt Nam: Cửa hàng vật liệu xây dựng tại Cần Thơ

**Bối cảnh**: Cửa hàng kinh doanh vật liệu xây dựng với hơn 500 mặt hàng khác nhau (xi măng, sắt thép, gạch, sơn, thiết bị vệ sinh), quản lý tồn kho hoàn toàn thủ công bằng sổ sách.

**Vấn đề**: Thường xuyên thiếu hàng bán chạy (xi măng, sắt) trong khi tồn đọng hàng chậm luân chuyển (một số mẫu gạch, thiết bị vệ sinh cũ), gây ứ đọng vốn khoảng 30% giá trị tồn kho vào nhóm hàng bán chậm.

**Giải pháp áp dụng**:
- Phân loại ABC: xác định 15% mặt hàng (xi măng, sắt thép, gạch phổ thông) chiếm 75% doanh thu → nhóm A cần theo dõi sát, đặt hàng thường xuyên.
- Áp dụng công thức EOQ đơn giản cho nhóm A để xác định số lượng đặt hàng tối ưu mỗi lần.
- Thanh lý giảm giá nhóm hàng C tồn đọng lâu (> 6 tháng không bán được) để thu hồi vốn.
- Chuyển sang phần mềm quản lý bán hàng giá rẻ (KiotViet) để theo dõi tồn kho theo thời gian thực thay vì sổ sách.

**Kết quả**: Sau 6 tháng, tỷ lệ hết hàng nhóm A giảm từ 15% xuống dưới 5%, vốn lưu động ứ đọng ở nhóm C giảm 20% nhờ thanh lý và kiểm soát đặt hàng chặt chẽ hơn.

### 4.4. Case study quốc tế - thất bại: Zara thời kỳ đầu và bài học tồn kho theo mùa

**Bối cảnh**: Nhiều thương hiệu thời trang truyền thống (không phải Zara ở giai đoạn trưởng thành) áp dụng mô hình dự báo và đặt hàng trước cả mùa (6 tháng trước), dẫn đến rủi ro lớn khi xu hướng thời trang thay đổi nhanh.

**Vấn đề điển hình trong ngành**: Nhiều nhà bán lẻ thời trang phải giảm giá tới 50-70% để xả hàng tồn kho cuối mùa do dự báo sai xu hướng, gây thiệt hại lớn về lợi nhuận.

**Bài học**: Đây là lý do các mô hình hiện đại (như Zara đã áp dụng - xem case study ở file 03) chuyển sang chiến lược sản xuất theo lô nhỏ, phản hồi nhanh theo dữ liệu bán hàng thực tế, giảm tồn kho theo mùa dự đoán trước, thay vào đó là tồn kho linh hoạt điều chỉnh liên tục trong mùa.

### 4.5. Case study Việt Nam SME - dịch vụ: Nhà thuốc tư nhân quản lý tồn kho thuốc theo hạn sử dụng

**Bối cảnh**: Chuỗi 8 nhà thuốc tư nhân tại Hà Nội gặp vấn đề thuốc hết hạn sử dụng phải tiêu huỷ, gây thiệt hại tài chính và vi phạm quy định dược phẩm nếu không xử lý đúng cách.

**Giải pháp**:
- Áp dụng nguyên tắc FEFO (First Expired First Out) thay vì FIFO thông thường - ưu tiên bán thuốc có hạn sử dụng gần nhất trước.
- Thiết lập cảnh báo tự động trên phần mềm quản lý khi thuốc còn 3 tháng đến hạn, kích hoạt chương trình khuyến mãi hoặc chuyển hàng giữa các chi nhánh có nhu cầu cao hơn.
- Giảm số lượng đặt hàng mỗi lần đối với thuốc có vòng đời ngắn, tăng tần suất đặt hàng.

**Kết quả**: Tỷ lệ thuốc phải tiêu huỷ do hết hạn giảm từ 4% xuống dưới 1% giá trị tồn kho, tiết kiệm đáng kể chi phí và giảm rủi ro pháp lý.

### 4.6. Bảng tổng hợp bài học từ các case study

| Case study | Công cụ áp dụng | Bài học chính |
|---|---|---|
| Toyota | JIT, Kanban | JIT hiệu quả nhưng cần tồn kho đệm chiến lược cho rủi ro hệ thống (chip, thiên tai) |
| Vinamilk | ABC + ERP + Safety Stock | Kết hợp phân loại ABC với tính toán an toàn tồn kho khoa học cho nguyên liệu nhập khẩu |
| Cửa hàng VLXD Cần Thơ | ABC + EOQ đơn giản | SME có thể áp dụng công cụ cơ bản (ABC, EOQ) hiệu quả mà không cần hệ thống phức tạp |
| Ngành thời trang truyền thống | (Bài học thất bại) | Tồn kho theo mùa dự đoán trước rủi ro cao trong ngành biến động nhanh |
| Chuỗi nhà thuốc Hà Nội | FEFO | Ngành hàng có hạn sử dụng cần nguyên tắc xuất kho đặc thù (FEFO thay vì FIFO) |

---

## V. Phương pháp triển khai từng bước

### 5.1. Quy trình 6 bước xây dựng hệ thống quản trị tồn kho

```
Bước 1: Thu thập dữ liệu lịch sử
   │  Nhu cầu, lead time, chi phí đặt hàng, chi phí lưu kho từng SKU
   ▼
Bước 2: Phân loại ABC toàn bộ danh mục
   │  Xác định nhóm ưu tiên quản trị
   ▼
Bước 3: Tính toán EOQ và Safety Stock cho từng nhóm/SKU quan trọng
   │  Áp dụng công thức phù hợp mức độ biến động nhu cầu
   ▼
Bước 4: Lựa chọn hệ thống kiểm soát (liên tục/định kỳ)
   │  Dựa trên khả năng đầu tư IT và đặc thù ngành hàng
   ▼
Bước 5: Triển khai công cụ theo dõi (phần mềm/Excel có cấu trúc)
   │  Thiết lập cảnh báo tự động khi chạm ROP
   ▼
Bước 6: Kiểm kê định kỳ & Điều chỉnh liên tục
      Cycle counting, đối chiếu số liệu, cập nhật lại thông số EOQ/SS định kỳ
```

### 5.2. Bảng các sai lầm thường gặp

| Sai lầm | Hậu quả | Cách phòng tránh |
|---|---|---|
| Áp dụng cùng chính sách tồn kho cho mọi SKU | Lãng phí nguồn lực quản trị cho hàng ít quan trọng | Phân loại ABC, ưu tiên nguồn lực theo nhóm |
| Không tính đến biến động nhu cầu khi tính Safety Stock | Thiếu hàng thường xuyên dù có "dự trữ" | Sử dụng công thức SS dựa trên độ lệch chuẩn và Z-score |
| Copy công thức EOQ máy móc không xét ràng buộc thực tế | Đặt hàng số lượng không khả thi (quá lớn so với kho chứa) | Điều chỉnh EOQ theo ràng buộc thực tế (MOQ của NCC, sức chứa kho) |
| Không kiểm kê định kỳ | Số liệu hệ thống sai lệch so với thực tế, mất kiểm soát | Thực hiện cycle counting theo tần suất ABC |
| Theo đuổi JIT tuyệt đối mà không đánh giá rủi ro chuỗi cung ứng | Dễ tổn thương khi gián đoạn nguồn cung | Đánh giá rủi ro theo Kraljic, giữ buffer cho hàng quan trọng |

---

## VI. Quy mô áp dụng – SME vs Doanh nghiệp lớn

### 6.1. Bảng so sánh mức độ áp dụng

| Thành phần | SME | Doanh nghiệp lớn |
|---|---|---|
| Phân loại ABC | Thực hiện thủ công trên Excel, 1-2 lần/năm | Tự động hoá trong ERP, cập nhật liên tục |
| Tính EOQ/Safety Stock | Công thức cơ bản, ước lượng thủ công | Mô hình thống kê nâng cao, tính riêng theo SKU |
| Hệ thống kiểm soát | Định kỳ (periodic review) phổ biến | Liên tục (continuous review) với hệ thống mã vạch/RFID |
| Kiểm kê | Kiểm kê toàn bộ 1-2 lần/năm | Cycle counting liên tục theo ABC |
| Công nghệ | Phần mềm bán hàng đơn giản (KiotViet, Sapo) | WMS (Warehouse Management System) chuyên dụng |

### 6.2. Chi phí đầu tư theo giai đoạn phát triển

| Giai đoạn | Công cụ tồn kho | Chi phí ước tính (VNĐ) |
|---|---|---|
| Khởi nghiệp | Sổ sách, Excel cơ bản | 0 - 5 triệu |
| Tăng trưởng | Phần mềm bán hàng có module tồn kho | 5 - 50 triệu/năm |
| Mở rộng | WMS cơ bản, mã vạch, tích hợp ERP nhỏ | 100 triệu - 1 tỷ |
| Doanh nghiệp lớn | WMS/ERP toàn diện, RFID, tự động hoá kho | 2 - 20+ tỷ |

### 6.3. Bảng sai lầm phổ biến theo quy mô

| Quy mô | Sai lầm phổ biến |
|---|---|
| SME | Không phân loại ABC, quản lý đồng đều mọi mặt hàng gây lãng phí nguồn lực |
| SME | Không tính Safety Stock khoa học, dựa hoàn toàn vào cảm tính |
| Doanh nghiệp lớn | Đầu tư hệ thống IT phức tạp nhưng thiếu quy trình quản trị dữ liệu chuẩn, dẫn đến "rác vào, rác ra" (garbage in, garbage out) |
| Doanh nghiệp lớn | Tồn kho an toàn được thiết lập một lần rồi không cập nhật theo biến động thị trường thực tế |
| Doanh nghiệp lớn | Đầu tư RFID/IoT nhưng thiếu tích hợp dữ liệu xuyên suốt các bộ phận, gây lãng phí đầu tư |

---

## VII. Công cụ & Templates hỗ trợ

### 7.1. Bảng công cụ phần mềm

| Công cụ | Chức năng | Chi phí ước tính | Phù hợp |
|---|---|---|---|
| Excel với công thức EOQ/SS | Tính toán cơ bản | Miễn phí | SME nhỏ |
| KiotViet, Sapo | Quản lý bán hàng + tồn kho cơ bản | 3-10 triệu/năm | SME bán lẻ |
| Odoo Inventory | WMS module trong ERP mã nguồn mở | 50-150 triệu/năm | SME vừa |
| SAP EWM, Oracle WMS | Quản lý kho chuyên sâu, tích hợp RFID | Hàng tỷ/năm | Doanh nghiệp lớn |

### 7.2. Template: Bảng tính EOQ và Safety Stock

```
SKU: _______________  Nhu cầu năm (D): _______  Chi phí đặt hàng (S): _______
Chi phí lưu kho/năm (H): _______  Lead Time (L, ngày): _______

EOQ = √(2 × D × S / H) = _______________
Số lần đặt hàng/năm = D / EOQ = _______________
Nhu cầu TB/ngày (d) = D / số ngày làm việc = _______________
Độ lệch chuẩn nhu cầu ngày (σd) = _______________
Mức phục vụ mong muốn: ____% → Hệ số Z = _______________
Safety Stock = Z × σd × √L = _______________
Reorder Point (ROP) = d×L + SS = _______________
```

### 7.3. Sơ đồ quyết định hệ thống kiểm soát tồn kho

```
                    Bắt đầu
                       │
        Có hệ thống IT theo dõi thời gian thực?
                /              \
             Có                Không
              │                   │
   SKU giá trị cao (nhóm A)?   HỆ THỐNG ĐỊNH KỲ
      /            \            (Periodic Review)
    Có             Không
     │                │
HỆ THỐNG LIÊN TỤC   Xem xét chuyển
(Continuous Review,  đổi số hoặc giữ
 ROP tự động)        định kỳ với tần
                     suất cao hơn
```

---

## VIII. Bài tập thực hành

1. Tính EOQ cho một sản phẩm thực tế của doanh nghiệp bạn với dữ liệu D, S, H tự thu thập hoặc ước lượng hợp lý.
2. Tính Safety Stock và ROP cho sản phẩm đó với 3 mức độ phục vụ khác nhau (90%, 95%, 99%), so sánh và giải thích sự đánh đổi chi phí.
3. Thực hiện phân loại ABC cho danh mục tối thiểu 20 SKU, vẽ biểu đồ Pareto minh hoạ.
4. Phân tích một trường hợp hết hàng (stockout) bạn từng gặp, xác định nguyên nhân có thể do ROP tính sai, Safety Stock không đủ, hay lead time thực tế dài hơn dự kiến.
5. So sánh chi phí vòng quay tồn kho hiện tại của doanh nghiệp bạn với trung bình ngành, đề xuất cải tiến.
6. Thiết kế quy trình cycle counting cho danh mục đã phân loại ABC ở bài tập 3.
7. Nghiên cứu case Toyota và khủng hoảng chip 2021, viết phân tích về đánh đổi giữa JIT thuần tuý và tồn kho đệm chiến lược.
8. Áp dụng nguyên tắc FEFO cho một ngành hàng có hạn sử dụng (thực phẩm, dược phẩm, mỹ phẩm) mà bạn quen thuộc.
9. Xây dựng bảng theo dõi tồn kho mẫu trên Excel với công thức tự động cảnh báo khi chạm ROP.
10. Đề xuất lộ trình chuyển đổi từ hệ thống kiểm soát định kỳ sang liên tục cho một SME giả định, bao gồm chi phí đầu tư ước tính.
11. Áp dụng mô hình Newsvendor để xác định số lượng đặt hàng tối ưu cho một sản phẩm thời vụ (bánh trung thu, mứt Tết, hoa lễ) với dữ liệu giá bán, giá vốn, giá thanh lý tự giả định hợp lý.
12. Phân tích một tình huống thực tế về "bán ảo" (oversell) trên sàn thương mại điện tử do đồng bộ tồn kho kém, đề xuất giải pháp kỹ thuật và quy trình khắc phục.
13. So sánh chi phí và lợi ích của việc đầu tư RFID so với mã vạch truyền thống cho một chuỗi bán lẻ giả định có 20 cửa hàng.
14. Tính toán nguyên lý gộp rủi ro (Risk Pooling): giả sử 3 kho khu vực có độ lệch chuẩn nhu cầu riêng lẻ, so sánh tổng Safety Stock cần thiết nếu gộp về 1 kho trung tâm so với duy trì 3 kho riêng biệt.

---

## IX. Phụ lục

### 9.1. Bảng thuật ngữ (Glossary)

| Thuật ngữ | Giải thích |
|---|---|
| EOQ | Economic Order Quantity - số lượng đặt hàng kinh tế tối ưu |
| ROP | Reorder Point - điểm đặt hàng lại |
| Safety Stock | Tồn kho an toàn, dự phòng biến động nhu cầu/lead time |
| ABC Analysis | Phân loại hàng hoá theo giá trị đóng góp (nguyên lý Pareto) |
| JIT | Just-In-Time - hệ thống sản xuất/cung ứng đúng lúc |
| Kanban | Thẻ tín hiệu điều phối sản xuất theo hệ thống kéo |
| Cycle Counting | Kiểm kê tồn kho theo chu kỳ, không kiểm toàn bộ một lần |
| FEFO | First Expired First Out - xuất hàng có hạn sử dụng gần nhất trước |
| DIO | Days of Inventory Outstanding - số ngày tồn kho bình quân |
| Newsvendor Model | Mô hình xác định số lượng đặt hàng tối ưu cho sản phẩm bán theo một chu kỳ duy nhất |
| Risk Pooling | Nguyên lý gộp rủi ro giúp giảm tổng tồn kho an toàn khi tập trung hoá kho |
| VMI | Vendor Managed Inventory - nhà cung cấp quản lý tồn kho tại kho khách hàng |
| Consignment Inventory | Tồn kho ký gửi - NCC giữ quyền sở hữu hàng đến khi khách hàng sử dụng/bán |

### 9.2. Bảng đo lường KPI tồn kho

| KPI | Công thức | Mục tiêu tham khảo |
|---|---|---|
| Vòng quay tồn kho | COGS / Tồn kho bình quân | Theo ngành, càng cao càng tốt |
| Tỷ lệ hết hàng (Stockout Rate) | Số lần hết hàng / Tổng số lần kiểm tra | < 5% |
| Độ chính xác tồn kho (Inventory Accuracy) | Số SKU khớp giữa hệ thống và thực tế / Tổng SKU | > 95% |
| Tỷ lệ hàng lỗi thời (Obsolete Inventory %) | Giá trị hàng tồn > 6-12 tháng / Tổng tồn kho | < 5% |
| Tỷ lệ đáp ứng đơn hàng (Fill Rate) | Số đơn hàng đáp ứng đầy đủ / Tổng số đơn hàng | > 95% |
| Chi phí lưu kho trên doanh thu | Tổng chi phí lưu kho / Doanh thu | 2-6% tuỳ ngành |

### 9.3. Sổ tay rủi ro tồn kho (Risk Register mẫu)

| Rủi ro | Xác suất | Tác động | Biện pháp giảm thiểu |
|---|---|---|---|
| Dự báo nhu cầu sai lệch lớn | Trung bình | Cao | Cải thiện mô hình dự báo, theo dõi sát biến động thị trường |
| NCC giao hàng trễ | Trung bình | Trung bình | Tăng Safety Stock, đa dạng hoá NCC |
| Hàng hoá lỗi thời/hết hạn | Thấp-Trung bình | Trung bình | FEFO, cảnh báo tự động, chương trình thanh lý sớm |
| Sai lệch số liệu hệ thống vs thực tế | Trung bình | Trung bình | Cycle counting thường xuyên |
| Oversell trên kênh thương mại điện tử | Trung bình | Trung bình | Đồng bộ tồn kho real-time giữa các kênh bán |
| Biến động giá nguyên liệu đầu vào | Cao | Trung bình | Hợp đồng giá cố định ngắn hạn, theo dõi thị trường |

### 9.4. Bảng tham chiếu nhanh các công thức cốt lõi

| Mục tiêu | Công thức |
|---|---|
| Số lượng đặt hàng tối ưu | $EOQ = \sqrt{2DS/H}$ |
| Điểm đặt hàng lại | $ROP = d \times L + SS$ |
| Tồn kho an toàn | $SS = Z \times \sigma_d \times \sqrt{L}$ |
| Tỷ lệ phục vụ tối ưu (Newsvendor) | $CR = C_u / (C_u + C_o)$ |
| Vòng quay tồn kho | $COGS / \text{Tồn kho bình quân}$ |

---

## X. Tài liệu tham khảo

### Sách tham khảo
1. Silver, E. A., Pyke, D. F., & Peterson, R. (1998). *Inventory Management and Production Planning and Scheduling*. Wiley.
2. Chopra, S. & Meindl, P. (2019). *Supply Chain Management: Strategy, Planning, and Operation*. Pearson.
3. Ohno, T. (1988). *Toyota Production System: Beyond Large-Scale Production*. Productivity Press.
4. Slack, N., Brandon-Jones, A., & Johnston, R. (2016). *Operations Management*. Pearson.
5. Nahmias, S. & Olsen, T. L. (2015). *Production and Operations Analysis*. Waveland Press.

### Liên kết nội bộ (Internal Cross-links)
- [01-process-design-analysis.md](./01-process-design-analysis.md) - Nền tảng thiết kế quy trình liên quan tồn kho.
- [03-supply-chain-management.md](./03-supply-chain-management.md) - Bullwhip Effect và mối liên hệ với biến động tồn kho.
- [05-capacity-planning.md](./05-capacity-planning.md) - Hoạch định năng lực sản xuất gắn với chiến lược tồn kho.
- [07-forecasting.md](./07-forecasting.md) - Dự báo nhu cầu là đầu vào quan trọng cho mọi công thức tồn kho trong file này.

### Nguồn học trực tuyến
- ASCM CPIM (Certified in Production and Inventory Management) - chứng chỉ chuyên sâu về quản trị tồn kho.
- Coursera: "Supply Chain Logistics" - Rutgers University.
- APICS Dictionary - thuật ngữ chuẩn ngành quản trị tồn kho và sản xuất.

### Ghi chú kết thúc file

File này tập trung vào các công thức định lượng cốt lõi (EOQ, Safety Stock, ROP, Newsvendor Model) kết hợp với các case study thực tiễn tại Việt Nam và quốc tế. Người đọc nên thực hành tính toán trực tiếp trên dữ liệu thực tế của doanh nghiệp mình để hiểu sâu hơn thay vì chỉ ghi nhớ công thức lý thuyết. Phần Phụ lục bổ sung về công nghệ (RFID, omnichannel, risk pooling) phản ánh xu hướng chuyển đổi số đang diễn ra mạnh mẽ trong quản trị tồn kho hiện đại tại cả doanh nghiệp lớn và SME Việt Nam.

---

## Phụ lục bổ sung: Công nghệ và xu hướng quản trị tồn kho hiện đại

### A.1. Vai trò của mã vạch (Barcode) và RFID trong quản trị tồn kho

| Công nghệ | Cách hoạt động | Ưu điểm | Nhược điểm | Chi phí đầu tư |
|---|---|---|---|---|
| Mã vạch (Barcode) | Quét từng mã một để ghi nhận nhập/xuất | Chi phí thấp, dễ triển khai | Phải quét từng đơn vị, tốn nhân công | 5-20 triệu (máy quét + phần mềm) |
| RFID (Radio Frequency ID) | Đọc nhiều thẻ cùng lúc qua sóng radio, không cần quét trực tiếp | Tốc độ kiểm kê nhanh gấp nhiều lần, giảm nhân công | Chi phí thẻ và đầu đọc cao hơn | 100 triệu - vài tỷ tuỳ quy mô |
| IoT Sensor | Cảm biến theo dõi điều kiện bảo quản (nhiệt độ, độ ẩm) theo thời gian thực | Phù hợp hàng hoá nhạy cảm (thực phẩm, dược phẩm) | Cần hạ tầng kết nối và bảo trì | Tuỳ quy mô, thường 200 triệu trở lên |

Doanh nghiệp lớn như Decathlon, Uniqlo đã triển khai RFID toàn bộ chuỗi cửa hàng để kiểm kê chỉ trong vài giờ thay vì vài ngày như phương pháp thủ công, đồng thời giảm đáng kể tỷ lệ sai lệch tồn kho giữa hệ thống và thực tế.

### A.2. Quản trị tồn kho đa kênh (Omnichannel Inventory Management)

Với sự phát triển của bán hàng đa kênh (cửa hàng vật lý, website, sàn thương mại điện tử, mạng xã hội), doanh nghiệp bán lẻ hiện đại phải giải quyết bài toán:

- **Tồn kho hợp nhất (Unified Inventory)**: một nguồn dữ liệu tồn kho duy nhất cho tất cả các kênh bán, tránh tình trạng bán trùng một sản phẩm trên nhiều kênh khi chỉ còn 1 đơn vị tồn kho thực tế.
- **Ship-from-store**: sử dụng tồn kho tại cửa hàng để giao đơn hàng online gần khách hàng nhất, giảm thời gian giao hàng và tận dụng tồn kho phân tán.
- **Click-and-Collect**: khách đặt online, nhận tại cửa hàng - đòi hỏi đồng bộ tồn kho thời gian thực giữa kênh online và offline.

**Thách thức phổ biến**: Nhiều doanh nghiệp Việt Nam giai đoạn đầu chuyển đổi số gặp tình trạng "bán ảo" (oversell) trên sàn thương mại điện tử do tồn kho online không đồng bộ real-time với tồn kho vật lý tại cửa hàng, dẫn đến huỷ đơn hàng và ảnh hưởng uy tín gian hàng.

### A.3. Tồn kho ký gửi (Consignment Inventory) và Vendor Managed Inventory (VMI)

**Tồn kho ký gửi (Consignment Inventory)**: nhà cung cấp giao hàng đến kho của khách hàng nhưng vẫn giữ quyền sở hữu hàng hoá cho đến khi khách hàng thực sự sử dụng/bán được. Khách hàng không phải trả tiền trước, giảm áp lực vốn lưu động; nhà cung cấp chịu rủi ro tồn kho nhưng đổi lại có được đơn hàng ổn định và mối quan hệ dài hạn.

**VMI (Vendor Managed Inventory)**: nhà cung cấp trực tiếp theo dõi và quyết định mức bổ sung tồn kho tại kho của khách hàng, dựa trên dữ liệu bán hàng/tiêu thụ được chia sẻ thời gian thực. Đây là mô hình hợp tác sâu giúp giảm hiệu ứng Bullwhip (đã phân tích ở file 03), phổ biến trong quan hệ giữa các nhà bán lẻ lớn (Walmart) và nhà cung cấp chiến lược (P&G).

### A.4. Bài toán tồn kho trong thương mại điện tử: Fulfillment và Kho hàng phân tán

Các sàn thương mại điện tử lớn (Shopee, Lazada, Tiki, Amazon) và các nhà bán hàng online quy mô vừa phải giải quyết bài toán tồn kho theo mô hình mạng lưới kho phân tán (distributed fulfillment network):

```
Mô hình kho tập trung (Centralized)         Mô hình kho phân tán (Distributed)

        ┌─────────┐                          ┌────┐   ┌────┐   ┌────┐
        │  Kho     │                          │Kho │   │Kho │   │Kho │
        │ Trung tâm│                          │Bắc │   │Trung│  │Nam │
        └────┬────┘                          └─┬──┘   └─┬──┘   └─┬──┘
             │                                  │        │        │
    ┌────────┼────────┐                        ▼        ▼        ▼
    ▼        ▼         ▼                 Khách hàng Khách hàng Khách hàng
 KH Bắc   KH Trung   KH Nam                  Bắc      Trung      Nam
(giao xa,               (giao nhanh hơn, chi phí vận
 chi phí vận             chuyển thấp hơn, nhưng cần
 chuyển cao)              quản lý tồn kho phức tạp hơn
                          ở nhiều địa điểm)
```

Đánh đổi chính: kho tập trung giúp đơn giản hoá quản trị và giảm tổng tồn kho an toàn cần thiết (nhờ hiệu ứng gộp - risk pooling), nhưng kho phân tán giúp giảm thời gian và chi phí giao hàng chặng cuối (last-mile delivery). Doanh nghiệp thương mại điện tử lớn tại Việt Nam thường áp dụng mô hình lai: kho trung tâm cho hàng chậm luân chuyển, kho vệ tinh khu vực cho hàng bán chạy cần giao nhanh.

### A.5. Nguyên lý gộp rủi ro tồn kho (Risk Pooling)

Nguyên lý này giải thích tại sao tổng tồn kho an toàn cần thiết khi gộp chung tại một kho trung tâm thường thấp hơn tổng tồn kho an toàn nếu duy trì riêng lẻ tại nhiều kho khu vực, do độ biến động nhu cầu tổng hợp (aggregate demand) thường thấp hơn tổng độ biến động của từng khu vực riêng lẻ (nhờ hiệu ứng bù trừ thống kê giữa các khu vực có nhu cầu không hoàn toàn tương quan với nhau).

$$SS_{\text{gộp}} < \sum SS_{\text{riêng lẻ}} \quad \text{khi các khu vực có tương quan nhu cầu} < 1$$

Đây là cơ sở lý thuyết cho quyết định tập trung hoá kho ở nhiều doanh nghiệp bán lẻ, đặc biệt phù hợp với hàng hoá có nhu cầu biến động lớn và không yêu cầu giao hàng siêu tốc.

### A.6. Tồn kho và mối liên hệ với báo cáo tài chính doanh nghiệp

Quản trị tồn kho không chỉ là bài toán vận hành mà còn ảnh hưởng trực tiếp đến các chỉ số tài chính quan trọng mà nhà đầu tư và ngân hàng thường xem xét:

| Chỉ số tài chính | Công thức | Ảnh hưởng của tồn kho |
|---|---|---|
| Vốn lưu động ròng (Net Working Capital) | Tài sản ngắn hạn - Nợ ngắn hạn | Tồn kho cao làm tăng tài sản ngắn hạn nhưng "chôn" tiền mặt |
| Chu kỳ chuyển đổi tiền mặt (Cash Conversion Cycle) | DIO + DSO - DPO | Giảm DIO (số ngày tồn kho) giúp rút ngắn chu kỳ, cải thiện dòng tiền |
| Tỷ suất sinh lời trên tài sản (ROA) | Lợi nhuận ròng / Tổng tài sản | Tồn kho dư thừa làm tăng mẫu số, giảm ROA dù lợi nhuận không đổi |
| Rủi ro giảm giá trị tài sản (Inventory Write-down) | Giá trị sổ sách - Giá trị thị trường (nếu thấp hơn) | Hàng lỗi thời phải trích lập dự phòng giảm giá hàng tồn kho theo chuẩn kế toán |

Đây là lý do các giám đốc tài chính (CFO) và giám đốc vận hành (COO) cần phối hợp chặt chẽ trong việc thiết lập chính sách tồn kho - không chỉ nhìn từ góc độ đáp ứng nhu cầu khách hàng mà còn từ góc độ hiệu quả sử dụng vốn của toàn doanh nghiệp. Việc trích lập dự phòng giảm giá hàng tồn kho (theo Thông tư 48/2019/TT-BTC tại Việt Nam) cũng là một hệ quả kế toán trực tiếp của việc quản trị tồn kho kém hiệu quả, ảnh hưởng đến lợi nhuận báo cáo của doanh nghiệp.
