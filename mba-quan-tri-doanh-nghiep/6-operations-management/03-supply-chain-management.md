# 03. Quản trị Chuỗi Cung ứng (Supply Chain Management - SCM)

> **Mục tiêu**: Giúp người mới hiểu *bản chất* của quản trị chuỗi cung ứng — vì sao phải tối ưu cả chuỗi chứ không chỉ từng khâu — nắm các công cụ cốt lõi (SCOR, Bullwhip, Fisher, Kraljic, Supplier Scorecard, TCO, S&OP, quản trị rủi ro), xem chúng vận hành qua các case phân tích từng bước (quốc tế, Việt Nam, SME) và áp dụng được ngay ở quy mô doanh nghiệp vừa và nhỏ (SME).

> File thuộc bộ kiến thức Quản trị Vận hành (Operations Management) - MBA Knowledge Base
> Liên kết: [01-process-design-analysis.md](./01-process-design-analysis.md) | [02-quality-management.md](./02-quality-management.md) | [04-inventory-management.md](./04-inventory-management.md)

---

## MỤC LỤC

- [I. Khái niệm & Lý thuyết](#i-khái-niệm--lý-thuyết)
- [II. Chi tiết từng thành phần](#ii-chi-tiết-từng-thành-phần)
- [III. Case Studies thực tế](#iii-case-studies-thực-tế)
- [IV. Ứng dụng cho SME](#iv-ứng-dụng-cho-sme)
- [V. Tools & Templates](#v-tools--templates)
- [VI. Bài tập thực hành](#vi-bài-tập-thực-hành)
- [PHỤ LỤC: CHECKLIST QUẢN TRỊ CHUỖI CUNG ỨNG TỔNG HỢP](#phụ-lục-checklist-quản-trị-chuỗi-cung-ứng-tổng-hợp)
- [TÀI LIỆU THAM KHẢO](#tài-liệu-tham-khảo)

> **Quy ước**: Số liệu doanh nghiệp quốc tế/Việt Nam không có nguồn kiểm chứng trong tài liệu này được ghi rõ "ước tính/minh họa". Mọi số liệu của các case SME và bài tập là **giả định minh họa** do tác giả tự thiết kế (đã kiểm tra tính nhất quán bằng tính toán).

---

## I. Khái niệm & Lý thuyết

### 1.1. Định nghĩa & nguồn gốc của Quản trị Chuỗi Cung ứng

**Chuỗi cung ứng (Supply Chain)** là mạng lưới các tổ chức, con người, hoạt động, thông tin và nguồn lực cùng tham gia đưa một sản phẩm/dịch vụ từ nhà cung cấp nguyên liệu thô đến tay khách hàng cuối cùng.

**Quản trị chuỗi cung ứng (Supply Chain Management - SCM)** là việc hoạch định, tổ chức và kiểm soát ba dòng chảy xuyên suốt mạng lưới đó: dòng vật chất (nguyên liệu, bán thành phẩm, thành phẩm), dòng thông tin (đơn hàng, dự báo, tồn kho) và dòng tài chính (thanh toán, công nợ), từ nhà cung cấp cấp 2 (Tier-2) đến khách hàng cuối (End Customer).

**Nguồn gốc**: thuật ngữ "Supply Chain Management" thường được ghi nhận là do Keith Oliver (Booz Allen Hamilton) đưa ra năm 1982, trong bối cảnh các doanh nghiệp phương Tây nhận ra đối thủ Nhật (Toyota và hệ sinh thái nhà cung cấp) cạnh tranh bằng *cả hệ thống* chứ không chỉ bằng nhà máy của mình. Hiệp hội CSCMP (Council of Supply Chain Management Professionals) mô tả SCM bao trùm tìm nguồn (sourcing), thu mua (procurement), chuyển đổi (conversion) và logistics, đồng thời nhấn mạnh sự phối hợp với đối tác trong kênh: nhà cung cấp, trung gian, nhà cung cấp dịch vụ logistics bên thứ ba (3PL) và khách hàng.

**Tại sao cần "quản trị cả chuỗi"?** Vấn đề kinh doanh mà SCM giải quyết là **tối ưu cục bộ (local optimization)**: phòng mua hàng chọn giá rẻ nhất → hàng kém chất lượng, giao trễ → phòng sản xuất dừng máy → phòng kinh doanh mất đơn. Mỗi bộ phận đạt KPI riêng nhưng *tổng chi phí và tổng lợi nhuận của cả chuỗi* xấu đi. SCM chuyển câu hỏi từ "khâu của tôi rẻ nhất chưa?" sang "**toàn chuỗi tạo ra giá trị cho khách hàng với tổng chi phí thấp nhất chưa?**".

### 1.2. Cấu trúc chuỗi cung ứng điển hình & ba dòng chảy

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ Nhà cung │───▶│ Nhà cung │───▶│  Doanh   │───▶│  Nhà     │───▶│  Nhà bán │───▶│  Khách   │
│ cấp cấp 2│    │ cấp cấp 1│    │ nghiệp   │    │ phân phối│    │  lẻ      │    │  hàng    │
│(Tier-2)  │    │(Tier-1)  │    │(Focal Co)│    │(Distributor)│ │(Retailer)│    │(Consumer)│
└──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
     ▲                ▲                ▲                ▲                ▲               │
     └────────────────┴────────────────┴── Dòng thông tin (đơn hàng, dự báo, POS data) ◀──┘
     │                │                │                │                │
     └────────────────┴────────────────┴──── Dòng tài chính (thanh toán, công nợ) ────────▶
                  (Dòng vật chất đi xuôi từ trái sang phải, dòng hàng trả về đi ngược lại)
```

| Dòng chảy | Nội dung | Hướng | Ý nghĩa quản trị |
|---|---|---|---|
| **Vật chất (Physical Flow)** | Nguyên liệu → sản xuất → thành phẩm → phân phối → bán lẻ; hàng trả lại, tái chế (reverse logistics) | Xuôi dòng (và ngược khi trả hàng) | Quyết định chi phí vận chuyển, tồn kho, thời gian giao |
| **Thông tin (Information Flow)** | Dự báo nhu cầu, đơn đặt hàng, mức tồn kho, lịch giao | Hai chiều, ngày càng real-time (EDI, API, IoT) | Thông tin sai/trễ là *gốc rễ* của hiệu ứng Bullwhip |
| **Tài chính (Financial Flow)** | Hạn mức tín dụng, điều khoản thanh toán, hóa đơn, dòng tiền | Ngược dòng (tiền chảy từ khách về nhà cung cấp) | Quyết định vốn lưu động (working capital) của mỗi bên |

### 1.3. Mô hình SCOR (Supply Chain Operations Reference)

**Tại sao cần SCOR?** Hai doanh nghiệp cùng nói "logistics" nhưng mỗi nơi hiểu một kiểu thì không thể so sánh hay cải tiến có hệ thống. SCOR cung cấp **ngôn ngữ chung** để mô tả, đo lường và benchmark chuỗi cung ứng.

**Nguồn gốc**: SCOR do Supply Chain Council (thành lập năm 1996 bởi hai công ty tư vấn PRTM và AMR Research cùng một nhóm doanh nghiệp tiên phong) phát triển; hội này sau đó sáp nhập vào APICS, nay là ASCM. Mô hình ban đầu có 4 quy trình (Plan, Source, Make, Deliver), về sau bổ sung Return rồi Enable; các phiên bản mới còn tiếp tục mở rộng theo hướng số hóa.

| Quy trình | Mô tả | Ví dụ hoạt động |
|---|---|---|
| **Plan (Hoạch định)** | Cân đối cung-cầu, hoạch định nguồn lực | Dự báo nhu cầu, S&OP, hoạch định năng lực |
| **Source (Tìm nguồn)** | Tìm và thu mua nguyên liệu, dịch vụ | Chọn NCC, đàm phán hợp đồng, đặt hàng |
| **Make (Sản xuất)** | Chuyển nguyên liệu thành thành phẩm | Lên lịch sản xuất, kiểm soát chất lượng |
| **Deliver (Giao hàng)** | Quản lý đơn hàng, kho, vận chuyển đến khách | Xử lý đơn, kho vận, vận tải, lắp đặt |
| **Return (Trả hàng)** | Xử lý hàng trả lại từ khách hoặc về NCC | Bảo hành, thu hồi sản phẩm lỗi, tái chế |
| **Enable (Hỗ trợ)** | Các hoạt động hỗ trợ xuyên suốt | Quản trị rủi ro, hợp đồng, dữ liệu, CNTT |

Từ SCOR, doanh nghiệp benchmark qua các chỉ số: Perfect Order Fulfillment, Order Fulfillment Cycle Time, Supply Chain Cost, Cash-to-Cash Cycle Time (giải thích công thức ở mục 2.8).

### 1.4. Hiệu ứng Bullwhip (Bullwhip Effect)

**Nguồn gốc**: Jay Forrester (MIT) mô tả hiện tượng khuếch đại nhu cầu trong cuốn *Industrial Dynamics* (1961). Năm 1997, Hau Lee, V. Padmanabhan và Seungjin Whang hệ thống hóa thành 4 nguyên nhân trong bài "The Bullwhip Effect in Supply Chains" (*Sloan Management Review*), sau khi quan sát hiện tượng tại Procter & Gamble: nhu cầu tã Pampers ở người tiêu dùng khá ổn định, nhưng đơn hàng gửi lên nhà máy P&G và nhà cung cấp nguyên liệu dao động mạnh hơn nhiều.

**Tại sao quan trọng?** Biến động bị khuếch đại → nhà sản xuất phải giữ tồn kho đệm lớn, thuê thêm công suất "phòng xa", lúc thừa lúc thiếu, chi phí tăng ở *mọi* mắt xích mà không ai thực sự bán thêm được hàng. Đây là bằng chứng rõ nhất rằng tối ưu cục bộ làm hại cả chuỗi.

```
Biến động nhu cầu tăng dần khi đi ngược dòng chuỗi cung ứng:

Nhu cầu thực    ▂▃▂▃▂▃▂▃  (dao động nhỏ, ổn định)       ← Người tiêu dùng
Đơn hàng        ▂▅▂▇▁▆▁█  (dao động lớn hơn)             ← Nhà bán lẻ
Đơn hàng        ▁▇▁█▁▇▁█  (dao động lớn hơn nữa)          ← Nhà phân phối
Đơn hàng        █▁█▁█▁█▁  (cực đại - "cái roi da")        ← Nhà sản xuất
```

**Hình dung**: cú vung nhẹ ở cán roi (nhu cầu cuối) tạo biên độ rất lớn ở đầu roi (nhà cung cấp thượng nguồn).

**4 nguyên nhân chính** (Lee, Padmanabhan, Whang, 1997):

| # | Nguyên nhân | Cơ chế | Ví dụ SME |
|---|---|---|---|
| 1 | **Xử lý tín hiệu nhu cầu (Demand Signal Processing)** | Mỗi mắt xích dự báo dựa trên *đơn hàng* của mắt xích liền kề thay vì nhu cầu thực → sai số được cộng dồn và nhân lên | Nhà phân phối thấy đơn tăng 10% nên đặt nhà máy +25% "cho chắc" |
| 2 | **Đặt hàng theo lô (Order Batching)** | Gộp đơn để tiết kiệm phí đặt hàng/vận chuyển hoặc đạt MOQ → đơn đến theo "cục" | Tiệm tạp hóa chỉ đặt 2 tuần/lần; nhà máy yêu cầu tối thiểu 1 pallet |
| 3 | **Biến động giá (Price Fluctuation)** | Khuyến mãi, chiết khấu khiến mua dồn trước (forward buying), đơn hàng không phản ánh nhu cầu | Giảm giá cuối quý → đại lý nhập gấp, sau đó im lặng 3 tuần |
| 4 | **Trò chơi phân bổ & thiếu hụt (Rationing & Shortage Gaming)** | Khi nghi thiếu hàng, khách đặt gấp đôi nhu cầu để được phân bổ nhiều hơn; hàng về đủ thì hủy đơn | Mùa khan hiếm nguyên liệu, mọi đại lý đều "đặt khống" |

**Định lượng hiệu ứng Bullwhip — Tại sao đo bằng phương sai?** Vì "dao động" là sự phân tán của các giá trị quanh trung bình; phương sai (variance) đo đúng điều đó và có thể so sánh giữa hai mắt xích. Hiệu ứng Bullwhip được đo bằng tỷ số phương sai đơn hàng đặt ra so với phương sai nhu cầu nhận vào:

$$BW = \frac{\text{Var}(\text{Đơn hàng đặt lên thượng nguồn})}{\text{Var}(\text{Nhu cầu cuối})}$$

- $BW = 1$: không khuếch đại. $BW > 1$: có Bullwhip, càng lớn càng nghiêm trọng.
- Ghi chú: nhiều nghiên cứu dùng hệ số biến thiên (CV = σ/trung bình) để so sánh khi các mắt xích có quy mô khác nhau; ở đây dùng phương sai cho gọn vì cùng đơn vị đo.

**Ví dụ lý thuyết (Chen, Drezner, Ryan & Simchi-Levi, 2000)**: với mô hình đặt hàng "bổ sung đến mức tối đa" (order-up-to) và dự báo bằng trung bình động p kỳ, lead time L kỳ, nhu cầu độc lập, hệ số khuếch đại *tối thiểu* là:

$$BW \ge 1 + \frac{2L}{p} + \frac{2L^2}{p^2}$$

Với $L = 2$ tuần, $p = 4$ tuần: $BW \ge 1 + \frac{2 \times 2}{4} + \frac{2 \times 4}{16} = 1 + 1 + 0{,}5 = 2{,}5$. Ý nghĩa: **chỉ riêng việc dự báo bằng trung bình động 4 tuần với lead time 2 tuần đã khuếch đại phương sai ít nhất 2,5 lần ở một mắt xích** — và hiệu ứng này nhân lên qua nhiều mắt xích. Lead time $L$ càng dài, khuếch đại càng mạnh (xuất hiện bình phương) → lý do rút ngắn lead time là giải pháp then chốt.

**Giải pháp giảm Bullwhip** (đối ứng từng nguyên nhân):
- **Chia sẻ dữ liệu bán hàng POS (Information Sharing)** → xử lý nguyên nhân 1: thượng nguồn thấy nhu cầu thực.
- **VMI (Vendor Managed Inventory)** và **CPFR** → nhà cung cấp cùng quản lý/hoạch định, giảm tín hiệu méo (mục 2.4).
- **Giảm quy mô lô và lead time** (đặt hàng điện tử, giao thường xuyên hơn) → xử lý nguyên nhân 2 và công thức trên.
- **Giá ổn định (EDLP - Every Day Low Price)** thay vì khuyến mãi dồn dập → xử lý nguyên nhân 3.
- **Phân bổ theo lịch sử bán thực (sell-through)** thay vì theo số đặt → xử lý nguyên nhân 4.

### 1.5. Mô hình chiến lược chuỗi cung ứng: Hiệu quả vs Đáp ứng nhanh (Fisher, 1997)

**Nguồn gốc**: Marshall Fisher (Wharton), bài "What Is the Right Supply Chain for Your Product?" (*Harvard Business Review*, 1997). Ông nhận thấy nhiều công ty có chuỗi cung ứng rất "tốt" nhưng *sai loại* cho sản phẩm của mình.

**Tại sao?** Mỗi chuỗi cung ứng đánh đổi giữa **chi phí thấp** và **phản ứng nhanh**. Tính chất nhu cầu của sản phẩm quyết định nên ưu tiên đầu nào: sản phẩm dễ dự báo thì "hy sinh" tốc độ lấy chi phí; sản phẩm khó dự báo thì "hy sinh" chi phí lấy tốc độ, vì thiếu hàng/dư hàng đều rất đắt.

| Tiêu chí | Sản phẩm chức năng (Functional) | Sản phẩm sáng tạo (Innovative) |
|---|---|---|
| Vòng đời sản phẩm | Dài (> 2 năm) | Ngắn (3 tháng - 1 năm) |
| Biên lợi nhuận | Thấp (5-20%) | Cao (20-60%) |
| Độ chính xác dự báo | Cao (sai số khoảng 10%) | Thấp (sai số 40-100%) |
| Ví dụ | Gạo, muối, giấy vệ sinh | Thời trang, điện thoại mới, đồ chơi theo trend |
| **Chiến lược phù hợp** | **Chuỗi cung ứng hiệu quả (Efficient SC)** | **Chuỗi cung ứng đáp ứng nhanh (Responsive SC)** |
| Trọng tâm | Tối thiểu hóa chi phí | Tối đa hóa tốc độ phản hồi |
| Tồn kho | Thấp, quay vòng nhanh | Tồn kho đệm cao hơn |
| Lead time | Rút ngắn nhưng không phải ưu tiên số 1 | Ưu tiên số 1 |
| Lựa chọn NCC | Theo chi phí và chất lượng | Theo tốc độ, linh hoạt |

Các con số trong bảng là ngưỡng minh họa của Fisher, không phải ranh giới cứng.

**Ma trận khớp chiến lược (Fit Matrix)**:

```
                       Chuỗi HIỆU QUẢ         Chuỗi ĐÁP ỨNG NHANH
                      (Efficient)            (Responsive)
Sản phẩm CHỨC NĂNG   ✔ KHỚP                  ✘ Lãng phí chi phí
(Functional)         (JIT, chi phí thấp)      (đệm quá nhiều, giá cao)

Sản phẩm SÁNG TẠO    ✘ KHÔNG KHỚP            ✔ KHỚP
(Innovative)         (thiếu hàng hoặc ế)     (lô nhỏ, lead time ngắn)
```

**Sai lầm phổ biến**: áp chiến lược "hiệu quả" cho sản phẩm sáng tạo → thiếu hàng khi nhu cầu bùng nổ hoặc tồn kho ế khi trend qua đi. Đây là nguyên nhân khiến nhiều hãng thời trang nhanh không linh hoạt gặp khó (xem Case Zara ở mục III).

### 1.6. Chuỗi cung ứng tinh gọn (Lean) vs Linh hoạt (Agile) vs Leagile

**Tại sao cần tách ba khái niệm?** Fisher cho biết *loại sản phẩm* nào cần gì; Lean/Agile/Leagile mô tả *cách thiết kế vận hành* để đạt điều đó. Một chuỗi thực tế thường là hỗn hợp: đoạn thượng nguồn (nguyên liệu, vải mộc) làm theo kế hoạch để rẻ, đoạn hạ nguồn (hoàn thiện, giao hàng) làm theo đơn để nhanh. Điểm chuyển giữa hai đoạn gọi là **điểm phân tách (Decoupling Point)**.

| Tiêu chí | Lean Supply Chain | Agile Supply Chain |
|---|---|---|
| Mục tiêu | Loại bỏ lãng phí, tối thiểu chi phí | Đáp ứng nhanh biến động nhu cầu |
| Tồn kho | Tối thiểu (JIT) | Tồn kho đệm chiến lược tại điểm phân tách |
| Phù hợp với | Nhu cầu ổn định, dự báo chính xác | Nhu cầu biến động, khó dự báo |
| Rủi ro chính | Dễ tổn thương khi gián đoạn bất ngờ | Chi phí vận hành cao hơn |
| Ví dụ ngành | Ô tô sản xuất hàng loạt, FMCG cơ bản | Thời trang nhanh, công nghệ, đồ chơi theo trend |

**Mô hình lai Leagile**: Lean từ thượng nguồn đến điểm phân tách, Agile từ điểm phân tách đến khách hàng (áp dụng ở Zara, Dell). Ví dụ SME: xưởng may tồn sẵn vải mộc (Lean, mua theo kế hoạch) nhưng chỉ cắt-may-nhuộm khi có đơn (Agile).

```
Nguyên liệu ──▶ [Sản xuất theo kế hoạch - LEAN] ──▶ ◆ ĐIỂM PHÂN TÁCH ──▶ [Hoàn thiện theo đơn - AGILE] ──▶ Khách
                  (tồn kho bán thành phẩm)           (tồn đệm chiến lược)
```

---

## II. Chi tiết từng thành phần

### 2.1. Quản trị quan hệ nhà cung cấp (Supplier Relationship Management - SRM)

#### 2.1.1. Ma trận Kraljic (Kraljic Matrix)

**Nguồn gốc**: Peter Kraljic (McKinsey), bài "Purchasing Must Become Supply Management" (*Harvard Business Review*, 1983), viết sau cú sốc dầu mỏ thập niên 1970 khi nhiều công ty nhận ra bộ phận mua hàng chỉ lo "ép giá" mà không nhìn thấy rủi ro nguồn cung.

**Tại sao?** Doanh nghiệp có hàng trăm mặt hàng và nhà cung cấp nhưng thời gian quản trị có hạn. Không thể "hợp tác chiến lược" với tất cả, cũng không nên chỉ "ép giá" với tất cả. Kraljic dùng **hai trục** để phân bổ nguồn lực quản trị đúng chỗ:

- Trục dọc **Rủi ro cung ứng (Supply Risk)**: nguồn hiếm? ít NCC? khó thay thế? biến động giá?
- Trục ngang **Tác động lợi nhuận (Profit Impact)**: chiếm bao nhiêu % chi phí/giá trị sản phẩm cuối?

```
Rủi ro cung ứng
    Cao  │  NÚT THẮT (Bottleneck)       │  CHIẾN LƯỢC (Strategic)
         │  - Ít NCC thay thế           │  - Giá trị cao + rủi ro cao
         │  - Giá trị thấp              │  - Đối tác dài hạn
         │  → Đảm bảo nguồn cung        │  → Hợp tác sâu, chia sẻ thông tin
         │──────────────────────────────┼──────────────────────────────
    Thấp │  KHÔNG QUAN TRỌNG            │  ĐÒN BẨY (Leverage)
         │  (Non-critical)              │  - Nhiều NCC thay thế
         │  - Giá trị thấp, rủi ro thấp │  - Giá trị cao
         │  → Đơn giản hóa quy trình    │  → Đấu thầu cạnh tranh, ép giá
         └──────────────────────────────┴──────────────────────────────
              Thấp                              Cao
                       Tác động lợi nhuận (Profit Impact)
```

| Nhóm | Chiến lược | Công cụ điển hình |
|---|---|---|
| **Chiến lược (Strategic)** | Quan hệ đối tác dài hạn, chia sẻ dự báo, đồng phát triển (co-development) | Hợp đồng khung nhiều năm, họp định kỳ, scorecard |
| **Đòn bẩy (Leverage)** | Tận dụng sức mạnh đàm phán | Đấu thầu RFQ, e-auction định kỳ, đa nguồn |
| **Nút thắt (Bottleneck)** | Bảo đảm nguồn cung dù giá cao hơn một chút | NCC dự phòng, tồn kho an toàn, hợp đồng bảo đảm sản lượng |
| **Không quan trọng (Non-critical)** | Giảm chi phí giao dịch | P-card, e-procurement, gộp đơn, danh mục chuẩn hóa |

**Cách chấm điểm để xếp vào ô (mẫu SME)**: chấm mỗi mặt hàng 1-5 cho "Tác động lợi nhuận" (dựa trên % chi phí) và "Rủi ro cung ứng" (số NCC thay thế, thời gian chuyển đổi, biến động giá); điểm ≥ 3,5 coi là "Cao". Ví dụ áp dụng cho xưởng gỗ nội thất ở mục III (Case 4).

#### 2.1.2. Đánh giá nhà cung cấp (Supplier Scorecard)

**Tại sao dùng điểm có trọng số?** Chọn NCC chỉ theo giá là "tối ưu cục bộ". NCC rẻ hơn 3% nhưng giao trễ 15% đơn hàng sẽ gây dừng dây chuyền, đắt hơn nhiều. Scorecard biến các khía cạnh *khác nhau* (chất lượng, giao hàng, giá, năng lực, ESG) thành một con số so sánh được; **trọng số thể hiện ưu tiên chiến lược** của doanh nghiệp (ngành thực phẩm tăng trọng số chất lượng; ngành xuất khẩu tăng ESG).

$$S = \sum_{i=1}^{n} w_i \cdot s_i, \qquad \sum w_i = 100\%$$

Trong đó $S$ là tổng điểm nhà cung cấp (thang 1-5), $w_i$ là trọng số tiêu chí $i$, $s_i$ là điểm tiêu chí $i$.

| Tiêu chí | Trọng số | Thang điểm | Chỉ số đo gợi ý |
|---|---|---|---|
| Chất lượng (Quality) | 30% | 1-5 | Tỷ lệ lỗi, PPM (parts per million) |
| Giao hàng đúng hạn (On-time Delivery - OTD) | 25% | 1-5 | % đơn giao đúng hạn |
| Giá cả & chi phí tổng (Total Cost) | 20% | 1-5 | Giá + chi phí ẩn (xem TCO mục 2.2.3) |
| Năng lực & công nghệ (Capability) | 15% | 1-5 | Công suất dự phòng, chứng nhận, R&D |
| Trách nhiệm xã hội (ESG compliance) | 10% | 1-5 | Chứng nhận, kết quả audit |

**Ví dụ tính (nhà cung cấp X)**: điểm lần lượt 4, 3, 5, 3, 2 → $S = 0{,}30\times4 + 0{,}25\times3 + 0{,}20\times5 + 0{,}15\times3 + 0{,}10\times2 = 1{,}20 + 0{,}75 + 1{,}00 + 0{,}45 + 0{,}20 = 3{,}60$ → xếp loại "Duy trì" (3,0-4,0). Nhận xét: X rẻ nhất nhưng yếu ESG và giao hàng; kế hoạch hành động là yêu cầu cải thiện OTD trước khi tăng tỷ trọng.

### 2.2. Thu mua & Tìm nguồn cung ứng (Procurement & Sourcing)

#### 2.2.1. Quy trình thu mua chiến lược (Strategic Sourcing) - 7 bước

**Tại sao theo quy trình?** Thu mua theo cảm tính (quen biết, báo giá đầu tiên) khiến doanh nghiệp không biết mình đang chi tiền vào đâu. Quy trình 7 bước bắt đầu từ *dữ liệu chi tiêu* — theo quy tắc Pareto, thường 20% mặt hàng chiếm khoảng 80% chi tiêu, nên tối ưu đúng 20% ấy mang lại phần lớn hiệu quả.

1. Phân tích chi tiêu (Spend Analysis) - phân loại chi tiêu theo danh mục, nhà cung cấp.
2. Phân tích thị trường cung ứng (Supply Market Analysis).
3. Xây dựng chiến lược tìm nguồn (theo ma trận Kraljic).
4. Thu thập thông tin NCC (RFI - Request for Information).
5. Đấu thầu/chào giá (RFP/RFQ - Request for Proposal/Quotation).
6. Đàm phán & lựa chọn NCC.
7. Triển khai hợp đồng & theo dõi hiệu suất (Contract Implementation & Performance Monitoring).

#### 2.2.2. Đơn nguồn vs đa nguồn (Single vs Multiple Sourcing)

| Tiêu chí | Đơn nguồn (Single Sourcing) | Đa nguồn (Multiple Sourcing) |
|---|---|---|
| Rủi ro gián đoạn | Cao | Thấp - phân tán rủi ro |
| Sức mạnh đàm phán giá | Thấp hơn về dài hạn | Cao hơn - NCC cạnh tranh nhau |
| Chất lượng & nhất quán | Dễ kiểm soát hơn | Khó đồng bộ chất lượng |
| Chi phí quản lý | Thấp | Cao hơn (quản lý nhiều NCC) |
| Phù hợp | Linh kiện đặc thù, quan hệ chiến lược | Nguyên liệu hàng hóa (commodity) |

**Quy tắc thực dụng**: tách đơn "chính - phụ" như 70/30 hoặc 60/25/15 — NCC chính giữ lợi thế quy mô, NCC phụ luôn "ấm máy" để thay thế được khi cần.

#### 2.2.3. Tổng chi phí sở hữu (Total Cost of Ownership - TCO) / Chi phí đưa về kho (Landed Cost)

**Tại sao?** Giá trên báo giá chỉ là phần nổi của tảng băng. Chi phí thật gồm vận chuyển, thuế, tồn kho (vốn bị chôn trong hàng đang đi đường), chất lượng kém, giao trễ... Ý tưởng TCO (do Gartner phổ biến cho CNTT thập niên 1980 và được ngành thu mua mở rộng) buộc người mua so sánh *chi phí đưa hàng về đến nơi sử dụng*, không chỉ giá mua.

$$\text{TCO} = P + F + D + H + Q + L$$

$P$: giá mua; $F$: vận chuyển/bảo hiểm; $D$: thuế, phí hải quan; $H$: chi phí vốn tồn kho (carrying cost); $Q$: chi phí chất lượng (lỗi, đổi trả); $L$: chi phí giao trễ (đặt gấp, dừng máy).

**Ví dụ: nhập khẩu hay mua trong nước?** (giả định minh họa) Một linh kiện: giá nhập 18 USD/cái (tỷ giá 25.500 VNĐ/USD); vận chuyển + bảo hiểm 8% giá; thuế nhập khẩu 5% trên giá CIF; lead time 45 ngày; chi phí vốn 15%/năm. Giá mua trong nước 520.000 VNĐ/cái, lead time 7 ngày.

- Nhập khẩu: $P = 18 \times 25.500 = 459.000$; $F = 8\% \times 459.000 = 36.720$; CIF $= 495.720$; $D = 5\% \times 495.720 = 24.786$; $H = 459.000 \times 15\% \times 45/365 \approx 8.488$.
  → TCO ≈ $459.000 + 36.720 + 24.786 + 8.488 = 528.994$ VNĐ/cái.
- Trong nước: $H = 520.000 \times 15\% \times 7/365 \approx 1.496$ → TCO ≈ $521.496$ VNĐ/cái.

**Kết luận**: giá niêm yết nhập khẩu rẻ hơn 61.000 VNĐ (11,7%) nhưng TCO lại **đắt hơn ≈ 7.500 VNĐ/cái** (chưa tính rủi ro tỷ giá, rủi ro chậm tàu). Đây là lý do SCM phải nhìn tổng chi phí.

### 2.3. Logistics & Phân phối (Logistics & Distribution)

**Logistics đầu vào (Inbound)**: vận chuyển nguyên vật liệu từ NCC đến nhà máy/kho. **Logistics đầu ra (Outbound)**: vận chuyển thành phẩm từ nhà máy đến khách hàng. **Logistics ngược (Reverse)**: hàng trả, bảo hành, tái chế.

#### 2.3.1. Các mô hình mạng lưới phân phối

**Tại sao nhiều mô hình?** Bài toán gốc là đánh đổi giữa *chi phí vận chuyển*, *chi phí tồn kho* và *tốc độ giao*. Không mô hình nào thắng tuyệt đối.

```
Mô hình 1: Phân phối trực tiếp (Direct Shipment)
NCC/Nhà máy ──────────────────────────▶ Khách hàng
(đơn giản; chi phí vận chuyển cao khi đơn hàng nhỏ lẻ)

Mô hình 2: Qua kho trung tâm (Distribution Center)
NCC/Nhà máy ──▶ Kho trung tâm (DC) ──▶ Khách hàng
(gộp đơn, tối ưu vận chuyển; tăng thời gian giao)

Mô hình 3: Cross-Docking
NCC A ──┐                    ┌──▶ Khách hàng vùng 1
NCC B ──┼──▶ Cross-Dock Hub──┼──▶ Khách hàng vùng 2
NCC C ──┘   (không lưu kho)  └──▶ Khách hàng vùng 3
(hàng đến và đi trong vài giờ, tồn kho gần như bằng 0)

Mô hình 4: Milk Run (thu gom tuần hoàn)
Xe tải ──▶ NCC A ──▶ NCC B ──▶ NCC C ──▶ Nhà máy
(một xe thu gom từ nhiều NCC theo tuyến cố định, tối ưu tải trọng)
```

**Ví dụ số tuyến — vì sao kho trung tâm giảm độ phức tạp**: có $n = 10$ nhà cung cấp và $m = 20$ khách hàng. Giao trực tiếp cần $n \times m = 10 \times 20 = 200$ tuyến; qua một DC chỉ cần $n + m = 10 + 20 = 30$ tuyến. Đổi lại, hàng phải qua thêm một điểm trung chuyển (thêm thời gian và chi phí xử lý).

#### 2.3.2. Lựa chọn phương thức vận tải

| Phương thức | Tốc độ | Chi phí | Phù hợp |
|---|---|---|---|
| Đường biển (Ocean) | Chậm nhất | Thấp nhất | Hàng khối lượng lớn, không gấp |
| Đường sắt (Rail) | Trung bình | Thấp | Hàng nặng, khoảng cách xa nội địa |
| Đường bộ (Truck) | Nhanh | Trung bình | Phân phối nội địa, linh hoạt |
| Đường hàng không (Air) | Nhanh nhất | Cao nhất | Hàng giá trị cao, gấp, dễ hỏng |
| Đường ống (Pipeline) | Liên tục | Thấp (đầu tư ban đầu cao) | Dầu khí, hóa chất lỏng |

### 2.4. Hoạch định nhu cầu & S&OP (Demand Planning & Sales and Operations Planning)

**Tại sao cần S&OP?** Trong nhiều doanh nghiệp, Kinh doanh nói "bán được 1.000", Sản xuất sản xuất theo công suất, Tài chính giữ ngân sách riêng — ba kế hoạch khác nhau cùng tồn tại, kết quả là vừa thiếu vừa thừa hàng. **S&OP** (do Oliver Wight phát triển từ thập niên 1980 trên nền MRP II) bắt buộc các bộ phận ngồi lại hàng tháng để đồng thuận **một con số duy nhất** cho kế hoạch cung-cầu, gắn với ngân sách.

**Chu trình S&OP 5 bước (theo tháng)**:

```
Tuần 1: Thu thập dữ liệu (Data Gathering)
   │  Doanh số thực tế, dự báo thị trường, đơn hàng tồn đọng
   ▼
Tuần 2: Hoạch định nhu cầu (Demand Planning Meeting)
   │  Marketing & Sales thống nhất dự báo nhu cầu
   ▼
Tuần 3: Hoạch định cung ứng (Supply Planning Meeting)
   │  Operations đánh giá năng lực đáp ứng, xác định gap
   ▼
Tuần 4: Họp tiền S&OP (Pre-S&OP Meeting)
   │  Giải quyết xung đột cung-cầu, đề xuất phương án
   ▼
Tuần 4: Họp S&OP điều hành (Executive S&OP Meeting)
      Ban lãnh đạo phê duyệt kế hoạch cuối cùng, gắn với ngân sách
```

**Mở rộng ra ngoài doanh nghiệp**:

| Cơ chế | Nội dung | Giải quyết nguyên nhân Bullwhip nào |
|---|---|---|
| **VMI (Vendor Managed Inventory)** | Nhà cung cấp quản lý tồn kho tại kho/cửa hàng khách theo mức tối thiểu-tối đa thỏa thuận | Xử lý tín hiệu nhu cầu, đặt hàng theo lô |
| **CPFR (Collaborative Planning, Forecasting and Replenishment)** | Hai bên cùng lập dự báo, kế hoạch khuyến mãi và bổ sung hàng, giải quyết chênh lệch dự báo | Cả 4 nguyên nhân, mạnh nhất với nguyên nhân 1 và 3 |

Về lịch sử: Walmart và Warner-Lambert thử nghiệm CPFR giữa thập niên 1990; Walmart - P&G nổi tiếng với các chương trình VMI/bổ sung liên tục. Đây là ví dụ để hiểu ý tưởng; chi tiết triển khai cụ thể ghi theo tài liệu gốc.

### 2.5. Rủi ro chuỗi cung ứng & Khả năng phục hồi (Supply Chain Risk & Resilience)

**Tại sao?** Chuỗi cung ứng toàn cầu tối ưu bằng JIT và đơn nguồn giúp giảm chi phí nhưng "mong manh" (fragile) — một mắt xích gãy là cả chuỗi dừng. Các cú sốc như COVID-19 (2020-2022), kẹt kênh đào Suez (2021) hay căng thẳng thương mại Mỹ-Trung đưa **khả năng phục hồi (Resilience)** thành mục tiêu ngang hàng với chi phí.

**Điểm số rủi ro**: chấm xác suất (P) và tác động (I) theo thang 1-5, điểm rủi ro $R = P \times I$ (tối đa 25). Rủi ro ≥ 15 cần kế hoạch ưu tiên; 8-14 cần giám sát và dự phòng; < 8 có thể chấp nhận. Lý do dùng tích: một rủi ro rất hiếm nhưng thảm khốc và một rủi ro thường xuyên nhưng nhẹ có thể có mức ưu tiên tương đương.

```
Mức độ tác động
   Cao  │  GIÁM SÁT (Monitor)       │  ƯU TIÊN CAO (High Priority)
        │  Xây kế hoạch dự phòng    │  Đa dạng hóa NCC, tồn kho đệm,
        │                           │  bảo hiểm, kế hoạch BCP
        │───────────────────────────┼────────────────────────────
   Thấp │  CHẤP NHẬN (Accept)       │  GIẢM THIỂU (Mitigate)
        │  Chi phí xử lý cao hơn    │  Kiểm soát định kỳ, hợp đồng
        │  thiệt hại                │  dự phòng
        └───────────────────────────┴────────────────────────────
             Thấp                       Cao
                  Xác suất xảy ra
```

**Chiến lược tăng khả năng phục hồi**:
- **Đa dạng hóa nguồn cung (Diversification)**: không phụ thuộc một quốc gia/NCC duy nhất.
- **"China+1" hoặc Near-shoring**: dịch chuyển một phần sản xuất về gần thị trường tiêu thụ hoặc sang nước thứ ba (Việt Nam hưởng lợi từ xu hướng này, nhưng cũng chịu rủi ro phụ thuộc nguyên liệu đầu vào nhập khẩu).
- **Tồn kho chiến lược (Strategic Buffer Stock)**: đánh đổi giữa chi phí tồn kho và rủi ro gián đoạn (chi tiết công thức tồn kho an toàn xem [04-inventory-management.md](./04-inventory-management.md)).
- **Digital Twin & Control Tower**: mô phỏng số và trung tâm điều phối thời gian thực để phát hiện sớm gián đoạn (mục 2.6).
- **Kế hoạch kinh doanh liên tục (BCP) và bảo hiểm**.

**Cách đánh đổi chi phí - rủi ro (công thức quyết định)**: một biện pháp phòng ngừa đáng làm khi

$$\text{Chi phí phòng ngừa hằng năm} \lesssim p \times L \times (1 - r)$$

$p$: xác suất sự cố mỗi năm; $L$: tổn thất một lần sự cố; $r$: phần tổn thất còn lại sau khi có biện pháp (residual). Với SME, nên cộng thêm "phần bù sống còn" (một sự cố lớn có thể làm công ty phá sản) vì tổn thất kỳ vọng chưa phản ánh rủi ro kiệt quệ dòng tiền. Ví dụ tính chi tiết ở Case 4 (xưởng gỗ).

### 2.6. Chuyển đổi số trong chuỗi cung ứng (Digital Supply Chain)

**Tại sao?** Quyết định chuỗi cung ứng chất lượng phụ thuộc vào *dữ liệu đúng, kịp thời*. Dữ liệu trễ → Bullwhip. Công nghệ số giảm độ trễ và tăng độ minh bạch (visibility).

| Công nghệ | Ứng dụng trong SCM | Ví dụ thực tế |
|---|---|---|
| IoT (Internet of Things) | Theo dõi vị trí, nhiệt độ, độ ẩm hàng hóa theo thời gian thực | Cảm biến nhiệt độ trong container hàng lạnh |
| Blockchain | Truy xuất nguồn gốc minh bạch, hợp đồng thông minh | Walmart truy xuất thực phẩm bằng IBM Food Trust |
| AI/Machine Learning | Dự báo nhu cầu, tối ưu tuyến vận tải | Amazon dự báo theo khu vực để đặt hàng trước vào kho |
| Digital Twin | Mô phỏng toàn chuỗi để kiểm thử kịch bản rủi ro | Các tập đoàn lớn (như Unilever) mô phỏng gián đoạn nguồn cung |
| Control Tower | Trung tâm điều phối, giám sát toàn chuỗi thời gian thực | DHL cung cấp dịch vụ control tower theo dõi lô hàng toàn cầu |
| Robotic Process Automation (RPA) | Tự động hóa xử lý đơn, đối chiếu hóa đơn | Tự động hóa 3-way matching (PO - Biên nhận - Hóa đơn) |

(Các ví dụ công ty ở bảng là minh họa xu hướng, chưa kiểm chứng chi tiết quy mô triển khai.)

**Lộ trình chuyển đổi số cho SME**:

```
Giai đoạn 1: Số hóa dữ liệu cơ bản
   │  Chuyển từ sổ sách giấy sang Excel/phần mềm quản lý đơn giản
   ▼
Giai đoạn 2: Kết nối dữ liệu nội bộ
   │  Tích hợp bán hàng - kho - mua hàng trên một nền tảng (ERP nhỏ)
   ▼
Giai đoạn 3: Kết nối với đối tác bên ngoài
   │  Chia sẻ tồn kho/đơn hàng với NCC chính qua API hoặc cổng thông tin
   ▼
Giai đoạn 4: Phân tích dự báo nâng cao
      Công cụ dự báo AI/ML đơn giản có sẵn trong các nền tảng SaaS
```

**Lưu ý cho SME**: không cần Control Tower hay Digital Twin ngay từ đầu. Ưu tiên số hóa dữ liệu nội bộ (Giai đoạn 1-2) — nền tảng bắt buộc trước khi nghĩ đến công nghệ nâng cao.

### 2.7. Chuỗi cung ứng bền vững (Sustainable Supply Chain & ESG)

**Tại sao?** Khách hàng lớn ở châu Âu, Mỹ ngày càng đưa ESG (Environmental, Social, Governance) vào điều kiện hợp đồng; doanh nghiệp Việt không đáp ứng sẽ mất đơn hàng xuất khẩu.

- **Môi trường (E)**: giảm phát thải carbon vận chuyển (tối ưu tuyến, chuyển sang đường sắt/đường biển khi có thể), bao bì tái chế.
- **Xã hội (S)**: điều kiện lao động công bằng tại NCC (audit nhà máy, tiêu chuẩn SA8000, BSCI).
- **Quản trị (G)**: minh bạch truy xuất nguồn gốc, tuân thủ quy định chống lao động cưỡng bức (ví dụ UFLPA của Mỹ).

Nhiều nhà bán lẻ/thương hiệu quốc tế (như H&M, Nike, IKEA) đưa yêu cầu ESG vào hợp đồng với nhà cung cấp; doanh nghiệp xuất khẩu nên chủ động chuẩn bị. Trọng số ESG 10% trong Supplier Scorecard (mục 2.1.2) là cách đưa yêu cầu này vào đánh giá hằng ngày.

### 2.8. Các chỉ số đo lường hiệu quả chuỗi cung ứng (KPI) — công thức & ý nghĩa

**Tại sao cần KPI chuỗi?** "Không đo lường được thì không cải tiến được". Nhưng KPI sai (ví dụ chỉ đo chi phí mua) sẽ đẩy doanh nghiệp vào tối ưu cục bộ; do đó SCOR đề xuất bộ chỉ số cân bằng giữa độ tin cậy, tốc độ, chi phí và tài sản.

**(a) Đơn hàng hoàn hảo (Perfect Order Fulfillment)**: đơn chỉ "hoàn hảo" khi *đồng thời* giao đúng hạn, đủ số lượng, không hư hỏng, đủ chứng từ. Vì các điều kiện độc lập, tỷ lệ hoàn hảo là **tích** của các tỷ lệ thành phần:

$$\text{POF} = \text{OT} \times \text{IF} \times \text{ND} \times \text{CD}$$

(On-time, In-full, No-damage, Correct-documents). Ví dụ: $0{,}96 \times 0{,}98 \times 0{,}99 \times 0{,}99 = 0{,}922$ → chỉ **92,2%** đơn hoàn hảo dù từng chỉ số đều ≥ 96%. Lý do dùng tích: một khâu hỏng là cả đơn hỏng trong mắt khách hàng; mục tiêu ngành thường > 95%.

**(b) Chu kỳ chuyển hóa tiền (Cash-to-Cash Cycle Time - CCC)**: bao nhiêu ngày tiền của doanh nghiệp "nằm" trong chuỗi trước khi quay lại thành tiền mặt.

$$\text{CCC} = \text{DIO} + \text{DSO} - \text{DPO}$$

- $\text{DIO} = \dfrac{\text{Tồn kho bình quân}}{\text{Giá vốn hàng bán}} \times 365$ (Days Inventory Outstanding: số ngày giữ tồn kho)
- $\text{DSO} = \dfrac{\text{Phải thu bình quân}}{\text{Doanh thu}} \times 365$ (Days Sales Outstanding: số ngày thu tiền)
- $\text{DPO} = \dfrac{\text{Phải trả bình quân}}{\text{Giá vốn hàng bán}} \times 365$ (Days Payable Outstanding: số ngày trả tiền NCC)

Logic: ta *ứng tiền* khi giữ hàng và khi bán chịu, *được ứng tiền* khi trả chậm NCC; CCC càng ngắn, vốn lưu động càng nhẹ (chi tiết xem [06-working-capital-management](../3-financial-management/06-working-capital-management.md)).

**(c) Độ chính xác dự báo (Forecast Accuracy)**: dùng WAPE (Weighted Absolute Percentage Error) để tránh bị lệch bởi các mặt hàng nhỏ:

$$\text{WAPE} = \frac{\sum |A_t - F_t|}{\sum A_t}, \qquad \text{Accuracy} = 1 - \text{WAPE}$$

($A_t$: nhu cầu thực kỳ $t$; $F_t$: dự báo kỳ $t$). Mục tiêu tham khảo > 80%.

**(d) Chi phí chuỗi cung ứng (Supply Chain Cost % Revenue)** = tổng chi phí chuỗi (mua, kho, vận tải, tồn kho, quản trị) / doanh thu; khoảng 5-12% tùy ngành (số tham khảo).

**(e) OTD, Order Fulfillment Cycle Time**: OTD = số đơn giao đúng hạn / tổng số đơn; thời gian chu kỳ đơn hàng = từ khi khách đặt đến khi nhận hàng.

### 2.9. Ưu điểm & Nhược điểm của SCM tích hợp

| Khía cạnh | Ưu điểm | Nhược điểm |
|---|---|---|
| Chi phí | Giảm chi phí tồn kho, vận chuyển nhờ tối ưu toàn chuỗi | Đầu tư ban đầu cao cho hệ thống, công nghệ (ERP, WMS, TMS) |
| Tốc độ đáp ứng | Rút ngắn lead time nhờ phối hợp thông tin tốt hơn | Cần thời gian xây dựng lòng tin và quy trình với đối tác |
| Chất lượng | Kiểm soát chất lượng xuyên suốt chuỗi | Phụ thuộc năng lực và thiện chí đối tác bên ngoài |
| Rủi ro | Phát hiện sớm gián đoạn nhờ visibility toàn chuỗi | Rủi ro lan truyền nhanh hơn khi các mắt xích liên kết chặt (hiệu ứng domino) |
| Linh hoạt | Dễ mở rộng/thu hẹp theo nhu cầu thị trường | Thay đổi một mắt xích có thể đòi hỏi thay đổi đồng bộ toàn chuỗi |
| Cạnh tranh | Lợi thế bền vững, khó sao chép hơn sản phẩm đơn lẻ | Đòi hỏi năng lực quản trị phức tạp, nhân sự chuyên môn cao |

| Quy mô | Ưu điểm khi áp dụng SCM bài bản | Thách thức/Nhược điểm |
|---|---|---|
| Doanh nghiệp lớn | Sức mạnh đàm phán, đầu tư công nghệ (ERP, control tower), mạng lưới logistics rộng | Bộ máy cồng kềnh, phản ứng chậm với thay đổi cục bộ, chi phí phối hợp cao |
| SME | Linh hoạt, ra quyết định nhanh, ít tầng nấc phê duyệt | Sức mạnh đàm phán yếu, khó tiếp cận công nghệ đắt tiền, phụ thuộc ít NCC |

---

## III. Case Studies thực tế

> **Lưu ý về số liệu**: các mô tả định tính về Zara, Thế Giới Di Động (MWG), Boeing dựa trên thông tin công khai được trích dẫn rộng rãi; các con số định lượng trong phần "phân tích từng bước" của những case này là **giả định minh họa** do tác giả thiết kế để làm rõ logic, *không phải số liệu thật của doanh nghiệp*. Các case SME (xưởng gỗ, chuỗi cà phê, Tân Phát Foods) hoàn toàn là **giả định minh họa**.

### 1. Case Study Thành công: Zara (Inditex) - Chuỗi cung ứng thời trang nhanh linh hoạt

#### Bối cảnh

Zara (thuộc tập đoàn Inditex, Tây Ban Nha) cạnh tranh trong ngành thời trang, nơi sản phẩm thuộc nhóm "sáng tạo" theo Fisher (vòng đời ngắn, dự báo kém chính xác). Mô hình truyền thống của ngành: nhà thiết kế lên bộ sưu tập từ 6 tháng trước mùa, đặt sản xuất hàng loạt ở nơi có nhân công rẻ (chủ yếu châu Á), phải đoán trước mốt.

#### Chiến lược chuỗi cung ứng (theo thông tin công khai)

- Áp dụng mô hình **Agile/Responsive**: chấp nhận sản xuất một phần gần thị trường (châu Âu, Bắc Phi, Thổ Nhĩ Kỳ) với giá thành đơn vị cao hơn để đổi lấy tốc độ.
- Thời gian từ ý tưởng/thiết kế đến cửa hàng khoảng 2-3 tuần (ngành truyền thống khoảng vài tháng).
- Sản xuất lô nhỏ (small batch), giao hàng khoảng 2 lần/tuần cho từng cửa hàng, không dự trữ lớn.
- Dữ liệu bán hàng POS từ cửa hàng chảy về trung tâm thiết kế; nhân viên cửa hàng phản hồi khách thích/không thích → điều chỉnh sản xuất tuần kế tiếp.
- Mô hình **Leagile**: vải chưa nhuộm/chưa hoàn thiện được dự trữ sẵn (Lean, điểm phân tách), cắt - may - hoàn thiện theo tín hiệu thị trường (Agile).

Tỷ lệ hàng phải giảm giá (markdown) của Zara thường được trích dẫn khoảng 15-20% so với 30-40% trung bình ngành (số liệu trích dẫn rộng rãi trong các case học thuật, *chưa kiểm chứng độc lập*).

#### Phân tích từng bước: vì sao chấp nhận giá thành cao hơn vẫn lãi hơn? (giả định minh họa)

**Giả định** (mỗi 1.000 sản phẩm sản xuất, giá bán đủ giá 100 đơn vị tiền tệ quy ước, giảm giá 40% còn 60, hàng tồn cuối mùa thanh lý còn 20):

| Thông số | Chuỗi truyền thống (Efficient, châu Á) | Chuỗi Zara (Agile, gần thị trường) |
|---|---|---|
| Giá thành/sản phẩm | 40 | 50 (cao hơn 25%) |
| Bán đủ giá | 600 sp | 850 sp |
| Bán giảm giá (60) | 300 sp | 150 sp |
| Thanh lý cuối mùa (20) | 100 sp | 0 sp |

**Bước 1 - Doanh thu**:
- Truyền thống: $600 \times 100 + 300 \times 60 + 100 \times 20 = 60.000 + 18.000 + 2.000 = 80.000$
- Zara: $850 \times 100 + 150 \times 60 + 0 = 85.000 + 9.000 = 94.000$

**Bước 2 - Giá vốn**: truyền thống $1.000 \times 40 = 40.000$; Zara $1.000 \times 50 = 50.000$.

**Bước 3 - Lợi nhuận gộp**: truyền thống $80.000 - 40.000 = 40.000$ (biên 50,0%); Zara $94.000 - 50.000 = 44.000$ (biên 46,8%).

**Bước 4 - Ngưỡng hòa vốn của chiến lược "chấp nhận giá thành cao"**: Zara còn lợi hơn khi $94.000 - 1.000c \ge 40.000 \Rightarrow c \le 54$, nghĩa là Zara có thể trả **giá thành cao hơn tới 35%** ($54/40 - 1$) so với đối thủ mà vẫn lãi tuyệt đối bằng nhau.

#### Ý nghĩa kinh doanh

Biên lợi nhuận *phần trăm* của Zara thấp hơn (46,8% so với 50,0%) nhưng **lợi nhuận tuyệt đối trên mỗi 1.000 sản phẩm cao hơn 10%** (44.000 so với 40.000). Lý do: với sản phẩm sáng tạo, chi phí thật nằm ở *giảm giá và hàng ế*, không nằm ở giá thành đơn vị. Tốc độ phản hồi biến "dự báo" thành "quan sát nhu cầu thật" nên tỷ lệ bán đủ giá tăng từ 60% lên 85%.

#### Bài học

1. Chọn chuỗi cung ứng theo **tính chất sản phẩm** (mô hình Fisher), không theo giá thành thấp nhất.
2. Đầu tư vào **thông tin** (POS, phản hồi cửa hàng) và **linh hoạt sản xuất** (lô nhỏ, gần thị trường) là tài sản cạnh tranh khó sao chép.
3. Khi áp dụng, hãy tính **ngưỡng hòa vốn** của khoản chi phí chấp nhận thêm (như bước 4) trước khi quyết định.

### 2. Case Study Việt Nam lớn: Thế Giới Di Động (MWG) - Chuỗi cung ứng bán lẻ đa kênh và bài học Bách Hóa Xanh

#### Bối cảnh

MWG vận hành hàng nghìn cửa hàng (Thế Giới Di Động, Điện Máy Xanh, Bách Hóa Xanh - BHX) trên toàn quốc. Hai nhóm hàng có đặc tính chuỗi cung ứng rất khác nhau: điện thoại/điện máy (giá trị cao, bền, dễ lưu kho) và thực phẩm tươi sống (giá trị thấp, hư hỏng nhanh, cần chuỗi lạnh).

#### Giải pháp triển khai (theo thông tin công khai, mô tả định tính)

- Hệ thống kho vận tập trung theo vùng, kết hợp cross-docking để rút ngắn thời gian lưu kho.
- Đầu tư hệ thống ERP/WMS tích hợp dữ liệu bán hàng real-time từ POS đến trung tâm điều phối.
- Dự báo nhu cầu theo từng cửa hàng dựa trên lịch sử bán, mùa vụ, sự kiện khuyến mãi.
- Với BHX: xây chuỗi lạnh (cold chain), tăng tần suất giao hàng (hàng ngày), mua trực tiếp từ nhà cung cấp nông sản để giảm trung gian.

Giai đoạn đầu mở rộng BHX, công ty gặp thách thức lớn về hao hụt hàng tươi sống do chuỗi lạnh chưa hoàn thiện và phải tái cấu trúc mạng lưới cửa hàng, kho và nhà cung cấp (số liệu chi tiết xem báo cáo công ty; không trích lại ở đây).

#### Phân tích từng bước: hao hụt hàng tươi tác động thế nào lên lợi nhuận? (giả định minh họa)

**Giả định** (mỗi 1.000 kg rau nhập về một cửa hàng, giá bán lẻ 28.000 VNĐ/kg):

| Thông số | Chuỗi cũ (qua trung gian, giao 2 ngày/lần) | Chuỗi mới (mua trực tiếp, chuỗi lạnh, giao hằng ngày) |
|---|---|---|
| Giá mua | 22.000 VNĐ/kg (đã gồm phần trung gian) | 20.000 VNĐ/kg |
| Chi phí chuỗi lạnh + vận chuyển thêm | 0 | 1.500 VNĐ/kg |
| Hao hụt (héo, dập, hết hạn) | 12% | 5% |

**Bước 1 - Lượng bán được**: cũ $1.000 \times (1 - 12\%) = 880$ kg; mới $1.000 \times (1 - 5\%) = 950$ kg.

**Bước 2 - Doanh thu**: cũ $880 \times 28.000 = 24.640.000$ VNĐ; mới $950 \times 28.000 = 26.600.000$ VNĐ.

**Bước 3 - Chi phí nhập**: cũ $1.000 \times 22.000 = 22.000.000$; mới $1.000 \times (20.000 + 1.500) = 21.500.000$.

**Bước 4 - Lợi nhuận gộp**: cũ $24.640.000 - 22.000.000 = 2.640.000$ VNĐ (biên 10,7%); mới $26.600.000 - 21.500.000 = 5.100.000$ VNĐ (biên 19,2%).

**Bước 5 - Ngưỡng hao hụt hòa vốn của chuỗi mới**: lợi nhuận gộp bằng 0 khi doanh thu = chi phí, tức $(1-s) \times 28.000 \times 1.000 = 21.500.000 \Rightarrow s = 1 - 21.500/28.000 \approx 23,2\%$. Chuỗi mới "an toàn" khi hao hụt dưới ~23% — nhưng thực tế ngưỡng để *có lãi sau chi phí cửa hàng, nhân sự* thấp hơn rất nhiều.

#### Ý nghĩa kinh doanh

Cắt hao hụt từ 12% xuống 5% và loại một tầng trung gian gần như **nhân đôi** lợi nhuận gộp trên mỗi 1.000 kg (2,64 triệu → 5,1 triệu). Với hàng tươi, **hao hụt (thuộc chi phí chất lượng/tồn kho) là biến số quyết định lợi nhuận**, không chỉ giá nhập. Cũng vì vậy, mô hình hiệu quả (Efficient) kiểu điện máy không áp dụng nguyên xi cho hàng tươi.

#### Bài học

1. Đầu tư **dữ liệu và hạ tầng** (ERP, POS, dự báo) là nền tảng của SCM bán lẻ quy mô lớn.
2. Mỗi ngành hàng cần một thiết kế chuỗi cung ứng riêng (hàng bền khác hàng tươi).
3. Rút ngắn chuỗi (bớt trung gian) giúp kiểm soát chất lượng và chi phí, nhưng đòi hỏi doanh nghiệp tự gánh năng lực logistics, chuỗi lạnh và quản lý nhà cung cấp nông sản.

### 3. Case Study Thất bại: Boeing 787 Dreamliner - Rủi ro của việc outsource quá mức

#### Bối cảnh

Boeing thiết kế 787 Dreamliner với chiến lược outsource sâu: giao thiết kế và sản xuất phần lớn các cụm cấu kiện chính (cánh, thân, hệ thống) cho một mạng lưới hơn 50 nhà cung cấp cấp 1 trên toàn cầu, để chia sẻ vốn đầu tư và rủi ro, rút ngắn thời gian phát triển. Tỷ trọng giá trị máy bay do bên ngoài thực hiện thường được trích dẫn rất cao (hơn một nửa, có nguồn nói khoảng 70%) — con số ước tính chưa kiểm chứng.

#### Vấn đề phát sinh (theo thông tin công khai)

- Thiếu phối hợp, giám sát giữa Boeing, nhà cung cấp cấp 1 và cấp 2; một số nhà cung cấp gặp khó khăn về tài chính, kỹ thuật; thiếu hụt chi tiết nhỏ như bu-lông ốc vít cũng làm kẹt dây chuyền lắp ráp.
- Nhiều cụm cấu kiện đến nhà máy lắp ráp cuối chưa hoàn thiện, phải làm lại tại chỗ ("travelled work"), mất thời gian hơn dự kiến.
- Dự án chuyển giao chuyến bay đầu tiên khoảng 3 năm sau kế hoạch ban đầu (giao máy đầu tiên năm 2011 so với kế hoạch 2008), chi phí phát triển đội lên nhiều tỷ USD.
- Năm 2013, sự cố pin lithium-ion khiến toàn bộ đội bay 787 phải tạm dừng; nguyên nhân kỹ thuật và quy trách nhiệm trong mạng lưới nhà cung cấp rất phức tạp.

#### Phân tích từng bước (có tính minh họa)

**Bước 1 - Số giao diện cần quản lý tăng theo bình phương số nhà cung cấp**. Nếu các nhà cung cấp lớn đều phải ghép nối kỹ thuật với nhau, số cặp giao diện tiềm năng là $\frac{n(n-1)}{2}$:

- Với $n = 10$ nhà cung cấp: $\frac{10 \times 9}{2} = 45$ cặp.
- Với $n = 50$ nhà cung cấp: $\frac{50 \times 49}{2} = 1.225$ cặp (gấp ≈ 27 lần).

Thực tế không phải cặp nào cũng cần ghép nối trực tiếp, nhưng ví dụ cho thấy **độ phức tạp phối hợp tăng nhanh hơn rất nhiều so với số nhà cung cấp**. Lợi ích chia sẻ vốn bị bào mòn bởi chi phí phối hợp.

**Bước 2 - Phân tích 5 Whys (giả thuyết)**:
1. Vì sao dự án trễ? → Cụm cấu kiện đến muộn, chưa hoàn chỉnh.
2. Vì sao cấu kiện không đạt? → Nhà cung cấp thiếu năng lực/thiết kế chưa đồng bộ.
3. Vì sao Boeing không phát hiện sớm? → Thiếu kênh giám sát và dữ liệu thời gian thực xuyên mạng lưới.
4. Vì sao thiếu giám sát? → Mô hình giao cả thiết kế cho nhà cung cấp, Boeing mất năng lực kỹ thuật nội bộ để đánh giá.
5. Vì sao chọn mô hình này? → Mục tiêu tối ưu vốn/chi phí *cục bộ* của Boeing, đánh giá thấp rủi ro tích hợp.

**Bước 3 - Xếp theo ma trận Kraljic**: cấu kiện cốt lõi của máy bay là hàng thuộc nhóm **Chiến lược** (giá trị cao, rủi ro cao). Khuyến nghị cho nhóm này là hợp tác sâu, chia sẻ thông tin, giữ năng lực kỹ thuật nội bộ — ngược lại với việc "giao trọn gói rồi chờ giao hàng".

#### Ý nghĩa kinh doanh

Outsource giúp giảm vốn đầu tư nhưng *không* chuyển được rủi ro cuối cùng: khách hàng vẫn đòi Boeing giao máy, Boeing chịu tổn hại thương hiệu, phạt hợp đồng và chi phí khắc phục.

#### Bài học

1. Không outsource cấu phần cốt lõi mà không giữ **năng lực giám sát và tích hợp hệ thống**.
2. Dùng **scorecard và kiểm tra định kỳ** cho nhà cung cấp chiến lược; chia sẻ dữ liệu thời gian thực.
3. Tính **tổng chi phí phối hợp** chứ không chỉ chi phí sản xuất khi quyết định outsource (make-or-buy).

### 4. Case Study SME Việt Nam: Xưởng đồ gỗ nội thất xuất khẩu tại Bình Dương (đa dạng hóa nhà cung cấp) *(giả định minh họa)*

#### Bối cảnh

Công ty TNHH Gỗ Nam Phát (tên giả định), 80 công nhân, sản xuất đồ gỗ nội thất xuất khẩu. Doanh thu 3.000 triệu VNĐ/tháng; tiêu thụ 120 m³ gỗ xẻ sấy mỗi tháng với giá 12 triệu VNĐ/m³; biên đóng góp (contribution margin) 38%. **Toàn bộ gỗ nguyên liệu do một nhà cung cấp duy nhất cung cấp.** Khi nhà cung cấp bị cháy kho và hạn chế khai thác, xưởng ngừng sản xuất 3 tuần; một số đơn hàng xuất khẩu có điều khoản phạt trễ hạn.

#### Bước 1 - Phân loại danh mục mua hàng theo Kraljic

Chấm điểm 1-5 (ngưỡng "Cao" ≥ 3,5): Tác động lợi nhuận (dựa trên % chi phí), Rủi ro cung ứng (số NCC thay thế, thời gian chuyển đổi).

| Mặt hàng | % chi phí NVL | Tác động LN | Rủi ro | Nhóm Kraljic | Chiến lược |
|---|---|---|---|---|---|
| Gỗ xẻ sấy | ~48% doanh thu | 5 | 4 | **Chiến lược** | NCC chính + 2 NCC phụ, hợp đồng khung, chia sẻ dự báo |
| Ván MDF/ván ép | Thấp-trung bình | 4 | 2 | Đòn bẩy | Đấu thầu định kỳ, đa nguồn |
| Vận tải container xuất khẩu | Trung bình | 4 | 3 | Đòn bẩy | So sánh báo giá hãng tàu/3PL theo quý |
| Sơn PU/dầu bóng | Thấp | 3 | 2 | Không quan trọng | Đặt theo định mức, gộp đơn |
| Bao bì carton, pallet gỗ | Thấp | 2 | 1 | Không quan trọng | Chuẩn hóa quy cách, P-card |
| Phụ kiện (bản lề, ray giảm chấn) nhập khẩu | Thấp | 2 | 4 | Nút thắt | Tồn kho an toàn 8-10 tuần, tìm NCC thay thế |
| Keo dán chuyên dụng nhập khẩu | Thấp | 2 | 4,5 | Nút thắt | Hợp đồng bảo đảm sản lượng, tồn kho đệm |

*Ghi chú*: bản gốc của tài liệu xếp "gỗ nguyên liệu" vào nhóm Nút thắt; khi chấm điểm theo % chi phí thì gỗ chiếm tỷ trọng lớn nên thuộc nhóm **Chiến lược** — nhóm đòi hỏi cả hợp tác sâu lẫn đa dạng hóa. Các phụ kiện giá trị thấp nhưng thiếu là dừng sản xuất mới là nhóm Nút thắt đúng nghĩa.

#### Bước 2 - Định lượng thiệt hại của một lần gián đoạn ($L$)

- Doanh thu 3 tuần bị ảnh hưởng: $3.000 \times \frac{3}{4} = 2.250$ triệu VNĐ.
- Giả định 70% doanh thu này mất hẳn (khách chuyển sang nơi khác): $2.250 \times 70\% = 1.575$ triệu; lợi nhuận đóng góp mất đi: $1.575 \times 38\% = 598{,}5$ triệu.
- Phạt trễ hạn: đơn xuất khẩu bị chậm giá trị 1.500 triệu × mức phạt 8% = 120 triệu.
- Mất một khách hàng xuất khẩu nhỏ, lợi nhuận gộp ≈ 250 triệu/năm (tính 1 năm).
- **$L = 598{,}5 + 120 + 250 = 968{,}5$ triệu VNĐ** cho mỗi sự cố.

#### Bước 3 - Chi phí phương án giảm rủi ro

- Giá trị mua hằng năm: $120 \times 12 \times 12 = 17.280$ triệu VNĐ.
- **Đa nguồn**: chuyển 30% khối lượng sang 2 NCC phụ với giá cao hơn 4%: $17.280 \times 30\% \times 4\% = 207{,}36$ triệu/năm (tương đương tăng chi phí nguyên liệu bình quân $30\% \times 4\% = 1{,}2\%$).
- **Tồn kho an toàn 4 tuần** = 120 m³ (bằng một tháng dùng) giá trị $120 \times 12 = 1.440$ triệu VNĐ; chi phí vốn 10%/năm = 144 triệu/năm.
- **Tổng chi phí phòng ngừa**: $207{,}36 + 144 = 351{,}36$ triệu VNĐ/năm.

#### Bước 4 - So sánh lợi ích - chi phí

Giả định xác suất sự cố nguồn gỗ là $p = 0{,}5$ lần/năm (chính sách khai thác, thời tiết, cháy kho...), phần tổn thất còn lại sau phòng ngừa $r = 15\%$:

- Tổn thất kỳ vọng khi đơn nguồn: $0{,}5 \times 968{,}5 = 484{,}25$ triệu/năm.
- Tổn thất tránh được: $0{,}5 \times 968{,}5 \times (1 - 0{,}15) = 411{,}61$ triệu/năm.
- **Lợi ích ròng**: $411{,}61 - 351{,}36 = +60{,}25$ triệu/năm.
- Điểm hòa vốn của xác suất: $p^* = \frac{351{,}36}{968{,}5 \times 0{,}85} \approx 0{,}427$ lần/năm — nếu sự cố ít hơn ≈ 1 lần/2,3 năm thì phương án chỉ còn là "mua bảo hiểm".

#### Bước 5 - Quyết định và triển khai

1. Giữ NCC cũ làm nguồn chính (70%), ký hợp đồng khung với 2 NCC phụ (mỗi nơi 15%), cam kết sản lượng tối thiểu.
2. Tăng tồn kho an toàn **dần** trong 6 tháng (từ 0 lên 4 tuần) để không "đóng băng" 1.440 triệu VNĐ vốn một lúc.
3. Bổ sung điều khoản bất khả kháng (force majeure) và ngưỡng phạt rõ ràng với khách xuất khẩu.
4. Kiểm tra OTD, chất lượng của NCC phụ bằng scorecard hằng quý.

#### Ý nghĩa kinh doanh & Bài học

Về kỳ vọng, phương án đa nguồn + tồn kho **chỉ lãi nhẹ (+60 triệu/năm)** — giá trị thật nằm ở chỗ nó **cắt đuôi rủi ro** (giảm tổn thất một sự cố từ 968,5 triệu xuống còn khoảng 145 triệu, tức $968{,}5 \times 15\%$). Với SME, một sự cố 968,5 triệu (xấp xỉ 85% lợi nhuận đóng góp của cả một tháng: $968{,}5 / (3.000 \times 38\%) = 0{,}85$) có thể đủ gây đứt gãy dòng tiền, vì vậy nên coi đây là khoản bảo hiểm sống còn. Các số liệu đều là giả định minh họa; hãy thay bằng số của doanh nghiệp mình để ra quyết định.

### 5. Case Study SME Việt Nam - dịch vụ: Chuỗi cà phê nhượng quyền miền Trung (tập trung hóa thu mua) *(giả định minh họa)*

#### Bối cảnh

Chuỗi "Cà phê Nắng Trung" (tên giả định) mở rộng từ 5 lên 25 cửa hàng tại miền Trung trong 18 tháng. Ban đầu mỗi cửa hàng tự đặt cà phê hạt, sữa, syrup từ các nhà cung cấp địa phương khác nhau → chất lượng không đồng nhất, giá mua cao vì mỗi cửa hàng mua lẻ, không có sức mạnh đàm phán tập trung. Với mô hình nhượng quyền, mỗi ly cà phê kém ở một cửa hàng làm tổn hại cả thương hiệu.

#### Giả định số liệu

- Chi phí nguyên liệu trung bình mỗi cửa hàng: 60 triệu VNĐ/tháng → toàn chuỗi $25 \times 60 = 1.500$ triệu VNĐ/tháng.
- Cơ cấu chi: cà phê hạt 40%, sữa 30%, syrup/bột 15%, ly-nắp-ống hút 15%.

#### Bước 1 - Mức giảm giá nhờ đàm phán tập trung

| Nhóm hàng | Tỷ trọng | Giảm giá đạt được | Đóng góp vào mức giảm chung |
|---|---|---|---|
| Cà phê hạt | 40% | 9% | $0{,}40 \times 9\% = 3{,}6\%$ |
| Sữa | 30% | 15% | $0{,}30 \times 15\% = 4{,}5\%$ |
| Syrup/bột | 15% | 14% | $0{,}15 \times 14\% = 2{,}1\%$ |
| Ly, nắp, ống hút | 15% | 12% | $0{,}15 \times 12\% = 1{,}8\%$ |
| **Tổng** | 100% | | **12,0%** |

→ Tiết kiệm gộp: $1.500 \times 12\% = 180$ triệu VNĐ/tháng (2.160 triệu/năm).

#### Bước 2 - Chi phí vận hành mô hình tập trung hóa

| Khoản | Triệu VNĐ/tháng | Tính chất |
|---|---|---|
| Thuê kho trung chuyển (regional hub) | 25 | Cố định |
| 2 nhân viên kho (12 triệu/người) | 24 | Cố định |
| 2 nhân viên thu mua trung tâm (15 triệu/người) | 30 | Cố định |
| Xe tải + nhiên liệu giao 2 lần/tuần cho 25 cửa hàng | 30 | Biến đổi (1,2 triệu/cửa hàng) |
| **Tổng** | **109** | Cố định 79 + biến đổi 30 |

**Tiết kiệm ròng**: $180 - 109 = 71$ triệu VNĐ/tháng (≈ 852 triệu/năm).

#### Bước 3 - Điểm hòa vốn: cần bao nhiêu cửa hàng thì nên tập trung hóa?

Tiết kiệm mỗi cửa hàng $= 60 \times 12\% = 7{,}2$ triệu/tháng; chi phí biến đổi mỗi cửa hàng $1{,}2$ triệu; đóng góp ròng mỗi cửa hàng $7{,}2 - 1{,}2 = 6{,}0$ triệu. Hòa vốn khi $6{,}0 \times N = 79$ triệu $\Rightarrow N = 13{,}2$, tức **từ cửa hàng thứ 14 trở đi** mô hình tập trung hóa mới có lãi. Với 5 cửa hàng, thuê kho + 4 nhân sự sẽ lỗ: $5 \times 6{,}0 - 79 = -49$ triệu/tháng.

#### Bước 4 - Chuẩn hóa chất lượng

Xây SOP công thức và quy cách nguyên liệu; một NCC cà phê hạt cho toàn chuỗi (đơn nguồn chiến lược), một NCC dự phòng cho sữa; kiểm tra lô hàng đầu vào tại kho; hạn mức tồn kho cửa hàng tối đa 5 ngày.

#### Ý nghĩa kinh doanh & Bài học

- Tập trung hóa thu mua giúp SME có "sức mạnh đàm phán" gần với doanh nghiệp lớn, đồng thời bảo vệ **tính nhất quán thương hiệu** — lợi ích khó định lượng nhưng quan trọng với nhượng quyền.
- Tập trung hóa có **chi phí cố định**: chỉ đáng khi đủ quy mô (≈ 14 cửa hàng theo giả định này). Doanh nghiệp nhỏ hơn có thể dùng 3PL hoặc liên kết mua chung.
- Rủi ro mới: phụ thuộc vào ít nhà cung cấp — cần chuẩn bị NCC dự phòng.

### 6. Case Study SME Việt Nam MỚI: Tân Phát Foods - Giảm hiệu ứng Bullwhip và chọn nhà cung cấp cho nhà phân phối thực phẩm đông lạnh *(giả định minh họa)*

#### Bối cảnh

Công ty TNHH Tân Phát Foods (tên và số liệu giả định) là nhà phân phối thực phẩm đông lạnh (chả giò, há cảo, cá viên) tại Cần Thơ, phục vụ khoảng 120 tiệm tạp hóa và siêu thị mini, mua từ 3 nhà máy. Triệu chứng: kho lạnh khi thì tràn hàng sắp hết hạn, khi thì hết hàng; thuê thêm xe giao gấp; nhà máy phàn nàn đơn hàng "lên xuống thất thường" dù khách bán đều. Chủ doanh nghiệp nghi ngờ **hiệu ứng Bullwhip**. Đơn vị đo: thùng (giá vốn 450.000 VNĐ/thùng).

#### Bước 1 - Thu thập dữ liệu 12 tuần

| Tuần | Nhu cầu thực (khách mua của tiệm - "sell-out") | Đơn của tiệm gửi Tân Phát | Đơn Tân Phát gửi nhà máy |
|---|---|---|---|
| 1 | 200 | 185 | 150 |
| 2 | 210 | 225 | 260 |
| 3 | 195 | 180 | 160 |
| 4 | 205 | 230 | 270 |
| 5 | 200 | 190 | 150 |
| 6 | 215 | 235 | 260 |
| 7 | 190 | 175 | 140 |
| 8 | 210 | 230 | 270 |
| 9 | 205 | 205 | 190 |
| 10 | 200 | 210 | 240 |
| 11 | 195 | 185 | 150 |
| 12 | 205 | 180 | 190 |
| **Tổng** | **2.430** | **2.430** | **2.430** |

Tổng ba cột bằng nhau (2.430 thùng): không có thất thoát hay tích lũy tồn kho dài hạn, nên chỉ có **độ dao động** là khác biệt.

#### Bước 2 - Tính trung bình, phương sai, độ lệch chuẩn

| Chỉ tiêu | Nhu cầu thực | Đơn của tiệm | Đơn gửi nhà máy |
|---|---|---|---|
| Trung bình (thùng/tuần) | 202,5 | 202,5 | 202,5 |
| Phương sai (Var) | 47,92 | 472,92 | 2.618,75 |
| Độ lệch chuẩn (σ) | 6,92 | 21,75 | 51,17 |
| Hệ số biến thiên CV = σ/TB | 3,4% | 10,7% | 25,3% |

**Cách tính mẫu (nhu cầu thực)**: $\text{Var} = \frac{1}{12}\sum (x_t - 202{,}5)^2 = 47{,}92$; $\sigma = \sqrt{47{,}92} = 6{,}92$.

#### Bước 3 - Tỷ số Bullwhip

- Tầng tiệm so với nhu cầu thực: $BW_1 = \frac{472{,}92}{47{,}92} \approx 9{,}87$ (phương sai bị khuếch đại ≈ 9,9 lần).
- Tầng nhà máy so với nhu cầu thực: $BW_2 = \frac{2.618{,}75}{47{,}92} \approx 54{,}65$ (≈ 54,7 lần).

**Diễn giải**: người tiêu dùng mua rất đều (CV chỉ 3,4%) nhưng nhà máy nhận đơn với CV 25,3%. Chính chuỗi đã tạo ra dao động chứ không phải thị trường.

#### Bước 4 - Chẩn đoán nguyên nhân (đối chiếu 4 nguyên nhân Lee-Padmanabhan-Whang)

| Dấu hiệu trong dữ liệu | Nguyên nhân | Giải thích |
|---|---|---|
| Đơn của tiệm tuần chẵn cao, tuần lẻ thấp (225, 230, 235 so với 185, 180, 190) | Đặt hàng theo lô | Nhóm tiệm quy ước đặt "cách tuần" để tiết kiệm phí giao hàng |
| Tân Phát gửi nhà máy 260-270 vào tuần chẵn, 140-160 tuần lẻ | Đặt hàng theo lô + xử lý tín hiệu | Nhà máy yêu cầu tối thiểu theo pallet; Tân Phát cộng thêm "phòng hờ" khi thấy đơn tiệm tăng |
| Nhà máy khuyến mãi giá vào tuần chẵn | Biến động giá | Tân Phát mua dồn khi có chiết khấu |
| Tin đồn thiếu cá nguyên liệu dịp lễ | Trò chơi phân bổ | Tiệm đặt dư để giữ hàng |

#### Bước 5 - Hành động khắc phục

1. **Chia sẻ dữ liệu sell-out hằng tuần**: 120 tiệm báo lượng bán qua Zalo/Google Sheet (đổi lại được hỗ trợ giao hàng cố định).
2. **Ngày đặt hàng cố định mỗi tuần** theo cụm tuyến (tránh "đặt cách tuần").
3. **Ngừng khuyến mãi theo đợt** ở khâu bán sỉ; chuyển sang giá ổn định (EDLP) + thưởng theo doanh số quý.
4. **Họp S&OP đơn giản hằng tháng** (kinh doanh, kho, mua hàng) để chốt một con số dự báo.
5. **Đàm phán lại MOQ** với nhà máy: đặt thường xuyên hơn, lô nhỏ hơn (từ 1 pallet/2 tuần xuống 1/2 pallet mỗi tuần).

#### Bước 6 - Kết quả sau 12 tuần áp dụng

| Chỉ tiêu | Trước | Sau |
|---|---|---|
| Phương sai nhu cầu thực | 47,92 | 25,14 |
| Phương sai đơn của tiệm / $BW_1$ | 472,92 / 9,87 | 56,64 / **2,25** |
| Phương sai đơn gửi nhà máy / $BW_2$ | 2.618,75 / 54,65 | 126,06 / **5,01** |
| σ đơn gửi nhà máy | 51,17 | 11,23 |

(Dữ liệu 12 tuần sau: nhu cầu 205, 198, 210, 202, 195, 208, 200, 212, 198, 204, 206, 200; đơn tiệm 203, 195, 214, 203, 191, 210, 198, 216, 196, 206, 208, 198; đơn nhà máy 200, 190, 218, 205, 185, 214, 196, 222, 192, 208, 212, 198.)

**Tác động tồn kho an toàn** (95% độ tin cậy, $z = 1{,}65$; lead time $L = 2$ tuần; theo công thức $SS = z \cdot \sigma \cdot \sqrt{L}$, xem [04-inventory-management.md](./04-inventory-management.md)): tồn kho đệm để bù dao động đơn của tiệm giảm từ $1{,}65 \times 21{,}75 \times \sqrt{2} \approx 50{,}7$ thùng xuống $1{,}65 \times 7{,}53 \times \sqrt{2} \approx 17{,}6$ thùng; đệm để bù dao động đơn gửi nhà máy giảm từ $1{,}65 \times 51{,}17 \times \sqrt{2} \approx 119{,}4$ thùng xuống $1{,}65 \times 11{,}23 \times \sqrt{2} \approx 26{,}2$ thùng.

**Hiệu quả tài chính** (giả định minh họa, mỗi 12 tuần):
- Hàng cận date phải hủy giảm từ 1,2% còn 0,4%: $2.430 \times 1{,}2\% = 29{,}16$ thùng → $2.438 \times 0{,}4\% = 9{,}75$ thùng; giá trị tiết kiệm $= (29{,}16 - 9{,}75) \times 450.000 \approx 8{,}7$ triệu VNĐ.
- Chuyến giao gấp giảm từ 5 xuống 1 chuyến, mỗi chuyến 1,8 triệu: tiết kiệm $4 \times 1{,}8 = 7{,}2$ triệu VNĐ.
- Tổng ≈ 15,9 triệu/12 tuần ≈ 69 triệu VNĐ/năm (nhân với $52/12$). Con số nhỏ so với quy mô vài tỷ, nhưng *chi phí cải tiến gần bằng 0* (Zalo, Google Sheet, một cuộc họp/tháng).

#### Bước 7 - Đánh giá và chọn nhà cung cấp (Supplier Scorecard + TCO)

Tân Phát mua từ 3 nhà máy. Số liệu 12 tuần:

| Nhà máy | Tỷ lệ lỗi | OTD | Giá (nghìn VNĐ/thùng) | Năng lực | ESG |
|---|---|---|---|---|---|
| A | 1,2% | 97% | 440 | Tốt | Trung bình |
| B | 0,4% | 94% | 465 | Rất tốt (chứng nhận HACCP/ISO 22000, xuất khẩu) | Tốt |
| C | 2,5% | 88% | 410 | Hạn chế (một dây chuyền) | Yếu |

Quy ước điểm 1-5: lỗi ≤ 0,5% → 5; 0,5-1,5% → 4; 1,5-3,0% → 3; OTD ≥ 96% → 5, 93-96% → 4, 85-93% → 3; giá ≤ 415 → 5, 416-445 → 3, > 460 → 2.

| Nhà máy | Chất lượng 30% | OTD 25% | Giá 20% | Năng lực 15% | ESG 10% | **Tổng điểm** |
|---|---|---|---|---|---|---|
| A | 4 | 5 | 3 | 4 | 3 | $1{,}20 + 1{,}25 + 0{,}60 + 0{,}60 + 0{,}30 = $ **3,95** |
| B | 5 | 4 | 2 | 5 | 5 | $1{,}50 + 1{,}00 + 0{,}40 + 0{,}75 + 0{,}50 = $ **4,15** |
| C | 3 | 3 | 5 | 2 | 2 | $0{,}90 + 0{,}75 + 1{,}00 + 0{,}30 + 0{,}20 = $ **3,15** |

**TCO mỗi thùng** (giả định: chi phí xử lý hàng lỗi = 2 × giá, chi phí giao trễ = 60 nghìn/thùng trễ):

$$\text{TCO} = \text{Giá} + \text{Tỷ lệ lỗi} \times \text{Giá} \times 2 + (1 - \text{OTD}) \times 60$$

- A: $440 + 0{,}012 \times 440 \times 2 + 0{,}03 \times 60 = 440 + 10{,}56 + 1{,}8 = 452{,}36$ nghìn.
- B: $465 + 0{,}004 \times 465 \times 2 + 0{,}06 \times 60 = 465 + 3{,}72 + 3{,}6 = 472{,}32$ nghìn.
- C: $410 + 0{,}025 \times 410 \times 2 + 0{,}12 \times 60 = 410 + 20{,}5 + 7{,}2 = 437{,}70$ nghìn.

**Nhận xét**: C vẫn rẻ nhất theo TCO nhưng điểm tổng chỉ 3,15 (mức "Duy trì/cần cải thiện") vì năng lực và ESG yếu, một dây chuyền nên rủi ro gián đoạn cao — không nên dựa chủ yếu vào C. B đắt nhất nhưng điểm cao nhất, phù hợp cho dòng sản phẩm cao cấp và khách hàng yêu cầu truy xuất/ESG.

**Quyết định phân bổ**: A 60% (nguồn chính, cân bằng giá-chất lượng), B 25% (dòng cao cấp), C 15% (đòn bẩy giá cho dòng bình dân, kèm kế hoạch cải thiện OTD; nếu OTD > 93% trong 2 quý sẽ tăng tỷ trọng). TCO bình quân gia quyền $= 0{,}60 \times 452{,}36 + 0{,}25 \times 472{,}32 + 0{,}15 \times 437{,}70 \approx 455{,}2$ nghìn VNĐ/thùng.

#### Ý nghĩa kinh doanh & Bài học

1. **Đo trước khi sửa**: tỷ số Bullwhip biến cảm giác "đơn hàng thất thường" thành con số (9,9 và 54,7 lần), chỉ ra *nguyên nhân nằm ở chính chuỗi*.
2. Giải pháp hiệu quả nhất **không tốn tiền công nghệ**: chia sẻ dữ liệu, cố định lịch đặt hàng, ổn định giá, S&OP đơn giản.
3. **Scorecard + TCO** giúp chọn nhà cung cấp đúng chiến lược thay vì chỉ nhìn giá thấp nhất; phân bổ tỷ trọng hợp lý vừa giữ giá vừa giảm rủi ro phụ thuộc một nhà máy.
4. Hiệu ứng Bullwhip *không biến mất hoàn toàn* ($BW > 1$ sau cải thiện): mục tiêu là **giảm tới mức chấp nhận được**, tiếp tục theo dõi hằng tháng.

### 7. Bảng tổng hợp bài học từ các case study

| Case study | Chiến lược/Công cụ áp dụng | Con số then chốt (minh họa) | Bài học chính |
|---|---|---|---|
| Zara | Agile + Leagile, mô hình Fisher | Lợi nhuận gộp +10% dù giá thành +25%; ngưỡng hòa vốn giá thành +35% | Chọn chuỗi cung ứng theo tính chất sản phẩm; chấp nhận chi phí cao hơn để đổi lấy tốc độ |
| Thế Giới Di Động (BHX) | Cross-docking, ERP tích hợp, chuỗi lạnh | Hao hụt 12% → 5% nhân đôi lợi nhuận gộp | Đầu tư dữ liệu/hạ tầng; mỗi ngành hàng cần thiết kế chuỗi riêng |
| Boeing 787 | Outsource quá mức (thất bại) | 10 NCC: 45 cặp giao diện; 50 NCC: 1.225 cặp | Cần giám sát và năng lực tích hợp khi outsource cấu phần cốt lõi |
| Xưởng gỗ Bình Dương | Kraljic + đa nguồn + tồn kho an toàn | Chi phí phòng ngừa 351 triệu/năm; lợi ích kỳ vọng 412 triệu | Không phụ thuộc một NCC; coi chi phí đa dạng hóa như bảo hiểm |
| Chuỗi cà phê miền Trung | Tập trung hóa thu mua + kho khu vực | Giảm 12% chi phí NVL; hòa vốn từ cửa hàng thứ 14 | Tập trung hóa có chi phí cố định, chỉ đáng khi đủ quy mô |
| Tân Phát Foods | Đo Bullwhip + S&OP + Scorecard/TCO | $BW$ nhà máy 54,7 → 5,0; điểm A/B/C = 3,95/4,15/3,15 | Đo trước khi sửa; chia sẻ dữ liệu là giải pháp rẻ và hiệu quả |

---

## IV. Ứng dụng cho SME

### 4.1. Quy trình 7 bước xây dựng/tái cấu trúc chuỗi cung ứng

**Tại sao theo thứ tự này?** Phải hiểu hiện trạng trước khi chọn chiến lược; chọn chiến lược theo sản phẩm (Fisher) trước khi chọn nhà cung cấp (Kraljic); thiết kế mạng lưới và hệ thống thông tin sau cùng, vì chúng phục vụ chiến lược chứ không dẫn dắt chiến lược.

```
Bước 1: Đánh giá hiện trạng (As-Is Assessment)
   │  Vẽ sơ đồ chuỗi cung ứng hiện tại, xác định các mắt xích, dòng chảy; đo Bullwhip, OTD, CCC
   ▼
Bước 2: Phân tích chiến lược sản phẩm (Fisher Model)
   │  Phân loại SP: Functional hay Innovative → chọn chiến lược Efficient/Agile
   ▼
Bước 3: Phân loại danh mục mua hàng (Kraljic Matrix)
   │  Xác định NCC chiến lược, đòn bẩy, nút thắt, không quan trọng
   ▼
Bước 4: Thiết kế mạng lưới (Network Design)
   │  Số lượng, vị trí kho/DC, phương thức vận tải, mô hình phân phối
   ▼
Bước 5: Xây dựng hệ thống thông tin (Information System)
   │  ERP, WMS, TMS; chia sẻ dữ liệu với đối tác (EDI/API/Zalo/Sheet)
   ▼
Bước 6: Triển khai thí điểm (Pilot Implementation)
   │  Chạy thử trên một khu vực/nhóm sản phẩm trước khi nhân rộng
   ▼
Bước 7: Đo lường & Cải tiến liên tục (Measure & Continuous Improvement)
      KPI theo dõi định kỳ, họp S&OP hàng tháng, điều chỉnh chiến lược
```

### 4.2. Vai trò của Giám đốc Chuỗi cung ứng (CSCO)

Trong doanh nghiệp lớn, Chief Supply Chain Officer (CSCO) chịu trách nhiệm xuyên suốt từ thu mua, sản xuất đến logistics, thường báo cáo trực tiếp CEO. Ở SME, vai trò này thường do Giám đốc Vận hành (COO) hoặc chủ doanh nghiệp kiêm nhiệm; cần được đào tạo tư duy hệ thống chuỗi cung ứng thay vì chỉ quản lý mua hàng đơn lẻ.

### 4.3. Mức độ áp dụng theo quy mô: SME vs Doanh nghiệp lớn

| Thành phần SCM | SME (< 200 lao động) | Doanh nghiệp lớn (> 500 lao động) |
|---|---|---|
| Hoạch định nhu cầu | Excel, kinh nghiệm chủ doanh nghiệp | Phần mềm dự báo AI/ML, S&OP chính thức hằng tháng |
| Quản lý NCC | 3-5 NCC chính, quan hệ cá nhân + scorecard đơn giản | Hàng trăm NCC, hệ thống SRM chính thức, scorecard định kỳ |
| Hệ thống thông tin | Excel/Google Sheets, phần mềm kế toán cơ bản | ERP (SAP, Oracle), WMS, TMS tích hợp |
| Mạng lưới kho | 1 kho trung tâm hoặc thuê ngoài (3PL) | Nhiều kho khu vực, trung tâm điều phối (Control Tower) |
| Nhân sự chuyên trách | Kiêm nhiệm (chủ DN, kế toán) | Phòng ban SCM riêng, CSCO chuyên trách |
| Công cụ dự báo | Kinh nghiệm + trung bình động đơn giản | Mô hình thống kê nâng cao, Machine Learning |

### 4.4. Chi phí đầu tư theo giai đoạn phát triển (ước tính tham khảo)

| Giai đoạn | Quy mô | Đầu tư SCM điển hình | Chi phí ước tính (VNĐ) |
|---|---|---|---|
| Khởi nghiệp | < 20 người | Excel, quan hệ trực tiếp với 1-2 NCC | 0 - 20 triệu (công cụ miễn phí) |
| Tăng trưởng | 20-100 người | Phần mềm quản lý kho cơ bản, thuê 3PL | 50 - 300 triệu/năm |
| Mở rộng | 100-500 người | ERP module nhỏ, WMS, đội mua hàng chuyên trách | 500 triệu - 3 tỷ (triển khai ban đầu) |
| Doanh nghiệp lớn | > 500 người | ERP toàn diện (SAP/Oracle), Control Tower, AI dự báo | 5 - 50+ tỷ (tùy mức độ tích hợp) |

### 4.5. Lộ trình khuyến nghị cho SME

1. Lập bản đồ chuỗi cung ứng hiện tại (dù đơn giản bằng sơ đồ tay) — 1 tuần.
2. Phân loại NCC theo ma trận Kraljic để ưu tiên nguồn lực quản trị — 2 tuần.
3. Số hóa dữ liệu tồn kho và đơn hàng bằng Excel có cấu trúc hoặc phần mềm giá rẻ (KiotViet, Sapo, Odoo) — 1-2 tháng.
4. Xây dựng ít nhất 1 NCC dự phòng cho nguyên liệu quan trọng nhất; chấm scorecard hằng quý — 3 tháng.
5. Đo hiệu ứng Bullwhip, chia sẻ dữ liệu bán hàng với đối tác, họp S&OP hằng tháng — 3-6 tháng.
6. Khi quy mô đủ lớn, đầu tư WMS/ERP phù hợp và tuyển nhân sự chuyên trách chuỗi cung ứng.

### 4.6. Các sai lầm thường gặp khi triển khai SCM

| Sai lầm | Hậu quả | Cách phòng tránh |
|---|---|---|
| Chỉ tối ưu chi phí từng mắt xích (local optimization) | Tổng chi phí toàn chuỗi tăng dù từng khâu "tối ưu" | Tính tổng chi phí sở hữu (TCO), không chỉ giá mua |
| Không chia sẻ dữ liệu nhu cầu với NCC | Hiệu ứng Bullwhip, tồn kho dư hoặc thiếu | Chia sẻ dữ liệu POS/sell-out, CPFR/VMI |
| Phụ thuộc một NCC duy nhất cho SP quan trọng | Rủi ro gián đoạn toàn bộ hoạt động | Đa dạng hóa theo Kraljic, tính chi phí - lợi ích (mục 2.5) |
| Chọn chiến lược Lean cho sản phẩm biến động cao | Thiếu hàng khi nhu cầu đột biến, mất doanh số | Dùng mô hình Fisher |
| Đầu tư công nghệ quá sớm, đắt tiền | Phần mềm không được dùng; dữ liệu không sạch | Số hóa dữ liệu nội bộ trước (mục 2.6) |
| Khuyến mãi dồn dập ở khâu bán sỉ | Mua dồn, Bullwhip | Giá ổn định + thưởng theo doanh số kỳ |
| Outsource cấu phần cốt lõi mà không giám sát | Mất kiểm soát chất lượng, trễ tiến độ (Boeing 787) | Giữ năng lực kỹ thuật, scorecard định kỳ |
| Chỉ dùng KPI chi phí | Tối ưu cục bộ, hy sinh dịch vụ | Dùng bộ KPI cân bằng (Perfect Order, CCC, OTD...) |

---

## V. Tools & Templates

### 5.1. Bảng công cụ phần mềm hỗ trợ SCM (chi phí ước tính, cần kiểm tra lại theo thời điểm)

| Công cụ | Chức năng chính | Chi phí ước tính | Phù hợp |
|---|---|---|---|
| Excel/Google Sheets | Theo dõi đơn hàng, tồn kho cơ bản, Scorecard, đo Bullwhip | Miễn phí | SME nhỏ |
| KiotViet, Sapo | Quản lý bán hàng, tồn kho, kho đơn giản | 3-10 triệu/năm | SME bán lẻ |
| Odoo, Bitrix24 | ERP module SCM cơ bản (mua hàng, kho, sản xuất) | 50-200 triệu/năm | SME vừa, mở rộng |
| SAP S/4HANA, Oracle SCM Cloud | ERP toàn diện, tích hợp toàn chuỗi | Hàng tỷ đến hàng chục tỷ/năm | Doanh nghiệp lớn |
| Blue Yonder, Kinaxis (Control Tower) | Hoạch định chuỗi cung ứng nâng cao, AI dự báo | Rất cao, theo hợp đồng riêng | Tập đoàn đa quốc gia |

### 5.2. Template: Bảng đánh giá nhà cung cấp (Supplier Scorecard)

```
TÊN NHÀ CUNG CẤP: _______________  NGÀNH HÀNG: _______________  KỲ ĐÁNH GIÁ: ________

| Tiêu chí             | Trọng số | Điểm (1-5) | Điểm x Trọng số |
|----------------------|----------|------------|-----------------|
| Chất lượng (PPM/lỗi) |   30%    |            |                 |
| Giao hàng đúng hạn   |   25%    |            |                 |
| Giá & Tổng chi phí   |   20%    |            |                 |
| Năng lực & công nghệ |   15%    |            |                 |
| ESG/Trách nhiệm XH   |   10%    |            |                 |
|----------------------|----------|------------|-----------------|
| TỔNG ĐIỂM            |   100%   |            |                 |

Phân loại: > 4,0 = Đối tác chiến lược | 3,0-4,0 = Duy trì | < 3,0 = Cần cải thiện/thay thế
```

**Công thức Google Sheets/Excel**: nếu trọng số ở `B2:B6`, điểm ở `C2:C6`, tổng điểm = `=SUMPRODUCT(B2:B6, C2:C6)`; xếp loại = `=IF(D8>4, "Chiến lược", IF(D8>=3, "Duy trì", "Cải thiện"))`.

### 5.3. Template: Chấm điểm ma trận Kraljic

| Mặt hàng | % chi phí | Tác động LN (1-5) | Số NCC thay thế | Rủi ro cung ứng (1-5) | Nhóm | Chiến lược | NCC dự phòng? |
|---|---|---|---|---|---|---|---|
| (điền) | | | | | =IF(AND(tác động≥3,5; rủi ro≥3,5),"Chiến lược", ...) | | |

### 5.4. Template: Bảng đo hiệu ứng Bullwhip (Excel/Google Sheets)

| Tuần | Nhu cầu thực (cột B) | Đơn của khách gửi bạn (cột C) | Đơn bạn gửi NCC (cột D) |
|---|---|---|---|
| 1..12 | ... | ... | ... |

- Phương sai: `=VAR.P(B2:B13)` (B), `=VAR.P(C2:C13)` (C), `=VAR.P(D2:D13)` (D).
- $BW_1$ = `=VAR.P(C2:C13)/VAR.P(B2:B13)`; $BW_2$ = `=VAR.P(D2:D13)/VAR.P(B2:B13)`.
- Cảnh báo: `=IF(BW>2,"Cần xử lý","Chấp nhận được")` (ngưỡng 2 là quy ước thực hành, không phải chuẩn).

### 5.5. Template: Bảng tính TCO (Landed Cost)

| Khoản | Nhà cung cấp 1 | Nhà cung cấp 2 | Công thức |
|---|---|---|---|
| Giá mua (P) | | | |
| Vận chuyển/bảo hiểm (F) | | | % giá hoặc phí cố định |
| Thuế/phí (D) | | | % × giá CIF |
| Chi phí vốn tồn kho (H) | | | Giá × lãi suất × ngày/365 |
| Chi phí chất lượng (Q) | | | Tỷ lệ lỗi × giá × hệ số xử lý |
| Chi phí giao trễ (L) | | | (1 - OTD) × phí xử lý/đơn vị |
| **TCO** | | | P + F + D + H + Q + L |

### 5.6. Sơ đồ quyết định lựa chọn chiến lược chuỗi cung ứng

```
                    Bắt đầu
                       │
          Nhu cầu SP có ổn định, dễ dự báo?
                 /            \
              Có               Không
               │                 │
      Biên lợi nhuận thấp?   Chiến lược AGILE
         /        \           (tồn kho đệm, NCC
       Có         Không        linh hoạt, lead
        │            │         time ngắn ưu tiên)
  EFFICIENT     Xem xét mô hình
  SUPPLY CHAIN   LEAGILE (Lean đến
  (JIT, chi phí   điểm phân tách,
   thấp nhất)     Agile sau đó)
```

---

## VI. Bài tập thực hành

### A. Bài tập tính toán (kèm đáp án)

**Bài 1 - Mô hình Fisher.** Một công ty có 5 sản phẩm: (a) gạo đóng gói, (b) giày thể thao mẫu mới theo mùa, (c) giấy vệ sinh, (d) phụ kiện điện thoại theo trend, (e) nước tương. Phân loại Functional/Innovative và đề xuất chiến lược.

*Đáp án*: (a), (c), (e): Functional (vòng đời dài, dự báo chính xác, biên thấp) → Efficient SC (JIT, chi phí thấp, đơn nguồn/đa nguồn theo giá). (b), (d): Innovative → Responsive SC (lô nhỏ, tồn đệm tại điểm phân tách, NCC linh hoạt, lead time ngắn). Gợi ý Leagile cho (b): dự trữ vải/đế giày (Lean), đóng giày theo tín hiệu thị trường (Agile).

**Bài 2 - Ma trận Kraljic.** Xưởng bánh có 8 mặt hàng với (Tác động LN, Rủi ro) theo thang 1-5: bột mì (5, 2), bơ nhập khẩu (4, 4), hương liệu đặc biệt nhập 1 NCC (2, 4,5), hộp giấy (2, 1), điện/gas (3, 2), vận chuyển lạnh (4, 3), băng keo (1, 1), nhãn mác in (2, 2). Phân loại (ngưỡng "Cao" ≥ 3,5).

*Đáp án*: Chiến lược: bơ nhập khẩu (4; 4). Đòn bẩy: bột mì (5; 2), vận chuyển lạnh (4; 3). Nút thắt: hương liệu đặc biệt (2; 4,5). Không quan trọng: hộp giấy, điện/gas (3; 2), băng keo, nhãn mác. Hành động: bơ → hợp đồng khung + NCC dự phòng; bột mì → đấu thầu định kỳ; hương liệu → tồn kho đệm + tìm NCC thay thế.

**Bài 3 - Supplier Scorecard.** Nhà cung cấp X: (4, 3, 5, 3, 2); Y: (5, 5, 2, 4, 4); Z: (2, 3, 4, 3, 3) theo thứ tự Chất lượng - OTD - Giá - Năng lực - ESG, trọng số 30/25/20/15/10. Tính điểm và xếp loại.

*Đáp án*: $S_X = 1{,}20 + 0{,}75 + 1{,}00 + 0{,}45 + 0{,}20 = 3{,}60$ (Duy trì); $S_Y = 1{,}50 + 1{,}25 + 0{,}40 + 0{,}60 + 0{,}40 = 4{,}15$ (Đối tác chiến lược); $S_Z = 0{,}60 + 0{,}75 + 0{,}80 + 0{,}45 + 0{,}30 = 2{,}90$ (Cần cải thiện/thay thế). Lưu ý Z điểm giá cao (4) nhưng chất lượng thấp (2) kéo tổng điểm xuống vì chất lượng có trọng số lớn nhất.

**Bài 4 - Hiệu ứng Bullwhip.** Nhu cầu thực 6 tuần: 100, 104, 98, 102, 100, 96. Đơn tiệm gửi nhà phân phối: 90, 115, 85, 112, 95, 103. Tính $BW$.

*Đáp án*: trung bình nhu cầu $= 100$; sai lệch $0, 4, -2, 2, 0, -4$ → bình phương $0, 16, 4, 4, 0, 16$ → $\text{Var}_d = 40/6 = 6{,}67$. Trung bình đơn $= 600/6 = 100$; sai lệch $-10, 15, -15, 12, -5, 3$ → bình phương $100, 225, 225, 144, 25, 9 = 728$ → $\text{Var}_r = 728/6 = 121{,}33$. $BW = 121{,}33/6{,}67 = 18{,}2$ — khuếch đại nghiêm trọng; nguyên nhân khả dĩ: đặt hàng luân phiên (lô) và khuyến mãi.

**Bài 5 - Cash-to-Cash.** Doanh thu 36.000 triệu, giá vốn 24.000 triệu, tồn kho bình quân 4.000 triệu, phải thu bình quân 3.000 triệu, phải trả bình quân 2.000 triệu. Tính CCC.

*Đáp án*: $\text{DIO} = \frac{4.000}{24.000} \times 365 = 60{,}8$ ngày; $\text{DSO} = \frac{3.000}{36.000} \times 365 = 30{,}4$ ngày; $\text{DPO} = \frac{2.000}{24.000} \times 365 = 30{,}4$ ngày; $\text{CCC} = 60{,}8 + 30{,}4 - 30{,}4 = 60{,}8$ ngày. Cách rút ngắn: giảm tồn kho (S&OP tốt hơn), thu tiền nhanh hơn, đàm phán thanh toán chậm hơn với NCC.

**Bài 6 - Perfect Order.** Giao đúng hạn 96%, đủ số lượng 98%, không hư hỏng 99%, chứng từ đúng 99%. Tính tỷ lệ đơn hoàn hảo.

*Đáp án*: $0{,}96 \times 0{,}98 \times 0{,}99 \times 0{,}99 = 0{,}922$ → 92,2% (thấp hơn mục tiêu 95%); cần cải thiện nhiều nhất ở chỉ số thấp nhất (đúng hạn, 96%).

**Bài 7 - TCO nhập khẩu vs nội địa.** Nhập khẩu 18 USD/cái (25.500 VNĐ/USD), vận chuyển 8%, thuế 5% trên CIF, lead time 45 ngày; nội địa 520.000 VNĐ/cái, lead time 7 ngày; chi phí vốn 15%/năm. So sánh TCO.

*Đáp án*: Nhập khẩu: $459.000 + 36.720 + 24.786 + 8.488 = 528.994$ VNĐ. Nội địa: $520.000 + 1.496 = 521.496$ VNĐ. Mua nội địa rẻ hơn ≈ 7.498 VNĐ/cái (≈ 1,4%) dù giá niêm yết nhập khẩu thấp hơn 11,7% (chưa tính rủi ro tỷ giá).

**Bài 8 - Độ chính xác dự báo (WAPE).** Nhu cầu thực 4 kỳ: 120, 150, 100, 130; dự báo: 100, 170, 90, 115. Tính độ chính xác.

*Đáp án*: sai số tuyệt đối $20 + 20 + 10 + 15 = 65$; tổng nhu cầu $500$; $\text{WAPE} = 65/500 = 13\%$; độ chính xác $= 87\%$ (> 80%, đạt).

**Bài 9 - Điểm hòa vốn tập trung hóa thu mua.** Chuỗi trà sữa: mỗi cửa hàng chi nguyên liệu 45 triệu/tháng; mua tập trung giảm 10%; chi phí cố định (kho + nhân sự) 50 triệu/tháng; chi phí giao hàng biến đổi 0,9 triệu/cửa hàng. Cần tối thiểu bao nhiêu cửa hàng?

*Đáp án*: tiết kiệm mỗi cửa hàng $= 45 \times 10\% = 4{,}5$ triệu; đóng góp ròng $= 4{,}5 - 0{,}9 = 3{,}6$ triệu; $N = 50/3{,}6 = 13{,}9 \Rightarrow$ **tối thiểu 14 cửa hàng**.

**Bài 10 - Quyết định phòng ngừa rủi ro.** Sự cố nhà cung cấp có xác suất 0,3 lần/năm, tổn thất 600 triệu/lần; phương án dự phòng giảm 80% tổn thất, chi phí 100 triệu/năm. Có nên làm?

*Đáp án*: lợi ích kỳ vọng $= 0{,}3 \times 600 \times 0{,}8 = 144$ triệu; chi phí $100$ triệu; lợi ích ròng $= +44$ triệu/năm → **nên làm** (và còn giảm rủi ro kiệt quệ dòng tiền).

### B. Bài tập phân tích & thực hành (hướng dẫn giải)

1. **Vẽ sơ đồ chuỗi cung ứng** của một sản phẩm bạn quen thuộc: xác định Tier-2, Tier-1, doanh nghiệp trung tâm, nhà phân phối, nhà bán lẻ, khách hàng; đánh dấu 3 dòng chảy. *Hướng dẫn*: hỏi "ai cung cấp cho ai", "thông tin chảy ngược từ đâu", "tiền trả vào lúc nào".
2. **Phân tích tình huống Bullwhip** bạn từng thấy: xác định nguyên nhân trong 4 nguyên nhân Lee và đề xuất giải pháp tương ứng (bảng ở mục 1.4).
3. **So sánh 3 mô hình phân phối** (trực tiếp, qua kho trung tâm, cross-docking) cho thực phẩm tươi, thời trang, điện tử. *Gợi ý*: thực phẩm tươi nghiêng về cross-docking/giao hằng ngày; thời trang nghiêng về DC + giao nhanh; điện tử giá trị cao có thể giao trực tiếp hoặc qua DC có bảo mật.
4. **Lập kế hoạch S&OP mẫu** cho một tháng của doanh nghiệp giả định theo 5 bước ở mục 2.4, ghi rõ ai tham dự, đầu vào, đầu ra mỗi cuộc họp.
5. **Nghiên cứu Boeing 787** bằng 5 Whys hoặc biểu đồ xương cá; đối chiếu với ma trận Kraljic và chi phí phối hợp theo công thức $n(n-1)/2$.
6. **Chiến lược đa dạng hóa** cho SME phụ thuộc 100% một NCC nguyên liệu nhập khẩu: tính $L$, $p$, $r$ theo mục 2.5, so sánh với chi phí phòng ngừa và quyết định.
7. **Tính chi phí đầu tư SCM** của doanh nghiệp bạn theo giai đoạn phát triển hiện tại, so sánh với bảng mục 4.4 và liệt kê khoản đầu tư ưu tiên.

---

## PHỤ LỤC: CHECKLIST QUẢN TRỊ CHUỖI CUNG ỨNG TỔNG HỢP

### P.1. Checklist triển khai

**Hiện trạng & chiến lược**
- □ Đã vẽ sơ đồ chuỗi cung ứng hiện tại (3 dòng chảy: vật chất, thông tin, tài chính).
- □ Đã phân loại từng nhóm sản phẩm theo mô hình Fisher (Functional/Innovative) và chọn chiến lược tương ứng.
- □ Đã xác định điểm phân tách (decoupling point) nếu dùng mô hình Leagile.

**Nhà cung cấp & thu mua**
- □ Đã phân tích chi tiêu (Spend Analysis) và xác định nhóm chiếm ~80% chi tiêu.
- □ Đã chấm điểm Kraljic cho các mặt hàng chính.
- □ Mỗi mặt hàng chiến lược/nút thắt có ít nhất 1 NCC dự phòng.
- □ Có Supplier Scorecard, cập nhật ít nhất hằng quý.
- □ So sánh nhà cung cấp theo TCO, không chỉ giá mua.
- □ Hợp đồng có điều khoản bất khả kháng, phạt trễ hạn, bảo đảm sản lượng.

**Hoạch định & thông tin**
- □ Có họp S&OP hằng tháng với một con số dự báo duy nhất.
- □ Đã đo Bullwhip (tỷ số phương sai) và xác định nguyên nhân chính.
- □ Chia sẻ dữ liệu bán hàng (sell-out/POS) với đối tác chính.
- □ Giá bán sỉ ổn định, hạn chế khuyến mãi dồn dập.

**Logistics & vận hành**
- □ Đã chọn mô hình phân phối phù hợp (trực tiếp/DC/cross-docking/milk run).
- □ Đã tính tuyến, tần suất giao, chi phí/đơn vị.
- □ Đã đo KPI cốt lõi (Perfect Order, OTD, CCC, Forecast Accuracy, Supply Chain Cost %).

**Rủi ro & bền vững**
- □ Có sổ tay rủi ro (risk register) chấm P×I và biện pháp giảm thiểu.
- □ Đã tính chi phí - lợi ích cho biện pháp phòng ngừa quan trọng nhất.
- □ Có BCP, bảo hiểm phù hợp, tồn kho an toàn cho hàng nút thắt.
- □ Đánh giá ESG của nhà cung cấp (nếu xuất khẩu).

**Số hóa**
- □ Dữ liệu tồn kho/đơn hàng được số hóa và đối chiếu định kỳ.
- □ Chỉ đầu tư công nghệ nâng cao (WMS, Control Tower...) sau khi dữ liệu nội bộ ổn định.

### P.2. Bảng thuật ngữ (Glossary)

| Thuật ngữ | Giải thích |
|---|---|
| SCOR | Supply Chain Operations Reference - mô hình tham chiếu vận hành chuỗi cung ứng |
| Bullwhip Effect | Hiệu ứng khuếch đại biến động nhu cầu ngược dòng chuỗi cung ứng |
| SRM | Supplier Relationship Management - quản trị quan hệ nhà cung cấp |
| Kraljic Matrix | Ma trận phân loại danh mục mua hàng theo tác động lợi nhuận và rủi ro cung ứng |
| S&OP | Sales and Operations Planning - hoạch định bán hàng và vận hành |
| CPFR | Collaborative Planning, Forecasting and Replenishment |
| VMI | Vendor Managed Inventory - nhà cung cấp quản lý tồn kho tại kho khách hàng |
| Cross-docking | Trung chuyển hàng không lưu kho dài hạn |
| 3PL | Third-Party Logistics - dịch vụ logistics thuê ngoài bên thứ ba |
| Leagile | Mô hình lai Lean + Agile với điểm phân tách |
| Decoupling Point | Điểm phân tách giữa phần sản xuất theo kế hoạch và theo đơn |
| Near-shoring | Dịch chuyển sản xuất về gần thị trường tiêu thụ |
| TCO / Landed Cost | Tổng chi phí sở hữu / chi phí đưa hàng về đến nơi sử dụng |
| MOQ | Minimum Order Quantity - số lượng đặt hàng tối thiểu |
| Tier-1/Tier-2 | Nhà cung cấp cấp 1 (trực tiếp)/cấp 2 (cung cấp cho NCC cấp 1) |
| BCP | Business Continuity Plan - kế hoạch kinh doanh liên tục |
| WAPE | Weighted Absolute Percentage Error - sai số phần trăm tuyệt đối có trọng số |

### P.3. Bảng công thức tổng hợp

| Chỉ số | Công thức | Ý nghĩa/Mục tiêu tham khảo |
|---|---|---|
| Bullwhip ratio | $BW = \dfrac{\text{Var}(\text{đơn hàng})}{\text{Var}(\text{nhu cầu cuối})}$ | 1 = không khuếch đại; càng lớn càng xấu |
| Cận dưới Bullwhip (Chen et al.) | $BW \ge 1 + \dfrac{2L}{p} + \dfrac{2L^2}{p^2}$ | Lead time $L$ dài làm khuếch đại mạnh |
| Điểm nhà cung cấp | $S = \sum w_i s_i$ | > 4,0 chiến lược; 3,0-4,0 duy trì; < 3,0 cải thiện |
| TCO | $P + F + D + H + Q + L$ | So sánh nhà cung cấp theo tổng chi phí |
| Perfect Order | $OT \times IF \times ND \times CD$ | > 95% |
| Cash-to-Cash | $DIO + DSO - DPO$ | Càng ngắn càng tốt |
| Forecast Accuracy | $1 - \dfrac{\sum \lvert A_t - F_t \rvert}{\sum A_t}$ | > 80% |
| Điểm rủi ro | $R = P \times I$ | ≥ 15 ưu tiên cao |
| Phòng ngừa đáng làm khi | $\text{Chi phí} \lesssim p \times L \times (1 - r)$ | Kèm phần bù sống còn cho SME |
| Hòa vốn tập trung hóa | $N^* = \dfrac{\text{Chi phí cố định}}{\text{Tiết kiệm/cửa hàng} - \text{Chi phí biến đổi/cửa hàng}}$ | Số điểm bán tối thiểu để đáng tập trung |
| Số tuyến mạng lưới | Trực tiếp $n \times m$; qua DC $n + m$ | Giảm độ phức tạp nhờ DC |
| Giao diện giữa $n$ NCC | $\dfrac{n(n-1)}{2}$ | Chi phí phối hợp tăng bình phương |
| Tồn kho an toàn | $SS = z \cdot \sigma \cdot \sqrt{L}$ | Xem file 04-inventory-management |
| Supply Chain Cost % | Chi phí chuỗi / Doanh thu | 5-12% tùy ngành |

### P.4. Bảng đo lường KPI chuỗi cung ứng

| KPI | Công thức | Mục tiêu tham khảo |
|---|---|---|
| Perfect Order Fulfillment | Đơn giao đúng, đủ, đúng hạn, không lỗi / Tổng đơn | > 95% |
| On-Time Delivery (OTD) | Số đơn giao đúng hạn / Tổng số đơn | > 95% |
| Order Fulfillment Cycle Time | Thời gian từ đặt hàng đến giao hàng | Càng ngắn càng tốt, theo ngành |
| Cash-to-Cash Cycle Time | Kỳ tồn kho + Kỳ phải thu - Kỳ phải trả | Càng ngắn càng tốt |
| Supply Chain Cost (% Revenue) | Tổng chi phí chuỗi cung ứng / Doanh thu | 5-12% tùy ngành |
| Forecast Accuracy | $1 - \text{WAPE}$ | > 80% |
| Bullwhip Ratio | Var(đơn đặt)/Var(nhu cầu) | Gần 1; < 2 là mục tiêu thực hành |

### P.5. Sổ tay rủi ro chuỗi cung ứng (Risk Register mẫu, thang P và I: 1-5)

| Rủi ro | Xác suất (P) | Tác động (I) | Điểm $R = P \times I$ | Biện pháp giảm thiểu |
|---|---|---|---|---|
| Gián đoạn nguồn cung nguyên liệu chính | 3 | 5 | 15 | Đa dạng hóa NCC, tồn kho an toàn |
| Biến động tỷ giá (nhập khẩu) | 4 | 3 | 12 | Hợp đồng kỳ hạn, đa dạng hóa đồng tiền thanh toán |
| Thiên tai, dịch bệnh | 2 | 5 | 10 | Kế hoạch kinh doanh liên tục (BCP), bảo hiểm |
| Lỗi hệ thống thông tin | 3 | 3 | 9 | Backup dữ liệu, quy trình thủ công dự phòng |
| Đình công/gián đoạn vận tải | 2 | 4 | 8 | Đa dạng phương thức vận tải, đối tác logistics dự phòng |

---

## TÀI LIỆU THAM KHẢO

### Sách tham khảo
1. Chopra, S. & Meindl, P. (2019). *Supply Chain Management: Strategy, Planning, and Operation*. Pearson.
2. Fisher, M. L. (1997). "What is the Right Supply Chain for Your Product?". *Harvard Business Review*.
3. Lee, H. L., Padmanabhan, V., & Whang, S. (1997). "The Bullwhip Effect in Supply Chains". *Sloan Management Review*.
4. Christopher, M. (2016). *Logistics & Supply Chain Management*. FT Publishing.
5. Simchi-Levi, D. (2008). *Designing and Managing the Supply Chain*. McGraw-Hill.
6. Kraljic, P. (1983). "Purchasing Must Become Supply Management". *Harvard Business Review*.
7. Forrester, J. W. (1961). *Industrial Dynamics*. MIT Press.
8. Chen, F., Drezner, Z., Ryan, J. K., & Simchi-Levi, D. (2000). "Quantifying the Bullwhip Effect in a Simple Supply Chain". *Management Science*.

### Liên kết nội bộ (Internal Cross-links)
- [01-process-design-analysis.md](./01-process-design-analysis.md) - Thiết kế quy trình nền tảng cho vận hành chuỗi cung ứng.
- [04-inventory-management.md](./04-inventory-management.md) - Quản trị tồn kho chi tiết (EOQ, JIT, Safety Stock).
- [05-capacity-planning.md](./05-capacity-planning.md) - Hoạch định năng lực gắn với hoạch định cung ứng.

### Nguồn học trực tuyến
- ASCM (Association for Supply Chain Management) - chứng chỉ CSCP, CPIM.
- Coursera: "Supply Chain Management" - Rutgers University.
- MIT CTL (Center for Transportation and Logistics) - tài liệu nghiên cứu mở.
