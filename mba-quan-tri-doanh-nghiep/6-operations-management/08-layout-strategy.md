# 08. Chiến lược Bố trí Mặt bằng (Layout Strategy)

> **Mục tiêu**: Hiểu bản chất của quyết định bố trí mặt bằng (đặt cái gì ở đâu để dòng chảy vật liệu, người và thông tin ngắn nhất, rẻ nhất, an toàn nhất), nắm các công cụ định lượng cốt lõi (REL Chart, Load-Distance, Center of Gravity, Line Balancing, Group Technology, SLP) và biết áp dụng từng bước cho SME Việt Nam với chi phí thấp.

## MỤC LỤC

- **I. Khái niệm & Lý thuyết**: định nghĩa, nguồn gốc, layout và chiến lược vận hành, 4 loại layout, layout bán lẻ/dịch vụ
- **II. Chi tiết từng công cụ/kỹ thuật**: REL Chart, From-To & Load-Distance, Center of Gravity, Line Balancing, Cellular/Group Technology, SLP, kỹ thuật layout bán lẻ, nguyên tắc thiết kế (một chiều, 5S, lối đi), tự động hoá & omnichannel, con người & bền vững, ưu/nhược điểm tổng hợp
- **III. Case Studies thực tế**: Toyota, IKEA, Vincom, chuỗi siêu thị thất bại, quán cà phê Hà Nội, phòng khám nha khoa, xưởng may Bình Dương, Tiki và Long Châu, **case SME mới: Xưởng nội thất Tân An (Load-Distance + Line Balancing)**
- **IV. Ứng dụng cho SME**: quy trình 6 bước, lộ trình, quy mô và chi phí, các bên liên quan, sai lầm thường gặp
- **V. Tools & Templates**
- **VI. Bài tập thực hành** (có đáp án tính toán)
- **PHỤ LỤC: CHECKLIST LAYOUT TỔNG HỢP** (checklist, thuật ngữ, KPI, sổ tay rủi ro, công thức, mức trưởng thành, câu hỏi tự kiểm tra)
- **TÀI LIỆU THAM KHẢO**

> **Quy ước số liệu**: các con số gắn nhãn "giả định minh họa" do tác giả tự thiết kế để làm rõ cách tính, không phải số liệu thật của doanh nghiệp được nhắc tên. Số liệu công ty thật (Toyota, IKEA, Vincom, Tiki, Long Châu...) chỉ được mô tả định tính ở mức chắc chắn; phần định lượng đi kèm là mô hình minh họa.

---

## I. KHÁI NIỆM & LÝ THUYẾT

### 1.1. Bố trí mặt bằng là gì và vì sao nó quan trọng?

Bố trí mặt bằng (Facility Layout) là việc sắp xếp vật lý các nguồn lực (máy móc, trạm làm việc, kho, quầy phục vụ, lối đi, khu chờ) trong một không gian nhất định sao cho dòng chảy của vật liệu, con người và thông tin đi qua không gian đó ngắn, trơn tru và rẻ nhất có thể.

**Vì sao đây là quyết định "nặng ký"?** Có ba lý do khiến layout khác hẳn đa số quyết định vận hành khác:

1. **Tốn kém và khó đảo ngược**: dời một dây chuyền hay dựng lại vách ngăn đồng nghĩa với dừng sản xuất, tháo lắp thiết bị, đi lại hệ thống điện nước. Sai lầm layout vì thế "đóng băng" trong nhiều năm.
2. **Tác động lặp lại hằng ngày**: một mét đi thừa mỗi lượt vận chuyển nghe nhỏ, nhưng nhân với hàng trăm lượt mỗi ngày và hàng nghìn ngày vận hành sẽ thành chi phí khổng lồ (xem ví dụ Load-Distance ở mục 2.2).
3. **Quyết định ràng buộc năng lực**: layout xác định trần công suất (capacity) và chi phí đơn vị của doanh nghiệp, vì năng lực không chỉ là số máy mà còn là máy được đặt ở đâu.

Vai trò cụ thể của layout:

- Giảm chi phí vận chuyển nội bộ (Material Handling Cost). Trong sản xuất, vận chuyển không tạo thêm giá trị cho khách hàng nên được xem là một dạng lãng phí (waste).
- Tối ưu hoá sử dụng diện tích, giảm diện tích chết.
- Làm trơn dòng chảy công việc, loại bỏ điểm nghẽn (bottleneck).
- Tăng an toàn lao động, tuân thủ PCCC và lối thoát hiểm.
- Với bán lẻ/dịch vụ: dẫn dắt hành vi khách hàng, tạo trải nghiệm và tăng doanh thu trên mỗi mét vuông.

### 1.2. Nguồn gốc và lịch sử phát triển

| Mốc | Nhân vật / Tổ chức | Đóng góp | Bối cảnh |
|---|---|---|---|
| 1913 | Henry Ford (Highland Park, Mỹ) | Dây chuyền lắp ráp di động (moving assembly line) cho xe Model T | Cần hạ giá thành để xe hơi trở thành hàng đại chúng; thời gian lắp mỗi xe giảm mạnh (con số cụ thể tuỳ nguồn) |
| 1950s | S. P. Mitrofanov (Liên Xô) | Đặt nền móng Group Technology: nhóm chi tiết tương tự để gia công chung | Sản xuất loạt nhỏ, đa chủng loại cần hiệu quả gần với sản xuất hàng loạt |
| 1955 | M. E. Salveson | Bài toán cân bằng dây chuyền (Assembly Line Balancing) được phát biểu chính thức | Cần phương pháp toán học để chia việc cho các trạm |
| 1961 | Richard Muther | Systematic Layout Planning (SLP), tái bản 1973 | Cần quy trình có hệ thống thay vì bố trí theo cảm tính |
| 1950-1970s | Toyota (Taiichi Ohno và cộng sự) | Cell sản xuất, dòng chảy một sản phẩm (one-piece flow), takt time trong Toyota Production System | Thị trường nhỏ, cần đa dạng mẫu mã mà vẫn ít tồn kho |
| 1980 | J. R. King | Thuật toán Rank Order Clustering để lập cell | Tự động hoá việc nhóm máy - chi tiết |
| 1999 | Paco Underhill | *Why We Buy*: quan sát khoa học hành vi di chuyển của khách trong cửa hàng | Bán lẻ cần dữ liệu thay vì trực giác để thiết kế layout |

Dòng chảy lịch sử có thể tóm gọn: từ chỗ bố trí "máy ở đâu tiện thì đặt", ngành vận hành tiến đến coi layout là một bài toán tối ưu có dữ liệu (khối lượng di chuyển, khoảng cách, thời gian) và có quy trình (SLP).

### 1.3. Layout là hệ quả của chiến lược vận hành

Layout không đứng độc lập: nó phải khớp với **chiến lược quy trình** (xem File 01 - Phân tích thiết kế quy trình) và **ma trận khối lượng - chủng loại (Volume-Variety)**:

```
Chủng loại (Variety)
   ▲
Cao│  PROCESS LAYOUT          CELLULAR LAYOUT
   │  (xưởng cơ khí theo      (nhóm sản phẩm tương tự,
   │   đơn, bệnh viện)         khối lượng vừa)
   │
   │                          PRODUCT LAYOUT
Thấp│  FIXED-POSITION          (dây chuyền lắp ráp,
   │  (công trình, tàu:        khối lượng lớn, ít mẫu)
   │   khối lượng = 1)
   └──────────────────────────────────────────────▶ Khối lượng (Volume)
         Thấp                                  Cao
```

#### Tại sao khối lượng quyết định loại layout? Phân tích cấu trúc chi phí

Mỗi loại layout là một "canh bạc" khác nhau giữa **chi phí cố định** (đầu tư thiết bị chuyên dụng, dây chuyền) và **chi phí biến đổi trên mỗi đơn vị** (nhân công, vận chuyển, chờ đợi):

- Process layout: đầu tư thấp (máy đa năng), nhưng mỗi đơn vị phải đi vòng qua nhiều khu, chờ đợi nhiều, nên chi phí biến đổi cao.
- Product layout: đầu tư cao (dây chuyền, đồ gá, băng tải), nhưng mỗi đơn vị chảy thẳng nên chi phí biến đổi thấp.

Tổng chi phí mỗi layout là:

$$TC = FC + VC \times Q$$

Trong đó $TC$ là tổng chi phí, $FC$ là chi phí cố định (đồng), $VC$ là chi phí biến đổi mỗi đơn vị (đồng/đơn vị), $Q$ là sản lượng. Điểm hoà vốn giữa hai layout (sản lượng mà tại đó hai layout tốn kém như nhau):

$$Q^* = \frac{FC_{product} - FC_{process}}{VC_{process} - VC_{product}}$$

**Ví dụ step-by-step (giả định minh họa)**: xưởng so sánh hai phương án:

| Phương án | FC (đồng) | VC (đồng/đơn vị) |
|---|---|---|
| Process layout | 200.000.000 | 90.000 |
| Product layout | 900.000.000 | 40.000 |

- Bước 1: chênh lệch cố định = 900.000.000 - 200.000.000 = 700.000.000
- Bước 2: chênh lệch biến đổi = 90.000 - 40.000 = 50.000
- Bước 3: $Q^* = 700.000.000 / 50.000 = 14.000$ đơn vị

Kiểm chứng: tại $Q = 14.000$ cả hai đều tốn 1.460.000.000; tại $Q = 10.000$ process rẻ hơn (1,10 tỷ so với 1,30 tỷ); tại $Q = 20.000$ product rẻ hơn (1,70 tỷ so với 2,00 tỷ).

**Diễn giải kinh doanh**: nếu nhu cầu chắc chắn trên 14.000 đơn vị trong vòng đời thiết bị thì đầu tư dây chuyền là hợp lý; nếu nhu cầu thấp hoặc bất định, giữ process layout (rẻ, linh hoạt) là phương án an toàn hơn. Đây là lý do SME mới khởi nghiệp hiếm khi nên bắt đầu bằng dây chuyền cố định.

### 1.4. Bốn loại hình bố trí mặt bằng cơ bản

```
┌─────────────────────────────────────────────────────────┐
│  1. LAYOUT THEO QUY TRÌNH (Process Layout)               │
│     Nhóm các máy/chức năng giống nhau lại với nhau        │
│     VD: Bệnh viện (khoa X-quang, khoa nội, khoa ngoại)    │
├─────────────────────────────────────────────────────────┤
│  2. LAYOUT THEO SẢN PHẨM (Product Layout)                │
│     Sắp xếp theo trình tự các bước sản xuất tuần tự       │
│     VD: Dây chuyền lắp ráp ô tô, chuyền may               │
├─────────────────────────────────────────────────────────┤
│  3. LAYOUT VỊ TRÍ CỐ ĐỊNH (Fixed-Position Layout)         │
│     Sản phẩm đứng yên, nguồn lực di chuyển đến             │
│     VD: Đóng tàu, xây dựng công trình, sản xuất máy bay   │
├─────────────────────────────────────────────────────────┤
│  4. LAYOUT DẠNG Ô/NHÓM (Cellular Layout)                  │
│     Nhóm máy móc thành các "tế bào" xử lý họ sản phẩm      │
│     tương tự (Group Technology)                            │
│     VD: Nhà máy linh kiện đa dạng nhưng theo họ           │
└─────────────────────────────────────────────────────────┘
```

Minh hoạ dòng chảy của hai loại phổ biến nhất:

```
PROCESS LAYOUT (đơn hàng đi "vòng" giữa các khu):

 [Cưa] ──────► [Phay] ◄──────┐
   ▲   ╲                      │      Đơn 1: Cưa→Phay→Sơn→Lắp
   │    ╲_____► [Sơn]         │      Đơn 2: Phay→Cưa→Lắp
 [Kho]            │           │      => đường đi đan chéo, dài
   ▲              ▼           │
   └──────── [Lắp ráp] ◄──────┘

PRODUCT LAYOUT (dòng chảy một chiều):

 [Kho]─►[Cưa]─►[Phay]─►[Sơn]─►[Lắp ráp]─►[Kho TP]
```

#### Bảng so sánh ưu - nhược điểm 4 loại layout

| Loại layout | Ưu điểm | Nhược điểm | Phù hợp khi |
|---|---|---|---|
| Process | Linh hoạt cao, máy đa năng, hỏng một máy ít ảnh hưởng toàn hệ | Vận chuyển nội bộ cao, WIP lớn, khó lập lịch, thời gian chu kỳ dài | Đa dạng sản phẩm, khối lượng thấp, làm theo đơn (make-to-order) |
| Product | Năng suất cao, chi phí đơn vị thấp, dễ kiểm soát | Thiếu linh hoạt; một trạm hỏng dừng cả chuyền; công việc đơn điệu | Khối lượng lớn, ổn định, ít mẫu mã |
| Fixed-Position | Phù hợp sản phẩm quá lớn/phức tạp không di chuyển được | Chi phí di chuyển nguồn lực cao, khó tối ưu không gian công trường | Công trình, tàu, máy bay, thi công SME (xây nhà, lắp đặt) |
| Cellular | Kết hợp tính linh hoạt và năng suất, giảm WIP, tăng trách nhiệm theo nhóm | Phân tích Group Technology ban đầu phức tạp, máy trùng lặp nhiều hơn | Khối lượng trung bình, họ sản phẩm có quy trình tương tự |

#### Sơ đồ quyết định chọn loại layout

```
   Sản phẩm đa dạng, khối lượng thấp?
        /                    \
      Có                    Không
       │                       │
  PROCESS LAYOUT      Sản phẩm cố định lớn (tàu, nhà)?
  (hoặc thử Cellular        /            \
   nếu có họ sản phẩm)    Có             Không
                           │                │
                 FIXED-POSITION      Khối lượng lớn, ít mẫu mã?
                    LAYOUT                /         \
                                        Có          Không
                                         │             │
                                PRODUCT LAYOUT   CELLULAR LAYOUT
```

#### Fixed-Position layout trong SME: công trường xây dựng và thi công

Với layout vị trí cố định, bài toán không còn là "đặt máy ở đâu" mà là "đặt kho vật liệu, khu gia công và lối đi quanh sản phẩm đứng yên ở đâu". Nguyên tắc: đặt vật liệu dùng nhiều và nặng nhất gần điểm sử dụng, theo thứ tự thi công (vật liệu dùng trước đặt ở vị trí dễ lấy), chừa lối cho cẩu/xe và lối thoát hiểm. Cùng tư duy áp dụng cho nhà thầu hoàn thiện nội thất, đội lắp điều hoà: sắp xếp xe, vật tư và dụng cụ theo thứ tự thao tác tại hiện trường.

### 1.5. Layout bán lẻ và dịch vụ (Retail/Service Layout)

Với bán lẻ và dịch vụ, ngoài việc giảm di chuyển, layout còn phải **tối đa hoá doanh thu trên mỗi mét vuông** (Sales per Square Meter) bằng cách dẫn dắt khách đi qua các khu vực trưng bày quan trọng và tạo trải nghiệm phù hợp thương hiệu.

| Mô hình | Mô tả | Ưu điểm | Nhược điểm | Ví dụ điển hình |
|---|---|---|---|---|
| Grid (lưới) | Các dãy kệ song song, lối đi thẳng | Tối ưu diện tích trưng bày, dễ tìm hàng | Ít thú vị, ít gợi ý mua thêm | Siêu thị, hiệu thuốc |
| Free-Flow (tự do) | Bố trí kệ/bàn không theo lưới, khách tự chọn lối | Khuyến khích khám phá, thương hiệu cao cấp | Dùng diện tích kém hiệu quả hơn, khó kiểm soát | Cửa hàng thời trang |
| Loop/Racetrack (vòng) | Một lối đi chính dẫn khách qua toàn bộ khu trưng bày | Mọi khu đều được nhìn thấy | Khó chịu nếu khách chỉ muốn mua nhanh | IKEA, Vincom (khu ẩm thực/rạp ở tầng trên) |

Dịch vụ như nhà hàng, phòng khám, spa còn có "servicescape" (môi trường dịch vụ): khách và nhân viên cùng nằm trong không gian, nên layout phải cân bằng giữa **hiệu quả phục vụ** (đường đi nhân viên ngắn) và **trải nghiệm** (riêng tư, âm thanh, ánh sáng).

---

## II. CHI TIẾT TỪNG CÔNG CỤ/KỸ THUẬT

### 2.1. Sơ đồ quan hệ hoạt động (Activity Relationship Chart - REL Chart)

**Vấn đề giải quyết**: không phải mọi mối quan hệ giữa các bộ phận đều đo được bằng số chuyến vận chuyển (ví dụ văn phòng quản đốc cần gần xưởng để giám sát, khu sơn cần xa khu hàn vì tia lửa). Muther đưa ra REL Chart để ghi lại **mức độ cần gần nhau** (kể cả lý do định tính) trong một bảng tam giác dễ đọc.

**Thang đo** (kèm điểm số thông dụng để tính tổng xếp hạng, quy ước có thể khác giữa tài liệu):

| Mã | Ý nghĩa | Điểm (quy ước) | Ví dụ |
|---|---|---|---|
| A | Tuyệt đối cần gần (Absolutely necessary) | 4 | Sản xuất và đóng gói chung băng tải |
| E | Đặc biệt quan trọng (Especially important) | 3 | Kho nguyên liệu và sản xuất |
| I | Quan trọng (Important) | 2 | Sản xuất và văn phòng quản đốc |
| O | Bình thường (Ordinary) | 1 | |
| U | Không quan trọng (Unimportant) | 0 | Kho và văn phòng |
| X | Không nên gần nhau (Undesirable) | -1 | Khu sơn và khu hàn, kho hoá chất và khu ăn |

**Tổng điểm gần kề (Total Closeness Rating - TCR)** của một bộ phận bằng tổng điểm các quan hệ của nó. Bộ phận có TCR cao nằm ở "trung tâm" của sơ đồ.

**Ví dụ step-by-step** (dữ liệu là mẫu REL ở mục 5.2): Kho(K), Sản xuất(S), Đóng gói(D), Văn phòng(V) với quan hệ K-S = A, K-D = E, K-V = U, S-D = A, S-V = I, D-V = O.

| Bộ phận | Cộng điểm | TCR |
|---|---|---|
| Kho | K-S (A=4) + K-D (E=3) + K-V (U=0) | 7 |
| Sản xuất | K-S (4) + S-D (A=4) + S-V (I=2) | 10 |
| Đóng gói | K-D (3) + S-D (4) + D-V (O=1) | 8 |
| Văn phòng | K-V (0) + S-V (2) + D-V (1) | 3 |

**Diễn giải**: Sản xuất (10) là trung tâm, đặt ở giữa; Đóng gói (8) và Kho (7) ôm hai phía; Văn phòng (3) có thể đặt ở rìa. Đây là cơ sở để vẽ Block Layout ở bước SLP.

### 2.2. Ma trận Từ-Đến (From-To Chart) và phương pháp Load-Distance

**Vấn đề giải quyết**: khi có dữ liệu thật về số lượt di chuyển giữa các bộ phận, ta không cần chỉ "cảm thấy" nên đặt gần nhau; ta có thể tính ra tổng "công di chuyển" của mỗi phương án và chọn phương án nhỏ nhất. From-To Chart là bảng dữ liệu đầu vào; Load-Distance (còn gọi Weighted Distance) là phép đánh giá.

**Logic công thức**: chi phí vận chuyển nội bộ gần như tỷ lệ thuận với (số lượt) × (quãng đường) × (đơn giá một lượt trên mỗi mét). Vì vậy:

$$\text{Total Cost} = \sum_i \sum_j X_{ij} \cdot C_{ij} \cdot D_{ij}$$

Trong đó $X_{ij}$ là số lượt di chuyển giữa bộ phận $i$ và $j$ (lượt/ngày), $C_{ij}$ là chi phí cho mỗi lượt trên mỗi mét (đồng/lượt/mét), $D_{ij}$ là khoảng cách giữa hai bộ phận (mét). Khi $C_{ij}$ như nhau cho mọi cặp, ta bỏ nó đi và chỉ so sánh **Load-Distance**:

$$LD = \sum_i \sum_j f_{ij} \times d_{ij}$$

Trong đó $f_{ij}$ là tải (lượt/ngày) giữa $i$ và $j$, $d_{ij}$ là khoảng cách (mét). Với kho/xưởng có lối đi vuông góc, $d_{ij}$ thường dùng khoảng cách rectilinear (Manhattan): $d = |x_i - x_j| + |y_i - y_j|$ vì xe nâng không đi đường chéo xuyên tường.

**Ví dụ step-by-step: 4 bộ phận trên một dãy nhà dài (giả định minh họa)**. Các ô cách nhau 20 m; đơn giá 200 đồng/lượt/mét. Ma trận tải (lượt/ngày): Kho→SX 120; SX→Đóng gói (ĐG) 100; ĐG→Kho thành phẩm (KTP) 100; Kho→ĐG 10; SX→KTP 5.

Phương án 1 (hiện tại, xếp lệch): vị trí Kho = 0 m, KTP = 20 m, SX = 40 m, ĐG = 60 m.

| Cặp | Tải | Khoảng cách (m) | Tải × Khoảng cách | Chi phí (đồng/ngày) |
|---|---|---|---|---|
| Kho-SX | 120 | 40 | 4.800 | 960.000 |
| SX-ĐG | 100 | 20 | 2.000 | 400.000 |
| ĐG-KTP | 100 | 40 | 4.000 | 800.000 |
| Kho-ĐG | 10 | 60 | 600 | 120.000 |
| SX-KTP | 5 | 20 | 100 | 20.000 |
| **Tổng** | | | **11.500** | **2.300.000** |

Phương án 2 (xếp theo dòng chảy): Kho = 0, SX = 20, ĐG = 40, KTP = 60.

| Cặp | Tải | Khoảng cách (m) | Tải × Khoảng cách | Chi phí (đồng/ngày) |
|---|---|---|---|---|
| Kho-SX | 120 | 20 | 2.400 | 480.000 |
| SX-ĐG | 100 | 20 | 2.000 | 400.000 |
| ĐG-KTP | 100 | 20 | 2.000 | 400.000 |
| Kho-ĐG | 10 | 40 | 400 | 80.000 |
| SX-KTP | 5 | 40 | 200 | 40.000 |
| **Tổng** | | | **7.000** | **1.400.000** |

**Diễn giải**: chỉ bằng việc xếp theo dòng chảy, tổng chi phí giảm từ 2,3 triệu xuống 1,4 triệu đồng/ngày (giảm 39%), tức tiết kiệm 900.000 đồng/ngày, khoảng 23,4 triệu đồng/tháng (26 ngày). Trực giác "các bộ phận nối tiếp nhau thì đặt cạnh nhau" đúng, nhưng Load-Distance cho ta con số để thuyết phục chủ doanh nghiệp.

**Thuật toán hoán đổi (Pairwise Exchange)** cho layout theo quy trình: (1) tính LD hiện tại; (2) thử hoán đổi vị trí từng cặp bộ phận, tính LD mới; (3) chọn hoán đổi giảm nhiều nhất và thực hiện; (4) lặp lại đến khi không còn hoán đổi nào cải thiện. Phương pháp này là heuristic (không bảo đảm tối ưu toàn cục) nhưng rất thực dụng. Ví dụ đầy đủ với 6 bộ phận ở Case 3.9.

### 2.3. Phương pháp trọng tâm (Center of Gravity)

**Vấn đề giải quyết**: chọn vị trí nhà kho/trung tâm phân phối phục vụ nhiều điểm giao hàng có sản lượng khác nhau. Vị trí tốt phải "gần" các điểm nhiều hàng hơn các điểm ít hàng. Ý tưởng giống tìm **tâm khối lượng** trong vật lý: điểm cân bằng của một tấm ván có đặt các quả cân ở nhiều vị trí.

$$C_x = \frac{\sum_i x_i \cdot W_i}{\sum_i W_i}, \quad C_y = \frac{\sum_i y_i \cdot W_i}{\sum_i W_i}$$

Trong đó $(x_i, y_i)$ là toạ độ điểm $i$ (km trên bản đồ), $W_i$ là khối lượng vận chuyển đến/từ điểm $i$ (kiện/ngày). Công thức là **trung bình có trọng số** của toạ độ: điểm càng nhiều hàng càng "kéo" tâm về phía mình.

**Ví dụ step-by-step (giả định minh họa)**: kho trung tâm phục vụ 4 cửa hàng.

| Cửa hàng | x (km) | y (km) | W (kiện/ngày) | x × W | y × W |
|---|---|---|---|---|---|
| A | 2 | 9 | 400 | 800 | 3.600 |
| B | 8 | 7 | 300 | 2.400 | 2.100 |
| C | 5 | 2 | 500 | 2.500 | 1.000 |
| D | 10 | 3 | 200 | 2.000 | 600 |
| **Tổng** | | | **1.400** | **7.700** | **7.300** |

- $C_x = 7.700 / 1.400 = 5,5$ km
- $C_y = 7.300 / 1.400 \approx 5,21$ km

Kiểm chứng bằng tổng (khối lượng × khoảng cách đường chim bay): tại tâm (5,5; 5,21) tổng $\approx$ 5.613,5 kiện·km; nếu đặt ngay tại cửa hàng C (điểm nhiều hàng nhất) là 5.815,4 (cao hơn 3,6%); nếu đặt tại A là 7.705,3 (cao hơn 37%).

**Giới hạn cần nhớ**: (1) công thức tối thiểu hoá khoảng cách đường chim bay có trọng số một cách xấp xỉ, không phải chi phí thật theo đường phố; (2) bỏ qua giá thuê đất, hạ tầng, hạn chế giờ lưu thông xe tải vào nội đô. Hãy coi kết quả là **điểm xuất phát** rồi cân nhắc các địa điểm khả thi quanh đó.

### 2.4. Cân bằng dây chuyền (Line Balancing)

**Vấn đề giải quyết**: trong layout theo sản phẩm, công việc được chia thành nhiều trạm. Nếu trạm này làm 40 giây còn trạm kia 100 giây thì cả chuyền chỉ chạy nhanh bằng trạm chậm nhất, các trạm khác phải đứng chờ (thời gian nhàn rỗi - idle time). Cân bằng dây chuyền là chia các công việc nhỏ (task) vào các trạm sao cho thời gian mỗi trạm gần bằng nhau và vừa đủ đáp ứng nhu cầu của khách hàng.

**Bối cảnh lịch sử**: Salveson (1955) phát biểu bài toán dưới dạng toán học; Helgeson và Birnie (1961) đề xuất phương pháp Ranked Positional Weight (RPW) mà ta dùng dưới đây. "Takt" là từ tiếng Đức nghĩa là nhịp, được Toyota dùng để chỉ nhịp sản xuất khớp với nhịp của khách hàng.

#### 2.4.1. Các khái niệm và công thức (kèm lý do)

**Takt time** là khoảng thời gian tối đa được phép để hoàn thành một sản phẩm tại mỗi trạm để theo kịp nhu cầu:

$$\text{Takt time} = \frac{\text{Thời gian sản xuất khả dụng mỗi ngày}}{\text{Nhu cầu mỗi ngày}}$$

*Tại sao chia như vậy?* Nếu khách cần 210 sản phẩm một ngày và ta có 25.200 giây, thì trung bình cứ 120 giây phải có một sản phẩm rời chuyền. Làm nhanh hơn takt là sản xuất dư (lãng phí), làm chậm hơn là thiếu hàng. Thời gian khả dụng phải trừ giờ nghỉ, họp đầu ca, bảo trì định kỳ.

**Chu kỳ chuyền (Cycle time, $C$)**: thời gian tối đa mỗi trạm được dùng. Trong cân bằng chuyền chọn $C \le$ takt time và $C \ge$ thời gian của task dài nhất (vì một task không thể chia nhỏ giữa hai trạm).

**Số trạm tối thiểu lý thuyết**:

$$N_{min} = \left\lceil \frac{\sum t_i}{C} \right\rceil$$

Trong đó $\sum t_i$ là tổng thời gian của tất cả task (giây), $C$ là chu kỳ (giây); $\lceil \cdot \rceil$ làm tròn lên. *Tại sao làm tròn lên?* Không thể có 3,54 trạm; 3 trạm không đủ chỗ cho tổng thời gian, nên phải 4.

**Hiệu suất chuyền (Efficiency)**, **thời gian nhàn rỗi** và **độ trễ cân bằng (Balance Delay)**:

$$E = \frac{\sum t_i}{N \times C} \times 100\%, \qquad \text{Idle} = N \times C - \sum t_i, \qquad \text{Balance Delay} = 100\% - E$$

Trong đó $N$ là số trạm thực tế. *Ý nghĩa*: $E$ cho biết bao nhiêu phần trăm "thời gian trả lương" thực sự dành cho công việc có ích; phần còn lại là thời gian đứng chờ.

**Nguyên tắc phân bổ**: (1) tuân thủ **thứ tự ưu tiên (precedence)** (task B cần A xong); (2) tổng thời gian trong một trạm không vượt $C$. Phương pháp RPW chọn task nào đưa vào trạm trước theo **trọng số vị trí**:

$$RPW_i = t_i + \sum_{j \in \text{các task theo sau } i} t_j$$

*Tại sao RPW?* Task có nhiều việc phía sau phụ thuộc vào nó (trọng số lớn) nếu bị trì hoãn sẽ làm nghẽn cả chuỗi, nên được xếp sớm.

#### 2.4.2. Ví dụ step-by-step: chuyền lắp ráp ghế văn phòng (giả định minh họa)

Dữ liệu: 9 task, thời gian (giây) và quan hệ tiền nhiệm:

| Task | Công việc | Thời gian (s) | Tiền nhiệm |
|---|---|---|---|
| A | Lắp khung ghế | 50 | - |
| B | Lắp trục nâng | 40 | A |
| C | Lắp tựa lưng | 60 | A |
| D | Lắp tay vịn | 35 | B |
| E | Lắp bệ ngồi | 45 | B |
| F | Lắp bản lề điều chỉnh | 30 | C |
| G | Lắp chân ghế và bánh xe | 55 | D, E |
| H | Kiểm tra độ nghiêng | 40 | F |
| I | Đóng gói | 70 | G, H |
| | **Tổng** | **425** | |

Sơ đồ thứ tự:

```
        ┌─► B(40) ─┬─► D(35) ─┐
 A(50) ─┤          └─► E(45) ─┴─► G(55) ─┐
        └─► C(60) ──► F(30) ──► H(40) ───┴─► I(70)
```

**Bước 1 - Takt time**: ca làm 8 giờ, nghỉ 1 giờ, thời gian khả dụng = 7 giờ = 25.200 giây. Nhu cầu 210 ghế/ngày. Takt = 25.200 / 210 = **120 giây**. Task dài nhất (I = 70 giây) nhỏ hơn 120, nên chọn $C = 120$ được.

**Bước 2 - Số trạm tối thiểu**: $N_{min} = \lceil 425/120 \rceil = \lceil 3{,}54 \rceil = 4$.

**Bước 3 - Tính RPW** (task + tất cả task theo sau):

| Task | Các task theo sau | RPW |
|---|---|---|
| A | B, C, D, E, F, G, H, I (tất cả) | 425 |
| B | D, E, G, I | 40 + 35 + 45 + 55 + 70 = 245 |
| C | F, H, I | 60 + 30 + 40 + 70 = 200 |
| E | G, I | 45 + 55 + 70 = 170 |
| D | G, I | 35 + 55 + 70 = 160 |
| F | H, I | 30 + 40 + 70 = 140 |
| G | I | 55 + 70 = 125 |
| H | I | 40 + 70 = 110 |
| I | - | 70 |

Thứ tự ưu tiên theo RPW giảm dần: A, B, C, E, D, F, G, H, I.

**Bước 4 - Phân bổ vào các trạm** (mỗi trạm chọn task RPW cao nhất đã đủ điều kiện tiền nhiệm và còn vừa thời gian):

| Trạm | Task | Tổng thời gian (s) | Thời gian rảnh (s) | Giải thích chọn |
|---|---|---|---|---|
| 1 | A, B | 50 + 40 = 90 | 30 | A (425) trước; sau A, B (245) đủ điều kiện, 90 ≤ 120; C (60) không vừa vì 90 + 60 = 150 > 120; D, E cần B nên phải xếp sau B nhưng 90 + 45 = 135 > 120 |
| 2 | C, E | 60 + 45 = 105 | 15 | C (200) và E (170) đủ điều kiện; thêm D (35) thì 105 + 35 = 140 > 120 |
| 3 | D, F, G | 35 + 30 + 55 = 120 | 0 | D (35), F (30), G (55) đủ điều kiện khi D, E đã xong; vừa khít 120 |
| 4 | H, I | 40 + 70 = 110 | 10 | H sau F; I sau G và H |

Kiểm tra tiền nhiệm: E (trạm 2) cần B (trạm 1), thoả; G (trạm 3) cần D (trạm 3, đặt trước G) và E (trạm 2), thoả; I cần G và H, thoả.

**Bước 5 - Đánh giá**:
- Số trạm $N = 4$ bằng $N_{min}$, tức đạt tối ưu về số trạm.
- Hiệu suất $E = 425 / (4 \times 120) = 425/480 = 88{,}5\%$.
- Thời gian nhàn rỗi mỗi chu kỳ = 480 - 425 = **55 giây** (30 + 15 + 0 + 10).
- Độ trễ cân bằng = 100% - 88,5% = **11,5%**.
- Sản lượng = 25.200 / 120 = 210 ghế/ngày, đúng nhu cầu.

**Diễn giải kinh doanh**: trạm 3 là "nút cổ chai" (không có thời gian dư), nếu một công nhân ở đó chậm 5 giây là cả chuyền giảm sản lượng. Trạm 1 có 30 giây rảnh là chỗ tự nhiên để giao thêm việc phụ (kiểm tra vật tư) hoặc xử lý khi nhu cầu tăng.

**Tình huống "nhu cầu thay đổi"** (cùng 425 giây công việc, cùng thuật toán RPW):

| Nhu cầu/ngày | Takt = $C$ (s) | $N_{min}$ | Số trạm thực tế | Hiệu suất |
|---|---|---|---|---|
| 150 | 168 | 3 (2,53) | 3 | 84,3% |
| 210 | 120 | 4 (3,54) | 4 | 88,5% |
| 252 | 100 | 5 (4,25) | 5 | 85,0% |
| 280 | 90 | 5 (4,72) | 6 | 78,7% |

*Bài học*: hiệu suất không tăng đơn điệu theo sản lượng; ở nhu cầu 280 ghế/ngày, dù $N_{min} = 5$ nhưng ràng buộc tiền nhiệm và độ lớn task khiến phải dùng 6 trạm (hiệu suất 78,7%). Muốn cải thiện cần **chia nhỏ task** (ví dụ tách task I đóng gói 70 giây thành hai thao tác) hoặc **giảm thời gian task** bằng đồ gá.

### 2.5. Layout dạng ô (Cellular) và Group Technology

**Vấn đề giải quyết**: layout theo quy trình linh hoạt nhưng sản phẩm đi vòng, chờ lâu, WIP nhiều; layout theo sản phẩm hiệu quả nhưng chỉ khi khối lượng lớn. Cellular layout là "đường giữa": gom các máy cần thiết để làm trọn một **họ sản phẩm** vào một cell, sản phẩm chảy theo dòng chảy trong cell như một mini product layout.

**Bối cảnh**: Mitrofanov (Liên Xô, thập niên 1950) nhận ra các chi tiết có hình dáng/quy trình gia công tương tự có thể nhóm lại (Group Technology - GT), nhờ đó sản xuất loạt nhỏ đạt hiệu quả gần với hàng loạt. Toyota tích hợp tư duy này vào TPS.

#### 2.5.1. Lập cell bằng Rank Order Clustering (ROC)

Ta lập **ma trận máy - chi tiết** (1 = chi tiết cần máy đó), rồi sắp xếp hàng/cột sao cho các số 1 tụ về đường chéo thành các khối. ROC của King (1980) làm việc đó bằng cách coi mỗi hàng/cột là một số nhị phân và sắp xếp giảm dần luân phiên.

**Ví dụ step-by-step (giả định minh họa)**: 5 máy (M1..M5), 6 chi tiết (P1..P6). Ma trận ban đầu:

| | P1 | P2 | P3 | P4 | P5 | P6 |
|---|---|---|---|---|---|---|
| M1 | 1 | 0 | 1 | 0 | 0 | 1 |
| M2 | 0 | 1 | 0 | 1 | 1 | 0 |
| M3 | 1 | 0 | 1 | 0 | 0 | 0 |
| M4 | 0 | 1 | 0 | 1 | 0 | 0 |
| M5 | 0 | 0 | 0 | 1 | 1 | 0 |

- **Bước 1 - Giá trị nhị phân mỗi hàng** (cột trái nhất có trọng số lớn nhất, $2^5$ đến $2^0$): M1 = 101001 = 41; M2 = 010110 = 22; M3 = 101000 = 40; M4 = 010100 = 20; M5 = 000110 = 6. Sắp xếp giảm dần: M1 (41), M3 (40), M2 (22), M4 (20), M5 (6).
- **Bước 2 - Giá trị nhị phân mỗi cột** (theo thứ tự hàng mới M1, M3, M2, M4, M5, trọng số $2^4$ đến $2^0$): P1 = 11000 = 24; P2 = 00110 = 6; P3 = 11000 = 24; P4 = 00111 = 7; P5 = 00101 = 5; P6 = 10000 = 16. Sắp xếp giảm dần: P1 (24), P3 (24), P6 (16), P4 (7), P2 (6), P5 (5).
- **Bước 3 - Ma trận sau sắp xếp** (lặp lại thấy không đổi, thuật toán dừng):

| | P1 | P3 | P6 | P4 | P2 | P5 |
|---|---|---|---|---|---|---|
| M1 | 1 | 1 | 1 | | | |
| M3 | 1 | 1 | | | | |
| M2 | | | | 1 | 1 | 1 |
| M4 | | | | 1 | 1 | |
| M5 | | | | 1 | | 1 |

**Kết quả**: hai cell tách biệt hoàn toàn, không có "phần tử ngoại lệ" (số 1 nằm ngoài khối): **Cell 1** gồm máy M1, M3 làm họ chi tiết {P1, P3, P6}; **Cell 2** gồm máy M2, M4, M5 làm họ {P2, P4, P5}. Trong thực tế hiếm khi tách sạch như vậy: nếu một chi tiết dùng máy của cell khác, có thể nhân đôi máy (đầu tư thêm) hoặc chấp nhận chạy liên cell.

#### 2.5.2. Vì sao cell giảm lead time? Mô hình batch-and-queue so với one-piece flow

Giả sử sản xuất 100 chi tiết qua 4 công đoạn, mỗi công đoạn 2 phút/chi tiết (giả định minh họa):

- **Process layout (batch-and-queue)**: cả lô 100 chi tiết xong công đoạn 1 mới chuyển sang công đoạn 2: thời gian = 4 × 100 × 2 = **800 phút** (chưa tính chờ và vận chuyển).
- **Cell (dòng chảy từng chi tiết)**: chi tiết đầu ra sau 4 × 2 = 8 phút, sau đó mỗi 2 phút có thêm một chi tiết: thời gian = 8 + 99 × 2 = **206 phút**.
- Giảm = (800 - 206) / 800 = **74,3%**.

*Nguyên nhân*: trong layout theo lô, mỗi chi tiết đứng chờ 99 chi tiết khác trước khi sang trạm kế. Dòng chảy từng chi tiết xoá thời gian chờ đó. Điều kiện: các công đoạn trong cell phải cân bằng (cùng 2 phút), và máy phải gần nhau để không cần xe chuyển.

### 2.6. Systematic Layout Planning (SLP - Muther)

**Vấn đề giải quyết**: khi thiết kế layout thường gặp hai sai lầm: (1) bắt tay vẽ ngay mà chưa hiểu dòng chảy; (2) chỉ nhìn một khía cạnh (vận chuyển) mà bỏ qua yếu tố định tính (an toàn, giám sát). Richard Muther (1961) tạo SLP như một **quy trình 6 bước có hệ thống** kết hợp cả hai.

| Bước | Tên | Nội dung | Công cụ |
|---|---|---|---|
| 1 | Phân tích sản phẩm - số lượng (P-Q) | Sản phẩm nào chiếm sản lượng chính? Họ sản phẩm nào? | Biểu đồ Pareto theo sản phẩm |
| 2 | Phân tích dòng chảy vật liệu | Vật liệu đi qua bộ phận nào, bao nhiêu? | Flow process chart, From-To Chart |
| 3 | Phân tích quan hệ hoạt động | Bộ phận nào cần gần nhau, vì sao? | REL Chart, TCR |
| 4 | Sơ đồ quan hệ và nhu cầu không gian | Mỗi bộ phận cần bao nhiêu m², có sẵn bao nhiêu? | Space Requirement, Relationship Diagram |
| 5 | Sơ đồ bố trí khối (Block Layout) | Sắp các khối diện tích theo quan hệ | Block Layout, các phương án |
| 6 | Đánh giá và chọn phương án; chi tiết hoá (Detailed Layout) | Cân nhắc ràng buộc (cột, điện nước, PCCC), chấm điểm phương án | Load-Distance, ma trận trọng số |

Điểm mạnh của SLP là **tạo nhiều phương án** (thường 2-3 Block Layout) rồi chấm điểm chung theo tiêu chí định lượng (Load-Distance) và định tính (an toàn, linh hoạt), thay vì "thiết kế một phương án rồi bảo vệ nó".

### 2.7. Kỹ thuật layout bán lẻ: vùng nóng/lạnh, tầm mắt và mật độ doanh thu

**Vùng nóng - vùng lạnh (Hot Zone vs Cold Zone)**: "Vùng nóng" là khu khách thấy đầu tiên khi bước vào hoặc gần quầy thanh toán (nơi dễ mua bốc phát); "vùng lạnh" là góc khuất ít người qua lại. *Tại sao?* Khách thường rẽ theo thói quen và chỉ dừng ở nơi có kích thích thị giác; do đó đặt sản phẩm lợi nhuận cao/mới ở vùng nóng, đặt hàng thiết yếu mua hằng ngày (sữa, gạo) ở sâu bên trong để khách đi xuyên qua cả cửa hàng.

**Tầm mắt (Eye-Level Selling)**: sản phẩm ở khoảng 1,4-1,7 m thường được chú ý và chọn nhiều hơn so với kệ quá cao hoặc quá thấp. Đây là lý do nhà cung cấp trả phí chỗ bày (slotting fee) để được ở vị trí đẹp. Mức chênh lệch cụ thể tuỳ ngành hàng và cần đo bằng dữ liệu của chính cửa hàng; không áp dụng con số chung.

**Doanh thu trên mét vuông** (chỉ số chính cho bán lẻ):

$$\text{Sales per m}^2 = \frac{\text{Doanh thu (đồng/tháng)}}{\text{Diện tích trưng bày (m}^2)}$$

Ví dụ (giả định minh họa): cửa hàng 120 m² đạt doanh thu 1,8 tỷ đồng/tháng thì Sales per m² = 1.800.000.000 / 120 = **15.000.000 đồng/m²/tháng**. Chỉ số này so sánh với chính mình theo thời gian và giữa các cửa hàng cùng chuỗi, cần ghép với biên lợi nhuận gộp: doanh thu/m² cao nhưng biên gộp thấp chưa chắc tốt.

**Phân bổ không gian cho khu vực**: nguyên tắc ưu tiên khu có lợi nhuận gộp trên mét vuông cao và gắn với khu tạo lưu lượng (traffic builder). Ví dụ phân bổ của hiệu thuốc theo ba biến thể diện tích ở Case 3.8.

### 2.8. Nguyên tắc thiết kế dòng chảy, 5S và lối đi

#### 2.8.1. Dòng chảy một chiều (One-Way Flow)

Thiết kế dòng chảy vật liệu/khách hàng theo một hướng duy nhất, tránh đi ngược chiều hoặc cắt ngang gây tắc nghẽn. *Tại sao?* Mỗi lần dòng chảy cắt nhau là một điểm nghẽn tiềm năng và một lần phải chờ; dòng chảy một chiều biến bài toán nhiều giao điểm thành đường thẳng dễ cân bằng. Áp dụng cho: nhà máy (nguyên liệu vào một đầu, thành phẩm ra đầu kia), nhà hàng (order, chế biến, phục vụ, thu dọn theo một chiều), kho (nhận, lưu trữ, lấy, xuất).

#### 2.8.2. 5S

5S (Sàng lọc - Sắp xếp - Sạch sẽ - Săn sóc - Sẵn sàng; tiếng Nhật: Seiri, Seiton, Seiso, Seiketsu, Shitsuke) là phương pháp tổ chức nơi làm việc của Nhật Bản. Ý nghĩa với layout: layout đẹp trên giấy sẽ hỏng sau vài tháng nếu mọi thứ chất lung tung; 5S bảo đảm "mỗi vật có chỗ của nó", giảm thời gian tìm kiếm và đi lại.

#### 2.8.3. Thiết kế lối đi (Aisle Design)

Lối đi cần cân bằng giữa **mật độ lưu trữ** (lối đi hẹp thì nhiều chỗ chứa) và **an toàn, tốc độ** (lối đi rộng để xe nâng quay đầu). Tham khảo: lối chính tối thiểu khoảng 3-3,5 m cho xe nâng quay đầu; lối phụ 1,5-2 m cho người đi bộ (kiểm tra theo loại xe và quy chuẩn thực tế).

**Ví dụ step-by-step (giả định minh họa)**: kho rộng 36 m, dài 40 m; giá kệ đôi sâu 2,4 m (2 hàng), pallet rộng 1,2 m, kệ 3 tầng.

- Cấu hình A (lối đi 3,5 m): mỗi module (giá kệ + lối đi) rộng 2,4 + 3,5 = 5,9 m; số module = ⌊36/5,9⌋ = 6. Số vị trí pallet mỗi module = 2 hàng × ⌊40/1,2⌋ = 2 × 33 = 66 vị trí mỗi tầng; tổng = 6 × 66 × 3 = **1.188 pallet**.
- Cấu hình B (lối đi hẹp 2,0 m, cần xe nâng lối hẹp chuyên dụng): module = 2,4 + 2,0 = 4,4 m; số module = ⌊36/4,4⌋ = 8; tổng = 8 × 66 × 3 = **1.584 pallet**.
- Tăng 1.584/1.188 - 1 = **33,3%** sức chứa trên cùng diện tích.

*Diễn giải*: lối đi hẹp tăng sức chứa nhưng đòi hỏi thiết bị đắt hơn và kỹ thuật vận hành cao hơn; phải so khoản đầu tư xe nâng với giá trị diện tích tiết kiệm (hoặc chi phí thuê kho thêm).

### 2.9. Tự động hoá layout, thương mại điện tử và đa kênh

#### 2.9.1. Kho thương mại điện tử và robot AGV/AMR

Kho thương mại điện tử cần lấy lẻ số lượng lớn (each-picking), thay vì lấy theo pallet. Xu hướng là **Goods-to-Person** (hàng đến người lấy bằng robot) thay cho **Person-to-Goods** (người đi đến hàng). Amazon (qua Kiva Systems, được Amazon mua lại năm 2012) tiên phong dùng robot di chuyển kệ đến trạm lấy hàng cố định; vì không cần lối đi cho người ở giữa các kệ nên có thể tăng mật độ lưu trữ trên cùng diện tích. Mức tăng cụ thể phụ thuộc cấu hình và không nên trích con số chung.

| Tiêu chí | Layout truyền thống (Person-to-Goods) | Layout tự động hoá (AGV/AMR) |
|---|---|---|
| Mật độ lưu trữ | Thấp hơn (cần lối đi rộng cho người) | Cao hơn đáng kể |
| Chi phí đầu tư | Thấp | Rất cao |
| Tốc độ lấy hàng | Trung bình, phụ thuộc kỹ năng người | Nhanh và ổn định |
| Khả năng mở rộng | Linh hoạt, dễ điều chỉnh | Cần hoạch định kỹ vì hệ thống phức tạp |
| Phù hợp | SME, khối lượng biến động | Doanh nghiệp lớn, khối lượng cao và ổn định |

#### 2.9.2. Phân tích hoà vốn khi đầu tư tự động hoá

$$\text{Payback (năm)} = \frac{\text{Chi phí đầu tư ban đầu}}{\text{Chi phí lao động tiết kiệm mỗi năm} - \text{Chi phí vận hành/bảo trì mỗi năm}}$$

*Tại sao dùng công thức này?* Lợi ích ròng của tự động hoá là lao động tiết kiệm trừ đi chi phí hệ thống (điện, bảo trì, phần mềm). Chia vốn đầu tư cho lợi ích ròng cho biết sau bao nhiêu năm thu hồi vốn.

**Ví dụ step-by-step (giả định minh họa)**: đầu tư hệ thống AGV 4,5 tỷ đồng, chi phí vận hành và bảo trì 450 triệu/năm. Mỗi công nhân lương 10 triệu/tháng, công ty đóng thêm bảo hiểm khoảng 21,5% (giả định) nên chi phí 1 công nhân/năm = 10 triệu × 12 × 1,215 = 145,8 triệu.

| Kịch bản | Số công nhân thay thế | Tiết kiệm lao động/năm | Lợi ích ròng/năm | Payback |
|---|---|---|---|---|
| Kho nhỏ | 6 | 874,8 triệu | 874,8 - 450 = 424,8 triệu | 4.500 / 424,8 = **10,6 năm** |
| Kho vừa | 12 | 1.749,6 triệu | 1.749,6 - 450 = 1.299,6 triệu | 4.500 / 1.299,6 = **3,5 năm** |
| Kho lớn (vận hành 550 triệu/năm) | 24 | 3.499,2 triệu | 3.499,2 - 550 = 2.949,2 triệu | 4.500 / 2.949,2 = **1,5 năm** |

**Diễn giải**: nguyên tắc thường dùng là hoàn vốn dưới 2-3 năm và hệ thống phải chạy tỷ lệ sử dụng cao. Kho 6 và 12 công nhân chưa đạt; chỉ kho 24 công nhân mới thuyết phục. SME nên tối ưu layout thủ công trước. Chưa tính giá trị tăng sức chứa, giảm sai sót, hoặc rủi ro tăng lương, nên đây là phân tích tối thiểu.

#### 2.9.3. Dark Store, Micro-fulfillment và layout đa kênh (Omnichannel)

- **Dark Store**: cửa hàng chỉ phục vụ giao online, không đón khách; layout tối ưu hoàn toàn cho tốc độ lấy và đóng gói (hàng chạy nhanh gần khu đóng gói), không cần trưng bày hấp dẫn.
- **Omnichannel**: cửa hàng vừa bán trực tiếp vừa là điểm lấy hàng (click-and-collect) hoặc giao từ cửa hàng (ship-from-store). Cần khu soạn đơn riêng (thường phía sau, gần kho) để việc soạn đơn online không cản lối đi và trải nghiệm của khách vào cửa hàng. Một số chuỗi thời trang tại Việt Nam đã bố trí góc nhỏ phía sau cửa hàng cho mục đích này.
- **Layout linh hoạt (module hoá)** so với **layout cố định**: layout module (kệ có bánh xe, vách ghép) đầu tư ban đầu cao hơn nhưng chi phí thay đổi sau này thấp, phù hợp doanh nghiệp tăng trưởng nhanh và hay đổi sản phẩm; layout cố định rẻ hơn ban đầu, phù hợp sản xuất ổn định. Cả hai cần so bằng chi phí vòng đời, không chỉ vốn ban đầu.

### 2.10. Yếu tố con người và tính bền vững trong layout

**Trải nghiệm nhân viên**: ánh sáng tự nhiên, thông gió, tiếng ồn và khu nghỉ ảnh hưởng đến năng suất và tỷ lệ giữ chân nhân viên, đặc biệt trong dịch vụ và văn phòng. Một số công ty công nghệ lớn đầu tư mạnh vào không gian làm việc; cách làm này tốn kém và chỉ hợp lý khi cạnh tranh nhân sự gay gắt; SME có thể bắt đầu từ các cải tiến rẻ (ánh sáng, lối đi sạch, khu nghỉ gọn).

**Bền vững**: tối ưu ánh sáng và thông gió tự nhiên để giảm điện năng và điều hoà; rút ngắn quãng đường vận chuyển nội bộ (giảm nhiên liệu xe nâng); thiết kế khu phân loại rác ngay trong dây chuyền; một số chứng chỉ công trình xanh (LEED, EDGE) xem xét layout trong tiêu chí chấm điểm.

### 2.11. Ưu - nhược điểm tổng hợp các lựa chọn layout

| Lựa chọn | Ưu điểm | Nhược điểm | Phù hợp |
|---|---|---|---|
| Grid (bán lẻ) | Tối ưu diện tích, dễ tìm hàng | Ít gợi ý mua thêm | Siêu thị, hiệu thuốc |
| Free-Flow | Trải nghiệm thú vị, khám phá | Hao diện tích | Thời trang, cao cấp |
| Loop | Khách đi qua toàn bộ khu trưng bày | Khó chịu khi chỉ muốn mua nhanh | IKEA, trung tâm thương mại |
| Tự động hoá (AGV/robot) | Mật độ cao, tốc độ ổn định, giảm phụ thuộc lao động | Đầu tư rất cao, cần quy mô để hoàn vốn | Doanh nghiệp lớn, khối lượng ổn định |
| Thủ công truyền thống | Đầu tư thấp, điều chỉnh nhanh | Phụ thuộc kỹ năng nhân viên | SME, khối lượng biến động |
| Chuẩn hoá layout chuỗi | Trải nghiệm nhất quán, đào tạo nhanh, dễ so sánh hiệu suất | Có thể không tối ưu cho từng mặt bằng; sửa mặt bằng lệch chuẩn tốn kém | Chuỗi nhiều chi nhánh |

---

## III. CASE STUDIES THỰC TẾ

> Cách đọc: mỗi case đi theo trình tự bối cảnh, số liệu, tính toán từng bước, diễn giải kinh doanh, bài học. Phần mô tả doanh nghiệp thật (Toyota, IKEA, Vincom, Tiki, Long Châu) chỉ nêu những nguyên lý được công bố rộng rãi; **mọi con số đi kèm là giả định minh họa** để làm rõ cơ chế, không phải số liệu thật của các công ty đó. Các case tên giả (quán cà phê, phòng khám, xưởng may, Tân An...) đều là tình huống tự thiết kế.

### 3.1. Case quốc tế: Toyota - Cellular Layout, one-piece flow và cân bằng chuyền

#### Bối cảnh
Trong Toyota Production System, nhà máy tổ chức máy móc thành các cell/chuyền theo thứ tự công đoạn, công nhân đa kỹ năng (multi-skilled) vận hành nhiều máy, và nguyên tắc dòng chảy từng chi tiết (one-piece flow) thay cho sản xuất theo lô lớn. Mục tiêu: rút ngắn lead time, giảm tồn kho bán thành phẩm (WIP), phát hiện lỗi sớm và vẫn đáp ứng nhiều mẫu mã. Takt time liên kết nhịp sản xuất với nhịp nhu cầu của khách hàng.

#### Phân tích định lượng (mô hình minh họa, không phải số liệu của Toyota)
Giả sử một họ chi tiết 100 cái qua 4 công đoạn, mỗi công đoạn 2 phút/chi tiết (tính toán đầy đủ ở mục 2.5.2):

| Chỉ tiêu | Process layout (theo lô) | Cell (one-piece flow) |
|---|---|---|
| Thời gian hoàn thành lô 100 chi tiết | 4 × 100 × 2 = 800 phút | 4 × 2 + 99 × 2 = 206 phút |
| WIP tại mỗi trạm | Tới 100 chi tiết chờ | 1-2 chi tiết |
| Lỗi phát hiện | Sau khi cả lô xong công đoạn đó | Gần như ngay chi tiết kế tiếp |

Dùng **Định luật Little** (Little's Law) để thấy liên hệ WIP với lead time:

$$WIP = Throughput \times Lead\ Time$$

Với throughput (sản lượng ra) 0,5 chi tiết/phút không đổi, lead time giảm 74% thì WIP trung bình cũng giảm tương ứng.

#### Ý nghĩa kinh doanh
Giảm thời gian chờ không cần máy nhanh hơn mà chỉ nhờ sắp xếp lại không gian và cách chảy. WIP thấp giải phóng vốn lưu động và diện tích; lỗi được phát hiện sớm nên ít phải làm lại cả lô.

#### Bài học và điều kiện áp dụng
(1) Cell chỉ hiệu quả khi các công đoạn cân bằng (xem Line Balancing) và công nhân đa kỹ năng; (2) cần nhu cầu đủ ổn định cho một họ sản phẩm; (3) SME có thể bắt đầu bằng một cell thí điểm cho sản phẩm bán chạy nhất.

### 3.2. Case quốc tế: IKEA - Loop Layout dẫn dắt hành vi mua sắm

#### Bối cảnh
Showroom IKEA thường được thiết kế để khách đi theo một lối chính xuyên qua các "căn phòng mẫu" trước khi tới khu kho tự lấy và quầy thanh toán, thay vì tự do chọn đường như các cửa hàng nội thất thông thường (có các lối tắt ở nhiều điểm). Các phòng mẫu trình bày sản phẩm trong bối cảnh sử dụng thực tế (phòng khách, bếp, phòng ngủ).

#### Phân tích cơ chế (mô hình minh họa)
Giả sử showroom có 50 khu và xác suất khách mua bốc phát một món cho mỗi khu được nhìn thấy là 0,8%, giá trị món bốc phát trung bình 120.000 đồng (giả định minh họa):

| Mô hình | Số khu khách đi qua | Công thức | Giá trị mua bốc phát kỳ vọng/khách |
|---|---|---|---|
| Free-flow (khách tự chọn lối, thấy 22/50 khu) | 22 | 22 × 0,008 × 120.000 | 21.120 đồng |
| Loop (khách đi qua 50/50 khu) | 50 | 50 × 0,008 × 120.000 | 48.000 đồng |
| Chênh lệch | +28 khu | | +26.880 đồng (gấp khoảng 2,3 lần) |

#### Ý nghĩa kinh doanh
Loop layout là đánh đổi: tăng số lần khách nhìn thấy sản phẩm (và thời gian ở lại) nhưng khách chỉ muốn mua nhanh sẽ khó chịu, vì thế cần các lối tắt ở một số điểm trong thực tế để giữ tự do cho khách có mục đích rõ ràng. Phòng mẫu trình bày theo bối cảnh khiến khách hình dung công năng và muốn mua cả bộ.

#### Bài học
Layout bán lẻ là **công cụ tác động hành vi**. Với SME, nguyên lý có thể áp dụng ở quy mô nhỏ: đặt sản phẩm bổ trợ cạnh nhau (bàn cùng ghế, nến cùng đế), tạo một lối chính dẫn qua các khu lợi nhuận cao, nhưng luôn để khách thấy lối ra.

### 3.3. Case Việt Nam (doanh nghiệp lớn): Vincom - layout trung tâm thương mại và dòng khách

#### Bối cảnh
Trung tâm thương mại cho thuê mặt bằng; doanh thu của chủ đầu tư phụ thuộc vào giá thuê (cố định và/hoặc theo doanh thu) và việc lấp đầy. Nguyên lý layout phổ biến: đặt khách thuê chủ lực (anchor tenant: siêu thị, rạp chiếu phim, khu ẩm thực) ở vị trí xa lối vào hoặc ở tầng trên để dòng khách đi qua các gian hàng nhỏ; thang cuốn, giếng trời giúp khách nhìn thấy nhiều gian hàng. (Mô tả định tính theo thông lệ ngành; thiết kế cụ thể của từng trung tâm không được kiểm chứng ở đây.)

#### Phân tích định lượng (mô hình minh họa)
Giả sử một trung tâm có 10.000 khách/ngày. Layout dẫn khách giúp thời gian lưu lại tăng từ 85 lên 110 phút; mỗi phút khách ở lại tạo trung bình 2.000 đồng doanh thu cho các khách thuê (giả định minh họa, quan hệ tuyến tính là một đơn giản hoá thô):

- Doanh thu khách thuê trên mỗi khách: trước = 85 × 2.000 = 170.000 đồng; sau = 110 × 2.000 = 220.000 đồng (tăng 29,4%).
- Tăng doanh thu mỗi ngày = 10.000 × (220.000 - 170.000) = **500 triệu đồng**.
- Giả sử chủ đầu tư thu tiền thuê theo doanh thu 8%: tăng thu = 500 triệu × 8% = **40 triệu đồng/ngày**, tương đương khoảng 1,2 tỷ đồng/tháng (30 ngày).

#### Ý nghĩa kinh doanh
Với chủ đầu tư, layout không chỉ là thẩm mỹ: nó quyết định giá trị mỗi mét vuông cho thuê và khả năng giữ chân khách thuê nhỏ (nếu dòng khách không đi qua thì họ không trụ được). Cần phân biệt tác dụng của layout với tác dụng của sự kiện, khuyến mại và thương hiệu: nên đo dòng khách (people counter) trước và sau khi thay đổi.

#### Bài học
SME bán lẻ trong trung tâm thương mại nên thương lượng vị trí gần lối đi của dòng khách chính, không chỉ nhìn giá thuê/m²; dòng khách qua cửa hàng (footfall) tiếp cận bằng đếm tay trong 3-5 ngày là cách rẻ nhất.

### 3.4. Case thất bại: chuỗi siêu thị mini mở rộng nhanh không chuẩn hoá layout

#### Bối cảnh (giả định minh họa)
Chuỗi 12 siêu thị mini, mỗi cửa hàng khoảng 120 m², thuê được mặt bằng nào thì thiết kế kệ theo mặt bằng đó. Có 3 cửa hàng bố trí theo mẫu chuẩn (nhóm hàng thiết yếu đặt cuối cửa hàng, hàng lợi nhuận cao ở lối vào và gần quầy thu ngân); 9 cửa hàng còn lại bố trí khác nhau, mỗi nơi một kiểu.

#### Hậu quả
- Khách quen khó tìm hàng khi sang cửa hàng khác trong chuỗi, trải nghiệm thương hiệu không nhất quán.
- Nhân viên mới học lại cách bố trí ở mỗi cửa hàng; chuyển nhân viên giữa các cửa hàng kém hiệu quả.
- Khó so sánh hiệu suất giữa các cửa hàng vì khác biệt do layout trộn lẫn với khác biệt do khu vực.

#### Phân tích định lượng (giả định minh họa)
Doanh thu trung bình trên mỗi m² của 9 cửa hàng không chuẩn là 12,0 triệu đồng/tháng; của 3 cửa hàng chuẩn là 13,2 triệu (cao hơn 10%). Biên lợi nhuận gộp 22%. Chi phí chuẩn hoá lại mỗi cửa hàng (kệ, bảng, di dời) 85 triệu.

- Chênh lệch doanh thu/m² = 13,2 - 12,0 = 1,2 triệu đồng/m²/tháng.
- Tăng doanh thu mỗi cửa hàng = 1,2 triệu × 120 m² = **144 triệu đồng/tháng**.
- Tăng lợi nhuận gộp mỗi cửa hàng = 144 triệu × 22% = **31,68 triệu đồng/tháng**.
- Hoàn vốn mỗi cửa hàng = 85 / 31,68 = **2,7 tháng**.
- Cho 9 cửa hàng: đầu tư 9 × 85 = 765 triệu; lợi nhuận gộp tăng 9 × 31,68 = 285,12 triệu/tháng.

#### Lưu ý phương pháp (rất quan trọng)
Cần cẩn trọng với kết luận "do layout": 3 cửa hàng chuẩn có thể ở vị trí tốt hơn. Cách kiểm chứng: chuẩn hoá thí điểm 2 cửa hàng, so sánh doanh thu trước/sau với 2 cửa hàng đối chứng (không đổi) cùng thời gian; chỉ khi chênh lệch ổn định mới nhân rộng. Nếu mức tăng thực chỉ bằng nửa giả định thì hoàn vốn kéo dài khoảng 5,4 tháng, vẫn hợp lý.

#### Bài học
Xây dựng "playbook layout" (xem Case 3.8 với hiệu thuốc) trước khi nhân chuỗi: gồm nguyên tắc vị trí nhóm hàng, kích thước chuẩn, và các biến thể được phê duyệt cho mặt bằng đặc thù.

### 3.5. Case SME dịch vụ: quán cà phê 80 m² tại Hà Nội tái bố trí quầy

#### Bối cảnh (giả định minh họa)
Quán cà phê 80 m² có hai nhân viên pha chế và một thu ngân. Khung giờ cao điểm (sáng 7-9 giờ) có khoảng 32 đơn/giờ; trung bình mỗi đơn 55.000 đồng. Hiện tại bố trí: quầy order một đầu, máy pha ở đầu kia, kho ly và đá ở góc xa; nhân viên pha chế liên tục đi qua lại, giao đồ uống cắt ngang hàng chờ order.

```
TRƯỚC (đi ngược và cắt chéo):                SAU (dòng chảy một chiều):

┌──────────────────────────────┐          ┌──────────────────────────────┐
│ [Order] ◄─┐        [Máy pha]  │          │ [Order]→[Pha chế: ly, đá,    │
│     ▲     │            ▲      │          │          máy, syrup trong    │
│     └─ giao đồ uống ───┘      │          │          tầm với]→[Giao đồ]  │
│ [Kho ly, đá]  (đi xa)         │          │  Khách: Vào→Order→Chờ→Nhận  │
└──────────────────────────────┘          └──────────────────────────────┘
```

#### Phân tích thời gian xử lý mỗi đơn (giây)

| Thành phần | Trước | Sau | Cách cải thiện |
|---|---|---|---|
| Nhận order và thu tiền | 45 | 45 | Giữ nguyên |
| Đi từ quầy đến khu pha | 15 | 0 | Đưa khu pha liền kề quầy order |
| Pha chế | 100 | 75 | Ly, đá, syrup trong tầm với, sắp theo tần suất dùng |
| Giao đồ uống | 20 | 12 | Điểm giao đặt cuối quầy, không cắt hàng chờ |
| Chờ do giao cắt dòng | 20 | 8 | Dòng chảy một chiều |
| **Tổng** | **200** | **140** | Giảm 60 giây = **30%** |

#### Phân tích năng lực: nút cổ chai là bartender
Phần việc của người pha chế = đi + pha + giao + chờ:
- Trước: 15 + 100 + 20 + 20 = 155 giây/đơn, năng lực = 3.600 / 155 = **23,2 đơn/giờ**.
- Sau: 75 + 12 + 8 = 95 giây/đơn, năng lực = 3.600 / 95 = **37,9 đơn/giờ**.
- Mức sử dụng so với nhu cầu 32 đơn/giờ: trước = 32 / 23,2 = **138%** (hàng đợi tăng không ngừng, khách bỏ đi); sau = 32 / 37,9 = **84%** (ổn định).

#### Ý nghĩa tài chính
Trước, quán không đáp ứng được 32 - 23,2 = 8,8 đơn/giờ; giả sử số khách này bỏ đi và giờ cao điểm kéo dài 2 giờ/ngày, 30 ngày/tháng: doanh thu bị mất = 8,8 × 2 × 55.000 × 30 ≈ **29 triệu đồng/tháng**. Việc tái bố trí dùng chính diện tích và nhân sự cũ, chi phí chủ yếu là di dời quầy và kệ.

#### Bài học
(1) Nút cổ chai thường nằm ở nhân viên đứng giữa nhiều di chuyển, không phải ở máy móc; (2) khi mức sử dụng vượt 100% hàng đợi không ổn định, nên mục tiêu thiết kế là mức sử dụng khoảng 80-85% vào giờ cao điểm; (3) cải tiến "5S + one-way flow" là rẻ nhất cho quán nhỏ.

### 3.6. Case SME dịch vụ: phòng khám nha khoa tại TP.HCM với layout module

#### Bối cảnh (giả định minh họa)
Phòng khám 80 m², mở cửa 9 giờ/ngày (540 phút), ban đầu 3 ghế khám đặt dọc hành lang; khu tiệt trùng dụng cụ ở cuối hành lang. Muốn tăng số ghế và giảm đi lại của y tá nhưng vẫn giữ riêng tư.

#### Giải pháp
Mỗi ghế là một "cell" độc lập có vách ngăn; khu tiệt trùng dụng cụ đặt ở trung tâm sao cho khoảng cách đến mọi ghế đều ngắn; khu tiếp đón và chờ ở mặt tiền.

```
TRƯỚC (hành lang dài)                SAU (module, khu tiệt trùng ở giữa)
[Ghế1][Ghế2][Ghế3]...[Tiệt trùng]   [Ghế1][Ghế2][Ghế3]
  khoảng cách TB 14 m                      [ Tiệt trùng ]
                                      [Ghế4][Ghế5]
                                       khoảng cách TB 6 m
```

#### Phân tích năng lực (mỗi ghế 45 phút/bệnh nhân, hiệu suất ghế 80%)
- Số bệnh nhân/ghế/ngày = 540 × 0,8 / 45 = 9,6. Với 3 ghế: 28,8 (khoảng 29); với 5 ghế: 48.
- Nhưng bác sĩ cũng là nguồn lực: giả sử 2 bác sĩ, mỗi bệnh nhân cần 25 phút thời gian bác sĩ, hiệu suất 85%: năng lực = 2 × 540 × 0,85 / 25 = 36,7, lấy **36** bệnh nhân/ngày.
- Năng lực thực tế = nhỏ hơn của hai ràng buộc: trước = min(28,8; 36) ≈ 29 (ghế là nút cổ chai); sau = min(48; 36) = 36 (bác sĩ trở thành nút cổ chai). Tăng 36 - 29 = 7 bệnh nhân/ngày (+25%, không phải +67% như số ghế).
- Muốn dùng hết 5 ghế (48 bệnh nhân) cần 48 × 25 / (540 × 0,85) = 2,61, tức **3 bác sĩ**.

#### Phân tích di chuyển của y tá
Mỗi bệnh nhân cần 3 lượt đi - về giữa ghế và khu tiệt trùng (mỗi lượt đi và về = 2 chiều):
- Trước: 29 × 3 × 2 × 14 m = **2.436 m/ngày**, với tốc độ đi 1 m/s mất 2.436 giây = 40,6 phút.
- Sau: 36 × 3 × 2 × 6 m = **1.296 m/ngày** = 21,6 phút.

Dù phục vụ nhiều bệnh nhân hơn 24%, y tá đi bộ ít hơn 47% (1 - 1.296/2.436), tức dành thời gian cho chăm sóc bệnh nhân.

#### Ý nghĩa kinh doanh
Doanh thu thêm: 7 bệnh nhân × 1,2 triệu đồng/lượt (giả định) × 26 ngày = **218,4 triệu đồng/tháng**. Bài học TOC: mở rộng ghế không tăng năng lực nếu nguồn lực khác (bác sĩ) mới là nút cổ chai; phải xem toàn hệ thống trước khi chi tiền cải tạo.

### 3.7. Case SME sản xuất: xưởng may Bình Dương chuyển từ Process Layout sang Cellular

#### Bối cảnh (giả định minh họa)
Xưởng may khoảng 200 công nhân. Layout cũ theo chức năng: khu cắt riêng, khu may riêng, khu ủi riêng, khu đóng gói riêng; bán thành phẩm vận chuyển theo bó (bundle) bằng xe đẩy. Thời gian một đơn hàng chảy qua xưởng (lead time) 12 ngày làm việc, trong đó thời gian di chuyển và chờ giữa các khu chiếm 30%.

#### Giải pháp
Chuyển sang 8 cell, mỗi cell khoảng 25 người có thể xử lý trọn một đơn nhỏ: cắt tại cell (hoặc cấp vải đã cắt tại điểm đầu cell), may, ủi, đóng gói, theo thứ tự trong cùng một khu; công nhân được đào tạo đa kỹ năng ở ít nhất hai công đoạn liền kề.

#### Phân tích số liệu
- Thời gian di chuyển và chờ trước: 12 × 30% = **3,6 ngày**; thời gian tạo giá trị = 12 - 3,6 = **8,4 ngày**.
- Mục tiêu giảm lead time 25%: lead time mới = 12 × 75% = **9 ngày**. Vì thời gian tạo giá trị không đổi (8,4 ngày), thời gian di chuyển và chờ sau = 9 - 8,4 = **0,6 ngày** (giảm 83% khoảng này).
- WIP theo Định luật Little: với sản lượng 400 áo/ngày, WIP trước = 400 × 12 = **4.800 áo**; sau = 400 × 9 = **3.600 áo** (giảm 1.200 áo).
- Vốn lưu động giải phóng: giả sử giá trị bán thành phẩm 80.000 đồng/áo: 1.200 × 80.000 = **96 triệu đồng**.

#### Ý nghĩa kinh doanh
Lead time ngắn hơn 3 ngày giúp nhận đơn nhỏ, đổi mẫu nhanh và giao sớm (lợi thế khi khách hàng thời trang ngày càng đặt đơn nhỏ). Trách nhiệm chất lượng cũng rõ hơn: lỗi có thể truy ngược về một cell nhất định.

#### Bài học và rủi ro
(1) Cần đầu tư thêm một số máy (mỗi cell cần đủ loại máy, máy ít dùng sẽ bị trùng lặp); (2) cần cân bằng công việc trong cell để tránh cell có người chờ; (3) công nhân quen làm một việc cần thời gian học; (4) nên thử một cell trước, đo lead time thực, rồi nhân rộng.

### 3.8. Case Việt Nam: Tiki (micro-fulfillment) và Long Châu (chuẩn hoá layout chuỗi)

#### 3.8.1. Tiki - phân vùng kho theo tốc độ luân chuyển (ABC slotting)

**Bối cảnh**: Tiki, nền tảng thương mại điện tử Việt Nam, vận hành các điểm lưu trữ gần khu dân cư để rút ngắn thời gian giao hàng; layout các điểm này ưu tiên hàng bán chạy (fast-moving SKU) gần khu đóng gói. Đây là ứng dụng của nguyên lý phân loại ABC (File 04 - Quản trị tồn kho). Mô tả chỉ ở mức nguyên lý; số liệu dưới đây là giả định minh họa.

**Phân tích định lượng**: giả sử kho nhỏ xử lý 5.000 dòng lấy hàng (pick line) mỗi ngày; quy tắc Pareto: 20% SKU chiếm khoảng 80% số lượt lấy. Trước khi phân vùng, quãng đường đi bộ trung bình mỗi dòng lấy là 38 m; sau khi đưa SKU nhóm A gần khu đóng gói còn 21 m.

- Quãng đường/ngày: trước = 5.000 × 38 = 190.000 m; sau = 5.000 × 21 = 105.000 m (giảm 44,7%).
- Thời gian đi bộ với 1 m/s: trước = 190.000 giây = 52,8 giờ; sau = 105.000 giây = 29,2 giờ.
- Tiết kiệm = 23,6 giờ/ngày, tương đương khoảng 3 người làm ca 8 giờ (23,6 / 7 giờ hiệu dụng ≈ 3,4 người).

**Bài học**: vị trí hàng chạy nhanh gần điểm đóng gói là cải tiến layout rẻ nhất; chỉ cần đổi vị trí lưu trữ, không cần thêm thiết bị; nhưng phải cập nhật phân loại theo định kỳ vì hàng bán chạy thay đổi theo mùa.

#### 3.8.2. Long Châu (chuỗi nhà thuốc) - playbook layout với biến thể được phê duyệt

**Bối cảnh**: chuỗi nhà thuốc mở rộng nhanh số chi nhánh cần trải nghiệm đồng nhất. Cách tiếp cận phổ biến của chuỗi bán lẻ: bộ tiêu chuẩn layout (playbook) quy định vị trí các nhóm sản phẩm (thuốc kê đơn, thực phẩm chức năng, chăm sóc cá nhân), quầy tư vấn dược sĩ và khu chờ, kèm các **biến thể được phê duyệt trước** (pre-approved variants) cho mặt bằng đặc thù. (Mô tả theo thông lệ ngành, cấu hình cụ thể của Long Châu không được kiểm chứng ở đây.)

**Ví dụ playbook với 3 biến thể diện tích (giả định minh họa, tỷ lệ phần trăm diện tích)**:

| Khu vực | 60 m² | 90 m² | 120 m² |
|---|---|---|---|
| Quầy thuốc kê đơn và tư vấn dược sĩ | 28% (16,8 m²) | 25% (22,5 m²) | 22% (26,4 m²) |
| Thực phẩm chức năng (khu lợi nhuận cao) | 30% (18,0 m²) | 30% (27,0 m²) | 30% (36,0 m²) |
| Chăm sóc cá nhân/mỹ phẩm | 12% (7,2 m²) | 15% (13,5 m²) | 18% (21,6 m²) |
| Khu chờ | 6% (3,6 m²) | 7% (6,3 m²) | 8% (9,6 m²) |
| Kho sau quầy | 14% (8,4 m²) | 13% (11,7 m²) | 12% (14,4 m²) |
| Lối đi, thanh toán và khác | 10% (6,0 m²) | 10% (9,0 m²) | 10% (12,0 m²) |
| **Tổng** | **100% (60 m²)** | **100% (90 m²)** | **100% (120 m²)** |

**Diễn giải**: cửa hàng nhỏ hơn dành tỷ lệ lớn hơn cho quầy tư vấn (vì chức năng bắt buộc) và ít hơn cho khu chờ; khu lợi nhuận cao giữ tỷ lệ cố định. Các thứ tự ưu tiên này giúp quản lý mở chi nhánh mới chỉ cần chọn biến thể gần nhất thay vì thiết kế lại.

**Bài học**: chuẩn hoá không phải cứng nhắc. Playbook tốt có (1) nguyên tắc bất biến (vị trí quầy tư vấn, thứ tự khu), (2) biến thể theo diện tích, (3) quy trình xin ngoại lệ có phê duyệt.

### 3.9. Case SME Việt Nam MỚI: Xưởng nội thất Tân An - Load-Distance và Line Balancing

> **Giả định minh họa**: tên "Xưởng nội thất Tân An" và toàn bộ số liệu do tác giả tự thiết kế để minh hoạ cách áp dụng hai kỹ thuật chính của bài. Mọi phép tính đã được kiểm chứng bằng Python.

#### Bối cảnh
Xưởng nội thất Tân An (Đồng Nai) có 40 lao động, sản xuất bàn ghế văn phòng; chủ xưởng thấy nhân công vận chuyển giữa các khu luôn "chạy" suốt ngày và dây chuyền lắp ráp ghế có 6 công nhân mà vẫn có người chờ, người quá tải. Nhu cầu ổn định 210 ghế/ngày; mỗi ca làm 8 giờ, nghỉ 1 giờ, thời gian khả dụng 25.200 giây.

Chủ xưởng thuê một sinh viên kỹ thuật công nghiệp thực tập 3 tuần để làm hai việc: (1) tối ưu bố trí 6 khu theo Load-Distance; (2) cân bằng lại chuyền lắp ráp theo Line Balancing.

#### Phần A - Bố trí lại 6 khu bằng Load-Distance

**Bước 1 - Thu thập dữ liệu**: đếm số chuyến xe đẩy/xe nâng giữa các khu trong 5 ngày, lấy trung bình mỗi ngày (From-To Chart tối giản, chỉ liệt kê cặp có tải):

| Cặp | Tải (chuyến/ngày) |
|---|---|
| Kho gỗ ↔ Cưa cắt | 90 |
| Cưa cắt ↔ Bào phay | 80 |
| Bào phay ↔ Lắp ráp | 70 |
| Lắp ráp ↔ Sơn | 60 |
| Sơn ↔ Kho thành phẩm | 55 |
| Lắp ráp ↔ Kho thành phẩm | 20 |
| Kho gỗ ↔ Bào phay | 15 |
| Cưa cắt ↔ Lắp ráp | 10 |
| Bào phay ↔ Sơn | 10 |
| Kho gỗ ↔ Lắp ráp | 5 |

Mặt bằng chia thành lưới 2 hàng × 3 cột, mỗi ô 10 m; khoảng cách tính rectilinear giữa tâm các ô.

**Bước 2 - Layout hiện tại** (do xưởng mở rộng dần mà ra):

```
Hàng 1:  [Kho gỗ]   [Sơn]        [Cưa cắt]
Hàng 2:  [Kho TP]   [Bào phay]   [Lắp ráp]
```

| Cặp | Tải | Khoảng cách (m) | Load × Distance |
|---|---|---|---|
| Kho gỗ - Cưa cắt | 90 | 20 | 1.800 |
| Cưa cắt - Bào phay | 80 | 20 | 1.600 |
| Bào phay - Lắp ráp | 70 | 10 | 700 |
| Lắp ráp - Sơn | 60 | 20 | 1.200 |
| Sơn - Kho TP | 55 | 20 | 1.100 |
| Kho gỗ - Bào phay | 15 | 20 | 300 |
| Cưa cắt - Lắp ráp | 10 | 10 | 100 |
| Lắp ráp - Kho TP | 20 | 20 | 400 |
| Kho gỗ - Lắp ráp | 5 | 30 | 150 |
| Bào phay - Sơn | 10 | 10 | 100 |
| **Tổng LD hiện tại** | | | **7.450 chuyến·m/ngày** |

**Bước 3 - Hoán đổi từng cặp (Pairwise Exchange)**. Ở mỗi vòng thử mọi cặp hoán đổi (15 cặp), chọn cặp giảm nhiều nhất:

| Vòng | LD trước | Ba hoán đổi tốt nhất (LD sau) | Chọn |
|---|---|---|---|
| 1 | 7.450 | Cưa cắt ↔ Kho TP (5.100); Cưa cắt ↔ Sơn (5.900); Bào phay ↔ Sơn (6.050) | Cưa cắt ↔ Kho TP |
| 2 | 5.100 | Sơn ↔ Kho TP (4.800); Lắp ráp ↔ Sơn (5.000); Bào phay ↔ Lắp ráp (5.600) | Sơn ↔ Kho TP |
| 3 | 4.800 | Lắp ráp ↔ Kho TP (4.700); Sơn ↔ Kho TP (5.100); Kho gỗ ↔ Cưa cắt (5.500) | Lắp ráp ↔ Kho TP |
| 4 | 4.700 | Không còn hoán đổi nào giảm LD | Dừng |

**Layout đề xuất** (LD = 4.700):

```
Hàng 1:  [Kho gỗ]   [Lắp ráp]    [Sơn]
Hàng 2:  [Cưa cắt]  [Bào phay]   [Kho TP]
```

Dòng chảy: Kho gỗ → Cưa cắt → Bào phay → Lắp ráp → Sơn → Kho TP, theo hình chữ U, các cặp lớn nhất (Kho gỗ-Cưa, Cưa-Bào, Bào-Lắp, Lắp-Sơn, Sơn-KTP) đều cách 10 m (ô liền kề). Kiểm chứng bằng vét cạn 720 hoán vị bằng Python: LD nhỏ nhất cũng là 4.700, nên đáp án heuristic tình cờ là tối ưu.

**Bước 4 - Hiệu quả tài chính**:
- LD giảm = 7.450 - 4.700 = 2.750 chuyến·m/ngày (giảm **36,9%**).
- Chi phí vận chuyển nội bộ (giả định 300 đồng/chuyến/mét, gồm nhân công và hao mòn xe): 2.750 × 300 = **825.000 đồng/ngày**; nhân 26 ngày = **21,45 triệu đồng/tháng**.
- Chi phí di dời (di máy, đi lại điện nước, nghỉ sản xuất 2 ngày): 60 triệu đồng.
- Hoàn vốn riêng hạng mục này: 60 / 21,45 = **2,8 tháng**.

#### Phần B - Cân bằng chuyền lắp ráp ghế

Dữ liệu 9 task như ví dụ ở mục 2.4.2 (tổng 425 giây/ghế). Hiện tại chuyền có 6 công nhân phân việc theo thói quen:

| Trạm | Task | Thời gian (s) |
|---|---|---|
| 1 | A | 50 |
| 2 | B, C | 100 |
| 3 | D, E | 80 |
| 4 | F, G | 85 |
| 5 | H | 40 |
| 6 | I | 70 |

- Chu kỳ thực tế của chuyền = trạm chậm nhất = 100 giây. Sản lượng = 25.200 / 100 = 252 ghế/ngày, nhiều hơn nhu cầu 210 (20% là sản xuất dư, dồn thành WIP và thành phẩm tồn).
- Hiệu suất = 425 / (6 × 100) = **70,8%**.

**Cân bằng lại** theo RPW với takt time 25.200 / 210 = 120 giây (xem mục 2.4.2): 4 trạm {A, B}, {C, E}, {D, F, G}, {H, I}; thời gian 90, 105, 120, 110 giây.

- Hiệu suất = 425 / (4 × 120) = **88,5%**.
- Giảm 2 công nhân (6 → 4), chuyển sang làm việc tại khu sơn đang thiếu người (hoặc giảm chi phí).
- Năng suất lao động = 210 / 4 = 52,5 ghế/người/ngày so với 210 / 6 = 35 (tăng 50%).
- Tiết kiệm nhân công = 2 × 10 triệu × 1,215 (có bảo hiểm) = **24,3 triệu đồng/tháng**.
- Đầu tư thêm đồ gá và băng truyền ngắn cho trạm 3: 15 triệu đồng.

**Rủi ro cần quản lý**: trạm 3 đầy 120/120 giây, không còn dư. Nếu công nhân trạm 3 chậm 5% (126 giây) thì chu kỳ chuyền thành 126 giây và sản lượng = 25.200 / 126 = 200 ghế (thiếu 10 ghế, 4,8% nhu cầu). Biện pháp: để trạm 3 làm bởi công nhân giỏi nhất, chuẩn bị vật tư sẵn bằng 5S, và dành 10-15 phút đầu ca dự phòng cho chuẩn bị.

#### Tổng hợp hiệu quả

| Hạng mục | Tiết kiệm/tháng (triệu đồng) | Đầu tư một lần (triệu đồng) |
|---|---|---|
| Bố trí lại 6 khu (Load-Distance) | 21,45 | 60 |
| Cân bằng chuyền (6 → 4 công nhân) | 24,30 | 15 |
| **Tổng** | **45,75** | **75** |

Hoàn vốn chung = 75 / 45,75 = **1,6 tháng**. Chưa tính lợi ích khó định lượng: ít va chạm xe nâng, mặt bằng gọn, ít tồn dư.

#### Bài học
(1) Chỉ với dữ liệu đếm chuyến trong 5 ngày và một bảng tính Excel, SME có thể giảm hơn 1/3 chi phí vận chuyển nội bộ mà không mua thiết bị mới; (2) cân bằng chuyền gắn với takt time, nhờ đó doanh nghiệp biết cần bao nhiêu người thay vì "đủ người thì làm"; (3) mọi tính toán nên đi kèm kiểm chứng nhạy cảm (nếu thời gian trạm chậm 5% thì sao); (4) thực hiện theo từng pha: chuyền lắp ráp trước (không cần di dời máy), sau đó mới di dời mặt bằng.

### 3.10. Bảng tổng hợp case study

| Case | Loại layout / công cụ | Kết quả định lượng (minh họa) | Bài học chính |
|---|---|---|---|
| 3.1 Toyota | Cellular, one-piece flow | Lead time lô 100 chi tiết giảm từ 800 xuống 206 phút (-74%) | Group Technology giảm WIP và thời gian chu kỳ |
| 3.2 IKEA | Loop Layout | Mua bốc phát kỳ vọng 21.120 → 48.000 đồng/khách | Layout là công cụ tác động hành vi |
| 3.3 Vincom | Retail/Anchor layout | Tăng thu chủ đầu tư khoảng 40 triệu/ngày (minh họa) | Dòng khách quyết định giá trị mặt bằng |
| 3.4 Chuỗi siêu thị | Thất bại do thiếu chuẩn hoá | Hoàn vốn chuẩn hoá khoảng 2,7 tháng/cửa hàng | Cần playbook và thí điểm có đối chứng |
| 3.5 Quán cà phê | One-way flow | Thời gian mỗi đơn giảm 30%, mức sử dụng 138% → 84% | Tìm nút cổ chai và đường đi nhân viên |
| 3.6 Phòng khám nha khoa | Modular / cell | Năng lực 29 → 36 ca/ngày; y tá đi bộ giảm 47% | Mở rộng ghế chưa đủ nếu bác sĩ là nút cổ chai |
| 3.7 Xưởng may | Process → Cellular | Lead time 12 → 9 ngày, WIP 4.800 → 3.600 áo | Cell giảm chờ, cần đa kỹ năng |
| 3.8 Tiki / Long Châu | ABC slotting / Playbook | Quãng đường lấy hàng giảm 44,7% | Hàng nhanh gần khu đóng gói; chuẩn hoá có biến thể |
| 3.9 Xưởng Tân An | Load-Distance + Line Balancing | LD giảm 36,9%; hiệu suất chuyền 70,8% → 88,5%; hoàn vốn 1,6 tháng | Dữ liệu đơn giản cũng đủ tối ưu hoá |

---

## IV. ỨNG DỤNG CHO SME

### 4.1. Quy trình 6 bước thiết kế lại layout

Quy trình rút gọn từ SLP (mục 2.6), điều chỉnh cho SME ít dữ liệu và ít vốn:

| Bước | Việc cần làm | Đầu ra | Lý do cần bước này |
|---|---|---|---|
| 1 | Thu thập dữ liệu khối lượng và tần suất di chuyển giữa các bộ phận (From-To Chart); đếm thực tế 3-5 ngày | Bảng tải giữa các cặp | Không có dữ liệu thì chỉ tranh luận cảm tính; Load-Distance cần số liệu thực |
| 2 | Xây REL Chart: mức cần gần/xa nhau, gồm cả lý do an toàn và giám sát | REL Chart và TCR | Những quan hệ không đo được bằng chuyến vận chuyển |
| 3 | Xác định nhu cầu không gian mỗi bộ phận (Space Requirement), có dự phòng tăng trưởng | Bảng diện tích | Tránh Block Layout vẽ đẹp nhưng không đủ chỗ |
| 4 | Lập Block Layout 2-3 phương án dựa trên REL và diện tích | Các sơ đồ khối | Tạo nhiều phương án để so sánh, tránh "bảo vệ phương án đầu tiên" |
| 5 | Chi tiết hoá thành Detailed Layout: cột nhà, điện nước, lối thoát hiểm, lối đi | Bản vẽ chi tiết | Ràng buộc thực tế thường loại bỏ phương án "đẹp trên giấy" |
| 6 | Mô phỏng/thử nghiệm quy mô nhỏ, đánh giá bằng Load-Distance và KPI, thu thập phản hồi, rồi triển khai | Quyết định và kế hoạch triển khai | Phát hiện lỗi khi chưa đầu tư lớn |

### 4.2. Lộ trình khuyến nghị cho SME (từ rẻ đến đắt)

1. Vẽ sơ đồ mặt bằng hiện tại, đánh dấu điểm tắc nghẽn quan sát được và đường đi của nhân viên (vẽ lên sơ đồ bằng bút màu).
2. Thu thập dữ liệu đơn giản về số chuyến giữa các khu vực chính.
3. Áp dụng dòng chảy một chiều và 5S: làm trước vì gần như không tốn vốn.
4. Thử thay đổi nhỏ (dời một quầy, một kệ), đo hiệu quả (thời gian phục vụ, năng suất) trước khi thay đổi lớn.
5. Khi quy mô đủ lớn, mới cân nhắc thuê tư vấn, dùng phần mềm mô phỏng, hoặc tự động hoá.

Quy tắc ngón tay cái: nếu thay đổi có thể hoàn tác trong một ngày thì thử ngay; nếu cần xây dựng lại thì phải qua mô phỏng và tính hoàn vốn.

### 4.3. Quy mô áp dụng: SME so với doanh nghiệp lớn

#### 4.3.1. So sánh mức độ áp dụng

| Tiêu chí | SME | Doanh nghiệp lớn |
|---|---|---|
| Công cụ | Sơ đồ tay, Excel, quan sát thực tế | Phần mềm CAD chuyên dụng, mô phỏng FlexSim/Arena |
| Tần suất thay đổi layout | Linh hoạt, điều chỉnh thường xuyên | Ít thay đổi do chi phí lớn, hoạch định kỹ |
| Yêu cầu chuyên môn | Tự làm dựa trên nguyên tắc cơ bản | Đội ngũ kỹ sư công nghiệp chuyên trách |

#### 4.3.2. Chi phí đầu tư theo giai đoạn (ước tính tham khảo)

| Giai đoạn | Hoạt động | Chi phí ước tính (VNĐ) |
|---|---|---|
| Khởi đầu | Sơ đồ layout cơ bản trên giấy/Excel | Miễn phí - 2 triệu |
| Tăng trưởng | Thuê tư vấn thiết kế layout, phần mềm CAD cơ bản | 10-50 triệu |
| Mở rộng/Doanh nghiệp lớn | Mô phỏng chuyên sâu, tư vấn kỹ sư công nghiệp, cải tạo mặt bằng | Hàng trăm triệu đến hàng tỷ đồng |

#### 4.3.3. Ma trận quyết định đầu tư layout theo giai đoạn phát triển

| Giai đoạn doanh nghiệp | Ưu tiên đầu tư layout | Mức đầu tư khuyến nghị |
|---|---|---|
| Khởi nghiệp (Startup) | Linh hoạt, dễ điều chỉnh, chi phí thấp | Thấp, chủ yếu dùng công cụ miễn phí |
| Tăng trưởng nhanh | Chuẩn hoá để nhân rộng, nhất quán | Trung bình: playbook và tư vấn cơ bản |
| Ổn định/Trưởng thành | Tối ưu hiệu suất, cân nhắc tự động hoá | Cao: phần mềm mô phỏng, có thể tự động hoá |
| Tái cấu trúc/Chuyển đổi | Đánh giá lại toàn bộ, có thể thiết kế lại từ đầu | Rất cao: tư vấn chuyên sâu, đầu tư dài hạn |

#### 4.3.4. Rủi ro tài chính giữa các chiến lược thay đổi layout

| Chiến lược | Vốn đầu tư ban đầu | Rủi ro nếu sai | Khả năng hoàn tác |
|---|---|---|---|
| Thay đổi nhỏ, thử nghiệm từng phần | Thấp | Thấp | Dễ dàng |
| Thiết kế lại toàn bộ mặt bằng hiện tại | Trung bình - Cao | Trung bình | Khó, tốn kém |
| Xây nhà xưởng/kho mới theo layout tối ưu | Rất cao | Cao (nếu dự báo tăng trưởng sai) | Rất khó |
| Đầu tư tự động hoá (AGV/robot) | Rất cao | Rất cao nếu quy mô không đủ hoàn vốn | Rất khó |

### 4.4. Vai trò của các bên liên quan

Không nên để một cá nhân (chủ doanh nghiệp hoặc kỹ sư) quyết định đơn phương:

- **Nhân viên vận hành trực tiếp**: hiểu rõ điểm tắc nghẽn hằng ngày mà dữ liệu đơn thuần không thể hiện hết; họ cũng là người phải sống với layout mới nên cần được tham gia để giảm kháng cự.
- **Quản lý sản xuất/vận hành**: nắm yêu cầu năng suất và kế hoạch mở rộng.
- **Bộ phận an toàn lao động/PCCC**: bảo đảm lối thoát hiểm, khoảng cách an toàn giữa thiết bị.
- **Khách hàng (bán lẻ/dịch vụ)**: phản hồi trực tiếp về trải nghiệm di chuyển.
- **Chủ nhà/đơn vị thi công**: các thay đổi kết cấu, điện nước cần sự đồng ý của họ.

### 4.5. Những sai lầm thường gặp khi thiết kế layout

| Sai lầm | Hậu quả | Cách phòng tránh |
|---|---|---|
| Không dự trù không gian cho tăng trưởng | Cải tạo tốn kém khi mở rộng | Dự trù ít nhất 20-30% không gian dự phòng |
| Bỏ qua an toàn lao động/PCCC | Vi phạm quy định, rủi ro tai nạn | Tham vấn quy chuẩn xây dựng và PCCC từ đầu |
| Thiết kế dựa trên trực giác, không dựa trên dữ liệu | Layout không tối ưu, chi phí vận chuyển cao | Dùng From-To Chart và REL Chart dựa trên dữ liệu thực |
| Không thử nghiệm/mô phỏng trước khi triển khai toàn bộ | Phát hiện lỗi khi đã đầu tư lớn | Thử quy mô nhỏ hoặc mô phỏng bằng phần mềm/mô hình giấy |
| Tối ưu cục bộ (một khu) mà quên nút cổ chai toàn hệ | Đầu tư không tăng được sản lượng (ví dụ thêm ghế khám nhưng thiếu bác sĩ) | Xác định nút cổ chai trước (xem File 09 - Theory of Constraints) |
| Cân bằng chuyền với tải đầy 100% mà không có dự phòng | Chậm một trạm là mất sản lượng | Để dư 5-10% thời gian trạm nút cổ chai, kiểm tra nhạy cảm |
| Đầu tư tự động hoá khi chưa đủ quy mô | Không hoàn vốn | Tính payback (mục 2.9.2) trước khi đầu tư |
| Không đo lại sau khi thay đổi | Không biết có hiệu quả không | Đo KPI trước/sau, đánh giá lại sau 3-6 tháng |

---

## V. TOOLS & TEMPLATES

### 5.1. Công cụ hỗ trợ thiết kế layout

| Công cụ | Loại | Chi phí tham khảo | Phù hợp |
|---|---|---|---|
| Giấy vẽ tay + thước, mô hình giấy tỷ lệ | Thủ công | Miễn phí | SME nhỏ |
| Google Sheets / Excel | Bảng tính Load-Distance, line balancing | Miễn phí / có sẵn trong gói Office | SME |
| draw.io (diagrams.net), Visio | Sơ đồ mặt bằng đơn giản | draw.io miễn phí; Visio theo gói Microsoft | SME, doanh nghiệp vừa |
| Công cụ vẽ mặt bằng online (Floorplanner, SketchUp bản miễn phí...) | Vẽ 2D/3D nhanh | Có bản miễn phí, bản trả phí theo tháng | Cửa hàng, quán, văn phòng |
| AutoCAD | Thiết kế kỹ thuật chi tiết | Giá bản quyền thay đổi theo gói, cần kiểm tra giá hiện hành (ước tính vài triệu đến hàng chục triệu VNĐ/năm) | Doanh nghiệp vừa và lớn |
| FlexSim/Arena | Mô phỏng dòng chảy | Hàng chục triệu VNĐ/năm trở lên (ước tính, kiểm tra nhà cung cấp) | Doanh nghiệp lớn |
| People counter / đếm tay | Đo dòng khách bán lẻ | Từ miễn phí đến vài triệu VNĐ/thiết bị | Bán lẻ |

> Giá công cụ thay đổi theo thời gian và khu vực; các mức trên chỉ để so sánh cấp độ, cần xác minh trước khi ngân sách.

### 5.2. Mẫu Activity Relationship Chart đơn giản

```
        Kho    Sản xuất   Đóng gói   Văn phòng
Kho       -        A          E          U
SX        A        -          A          I
Đóng gói  E        A          -          O
VP        U        I          O          -
```

TCR (A=4, E=3, I=2, O=1, U=0): Kho 7; SX 10; Đóng gói 8; VP 3 (tính ở mục 2.1).

### 5.3. Bảng tính chi phí vận chuyển nội bộ (Material Handling Cost Worksheet)

Mẫu để điền (cột cuối là công thức nhân ba cột trước):

| Cặp bộ phận | Tần suất/ngày | Khoảng cách (m) | Đơn giá (đồng/lượt/mét) | Chi phí/ngày |
|---|---|---|---|---|
| Kho ↔ Sản xuất | ___ | ___ | ___ | = tần suất × khoảng cách × đơn giá |
| Sản xuất ↔ Đóng gói | ___ | ___ | ___ | ___ |
| Đóng gói ↔ Kho thành phẩm | ___ | ___ | ___ | ___ |

Ví dụ đã điền (dữ liệu mục 2.2, phương án 2, đơn giá 200 đồng):

| Cặp | Tần suất | Khoảng cách (m) | Đơn giá | Chi phí/ngày (đồng) |
|---|---|---|---|---|
| Kho - SX | 120 | 20 | 200 | 480.000 |
| SX - Đóng gói | 100 | 20 | 200 | 400.000 |
| Đóng gói - KTP | 100 | 20 | 200 | 400.000 |
| Kho - Đóng gói | 10 | 40 | 200 | 80.000 |
| SX - KTP | 5 | 40 | 200 | 40.000 |
| **Tổng** | | | | **1.400.000** |

**Công thức Excel/Google Sheets**:

- Chi phí mỗi dòng: `=B2*C2*D2`
- Tổng chi phí/ngày: `=SUM(E2:E6)` hoặc gộp `=SUMPRODUCT(B2:B6,C2:C6,D2:D6)`
- Khoảng cách rectilinear từ toạ độ ô: `=ABS(x1-x2)+ABS(y1-y2)`
- Load-Distance: `=SUMPRODUCT(Tải, Khoảng_cách)`

### 5.4. Bảng tính cân bằng chuyền (Line Balancing)

Bố cục các cột: Task | Thời gian | Tiền nhiệm | RPW | Trạm | Thời gian trạm.

- Takt time: `=Thời_gian_khả_dụng/Nhu_cầu` (ví dụ `=25200/210` ra 120)
- Số trạm tối thiểu: `=ROUNDUP(SUM(Thời_gian)/Chu_kỳ,0)`
- Hiệu suất: `=SUM(Thời_gian)/(Số_trạm*Chu_kỳ)`
- Thời gian rảnh: `=Số_trạm*Chu_kỳ-SUM(Thời_gian)`
- Kiểm tra trạm vượt chu kỳ: `=IF(SUMIF(Cột_trạm,n,Cột_thời_gian)>Chu_kỳ,"VƯỢT","OK")`

### 5.5. Sơ đồ quyết định chọn loại layout

Xem sơ đồ ở mục 1.4.

### 5.6. Ước tính thời gian triển khai theo quy mô dự án

| Quy mô dự án | Thời gian khảo sát | Thời gian thiết kế | Thời gian triển khai thực tế |
|---|---|---|---|
| Cửa hàng/văn phòng nhỏ | 1-2 tuần | 1-2 tuần | 1-2 tuần |
| Xưởng sản xuất vừa | 2-4 tuần | 4-6 tuần | 4-8 tuần |
| Nhà máy/kho lớn | 1-2 tháng | 2-3 tháng | 3-6 tháng |

---

## VI. BÀI TẬP THỰC HÀNH

Các bài có số liệu kèm đáp án tính toán (đã kiểm chứng bằng Python); các bài thiết kế mở kèm hướng dẫn giải.

**Bài 1.** Vẽ sơ đồ mặt bằng hiện tại của một cửa hàng/văn phòng bạn quen thuộc, đánh dấu điểm tắc nghẽn.
*Hướng dẫn*: vẽ tường, cửa, quầy; dùng bút màu vẽ đường đi của nhân viên và khách trong một giờ cao điểm; chỗ đường giao nhau hoặc quay đầu là ứng viên tắc nghẽn.

**Bài 2.** Xây REL Chart cho 4-5 bộ phận trong một doanh nghiệp giả định.
*Hướng dẫn*: lập bảng tam giác, gán A/E/I/O/U/X và lý do; tính TCR (A=4, E=3, I=2, O=1, U=0, X=-1); bộ phận có TCR cao đặt ở giữa. Mẫu ở mục 2.1.

**Bài 3.** Tính vị trí kho trung tâm bằng Center of Gravity cho 3 điểm giao hàng: (10; 20) khối lượng 200; (40; 10) khối lượng 300; (30; 50) khối lượng 100.
*Đáp án*: tổng khối lượng = 600. $C_x = (10 \times 200 + 40 \times 300 + 30 \times 100)/600 = (2.000 + 12.000 + 3.000)/600 = 17.000/600 = 28{,}33$. $C_y = (20 \times 200 + 10 \times 300 + 50 \times 100)/600 = (4.000 + 3.000 + 5.000)/600 = 20$. Vậy toạ độ khoảng **(28,33; 20)**, nằm gần điểm có khối lượng lớn nhất.

**Bài 4.** So sánh ưu nhược điểm khi chuyển từ Process Layout sang Cellular Layout cho một xưởng giả định.
*Hướng dẫn*: dùng bảng ở mục 1.4; thêm tính lead time theo mục 2.5.2 (ví dụ lô 50 chi tiết, 5 công đoạn, mỗi công đoạn 3 phút: theo lô = 5 × 50 × 3 = 750 phút; cell = 5 × 3 + 49 × 3 = 162 phút, giảm 78,4%) và chi phí máy trùng lặp.

**Bài 5.** Thiết kế lại layout quán cà phê/nhà hàng để giảm tắc nghẽn giờ cao điểm bằng one-way flow.
*Hướng dẫn*: làm bảng thời gian mỗi đơn như Case 3.5, tìm thành phần di chuyển/chờ có thể loại bỏ, tính năng lực của người đứng ở nút cổ chai (3.600 / thời gian xử lý của họ) và so với nhu cầu giờ cao điểm.

**Bài 6.** Phân tích case thất bại về thiếu chuẩn hoá layout chuỗi (Case 3.4), đề xuất playbook.
*Hướng dẫn*: xác định nguyên tắc bất biến (vị trí nhóm hàng chủ lực), biến thể theo diện tích (bảng ở Case 3.8.2), kế hoạch thí điểm có cửa hàng đối chứng.

**Bài 7.** 4 bộ phận A, B, C, D xếp trên một dãy tại các vị trí 0, 15, 30, 45 m. Tải (lượt/ngày): A-B 60, B-C 40, C-D 30, A-C 10, B-D 20; đơn giá 250 đồng/lượt/mét. So sánh thứ tự A-C-B-D với A-B-C-D.
*Đáp án*:
- Thứ tự A, C, B, D (A=0, C=15, B=30, D=45): khoảng cách A-B = 30, B-C = 15, C-D = 30, A-C = 15, B-D = 15. Load-Distance = 60×30 + 40×15 + 30×30 + 10×15 + 20×15 = 1.800 + 600 + 900 + 150 + 300 = **3.750**; chi phí = 3.750 × 250 = **937.500 đồng/ngày**.
- Thứ tự A, B, C, D (A=0, B=15, C=30, D=45): A-B = 15, B-C = 15, C-D = 15, A-C = 30, B-D = 30. LD = 60×15 + 40×15 + 30×15 + 10×30 + 20×30 = 900 + 600 + 450 + 300 + 600 = **2.850**; chi phí = **712.500 đồng/ngày**.
- Tiết kiệm = 225.000 đồng/ngày (24%), khoảng 5,85 triệu đồng/tháng (26 ngày). Đây cũng là thứ tự tối ưu trong 24 hoán vị.

**Bài 8.** Thiết kế Grid Layout cho siêu thị mini giả định, giải thích logic nhóm hàng.
*Hướng dẫn*: hàng thiết yếu (gạo, sữa) đặt sâu bên trong; hàng lợi nhuận cao ở vùng nóng gần lối vào và quầy thu ngân; lối đi chính rộng hơn lối đi phụ; ghi cả tính Sales per m².

**Bài 9.** Đề xuất layout phòng khám/spa nhỏ tối ưu số khách phục vụ đồng thời.
*Hướng dẫn*: tính năng lực theo cả hai ràng buộc (giường/ghế và nhân viên chuyên môn) như Case 3.6; năng lực = min của hai ràng buộc; đặt khu dùng chung (tiệt trùng, kho) ở trung tâm.

**Bài 10.** Nghiên cứu Toyota Cellular Layout, giải thích Group Technology giảm thời gian chu kỳ thế nào.
*Hướng dẫn*: dùng mục 2.5 (ROC) và 2.5.2 (batch-and-queue so với one-piece flow); nhấn mạnh điều kiện: công đoạn cân bằng, công nhân đa kỹ năng.

**Bài 11.** Phân tích IKEA Loop Layout: cơ chế tâm lý học hành vi.
*Hướng dẫn*: tiếp xúc nhiều hơn (số khu nhìn thấy), phòng mẫu giúp hình dung bối cảnh sử dụng, chi phí chìm về thời gian/công sức khiến khách thấy mua thêm là hợp lý; tính mô hình như Case 3.2 và nêu đánh đổi (lối tắt).

**Bài 12.** Weighted Distance cho 3 bộ phận A, B, C với các vị trí có sẵn cách nhau: S1 = 0 m, S2 = 10 m, S3 = 40 m. Tần suất: A-B 50, A-C 20, B-C 30 (lượt/ngày). Hiện tại A ở S1, C ở S2, B ở S3. Tìm phương án hoán đổi tốt nhất.
*Đáp án*: hiện tại khoảng cách A-B = 40, A-C = 10, B-C = 30; WD = 50×40 + 20×10 + 30×30 = 2.000 + 200 + 900 = **3.100**. Thử các hoán vị: (A, C, B) = 3.100; (B, A, C) = 2.300; (C, B, A) = 2.600; (A, B, C) = 2.200; (B, C, A) = 2.900; (C, A, B) = 2.900. Tốt nhất: A ở S1, B ở S2, C ở S3, tức **hoán đổi vị trí B và C**; WD = 50×10 + 20×40 + 30×30 = 500 + 800 + 900 = **2.200**, giảm (3.100 - 2.200) / 3.100 = **29%**. *Lý do*: cặp A-B có tần suất lớn nhất (50) nên cần gần nhất.

**Bài 13.** Thiết kế checklist kiểm tra trước khi chốt layout cho một dự án cụ thể.
*Hướng dẫn*: bắt đầu từ checklist ở Phụ lục, thêm tiêu chí đặc thù (ví dụ nhiệt độ cho kho lạnh) và người chịu trách nhiệm cho mỗi mục.

**Bài 14.** So sánh kho truyền thống và kho tự động hoá (AGV); khi nào nên tự động hoá? Giả sử đầu tư 3 tỷ đồng, thay 8 công nhân (lương 9 triệu/tháng, bảo hiểm 21,5% giả định), chi phí vận hành 300 triệu/năm.
*Đáp án*: lao động tiết kiệm = 8 × 9 triệu × 12 × 1,215 = 1.049,76 triệu/năm. Lợi ích ròng = 1.049,76 - 300 = 749,76 triệu/năm. Payback = 3.000 / 749,76 = **4,0 năm**, vượt ngưỡng 2-3 năm, nên **chưa nên đầu tư**; nên tối ưu layout thủ công trước. Điều kiện nên làm: số công nhân thay thế lớn hơn (nhiều ca) hoặc khối lượng tăng chắc chắn.

**Bài 15 (Line Balancing).** 8 task, thời gian (giây): A 12 (không tiền nhiệm), B 18 (sau A), C 9 (sau A), D 14 (sau B), E 10 (sau C), F 15 (sau D và E), G 8 (sau F), H 6 (sau G). Nhu cầu 900 sản phẩm/ngày, thời gian khả dụng 450 phút. Tính takt time, số trạm tối thiểu, phân bổ theo RPW, hiệu suất.
*Đáp án*:
- Thời gian khả dụng = 450 × 60 = 27.000 giây; takt = 27.000 / 900 = **30 giây**. Tổng thời gian = 12 + 18 + 9 + 14 + 10 + 15 + 8 + 6 = 92 giây. $N_{min} = \lceil 92/30 \rceil = \lceil 3{,}07 \rceil = 4$.
- RPW: A = 92; B = 61 (18+14+15+8+6); C = 48 (9+10+15+8+6); D = 43 (14+15+8+6); E = 39 (10+15+8+6); F = 29; G = 14; H = 6.
- Phân bổ với C = 30: Trạm 1 {A, B} = 30 (đầy); Trạm 2 {C, D} = 23; Trạm 3 {E, F} = 25; Trạm 4 {G, H} = 14.
- Hiệu suất = 92 / (4 × 30) = 92/120 = **76,7%**; thời gian nhàn rỗi = 120 - 92 = 28 giây.
- *Nhận xét*: tổng 92 giây chỉ vượt 90 giây (3 trạm × 30) có 2 giây; nếu cải tiến thao tác giảm tổng xuống 90 giây trở xuống và vẫn phân bổ được thì chỉ cần 3 trạm, hiệu suất lên tới 100%. Đây là ví dụ cho thấy cải tiến nhỏ ở đúng chỗ có thể bỏ được cả một trạm.

**Bài 16 (Chọn layout theo khối lượng).** Process layout: FC = 150 triệu đồng, VC = 80.000 đồng/sản phẩm; Product layout: FC = 600 triệu, VC = 35.000. Tìm điểm hoà vốn và kết luận cho nhu cầu 8.000 và 12.000 sản phẩm.
*Đáp án*: $Q^* = (600 - 150) \text{ triệu} / (80.000 - 35.000) = 450.000.000 / 45.000 = 10.000$. Tại 8.000: process = 150 + 0,08 × 8.000 = 790 triệu; product = 600 + 0,035 × 8.000 = 880 triệu, chọn **process**. Tại 12.000: process = 1.110 triệu; product = 1.020 triệu, chọn **product**.

**Bài 17 (KPI).** Cửa hàng có tổng diện tích 700 m², diện tích hữu ích (trưng bày, kho, quầy) 520 m², doanh thu 1,8 tỷ đồng/tháng, diện tích trưng bày 120 m². Tính Space Utilization và Sales per m².
*Đáp án*: Space Utilization = 520 / 700 = **74,3%** (đạt mục tiêu > 70%). Sales per m² = 1.800.000.000 / 120 = **15.000.000 đồng/m²/tháng**.

---

## PHỤ LỤC: CHECKLIST LAYOUT TỔNG HỢP

### A. Checklist kiểm tra trước khi chốt layout cuối cùng

- □ Đã xác nhận luồng di chuyển chính không bị cắt ngang/chồng chéo?
- □ Đã thu thập dữ liệu thực về tần suất di chuyển (From-To Chart) thay vì ước lượng cảm tính?
- □ Đã tính Load-Distance hoặc chi phí vận chuyển nội bộ trước và sau khi thay đổi?
- □ Đã lập ít nhất 2-3 phương án Block Layout để so sánh?
- □ Đã xác định nút cổ chai của toàn hệ thống (không chỉ cải thiện một khu)?
- □ Với chuyền: đã tính takt time, số trạm, hiệu suất và kiểm tra trạm nút cổ chai có dư thời gian?
- □ Đã dự trù không gian cho tăng trưởng ít nhất 20%?
- □ Đã kiểm tra tuân thủ PCCC, lối thoát hiểm, an toàn lao động?
- □ Đã tham vấn ý kiến nhân viên vận hành trực tiếp?
- □ Đã thử nghiệm quy mô nhỏ hoặc mô phỏng trước khi triển khai toàn bộ?
- □ Đã đánh giá tác động đến trải nghiệm nhân viên (ánh sáng, tiếng ồn, nghỉ ngơi)?
- □ Với chuỗi: đã có playbook và biến thể được phê duyệt trước?
- □ Đã xác định ai chịu trách nhiệm giám sát và đánh giá lại layout sau 3-6 tháng?

### B. Bảng thuật ngữ (Glossary)

| Thuật ngữ | Giải thích |
|---|---|
| Process Layout | Bố trí theo quy trình/chức năng |
| Product Layout | Bố trí theo trình tự sản xuất sản phẩm |
| Fixed-Position Layout | Bố trí vị trí cố định, nguồn lực di chuyển đến |
| Cellular Layout | Bố trí dạng ô/nhóm theo Group Technology |
| REL Chart | Activity Relationship Chart, sơ đồ quan hệ hoạt động |
| TCR | Total Closeness Rating, tổng điểm gần kề của một bộ phận trong REL Chart |
| From-To Chart | Ma trận khối lượng di chuyển giữa các bộ phận |
| Load-Distance / Weighted Distance | Tổng (tải × khoảng cách), đo công di chuyển |
| SLP | Systematic Layout Planning, phương pháp luận Muther |
| Block Layout | Sơ đồ bố trí khối tổng thể trước khi chi tiết hoá |
| Group Technology | Kỹ thuật nhóm chi tiết/quy trình tương tự |
| ROC | Rank Order Clustering, thuật toán lập cell |
| Takt Time | Nhịp sản xuất khớp nhu cầu = thời gian khả dụng / nhu cầu |
| Cycle Time (chuyền) | Thời gian tối đa mỗi trạm được dùng |
| RPW | Ranked Positional Weight, trọng số vị trí |
| Balance Delay | Tỷ lệ thời gian nhàn rỗi của chuyền = 100% - hiệu suất |
| One-piece flow | Dòng chảy từng chi tiết giữa các công đoạn |
| WIP | Work In Process, bán thành phẩm đang chờ |
| AGV/AMR | Robot tự hành vận chuyển hàng hoá |
| Goods-to-Person | Hàng di chuyển đến người lấy (thay vì người đi đến hàng) |
| Dark Store | Cửa hàng chỉ phục vụ giao hàng online |
| Click-and-Collect / Ship-from-Store | Mua online nhận tại cửa hàng / giao hàng từ kho cửa hàng |
| 5S | Phương pháp tổ chức nơi làm việc của Nhật Bản |
| Hot Zone / Cold Zone | Vùng tiếp xúc khách hàng cao / thấp |
| Eye-Level Selling | Trưng bày ở tầm mắt để tăng khả năng bán |
| Slotting Fee | Phí nhà cung cấp trả để có vị trí trưng bày thuận lợi |

### C. KPI đo lường layout

| KPI | Công thức/Ý nghĩa | Mục tiêu tham khảo |
|---|---|---|
| Material Handling Cost | Tổng chi phí vận chuyển nội bộ | Giảm liên tục |
| Load-Distance | Tổng tải × khoảng cách | Giảm so với trước thay đổi |
| Space Utilization | Diện tích hữu ích / Tổng diện tích | > 70% |
| Sales per m² | Doanh thu / Diện tích trưng bày (bán lẻ) | Tăng theo benchmark ngành |
| Travel Distance | Quãng đường di chuyển trung bình/ca | Giảm liên tục |
| Order Picking Time | Thời gian trung bình lấy một đơn | Giảm theo benchmark |
| Throughput per m² | Sản lượng trên mét vuông | Tăng theo thời gian |
| Hiệu suất chuyền | $\sum t_i / (N \times C)$ | Thường nhắm trên 85% (tuỳ ngành) |
| Lead time | Thời gian từ đầu vào đến đầu ra | Giảm liên tục |
| Employee Satisfaction Score | Khảo sát mức hài lòng về không gian làm việc | Trên 4/5 |
| Absenteeism Rate | Tỷ lệ vắng mặt liên quan điều kiện làm việc | Giảm |
| Return on Layout Investment | Lợi ích tài chính / Chi phí đầu tư layout | Càng cao càng tốt, đánh giá hằng năm |
| Aisle Utilization Rate | Tỷ lệ lối đi được dùng hiệu quả | Không quá hẹp gây nghẽn, không quá rộng gây lãng phí |
| Layout Change Frequency | Số lần điều chỉnh layout/năm | Ổn định, chỉ thay đổi khi có lý do rõ ràng |

### D. Sổ tay rủi ro layout (Risk Register mẫu)

| Rủi ro | Xác suất | Tác động | Biện pháp giảm thiểu |
|---|---|---|---|
| Không dự trù không gian mở rộng | Trung bình | Cao | Dự trù 20-30% không gian dự phòng |
| Vi phạm PCCC/an toàn lao động | Thấp | Rất cao | Tham vấn quy chuẩn từ giai đoạn thiết kế |
| Layout không nhất quán khi mở rộng chuỗi | Trung bình | Trung bình | Xây playbook chuẩn hoá và biến thể phê duyệt |
| Tự động hoá khi quy mô chưa đủ lớn | Trung bình | Cao | Phân tích hoà vốn trước khi đầu tư |
| Thiết kế không tham vấn nhân viên vận hành | Cao | Trung bình | Đưa nhân viên vào quy trình từ đầu |
| Chuyền cân bằng quá chặt, một trạm chậm là mất sản lượng | Trung bình | Trung bình | Kiểm tra nhạy cảm, dự phòng 5-10% thời gian |
| Tối ưu cục bộ bỏ sót nút cổ chai | Trung bình | Cao | Phân tích năng lực theo từng nguồn lực (ghế, bác sĩ...) |

### E. Bảng công thức tham chiếu nhanh

| Công thức | Ký hiệu | Ứng dụng |
|---|---|---|
| Tổng chi phí layout | $TC = FC + VC \times Q$; $Q^* = \Delta FC / \Delta VC$ | Chọn Process hay Product theo khối lượng |
| Center of Gravity | $C_x = \sum x_i W_i / \sum W_i$ | Vị trí tối ưu của cơ sở |
| Load-Distance | $LD = \sum f_{ij} \times d_{ij}$ | Đánh giá layout theo quy trình |
| Total Material Handling Cost | $\sum X_{ij} \cdot C_{ij} \cdot D_{ij}$ | Tổng chi phí vận chuyển nội bộ |
| Takt time | Thời gian khả dụng / Nhu cầu | Nhịp chuyền |
| Số trạm tối thiểu | $N_{min} = \lceil \sum t_i / C \rceil$ | Thiết kế chuyền |
| Hiệu suất chuyền | $E = \sum t_i / (N \times C)$ | Đánh giá cân bằng chuyền |
| RPW | $t_i +$ tổng thời gian task theo sau | Thứ tự ưu tiên phân bổ |
| Little's Law | $WIP = Throughput \times Lead\ Time$ | Quan hệ WIP và lead time |
| Payback tự động hoá | Đầu tư / (Tiết kiệm lao động - Chi phí vận hành) | Quyết định tự động hoá |
| Sales per m² | Doanh thu / Diện tích trưng bày | KPI bán lẻ |
| Space Utilization | Diện tích hữu ích / Tổng diện tích | Hiệu quả sử dụng không gian |

### F. Mức độ trưởng thành layout của doanh nghiệp

| Cấp độ | Đặc điểm | Hành động khuyến nghị |
|---|---|---|
| Sơ khai | Layout tự phát, không có dữ liệu | Bắt đầu ghi nhận tần suất di chuyển cơ bản |
| Cơ bản | Có sơ đồ nhưng chưa tối ưu theo dữ liệu | Áp dụng REL Chart và From-To Chart đơn giản |
| Trung bình | Đã áp dụng dòng chảy một chiều, giảm tắc nghẽn rõ | Chuẩn hoá thành playbook nếu có kế hoạch mở rộng |
| Nâng cao | Dùng phần mềm mô phỏng, tối ưu theo KPI | Cân nhắc tự động hoá nếu quy mô đủ lớn |

### G. Các yếu tố cần cân nhắc khi thiết kế layout tổng thể

| Yếu tố | Câu hỏi cần trả lời |
|---|---|
| Chiến lược quy trình | Sản phẩm/dịch vụ chuẩn hoá cao hay tuỳ biến theo khách? |
| Quy mô và tăng trưởng | Cần dự trù không gian mở rộng bao nhiêu trong 3-5 năm? |
| Ngân sách | Đủ nguồn lực cho tự động hoá hay chỉ ở mức thủ công? |
| An toàn và pháp lý | Có tuân thủ PCCC, an toàn lao động? |
| Trải nghiệm người dùng | Có tối ưu cho khách hàng/nhân viên? |
| Khả năng mở rộng/tái cấu hình | Có dễ điều chỉnh khi nhu cầu thay đổi? |

### H. Câu hỏi phỏng vấn nhân viên vận hành khi thu thập dữ liệu layout

Khi thực hiện bước 1 của quy trình thiết kế, nên phỏng vấn nhân viên trực tiếp để bổ sung thông tin định tính:

1. Khu vực nào bạn thấy thường xuyên bị tắc nghẽn hoặc phải chờ đợi?
2. Bạn phải di chuyển qua lại nhiều lần giữa các khu nào trong ca làm việc?
3. Có khu vực nào bạn thấy không an toàn hoặc bất tiện khi thao tác?
4. Nếu được đề xuất thay đổi một điều trong bố trí hiện tại, bạn sẽ đề xuất điều gì?

**Ghi chú về kết hợp định lượng và định tính**: các dự án layout thành công thường kết hợp phân tích định lượng nghiêm túc (From-To Chart, Load-Distance) và thông tin định tính từ người dùng không gian hằng ngày; chỉ dựa vào số liệu có thể bỏ lỡ những vấn đề mà chỉ người trong cuộc nhận biết.

### I. Câu hỏi tự kiểm tra nhanh

1. Bốn loại layout cơ bản là gì và mỗi loại phù hợp với tình huống nào?
2. Vì sao dòng chảy một chiều quan trọng với cả layout sản xuất lẫn dịch vụ?
3. Center of Gravity giải quyết bài toán gì? Giới hạn của nó là gì?
4. Khi nào doanh nghiệp nên cân nhắc layout tự động hoá (AGV/robot)? Công thức nào để quyết định?
5. Vì sao cần chuẩn hoá layout thành "playbook" khi mở rộng chuỗi, và vì sao playbook cần biến thể được phê duyệt?
6. Nêu 3 yếu tố cần cân nhắc khi thiết kế layout bền vững.
7. Giải thích "Hot Zone" và "Cold Zone" và ứng dụng thực tế.
8. Vì sao layout omnichannel cần thiết kế khác layout bán lẻ truyền thống?
9. Nêu ví dụ thực tế về Eye-Level Selling trong một cửa hàng bạn từng ghé thăm.
10. Giải thích mối liên hệ giữa 5S và hiệu quả của layout đã thiết kế tốt.
11. So sánh chi phí và rủi ro giữa layout linh hoạt (module hoá) và layout cố định dài hạn cho doanh nghiệp tăng trưởng nhanh.
12. Vì sao takt time bằng thời gian khả dụng chia cho nhu cầu, và vì sao số trạm tối thiểu phải làm tròn lên?
13. Vì sao hiệu suất chuyền không tăng đơn điệu khi sản lượng tăng (xem bảng tình huống mục 2.4.2)?
14. Vì sao mở rộng một nguồn lực (thêm ghế khám) có thể không tăng năng lực toàn hệ thống?

---

## TÀI LIỆU THAM KHẢO

### Sách tham khảo
1. Heizer, J., Render, B., & Munson, C. (2020). *Operations Management: Sustainability and Supply Chain Management*. Pearson (chương Facility Layout).
2. Tompkins, J. A. et al. (2010). *Facilities Planning*. Wiley.
3. Muther, R. (1973). *Systematic Layout Planning*. Cahners Books (xuất bản lần đầu 1961).
4. Underhill, P. (2009). *Why We Buy: The Science of Shopping*. Simon & Schuster (nghiên cứu hành vi khách hàng và thiết kế cửa hàng bán lẻ).

### Nguồn tài liệu trực tuyến bổ sung
1. Tài liệu hướng dẫn Systematic Layout Planning (SLP) của Muther Associates.
2. Các bài viết phân tích case study Amazon Kiva Systems về robot AGV trong kho hàng.
3. Báo cáo nghiên cứu hành vi mua sắm bán lẻ của Nielsen/Kantar về hiệu ứng vị trí trưng bày.

### Liên kết nội bộ
- [01-process-design-analysis.md](./01-process-design-analysis.md) - Chiến lược quy trình quyết định loại layout phù hợp.
- [05-capacity-planning.md](./05-capacity-planning.md) - Line Balancing liên quan trực tiếp đến Product Layout.
- [03-supply-chain-management.md](./03-supply-chain-management.md) - Cross-docking và mô hình phân phối liên quan đến thiết kế layout kho hàng.
- [04-inventory-management.md](./04-inventory-management.md) - ABC Analysis ảnh hưởng đến vị trí lưu trữ hàng hoá trong kho.
- [09-theory-of-constraints.md](./09-theory-of-constraints.md) - Nút cổ chai, liên quan đến bài toán năng lực ở Case 3.6.

*Tài liệu tham khảo: các số liệu trong các case study tên giả và mô hình minh họa là giả định do tác giả thiết kế; các tên tuổi, mốc lịch sử (Ford 1913, Salveson 1955, Muther 1961, King 1980, Underhill 1999) được nêu theo kiến thức học thuật phổ biến và nên đối chiếu nguồn gốc khi trích dẫn chính thức.*

*(Hết file 08 - Chiến lược Bố trí Mặt bằng)*
