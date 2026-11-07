# Variance Analysis – Phân Tích Chênh Lệch

> **Mục tiêu**: Hiểu bản chất phân tích chênh lệch (Variance Analysis) – công cụ so sánh kết quả thực tế với kế hoạch/tiêu chuẩn; biết vì sao từng công thức được xây dựng như vậy, cách bóc tách chênh lệch thành các nguyên nhân có thể quy trách nhiệm, rút bài học từ doanh nghiệp lớn (Toyota, GM) và áp dụng được cho SME Việt Nam (xưởng may, quán cà phê, nhà hàng, shop online).

> **Lưu ý về số liệu**: Mọi số liệu trong các ví dụ và case SME ở file này là **giả định minh họa**, đã được kiểm tra nhất quán bằng phép tính. Số liệu gắn với công ty thật (Toyota, GM) chỉ mang tính minh họa nguyên lý, **cần đối chiếu nguồn** trước khi trích dẫn. Mọi quy định pháp lý/thuế/chuẩn mực kế toán nêu ở mức nguyên tắc – **cần xác nhận hiện hành**.

---

## I. KHÁI NIỆM & LÝ THUYẾT

### 1. Định nghĩa

**Variance Analysis (Phân tích chênh lệch)** là quá trình **so sánh kết quả thực tế (Actual) với tiêu chuẩn/kế hoạch (Standard/Budget)**, xác định nguyên nhân chênh lệch, quy trách nhiệm và đề xuất hành động khắc phục.

$$\text{Variance} = \text{Actual} - \text{Standard (Budget)}$$

- **Favorable Variance (F – Thuận lợi)**: thực tế TỐT HƠN kế hoạch (doanh thu cao hơn hoặc chi phí thấp hơn) → làm lợi nhuận tăng.
- **Unfavorable Variance (U – Bất lợi)**: thực tế XẤU HƠN kế hoạch (doanh thu thấp hơn hoặc chi phí cao hơn) → làm lợi nhuận giảm.

> **Quy ước dấu dùng trong file này**: với **chi phí**, Variance = Actual − Standard nên dấu **dương = U** (chi phí vượt), dấu **âm = F**. Với **doanh thu/lợi nhuận**, ta thường diễn giải ngược lại: dấu **âm = U**, dấu dương = F. Để tránh nhầm, luôn ghi kèm chữ (F) hoặc (U) sau mỗi con số.

> **"What gets measured gets managed. What gets compared gets improved."**

### 2. Tại sao cần Variance Analysis? Bối cảnh lịch sử

**Vấn đề kinh doanh cần giải quyết**: Cuối tháng, chủ doanh nghiệp thấy lợi nhuận thấp hơn kế hoạch 80 triệu. Câu hỏi "vì sao?" có hàng chục đáp án: bán ít? bán rẻ? vải đắt? thợ làm chậm? điện nước tăng? Nếu chỉ nhìn con số tổng, không ai biết **sửa ở đâu và giao cho ai sửa**. Variance Analysis **bóc con số tổng thành các mảnh nhỏ, mỗi mảnh gắn với một người/bộ phận kiểm soát được** (Mua hàng → giá; Sản xuất → định mức tiêu hao; Nhân sự → đơn giá giờ công; Kinh doanh → giá bán/số lượng).

**Nguồn gốc lịch sử** (cần đối chiếu nguồn cụ thể khi trích dẫn):
- **Đầu thế kỷ 20 – Scientific Management (Frederick W. Taylor)**: ý tưởng đo "thời gian chuẩn" cho từng thao tác để so sánh với thời gian thực tế, đặt nền cho định mức nhân công.
- **Khoảng 1910s–1920s – Standard Costing**: các kế toán/kỹ sư ở Mỹ (thường nhắc tên G. Charter Harrison với các công thức chênh lệch giá/lượng) hệ thống hóa chi phí tiêu chuẩn và việc phân tích chênh lệch; cùng thời kỳ DuPont và General Motors phát triển hệ thống kiểm soát tài chính theo kế hoạch – thực tế (cùng "dòng họ" với mô hình DuPont phân tách ROE).
- **Sau 1950s**: phương pháp được đưa vào giáo trình Kế toán quản trị (Managerial/Cost Accounting) và kỳ thi CMA; từ thập niên 1980–1990, các trường phái Lean/Toyota phê bình việc lạm dụng variance trong môi trường cải tiến liên tục (xem Case 1 và 2 ở mục III).

**Logic cốt lõi của công thức**: mọi chi phí đều là tích của **Giá × Lượng** (VD: tiền vải = giá/m × số m). Khi tích này lệch kế hoạch, ta tách theo "từng lần thay một biến": đổi **giá** trước (giữ lượng thực tế) để ra chênh lệch giá, rồi đổi **lượng** (giữ giá chuẩn) để ra chênh lệch lượng. Cách tách này đảm bảo **hai phần cộng lại đúng bằng tổng chênh lệch** – không thừa, không thiếu.

### 3. Vai trò trong Management Control (Vòng kiểm soát quản trị)

```
┌──────────────────────────────────────────────────┐
│         MANAGEMENT CONTROL CYCLE                 │
│                                                  │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    │
│  │ PLAN     │───►│ EXECUTE  │───►│ MEASURE  │    │
│  │ (Budget) │    │ (Do)     │    │ (Actual) │    │
│  └────┬─────┘    └──────────┘    └────┬─────┘    │
│       │                               │          │
│       │         ┌──────────┐          │          │
│       └────────►│ COMPARE  │◄─────────┘          │
│                 │ VARIANCE │                     │
│                 │ ANALYSIS │                     │
│                 └────┬─────┘                     │
│                      │                           │
│               ┌──────▼──────┐                    │
│               │ CORRECTIVE  │                    │
│               │ ACTION      │                    │
│               │ (Act)       │                    │
│               └─────────────┘                    │
└──────────────────────────────────────────────────┘
```

Variance Analysis là bước **"Check"** trong vòng PDCA (Plan–Do–Check–Act): không có bước này, ngân sách chỉ là tờ giấy; không có hành động khắc phục, phân tích chỉ là báo cáo "khám nghiệm tử thi".

### 4. Standard Costs (Chi phí tiêu chuẩn)

**Tại sao cần chi phí tiêu chuẩn?** Muốn biết thực tế "tốt hay xấu" phải có **thước đo**. Chi phí tiêu chuẩn là thước đo đó: chi phí **kỳ vọng** để làm ra 1 đơn vị sản phẩm/dịch vụ trong điều kiện hoạt động hợp lý. Nếu không có thước, mọi so sánh chỉ là so với tháng trước (mà tháng trước có thể đã kém).

| Loại Standard | Mức độ | Sử dụng khi | Rủi ro |
|---------------|--------|-------------|--------|
| **Ideal Standard** | Hoàn hảo, không lãng phí, không hỏng máy | Mục tiêu dài hạn (Toyota, Lean) | Luôn U → nhân viên nản nếu dùng để đánh giá |
| **Currently Attainable** | Khả thi, cho phép hao hụt hợp lý | Phổ biến nhất – lập ngân sách & đánh giá | Nếu đặt dễ quá → "luôn đạt" nhưng không cải tiến (xem GM) |
| **Basic Standard** | Cố định, không đổi nhiều năm | So sánh xu hướng dài hạn | Lạc hậu khi giá/công nghệ đổi |

**Ví dụ Standard Cost Card (Áo thun – số liệu giả định minh họa):**

```
┌──────────────────────────────────────────────┐
│  STANDARD COST CARD – Sản phẩm: Áo thun      │
│                                              │
│  Direct Materials (NVL trực tiếp):           │
│    Vải:    1.2m × 50,000/m      =  60,000    │
│    Phụ kiện (nút, nhãn)         =   5,000    │
│                                              │
│  Direct Labor (Nhân công trực tiếp):         │
│    Cắt:    0.5h × 40,000/h      =  20,000    │
│    May:    1.0h × 40,000/h      =  40,000    │
│    QC:     0.2h × 40,000/h      =   8,000    │
│    (Tổng 1.7 giờ/áo × 40,000)   =  68,000    │
│                                              │
│  Variable MOH (SX chung biến đổi):           │
│    1.7 DLH × 15,000/DLH         =  25,500    │
│                                              │
│  Fixed MOH (phân bổ):                        │
│    1.7 DLH × 20,000/DLH         =  34,000    │
│                                              │
│  ═══════════════════════════════════════     │
│  TOTAL STANDARD COST/unit       = 192,500    │
└──────────────────────────────────────────────┘
```

> Kiểm tra: 65,000 + 68,000 + 25,500 + 34,000 = **192,500**. Biến phí/đơn vị = 65,000 + 68,000 + 25,500 = 158,500; với giá bán 350,000 thì **Contribution Margin (CM – Số dư đảm phí) = 191,500/áo** và **lãi gộp theo absorption costing = 350,000 − 192,500 = 157,500/áo**. Hai con số này sẽ được dùng ở mục II.5 và II.6.

> *(File cũ ghi QC 35,000/h làm lệch đơn giá bình quân và FOH rate 19,608 làm lệch thẻ giá thành; đã thống nhất lại thành 40,000/h và 20,000/DLH.)*

### 5. Ngân sách tĩnh (Static Budget) vs Ngân sách linh hoạt (Flexible Budget) – nền tảng của mọi phân tích

**Vấn đề**: Ngân sách ban đầu lập cho 1.200 áo (static). Thực tế chỉ sản xuất 1.000 áo. Nếu so thẳng chi phí thực tế của 1.000 áo với ngân sách của 1.200 áo, mọi khoản biến phí đều "tiết kiệm" – kết luận hoàn toàn sai (so táo với cam).

**Giải pháp (Flexible Budget – Ngân sách linh hoạt)**: **tính lại ngân sách cho đúng mức hoạt động thực tế** (1.000 áo), rồi mới so với chi phí thực tế. Chênh lệch tách thành hai tầng:

```
 STATIC BUDGET        FLEXIBLE BUDGET         ACTUAL
 (1.200 áo)           (1.000 áo @ chuẩn)      (1.000 áo thực tế)
     │                      │                      │
     ├── SALES VOLUME ──────┤                      │
     │   VARIANCE           ├── PRICE/COST ────────┤
     │   (do bán ít/nhiều)  │   VARIANCE           │
     │                      │   (do giá, hao phí,  │
     │                      │    hiệu suất)        │
     └────────────── TOTAL VARIANCE ───────────────┘
```

- **Tầng 1 – Sales Volume Variance**: do bán nhiều/ít hơn kế hoạch – thường ngoài tầm kiểm soát của bộ phận sản xuất.
- **Tầng 2 – Flexible Budget Variance**: do giá/lượng/hiệu suất – chính là nhóm DM, DL, MOH, Sales Price ở mục II.

Ý nghĩa quản trị: nhà quản lý sản xuất chỉ nên bị đánh giá trên tầng 2, vì tầng 1 phụ thuộc vào thị trường/kinh doanh.

### 6. Bối cảnh kế toán Việt Nam (nguyên tắc – cần xác nhận hiện hành)

- Kế toán quản trị (Variance Analysis, Standard Costing) là **công cụ nội bộ**, không bắt buộc theo VAS; tuy nhiên báo cáo tài chính (BCTC) phải theo **VAS và Thông tư 200/2014/TT-BTC** (hoặc Thông tư 133/2016/TT-BTC cho DN nhỏ và vừa) – cần xác nhận hiện hành.
- **VAS 02 – Hàng tồn kho**: cho phép dùng giá thành **định mức/tiêu chuẩn** để ghi nhận hàng tồn kho nếu giá này xấp xỉ giá thực tế; chênh lệch cuối kỳ phải được điều chỉnh (phân bổ cho hàng tồn kho và giá vốn). Với mục đích BCTC, chi phí sản xuất chung cố định phân bổ theo công suất bình thường; phần vượt thì ghi nhận vào giá vốn trong kỳ – đây chính là cơ sở của khái niệm **Fixed Overhead Volume Variance** (xem II.4).
- Hệ thống tài khoản (621 – NVL trực tiếp, 622 – Nhân công trực tiếp, 627 – Chi phí SX chung, 154, 632) theo Thông tư 200 cung cấp dữ liệu "Actual" cho phân tích; "Standard" lấy từ định mức nội bộ.
- **IFRS** (IAS 2 – Inventories) cũng cho phép chi phí tiêu chuẩn với điều kiện phản ánh gần mức chi phí thực tế; lộ trình áp dụng IFRS tại Việt Nam cần xác nhận hiện hành.

---

## II. CHI TIẾT TỪNG THÀNH PHẦN

### 1. Sơ đồ tổng quan

```
                    TOTAL PROFIT VARIANCE
              (Actual Profit − Budgeted Profit)
                          │
            ┌─────────────┴─────────────┐
            │                           │
      REVENUE                         COST
      VARIANCE                      VARIANCE
            │                           │
     ┌──────┼──────┐          ┌─────────┼─────────┐
     │      │      │          │         │         │
   Sales  Sales  Sales        DM        DL       MOH
   Price  Volume  Mix      Variance  Variance  Variance
   Var    Var     Var         │         │         │
                           ┌──┴──┐   ┌──┴──┐   ┌──┴──┐
                         Price  Qty  Rate  Eff Spend/Eff/Vol
```

### 2. Direct Materials Variance (Chênh lệch NVL trực tiếp)

**Tại sao tách thành Price và Quantity?** Vì hai nguyên nhân thuộc về **hai người khác nhau**: giá mua là trách nhiệm của bộ phận Mua hàng (thương lượng, thời điểm mua, nhà cung cấp); lượng dùng là trách nhiệm của Sản xuất (phế phẩm, tay nghề, máy móc). Gộp chung sẽ không ai phải giải trình.

$$\text{Total DM Variance} = \text{Actual Cost} - \text{Standard Cost for Actual Output}$$

$$\text{DM Price Variance} = (\text{AP} - \text{SP}) \times \text{AQ}$$

$$\text{DM Quantity Variance} = (\text{AQ} - \text{SQ}) \times \text{SP}$$

Trong đó: AP = giá mua thực tế (Actual Price); SP = giá mua tiêu chuẩn (Standard Price); AQ = lượng sử dụng thực tế (Actual Quantity); SQ = lượng tiêu chuẩn **cho sản lượng thực tế** (Standard Quantity allowed).

> **Vì sao Price Variance nhân với AQ (lượng thực tế) còn Quantity Variance nhân với SP (giá chuẩn)?** Giá mua tác động lên **toàn bộ lượng đã mua/dùng thực tế** (kể cả phần hao phí), nên nhân AQ. Còn chênh lệch lượng được định giá bằng **giá chuẩn** để loại trừ ảnh hưởng của giá – nhờ đó lượng dùng thừa không bị "ô nhiễm" bởi biến động giá và trách nhiệm của Sản xuất được đo công bằng. Tổng hai phần = (AP×AQ) − (SP×SQ) đúng bằng tổng chênh lệch.

**Ví dụ chi tiết (1.000 áo thun trong tháng):**

| | Tiêu chuẩn (Standard) | Thực tế (Actual) |
|---|----------------------|-----------------|
| Lượng vải/áo | 1,2 m | 1,35 m (tổng AQ = 1.350 m) |
| Giá vải/m | 50.000 | 48.000 |
| SQ allowed | 1.000 × 1,2 = 1.200 m | – |

**Bước 1 – Price Variance**: (48.000 − 50.000) × 1.350 = **−2.700.000 (F)** → mua rẻ hơn 2.000đ/m.

**Bước 2 – Quantity Variance**: (1.350 − 1.200) × 50.000 = **+7.500.000 (U)** → dùng thừa 150 m.

**Bước 3 – Tổng**: −2.700.000 + 7.500.000 = **+4.800.000 (U)**. Đối chiếu: chi phí thực tế 1.350 × 48.000 = 64.800.000; chuẩn 1.200 × 50.000 = 60.000.000; chênh = 4.800.000 ✔.

```
       AQ × AP              AQ × SP              SQ × SP
      (Actual Cost)    (Actual Qty @ Std Price)  (Standard Cost)
     1.350 × 48k          1.350 × 50k          1.200 × 50k
     = 64.800.000         = 67.500.000         = 60.000.000
          │                     │                    │
          ├─ Price Var ─────────┤                    │
          │  = −2,7tr (F)       ├─ Quantity Var ─────┤
          │                     │  = +7,5tr (U)      │
          ├────────── Total DM Variance ─────────────┤
          │              = +4,8tr (U)                │
```

**Diễn giải**: tiết kiệm 2,7 triệu nhờ giá, nhưng đánh mất 7,5 triệu do hao phí. Nếu chỉ nhìn tổng (+4,8 triệu U) sẽ không biết rằng bộ phận Mua hàng làm tốt còn Sản xuất làm kém.

**Nguyên nhân có thể:**

| Variance | Favorable | Unfavorable |
|----------|----------|-------------|
| **Price** | Đàm phán giá tốt, mua sỉ | NVL tăng giá, khan hiếm |
| | Đổi nhà cung cấp rẻ hơn | Mua gấp, không có deal |
| | Giảm giá theo mùa | Nhà cung cấp thay đổi chính sách |
| **Quantity** | Thợ lành nghề, ít phế phẩm | Thợ mới, chất lượng NVL kém |
| | Cải tiến quy trình | Máy cũ, hao phí nhiều |
| | NVL chất lượng cao hơn | Thiết kế phức tạp hơn dự kiến |

> ⚠️ **Phải phân tích CẶP, không tách rời**: Price (F) + Quantity (U) thường liên quan nhau – mua vải rẻ → chất lượng kém → hao phí nhiều hơn. Trong ví dụ trên, lợi 2,7 triệu giá nhưng mất 7,5 triệu lượng → quyết định "mua rẻ" thực ra làm lỗ ròng. Nếu để Mua hàng chỉ bị đánh giá theo Price Variance, họ sẽ có động cơ mua hàng rẻ và kém.

### 3. Direct Labor Variance (Chênh lệch nhân công trực tiếp)

**Tại sao có cấu trúc giống DM?** Nhân công cũng là tích **Giá × Lượng**: Giá = đơn giá giờ công (Rate), Lượng = số giờ (Efficiency). Rate thuộc về nhân sự/lập kế hoạch ca (thuê ai, trả bao nhiêu, tăng ca không); Efficiency thuộc về quản đốc (làm nhanh hay chậm).

$$\text{DL Rate Variance} = (\text{AR} - \text{SR}) \times \text{AH}$$

$$\text{DL Efficiency Variance} = (\text{AH} - \text{SH}) \times \text{SR}$$

Trong đó: AR = lương thực tế/giờ; SR = lương tiêu chuẩn/giờ; AH = giờ làm thực tế; SH = giờ tiêu chuẩn cho sản lượng thực tế.

**Ví dụ (tiếp tục 1.000 áo thun):**

| | Standard | Actual |
|---|---------|--------|
| Giờ/áo | 1,7 h | 1,9 h (tổng AH = 1.900 h) |
| Lương/giờ | 40.000 | 42.000 |
| SH allowed | 1.000 × 1,7 = 1.700 h | – |

- **Rate Var** = (42.000 − 40.000) × 1.900 = **+3.800.000 (U)**
- **Efficiency Var** = (1.900 − 1.700) × 40.000 = **+8.000.000 (U)**
- **Tổng** = 11.800.000 (U). Đối chiếu: 1.900 × 42.000 = 79.800.000; 1.700 × 40.000 = 68.000.000; chênh = 11.800.000 ✔.

**Giải thích:** Rate (U) – trả lương cao hơn, có thể do thuê thợ lành nghề hơn, tăng ca (OT), tăng lương, hoặc tăng lương tối thiểu vùng (cần xác nhận mức hiện hành). Efficiency (U) – làm chậm hơn do thợ mới, máy hỏng, NVL kém, bố trí dây chuyền chưa hợp lý.

> **Ví dụ tương tác Rate–Efficiency**: thuê thợ giỏi (Rate U) có thể làm giảm giờ (Efficiency F); nếu Efficiency F lớn hơn Rate U thì quyết định đúng, và ngược lại. Cũng như DM, phải đọc cặp.

### 4. Manufacturing Overhead Variance (Chênh lệch chi phí sản xuất chung)

**Vấn đề đặc thù**: MOH (điện, khấu hao máy, thuê xưởng, quản đốc…) không gắn trực tiếp từng sản phẩm. Phải **phân bổ** theo một tiêu thức (ở đây là giờ nhân công trực tiếp – DLH). Vì phân bổ dựa trên giả định sản lượng, sinh ra thêm một loại chênh lệch không có ở DM/DL: **Volume Variance**. Để xử lý đúng, MOH tách thành biến phí (thay đổi theo hoạt động) và định phí (không đổi trong phạm vi công suất).

#### a. Variable MOH Variance

$$\text{VOH Spending Var} = \text{Actual VOH} - (\text{AH} \times \text{Std VOH Rate})$$

$$\text{VOH Efficiency Var} = (\text{AH} - \text{SH}) \times \text{Std VOH Rate}$$

- **Spending**: chi tiêu thực tế so với mức "phải chi" cho số giờ thực tế (giá điện, gas, vật tư phụ đắt hơn).
- **Efficiency**: biến phí MOH tăng theo giờ nhân công; nếu làm chậm (AH > SH) thì biến phí MOH tăng theo. Tức Efficiency của VOH **chỉ là hệ quả** của Efficiency của DL.

#### b. Fixed MOH Variance

$$\text{FOH Budget (Spending) Var} = \text{Actual FOH} - \text{Budgeted FOH}$$

$$\text{FOH Volume Var} = \text{Budgeted FOH} - \text{Applied FOH}, \quad \text{Applied FOH} = \text{SH} \times \text{FOH Rate}$$

$$\text{FOH Rate} = \frac{\text{Budgeted FOH}}{\text{Budgeted Output} \times \text{Std Hours/unit}}$$

> **Tại sao có Volume Variance? (phần dễ gây nhầm nhất)** Định phí là tiền chi ra **không đổi** dù sản xuất nhiều hay ít. Nhưng kế toán phải phân bổ vào từng sản phẩm bằng **một mức/đơn vị cố định** (FOH Rate), được tính từ sản lượng *kế hoạch*. Nếu thực tế sản xuất **ít hơn** kế hoạch, số FOH được "gánh" vào sản phẩm (Applied) sẽ **thấp hơn** số FOH đã dự toán → phần chưa gánh hết chính là Volume Variance (U) – tức **công suất bị bỏ không**. Đây không phải sai sót chi tiêu mà là hệ quả toán học của cách phân bổ định phí; nó cho biết "bao nhiêu tiền định phí đang trả cho công suất không dùng tới".

**Ví dụ (số liệu giả định đã thống nhất với thẻ giá thành):**

| | Budget | Actual |
|---|-------|--------|
| Variable MOH rate | 15.000/DLH | – |
| Actual Variable MOH | – | 30.000.000 |
| Fixed MOH | 40.800.000 | 42.000.000 |
| Output | 1.200 áo | 1.000 áo |
| FOH Rate | 40.800.000 / (1.200 × 1,7) = **20.000/DLH** | – |

- **VOH Spending** = 30.000.000 − (1.900 × 15.000 = 28.500.000) = **+1.500.000 (U)**
- **VOH Efficiency** = (1.900 − 1.700) × 15.000 = **+3.000.000 (U)**
- **FOH Budget** = 42.000.000 − 40.800.000 = **+1.200.000 (U)**
- **FOH Volume** = 40.800.000 − (1.700 × 20.000 = 34.000.000) = **+6.800.000 (U)**

→ Volume Variance (U): sản xuất ít hơn công suất kế hoạch (1.000 so với 1.200 áo) nên định phí bị "phân bổ thiếu" 6,8 triệu. Tổng MOH chưa phân bổ hết = Actual FOH 42,0 − Applied 34,0 = 8,0 triệu = 1,2 (Budget) + 6,8 (Volume) ✔.

> **Cảnh báo (liên hệ Case GM)**: có thể làm Volume Variance = 0 bằng cách sản xuất đủ 1.200 áo – nhưng nếu thị trường chỉ cần 1.000 thì 200 áo thừa chỉ tạo tồn kho. Volume Variance là chỉ báo để **xem xét công suất/kế hoạch bán hàng**, không phải mục tiêu để "tối ưu".

### 5. Sales Variance (Chênh lệch doanh thu)

**Tại sao doanh thu cũng phải tách?** Lợi nhuận thấp hơn kế hoạch có thể do bán **giá thấp hơn** (chính sách giảm giá), bán **ít hơn** (cầu yếu), hoặc bán **cơ cấu sản phẩm kém lợi nhuận hơn** (Mix). Ba nguyên nhân dẫn tới ba hành động khác nhau (chỉnh giá, tăng marketing, đổi cơ cấu bán).

$$\text{Sales Price Var} = (\text{Actual Price} - \text{Budgeted Price}) \times \text{Actual Qty}$$

$$\text{Sales Volume Var} = (\text{Actual Qty} - \text{Budgeted Qty}) \times \text{Budgeted Margin/unit}$$

> **Vì sao Volume Variance nhân với *margin* chứ không phải *giá bán*?** Bán thêm 1 sản phẩm chỉ làm lợi nhuận tăng thêm đúng phần margin của nó (phần còn lại là chi phí bù đắp cho chính sản phẩm đó). Nếu nhân với giá bán sẽ cường điệu tác động lên lợi nhuận. Cần nhất quán: dùng **Contribution Margin (CM)** (Variable/Direct costing) hoặc **lãi gộp theo absorption costing** (Absorption costing) – hai cách cho kết quả khác nhau ở khoản Fixed Overhead Volume (xem mục II.6).

**Ví dụ:**

| | Budget | Actual |
|---|-------|--------|
| Giá bán/áo | 350.000 | 330.000 |
| Số lượng bán | 1.200 | 1.000 |
| Lãi gộp chuẩn/áo (absorption) | 350.000 − 192.500 = **157.500** | – |

- **Price Var** = (330.000 − 350.000) × 1.000 = **−20.000.000 (U)**
- **Volume Var** = (1.000 − 1.200) × 157.500 = **−31.500.000 (U)**

→ Bán giá thấp hơn VÀ số lượng ít hơn → "double hit": −51,5 triệu lợi nhuận.

#### Sales Mix Variance và Quantity Variance (khi bán nhiều sản phẩm)

Khi doanh nghiệp bán nhiều sản phẩm có margin khác nhau, Sales Volume Variance còn tách tiếp thành:

$$\text{Sales Quantity Var} = (\text{Total Actual Qty} - \text{Total Budgeted Qty}) \times \text{Budgeted Avg CM/unit}$$

$$\text{Sales Mix Var} = \sum \left(\text{Actual Qty}_i - \text{Total Actual Qty} \times \text{Budgeted Mix}_i\right) \times \text{CM}_i$$

**Tại sao cần?** Bán đủ số ly nhưng dồn vào món margin thấp thì lợi nhuận vẫn thua kế hoạch – tổng số lượng không nói lên điều đó.

**Ví dụ (quán cà phê, giả định):** ngân sách 6.000 ly = 3.600 cà phê (CM 24.000) + 2.400 trà trái cây (CM 18.000); thực tế bán 5.400 ly = 2.700 cà phê + 2.700 trà.

- CM bình quân ngân sách = (3.600×24.000 + 2.400×18.000)/6.000 = **21.600**/ly
- **Quantity Var** = (5.400 − 6.000) × 21.600 = **−12.960.000 (U)**
- Cơ cấu ngân sách áp lên 5.400 ly: cà phê 3.240, trà 2.160 → **Mix Var** = (2.700 − 3.240)×24.000 + (2.700 − 2.160)×18.000 = −12.960.000 + 9.720.000 = **−3.240.000 (U)**
- **Tổng Volume Var** = −12.960.000 − 3.240.000 = **−16.200.000 (U)**; kiểm tra trực tiếp: (2.700−3.600)×24.000 + (2.700−2.400)×18.000 = −21.600.000 + 5.400.000 = −16.200.000 ✔.

→ Khách chuyển dần sang trà (margin thấp hơn) làm mất thêm 3,24 triệu ngoài việc bán ít hơn.

### 6. Bảng tổng hợp và đối chiếu (Reconciliation) – Công ty áo thun

Lập báo cáo lợi nhuận kế hoạch → thực tế để chứng minh các variance cộng lại đúng bằng tổng chênh lệch:

| Chỉ tiêu | Kế hoạch (1.200 áo) | Thực tế (1.000 áo) |
|---|---:|---:|
| Doanh thu | 1.200 × 350.000 = 420.000.000 | 1.000 × 330.000 = 330.000.000 |
| NVL (vải 64,8 + phụ kiện 5,0) | 1.200 × 65.000 = 78.000.000 | 69.800.000 |
| Nhân công | 1.200 × 68.000 = 81.600.000 | 79.800.000 |
| VOH | 1.200 × 25.500 = 30.600.000 | 30.000.000 |
| FOH | 40.800.000 | 42.000.000 |
| **Lợi nhuận** | **189.000.000** | **108.400.000** |

Chênh lệch lợi nhuận = 108,4 − 189,0 = **−80,6 triệu (U)**. Bóc tách:

```
┌──────────────────────────────────────────────────────────┐
│     VARIANCE ANALYSIS REPORT – THÁNG XX/20XX             │
│     Sản phẩm: Áo thun | Output: 1.000 cái                │
│                                                          │
│  VARIANCE              AMOUNT (tr)   STATUS   ƯU TIÊN    │
│  ──────────────────────────────────────────────────────  │
│  Sales Price            (20,0)        (U)      Cao       │
│  Sales Volume           (31,5)        (U)      Cao       │
│  ──────────────────────────────────────────────────────  │
│  DM Price                (2,7)         F       Theo dõi  │
│  DM Quantity             +7,5         (U)      Cao       │
│  DL Rate                 +3,8         (U)      TB        │
│  DL Efficiency           +8,0         (U)      Cao       │
│  VOH Spending            +1,5         (U)      TB        │
│  VOH Efficiency          +3,0         (U)      TB        │
│  FOH Budget              +1,2         (U)      TB        │
│  FOH Volume              +6,8         (U)      Cao       │
│  ──────────────────────────────────────────────────────  │
│  Tổng chi phí U          29,1                            │
│  TỔNG TÁC ĐỘNG LỢI NHUẬN (80,6)       (U)      ★★        │
└──────────────────────────────────────────────────────────┘
```

Kiểm tra: 20,0 + 31,5 + 29,1 = **80,6** ✔ (khớp chênh lệch lợi nhuận). Trong đó 29,1 = 4,8 (DM) + 11,8 (DL) + 4,5 (VOH) + 8,0 (FOH = 1,2 + 6,8).

> *(File cũ có tổng "49,0 triệu U" không khớp với các thành phần; đã sửa thành 80,6 sau khi thống nhất lại lãi gộp chuẩn và FOH.)*

**Hai cách nhìn Volume Variance – Absorption costing vs Contribution (Variable) costing:**

| | Absorption costing | Contribution costing |
|---|---|---|
| Margin dùng cho Sales Volume | 157.500/áo → (200) × 157.500 = −31,5tr | CM 191.500/áo → (200) × 191.500 = −38,3tr |
| Fixed overhead | Có **FOH Volume Var** 6,8tr | Chỉ có **FOH Budget Var** 1,2tr (không có Volume Var) |
| Tổng | 31,5 + 6,8 = 38,3 (cùng chiều) | 38,3 |

Hai cách cùng cho tổng −80,6tr (20,0 + 38,3 + 4,8 + 11,8 + 4,5 + 1,2 = 80,6 ✔) nhưng cách Contribution **rõ hơn cho SME**: không sinh ra "Volume Variance" khó hiểu, vì định phí được xem là chi phí kỳ này, không phân bổ theo sản lượng.

### 7. Framework phân tích nguyên nhân

#### a. Quy trình điều tra Variance

```
  Bước 1: Variance có significant không?
       │   Rule of thumb: > 5-10% hoặc > X triệu
       │
  Bước 2: Favorable hay Unfavorable? (F cũng cần xem – có thể do cắt chất lượng)
       │
  Bước 3: Root Cause Analysis (5 Whys)
       │
  Bước 4: Controllable hay Uncontrollable?
       │   - Controllable: Manager có thể sửa
       │   - Uncontrollable: Thị trường, thiên tai, chính sách
       │
  Bước 5: Corrective Action (ai – làm gì – khi nào)
       │
  Bước 6: Cập nhật Standard nếu điều kiện đã thay đổi bền vững
```

#### b. Ma trận nguyên nhân Variance

| Variance | Nguyên nhân Controllable | Nguyên nhân Uncontrollable |
|----------|------------------------|--------------------------|
| **DM Price (U)** | Mua ngoài deal, không tender | Giá nguyên liệu thế giới tăng |
| **DM Qty (U)** | Thợ tay nghề kém, setup máy sai | NVL kém chất lượng đợt này |
| **DL Rate (U)** | Tăng ca nhiều, thuê thợ đắt hơn | Tăng lương tối thiểu vùng (cần xác nhận) |
| **DL Eff (U)** | Training không đủ, workflow sai | Mất điện, máy hỏng |
| **Sales Price (U)** | Giảm giá nhiều, push volume | Đối thủ giảm giá, chiến tranh giá |
| **Sales Vol (U)** | Marketing yếu, đội bán hàng kém | Suy thoái kinh tế, mùa thấp điểm |
| **FOH Volume (U)** | Kế hoạch sản xuất kém | Đơn hàng giảm đột ngột |

#### c. Ví dụ 5-Why Analysis (5 Whys – kỹ thuật do Sakichi Toyoda phát triển và được Toyota phổ biến, cần đối chiếu nguồn)

**Variance:** DM Quantity Unfavorable (+7,5 triệu)

```
  Why 1: Tại sao dùng nhiều vải hơn standard?
  → Tỷ lệ phế phẩm tăng từ 5% lên 15%
  Why 2: Tại sao phế phẩm tăng?
  → Máy cắt bị lệch, cắt sai kích thước
  Why 3: Tại sao máy cắt lệch?
  → Lưỡi dao cũ, chưa được thay đúng lịch
  Why 4: Tại sao chưa thay lưỡi dao?
  → Không có lịch bảo trì định kỳ (preventive maintenance)
  Why 5: Tại sao không có lịch bảo trì?
  → Quản đốc mới chưa được training về SOP bảo trì

  ROOT CAUSE: Thiếu training SOP cho quản đốc mới
  ACTION: Lập SOP bảo trì máy + training bắt buộc cho quản lý mới
```

#### d. Nguyên tắc Management by Exception (Quản trị theo ngoại lệ)

**Tại sao?** Nguồn lực chú ý của chủ SME có hạn; điều tra mọi variance nhỏ tốn kém hơn lợi ích. Chỉ tập trung vào các chênh lệch **đủ lớn** (theo % và theo giá trị tuyệt đối) hoặc **lặp lại**.

| Tiêu chí | Threshold (tham khảo) | Hành động |
|----------|----------|----------|
| **Insignificant** | < 3% VÀ < 2 triệu | Bỏ qua |
| **Moderate** | 3–10% HOẶC 2–10 triệu | Theo dõi, báo cáo hàng tháng |
| **Significant** | > 10% HOẶC > 10 triệu | Điều tra ngay, hành động khắc phục |
| **Recurring** | Cùng variance 3+ tháng liên tiếp | Rà soát standard, có thể vấn đề hệ thống |

### 8. Ưu điểm và nhược điểm

| Ưu điểm | Chi tiết |
|---------|---------|
| **Accountability** | Gắn trách nhiệm: Price Var → Mua hàng, Qty Var → Sản xuất |
| **Early Warning** | Phát hiện vấn đề sớm trước khi tích lũy |
| **Continuous Improvement** | Tạo văn hóa so sánh & cải tiến |
| **Data-driven** | Quyết định dựa trên số liệu |
| **Cost Control** | Kiểm soát chi phí chặt chẽ |
| **Performance Evaluation** | Đánh giá hiệu suất bộ phận/cá nhân |

| Nhược điểm | Chi tiết |
|-----------|---------|
| **Backward-looking** | Phân tích SAU khi xảy ra |
| **Gaming** | Quản lý đặt standard dễ → luôn favorable |
| **Blame culture** | Dùng sai → văn hóa đổ lỗi |
| **Standard outdated** | Standard cũ không phản ánh thực tế mới |
| **Ignore qualitative** | Chỉ thấy con số, không thấy root cause |
| **Short-term focus** | Cắt R&D, training, bảo trì để "đẹp" variance |
| **Complexity** | Tốn thời gian & nguồn lực |

### 9. Hoàn cảnh và môi trường áp dụng

| Hiệu quả nhất khi… | Vì sao |
|----------|----------------|
| **Sản xuất lặp lại** | Standard dễ xác định, so sánh có ý nghĩa |
| **Chi phí chiếm tỷ trọng lớn** | Variance nhỏ % nhưng lớn về giá trị |
| **Nhiều yếu tố biến động** | Cần tracking giá NVL, năng suất, overhead |
| **DN đã có hệ thống ngân sách** | Variance analysis bổ sung cho budgeting |
| **Cần kiểm soát chi phí chặt** | Startup cần tối ưu burn rate |

| KHÔNG nên quá tập trung khi… | Vì sao |
|----------|--------|
| **Innovation/R&D** | Standard không có ý nghĩa cho sáng tạo |
| **Startup phase** | Chưa đủ dữ liệu lập standard |
| **Thị trường biến động mạnh** | Standard lỗi thời nhanh |
| **Ngành dịch vụ** | Khó chuẩn hóa từng dịch vụ (cần chuẩn hóa theo "đơn vị dịch vụ" ví dụ ly/lượt/bàn) |

---

## III. CASE STUDIES THỰC TẾ

### 1. Case Study Thành công: Toyota – Variance Analysis trong văn hóa Kaizen

> *Số liệu dưới đây mang tính minh họa nguyên lý, **cần đối chiếu nguồn** (báo cáo Toyota, Imai 1986, Liker 2004) trước khi trích dẫn chính thức.*

#### Bối cảnh
Toyota dùng variance như một phần của **Toyota Production System (TPS)** và triết lý **Kaizen** (cải tiến liên tục). Khác với mô hình "báo cáo cuối tháng cho kế toán", Toyota xem variance là **tín hiệu cải tiến tại hiện trường (genba)**.

#### Cách Toyota sử dụng so với doanh nghiệp thông thường

| Khía cạnh | Toyota | Doanh nghiệp thường |
|----------|---------|---------------------------|
| **Tần suất** | Hằng ngày/hằng giờ | Hàng tháng/quý |
| **Mức chi tiết** | Từng dây chuyền, ca, công đoạn | Tổng nhà máy |
| **Ai phân tích** | Tổ trưởng + công nhân tại hiện trường | Kế toán |
| **Standard** | Ideal Standard (mục tiêu cải tiến) | Currently Attainable |
| **Phản ứng** | Andon: dừng dây chuyền ngay | Chờ cuối tháng |
| **Văn hóa** | Variance = cơ hội cải tiến | Tìm người chịu trách nhiệm |

#### Diễn giải từng bước một chu kỳ Kaizen (số liệu giả định minh họa)

```
  Standard ban đầu: lắp ráp 1 xe mất 18,0 giờ nhân công (DL)

  Tuần 1: Actual = 18,3h → DL Efficiency Var = +0,3h (U)
          Root cause: bước gắn táp-lô mất thêm 0,3h
          Kaizen: thiết kế đồ gá (jig) mới

  Tuần 4: Actual = 17,8h → DL Efficiency Var = −0,2h (F)
          Jig mới hiệu quả → CẬP NHẬT Standard: 18,0h → 17,8h

  Tuần 8: Actual = 17,5h → tiếp tục Kaizen ...
  Sau 1 năm (giả định): Standard giảm 18,0h → 16,5h
```

**Tính tác động (giả định sản lượng 400.000 xe/năm):** tiết kiệm (18,0 − 16,5) = 1,5 giờ × 400.000 = **600.000 giờ công/năm**. Nếu đơn giá giờ công giả định 400.000đ/giờ thì tương đương 240 tỷ đồng/năm (600.000 × 400.000).

> **Điểm then chốt**: mỗi lần variance (F) xuất hiện, standard được **kéo xuống** – variance không bao giờ là "dừng ở đạt chuẩn" mà là điểm khởi đầu của vòng cải tiến mới.

#### Bài học
1. **Real-time** – phân tích ngay, không đợi cuối tháng.
2. **At the source** – người trực tiếp làm việc phân tích, không chỉ kế toán.
3. **Improvement, not blame** – variance = cơ hội, không phải lỗi.
4. **Update standards** – standard phải tiến hóa theo Kaizen.

---

### 2. Case Study Thất bại: General Motors – Variance Analysis tạo văn hóa "đạt chỉ tiêu"

> *Minh họa nguyên lý theo các phân tích học thuật về GM trước 2009; số liệu giả định, **cần đối chiếu nguồn** khi trích dẫn.*

#### Bối cảnh
Trước khi phá sản năm 2009 (Chapter 11), GM được nhiều tài liệu quản trị mô tả là dùng chỉ tiêu tài chính theo kiểu "hit the number", dẫn tới tối ưu cục bộ thay vì cải tiến thực sự.

#### Các sai lầm

| Sai lầm | Chi tiết | Hệ quả |
|--------|---------|--------|
| **Standard quá dễ** | Đặt theo lịch sử (kém) thay vì best practice | Luôn "đạt" nhưng thua đối thủ |
| **Blame game** | Variance U → quản lý bị phạt | Che giấu vấn đề |
| **Short-term fixes** | Cắt bảo trì, đào tạo để đạt chỉ tiêu tháng | Chất lượng giảm dần |
| **Ám ảnh Volume Variance** | Sản xuất nhiều để "dàn" định phí | Tồn kho phình to, phải giảm giá |
| **Phân tích theo silo** | Mỗi bộ phận tối ưu cho mình | Mua NVL rẻ → chất lượng kém → chi phí bảo hành tăng |

#### Phân tích bẫy Volume Variance từng bước (số liệu giả định)

Giả sử: công suất kế hoạch 500.000 xe, định phí kế hoạch 5.000 tỷ → FOH Rate = 5.000 tỷ / 500.000 = **10 triệu/xe**; cầu thị trường chỉ 350.000 xe.

- **Nếu sản xuất đúng cầu (350.000 xe)**: Applied FOH = 350.000 × 10tr = 3.500 tỷ → **Volume Var = 5.000 − 3.500 = 1.500 tỷ (U)** – báo cáo "xấu" nhưng không có tồn kho.
- **Nếu sản xuất 500.000 xe**: Applied = 5.000 tỷ → Volume Var = 0 – báo cáo "đẹp"; nhưng **150.000 xe thừa**. Nếu phải giảm giá 20% để bán, mỗi xe giá 500 triệu mất 100 triệu → thiệt hại 150.000 × 100tr = **15.000 tỷ** doanh thu, lớn hơn nhiều so với 1.500 tỷ "Volume Var" ban đầu. Ngoài ra còn chi phí lưu kho, thương hiệu bị hạ giá, khách chờ giảm giá mới mua.

→ Bài học số: **Volume Var (U) 1.500 tỷ là chi phí thật của công suất dư, nhưng "chữa" bằng sản xuất thừa tốn 10 lần hơn**.

```
  Sản xuất 500k xe ──► Volume Var = 0 (báo cáo đẹp)
       │                      │
       ▼                      ▼
  Nhu cầu chỉ 350k      Tồn kho 150k xe → giảm giá 20%
                        → Thương hiệu mất giá → Doanh thu & margin giảm
```

#### So sánh GM vs Toyota

| | GM | Toyota |
|---|------------|----------------|
| Variance = | Vấn đề → tìm người chịu lỗi | Cơ hội → cải tiến quy trình |
| Standard = | Dễ đạt | Khó, kéo giãn (stretch) |
| Khi (U) | Che giấu hoặc gaming | Andon: dừng & sửa ngay |
| Volume | Sản xuất max để giảm unit cost | Sản xuất theo demand (pull system) |

#### Bài học
1. **Variance analysis là công cụ cải tiến, không phải vũ khí đổ lỗi.**
2. **Volume Variance Favorable ≠ Tốt** – sản xuất thừa tạo vấn đề lớn hơn.
3. **Standard phải đủ thách thức.**
4. **Nhìn toàn cục** – tối ưu cục bộ có thể làm hại tổng thể (Mua rẻ → Bảo hành đắt).

---

### 3. Case Study SME Việt Nam: Quán cà phê "Hẻm 25" – Phân tích chênh lệch tháng 9 (số liệu giả định minh họa)

#### Bối cảnh
"Cà phê Hẻm 25" là quán cà phê nhỏ (1 cơ sở, TP.HCM), chủ quán lập ngân sách tháng 9 như sau: bán **6.000 ly**, giá bán trung bình **45.000đ/ly**, kỳ vọng lợi nhuận **72,6 triệu**. Cuối tháng, báo cáo thực tế chỉ có **29,22 triệu** – thấp hơn 43,38 triệu. Chủ quán cần biết: lỗi do đâu, ai/khâu nào cần sửa, và có đáng lo không. Quán dùng định mức theo ly: hạt cà phê, nguyên liệu khác (sữa, đường, ly nắp), giờ barista, biến phí chung (điện, gas, vật tư), định phí (thuê mặt bằng, khấu hao, lương quản lý).

#### Bước 1 – Lập thẻ định mức (Standard Cost Card) trên 1 ly

| Khoản mục | Định mức | Thành tiền/ly |
|---|---|---:|
| Hạt cà phê | 18 g × 450đ/g | 8.100 |
| NVL khác (sữa, đường, ly, nắp) | – | 9.000 |
| Nhân công trực tiếp | 0,08 giờ × 35.000đ/giờ | 2.800 |
| Biến phí chung (điện, gas…) | – | 3.000 |
| **Tổng biến phí** | | **22.900** |
| Định phí phân bổ | 60.000.000 / 6.000 ly | 10.000 |
| **Giá thành tiêu chuẩn đầy đủ** | | **32.900** |

Contribution Margin tiêu chuẩn = 45.000 − 22.900 = **22.100/ly**; lãi gộp absorption = 45.000 − 32.900 = **12.100/ly**.

**Ngân sách tĩnh (6.000 ly)**: Doanh thu = 6.000 × 45.000 = **270.000.000**; Chi phí = 6.000 × 32.900 = 197.400.000; **Lợi nhuận = 72.600.000**.

#### Bước 2 – Số liệu thực tế tháng 9

| Khoản mục | Thực tế |
|---|---|
| Số ly bán | 5.400 ly |
| Giá bán bình quân | 43.000đ/ly (do khuyến mãi) |
| Hạt cà phê dùng | 20 g/ly → 108.000 g; giá mua 480đ/g |
| NVL khác | 9.400đ/ly |
| Giờ barista | 520 giờ; đơn giá 36.500đ/giờ (có tăng ca) |
| Biến phí chung | 18.900.000 |
| Định phí chung | 62.500.000 |

Doanh thu thực tế = 5.400 × 43.000 = **232.200.000**. Chi phí: hạt = 108.000 × 480 = 51.840.000; NVL khác = 5.400 × 9.400 = 50.760.000; nhân công = 520 × 36.500 = 18.980.000; biến phí chung 18.900.000; định phí 62.500.000 → tổng **202.980.000**. **Lợi nhuận thực tế = 29.220.000.** Chênh lệch = 29,22 − 72,60 = **−43,38 triệu (U)**.

#### Bước 3 – Ngân sách linh hoạt cho 5.400 ly (để so sánh công bằng)

- Doanh thu linh hoạt = 5.400 × 45.000 = 243.000.000
- Biến phí chuẩn = 5.400 × 22.900 = 123.660.000; định phí không đổi = 60.000.000 → tổng 183.660.000
- **Lợi nhuận linh hoạt = 243,0 − 183,66 = 59,34 triệu**

Tầng 1 – **Sales Volume Variance (CM)** = (5.400 − 6.000) × 22.100 = **−13,26 triệu (U)** (72,60 → 59,34). Đây là phần do bán ít hơn, phần lớn ngoài quyền kiểm soát của barista.
Tầng 2 – chênh lệch từ 59,34 → 29,22 = **−30,12 triệu (U)**, cần phân tích tiếp (sau đây).

#### Bước 4 – Phân tích từng khoản

**a. Hạt cà phê**
- Lượng chuẩn SQ = 5.400 × 18 = 97.200 g; AQ = 108.000 g.
- **Price Var** = (480 − 450) × 108.000 = **+3.240.000 (U)**
- **Quantity Var** = (108.000 − 97.200) × 450 = **+4.860.000 (U)**
- Tổng = 8.100.000 (U). Đối chiếu: 51.840.000 − 97.200×450 (43.740.000) = 8.100.000 ✔.

**b. NVL khác** = 50.760.000 − 5.400×9.000 (48.600.000) = **+2.160.000 (U)** (không có dữ liệu giá/lượng riêng nên gộp một chỉ số; nên bổ sung ghi chép nếu muốn tách).

**c. Nhân công**
- SH = 5.400 × 0,08 = 432 giờ; AH = 520 giờ.
- **Rate Var** = (36.500 − 35.000) × 520 = **+780.000 (U)**
- **Efficiency Var** = (520 − 432) × 35.000 = **+3.080.000 (U)**
- Tổng = 3.860.000 (U). Đối chiếu: 18.980.000 − 432×35.000 (15.120.000) = 3.860.000 ✔.

**d. Biến phí chung** = 18.900.000 − 5.400×3.000 (16.200.000) = **+2.700.000 (U)** (định mức tính theo ly nên chỉ có Spending Variance).

**e. Định phí**
- **FOH Budget Var** = 62.500.000 − 60.000.000 = **+2.500.000 (U)**
- **FOH Volume Var** (absorption) = 60.000.000 − 5.400×10.000 (54.000.000) = **+6.000.000 (U)** – chỉ xuất hiện nếu dùng absorption costing; trong cách nhìn CM, chỉ cần FOH Budget Var.

**f. Giá bán**
- **Sales Price Var** = (43.000 − 45.000) × 5.400 = **−10.800.000 (U)** – khuyến mãi làm doanh thu mất 10,8 triệu.

#### Bước 5 – Đối chiếu tổng (Reconciliation)

| Thành phần | Số tiền | Ảnh hưởng LN |
|---|---:|---|
| Sales Volume (CM) | −13.260.000 | U |
| Sales Price | −10.800.000 | U |
| Hạt – giá | −3.240.000 | U |
| Hạt – lượng | −4.860.000 | U |
| NVL khác | −2.160.000 | U |
| Nhân công – rate | −780.000 | U |
| Nhân công – hiệu suất | −3.080.000 | U |
| Biến phí chung | −2.700.000 | U |
| Định phí – chi vượt | −2.500.000 | U |
| **Tổng** | **−43.380.000** | **U** |

Kiểm tra: 13,26 + 10,8 + 3,24 + 4,86 + 2,16 + 0,78 + 3,08 + 2,70 + 2,50 = **43,38** ✔ (khớp chênh lệch lợi nhuận 72,60 − 29,22). Nếu dùng absorption costing: Volume (12.100×600 = 7,26) + FOH Volume 6,0 = 13,26 ✔ – cùng kết quả.

#### Bước 6 – Phân loại theo Management by Exception (tỷ lệ so với chuẩn của khoản mục)

| Variance | Số tiền | % so với chuẩn | Mức |
|---|---:|---:|---|
| Hạt – lượng | 4,86tr | 11,1% (4,86/43,74) | Significant |
| Hạt – giá | 3,24tr | 7,4% | Moderate |
| Nhân công – hiệu suất | 3,08tr | 20,4% (3,08/15,12) | Significant |
| Nhân công – rate | 0,78tr | 4,3% (0,78/18,2) | Insignificant/Moderate |
| NVL khác | 2,16tr | 4,4% | Moderate |
| Biến phí chung | 2,70tr | 16,7% (2,7/16,2) | Significant |
| Định phí chi vượt | 2,50tr | 4,2% | Moderate |
| Giá bán | 10,8tr | 4,4% nhưng >10tr | Significant |

#### Bước 7 – Diễn giải ý nghĩa kinh doanh & hành động

1. **Hạt cà phê dùng 20 g/ly thay vì 18 g (+11%)** – nguyên nhân tiềm năng: barista pha "đậm tay", chưa cân định lượng, hoặc đổi sang loại hạt cần nhiều hơn. *Hành động*: cân hạt trước khi xay, SOP pha chế, kiểm tra ngẫu nhiên hàng tuần; mỗi 1 g/ly tiết kiệm 5.400 × 450 = 2,43 triệu/tháng.
2. **Giá hạt tăng 450 → 480đ/g (+6,7%)** – thường không kiểm soát được (giá nguyên liệu); *Hành động*: so báo giá 2–3 nhà rang, ký hợp đồng giá 3–6 tháng, nhưng **đọc cặp** với chất lượng/lượng dùng (không đổi sang hạt rẻ để rồi dùng nhiều hơn).
3. **Nhân công hiệu suất U 3,08 triệu** – barista dùng 520 giờ thay vì 432 giờ cho 5.400 ly: ca ít khách vẫn giữ nhiều người (định mức giờ giả định tỷ lệ theo ly nhưng thực tế một phần là cố định theo ca). *Hành động*: lập lịch ca theo khung giờ cao điểm; đánh giá lại định mức 0,08h/ly.
4. **Giá bán U 10,8 triệu** – khuyến mãi giảm 2.000đ/ly nhưng **không bù được lượng**: khuyến mãi vẫn bán 5.400 ly, ít hơn kế hoạch 600 ly! Lẽ ra khuyến mãi phải kéo lượng; đây là dấu hiệu **chương trình không hiệu quả**. *Hành động*: dừng hoặc thiết kế lại khuyến mãi (giới hạn món, khung giờ).
5. **Biến phí chung và định phí chi vượt** – điện, gas và có khả năng tiền thuê tăng; kiểm tra hóa đơn, thay thiết bị tiêu thụ cao.
6. **Volume U 13,26 triệu** – bán ít hơn 10%: cần xem lại Marketing/vị trí, không đổ cho barista.

**Kết luận**: trong tổng thiếu 43,38 triệu chỉ khoảng 13,26 triệu (31%) do bán ít hơn; **phần lớn (30,12 triệu, ~69%) do chính quán kiểm soát được** (khuyến mãi, định lượng, ca làm, chi phí chung). Cần xử lý ưu tiên: (1) định lượng hạt (4,86tr), (2) lịch ca (3,08tr), (3) chương trình khuyến mãi (10,8tr).

#### Bài học
- Phân tích tổng "lỗ 43 triệu" không giúp gì; bóc tầng bằng **flexible budget** cho biết 31% là do thị trường/bán hàng, 69% là vận hành.
- Một khuyến mãi làm **giảm giá mà không tăng lượng** là lỗi kép (Price U + Volume U) – chỉ lộ ra khi tách riêng hai variance.
- Dùng **Management by Exception** để chọn 3 việc cần làm thay vì 10.

---

## IV. ỨNG DỤNG CHO SME

### 1. Đặc thù SME Việt Nam khi áp dụng Variance Analysis

- **Không cần hệ thống phức tạp**: bắt đầu từ ngân sách theo tháng + định mức cho 3–5 khoản chi lớn nhất (thường NVL, nhân công, mặt bằng, marketing).
- **Dữ liệu là điểm nghẽn**: nhiều SME ghi chép sổ tay/Zalo; trước tiên cần thu thập số liệu thực tế đủ và kịp (xem mục V về phần mềm).
- **Chi phí không chính thức**: tiền mặt, nhân công thời vụ, chi phí giao nhận – nên đưa vào sổ quản trị để định mức sát thực tế.
- **Dễ "đặt chuẩn quá thấp" hoặc "chuẩn theo trí nhớ"**: dựa vào dữ liệu 3–6 tháng gần nhất + test thực tế (cân đo, bấm giờ) để lập định mức.
- **Tách báo cáo quản trị và báo cáo thuế**: variance dùng quản trị nội bộ; số liệu BCTC/thuế theo VAS/Thông tư 200 (hoặc 133) – cần xác nhận hiện hành với kế toán/thuế.

### 2. Template Variance Report đơn giản

```
┌──────────────────────────────────────────────────┐
│  VARIANCE REPORT THÁNG XX/20XX                   │
│  Sản phẩm/Cơ sở: __________                      │
│                                                  │
│              Budget   Flex.Bdg  Actual  Var  F/U │
│  ────────────────────────────────────────────    │
│  Doanh thu    ____    ____      ____    ____     │
│  - NVL        ____    ____      ____    ____     │
│  - Nhân công  ____    ____      ____    ____     │
│  - Overhead   ____    ____      ____    ____     │
│  ────────────────────────────────────────────    │
│  Lãi gộp      ____    ____      ____    ____     │
│  - Sales exp  ____    ____      ____    ____     │
│  - Admin exp  ____    ____      ____    ____     │
│  ────────────────────────────────────────────    │
│  Lợi nhuận    ____    ____      ____    ____     │
│                                                  │
│  TOP 3 VARIANCE CẦN XỬ LÝ:                       │
│  1. ____________ → Action: ______ / Ai: ___ / Hạn │
│  2. ____________ → Action: ______                │
│  3. ____________ → Action: ______                │
└──────────────────────────────────────────────────┘
```

### 3. Quy trình hằng tháng cho SME

| Bước | Hành động | Công cụ | Tần suất |
|------|----------|---------|---------|
| 1 | So sánh doanh thu & chi phí thực tế vs ngân sách linh hoạt | Excel/Google Sheets | Hằng tháng |
| 2 | Tô màu variance vượt ngưỡng (ví dụ >10% hoặc >5 triệu) | Conditional formatting | Hằng tháng |
| 3 | Top 3 variance → hỏi "Why?" ít nhất 3 lần | Họp 30 phút | Hằng tháng |
| 4 | Ghi action items (ai – làm gì – hạn) | Notion/Trello | Hằng tháng |
| 5 | Follow-up action tháng sau | Họp review | Hằng tháng |
| 6 | Cập nhật ngân sách/định mức nếu cần | Họp quý | Hằng quý |

### 4. Sai lầm thường gặp

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| So sánh thực tế với ngân sách **tĩnh** khi sản lượng khác | Kết luận sai (biến phí "tiết kiệm" giả) | Luôn lập flexible budget |
| Đặt định mức theo cảm tính | Variance vô nghĩa | Bấm giờ, cân đo, lấy dữ liệu thật |
| Chỉ đọc từng variance riêng lẻ | Bỏ sót cặp Price–Quantity | Đọc cặp giá–lượng, rate–efficiency |
| Phạt khi U | Nhân viên che giấu | Đánh giá theo cải tiến và nguyên nhân |
| Không cập nhật định mức | U/F liên tục, mất ý nghĩa | Rà soát định mức mỗi quý/6 tháng |
| Theo đuổi Volume Variance = 0 | Tồn kho, giảm giá | Sản xuất theo cầu |
| Không gắn hành động | Báo cáo "để đó" | Mỗi variance lớn có người chịu trách nhiệm + hạn |

---

## V. TOOLS & TEMPLATES

### 1. Phần mềm kế toán/bán hàng phổ biến tại Việt Nam (giá tham khảo – **ước tính cần xác nhận** với nhà cung cấp)

| Phần mềm | Dùng để | Hỗ trợ variance? | Giá tham khảo (ước tính, cần xác nhận) |
|---|---|---|---|
| **MISA SME / MISA AMIS Kế toán** | Kế toán, giá thành, công nợ | Có báo cáo giá thành; so sánh thực tế–kế hoạch cần xuất Excel | Từ khoảng vài triệu/năm (gói nhỏ), cần xác nhận |
| **FAST Accounting** | Kế toán doanh nghiệp, sản xuất | Giá thành, định mức NVL (BOM) | Tùy module, cần báo giá |
| **KiotViet** | POS bán lẻ/F&B, tồn kho | Doanh thu, giá bán thực tế, tồn kho, lãi gộp theo sản phẩm | Khoảng vài trăm nghìn/tháng, cần xác nhận |
| **Sapo / iPOS** | POS, tồn kho, kênh online | Phân tích lãi gộp, doanh số theo kênh | Tương tự, cần xác nhận |
| **Google Sheets / Excel** | Ngân sách, flexible budget, variance | Linh hoạt nhất cho SME nhỏ | Miễn phí / Microsoft 365 theo gói |
| **Power BI / Looker Studio** | Dashboard variance | Có – nối với Sheets | Looker Studio miễn phí; Power BI theo gói, cần xác nhận |
| **Notion / Trello** | Ghi action items sau họp variance | Quản lý hành động | Gói cơ bản miễn phí |

*(Tham khảo thêm danh mục công cụ ở file `cong-cu-quan-tri-doanh-nghiep-sme.md`.)*

### 2. Cấu trúc Excel/Google Sheets mẫu cho variance

| Sheet | Nội dung |
|---|---|
| **Standards** | Thẻ định mức (giá, lượng, giờ, biến phí, định phí) – ô input màu xanh |
| **Budget** | Ngân sách tĩnh theo tháng |
| **Actual** | Dữ liệu thực tế (nhập từ POS/kế toán) |
| **Flexible** | Ngân sách linh hoạt = sản lượng thực tế × định mức |
| **Variance** | Công thức Price/Qty/Rate/Efficiency/Spending/Volume; cột F/U tự động bằng `IF` |
| **Dashboard** | Biểu đồ waterfall từ lợi nhuận ngân sách → thực tế |

Công thức Excel gợi ý: `=(AP-SP)*AQ` cho Price Var; `=(AQ-SQ)*SP` cho Qty Var; `=IF(Var>0,"U","F")` cho chi phí (đảo chiều cho doanh thu); `=IF(ABS(Var)/Standard>0.1,"Điều tra","OK")` cho ngưỡng ngoại lệ.

---

## VI. BÀI TẬP THỰC HÀNH

**Bài 1 – DM.** Xưởng may định mức: 2.000 m vải cho sản lượng thực tế, giá chuẩn 100.000đ/m. Thực tế dùng 2.100 m, giá mua 95.000đ/m. Tính Price Var, Quantity Var, Total, và nhận định.

**Bài 2 – DL.** Tiêu chuẩn 1.400 giờ cho sản lượng thực tế, lương chuẩn 50.000đ/giờ. Thực tế 1.500 giờ, lương 52.000đ/giờ. Tính Rate Var và Efficiency Var; nêu 2 nguyên nhân có thể.

**Bài 3 – Sales.** Ngân sách bán 1.000 sản phẩm, giá 200.000, chi phí chuẩn 120.000 (margin 80.000). Thực tế bán 900 sản phẩm giá 180.000. Tính Sales Price Var và Sales Volume Var.

**Bài 4 – Mix.** Dùng số liệu mục II.5 (quán cà phê: ngân sách 3.600 cà phê CM 24.000 + 2.400 trà CM 18.000; thực tế 2.700 + 2.700). Tính Quantity Var, Mix Var, Total Volume Var.

**Bài 5 – Case "Hẻm 25".** Giả sử chủ quán ngừng khuyến mãi, giá về 45.000, bán 5.400 ly (giả định lượng không đổi). Dựa vào bảng reconciliation, lợi nhuận thực tế mới là bao nhiêu? Nếu đồng thời giảm lượng hạt còn 18 g/ly (giá vẫn 480đ/g), lợi nhuận thay đổi thế nào?

**Bài 6 – Tình huống thảo luận.** Bộ phận mua hàng báo cáo DM Price (F) lớn nhưng DM Quantity (U) lớn hơn. Bạn thiết kế lại cách đánh giá bộ phận Mua hàng như thế nào để tránh động cơ "mua rẻ, chất kém"?

### Gợi ý đáp số (đã kiểm tra bằng Python)

- **Bài 1**: Price = (95.000 − 100.000) × 2.100 = **−10.500.000 (F)**; Quantity = (2.100 − 2.000) × 100.000 = **+10.000.000 (U)**; Total = **−500.000 (F)** (chi phí thực tế 199,5tr vs chuẩn 200tr). Nhận định: tiết kiệm giá gần như bị triệt tiêu bởi hao phí → xem lại chất lượng vải.
- **Bài 2**: Rate = (52.000 − 50.000) × 1.500 = **+3.000.000 (U)**; Efficiency = (1.500 − 1.400) × 50.000 = **+5.000.000 (U)**; Total = 8.000.000 (U). Nguyên nhân: tăng ca/thuê thợ đắt; thợ mới, máy hỏng.
- **Bài 3**: Price = (180.000 − 200.000) × 900 = **−18.000.000 (U)**; Volume = (900 − 1.000) × 80.000 = **−8.000.000 (U)**; tổng −26.000.000.
- **Bài 4**: Quantity = −12.960.000 (U); Mix = −3.240.000 (U); Total = −16.200.000 (U).
- **Bài 5**: Sales Price Var = 0 → lợi nhuận tăng thêm 10,8tr → **40,02 triệu**. Giảm hạt còn 18g: lượng hạt dùng = 97.200g; chi phí = 97.200 × 480 = 46.656.000 (giảm 51.840.000 − 46.656.000 = 5.184.000) → lợi nhuận **45,204 triệu** (kiểm tra: Quantity Var còn 0, Price Var còn (480−450)×97.200 = 2.916.000; tổng hạt U = 2,916 so với 8,1 trước → giảm 5,184 ✔).
- **Bài 6**: Gợi ý: đánh giá theo **tổng chi phí NVL trên đơn vị thành phẩm** (đạt chất lượng), kèm tỷ lệ phế phẩm/trả hàng, thay vì chỉ giá mua; chia sẻ chỉ tiêu giữa Mua hàng và Sản xuất.

---

## PHỤ LỤC: CHECKLIST VARIANCE ANALYSIS TỔNG HỢP

### A. Checklist trước khi áp dụng (thiết lập)
- □ Đã xác định đơn vị tính cho sản phẩm/dịch vụ (áo, ly, suất ăn, đơn hàng…)
- □ Đã lập thẻ định mức (giá, lượng, giờ, biến phí chung, định phí) từ dữ liệu thực tế 3–6 tháng
- □ Đã chọn loại standard (Ideal / Currently Attainable / Basic) và thống nhất với nhân viên
- □ Đã lập ngân sách tĩnh VÀ có cách tính ngân sách linh hoạt (flexible budget)
- □ Đã chọn cách tính margin nhất quán (CM hay absorption) cho Sales Volume Variance
- □ Đã có nguồn dữ liệu thực tế đầy đủ (POS, kế toán, bảng chấm công, phiếu xuất kho)
- □ Đã thống nhất ngưỡng Management by Exception (% và triệu đồng)
- □ Đã xác nhận với kế toán/thuế các quy định hiện hành (VAS 02, TT200/TT133…) khi dùng định mức cho BCTC

### B. Checklist hằng tháng
- □ So sánh Doanh thu: Actual vs Budget vs Flexible (theo sản phẩm/kênh)
- □ Tách Sales Price, Sales Volume (và Mix nếu nhiều sản phẩm)
- □ So sánh COGS: NVL (Price/Qty), nhân công (Rate/Efficiency), overhead
- □ So sánh chi phí hoạt động: marketing, quản lý, IT
- □ Highlight top 3 variance lớn nhất
- □ Root cause analysis (5 Whys) cho variance significant
- □ Phân loại controllable/uncontrollable
- □ Đọc cặp Price–Quantity và Rate–Efficiency trước khi kết luận
- □ Gán hành động khắc phục với người chịu trách nhiệm và hạn
- □ Follow-up hành động tháng trước
- □ Kiểm tra variance lặp ≥ 3 tháng → rà soát standard
- □ Cập nhật rolling forecast nếu xu hướng đổi
- □ Kiểm tra tổng các variance = chênh lệch lợi nhuận (reconciliation)

### C. Công thức tổng hợp

| Nhóm | Công thức | Ý nghĩa |
|---|---|---|
| **DM Price** | (AP − SP) × AQ | Giá mua lệch chuẩn (Mua hàng) |
| **DM Quantity** | (AQ − SQ) × SP | Lượng dùng lệch chuẩn (Sản xuất) |
| **DL Rate** | (AR − SR) × AH | Đơn giá giờ công lệch chuẩn |
| **DL Efficiency** | (AH − SH) × SR | Số giờ lệch chuẩn |
| **VOH Spending** | Actual VOH − AH × Std VOH Rate | Chi tiêu biến phí chung lệch |
| **VOH Efficiency** | (AH − SH) × Std VOH Rate | Hệ quả hiệu suất giờ công |
| **FOH Budget** | Actual FOH − Budgeted FOH | Chi định phí vượt ngân sách |
| **FOH Volume** | Budgeted FOH − SH × FOH Rate | Công suất bỏ không (chỉ absorption) |
| **FOH Rate** | Budgeted FOH ÷ (Budgeted Output × Std Hours) | Mức phân bổ định phí |
| **Sales Price** | (AP − BP) × AQ | Giá bán thực tế vs kế hoạch |
| **Sales Volume** | (AQ − BQ) × Budgeted margin/unit | Bán nhiều/ít hơn kế hoạch |
| **Sales Quantity** | (Total AQ − Total BQ) × Budgeted avg CM | Tổng lượng lệch |
| **Sales Mix** | Σ (AQ_i − Total AQ × Budgeted Mix_i) × CM_i | Cơ cấu sản phẩm lệch |
| **Check** | Σ variances = Actual Profit − Budgeted Profit | Đối chiếu |

> Dấu: chi phí dương = U; doanh thu/lợi nhuận âm = U. Luôn ghi (F)/(U).

---

*Tài liệu tham khảo:*

1. **Horngren, Datar & Rajan** – "Cost Accounting: A Managerial Emphasis" Ch. 7–8 (Flexible Budgets & Variances)
2. **Garrison, Noreen & Brewer** – "Managerial Accounting" Ch. 10–11
3. **Kaplan & Norton** – "The Balanced Scorecard" (beyond variance)
4. **Imai, Masaaki** – "Kaizen: The Key to Japan's Competitive Success"
5. **Womack & Jones** – "Lean Thinking" (Toyota's approach)
6. **CMA** – Part 1: Planning, Budgeting & Forecasting (variance analysis)
7. **Harvard Business Review** – "Stop Using Cost Variance Analysis" (critical view)
8. Chuẩn mực kế toán Việt Nam VAS 02 – Hàng tồn kho; Thông tư 200/2014/TT-BTC; Thông tư 133/2016/TT-BTC (cần xác nhận hiện hành); IAS 2 – Inventories
