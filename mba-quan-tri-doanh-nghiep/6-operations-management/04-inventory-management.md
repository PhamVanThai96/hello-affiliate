# 04. Quản trị Tồn kho (Inventory Management)

> **Mục tiêu**: Giúp người học (kể cả người mới) hiểu *bản chất* của quản trị tồn kho - bài toán cân bằng giữa chi phí giữ hàng và rủi ro hết hàng - và biết tính toán, áp dụng các công cụ cốt lõi (EOQ, ROP, Safety Stock, ABC, JIT, Newsvendor) cho doanh nghiệp vừa và nhỏ (SME) tại Việt Nam.

> File thuộc bộ kiến thức Quản trị Vận hành (Operations Management) - MBA Knowledge Base
> Liên kết: [01-process-design-analysis.md](./01-process-design-analysis.md) | [03-supply-chain-management.md](./03-supply-chain-management.md) | [05-capacity-planning.md](./05-capacity-planning.md)

> **Quy ước số liệu**: Các con số ghi "giả định minh họa" là số tự thiết kế để làm rõ cách tính, KHÔNG phải số liệu thật của doanh nghiệp được nhắc tên. Dữ kiện lịch sử/doanh nghiệp quốc tế đã được giữ ở mức khái quát; chi tiết định lượng chưa kiểm chứng nguồn được ghi rõ "ước tính".

---

## MỤC LỤC

- [I. Khái niệm & Lý thuyết](#i-khái-niệm--lý-thuyết)
- [II. Chi tiết từng thành phần (công cụ/kỹ thuật)](#ii-chi-tiết-từng-thành-phần-công-cụkỹ-thuật)
- [III. Case Studies thực tế](#iii-case-studies-thực-tế)
- [IV. Ứng dụng cho SME](#iv-ứng-dụng-cho-sme)
- [V. Tools & Templates](#v-tools--templates)
- [VI. Bài tập thực hành](#vi-bài-tập-thực-hành)
- [PHỤ LỤC: CHECKLIST QUẢN TRỊ TỒN KHO TỔNG HỢP](#phụ-lục-checklist-quản-trị-tồn-kho-tổng-hợp)
- [TÀI LIỆU THAM KHẢO](#tài-liệu-tham-khảo)

---

## I. Khái niệm & Lý thuyết

### 1.1. Định nghĩa và vai trò của tồn kho

**Tồn kho (Inventory)** là toàn bộ nguyên vật liệu, bán thành phẩm, thành phẩm mà doanh nghiệp lưu giữ để phục vụ sản xuất hoặc bán hàng trong tương lai. Về mặt tài chính, tồn kho là một khoản đầu tư: tiền mặt đã chi ra nhưng chưa thu về, tức vốn lưu động bị "đóng băng" trên kệ và trong kho. Vì vậy quản trị tồn kho thực chất là bài toán **cân bằng giữa hai nỗi sợ đối lập**: sợ hết hàng (mất khách, mất doanh số) và sợ thừa hàng (chôn vốn, hư hỏng, lỗi thời).

**Tại sao doanh nghiệp vẫn phải giữ tồn kho (thay vì "có đơn mới mua")?** Có 5 lý do kinh tế cơ bản:

| Lý do | Giải thích | Ví dụ |
|---|---|---|
| Tách rời cung - cầu (Decoupling) | Nhà cung cấp giao theo lô, khách hàng mua lẻ liên tục, cần "bể chứa" ở giữa | Cửa hàng mua 1 xe tải xi măng, bán từng bao |
| Thời gian giao hàng (Lead time) | Hàng đặt hôm nay chưa về ngay, phải có hàng bán trong lúc chờ | Sữa bột nhập mất 45-60 ngày |
| Biến động nhu cầu/nguồn cung | Nhu cầu và lead time không cố định, cần vùng đệm | Mưa lớn làm tăng nhu cầu tôn, ngói |
| Kinh tế theo quy mô | Mua/sản xuất lô lớn rẻ hơn (chiết khấu, ít chi phí đặt hàng) | Chiết khấu khi mua từ 1.000 cái |
| Đầu cơ/mùa vụ | Tích trữ trước mùa cao điểm hoặc trước khi giá tăng | Bánh trung thu, hàng Tết |

**Bốn loại tồn kho chính theo mục đích**:

| Loại tồn kho | Mục đích | Ví dụ |
|---|---|---|
| Tồn kho chu kỳ (Cycle Stock) | Đáp ứng nhu cầu bình thường giữa 2 lần đặt hàng | Hàng đặt định kỳ hàng tuần |
| Tồn kho an toàn (Safety Stock) | Phòng ngừa biến động nhu cầu hoặc lead time | Dự trữ thêm cho mức phục vụ 95% |
| Tồn kho theo mùa (Seasonal Stock) | Đáp ứng nhu cầu tăng đột biến theo mùa vụ | Bánh trung thu, hàng Tết |
| Tồn kho trong chuyển (Pipeline/Transit Stock) | Hàng đang vận chuyển giữa các mắt xích | Hàng trên tàu biển từ Trung Quốc về Việt Nam |

Ngoài ra, trong sản xuất, tồn kho còn được phân theo hình thái: nguyên vật liệu (Raw Materials), sản phẩm dở dang (Work-in-Process - WIP), thành phẩm (Finished Goods) và vật tư bảo trì/sửa chữa (MRO).

### 1.2. Chi phí liên quan đến tồn kho

**Vấn đề kinh doanh**: Nếu chỉ quan tâm "mua rẻ" hoặc "luôn đủ hàng", doanh nghiệp sẽ ra quyết định lệch. Muốn quyết định tối ưu phải nhìn đồng thời 3 nhóm chi phí đối lập nhau:

1. **Chi phí đặt hàng (Ordering Cost - S)**: chi phí phát sinh *mỗi lần* đặt hàng, không phụ thuộc số lượng đặt (hành chính, vận chuyển cố định, kiểm tra nhận hàng). Đặt ít lần, mỗi lần nhiều hàng giúp giảm tổng chi phí đặt hàng.
2. **Chi phí lưu kho (Holding/Carrying Cost - H)**: chi phí giữ hàng, gồm chi phí vốn (cơ hội hoặc lãi vay), kho bãi, bảo hiểm, hao hụt, lỗi thời. Thường tính bằng 15-30% giá trị hàng tồn mỗi năm (ước tính tham khảo; với hàng dễ hỏng có thể cao hơn). Nếu giá mua một đơn vị là $P$ và tỷ lệ lưu kho là $i$ thì $H = i \times P$.
3. **Chi phí thiếu hàng (Stockout/Shortage Cost)**: mất doanh số, mất khách hàng, phạt hợp đồng, chi phí đặt hàng khẩn cấp. Đây là chi phí khó đo nhất nên thường được quy đổi gián tiếp qua "mức độ phục vụ" (Service Level).

Hai nhóm chi phí đầu *đối nghịch*: đặt lô lớn thì chi phí đặt hàng giảm nhưng chi phí lưu kho tăng và ngược lại. Điểm tối ưu nằm ở chỗ hai đường cắt nhau.

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

### 1.3. Mô hình EOQ (Economic Order Quantity)

#### 1.3.1. Nguồn gốc

EOQ do **Ford W. Harris** công bố năm **1913** trong bài báo "How Many Parts to Make at Once" (tạp chí *Factory, The Magazine of Management*), khi các nhà máy Mỹ đầu thế kỷ 20 đứng trước câu hỏi thực tế: mỗi lần chuyển máy sang sản xuất một loại chi tiết tốn thời gian và tiền chuẩn bị (setup), vậy nên sản xuất lô lớn cỡ nào? Công thức được **R. H. Wilson** phổ biến rộng rãi từ năm 1934 nên còn gọi là "công thức Wilson". Đây là mô hình toán học quản trị tồn kho lâu đời nhất vẫn còn dùng.

#### 1.3.2. Logic xây dựng công thức (tại sao có căn bậc hai?)

Giả định (mô hình cơ bản): nhu cầu $D$ ổn định, biết trước; lead time cố định; toàn bộ lô $Q$ về cùng lúc; không cho phép thiếu hàng; giá mua không đổi theo số lượng.

Khi đó tồn kho dao động từ $Q$ (vừa nhập) về 0 (vừa hết) theo hình răng cưa, nên **tồn kho bình quân là $Q/2$**:

```
Tồn kho
  Q │╲    ╲    ╲    ╲        Tồn kho bình quân = Q/2
    │ ╲    ╲    ╲    ╲
    │  ╲    ╲    ╲    ╲
  0 └───┴────┴────┴────┴──▶ Thời gian
     (mỗi chu kỳ dài T = Q/D năm, mỗi lần hết hàng thì hàng mới về)
```

- Chi phí đặt hàng một năm = (số lần đặt) × S = $\frac{D}{Q} \times S$
- Chi phí lưu kho một năm = (tồn kho bình quân) × H = $\frac{Q}{2} \times H$
- Tổng chi phí biến đổi: $TC(Q) = \frac{D}{Q}S + \frac{Q}{2}H$

Lấy đạo hàm theo $Q$ và cho bằng 0: $-\frac{DS}{Q^2} + \frac{H}{2} = 0 \Rightarrow Q^2 = \frac{2DS}{H}$. Ý nghĩa: **tại điểm tối ưu, chi phí đặt hàng bằng chi phí lưu kho** ($\frac{D}{Q}S = \frac{Q}{2}H$). Đó cũng là điểm hai đường trong biểu đồ 1.2 cắt nhau.

**Công thức EOQ**:

$$EOQ = Q^* = \sqrt{\frac{2DS}{H}}$$

Trong đó:
- $D$ = Nhu cầu hàng năm (Annual Demand, đơn vị/năm)
- $S$ = Chi phí đặt hàng mỗi lần (Ordering Cost per order)
- $H$ = Chi phí lưu kho mỗi đơn vị mỗi năm (Holding Cost per unit per year)

**Các chỉ số đi kèm**:

$$N^* = \frac{D}{Q^*} \quad \text{(số lần đặt hàng tối ưu mỗi năm)}$$

$$T^* = \frac{\text{Số ngày làm việc trong năm}}{N^*} \quad \text{(chu kỳ đặt hàng tối ưu, ngày)}$$

$$TC^* = \sqrt{2DSH} \quad \text{(tổng chi phí tồn kho biến đổi tối ưu mỗi năm)}$$

**Hàm ý quan trọng của căn bậc hai**: Nhu cầu $D$ tăng gấp 4 lần thì EOQ chỉ tăng gấp 2 lần; chi phí đặt hàng $S$ tăng gấp 4 thì EOQ chỉ tăng gấp 2. Do đó EOQ khá "bền" trước sai số ước lượng, như bảng độ nhạy dưới đây chỉ ra.

#### 1.3.3. Ví dụ từng bước

Một cửa hàng bán lẻ: $D = 12{,}000$ đơn vị/năm, $S = 500{,}000$ VNĐ/lần, giá mua 100,000 VNĐ/đơn vị, tỷ lệ lưu kho 20%/năm nên $H = 0.2 \times 100{,}000 = 20{,}000$ VNĐ/đơn vị/năm.

**Bước 1 - Tính EOQ**:

$$EOQ = \sqrt{\frac{2 \times 12{,}000 \times 500{,}000}{20{,}000}} = \sqrt{600{,}000} \approx 775 \text{ đơn vị}$$

**Bước 2 - Số lần đặt hàng**: $N^* = 12{,}000 / 774.6 \approx 15.5$ lần/năm.

**Bước 3 - Chu kỳ đặt hàng** (360 ngày làm việc): $T^* = 360 / 15.49 \approx 23.2$ ngày, tức khoảng 23 ngày đặt hàng một lần.

**Bước 4 - Kiểm tra tổng chi phí**:
- Chi phí đặt hàng: $15.49 \times 500{,}000 \approx 7{,}746{,}000$ VNĐ
- Chi phí lưu kho: $\frac{774.6}{2} \times 20{,}000 \approx 7{,}746{,}000$ VNĐ (bằng chi phí đặt hàng, đúng như lý thuyết)
- $TC^* = 7{,}746{,}000 + 7{,}746{,}000 \approx 15{,}492{,}000$ VNĐ, trùng với $\sqrt{2 \times 12{,}000 \times 500{,}000 \times 20{,}000} \approx 15{,}492{,}000$.

**Bước 5 - Độ nhạy: nếu đặt sai Q thì thiệt bao nhiêu?**

| Q đặt mỗi lần | Chi phí đặt hàng/năm (VNĐ) | Chi phí lưu kho/năm (VNĐ) | Tổng chi phí (VNĐ) | Chênh so với tối ưu |
|---|---|---|---|---|
| 400 | 15,000,000 | 4,000,000 | 19,000,000 | +22.6% |
| 500 | 12,000,000 | 5,000,000 | 17,000,000 | +9.7% |
| **775 (EOQ)** | 7,741,935 | 7,750,000 | **15,491,935** | 0% |
| 1,200 | 5,000,000 | 12,000,000 | 17,000,000 | +9.7% |
| 2,000 | 3,000,000 | 20,000,000 | 23,000,000 | +48.5% |

**Diễn giải**: Lệch khỏi EOQ khoảng 35% (Q=500) chỉ làm tổng chi phí tăng khoảng 10%; đường tổng chi phí rất "phẳng" quanh điểm tối ưu. Bài học cho SME: *không cần EOQ chính xác tuyệt đối*, có thể làm tròn theo quy cách đóng gói/xe vận chuyển; nhưng đặt lô quá lớn (2.000, gấp 2,6 lần EOQ) lại gây thiệt hại gần 50%.

> Lưu ý: Bản cũ của file ghi nhầm $\sqrt{600{,}000{,}000}$; con số đúng trong căn là $600{,}000$ (kết quả 775 vẫn đúng).

### 1.4. Điểm đặt hàng lại (ROP) và Tồn kho an toàn (Safety Stock)

#### 1.4.1. Vấn đề cần giải quyết

EOQ trả lời "đặt *bao nhiêu*", còn ROP trả lời "đặt *khi nào*". Vì hàng đặt hôm nay chưa về ngay (lead time $L$), nếu chờ hết hàng mới đặt thì chắc chắn bị gián đoạn bán hàng trong suốt $L$ ngày. Do đó phải đặt khi lượng tồn còn đủ bán trong thời gian chờ:

$$ROP = d \times L + SS$$

- $d$ = Nhu cầu trung bình mỗi ngày (Average daily demand)
- $L$ = Thời gian giao hàng (Lead Time, ngày)
- $SS$ = Tồn kho an toàn (Safety Stock)

Nếu nhu cầu và lead time cố định tuyệt đối thì $SS = 0$ vẫn đủ. Nhưng thực tế nhu cầu mỗi ngày lúc nhiều lúc ít, giao hàng lúc sớm lúc trễ, nên cần tồn kho an toàn - phần "bảo hiểm" chống lại sự bất định.

#### 1.4.2. Logic của công thức Safety Stock

Giả sử nhu cầu mỗi ngày độc lập, phân phối chuẩn (Normal) với độ lệch chuẩn $\sigma_d$. Theo thống kê, **phương sai cộng dồn, độ lệch chuẩn không cộng dồn**: nhu cầu trong $L$ ngày có phương sai $L \times \sigma_d^2$, tức độ lệch chuẩn $\sigma_d\sqrt{L}$ (không phải $L \times \sigma_d$, vì ngày nhiều ngày ít bù trừ cho nhau một phần). Mức phục vụ mong muốn được quy đổi thành số độ lệch chuẩn cần dự phòng qua hệ số $Z$ (tra bảng phân phối chuẩn):

$$SS = Z \times \sigma_d \times \sqrt{L}$$

- $Z$ = Hệ số mức độ tin cậy (Service Level Z-score)
- $\sigma_d$ = Độ lệch chuẩn của nhu cầu hàng ngày
- $L$ = Lead time (ngày)

**Bảng hệ số Z theo mức độ phục vụ**:

| Mức độ phục vụ (Service Level) | Hệ số Z |
|---|---|
| 90% | 1.28 |
| 95% | 1.65 |
| 97.5% | 1.96 |
| 99% | 2.33 |
| 99.9% | 3.09 |

> "Mức phục vụ" ở đây là xác suất *không hết hàng trong một chu kỳ đặt hàng* (Cycle Service Level), khác với Fill Rate (tỷ lệ nhu cầu được đáp ứng đầy đủ).

**Trường hợp lead time cũng biến động** (thực tế ở Việt Nam thường gặp: xe hàng trễ, thời tiết, tắc đường). Gọi $\sigma_L$ là độ lệch chuẩn của lead time (ngày):

$$SS = Z \times \sqrt{L \times \sigma_d^2 + d^2 \times \sigma_L^2}$$

**Hệ thống kiểm tra định kỳ** (chu kỳ rà soát $R$ ngày): tồn kho phải bảo vệ trong cả $R + L$ ngày, nên:

$$SS = Z \times \sigma_d \times \sqrt{R + L}$$

#### 1.4.3. Ví dụ từng bước

Nhu cầu trung bình $d = 40$ đơn vị/ngày, $\sigma_d = 8$, lead time $L = 9$ ngày, mức phục vụ 95% ($Z = 1.65$), giá trị lưu kho $H = 20{,}000$ VNĐ/đơn vị/năm.

**Bước 1 - Nhu cầu trong lead time**: $d \times L = 40 \times 9 = 360$ đơn vị.

**Bước 2 - Tồn kho an toàn**: $SS = 1.65 \times 8 \times \sqrt{9} = 1.65 \times 8 \times 3 = 39.6 \approx 40$ đơn vị.

**Bước 3 - Điểm đặt hàng lại**: $ROP = 360 + 39.6 = 399.6 \approx 400$ đơn vị. Nghĩa là khi tồn kho tụt xuống 400, phải đặt hàng ngay.

**Bước 4 - So sánh các mức phục vụ** (sự đánh đổi chi phí):

| Mức phục vụ | Z | SS = Z × 8 × 3 | ROP | Chi phí giữ SS/năm (SS × 20,000) |
|---|---|---|---|---|
| 90% | 1.28 | 30.7 | 390.7 | 614,400 VNĐ |
| 95% | 1.65 | 39.6 | 399.6 | 792,000 VNĐ |
| 99% | 2.33 | 55.9 | 415.9 | 1,118,400 VNĐ |

**Diễn giải**: Từ 95% lên 99% (cải thiện 4 điểm %), phải thêm 16.3 đơn vị SS, tăng 41% chi phí giữ SS; từ 90% lên 95% chỉ thêm 8.9 đơn vị. Chi phí tăng *phi tuyến* khi gần 100% - vì vậy hàng nhóm A giá trị cao thường chọn 95%, hàng gây dừng sản xuất mới chọn 99%.

**Bước 5 - Hậu quả khi lead time biến động**: giả sử $\sigma_L = 2$ ngày:

$$SS = 1.65 \times \sqrt{9 \times 8^2 + 40^2 \times 2^2} = 1.65 \times \sqrt{576 + 6{,}400} = 1.65 \times 83.5 \approx 138 \text{ đơn vị}$$

Gấp hơn 3,4 lần mức 39.6 ở trên. **Bài học**: với nhiều SME Việt Nam, *sự thiếu ổn định của nhà cung cấp* gây thiếu hàng nhiều hơn biến động nhu cầu; giải pháp rẻ nhất thường là ký hợp đồng cam kết giao hàng đúng hạn hoặc chọn nhà cung cấp gần, chứ không phải chỉ tăng SS.

### 1.5. Phân loại ABC (ABC Analysis)

#### 1.5.1. Nguồn gốc và lý do

Vilfredo Pareto (nhà kinh tế Ý) quan sát năm **1896** rằng khoảng 80% đất đai ở Ý thuộc về khoảng 20% dân số - "nguyên lý 80/20". Joseph Juran sau đó khái quát hoá thành "thiểu số quan trọng, đa số tầm thường" (vital few, trivial many). Phân loại ABC trong tồn kho thường được ghi nhận là do **H. Ford Dickie** (General Electric) hệ thống hoá vào đầu thập niên 1950.

**Vấn đề kinh doanh**: Một cửa hàng có hàng trăm đến hàng nghìn mã hàng (SKU), nhưng thời gian và tiền của chủ doanh nghiệp có hạn. Đối xử với một ốc vít giá 5.000 VNĐ giống như một lô nhông sên dĩa trị giá hàng trăm triệu là lãng phí nguồn lực quản trị. ABC cho biết *nên dồn sự chú ý vào đâu*.

| Nhóm | % số lượng mặt hàng (SKU) | % giá trị sử dụng hàng năm | Mức độ kiểm soát |
|---|---|---|---|
| **A** | 10-20% | 70-80% | Kiểm soát chặt chẽ, kiểm kê thường xuyên, dự báo chính xác cao |
| **B** | 20-30% | 15-25% | Kiểm soát trung bình, kiểm kê định kỳ |
| **C** | 50-70% | 5-10% | Kiểm soát đơn giản, đặt hàng số lượng lớn ít lần |

```
% Giá trị tích luỹ
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

#### 1.5.2. Quy trình thực hiện (5 bước)

1. Lập danh sách toàn bộ SKU với **nhu cầu năm** và **đơn giá** (hoặc giá vốn).
2. Tính **giá trị sử dụng hàng năm** = nhu cầu năm × đơn giá.
3. Sắp xếp giảm dần theo giá trị.
4. Tính % giá trị và % **tích luỹ**.
5. Cắt nhóm theo ngưỡng (ví dụ A đến khoảng 70-80%, B đến khoảng 90-95%, phần còn lại là C).

> Phân loại theo giá trị chỉ là một chiều. Hàng giá trị thấp nhưng thiếu là dừng cả dây chuyền (ví dụ con ốc đặc chủng) cần được nâng nhóm; hàng dễ hư hỏng cũng cần quản lý chặt dù giá trị thấp. Có thể kết hợp ma trận ABC - XYZ (XYZ phân loại theo mức độ biến động nhu cầu).

Ví dụ thực hiện đầy đủ xem Case 3.6 (cửa hàng phụ tùng xe máy) và Bài tập 3.

### 1.6. Hệ thống kiểm soát tồn kho: Liên tục (Continuous Review) vs Định kỳ (Periodic Review)

**Vấn đề kinh doanh**: Cần quy tắc rõ ràng để quyết định *đặt hàng khi nào, bao nhiêu*. Có hai họ quy tắc chính:

| Tiêu chí | Hệ thống liên tục (Q-system, ký hiệu (s, Q)) | Hệ thống định kỳ (P-system, ký hiệu (R, S)) |
|---|---|---|
| Cách theo dõi | Theo dõi tồn kho liên tục theo thời gian thực | Kiểm tra tồn kho theo chu kỳ cố định (VD: mỗi tuần) |
| Thời điểm đặt hàng | Khi tồn kho chạm ROP | Vào thời điểm kiểm tra định kỳ |
| Số lượng đặt hàng | Cố định (EOQ) | Biến đổi (đặt đủ để đạt mức tồn kho mục tiêu S) |
| Yêu cầu hệ thống | Cần theo dõi thời gian thực (POS, mã vạch) | Đơn giản hơn, phù hợp kiểm kê thủ công |
| Tồn kho an toàn cần thiết | Thấp hơn (bảo vệ trong $L$ ngày) | Cao hơn (bảo vệ trong $R + L$ ngày) |
| Phù hợp | Hàng giá trị cao, nhu cầu ổn định, có hệ thống IT | SME, hàng giá trị thấp, kiểm kê thủ công; nhiều mặt hàng chung 1 nhà cung cấp (đặt gộp) |

**Công thức mức tồn kho mục tiêu của hệ thống định kỳ (Order-up-to level)**:

$$S = d \times (R + L) + Z \times \sigma_d \times \sqrt{R + L}$$

Mỗi lần kiểm tra, số lượng đặt = $S$ - (tồn kho hiện có + hàng đang trên đường về). Ví dụ minh hoạ xem Case 3.5 và Bài tập 9.

---

## II. Chi tiết từng thành phần (công cụ/kỹ thuật)

### 2.1. Just-In-Time (JIT) - Hệ thống tồn kho tinh gọn của Toyota

#### 2.1.1. Bối cảnh và triết lý

JIT là triết lý giảm tồn kho xuống mức tối thiểu bằng cách chỉ sản xuất/nhận hàng đúng số lượng, đúng thời điểm cần thiết, dựa trên hệ thống kéo (Pull System) thay vì đẩy (Push System). Ý tưởng "đúng lúc" được **Kiichiro Toyoda** nêu từ thập niên 1930 và được **Taiichi Ohno** biến thành hệ thống thực tế (Toyota Production System - TPS) trong thập niên 1950, trong bối cảnh Nhật Bản sau chiến tranh thiếu vốn, thiếu không gian và thị trường nhỏ, không thể sản xuất lô lớn như Mỹ. Ohno coi tồn kho dư thừa là một trong 7 loại lãng phí (muda) vì nó **che giấu** các vấn đề khác (máy hỏng, lỗi chất lượng, nhà cung cấp trễ).

**Liên hệ với EOQ**: Ở mô hình EOQ, $S$ (chi phí đặt hàng/chuẩn bị) được coi là *cố định* nên lô tối ưu lớn. JIT đặt câu hỏi ngược lại: "Làm sao giảm $S$ gần bằng 0 (setup nhanh, giao hàng nhiều chuyến nhỏ)?" Vì $EOQ = \sqrt{2DS/H}$, khi $S$ giảm thì EOQ giảm, và lý tưởng là lô bằng 1.

#### 2.1.2. Nguyên lý cốt lõi

- **Kanban**: thẻ tín hiệu (vật lý hoặc điện tử) ra lệnh sản xuất/bổ sung chỉ khi công đoạn sau đã tiêu thụ hàng của công đoạn trước.
- **Heijunka (San bằng sản xuất)**: san đều khối lượng và chủng loại sản xuất để tránh biến động đột ngột.
- **Quan hệ đối tác chặt chẽ với nhà cung cấp**: giao hàng nhiều lần trong ngày, số lượng nhỏ, độ tin cậy gần như tuyệt đối.

**Tính số lượng thẻ Kanban cần thiết**:

$$N = \frac{d \times L \times (1 + \alpha)}{C}$$

- $N$ = số thẻ (hoặc thùng) kanban; $d$ = nhu cầu trung bình mỗi đơn vị thời gian; $L$ = thời gian hoàn tất một chu kỳ bổ sung (chờ, sản xuất, vận chuyển), cùng đơn vị thời gian với $d$; $\alpha$ = hệ số an toàn (phần trăm đệm, do quản lý quyết định); $C$ = sức chứa một thùng (đơn vị).

*Ví dụ minh họa (giả định)*: $d = 400$ chi tiết/ngày, $L = 0.5$ ngày, $\alpha = 0.1$, $C = 20$ chi tiết/thùng:

$$N = \frac{400 \times 0.5 \times 1.1}{20} = 11 \text{ thẻ} \Rightarrow \text{tồn kho tối đa trong vòng kéo} = 11 \times 20 = 220 \text{ chi tiết}$$

Nếu cải tiến (kaizen) rút ngắn chu kỳ bổ sung còn $L = 0.25$ ngày: $N = \frac{400 \times 0.25 \times 1.1}{20} = 5.5 \rightarrow 6$ thẻ, tồn kho tối đa còn $6 \times 20 = 120$ chi tiết (giảm 45%). Đây là cơ chế "hạ mực nước để lộ đá ngầm": giảm số thẻ buộc nhà máy phải giải quyết nguyên nhân gây chậm.

#### 2.1.3. Điều kiện áp dụng và rủi ro

Điều kiện tiên quyết:
1. Nhu cầu ổn định và dự báo được.
2. Nhà cung cấp đáng tin cậy, khoảng cách địa lý gần hoặc logistics rất hiệu quả.
3. Chất lượng sản phẩm ổn định (tỷ lệ lỗi cao thì không có tồn kho đệm để bù).
4. Văn hoá cải tiến liên tục (Kaizen) trong toàn tổ chức.

**Rủi ro của JIT**: Đại dịch COVID-19 và đứt gãy chuỗi cung ứng toàn cầu 2020-2022 phơi bày điểm yếu của JIT thuần tuý: không có tồn kho đệm khiến nhiều ngành (ô tô, bán dẫn) phải dừng sản xuất. Xu hướng hậu COVID là "Just-In-Case" (JIC) có chọn lọc: giữ đệm cho linh kiện quan trọng/khó thay thế, giữ JIT cho phần còn lại. Có thể dùng ma trận Kraljic (xem file 03) để chọn nhóm hàng cần đệm.

### 2.2. Mô hình chiết khấu theo số lượng (Quantity Discount Model)

**Vấn đề kinh doanh**: Nhà cung cấp thường giảm giá nếu mua nhiều ("mua từ 1.000 cái giảm 5%"). Nhưng mua nhiều làm tăng tồn kho trung bình và chi phí lưu kho. Phải so sánh *tổng chi phí* chứ không chỉ nhìn giá thấp nhất. Vì giá $P$ nay thay đổi theo mức mua nên $H = i \times P$ cũng thay đổi, và phải cộng cả chi phí mua hàng vào tổng chi phí:

$$TC = \frac{D}{Q} \times S + \frac{Q}{2} \times H + D \times P, \quad H = i \times P$$

**Quy trình**: (1) tính EOQ tại mỗi mức giá; (2) nếu EOQ nằm ngoài khoảng số lượng được hưởng giá đó, điều chỉnh Q lên đúng ngưỡng thấp nhất của khoảng (hoặc loại nếu EOQ lớn hơn khoảng); (3) tính TC cho từng phương án khả thi và chọn nhỏ nhất.

**Ví dụ từng bước (giả định minh họa)**: $D = 12{,}000$, $S = 500{,}000$, $i = 20\%$. Bảng giá: dưới 500 đơn vị: 100,000; 500-999: 97,000; từ 1,000: 95,000 VNĐ.

| Mức giá P | H = 20% × P | EOQ tại mức này | Q khả thi dùng | TC đặt hàng | TC lưu kho | Chi phí mua D×P | Tổng chi phí (VNĐ) |
|---|---|---|---|---|---|---|---|
| 100,000 (Q<500) | 20,000 | 775 (ngoài khoảng, vượt 499) | 499 | 12,024,048 | 4,990,000 | 1,200,000,000 | 1,217,014,048 |
| 97,000 (500-999) | 19,400 | 786 (hợp lệ) | 786 | 7,628,892 | 7,628,892 | 1,164,000,000 | 1,179,257,785 |
| 95,000 (≥1,000) | 19,000 | 795 (dưới 1,000, nâng lên ngưỡng) | 1,000 | 6,000,000 | 9,500,000 | 1,140,000,000 | **1,155,500,000** |

**Diễn giải**: Phương án mua 1.000 đơn vị/lần giá 95,000 rẻ nhất, tiết kiệm khoảng 23,8 triệu VNĐ/năm so với EOQ giá 97,000 (1,179.26 - 1,155.50 triệu). Dù chi phí đặt hàng + lưu kho tăng (15.5 triệu so với 15.26 triệu), khoản tiết kiệm trên giá mua (24 triệu) lớn hơn nhiều. **Lưu ý thực tế**: cần kiểm tra thêm sức chứa kho, hạn sử dụng và áp lực vốn lưu động trước khi chốt (chiết khấu lớn nhưng hàng dễ hỏng thì không nên mua nhiều).

### 2.3. Mô hình EOQ khi có thiếu hàng có kế hoạch (Planned Backorder Model)

**Vấn đề kinh doanh**: Trong ngành đặt hàng theo yêu cầu (make-to-order), khách hàng chấp nhận chờ thay vì bỏ đi. Cho phép "thiếu hàng có kế hoạch" giúp giảm tồn kho, đổi lại phải trả chi phí thiếu hàng $B$ (VNĐ/đơn vị/năm: phạt, chiết khấu bù, mất thiện cảm). Công thức mở rộng:

$$Q^*_{b} = \sqrt{\frac{2DS}{H}} \times \sqrt{\frac{H + B}{B}}, \qquad \text{Mức tồn kho tối đa } I_{max} = Q^*_{b} \times \frac{B}{H + B}, \qquad \text{Số đơn chờ tối đa } = Q^*_{b} - I_{max}$$

*Ví dụ (số của ví dụ EOQ, thêm $B = 60{,}000$)*: $Q^*_b = 774.6 \times \sqrt{80{,}000/60{,}000} = 894.4$; $I_{max} = 894.4 \times 0.75 = 670.8$; số đơn chờ tối đa $= 223.6$; tổng chi phí $= 15.49 \text{ triệu} \times \sqrt{60/80} = 13.42$ triệu VNĐ (thấp hơn 15.49 triệu nhờ cho phép chờ). Nếu $B \to \infty$ (khách không chấp nhận chờ), công thức quay về EOQ cơ bản. Với bán lẻ ở Việt Nam hiếm khi áp dụng vì khách đi mua nơi khác; mô hình phù hợp hơn cho hàng đặt trước (nội thất theo yêu cầu, máy móc).

### 2.4. Kiểm kê tồn kho theo chu kỳ (Cycle Counting)

**Vấn đề kinh doanh**: Số liệu trong phần mềm thường lệch với hàng thực (mất cắp, nhập sai, xuất nhầm). Mọi công thức EOQ/ROP đều "rác vào, rác ra" nếu số tồn sai. Kiểm kê toàn bộ cuối năm tốn công, phải đóng cửa kho; Cycle Counting chia nhỏ việc đếm quanh năm, ưu tiên nhóm A (sai lệch ở nhóm A tốn tiền nhất):

| Nhóm ABC | Tần suất kiểm kê khuyến nghị |
|---|---|
| A | Hàng tháng hoặc hàng tuần |
| B | Hàng quý |
| C | Nửa năm hoặc hàng năm |

*Ví dụ tính tải công việc*: kho 1,000 SKU gồm 150 SKU nhóm A (đếm 12 lần/năm), 250 nhóm B (4 lần/năm), 600 nhóm C (1 lần/năm). Tổng số lượt đếm: $150 \times 12 + 250 \times 4 + 600 \times 1 = 1{,}800 + 1{,}000 + 600 = 3{,}400$ lượt/năm; với 250 ngày làm việc, mỗi ngày chỉ cần đếm khoảng $3{,}400 / 250 = 13.6$ SKU, rất khả thi cho 1 nhân viên kho kiêm nhiệm. Khi phát hiện sai lệch phải điều tra *nguyên nhân gốc* (quy trình nhập/xuất) chứ không chỉ điều chỉnh số.

### 2.5. Chỉ số vòng quay tồn kho (Inventory Turnover) và Số ngày tồn kho (DIO)

**Vấn đề kinh doanh**: Làm sao biết tồn kho "nhiều hay ít"? So con số tuyệt đối không có ý nghĩa; cần so với quy mô bán hàng. Chỉ số này đo *bao nhiêu lần trong năm doanh nghiệp bán hết và nhập lại lượng tồn bình quân*. Dùng giá vốn (COGS) làm tử số để cùng "đơn vị giá" với tồn kho (đều theo giá vốn, không lẫn lợi nhuận).

$$\text{Vòng quay tồn kho} = \frac{\text{Giá vốn hàng bán (COGS)}}{\text{Tồn kho bình quân}}, \quad \text{Tồn kho bình quân} = \frac{\text{Tồn đầu kỳ} + \text{Tồn cuối kỳ}}{2}$$

$$\text{Số ngày tồn kho (DIO)} = \frac{365}{\text{Vòng quay tồn kho}}$$

*Ví dụ từng bước*: COGS cả năm 1,800 triệu VNĐ; tồn đầu kỳ 260 triệu, cuối kỳ 340 triệu. Tồn bình quân $= (260 + 340)/2 = 300$ triệu. Vòng quay $= 1{,}800/300 = 6$ vòng/năm. DIO $= 365/6 \approx 60.8$ ngày: trung bình hàng nằm trong kho khoảng 61 ngày trước khi bán.

**Cách đọc**: vòng quay cao (DIO thấp) = vốn quay nhanh, nhưng quá cao có thể báo hiệu hay hết hàng; thấp = ứ vốn hoặc hàng chậm bán. Phải benchmark với trung bình ngành (siêu thị, thực phẩm thường quay nhanh; vật liệu xây dựng, nội thất quay chậm hơn).

### 2.6. Mô hình người bán báo (Newsvendor Model) cho sản phẩm có vòng đời ngắn

#### 2.6.1. Nguồn gốc và vấn đề cần giải quyết

Bài toán xuất phát từ ý tưởng của nhà kinh tế Francis Edgeworth (1888, nghiên cứu dự trữ tiền mặt của ngân hàng) và được phát triển thành mô hình "người bán báo" trong các công trình của Arrow, Harris, Marschak (1951). Người bán báo phải quyết định mua bao nhiêu tờ báo buổi sáng; báo ế cuối ngày chỉ còn giá giấy lộn, thiếu báo thì mất lãi. Cùng bản chất với bánh trung thu, mứt Tết, thời trang theo mùa, vé sự kiện, hoa dịp lễ: *chỉ có một cơ hội đặt hàng*, EOQ/ROP không áp dụng được.

#### 2.6.2. Logic của công thức

Xét việc đặt thêm *đơn vị thứ Q*. Nếu bán được, lãi thêm $C_u$; nếu không bán được, lỗ thêm $C_o$. Đặt thêm đơn vị đó có lợi chừng nào **xác suất bán được × $C_u$ ≥ xác suất không bán được × $C_o$**. Điểm cân bằng cho ra xác suất không hết hàng tối ưu (Critical Ratio):

$$CR = \frac{C_u}{C_u + C_o}$$

- $C_u$ = Chi phí thiếu hàng (Underage Cost) = giá bán - giá vốn (lãi biên mất đi khi thiếu 1 đơn vị)
- $C_o$ = Chi phí thừa hàng (Overage Cost) = giá vốn - giá thanh lý (lỗ khi thừa 1 đơn vị)

Số lượng tối ưu $Q^*$ là phân vị thứ $CR$ của phân phối nhu cầu; với nhu cầu phân phối chuẩn: $Q^* = \mu + Z_{CR} \times \sigma$.

#### 2.6.3. Ví dụ từng bước

Cửa hàng bánh trung thu: giá bán 150,000, giá vốn 90,000, giá thanh lý cuối mùa 40,000 VNĐ/hộp. Nhu cầu dự báo trung bình $\mu = 1{,}000$ hộp, $\sigma = 200$.

- $C_u = 150{,}000 - 90{,}000 = 60{,}000$ VNĐ
- $C_o = 90{,}000 - 40{,}000 = 50{,}000$ VNĐ
- $CR = \frac{60{,}000}{60{,}000 + 50{,}000} = \frac{60{,}000}{110{,}000} \approx 0.545$
- Tra bảng chuẩn: phân vị 0.545 tương ứng $Z \approx 0.114$
- $Q^* = 1{,}000 + 0.114 \times 200 \approx 1{,}023$ hộp (làm tròn 1,020-1,025)

**Diễn giải**: Vì lãi biên (60k) chỉ hơi lớn hơn lỗ thanh lý (50k) nên nên đặt cao hơn mức dự báo rất ít. Nếu bánh có lãi biên cao hơn (giá bán 200,000, $C_u = 110{,}000$) thì $CR = 110/160 = 0.6875$ và nên đặt nhiều hơn dự báo; nếu hàng thanh lý lỗ nặng (thực phẩm hết hạn, $C_o$ lớn) thì nên đặt *thấp hơn* dự báo. Nguyên tắc: "đặt thừa khi thiếu hàng đắt hơn thừa hàng, đặt thiếu trong trường hợp ngược lại".

**Ứng dụng thực tế**: bánh trung thu, mứt Tết, hàng thời trang theo mùa, hoa dịp lễ (Valentine, 20/10, 8/3) - nơi quyết định số lượng ban đầu gần như không thể điều chỉnh. Muốn giảm rủi ro, thương lượng quyền đổi/trả hàng với nhà cung cấp (làm tăng giá thanh lý, giảm $C_o$) hoặc đặt thêm lô bổ sung giữa mùa (biến bài toán một kỳ thành hai kỳ).

### 2.7. Nguyên lý gộp rủi ro (Risk Pooling)

#### 2.7.1. Vấn đề và logic

Doanh nghiệp có nhiều điểm bán (hoặc nhiều kho khu vực) thường tự giữ SS riêng ở từng nơi. Nhu cầu mỗi khu vực dao động ngẫu nhiên; khu vực này thừa thì khu vực khác có thể thiếu. Nếu gộp tồn kho về một kho trung tâm, các biến động **bù trừ** lẫn nhau: phương sai của tổng nhỏ hơn tổng phương sai khi các khu vực không tương quan hoàn toàn. Với $n$ kho giống nhau, nhu cầu độc lập, độ lệch chuẩn gộp chỉ bằng $\sqrt{n}$ lần (không phải $n$ lần) độ lệch chuẩn từng kho - gọi là "quy luật căn bậc hai" (square root law, được Maister (1976) và Eppen (1979) nghiên cứu).

$$SS_{\text{gộp}} < \sum SS_{\text{riêng lẻ}} \quad \text{khi tương quan nhu cầu } \rho < 1$$

#### 2.7.2. Ví dụ từng bước (giả định minh họa)

3 kho khu vực, mỗi kho $\sigma_d = 30$ đơn vị/ngày, lead time $L = 4$ ngày, mức phục vụ 95% ($Z = 1.65$).

- **Duy trì 3 kho riêng**: $SS$ mỗi kho $= 1.65 \times 30 \times \sqrt{4} = 99$; tổng $= 3 \times 99 = 297$ đơn vị.
- **Gộp 1 kho, nhu cầu độc lập** ($\rho = 0$): $\sigma_{gộp} = 30 \times \sqrt{3} = 51.96$; $SS = 1.65 \times 51.96 \times 2 \approx 171.5$ (giảm 42%).
- **Gộp 1 kho, tương quan vừa** ($\rho = 0.5$): phương sai gộp $= 3 \times 30^2 + 6 \times 0.5 \times 30^2 = 5{,}400 \Rightarrow \sigma = 73.5$; $SS = 1.65 \times 73.5 \times 2 \approx 242.5$ (giảm 18%).
- Nếu $\rho = 1$ (nhu cầu hoàn toàn đồng pha) thì gộp không giảm được gì: $SS = 297$.

**Đánh đổi**: gộp kho làm tăng chi phí và thời gian giao hàng chặng cuối, nên chỉ phù hợp hàng biến động lớn, giá trị cao, không yêu cầu giao siêu tốc. Hàng bán chạy cần giao nhanh thường giữ ở kho vệ tinh gần khách (xem mục 5.6).

### 2.8. Tồn kho ký gửi (Consignment) và Vendor Managed Inventory (VMI)

**Tồn kho ký gửi (Consignment Inventory)**: nhà cung cấp giao hàng đến kho của khách nhưng vẫn giữ quyền sở hữu cho đến khi khách thực sự sử dụng/bán. Khách không phải trả tiền trước, giảm áp lực vốn lưu động; nhà cung cấp chịu rủi ro tồn kho nhưng đổi lại có đơn hàng ổn định và quan hệ dài hạn. SME Việt Nam thường dùng hình thức ký gửi cho hàng mới/hàng thời trang/mỹ phẩm để giảm rủi ro nhập hàng.

**VMI (Vendor Managed Inventory)**: nhà cung cấp trực tiếp theo dõi và quyết định lượng bổ sung tại kho khách dựa trên dữ liệu bán hàng chia sẻ thời gian thực. Mô hình hợp tác sâu này giúp giảm hiệu ứng Bullwhip (xem file 03), phổ biến giữa nhà bán lẻ lớn (Walmart) và nhà cung cấp chiến lược (P&G). Điều kiện: có hệ thống chia sẻ dữ liệu và lòng tin lẫn nhau.

### 2.9. Ưu điểm & Nhược điểm của các chiến lược tồn kho

| Chiến lược | Ưu điểm | Nhược điểm |
|---|---|---|
| Tồn kho cao (High Inventory) | Đáp ứng nhanh nhu cầu đột biến, ít rủi ro thiếu hàng | Vốn lưu động bị đóng băng lớn, chi phí lưu kho cao, rủi ro lỗi thời |
| JIT/Tồn kho thấp | Giảm chi phí vốn, giảm lãng phí, tăng vòng quay | Rủi ro gián đoạn cao khi chuỗi cung ứng bất ổn |
| Phân loại ABC | Tập trung nguồn lực hiệu quả vào SKU quan trọng | Cần dữ liệu lịch sử đủ tốt để phân loại chính xác |
| Hệ thống liên tục (Continuous Review) | Phát hiện thiếu hàng sớm, tồn kho an toàn thấp hơn | Đòi hỏi đầu tư hệ thống IT theo dõi thời gian thực |
| Hệ thống định kỳ (Periodic Review) | Đơn giản, dễ triển khai thủ công | Cần tồn kho an toàn cao hơn, độ trễ phát hiện vấn đề |

**Chi phí ẩn của tồn kho quá cao so với quá thấp**:

| Hậu quả | Tồn kho quá cao (Overstock) | Tồn kho quá thấp (Understock) |
|---|---|---|
| Chi phí tài chính | Vốn lưu động bị chôn, tăng chi phí lãi vay | Không tận dụng được chiết khấu số lượng lớn |
| Rủi ro | Hàng lỗi thời, hết hạn, giảm giá thanh lý | Mất doanh số, mất khách hàng, chi phí đặt hàng khẩn cấp |
| Không gian | Cần kho bãi lớn hơn, tăng chi phí thuê/vận hành kho | Không tận dụng hết công suất kho hiện có |
| Ảnh hưởng thương hiệu | Không đáng kể trực tiếp | Nghiêm trọng - mất uy tín "luôn có hàng" |

### 2.10. Tồn kho và mối liên hệ với báo cáo tài chính

Quản trị tồn kho ảnh hưởng trực tiếp đến các chỉ số tài chính mà ngân hàng và nhà đầu tư quan tâm:

| Chỉ số tài chính | Công thức | Ảnh hưởng của tồn kho |
|---|---|---|
| Vốn lưu động ròng (Net Working Capital) | Tài sản ngắn hạn - Nợ ngắn hạn | Tồn kho cao làm tăng tài sản ngắn hạn nhưng "chôn" tiền mặt |
| Chu kỳ chuyển đổi tiền mặt (Cash Conversion Cycle - CCC) | DIO + DSO - DPO | Giảm DIO giúp rút ngắn chu kỳ, cải thiện dòng tiền |
| Tỷ suất sinh lời trên tài sản (ROA) | Lợi nhuận ròng / Tổng tài sản | Tồn kho dư thừa làm tăng mẫu số, giảm ROA dù lợi nhuận không đổi |
| Dự phòng giảm giá hàng tồn kho (Inventory Write-down) | Giá trị sổ sách - Giá trị thuần có thể thực hiện | Hàng lỗi thời phải trích lập dự phòng, giảm lợi nhuận báo cáo |

*Ví dụ từng bước*: COGS 2,400 triệu/năm, tồn đầu 380, tồn cuối 420 triệu. Tồn bình quân 400 triệu → vòng quay 6, DIO ≈ 60.8 ngày. Với DSO = 25 ngày, DPO = 30 ngày: $CCC = 60.8 + 25 - 30 = 55.8$ ngày. Nếu nhờ ABC/EOQ giảm DIO 10 ngày thì tiền mặt giải phóng $= 2{,}400 \times 10 / 365 \approx 65.8$ triệu VNĐ, và CCC còn khoảng 45.8 ngày.

Việc trích lập dự phòng giảm giá hàng tồn kho theo quy định kế toán Việt Nam (ví dụ Thông tư 48/2019/TT-BTC; người đọc nên đối chiếu văn bản hiện hành) là hệ quả kế toán trực tiếp của quản trị tồn kho kém. Giám đốc tài chính (CFO) và giám đốc vận hành (COO) cần phối hợp thiết lập chính sách tồn kho, nhìn cả đáp ứng khách hàng lẫn hiệu quả sử dụng vốn.

---

## III. Case Studies thực tế

> Ghi chú về độ tin cậy: các case Toyota, Vinamilk, thời trang/Zara chỉ nêu những dữ kiện khái quát được ghi nhận rộng rãi; mọi con số cụ thể kèm nhãn "giả định minh họa" là số tự thiết kế để minh hoạ phương pháp tính, không phải số liệu thật của doanh nghiệp. Các case SME (Cần Thơ, Hà Nội, phụ tùng xe máy) là tình huống tự thiết kế.

### 3.1. Case study quốc tế lớn: Toyota - Kanban, JIT và bài học về tồn kho đệm chiến lược

#### Bối cảnh

Toyota Production System (TPS) hình thành từ thập niên 1950 do Taiichi Ohno xây dựng. Hoàn cảnh: Nhật Bản sau chiến tranh thiếu vốn, nhà xưởng chật, thị trường nội địa nhỏ với nhiều mẫu xe, không thể sản xuất lô lớn rồi chất kho như Mỹ. Ohno cho rằng tồn kho dư thừa là một trong 7 lãng phí (muda) vì nó vừa chôn vốn vừa che giấu sự cố sản xuất. Theo các tài liệu về TPS, ông lấy cảm hứng từ cách siêu thị Mỹ chỉ bổ sung hàng lên kệ khi khách lấy đi.

#### Triển khai

- **Hệ thống kéo bằng Kanban**: công đoạn sau "kéo" chi tiết từ công đoạn trước bằng thẻ; công đoạn trước chỉ sản xuất bù đúng lượng đã bị lấy.
- **Giảm chi phí chuẩn bị $S$ (SMED)**: rút ngắn thời gian đổi khuôn để sản xuất lô nhỏ vẫn kinh tế (xem logic EOQ ở 2.1.1).
- **Giao hàng sát dây chuyền (line-side delivery)**: nhà cung cấp giao nhiều chuyến nhỏ/ngày, ít cần kho trung gian.

#### Phân tích định lượng (giả định minh họa về cách tính số thẻ)

Một vòng kéo chi tiết có $d = 400$ chi tiết/ngày, thời gian bổ sung $L = 0.5$ ngày, $\alpha = 10\%$, thùng 20 chi tiết:

- $N = \frac{400 \times 0.5 \times 1.1}{20} = 11$ thẻ → tối đa $11 \times 20 = 220$ chi tiết trong vòng kéo.
- Sau khi rút ngắn $L$ còn 0.25 ngày: $N = 5.5 \rightarrow 6$ thẻ → 120 chi tiết (giảm 45% tồn kho).
- Với 1,000 vòng kéo tương tự, mức giảm 100 chi tiết/vòng tức là 100,000 chi tiết ít hơn phải đầu tư vốn - đó là lý do "mỗi thẻ bỏ bớt là một khoản vốn được giải phóng".

#### Kết quả và rủi ro

Toyota thường được các tài liệu xếp vào nhóm có vòng quay tồn kho cao trong ngành ô tô (mức độ cụ thể chưa được kiểm chứng ở đây, nên không nêu số). Tuy nhiên JIT thuần tuý có điểm yếu: sau động đất - sóng thần Nhật Bản 2011 làm đứt nguồn cung linh kiện, Toyota theo các nguồn tin kinh tế đã xây dựng chiến lược đệm cho linh kiện quan trọng (bán dẫn, vi điều khiển); nhờ vậy trong khủng hoảng chip 2020-2022 hãng được đánh giá chịu tác động nhẹ hơn nhiều đối thủ (ước tính theo báo chí, cần đối chiếu nguồn gốc khi trích dẫn).

#### Bài học

1. JIT tối ưu *chi phí tồn kho* nhưng không tối ưu *rủi ro gián đoạn*; phải phân biệt linh kiện thay thế dễ (JIT) với linh kiện độc quyền/khó thay (cần đệm - Just-In-Case).
2. Giảm tồn kho là cách phát hiện vấn đề, không phải mục đích tự thân: giảm thẻ kanban buộc nhà máy xử lý nguyên nhân chậm trễ.
3. Với SME: không cần Kanban phức tạp, nhưng nguyên tắc "giao hàng lô nhỏ, nhiều lần" với nhà cung cấp gần là áp dụng được.

### 3.2. Case study Việt Nam lớn: Vinamilk - Quản trị tồn kho nguyên liệu sữa

#### Bối cảnh

Vinamilk cần quản trị tồn kho nguyên liệu sữa tươi (dễ hư hỏng, cần chuỗi lạnh) và sữa bột nhập khẩu (vận chuyển dài từ New Zealand, Mỹ, châu Âu). Nội dung dưới đây mô tả *cách vận dụng phương pháp* ở mức khái quát; các số liệu tính toán là giả định minh họa, không phải dữ liệu nội bộ của Vinamilk.

#### Giải pháp (khái quát)

- Phân loại ABC cho hàng nghìn SKU nguyên vật liệu và bao bì, kiểm soát chặt nhóm A (nguyên liệu chính, bao bì đặc thù).
- Dùng hệ thống hoạch định nguồn lực (ERP) liên kết kế hoạch sản xuất với kế hoạch nhập khẩu nguyên liệu.
- Tính tồn kho an toàn dựa trên biến động nhu cầu *và* biến động thời gian vận chuyển.

#### Phân tích định lượng (giả định minh họa)

Giả sử nguyên liệu sữa bột nhóm A: nhu cầu trung bình $d = 50$ tấn/ngày, $\sigma_d = 8$ tấn/ngày, lead time $L = 50$ ngày, mức phục vụ 95% ($Z = 1.65$).

- **Chỉ xét biến động nhu cầu**: $SS = 1.65 \times 8 \times \sqrt{50} = 1.65 \times 8 \times 7.07 \approx 93.3$ tấn; $ROP = 50 \times 50 + 93.3 = 2{,}593$ tấn. Nâng lên 99% ($Z = 2.33$): $SS \approx 131.8$ tấn.
- **Xét thêm biến động lead time** $\sigma_L = 7$ ngày (tàu biển trễ/lệch lịch): $SS = 1.65 \times \sqrt{50 \times 8^2 + 50^2 \times 7^2} = 1.65 \times \sqrt{3{,}200 + 122{,}500} = 1.65 \times 354.5 \approx 585$ tấn; $ROP \approx 2{,}500 + 585 = 3{,}085$ tấn.

**Ý nghĩa**: Khi lead time dài, *biến động thời gian giao hàng* mới là nguồn rủi ro chính (585 tấn so với 93 tấn, gấp hơn 6 lần). Vì vậy ngoài tăng SS, doanh nghiệp phải đầu tư đa dạng hoá nhà cung cấp, theo dõi lịch tàu, ký hợp đồng giao hàng ổn định và đồng thời dùng ABC để chỉ giữ SS lớn ở nhóm A có giá trị cao thực sự.

#### Bài học

1. Với hàng nhập khẩu lead time dài, SS là một khoản vốn lớn nhưng cần thiết; tính bằng công thức thay vì cảm tính.
2. ABC + ERP cho phép áp dụng các mức phục vụ khác nhau theo nhóm (A: 97.5-99%, B: 95%, C: 90%).
3. Kết hợp quản trị nhu cầu và quản trị nhà cung cấp quan trọng ngang quản trị kho.

### 3.3. Case study SME Việt Nam: Cửa hàng vật liệu xây dựng tại Cần Thơ (phân tích chi tiết, giả định minh họa)

#### Bối cảnh

Cửa hàng vật liệu xây dựng "VLXD Hậu Giang" (tên giả định) có hơn 500 mã hàng (xi măng, sắt thép, gạch, sơn, thiết bị vệ sinh), quản lý tồn kho thủ công bằng sổ sách. Số liệu giả định: giá vốn hàng bán (COGS) 10.8 tỷ VNĐ/năm; tồn kho bình quân 2.4 tỷ VNĐ.

**Chẩn đoán ban đầu**:
- Vòng quay $= 10.8 / 2.4 = 4.5$ vòng; DIO $= 365 / 4.5 \approx 81$ ngày.
- Nghịch lý: *vừa hết hàng bán chạy (xi măng, sắt) - tỷ lệ hết hàng nhóm A 15% - vừa ứ đọng hàng chậm*: khoảng 30% giá trị tồn kho $= 0.3 \times 2{,}400 = 720$ triệu nằm ở mẫu gạch cũ, thiết bị vệ sinh ít bán. Nguyên nhân: đặt hàng theo cảm tính, không có ROP, không phân biệt nhóm hàng.

#### Bước 1 - Phân loại ABC

500 mã hàng được sắp theo giá trị bán hàng năm:

| Nhóm | Số mã | % số mã | % doanh thu | Quản trị |
|---|---|---|---|---|
| A (xi măng, sắt thép, gạch phổ thông) | 75 | 15% | 75% | ROP tự động, đếm tháng |
| B | 125 | 25% | 18% | Kiểm tra định kỳ hai tuần, đếm quý |
| C (gạch mẫu, thiết bị vệ sinh, phụ kiện) | 300 | 60% | 7% | Đặt lô nhỏ/theo đơn, đếm 1 lần/năm |

Số lượt đếm/năm: $75 \times 12 + 125 \times 4 + 300 \times 1 = 900 + 500 + 300 = 1{,}700$; tính 300 ngày/năm → khoảng 5.7 mã/ngày, một nhân viên kho có thể làm được.

#### Bước 2 - EOQ cho xi măng (nhóm A)

Dữ liệu giả định: $D = 36{,}000$ bao/năm (100 bao/ngày, 360 ngày), giá vốn 90,000 VNĐ/bao, chi phí đặt hàng $S = 300{,}000$ VNĐ (vận chuyển cố định + bốc xếp + thủ tục), tỷ lệ lưu kho 25% (gồm lãi vốn + hao hụt do ẩm, vỡ bao) nên $H = 0.25 \times 90{,}000 = 22{,}500$ VNĐ/bao/năm.

$$EOQ = \sqrt{\frac{2 \times 36{,}000 \times 300{,}000}{22{,}500}} = \sqrt{960{,}000} \approx 980 \text{ bao}$$

$N^* = 36{,}000 / 980 \approx 36.7$ lần/năm, chu kỳ khoảng 9.8 ngày.

**So sánh với cách đặt cũ** (đặt lô 2,000 bao mỗi khi "nhìn kho vơi"):

| Chỉ tiêu | Lô cũ Q = 2,000 | EOQ ≈ 980 |
|---|---|---|
| Chi phí đặt hàng/năm | $18 \times 300{,}000 = 5{,}400{,}000$ | $36.74 \times 300{,}000 \approx 11{,}020{,}000$ |
| Chi phí lưu kho/năm | $1{,}000 \times 22{,}500 = 22{,}500{,}000$ | $490 \times 22{,}500 \approx 11{,}025{,}000$ |
| **Tổng** | **27,900,000** | **≈ 22,045,000** |

Tiết kiệm $\approx 5.85$ triệu VNĐ/năm cho riêng xi măng; tồn kho chu kỳ bình quân giảm từ 1,000 xuống 490 bao, giải phóng $510 \times 90{,}000 = 45.9$ triệu VNĐ vốn.

#### Bước 3 - Safety Stock và ROP cho xi măng

Nhu cầu/ngày $d = 100$ bao, $\sigma_d = 25$, lead time của đại lý $L = 2$ ngày, mức phục vụ 95%:

$SS = 1.65 \times 25 \times \sqrt{2} \approx 58.3$ bao → làm tròn 58 bao; $ROP = 100 \times 2 + 58.3 \approx 258$ bao.

Quy tắc đơn giản treo tại kho: "Xi măng còn 260 bao là gọi đại lý đặt 980 bao". SS tốn thêm $58 \times 90{,}000 \approx 5.2$ triệu vốn, nhưng đổi lại tỷ lệ hết hàng giảm mạnh (mục tiêu dưới 5%, ứng với mức phục vụ 95%).

#### Bước 4 - Xử lý hàng chậm và công cụ

- Thanh lý giảm giá nhóm C tồn quá 6 tháng không bán; kết quả giả định: hàng chậm giảm 20%, từ 720 xuống 576 triệu, giải phóng 144 triệu.
- Dùng phần mềm quản lý bán hàng giá rẻ (như KiotViet) để theo dõi tồn theo thời gian thực, đặt cảnh báo khi chạm ROP.

#### Kết quả sau 6 tháng (giả định minh họa)

| Chỉ tiêu | Trước | Sau |
|---|---|---|
| Tỷ lệ hết hàng nhóm A | 15% | dưới 5% |
| Tồn kho bình quân | 2,400 triệu | $2{,}400 - 144 - (45.9 - 5.22) = 2{,}215.3$ triệu |
| Vòng quay tồn kho | 4.5 vòng | $10.8 / 2.2153 \approx 4.88$ vòng |
| DIO | ≈ 81 ngày | ≈ 75 ngày |

(Trong đó $45.9 - 5.22 = 40.68$ triệu là mức giảm ròng của xi măng: giảm tồn chu kỳ, cộng thêm SS.)

**Lợi ích tài chính định lượng**: giảm chi phí tồn kho xi măng 5.85 triệu/năm + tiết kiệm lãi vay trên 144 triệu thanh lý (giả định lãi 12%/năm) $= 144 \times 12\% = 17.28$ triệu → khoảng 23.1 triệu VNĐ/năm, chưa tính doanh thu giữ lại nhờ ít hết hàng.

#### Bài học

1. Chỉ cần ABC + EOQ + ROP và một phần mềm bán hàng giá rẻ là SME đã cải thiện rõ.
2. EOQ không phải để "đặt chính xác", mà để tránh hai thái cực (lô quá lớn hoặc quá nhỏ).
3. Phải đi cùng thanh lý hàng chậm; nếu không, "tối ưu mới" vẫn bị kéo lùi bởi vốn nằm ở hàng cũ.

### 3.4. Case study quốc tế - bài học thất bại: thời trang truyền thống và Zara (số liệu giả định minh họa)

#### Bối cảnh

Nhiều nhà bán lẻ thời trang truyền thống đặt hàng trước cả mùa (khoảng 6 tháng) dựa trên dự báo. Vì xu hướng đổi nhanh, sai số dự báo rất lớn, cuối mùa phải giảm giá sâu (thường được nhắc ở mức 50-70%, ước tính theo báo chí ngành) để xả hàng. Zara (thuộc Inditex) được phân tích rộng rãi như mô hình ngược lại: thiết kế - sản xuất theo lô nhỏ, phản hồi nhanh dữ liệu bán hàng (xem file 03).

#### Phân tích bằng Newsvendor (giả định minh họa)

Một mẫu áo: giá bán 500,000, giá vốn 200,000, giá thanh lý 150,000 VNĐ. Nhu cầu trung bình toàn mùa $\mu = 10{,}000$ chiếc.

- $C_u = 500{,}000 - 200{,}000 = 300{,}000$; $C_o = 200{,}000 - 150{,}000 = 50{,}000$.
- $CR = 300 / (300 + 50) = 0.857 \Rightarrow Z \approx 1.068$.

| Chỉ tiêu | Mô hình đặt trước cả mùa ($\sigma = 4{,}000$, sai số 40%) | Mô hình phản hồi nhanh ($\sigma = 1{,}500$, sai số 15%) |
|---|---|---|
| Số lượng tối ưu $Q^* = 10{,}000 + 1.068\sigma$ | ≈ 14,270 | ≈ 11,601 |
| Số chiếc dư dự kiến | ≈ 4,563 | ≈ 1,711 |
| Thiệt hại thanh lý ($\times 50{,}000$) | ≈ 228 triệu | ≈ 86 triệu |
| Doanh thu lãi mất do thiếu hàng ($\times 300{,}000$) | ≈ 88 triệu | ≈ 33 triệu |
| **Tổng chi phí bất định** | **≈ 316 triệu** | **≈ 119 triệu** |

**Diễn giải**: Cùng một mẫu áo, nếu giảm độ bất định của dự báo từ 40% xuống 15% (nhờ đặt hàng gần mùa bán, đặt bổ sung giữa mùa), chi phí bất định giảm khoảng 62%. Nghĩa là *tốc độ phản hồi (rút ngắn lead time đến thời điểm biết rõ nhu cầu) có giá trị kinh tế lớn hơn việc dự báo giỏi hơn*.

#### Bài học

1. Với hàng thời vụ, quyết định quan trọng không phải con số dự báo, mà là *giảm độ không chắc chắn* (đặt muộn, lô nhỏ, đặt bổ sung).
2. Thương lượng quyền đổi/trả với nhà cung cấp giúp giảm $C_o$.
3. SME thời trang online có thể bắt chước: đặt lô thử nhỏ, bán thử qua livestream/pre-order, rồi đặt lô lớn cho mẫu bán chạy.

### 3.5. Case study SME Việt Nam - dịch vụ: Chuỗi nhà thuốc tư nhân quản lý hàng theo hạn sử dụng (phân tích chi tiết, giả định minh họa)

#### Bối cảnh

Chuỗi 8 nhà thuốc tư nhân (tên giả định "Nhà thuốc An Khang") tại Hà Nội gặp tình trạng thuốc hết hạn phải tiêu huỷ, gây thiệt hại tài chính và có thể vi phạm quy định dược phẩm nếu xử lý sai cách. Số liệu giả định: tồn kho bình quân cả chuỗi 4.8 tỷ VNĐ; tỷ lệ tiêu huỷ do hết hạn 4%/năm giá trị tồn kho.

**Thiệt hại ban đầu**: $4\% \times 4{,}800 = 192$ triệu VNĐ/năm.

#### Giải pháp và phân tích

**1. Nguyên tắc FEFO (First Expired, First Out)** thay vì FIFO: với hàng có hạn dùng, hàng nhập trước chưa chắc hết hạn sớm hơn; FEFO xuất lô gần hạn trước. Nhân viên được hướng dẫn sắp xếp lô gần hạn phía trước kệ.

**2. Cảnh báo tự động khi còn 3 tháng đến hạn**: phần mềm đánh dấu mặt hàng, chuyển sang chi nhánh có tốc độ bán cao hơn hoặc áp dụng khuyến mãi/combo.

**3. Chuyển hàng dễ hết hạn sang hệ thống kiểm tra định kỳ ngắn (weekly order-up-to)**: ví dụ thuốc A: $d = 15$ hộp/ngày, $\sigma_d = 5$, chu kỳ kiểm tra $R = 7$ ngày, lead time $L = 2$ ngày, mức phục vụ 95%:

- $SS = 1.65 \times 5 \times \sqrt{7 + 2} = 1.65 \times 5 \times 3 = 24.75 \approx 25$ hộp.
- $S = 15 \times (7 + 2) + 24.75 = 135 + 24.75 \approx 160$ hộp (mức tồn mục tiêu mỗi lần kiểm tra).

**So sánh với đặt hàng theo tháng** ($R = 30$): $SS = 1.65 \times 5 \times \sqrt{32} \approx 46.7$; $S = 15 \times 32 + 46.7 \approx 527$ hộp. Tồn kho bình quân xấp xỉ $d R/2 + SS$: tuần ≈ $52.5 + 24.75 = 77.3$ hộp; tháng ≈ $225 + 46.7 = 271.7$ hộp. Kiểm tra mỗi tuần giữ ít hơn khoảng 3.5 lần số hộp trên kệ, nên rủi ro hết hạn thấp hơn đáng kể (đánh đổi: tăng số lần đặt hàng).

#### Kết quả (giả định)

Tỷ lệ tiêu huỷ giảm từ 4% xuống 0.8%: $0.8\% \times 4{,}800 = 38.4$ triệu; tiết kiệm $192 - 38.4 = 153.6$ triệu VNĐ/năm, giảm rủi ro pháp lý. Chi phí phần mềm (vài chục triệu/năm cho chuỗi) hoàn vốn trong năm đầu.

#### Bài học

1. Với hàng có hạn sử dụng, FEFO và kiểm tra định kỳ ngắn quan trọng hơn EOQ.
2. Cảnh báo sớm 3 tháng chuyển "tiêu huỷ" thành "khuyến mãi/điều chuyển" - thu hồi được một phần giá vốn.
3. Cần lưu ý quy định chuyên ngành dược khi xử lý thuốc cận date.

### 3.6. Case study SME Việt Nam MỚI: Cửa hàng phụ tùng xe máy "Hòa Phát Parts" tại Biên Hòa (toàn bộ số liệu giả định minh họa)

#### Bối cảnh

Cửa hàng phụ tùng xe máy "Hòa Phát Parts" (tên giả định) tại Biên Hòa, Đồng Nai, có khoảng 600 mã hàng, 4 nhân viên, bán cho khách lẻ và vài tiệm sửa xe. Giá vốn hàng bán (COGS) 1,643 triệu VNĐ/năm; tồn kho bình quân 410.75 triệu → **vòng quay = 1,643 / 410.75 = 4.0 vòng, DIO = 365/4 ≈ 91 ngày**. Vấn đề: nhớt và lốp hay hết lúc cao điểm, trong khi nhiều phụ tùng cũ nằm kho; chủ cửa hàng đặt "gần hết thì gọi" theo cảm tính, lô lớn khi có chiết khấu.

Để dễ trình bày, ta dùng 10 nhóm hàng đại diện (trong thực tế là 600 mã).

#### Bước 1 - Phân loại ABC

Giá trị sử dụng năm = nhu cầu năm × giá vốn:

| Xếp hạng | Mã hàng | Nhu cầu/năm | Giá vốn (VNĐ) | Giá trị năm (triệu) | % | % tích luỹ | Nhóm |
|---|---|---|---|---|---|---|---|
| 1 | Nhớt máy 0.8L | 6,000 | 70,000 | 420 | 25.6% | 25.6% | A |
| 2 | Lốp xe (vỏ) | 1,500 | 280,000 | 420 | 25.6% | 51.1% | A |
| 3 | Nhông sên dĩa (bộ) | 900 | 250,000 | 225 | 13.7% | 64.8% | A |
| 4 | Bố thắng | 3,200 | 55,000 | 176 | 10.7% | 75.5% | A |
| 5 | Bugi | 4,000 | 30,000 | 120 | 7.3% | 82.8% | B |
| 6 | Ắc quy | 400 | 300,000 | 120 | 7.3% | 90.1% | B |
| 7 | Dây curoa | 600 | 150,000 | 90 | 5.5% | 95.6% | C |
| 8 | Gương chiếu hậu | 700 | 60,000 | 42 | 2.6% | 98.2% | C |
| 9 | Đèn xi nhan | 500 | 40,000 | 20 | 1.2% | 99.4% | C |
| 10 | Ốc vít (bộ) | 2,000 | 5,000 | 10 | 0.6% | 100% | C |
| | **Tổng** | | | **1,643** | 100% | | |

Quy tắc cắt nhóm: A đến ≤ 80% tích luỹ, B đến ≤ 95%, còn lại C. Kết quả: A = 4 mã (40% số mã) chiếm 75.5% giá trị; B = 2 mã chiếm 14.6%; C = 4 mã chiếm 9.9%. (Trong danh mục 600 mã thật, nhóm A thường chỉ 10-20% số mã; ở đây mẫu 10 mã nên tỷ lệ cao hơn.)

#### Bước 2 - EOQ, SS, ROP cho nhớt máy 0.8L (nhóm A)

Dữ liệu: $D = 6{,}000$ chai/năm (làm việc 300 ngày → $d = 20$/ngày), $\sigma_d = 6$, giá vốn 70,000; chi phí đặt hàng $S = 150{,}000$ VNĐ/lần; $i = 20\%$ → $H = 14{,}000$ VNĐ/chai/năm; lead time $L = 5$ ngày; mức phục vụ 95%.

$$EOQ = \sqrt{\frac{2 \times 6{,}000 \times 150{,}000}{14{,}000}} = \sqrt{128{,}571} \approx 359 \text{ chai (làm tròn 360 = 15 thùng 24 chai)}$$

- Số lần đặt: $6{,}000 / 359 \approx 16.7$ lần/năm (khoảng 18 ngày/lần).
- $SS = 1.65 \times 6 \times \sqrt{5} \approx 22.1$ chai; $ROP = 20 \times 5 + 22.1 \approx 122$ chai.

| Chỉ tiêu | Cũ (Q = 1,000 chai mỗi lần) | Mới (EOQ ≈ 359) |
|---|---|---|
| Chi phí đặt hàng/năm | $6 \times 150{,}000 = 900{,}000$ | $16.7 \times 150{,}000 \approx 2{,}510{,}000$ |
| Chi phí lưu kho/năm | $500 \times 14{,}000 = 7{,}000{,}000$ | $179.3 \times 14{,}000 \approx 2{,}510{,}000$ |
| **Tổng** | **7,900,000** | **≈ 5,020,000** |

Tiết kiệm ≈ 2.88 triệu/năm; tồn chu kỳ giảm từ 500 xuống ≈ 180 chai (giải phóng $320 \times 70{,}000 = 22.4$ triệu); thêm SS 22 chai ≈ 1.5 triệu.

#### Bước 3 - Lốp xe (nhóm A)

$D = 1{,}500$, giá vốn 280,000, $S = 200{,}000$, $i = 20\%$ → $H = 56{,}000$; $d = 5$/ngày, $\sigma_d = 2$, $L = 4$ ngày, mức phục vụ 99% ($Z = 2.33$, vì khách đang chờ thay lốp, hết hàng mất khách ngay).

- $EOQ = \sqrt{2 \times 1{,}500 \times 200{,}000 / 56{,}000} = \sqrt{10{,}714} \approx 103.5 \rightarrow 104$ chiếc; khoảng 14.5 lần/năm.
- $SS = 2.33 \times 2 \times \sqrt{4} \approx 9.3$; $ROP = 5 \times 4 + 9.3 \approx 29$ chiếc.
- Cũ đặt lô 300: tổng $= \frac{1{,}500}{300} \times 200{,}000 + \frac{300}{2} \times 56{,}000 = 1{,}000{,}000 + 8{,}400{,}000 = 9{,}400{,}000$. Mới (Q = 104): $\approx 5{,}797{,}000$ → tiết kiệm ≈ 3.6 triệu/năm; tồn chu kỳ giảm từ 150 xuống 52.5 chiếc, giải phóng $97.5 \times 280{,}000 = 27.3$ triệu.

#### Bước 4 - Nhóm C: hệ thống định kỳ (ốc vít)

Mỗi 14 ngày kiểm tra một lần theo chuyến giao hàng của nhà phân phối (đặt gộp nhiều mã C chung 1 đơn): $d = 2{,}000/300 \approx 6.67$ bộ/ngày, $\sigma_d = 3$, $R = 14$, $L = 3$, mức phục vụ 90% ($Z = 1.28$):

$SS = 1.28 \times 3 \times \sqrt{17} \approx 15.8$; $S = 6.67 \times 17 + 15.8 \approx 129$ bộ. Nhân viên chỉ cần đếm tồn và đặt cho đủ 129 bộ. Đặt gộp nhóm C giúp chia nhỏ chi phí $S$ cho nhiều mã.

#### Bước 5 - Kết quả tài chính (sau 6 tháng)

Thanh lý hàng chậm và các điều chỉnh khác giải phóng thêm vốn. Tổng tồn kho bình quân giảm từ 410.75 xuống 328.6 triệu (giảm 82.15 triệu), tính như sau: giảm tồn chu kỳ nhớt + lốp $= 22.4 + 27.3 = 49.7$ triệu; thêm SS hai mã $\approx 4.06$ triệu ($22 \times 70{,}000 + 9 \times 280{,}000$); thanh lý hàng chậm $= 82.15 - 49.7 + 4.06 = 36.51$ triệu.

| Chỉ tiêu | Trước | Sau |
|---|---|---|
| Tồn kho bình quân | 410.75 triệu | 328.6 triệu |
| Vòng quay (COGS 1,643) | 4.0 vòng | 5.0 vòng |
| DIO | 91.25 ngày | 73 ngày |
| Vốn giải phóng | | 82.15 triệu |

**Lợi ích quy đổi**: chi phí tồn kho giảm $2.88 + 3.60 = 6.48$ triệu/năm (nhớt + lốp, đã gồm lãi vốn) + lãi tiết kiệm trên 36.51 triệu hàng chậm thanh lý (lãi 12%) $\approx 4.38$ triệu → khoảng 10.9 triệu VNĐ/năm, cộng với doanh số giữ lại nhờ ít hết nhớt/lốp vào mùa cao điểm.

#### Bài học

1. Mỗi nhóm hàng một chính sách: A dùng EOQ + ROP + mức phục vụ cao; C dùng kiểm tra định kỳ đặt gộp.
2. Mức phục vụ nên chọn theo *hậu quả khi hết hàng* (lốp 99%, ốc vít 90%), không áp một mức cho tất cả.
3. Lợi ích lớn nhất của SME thường đến từ giải phóng vốn và giảm hết hàng, không phải tiết kiệm vài triệu chi phí đặt hàng.

### 3.7. Bảng tổng hợp bài học từ các case study

| Case study | Công cụ áp dụng | Bài học chính |
|---|---|---|
| Toyota | JIT, Kanban | JIT hiệu quả nhưng cần tồn kho đệm chiến lược cho rủi ro hệ thống (chip, thiên tai) |
| Vinamilk | ABC + ERP + Safety Stock | Lead time dài và biến động: SS phải tính cả $\sigma_L$ |
| VLXD Cần Thơ | ABC + EOQ + ROP | SME dùng công cụ cơ bản cũng giảm hết hàng và giải phóng vốn |
| Thời trang/Zara | Newsvendor | Giảm độ bất định (đặt muộn, lô nhỏ) có giá trị hơn dự báo giỏi hơn |
| Nhà thuốc Hà Nội | FEFO + Order-up-to | Hàng có hạn dùng: kiểm tra định kỳ ngắn, cảnh báo sớm |
| Phụ tùng xe máy Biên Hòa | ABC + EOQ/SS/ROP theo nhóm | Mỗi nhóm một chính sách, mức phục vụ theo hậu quả thiếu hàng |

---

## IV. Ứng dụng cho SME

### 4.1. Quy trình 6 bước xây dựng hệ thống quản trị tồn kho

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

**Gợi ý lộ trình 90 ngày cho SME**: Tháng 1 - làm sạch dữ liệu (mã hàng, đơn giá, nhu cầu 12 tháng gần nhất), chạy ABC trên Excel, thanh lý hàng tồn quá 6-12 tháng. Tháng 2 - tính EOQ/SS/ROP cho nhóm A, dán bảng ROP tại kho, bắt đầu cycle counting nhóm A. Tháng 3 - chuyển sang phần mềm bán hàng có tồn kho thời gian thực, thiết lập cảnh báo, đo KPI đầu tiên (vòng quay, tỷ lệ hết hàng).

**Cách ước lượng các tham số khi thiếu dữ liệu**: $S$ = (lương giờ nhân viên × giờ xử lý đơn) + phí vận chuyển cố định mỗi chuyến; $H$ = (lãi vay hoặc chi phí cơ hội vốn 10-15%) + hao hụt + thuê kho/bảo hiểm tính theo % giá vốn; $\sigma_d$ lấy từ độ lệch chuẩn doanh số bán hằng ngày/tuần của 3-6 tháng gần nhất (hàm STDEV trong Excel).

### 4.2. Quy mô áp dụng - SME và doanh nghiệp lớn

| Thành phần | SME | Doanh nghiệp lớn |
|---|---|---|
| Phân loại ABC | Thủ công trên Excel, 1-2 lần/năm | Tự động hoá trong ERP, cập nhật liên tục |
| Tính EOQ/Safety Stock | Công thức cơ bản, ước lượng thủ công | Mô hình thống kê nâng cao, tính riêng theo SKU |
| Hệ thống kiểm soát | Định kỳ (periodic review) phổ biến | Liên tục (continuous review) với mã vạch/RFID |
| Kiểm kê | Kiểm kê toàn bộ 1-2 lần/năm | Cycle counting liên tục theo ABC |
| Công nghệ | Phần mềm bán hàng đơn giản (KiotViet, Sapo) | WMS (Warehouse Management System) chuyên dụng |

**Chi phí đầu tư theo giai đoạn phát triển (ước tính tham khảo)**:

| Giai đoạn | Công cụ tồn kho | Chi phí ước tính (VNĐ) |
|---|---|---|
| Khởi nghiệp | Sổ sách, Excel cơ bản | 0 - 5 triệu |
| Tăng trưởng | Phần mềm bán hàng có module tồn kho | 5 - 50 triệu/năm |
| Mở rộng | WMS cơ bản, mã vạch, tích hợp ERP nhỏ | 100 triệu - 1 tỷ |
| Doanh nghiệp lớn | WMS/ERP toàn diện, RFID, tự động hoá kho | 2 - 20+ tỷ |

### 4.3. Các sai lầm thường gặp

| Sai lầm | Hậu quả | Cách phòng tránh |
|---|---|---|
| Áp dụng cùng chính sách tồn kho cho mọi SKU | Lãng phí nguồn lực quản trị cho hàng ít quan trọng | Phân loại ABC, ưu tiên nguồn lực theo nhóm |
| Không tính biến động nhu cầu/lead time khi tính Safety Stock | Thiếu hàng thường xuyên dù có "dự trữ" | Dùng công thức SS theo độ lệch chuẩn và Z-score; đo cả $\sigma_L$ |
| Copy công thức EOQ máy móc, bỏ qua ràng buộc thực tế | Đặt số lượng không khả thi (quá lớn so với kho, MOQ) | Điều chỉnh EOQ theo MOQ của NCC, sức chứa kho, quy cách đóng gói |
| Không kiểm kê định kỳ | Số liệu hệ thống lệch thực tế, mất kiểm soát | Cycle counting theo tần suất ABC |
| Theo đuổi JIT tuyệt đối mà không đánh giá rủi ro chuỗi cung ứng | Dễ tổn thương khi gián đoạn nguồn cung | Đánh giá theo Kraljic, giữ buffer cho hàng quan trọng |
| Chạy theo chiết khấu số lượng mà không tính tổng chi phí | Ứ vốn, hàng hỏng/lỗi thời | So sánh TC theo mô hình 2.2, kiểm tra sức chứa/hạn dùng |
| SME: không phân loại ABC, quản lý đồng đều mọi mặt hàng | Lãng phí nguồn lực | Làm ABC trên Excel mỗi 6 tháng |
| SME: Safety Stock dựa hoàn toàn vào cảm tính | Hết hàng hoặc ứ vốn | Tính SS theo công thức, điều chỉnh theo kết quả thực |
| Doanh nghiệp lớn: đầu tư IT phức tạp nhưng dữ liệu không chuẩn | "Rác vào, rác ra" (garbage in, garbage out) | Chuẩn hoá dữ liệu gốc trước khi mua hệ thống |
| Doanh nghiệp lớn: SS đặt một lần rồi không cập nhật | SS lỗi thời so với biến động thị trường | Tính lại SS hằng quý/khi có thay đổi lớn |
| Doanh nghiệp lớn: đầu tư RFID/IoT nhưng thiếu tích hợp dữ liệu | Lãng phí đầu tư | Lập lộ trình tích hợp xuyên bộ phận, tính ROI trước |

---

## V. Tools & Templates

### 5.1. Bảng công cụ phần mềm

| Công cụ | Chức năng | Chi phí ước tính | Phù hợp |
|---|---|---|---|
| Excel/Google Sheets với công thức EOQ/SS | Tính toán cơ bản | Miễn phí | SME nhỏ |
| KiotViet, Sapo | Quản lý bán hàng + tồn kho cơ bản | 3-10 triệu/năm (ước tính, nên kiểm tra bảng giá hiện hành) | SME bán lẻ |
| Odoo Inventory | Module kho trong ERP mã nguồn mở | 50-150 triệu/năm (gồm triển khai, ước tính) | SME vừa |
| SAP EWM, Oracle WMS | Quản lý kho chuyên sâu, tích hợp RFID | Hàng tỷ/năm | Doanh nghiệp lớn |

### 5.2. Template: Bảng tính EOQ và Safety Stock

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

**Công thức Excel/Google Sheets tương ứng** (giả sử D ở ô B1, S ở B2, H ở B3, L ở B4, σd ở B5, mức phục vụ ở B6, số ngày làm việc ở B7):

| Chỉ tiêu | Công thức |
|---|---|
| EOQ | `=SQRT(2*B1*B2/B3)` |
| Số lần đặt hàng/năm | `=B1/EOQ` |
| Nhu cầu ngày d | `=B1/B7` |
| Hệ số Z | `=NORM.S.INV(B6)` |
| Safety Stock | `=Z*B5*SQRT(B4)` |
| ROP | `=d*B4+SS` |
| Newsvendor Q* | `=NORM.INV(Cu/(Cu+Co), mu, sigma)` |
| Vòng quay tồn kho | `=COGS/AVERAGE(tồn đầu, tồn cuối)` |
| Cảnh báo chạm ROP | `=IF(Tồn_hiện_tại<=ROP,"ĐẶT HÀNG","OK")` |

### 5.3. Sơ đồ quyết định hệ thống kiểm soát tồn kho

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

### 5.4. Vai trò của mã vạch (Barcode), RFID và IoT

| Công nghệ | Cách hoạt động | Ưu điểm | Nhược điểm | Chi phí đầu tư (ước tính) |
|---|---|---|---|---|
| Mã vạch (Barcode) | Quét từng mã một để ghi nhận nhập/xuất | Chi phí thấp, dễ triển khai | Phải quét từng đơn vị, tốn nhân công | 5-20 triệu (máy quét + phần mềm) |
| RFID (Radio Frequency ID) | Đọc nhiều thẻ cùng lúc qua sóng radio | Kiểm kê nhanh gấp nhiều lần, giảm nhân công | Chi phí thẻ và đầu đọc cao hơn | 100 triệu - vài tỷ tuỳ quy mô |
| IoT Sensor | Cảm biến theo dõi điều kiện bảo quản (nhiệt độ, độ ẩm) | Phù hợp hàng nhạy cảm (thực phẩm, dược phẩm) | Cần hạ tầng kết nối và bảo trì | Thường 200 triệu trở lên (ước tính) |

Một số nhà bán lẻ lớn quốc tế (như Decathlon, Uniqlo) được báo cáo đã triển khai RFID trên diện rộng để rút ngắn đáng kể thời gian kiểm kê và giảm sai lệch tồn kho (mức độ cụ thể chưa kiểm chứng nên không nêu số). Quyết định RFID phải dựa trên bài toán kinh tế: xem Bài tập 10.

### 5.5. Quản trị tồn kho đa kênh (Omnichannel Inventory Management)

Với bán hàng đa kênh (cửa hàng, website, sàn thương mại điện tử, mạng xã hội), cần giải quyết:

- **Tồn kho hợp nhất (Unified Inventory)**: một nguồn dữ liệu tồn kho duy nhất cho mọi kênh, tránh bán trùng khi chỉ còn 1 đơn vị.
- **Ship-from-store**: dùng tồn kho tại cửa hàng để giao đơn online gần khách nhất.
- **Click-and-Collect**: khách đặt online, nhận tại cửa hàng - cần đồng bộ thời gian thực giữa online và offline.

**Thách thức phổ biến**: nhiều doanh nghiệp Việt Nam giai đoạn đầu chuyển đổi số bị "bán ảo" (oversell) trên sàn thương mại điện tử vì tồn kho online không đồng bộ real-time với kho thực, dẫn đến huỷ đơn và ảnh hưởng uy tín gian hàng. Giải pháp: dùng phần mềm đồng bộ đa kênh, giữ một "tồn kho đệm" (buffer) cho mỗi sàn (ví dụ để lại 1-2 đơn vị không đăng bán), quy trình trừ kho ngay khi có đơn.

### 5.6. Tồn kho trong thương mại điện tử: Fulfillment và kho phân tán

```
Mô hình kho tập trung (Centralized)        Mô hình kho phân tán (Distributed)

        ┌──────────┐                        ┌─────┐   ┌─────┐   ┌─────┐
        │  Kho     │                        │ Kho │   │ Kho │   │ Kho │
        │ Trung tâm│                        │ Bắc │   │Trung│   │ Nam │
        └────┬─────┘                        └──┬──┘   └──┬──┘   └──┬──┘
             │                                 │         │         │
    ┌────────┼────────┐                        ▼         ▼         ▼
    ▼        ▼        ▼                     Khách hàng Khách hàng Khách hàng
 KH Bắc   KH Trung   KH Nam                    Bắc      Trung      Nam
(giao xa,  ...        ...                (giao nhanh, chi phí vận chuyển thấp,
 chi phí vận                              nhưng quản lý tồn kho phức tạp hơn)
 chuyển cao)
```

Đánh đổi chính: kho tập trung đơn giản hơn và giảm tổng SS cần thiết nhờ gộp rủi ro (mục 2.7), nhưng kho phân tán giảm thời gian và chi phí giao hàng chặng cuối (last-mile). Doanh nghiệp thương mại điện tử lớn ở Việt Nam thường dùng mô hình lai: kho trung tâm cho hàng chậm luân chuyển, kho vệ tinh khu vực cho hàng bán chạy cần giao nhanh.

---

## VI. Bài tập thực hành

> Đáp án tính toán đã được kiểm tra lại bằng Python. Các bài thực hành thực tế (bài 11-14) có hướng dẫn thay vì đáp số.

**Bài 1 (EOQ)**. Một xưởng mắm cần $D = 9{,}000$ chai/năm; chi phí đặt hàng $S = 240{,}000$ VNĐ/lần; giá mua 40,000 VNĐ/chai, tỷ lệ lưu kho 25%/năm. Tính EOQ, số lần đặt, chu kỳ đặt (360 ngày) và tổng chi phí tối ưu.

*Đáp án*: $H = 0.25 \times 40{,}000 = 10{,}000$; $EOQ = \sqrt{2 \times 9{,}000 \times 240{,}000 / 10{,}000} = \sqrt{432{,}000} \approx 657$ chai; $N^* = 9{,}000 / 657.3 \approx 13.7$ lần/năm; $T^* = 360 / 13.7 \approx 26.3$ ngày; $TC^* = \sqrt{2DSH} \approx 6.57$ triệu VNĐ/năm.

**Bài 2 (SS và ROP theo 3 mức phục vụ)**. $d = 30$ đơn vị/ngày, $\sigma_d = 6$, $L = 4$ ngày, $H = 10{,}000$ VNĐ/đơn vị/năm. Tính SS, ROP và chi phí giữ SS cho mức 90%, 95%, 99%.

*Đáp án*: $\sigma_d\sqrt{L} = 6 \times 2 = 12$.

| Mức phục vụ | Z | SS = 12Z | ROP = 120 + SS | Chi phí giữ SS/năm |
|---|---|---|---|---|
| 90% | 1.28 | 15.4 | 135.4 | 153,600 |
| 95% | 1.65 | 19.8 | 139.8 | 198,000 |
| 99% | 2.33 | 28.0 | 148.0 | 279,600 |

Từ 95% lên 99% tốn thêm khoảng 8.2 đơn vị SS (~81,600 VNĐ/năm); quyết định có đáng hay không tuỳ vào lãi biên mất đi khi hết hàng.

**Bài 3 (ABC)**. Cho 12 mã (nhu cầu/năm × đơn giá VNĐ): A 1,800 × 50,000; B 300 × 200,000; C 5,000 × 4,000; D 900 × 35,000; E 150 × 120,000; F 2,500 × 8,000; G 60 × 400,000; H 1,200 × 12,000; I 3,000 × 3,000; J 400 × 20,000; K 800 × 5,000; L 700 × 2,000. Phân loại ABC với quy tắc A đến ≤ 70% tích luỹ, B đến ≤ 90%, còn lại C.

*Đáp án*: tổng giá trị 300.3 triệu. Thứ tự: A 90.0 (30.0%) → B 60.0 (50.0%) → D 31.5 (60.4%) → G 24.0 (68.4%) → C 20.0 (75.1%) → F 20.0 (81.8%) → E 18.0 (87.7%) → H 14.4 (92.5%) → I 9.0 (95.5%) → J 8.0 (98.2%) → K 4.0 (99.5%) → L 1.4 (100%) (đơn vị triệu VNĐ, % tích luỹ trong ngoặc). **Nhóm A**: A, B, D, G (4 mã = 33% số mã, 68.4% giá trị); **nhóm B**: C, F, E (3 mã, 19.3% giá trị); **nhóm C**: H, I, J, K, L (5 mã, 12.3%). Vẽ biểu đồ Pareto bằng cột giá trị + đường % tích luỹ.

**Bài 4 (Newsvendor)**. Shop hoa bán hoa hồng Valentine: giá bán 120,000, giá vốn 50,000, hoa dư cuối ngày chỉ bán được 10,000 VNĐ/bó. Nhu cầu trung bình 500 bó, $\sigma = 100$. Xác định số bó nên đặt.

*Đáp án*: $C_u = 70{,}000$; $C_o = 40{,}000$; $CR = 70/110 = 0.636$; $Z \approx 0.349$; $Q^* = 500 + 0.349 \times 100 \approx 535$ bó.

**Bài 5 (chiết khấu số lượng)**. $D = 6{,}000$; $S = 100{,}000$; $i = 20\%$. Giá: Q < 300: 50,000; 300-799: 48,000; từ 800: 46,000 VNĐ. Chọn Q tối ưu.

*Đáp án*:

| Giá | H | EOQ | Q dùng | TC (VNĐ) |
|---|---|---|---|---|
| 50,000 | 10,000 | 346 (ngoài khoảng <300) | 299 | 303,501,689 |
| 48,000 | 9,600 | 353.6 (hợp lệ) | 354 | ≈ 291,394,113 |
| 46,000 | 9,200 | 361 (dưới 800) | 800 | **280,430,000** |

Chọn mua 800 đơn vị/lần giá 46,000; tiết kiệm ≈ 10.96 triệu/năm so với phương án giá 48,000 (còn phải kiểm tra sức chứa kho và hạn sử dụng).

**Bài 6 (Risk Pooling)**. 4 kho khu vực, mỗi kho $\sigma_d = 20$/ngày, $L = 9$ ngày, mức phục vụ 95%, nhu cầu các kho độc lập. So sánh tổng SS khi giữ 4 kho riêng và khi gộp 1 kho.

*Đáp án*: Kho riêng: $1.65 \times 20 \times 3 = 99$ mỗi kho, tổng 396. Gộp: $\sigma = 20 \times \sqrt{4} = 40$, $SS = 1.65 \times 40 \times 3 = 198$ (giảm 50%; đúng quy luật $1/\sqrt{n}$ khi $n = 4$). Nếu tương quan càng cao, mức giảm càng ít.

**Bài 7 (Vòng quay, DIO, CCC)**. COGS 2,400 triệu; tồn đầu 380, cuối 420 triệu; DSO = 25, DPO = 30 ngày. Tính vòng quay, DIO, CCC; nếu giảm DIO 10 ngày thì giải phóng bao nhiêu tiền?

*Đáp án*: Tồn bình quân 400; vòng quay $= 2{,}400/400 = 6$; $DIO = 365/6 \approx 60.8$; $CCC = 60.8 + 25 - 30 = 55.8$ ngày; giải phóng $2{,}400 \times 10 / 365 \approx 65.8$ triệu VNĐ.

**Bài 8 (Kanban)**. $d = 600$ chi tiết/ngày, chu kỳ bổ sung $L = 0.25$ ngày, $\alpha = 20\%$, thùng 30 chi tiết. Tính số thẻ và tồn kho tối đa.

*Đáp án*: $N = 600 \times 0.25 \times 1.2 / 30 = 6$ thẻ; tồn kho tối đa $= 6 \times 30 = 180$ chi tiết.

**Bài 9 (Order-up-to)**. Hệ thống định kỳ: $d = 40$, $\sigma_d = 10$, $R = 14$ ngày, $L = 6$ ngày, mức phục vụ 95%. Tính S.

*Đáp án*: $R + L = 20$; $SS = 1.65 \times 10 \times \sqrt{20} \approx 73.8$; $S = 40 \times 20 + 73.8 \approx 874$. Nếu tồn hiện có + đang về là 310 thì đặt $874 - 310 = 564$.

**Bài 10 (RFID so với mã vạch, chuỗi 20 cửa hàng, số giả định)**. RFID: đầu tư 120 triệu/cửa hàng, chi phí thẻ 900 triệu/năm cho cả chuỗi; mã vạch: 12 triệu/cửa hàng. Lợi ích RFID so với mã vạch: tiết kiệm nhân công kiểm kê 30 giờ × 12 lần/năm × 20 cửa hàng × 40,000 VNĐ/giờ; giảm thất thoát/bán lỡ làm tăng 2% doanh thu chuỗi (120 tỷ/năm), biên lợi nhuận gộp 35%. Có nên đầu tư RFID?

*Đáp án*: Đầu tư chênh lệch $= 20 \times (120 - 12) = 2{,}160$ triệu. Lợi ích/năm: nhân công $= 30 \times 12 \times 20 \times 40{,}000 = 288$ triệu; doanh thu thêm $= 120{,}000 \times 2\% \times 35\% = 840$ triệu → 1,128 triệu. Trừ chi phí thẻ 900 triệu → ròng 228 triệu/năm. Hoàn vốn $= 2{,}160 / 228 \approx 9.5$ năm: **không hấp dẫn** (so với vòng đời công nghệ). Kết luận: chỉ nên dùng RFID cho nhóm hàng giá trị cao, hoặc chờ chi phí thẻ giảm, hoặc dùng mã vạch.

**Bài 11 (thực hành - phân tích hết hàng)**. Phân tích một trường hợp hết hàng (stockout) bạn từng gặp: nguyên nhân do ROP tính sai, SS không đủ hay lead time thực tế dài hơn? *Hướng dẫn*: thu thập nhu cầu và lead time thực tế 3 tháng, tính lại $\sigma_d$, $\sigma_L$, tính SS theo công thức có $\sigma_L$ (mục 1.4.3) và so với mức đã dùng.

**Bài 12 (thực hành - thiết kế quy trình)**. Thiết kế quy trình cycle counting cho danh mục đã ABC ở bài 3 (tần suất, người thực hiện, xử lý sai lệch); áp dụng FEFO cho một ngành hàng có hạn dùng (thực phẩm, dược phẩm, mỹ phẩm) bạn quen thuộc.

**Bài 13 (thực hành - Excel)**. Xây dựng bảng theo dõi tồn kho mẫu với công thức tự động cảnh báo khi chạm ROP, dùng các công thức ở mục 5.2.

**Bài 14 (tình huống)**. (a) Nghiên cứu Toyota và khủng hoảng chip, viết phân tích về đánh đổi giữa JIT thuần tuý và tồn kho đệm chiến lược. (b) Phân tích tình huống "bán ảo" trên sàn thương mại điện tử, đề xuất giải pháp kỹ thuật và quy trình. (c) Đề xuất lộ trình chuyển từ kiểm soát định kỳ sang liên tục cho một SME giả định, kèm chi phí ước tính (tham khảo mục 4.2).

---

## PHỤ LỤC: CHECKLIST QUẢN TRỊ TỒN KHO TỔNG HỢP

### A. Bảng thuật ngữ (Glossary)

| Thuật ngữ | Giải thích |
|---|---|
| EOQ | Economic Order Quantity - số lượng đặt hàng kinh tế tối ưu |
| ROP | Reorder Point - điểm đặt hàng lại |
| Safety Stock | Tồn kho an toàn, dự phòng biến động nhu cầu/lead time |
| ABC Analysis | Phân loại hàng hoá theo giá trị đóng góp (nguyên lý Pareto) |
| JIT | Just-In-Time - hệ thống sản xuất/cung ứng đúng lúc |
| Kanban | Thẻ tín hiệu điều phối sản xuất theo hệ thống kéo |
| Cycle Counting | Kiểm kê theo chu kỳ, không kiểm toàn bộ một lần |
| FEFO | First Expired First Out - xuất hàng có hạn sử dụng gần nhất trước |
| DIO | Days of Inventory Outstanding - số ngày tồn kho bình quân |
| Newsvendor Model | Mô hình xác định số lượng đặt hàng tối ưu cho sản phẩm bán theo một chu kỳ |
| Risk Pooling | Gộp rủi ro: gộp kho giúp giảm tổng tồn kho an toàn |
| VMI | Vendor Managed Inventory - nhà cung cấp quản lý tồn kho tại kho khách hàng |
| Consignment Inventory | Tồn kho ký gửi - nhà cung cấp giữ quyền sở hữu đến khi khách dùng/bán |

### B. Bảng đo lường KPI tồn kho

| KPI | Công thức | Mục tiêu tham khảo |
|---|---|---|
| Vòng quay tồn kho | COGS / Tồn kho bình quân | Theo ngành, càng cao càng tốt |
| Tỷ lệ hết hàng (Stockout Rate) | Số lần hết hàng / Tổng số lần kiểm tra | < 5% |
| Độ chính xác tồn kho (Inventory Accuracy) | Số SKU khớp giữa hệ thống và thực tế / Tổng SKU | > 95% |
| Tỷ lệ hàng lỗi thời (Obsolete %) | Giá trị hàng tồn > 6-12 tháng / Tổng tồn kho | < 5% |
| Tỷ lệ đáp ứng đơn hàng (Fill Rate) | Số đơn đáp ứng đầy đủ / Tổng số đơn | > 95% |
| Chi phí lưu kho trên doanh thu | Tổng chi phí lưu kho / Doanh thu | 2-6% tuỳ ngành (tham khảo) |

### C. Sổ tay rủi ro tồn kho (Risk Register mẫu)

| Rủi ro | Xác suất | Tác động | Biện pháp giảm thiểu |
|---|---|---|---|
| Dự báo nhu cầu sai lệch lớn | Trung bình | Cao | Cải thiện dự báo, theo dõi biến động thị trường |
| NCC giao hàng trễ | Trung bình | Trung bình | Tăng Safety Stock, đa dạng hoá NCC |
| Hàng lỗi thời/hết hạn | Thấp-Trung bình | Trung bình | FEFO, cảnh báo tự động, thanh lý sớm |
| Sai lệch số liệu hệ thống vs thực tế | Trung bình | Trung bình | Cycle counting thường xuyên |
| Oversell trên kênh thương mại điện tử | Trung bình | Trung bình | Đồng bộ tồn kho real-time giữa các kênh |
| Biến động giá nguyên liệu đầu vào | Cao | Trung bình | Hợp đồng giá cố định ngắn hạn, theo dõi thị trường |

### D. Bảng công thức tổng hợp

| Mục tiêu | Công thức |
|---|---|
| Số lượng đặt hàng tối ưu | $EOQ = \sqrt{2DS/H}$ |
| Số lần đặt hàng/năm | $N^* = D / Q^*$ |
| Tổng chi phí biến đổi tối ưu | $TC^* = \sqrt{2DSH}$ |
| Điểm đặt hàng lại | $ROP = d \times L + SS$ |
| Tồn kho an toàn (nhu cầu biến động) | $SS = Z \times \sigma_d \times \sqrt{L}$ |
| Tồn kho an toàn (nhu cầu + lead time biến động) | $SS = Z \times \sqrt{L\sigma_d^2 + d^2\sigma_L^2}$ |
| Mức tồn mục tiêu (hệ thống định kỳ) | $S = d(R+L) + Z\sigma_d\sqrt{R+L}$ |
| Tổng chi phí có chiết khấu số lượng | $TC = \frac{D}{Q}S + \frac{Q}{2}H + DP$ |
| EOQ có cho phép thiếu hàng | $Q^*_b = EOQ \times \sqrt{(H+B)/B}$ |
| Tỷ lệ phục vụ tối ưu (Newsvendor) | $CR = C_u / (C_u + C_o)$ |
| Số thẻ Kanban | $N = d \times L \times (1+\alpha) / C$ |
| Vòng quay tồn kho / DIO | $COGS / \text{Tồn bình quân}$; $365 / \text{Vòng quay}$ |
| Chu kỳ chuyển đổi tiền mặt | $CCC = DIO + DSO - DPO$ |
| Gộp rủi ro (độc lập, n kho giống nhau) | $\sigma_{gộp} = \sigma\sqrt{n}$ |

### E. Checklist rà soát trước khi áp dụng

**Chuẩn bị dữ liệu**
- □ Đã có danh mục SKU với nhu cầu 12 tháng gần nhất và đơn giá/giá vốn
- □ Đã ước lượng chi phí đặt hàng $S$ và chi phí lưu kho $H$ (tỷ lệ % giá vốn)
- □ Đã đo lead time thực tế và độ lệch chuẩn của nó (không chỉ lead time hứa hẹn)
- □ Đã tính $\sigma_d$ từ dữ liệu bán hàng theo ngày/tuần

**Phân loại và chính sách**
- □ Đã phân loại ABC (và cân nhắc XYZ/hàng nhạy cảm)
- □ Mức phục vụ được chọn theo hậu quả thiếu hàng, từng nhóm khác nhau
- □ Nhóm A: có EOQ, SS, ROP; nhóm C: dùng kiểm tra định kỳ đặt gộp
- □ Đã kiểm tra ràng buộc thực tế: MOQ, sức chứa kho, quy cách đóng gói, hạn sử dụng
- □ Đã so sánh tổng chi phí khi có chiết khấu số lượng

**Vận hành**
- □ Có bảng ROP/cảnh báo tự động tại kho hoặc trong phần mềm
- □ Có lịch cycle counting theo ABC, và quy trình điều tra sai lệch
- □ Áp dụng FEFO cho hàng có hạn dùng; cảnh báo cận date 3 tháng
- □ Hàng thời vụ: đã dùng Newsvendor, đã thương lượng quyền đổi/trả hoặc đặt bổ sung
- □ Tồn kho đa kênh được đồng bộ; có đệm chống bán ảo

**Theo dõi và cải tiến**
- □ Theo dõi KPI: vòng quay, DIO, tỷ lệ hết hàng, độ chính xác tồn, hàng lỗi thời
- □ Cập nhật lại EOQ, SS hằng quý hoặc khi nhu cầu/lead time thay đổi
- □ Thanh lý hàng chậm theo quy tắc (ví dụ quá 6 tháng)
- □ Đánh giá rủi ro chuỗi cung ứng trước khi áp dụng JIT; giữ đệm cho linh kiện quan trọng
- □ Phối hợp với kế toán: dự phòng giảm giá hàng tồn kho, đánh giá CCC

---

## TÀI LIỆU THAM KHẢO

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
File này tập trung vào các công thức định lượng cốt lõi (EOQ, Safety Stock, ROP, Newsvendor) kết hợp với case study thực tiễn tại Việt Nam và quốc tế. Người đọc nên thực hành tính toán trực tiếp trên dữ liệu của chính doanh nghiệp mình thay vì chỉ ghi nhớ công thức. Các nội dung công nghệ (RFID, omnichannel) và nguyên lý gộp rủi ro phản ánh xu hướng chuyển đổi số trong quản trị tồn kho hiện đại tại cả doanh nghiệp lớn và SME Việt Nam.

*Tài liệu tham khảo bổ sung (nguồn gốc lý thuyết): Harris, F. W. (1913), "How Many Parts to Make at Once", Factory, The Magazine of Management; Wilson, R. H. (1934), "A Scientific Routine for Stock Control", Harvard Business Review; Arrow, K., Harris, T., & Marschak, J. (1951), "Optimal Inventory Policy", Econometrica; Eppen, G. (1979), "Effects of Centralization on Expected Costs in a Multi-Location Newsboy Problem", Management Science.*
