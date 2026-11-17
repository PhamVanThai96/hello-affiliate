# 07. Dự báo Nhu cầu (Demand Forecasting)

> **Mục tiêu**: Giúp người mới hiểu *bản chất* của dự báo nhu cầu: vì sao dự báo luôn có sai số, mỗi kỹ thuật (trung bình động, san bằng số mũ, Holt/Holt-Winters, hồi quy, phân rã mùa vụ, định tính) giải quyết vấn đề gì, cách tính từng bước, cách đo sai số (MAD, MSE, RMSE, MAPE, Bias, Tracking Signal) và cách chọn mô hình phù hợp cho SME Việt Nam.

> File thuộc bộ kiến thức Quản trị Vận hành (Operations Management) - MBA Knowledge Base
> Liên kết: [04-inventory-management.md](./04-inventory-management.md) | [05-capacity-planning.md](./05-capacity-planning.md) | [08-layout-strategy.md](./08-layout-strategy.md)

> **Quy ước số liệu trong file**: Mọi bộ số có nhãn "giả định minh họa" do tác giả tự thiết kế để tính toán và đã được kiểm tra bằng Python. Số liệu về doanh nghiệp thật (Walmart, Vinamilk, Coca-Cola, Grab...) chỉ mang tính mô tả khái quát hoặc "ước tính/minh họa", không phải số liệu công bố đã kiểm chứng.

---

## MỤC LỤC

- [I. Khái niệm & Lý thuyết](#i-khái-niệm--lý-thuyết)
- [II. Chi tiết từng kỹ thuật dự báo](#ii-chi-tiết-từng-kỹ-thuật-dự-báo)
- [III. Case Studies thực tế](#iii-case-studies-thực-tế)
- [IV. Ứng dụng cho SME](#iv-ứng-dụng-cho-sme)
- [V. Tools & Templates](#v-tools--templates)
- [VI. Bài tập thực hành](#vi-bài-tập-thực-hành)
- [PHỤ LỤC: CHECKLIST DỰ BÁO TỔNG HỢP](#phụ-lục-checklist-dự-báo-tổng-hợp)
- [TÀI LIỆU THAM KHẢO](#tài-liệu-tham-khảo)

---

## I. Khái niệm & Lý thuyết

### 1.1. Định nghĩa và vai trò của Dự báo trong Quản trị Vận hành

**Dự báo (Forecasting)** là quá trình ước lượng các sự kiện tương lai bằng cách phân tích dữ liệu lịch sử và các yếu tố liên quan, nhằm hỗ trợ ra quyết định về hoạch định nhu cầu, tồn kho, năng lực, nhân sự và tài chính.

**Vấn đề kinh doanh mà dự báo giải quyết**: mọi quyết định vận hành đều phải được đưa ra *trước* khi biết nhu cầu thật. Nhà hàng phải đặt hải sản tươi từ 4 giờ sáng, nhà máy phải đặt nguyên liệu trước 4-8 tuần, một chuỗi cửa hàng phải thuê mặt bằng trước 3-5 năm. Nếu đoán thấp, doanh nghiệp mất doanh thu và khách hàng (thiếu hàng - Stockout); nếu đoán cao, doanh nghiệp chôn vốn vào tồn kho, hàng hỏng, hàng lỗi mốt (dư hàng - Overstock). Dự báo là cách làm cho việc "đoán" này có hệ thống, đo được và cải thiện được.

Dự báo là đầu vào nền tảng cho hầu hết các quyết định vận hành đã phân tích ở các file trước: công thức EOQ và Safety Stock (file 04) cần dự báo nhu cầu và độ biến động; hoạch định năng lực (file 05) cần dự báo tăng trưởng dài hạn; quản trị dự án (file 06) cần ước lượng thời gian dựa trên dữ liệu lịch sử.

### 1.2. Bốn nguyên lý cơ bản của dự báo

1. **Dự báo hầu như luôn sai** - mục tiêu là giảm thiểu và *đo lường* sai số, không phải loại bỏ hoàn toàn. Vì vậy mọi dự báo nên đi kèm một con số sai số (ví dụ MAPE, RMSE) để người dùng biết nên tin đến mức nào.
2. **Dự báo cho nhóm tổng hợp chính xác hơn dự báo từng SKU/khu vực riêng lẻ** (nguyên lý Risk Pooling, file 04). Lý do thống kê: khi cộng nhiều chuỗi độc lập, sai số ngẫu nhiên có xu hướng bù trừ cho nhau (cái dư của sản phẩm A bù cái thiếu của sản phẩm B), nên sai số *tương đối* của tổng nhỏ hơn.
3. **Dự báo ngắn hạn chính xác hơn dự báo dài hạn** - tương lai gần còn giống hiện tại, tương lai xa chịu nhiều cú sốc chưa xảy ra.
4. **Dự báo tốt là dự báo được giám sát liên tục** - thị trường thay đổi, mô hình tốt hôm nay có thể kém vào quý sau (xem Tracking Signal, mục 2.8).

### 1.3. Lịch sử hình thành (Origin) các kỹ thuật chính

| Kỹ thuật | Người/tổ chức | Năm | Bối cảnh ra đời |
|---|---|---|---|
| San bằng số mũ đơn | Robert G. Brown | Giữa thập niên 1950 | Dự báo nhu cầu phụ tùng cho Hải quân Mỹ: hàng trăm nghìn mã hàng, máy tính thời đó rất yếu nên cần công thức chỉ phải nhớ 1 con số cho mỗi mã |
| Holt (xu hướng) | Charles C. Holt | 1957 | Mở rộng san bằng số mũ cho dữ liệu có xu hướng |
| Holt-Winters (mùa vụ) | Peter R. Winters (sinh viên của Holt) | 1960 | Thêm thành phần mùa vụ, kiểm chứng trên dữ liệu bán hàng thực |
| Phương pháp Delphi | Dalkey, Helmer (RAND Corporation) | Thập niên 1950-1960 | Dự báo công nghệ quân sự khi không có dữ liệu lịch sử; hạn chế ảnh hưởng của người có chức vị cao trong nhóm |
| ARIMA | George Box & Gwilym Jenkins | 1970 | Hệ thống hoá phương pháp xây dựng mô hình chuỗi thời gian (cuốn "Time Series Analysis") |
| Hồi quy bình phương nhỏ nhất | Legendre/Gauss (đầu thế kỷ 19); thuật ngữ "regression" gắn với Francis Galton (1880s) | - | Ban đầu dùng trong thiên văn, sau mở rộng sang kinh tế và kinh doanh |
| CPFR | Hiệp hội VICS (ngành bán lẻ Mỹ) | Cuối thập niên 1990 | Chuẩn hoá cách nhà sản xuất và nhà bán lẻ cùng lập dự báo (xem file 03) |
| Prophet | Nhóm dữ liệu của Facebook/Meta | 2017 (mã nguồn mở) | Công cụ dự báo dễ dùng cho dữ liệu kinh doanh nhiều mùa vụ và ngày lễ |
| Các cuộc thi M-Competitions | Spyros Makridakis và cộng sự | 1982 đến nay (M3, M4 năm 2018, M5 năm 2020) | So sánh khách quan nhiều phương pháp trên hàng nghìn đến hàng trăm nghìn chuỗi thật |

### 1.4. Phân loại dự báo theo khoảng thời gian

| Loại dự báo | Khoảng thời gian | Mục đích sử dụng |
|---|---|---|
| Ngắn hạn (Short-term) | Dưới 3 tháng | Lập lịch sản xuất, đặt hàng, phân bổ nhân sự hàng ngày/tuần |
| Trung hạn (Medium-term) | 3 tháng - 2 năm | Hoạch định tổng hợp (Aggregate Planning), ngân sách |
| Dài hạn (Long-term) | Trên 2 năm | Hoạch định năng lực, đầu tư nhà máy, chiến lược sản phẩm mới |

### 1.5. Phân loại phương pháp: Định tính vs Định lượng

```
                        PHƯƠNG PHÁP DỰ BÁO
                                │
              ┌─────────────────┴─────────────────┐
              ▼                                     ▼
      ĐỊNH TÍNH (Qualitative)              ĐỊNH LƯỢNG (Quantitative)
    (dựa trên ý kiến, kinh nghiệm)      (dựa trên dữ liệu số lịch sử)
              │                                     │
    ┌─────────┼─────────┐                ┌─────────┼─────────┐
    ▼         ▼         ▼                ▼         ▼         ▼
  Delphi   Ý kiến    Nghiên cứu      Chuỗi thời gian   Nhân quả
  Method   chuyên     thị trường      (Time Series)    (Causal/
           gia        (Market                          Regression)
                       Survey)
```

**Khi nào dùng định tính**: khi thiếu dữ liệu lịch sử (sản phẩm mới, thị trường mới), hoặc khi cần tích hợp thông tin quan trọng mà mô hình số không nắm bắt được (thay đổi chính sách, công nghệ đột phá, đối thủ ra mắt sản phẩm).

**Khi nào dùng định lượng**: khi có đủ dữ liệu lịch sử đáng tin cậy và mối quan hệ giữa các biến tương đối ổn định theo thời gian.

**Bảng chọn phương pháp theo giai đoạn vòng đời sản phẩm**:

| Giai đoạn vòng đời sản phẩm | Phương pháp phù hợp | Lý do |
|---|---|---|
| Giới thiệu (Introduction) | Định tính (Delphi, nghiên cứu thị trường) | Chưa có dữ liệu lịch sử |
| Tăng trưởng (Growth) | Kết hợp định tính + định lượng đơn giản (Holt, hồi quy xu hướng) | Dữ liệu bắt đầu tích luỹ nhưng còn ít, xu hướng thay đổi nhanh |
| Trưởng thành (Maturity) | Định lượng (Holt-Winters, hồi quy, phân rã mùa vụ) | Dữ liệu lịch sử đầy đủ, xu hướng và mùa vụ ổn định |
| Suy thoái (Decline) | Định lượng kết hợp giám sát xu hướng giảm | Cần phát hiện sớm tốc độ suy giảm để điều chỉnh sản xuất/tồn kho |

### 1.6. Các thành phần của chuỗi thời gian (Time Series Components)

**Tại sao phải tách thành phần?** Một con số doanh số tháng này là sự pha trộn của nhiều lực: thị trường đang lớn dần, tháng này vào mùa cao điểm, nền kinh tế đang chu kỳ tốt và một chút may rủi. Mỗi lực đòi hỏi một cách xử lý khác nhau; nếu không tách ra, ta sẽ nhầm "mùa vụ" thành "tăng trưởng" (và đặt hàng quá tay) hoặc nhầm "nhiễu ngẫu nhiên" thành "xu hướng".

```
Nhu cầu
    │           Xu hướng (Trend)
    │          ╱────────────────
    │        ╱      ╱╲    ╱╲
    │      ╱      ╱    ╲╱    ╲     ← Biến động mùa vụ (Seasonality)
    │    ╱      ╱                ╲
    │  ╱      ╱                    ╲
    │╱      ╱                        ╲___
    └──────────────────────────────────────▶ Thời gian
      Chu kỳ (Cyclical)    Biến động ngẫu nhiên (Random/Irregular)
      - dao động dài hạn    - nhiễu không dự đoán được
      (kinh tế vĩ mô)
```

Bốn thành phần cơ bản:
1. **Xu hướng (Trend - T)**: hướng tăng/giảm dài hạn của dữ liệu.
2. **Mùa vụ (Seasonality - S)**: biến động lặp lại theo chu kỳ cố định (ngày, tuần, tháng, quý, năm).
3. **Chu kỳ (Cyclical - C)**: dao động dài hạn không cố định về thời gian, thường gắn với chu kỳ kinh tế vĩ mô (khác mùa vụ ở chỗ không có tần suất cố định).
4. **Biến động ngẫu nhiên (Random/Irregular - R)**: nhiễu không thể dự đoán, do các sự kiện bất thường.

**Mô hình phân rã (Decomposition Model)**:
- Mô hình cộng (Additive): $Y = T + S + C + R$ - phù hợp khi biên độ mùa vụ ổn định theo thời gian (mùa cao điểm luôn cao hơn bình thường khoảng +50 đơn vị).
- Mô hình nhân (Multiplicative): $Y = T \times S \times C \times R$ - phù hợp khi biên độ mùa vụ tỷ lệ với quy mô (mùa cao điểm luôn cao hơn bình thường khoảng +20%). Trong kinh doanh, khi doanh số tăng thì đỉnh mùa vụ cũng cao theo nên mô hình nhân thường hợp lý hơn; các ví dụ mùa vụ trong file này dùng mô hình nhân.

### 1.7. Bộ dữ liệu mẫu dùng xuyên suốt Chương II

Để người đọc so sánh các kỹ thuật một cách công bằng, mục II dùng chung một bộ số (giả định minh họa): doanh số 12 tháng của một cửa hàng bán lẻ, đơn vị: thùng hàng/tháng.

| Tháng (t) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Doanh số $Y_t$ | 120 | 132 | 128 | 141 | 150 | 147 | 160 | 172 | 165 | 178 | 185 | 181 |

Đặc điểm: có xu hướng tăng rõ (khoảng +6 thùng/tháng) và nhiễu ngẫu nhiên vài thùng, chưa có mùa vụ. Bộ số này cố ý chọn có xu hướng để minh họa điểm yếu cốt lõi của các phương pháp "không biết xu hướng" (trung bình động, san bằng số mũ đơn).

---

## II. Chi tiết từng kỹ thuật dự báo

### 2.1. Trung bình động (Moving Average) và Trung bình động có trọng số

**Tại sao cần?** Phương pháp ngây thơ "tháng sau = tháng này" (Naive) quá nhạy với nhiễu: một tháng có chương trình khuyến mãi lớn sẽ làm dự báo tháng sau bị méo. Trung bình động giải quyết bằng cách *lấy trung bình của $n$ kỳ gần nhất* để các nhiễu ngẫu nhiên (lúc cao lúc thấp) triệt tiêu lẫn nhau, chỉ còn mức nhu cầu "nền".

$$MA_n = \frac{\sum_{i=1}^{n} Y_{t-i+1}}{n}$$

Trong đó $n$ là số kỳ lấy trung bình, $Y_{t-i+1}$ là doanh số của kỳ thứ $i$ tính ngược từ kỳ hiện tại. Dự báo kỳ $t+1$ chính là $MA_n$ tính tại kỳ $t$.

**Đánh đổi chọn $n$**: $n$ lớn thì đường dự báo mượt (giảm nhiễu) nhưng phản ứng chậm khi nhu cầu thực sự thay đổi; $n$ nhỏ thì phản ứng nhanh nhưng dễ bị nhiễu kéo.

**Ví dụ tính nhanh**: doanh số tháng 1, 2, 3 là 100, 120, 110 thì dự báo tháng 4: $MA_3 = \frac{100+120+110}{3} = 110$ đơn vị.

**Trung bình động có trọng số (Weighted Moving Average - WMA)**: gán trọng số cao hơn cho dữ liệu gần đây vì chúng phản ánh tốt hơn tình trạng hiện tại:

$$WMA = \sum w_i \times Y_{t-i+1}, \quad \sum w_i = 1$$

Ví dụ với bộ 100, 120, 110 và trọng số 0.5 (kỳ gần nhất), 0.3, 0.2: $WMA = 0.5 \times 110 + 0.3 \times 120 + 0.2 \times 100 = 55 + 36 + 20 = 111$ đơn vị.

#### Áp dụng trên bộ dữ liệu mẫu (MA3, từng bước)

Dự báo tháng 4 = $(120+132+128)/3 = 126.67$. Sai số $e_4 = 141 - 126.67 = 14.33$. Tương tự cho các tháng sau:

| Tháng | Thực tế $Y$ | Dự báo $F$ (MA3) | Sai số $e=Y-F$ | $\lvert e \rvert$ | $e^2$ | $\lvert e \rvert / Y$ |
|---|---|---|---|---|---|---|
| 4 | 141 | 126.67 | 14.33 | 14.33 | 205.44 | 10.17% |
| 5 | 150 | 133.67 | 16.33 | 16.33 | 266.78 | 10.89% |
| 6 | 147 | 139.67 | 7.33 | 7.33 | 53.78 | 4.99% |
| 7 | 160 | 146.00 | 14.00 | 14.00 | 196.00 | 8.75% |
| 8 | 172 | 152.33 | 19.67 | 19.67 | 386.78 | 11.43% |
| 9 | 165 | 159.67 | 5.33 | 5.33 | 28.44 | 3.23% |
| 10 | 178 | 165.67 | 12.33 | 12.33 | 152.11 | 6.93% |
| 11 | 185 | 171.67 | 13.33 | 13.33 | 177.78 | 7.21% |
| 12 | 181 | 176.00 | 5.00 | 5.00 | 25.00 | 2.76% |
| **Tổng** | | | **107.67** | **107.67** | **1,492.11** | **66.35%** |

- MAD $= 107.67 / 9 = 11.96$ thùng; MSE $= 1492.11/9 = 165.79$; RMSE $= \sqrt{165.79} = 12.88$; MAPE $= 66.35\%/9 = 7.37\%$; Bias $= +11.96$.
- Dự báo tháng 13 (MA3) $= (178+185+181)/3 = 181.33$. Với trọng số 0.5/0.3/0.2: $0.5 \times 181 + 0.3 \times 185 + 0.2 \times 178 = 181.6$.

**Diễn giải**: cả 9 sai số đều *dương* (Bias = MAD = 11.96): trung bình động *luôn dự báo thấp hơn thực tế* khi dữ liệu có xu hướng tăng. Đây không phải ngẫu nhiên mà là hệ quả toán học: MA$_n$ phản ánh mức trung bình của $n$ kỳ trước, tức "trễ" khoảng $(n+1)/2$ kỳ so với mức hiện tại. Với xu hướng thật khoảng 5.93 thùng/tháng (tính ở mục 2.5) và $n=3$ thì độ trễ kỳ vọng $\approx 5.93 \times (3+1)/2 = 11.87$, rất sát Bias quan sát (11.96). Bài học: **trung bình động chỉ phù hợp với chuỗi nhu cầu đi ngang (ổn định)**; nếu có xu hướng thì phải dùng Holt hoặc hồi quy.

### 2.2. San bằng số mũ đơn (Simple Exponential Smoothing)

**Tại sao cần?** Trung bình động có hai điểm yếu: (1) phải lưu $n$ giá trị cho *mỗi* mã hàng, (2) coi $n$ kỳ gần nhất có trọng số bằng nhau rồi bỏ rơi hoàn toàn kỳ thứ $n+1$ một cách đột ngột. Brown (1950s, bài toán phụ tùng Hải quân với hàng trăm nghìn mã) cần phương pháp chỉ phải nhớ một con số mỗi mã và có trọng số giảm dần êm ái theo độ cũ của dữ liệu.

$$F_{t+1} = \alpha \times Y_t + (1-\alpha) \times F_t$$

- $F_{t+1}$ = dự báo cho kỳ tiếp theo; $Y_t$ = thực tế kỳ hiện tại; $F_t$ = dự báo đã có cho kỳ hiện tại.
- $\alpha$ = hệ số san bằng (Smoothing constant), $0 < \alpha < 1$.

**Cách đọc công thức**: dự báo mới = dự báo cũ + một phần sai số vừa mắc phải, tức $F_{t+1} = F_t + \alpha(Y_t - F_t)$. Nếu dự báo thấp hơn thực tế thì nâng dự báo lên; $\alpha$ quyết định "tin vào sai số vừa rồi bao nhiêu". Khai triển ra, trọng số của dữ liệu cách đây $k$ kỳ là $\alpha(1-\alpha)^k$, giảm theo cấp số nhân (nên có tên "số mũ"):

| Độ cũ của dữ liệu | $\alpha = 0.1$ | $\alpha = 0.3$ | $\alpha = 0.7$ |
|---|---|---|---|
| Kỳ gần nhất ($k=0$) | 0.100 | 0.300 | 0.700 |
| 1 kỳ trước | 0.090 | 0.210 | 0.210 |
| 2 kỳ trước | 0.081 | 0.147 | 0.063 |
| 3 kỳ trước | 0.073 | 0.103 | 0.019 |

**Chọn $\alpha$**: $\alpha$ cao (gần 1) phản ứng nhanh nhưng nhạy với nhiễu; $\alpha$ thấp (gần 0) mượt nhưng chậm. Thực hành: thử nhiều giá trị $\alpha$ (0.1 đến 0.9) trên dữ liệu lịch sử và chọn giá trị làm MAD hoặc MSE nhỏ nhất (Excel Solver làm được việc này).

**Khởi tạo**: cần giá trị $F_1$ ban đầu; cách đơn giản là đặt $F_1 = Y_1$ (hoặc trung bình vài kỳ đầu).

#### Áp dụng trên bộ dữ liệu mẫu với $\alpha = 0.3$ và $\alpha = 0.7$ (từng bước)

Đặt $F_1 = Y_1 = 120$. Với $\alpha = 0.3$: $F_2 = 0.3 \times 120 + 0.7 \times 120 = 120$; $e_2 = 132-120 = 12$; $F_3 = 0.3 \times 132 + 0.7 \times 120 = 123.6$; $e_3 = 128 - 123.6 = 4.4$; $F_4 = 0.3 \times 128 + 0.7 \times 123.6 = 124.92$... Kết quả đầy đủ:

| Tháng | $Y$ | $F$ ($\alpha=0.3$) | $e$ | $F$ ($\alpha=0.7$) | $e$ |
|---|---|---|---|---|---|
| 2 | 132 | 120.00 | 12.00 | 120.00 | 12.00 |
| 3 | 128 | 123.60 | 4.40 | 128.40 | -0.40 |
| 4 | 141 | 124.92 | 16.08 | 128.12 | 12.88 |
| 5 | 150 | 129.74 | 20.26 | 137.14 | 12.86 |
| 6 | 147 | 135.82 | 11.18 | 146.14 | 0.86 |
| 7 | 160 | 139.17 | 20.83 | 146.74 | 13.26 |
| 8 | 172 | 145.42 | 26.58 | 156.02 | 15.98 |
| 9 | 165 | 153.40 | 11.60 | 167.21 | -2.21 |
| 10 | 178 | 156.88 | 21.12 | 165.66 | 12.34 |
| 11 | 185 | 163.21 | 21.79 | 174.30 | 10.70 |
| 12 | 181 | 169.75 | 11.25 | 181.79 | -0.79 |
| **Tổng sai số** | | | **177.08** | | **87.48** |

Dự báo tháng 13: $F_{13}(\alpha=0.3) = 0.3 \times 181 + 0.7 \times 169.75 = 173.12$; $F_{13}(\alpha=0.7) = 181.24$.

**Tóm tắt chỉ số trên cùng 11 kỳ (tháng 2-12)**:

| $\alpha$ | MAD | MSE | RMSE | MAPE | Bias | Tracking Signal |
|---|---|---|---|---|---|---|
| 0.1 | 27.46 | 879.83 | 29.66 | 16.76% | +27.46 | +11.0 |
| 0.3 | 16.10 | 298.12 | 17.27 | 10.04% | +16.10 | +11.0 |
| 0.7 | 8.57 | 107.23 | 10.36 | 5.43% | +7.95 | +10.2 |

**Diễn giải**: (1) $\alpha$ càng cao thì sai số càng thấp *trên bộ dữ liệu này*, vì dữ liệu có xu hướng nên cần "chạy theo" dữ liệu mới nhanh. Nếu dữ liệu chỉ đi ngang kèm nhiễu thì $\alpha$ thấp mới tốt hơn. (2) Dù $\alpha$ nào, Bias vẫn dương và Tracking Signal $\approx 10-11$ (vượt xa ngưỡng ±4): san bằng số mũ đơn cũng "trễ" khi có xu hướng, giống trung bình động. Cách chữa không phải là tăng $\alpha$ mãi mà là thêm thành phần xu hướng (Holt, mục 2.3).

### 2.3. San bằng số mũ điều chỉnh xu hướng (Holt - Double Exponential Smoothing)

**Tại sao cần?** Như đã thấy, hai phương pháp trên luôn trễ khi nhu cầu có xu hướng. Holt (1957) giải quyết bằng cách theo dõi *hai* đại lượng: mức hiện tại (Level $L$) và độ dốc (Trend $T$ - mỗi kỳ tăng/giảm bao nhiêu), mỗi đại lượng có hệ số san bằng riêng.

$$L_t = \alpha Y_t + (1-\alpha)(L_{t-1} + T_{t-1})$$
$$T_t = \beta (L_t - L_{t-1}) + (1-\beta) T_{t-1}$$
$$F_{t+h} = L_t + h \times T_t$$

- $L_t$ = mức đã san bằng; $T_t$ = độ dốc đã san bằng (số đơn vị tăng thêm mỗi kỳ); $\beta$ = hệ số san bằng cho xu hướng; $h$ = số kỳ dự báo phía trước.
- Dòng 1: mức mới = pha trộn giữa quan sát mới và "mức cũ cộng thêm đà tăng". Dòng 2: độ dốc mới = pha trộn giữa độ dốc vừa quan sát được ($L_t - L_{t-1}$) và độ dốc cũ.

#### Áp dụng trên bộ dữ liệu mẫu ($\alpha=0.5$, $\beta=0.3$)

Khởi tạo $L_1 = Y_1 = 120$, $T_1 = (Y_4 - Y_1)/3 = (141-120)/3 = 7$ (lấy độ dốc trung bình 3 kỳ đầu thay vì chỉ $Y_2 - Y_1 = 12$ vì một cặp quan sát đơn lẻ dễ bị nhiễu; nếu dùng 12 thì mô hình dự báo vượt thực tế nhiều hơn, Tracking Signal $= -8.1$).

Bước tháng 2: $F_2 = L_1 + T_1 = 127$; thực tế 132, $e_2 = 5$. Cập nhật: $L_2 = 0.5 \times 132 + 0.5 \times 127 = 129.5$; $T_2 = 0.3 \times (129.5 - 120) + 0.7 \times 7 = 2.85 + 4.9 = 7.75$. Bước tháng 3: $F_3 = 129.5 + 7.75 = 137.25$; thực tế 128, $e_3 = -9.25$...

| Tháng | $Y$ | $F=L_{t-1}+T_{t-1}$ | $e$ | $L_t$ | $T_t$ |
|---|---|---|---|---|---|
| 2 | 132 | 127.00 | 5.00 | 129.50 | 7.75 |
| 3 | 128 | 137.25 | -9.25 | 132.62 | 6.36 |
| 4 | 141 | 138.99 | 2.01 | 139.99 | 6.66 |
| 5 | 150 | 146.66 | 3.34 | 148.33 | 7.17 |
| 6 | 147 | 155.49 | -8.49 | 151.25 | 5.89 |
| 7 | 160 | 157.14 | 2.86 | 158.57 | 6.32 |
| 8 | 172 | 164.89 | 7.11 | 168.45 | 7.39 |
| 9 | 165 | 175.83 | -10.83 | 170.42 | 5.76 |
| 10 | 178 | 176.18 | 1.82 | 177.09 | 6.04 |
| 11 | 185 | 183.12 | 1.88 | 184.06 | 6.32 |
| 12 | 181 | 190.38 | -9.38 | 185.69 | 4.91 |

- Kết quả trên 11 kỳ: MAD $= 5.63$; MSE $= 42.62$; RMSE $= 6.53$; MAPE $= 3.65\%$; Bias $= -1.27$; Tracking Signal $= -2.47$ (trong ±4).
- Dự báo: $F_{13} = L_{12} + T_{12} = 185.69 + 4.91 = 190.60$; $F_{14} = 185.69 + 2 \times 4.91 = 195.51$.

**Diễn giải**: so với SES $\alpha=0.7$ (MAD 8.57, MAPE 5.43%, TS $+10.2$), Holt giảm MAD khoảng 34% và đưa Tracking Signal về vùng an toàn. Sai số không còn một chiều (có dương có âm) - dấu hiệu mô hình đã nắm được xu hướng.

### 2.4. Holt-Winters (San bằng số mũ ba tham số)

**Tại sao cần?** Holt chưa xử lý được mùa vụ: kem, nước giải khát, bánh Trung thu, hàng Tết có đỉnh và đáy lặp lại hằng năm. Winters (1960) thêm tham số thứ ba $\gamma$ để theo dõi *chỉ số mùa vụ* $s$ cho từng vị trí trong chu kỳ (chu kỳ có $p$ kỳ: $p=12$ cho dữ liệu tháng, $p=4$ cho quý, $p=7$ cho ngày trong tuần).

Dạng nhân (Multiplicative), phù hợp khi biên độ mùa vụ tỷ lệ với quy mô:

$$L_t = \alpha \frac{Y_t}{s_{t-p}} + (1-\alpha)(L_{t-1} + T_{t-1})$$
$$T_t = \beta (L_t - L_{t-1}) + (1-\beta) T_{t-1}$$
$$s_t = \gamma \frac{Y_t}{L_t} + (1-\gamma) s_{t-p}$$
$$F_{t+h} = (L_t + h T_t) \times s_{t+h-p}$$

Ý nghĩa: dòng đầu chia $Y_t$ cho chỉ số mùa vụ cũ để "gỡ mùa vụ" trước khi cập nhật mức; dòng cuối nhân lại chỉ số mùa vụ của đúng kỳ cần dự báo.

**Ví dụ một bước (giả định minh họa)**: $L_{t-1}=500$, $T_{t-1}=5$, $s_{t-p}=1.2$ (kỳ cao điểm), $Y_t=630$, $\alpha=0.3$, $\beta=0.1$, $\gamma=0.2$.
- Dự báo trước đó cho kỳ này: $(500+5) \times 1.2 = 606$; thực tế 630 (cao hơn 24).
- $L_t = 0.3 \times 630/1.2 + 0.7 \times 505 = 157.5 + 353.5 = 511.0$.
- $T_t = 0.1 \times (511 - 500) + 0.9 \times 5 = 5.6$.
- $s_t = 0.2 \times 630/511 + 0.8 \times 1.2 = 0.2466 + 0.96 = 1.2066$ (chỉ số mùa vụ nhích nhẹ lên vì kỳ này bán tốt hơn dự kiến).
- Nếu kỳ kế tiếp có chỉ số mùa vụ 0.9: $F = (511 + 5.6) \times 0.9 = 464.94$.

**Yêu cầu dữ liệu**: tối thiểu 2 đến 3 chu kỳ mùa vụ đầy đủ (ví dụ 24-36 tháng dữ liệu tháng) để ước lượng tham số khởi tạo. Với ít dữ liệu hơn, ước lượng mùa vụ không đáng tin (xem Case 9 phía sau, nơi cách phân rã đơn giản bằng Excel cho kết quả tốt hơn Holt khi chỉ có 24 tháng).

### 2.5. Phân tích hồi quy (Regression Analysis)

**Tại sao cần?** Các phương pháp chuỗi thời gian chỉ nhìn vào *lịch sử của chính biến doanh số*. Nhưng nhà quản lý thường muốn biết "nếu tôi tăng quảng cáo 2 triệu hay giảm giá 1.000 đồng thì doanh số đổi bao nhiêu?" - cần mô hình nhân quả (Causal). Hồi quy cho ra một công thức định lượng mối quan hệ đó.

#### Hồi quy tuyến tính đơn (Simple Linear Regression)

$$Y = a + bX$$

- $a$ = hệ số chặn (intercept): giá trị $Y$ khi $X=0$; $b$ = hệ số góc (slope): $Y$ thay đổi bao nhiêu khi $X$ tăng 1 đơn vị.
- Ước lượng bằng **phương pháp bình phương nhỏ nhất (Ordinary Least Squares - OLS)**: chọn đường thẳng làm *tổng bình phương sai số* nhỏ nhất. Lý do bình phương: sai số dương và âm không triệt tiêu nhau, đồng thời phạt nặng sai số lớn, và cho công thức đóng (không cần thử sai).

$$b = \frac{n\sum XY - \sum X \sum Y}{n\sum X^2 - (\sum X)^2}, \quad a = \bar{Y} - b\bar{X}$$

Khi $X$ là thời gian ($X = 1, 2, 3, \dots$) ta có **hồi quy xu hướng (trend regression)**.

**Áp dụng trên bộ dữ liệu mẫu ($X = t$)**: $n=12$, $\sum X = 78$, $\sum Y = 1859$, $\sum XY = 12932$, $\sum X^2 = 650$.
- $b = \dfrac{12 \times 12932 - 78 \times 1859}{12 \times 650 - 78^2} = \dfrac{155184 - 145002}{7800 - 6084} = \dfrac{10182}{1716} = 5.934$ thùng/tháng.
- $\bar{Y} = 1859/12 = 154.92$; $\bar{X} = 6.5$; $a = 154.92 - 5.934 \times 6.5 = 116.35$.
- Mô hình: $\hat{Y}_t = 116.35 + 5.934\,t$. Dự báo tháng 13: $116.35 + 5.934 \times 13 = 193.48$; tháng 14: $199.42$.
- Giá trị khớp (fitted) tháng 1 đến 12: 122.28; 128.22; 134.15; 140.08; 146.02; 151.95; 157.88; 163.82; 169.75; 175.68; 181.62; 187.55.

**Hệ số xác định $R^2$ (Coefficient of Determination)**: tỷ lệ biến động của $Y$ được mô hình giải thích: $R^2 = 1 - \dfrac{SSE}{SST}$ với $SSE = \sum(Y_t - \hat{Y}_t)^2$ (phần chưa giải thích) và $SST = \sum(Y_t - \bar{Y})^2$ (tổng biến động). Ở đây $SSE = 252.29$, $SST = 5286.92$ nên $R^2 = 1 - 0.0477 = 0.9523$: thời gian giải thích 95.2% biến động doanh số. Sai số chuẩn của hồi quy $s_e = \sqrt{SSE/(n-2)} = \sqrt{25.23} = 5.02$ thùng; khoảng dự báo xấp xỉ $\pm 2 s_e \approx \pm 10$ thùng, tức tháng 13 nằm trong khoảng 183 đến 203 thùng.

**Cảnh báo**: sai số "trong mẫu" của hồi quy (MAD 4.11, MAPE 2.66%) *không so sánh công bằng được* với sai số dự báo "ngoài mẫu" của MA/SES/Holt ở trên, vì đường hồi quy đã được "nhìn thấy" cả 12 điểm khi ước lượng. Để so sánh đúng cần backtesting (mục 2.7). Hồi quy xu hướng cũng giả định xu hướng tuyến tính mãi mãi, không tự thích nghi như Holt.

#### Hồi quy đa biến (Multiple Regression)

$$Y = a + b_1X_1 + b_2X_2 + ... + b_kX_k$$

**Ví dụ (giả định minh họa)**: 8 cửa hàng/kỳ, $X_1$ = giá bán (nghìn đồng), $X_2$ = chi phí quảng cáo (triệu đồng), $Y$ = số lượng bán:

| Quan sát | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Giá $X_1$ | 30 | 28 | 32 | 27 | 29 | 31 | 26 | 30 |
| Quảng cáo $X_2$ | 5 | 8 | 4 | 10 | 7 | 5 | 12 | 9 |
| Số lượng $Y$ | 258 | 304 | 237 | 340 | 291 | 248 | 377 | 313 |

Ước lượng bình phương nhỏ nhất (tính bằng Python/Excel LINEST): $\hat{Y} = 308.12 - 4.14 X_1 + 14.46 X_2$, $R^2 = 0.9962$, $R^2$ hiệu chỉnh $= 0.9947$. Diễn giải: giá tăng 1 nghìn thì lượng bán giảm trung bình 4.14 đơn vị (giữ nguyên quảng cáo); thêm 1 triệu quảng cáo thì tăng 14.46 đơn vị (giữ nguyên giá). Dự báo với giá 29 nghìn, quảng cáo 8 triệu: $308.12 - 4.14 \times 29 + 14.46 \times 8 = 303.75$ đơn vị. So sánh: hồi quy chỉ với quảng cáo có $R^2 = 0.9903$, nghĩa là thêm biến giá chỉ cải thiện 0.6 điểm phần trăm: nếu thu thập biến thứ hai tốn kém, đáng cân nhắc.

**Cảnh báo overfitting**: thêm biến luôn làm $R^2$ tăng, kể cả biến vô nghĩa; với 8 quan sát và 3 tham số, mô hình dễ "học thuộc" nhiễu. Dùng $R^2$ hiệu chỉnh, kiểm tra dấu của hệ số có hợp lý kinh doanh không (giá tăng mà bán nhiều hơn là dấu hiệu sai), và đánh giá trên dữ liệu chưa dùng để ước lượng. Quy tắc kinh nghiệm: có ít nhất 10-15 quan sát cho mỗi biến độc lập.

### 2.6. Phân rã chuỗi thời gian và chỉ số mùa vụ (Seasonal Index)

**Tại sao cần?** Khi doanh số quý 3 cao hơn quý 1, ta cần biết đó là do doanh nghiệp đang lớn lên (xu hướng) hay chỉ do mùa. Chỉ số mùa vụ trả lời: "quý này thường cao/thấp hơn mức trung bình bao nhiêu lần". Chỉ số bằng 1.20 nghĩa là kỳ đó thường cao hơn trung bình 20%.

**Ví dụ (giả định minh họa) - doanh số theo quý của một dòng sản phẩm giải khát, đơn vị: nghìn thùng**:

| Năm | Q1 | Q2 | Q3 | Q4 | Tổng năm |
|---|---|---|---|---|---|
| 1 | 80 | 120 | 150 | 90 | 440 |
| 2 | 88 | 132 | 162 | 98 | 480 |
| 3 | 95 | 141 | 177 | 106 | 519 |
| **Trung bình quý** | 87.67 | 131.00 | 163.00 | 98.00 | |

Trung bình chung $= 1439/12 = 119.92$ (với tổng 3 năm $= 440+480+519 = 1439$). Chỉ số mùa vụ $S_q = $ trung bình quý $/$ trung bình chung:

| Quý | Q1 | Q2 | Q3 | Q4 | Tổng |
|---|---|---|---|---|---|
| Chỉ số mùa vụ $S$ | 0.731 | 1.092 | 1.359 | 0.817 | 4.000 |

Tổng 4 chỉ số bằng 4 (số kỳ trong chu kỳ) là điều kiện kiểm tra. **Quy trình dự báo bằng phân rã (Decomposition)**:
1. Tính chỉ số mùa vụ $S$ như trên.
2. **Gỡ mùa vụ (Deseasonalize)**: $Y^{adj} = Y / S$. Chuỗi gỡ mùa vụ của 3 năm (làm tròn 1 chữ số thập phân): năm 1: 109.4; 109.8; 110.4; 110.1; năm 2: 120.4; 120.8; 119.2; 119.9; năm 3: 129.9; 129.1; 130.2; 129.7 - quan sát được xu hướng tăng đều, không còn "răng cưa".
3. Hồi quy xu hướng trên chuỗi đã gỡ: $\hat{Y}^{adj}_t = 105.52 + 2.215\,t$ ($t = 1 \dots 12$).
4. **Dự báo** $= \hat{Y}^{adj}_t \times S$. Năm 4: $t=13$: $(105.52 + 2.215 \times 13) \times 0.731 = 98.2$; Q2: $(105.52 + 2.215 \times 14) \times 1.092 = 149.1$; Q3: $188.6$; Q4: $115.2$ nghìn thùng; tổng năm 4 $\approx 551.1$ nghìn thùng (tăng 6.2% so với năm 3).

Dùng chỉ số mùa vụ thay vì lấy "bằng cùng kỳ năm trước" giúp tránh việc lặp lại cả phần nhiễu ngẫu nhiên của năm đó.

### 2.7. Đo lường sai số dự báo (Forecast Error Measurement)

**Tại sao cần nhiều chỉ số?** Vì mỗi chỉ số trả lời một câu hỏi khác nhau:
- Sai số trung bình lớn cỡ nào *theo đơn vị hàng*? (MAD, RMSE) - dùng để tính tồn kho an toàn.
- Sai số lớn cỡ nào *theo %*? (MAPE) - để so sánh giữa sản phẩm có quy mô khác nhau.
- Có sai số *thiên lệch một chiều* (luôn thừa hoặc luôn thiếu) không? (Bias, Tracking Signal) - dấu hiệu mô hình sai cấu trúc.

Ký hiệu sai số mỗi kỳ: $e_t = Y_t - F_t$ (thực tế trừ dự báo; $e>0$ nghĩa là dự báo thấp hơn thực tế).

| Chỉ số | Công thức | Ý nghĩa |
|---|---|---|
| MAD (Mean Absolute Deviation) | $\frac{\sum \lvert Y_t - F_t \rvert}{n}$ | Sai số tuyệt đối trung bình, cùng đơn vị với dữ liệu gốc; dễ hiểu nhất |
| MSE (Mean Squared Error) | $\frac{\sum (Y_t - F_t)^2}{n}$ | Phạt nặng các sai số lớn do bình phương; đơn vị là bình phương nên khó diễn giải trực tiếp |
| RMSE (Root MSE) | $\sqrt{MSE}$ | Đưa MSE về đơn vị gốc; liên hệ trực tiếp với độ lệch chuẩn sai số, dùng trong công thức Safety Stock |
| MAPE (Mean Absolute Percentage Error) | $\frac{1}{n}\sum \left\lvert \frac{Y_t-F_t}{Y_t} \right\rvert \times 100\%$ | Sai số theo %, dễ so sánh giữa các sản phẩm/quy mô khác nhau |
| Bias (Độ lệch trung bình) | $\frac{\sum (Y_t - F_t)}{n}$ | Phát hiện xu hướng dự báo thừa/thiếu hệ thống (không chỉ độ lớn sai số) |

**Quan hệ giữa MAD và RMSE**: nếu sai số xấp xỉ phân phối chuẩn thì $RMSE \approx 1.25 \times MAD$ (vì $\sqrt{\pi/2} \approx 1.2533$). Ví dụ trên dữ liệu MA3: $1.25 \times 11.96 = 14.95$ so với RMSE thực $12.88$ (không khớp lắm vì chỉ có 9 điểm và sai số không chuẩn). Nếu RMSE lớn hơn nhiều lần MAD nghĩa là có vài sai số rất lớn (ngoại lệ).

**Hạn chế của MAPE**: không xác định khi $Y_t = 0$ (hàng bán chậm, nhiều ngày bằng 0) và thiên về phạt dự báo *quá cao* hơn dự báo *quá thấp*. Với hàng bán rời rạc có thể dùng WAPE $= \sum|e_t| / \sum Y_t$, sMAPE hoặc MASE (do Hyndman và Koehler đề xuất năm 2006).

**Bảng đánh giá nhanh độ chính xác dựa trên MAPE** (ngưỡng tham khảo, tùy ngành):

| MAPE | Đánh giá |
|---|---|
| < 10% | Dự báo rất chính xác |
| 10-20% | Dự báo tốt |
| 20-50% | Dự báo chấp nhận được |
| > 50% | Dự báo kém, cần xem xét lại phương pháp/dữ liệu |

**Backtesting (kiểm định ngược)**: để so sánh công bằng, chia dữ liệu thành phần *huấn luyện* (ước lượng tham số) và phần *kiểm tra* (giấu đi, dự báo rồi so với thực tế). Chọn phương pháp theo sai số trên phần kiểm tra, không phải phần huấn luyện.

#### Tổng hợp so sánh trên bộ dữ liệu mẫu 12 tháng

| Phương pháp | Cửa sổ đo | MAD | RMSE | MAPE | Bias | Nhận xét |
|---|---|---|---|---|---|---|
| MA3 | tháng 4-12 (9 kỳ) | 11.96 | 12.88 | 7.37% | +11.96 | Luôn dự báo thấp (trễ xu hướng) |
| WMA (0.5/0.3/0.2) | tháng 4-12 (9 kỳ) | 10.12 | 11.57 | 6.24% | +10.12 | Tốt hơn MA3 nhẹ, vẫn trễ |
| SES $\alpha=0.3$ | tháng 2-12 (11 kỳ) | 16.10 | 17.27 | 10.04% | +16.10 | Trễ nhiều nhất khi $\alpha$ thấp |
| SES $\alpha=0.7$ | tháng 2-12 (11 kỳ) | 8.57 | 10.36 | 5.43% | +7.95 | Tốt hơn nhờ phản ứng nhanh |
| Holt ($\alpha=0.5$, $\beta=0.3$) | tháng 2-12 (11 kỳ) | 5.63 | 6.53 | 3.65% | -1.27 | Tốt nhất trong nhóm ngoài mẫu; Bias gần 0 |

(Các cửa sổ đo khác nhau do MA3 cần 3 kỳ khởi động; để so sánh nghiêm ngặt hơn nên đo trên cùng cửa sổ - trên tháng 4-12, SES $\alpha=0.7$ có MAD 9.10 và MAPE 5.60%, vẫn kém Holt.)

### 2.8. Tín hiệu theo dõi (Tracking Signal)

**Tại sao cần?** MAD chỉ cho biết sai số lớn đến đâu, không cho biết sai số có *cùng một chiều* hay không. Mô hình tốt cho sai số lúc dương lúc âm nên tổng sai số lũy kế gần 0; mô hình bị lệch (luôn thấp hoặc luôn cao) thì sai số cộng dồn trôi xa khỏi 0. Tracking Signal đo "tổng sai số lũy kế bằng bao nhiêu lần sai số trung bình" - một cảnh báo sớm (như đèn báo động) rằng mô hình cần xem lại.

$$TS = \frac{\sum (Y_t - F_t)}{MAD}$$

Nếu $TS$ vượt khoảng kiểm soát thường dùng (±4; một số tổ chức dùng ±3 đến ±6 tùy chi phí sai lệch), cần xem xét lại hoặc điều chỉnh mô hình.

**Ví dụ tính từng bước - SES $\alpha = 0.3$ trên bộ dữ liệu mẫu**: tổng sai số lũy kế và MAD lũy kế tại từng tháng:

| Tháng | $e$ | $\sum e$ | MAD lũy kế | TS |
|---|---|---|---|---|
| 2 | 12.00 | 12.00 | 12.00 | 1.0 |
| 3 | 4.40 | 16.40 | 8.20 | 2.0 |
| 4 | 16.08 | 32.48 | 10.83 | 3.0 |
| 5 | 20.26 | 52.74 | 13.19 | **4.0** |
| 6 | 11.18 | 63.92 | 12.78 | **5.0** |
| 7 | 20.83 | 84.74 | 14.12 | 6.0 |
| 12 | 11.25 | 177.08 | 16.10 | 11.0 |

Vì *tất cả* sai số đều dương nên $\sum e = n \times MAD$, tức TS tăng đều 1 đơn vị mỗi kỳ, chạm 4.0 ở tháng 5 và vượt ngưỡng ở tháng 6. **Diễn giải**: mô hình SES đơn bị "chặn đèn đỏ" chỉ sau 5-6 tháng; nếu doanh nghiệp theo dõi Tracking Signal hằng tháng thì sẽ đổi sang mô hình có xu hướng (Holt) sớm thay vì để thiếu hàng cả năm.

### 2.9. Phương pháp định tính: Delphi và dự báo hợp tác (CPFR)

#### Phương pháp Delphi (Delphi Method)

**Tại sao cần?** Với sản phẩm hoàn toàn mới, không có dữ liệu lịch sử, và họp nhóm trực tiếp thường bị chi phối bởi người nói to hoặc chức vị cao (groupthink). Delphi (RAND, những năm 1950-1960) thu thập ý kiến từ nhóm chuyên gia *ẩn danh*, qua nhiều vòng: mỗi vòng tổng hợp kết quả (trung vị, khoảng dao động) và gửi lại để chuyên gia xem xét điều chỉnh, cho đến khi đạt đồng thuận tương đối.

**Ví dụ (giả định minh họa)**: dự báo lượng bán tháng đầu của một thiết bị mới, 5 chuyên gia (đơn vị/tháng):

| Vòng | Ý kiến các chuyên gia | Khoảng (min-max) | Trung vị | Trung bình |
|---|---|---|---|---|
| 1 | 200; 350; 500; 300; 800 | 200-800 | 350 | 430 |
| 2 | 300; 380; 450; 350; 550 | 300-550 | 380 | 406 |
| 3 | 350; 380; 420; 360; 450 | 350-450 | 380 | 392 |

Khoảng dao động thu hẹp từ 600 xuống 100 đơn vị; trung vị ổn định ở 380 - dùng làm dự báo định tính (kèm khoảng 350-450 để thể hiện độ bất định). Chuyên gia có ý kiến cực đoan (800) được yêu cầu nêu lý do và đa số đã hiệu chỉnh.

#### Hoạch định hợp tác dự báo (CPFR)

Đã đề cập ở file 03, CPFR mở rộng dự báo ra ngoài phạm vi nội bộ, tích hợp dữ liệu và nhận định từ đối tác chuỗi cung ứng (nhà bán lẻ, nhà phân phối) để dự báo chính xác hơn dự báo đơn lẻ từng bên và hạn chế hiệu ứng Bullwhip.

### 2.10. Phương pháp nâng cao: ARIMA, Prophet, Machine Learning và dữ liệu thay thế

#### ARIMA (AutoRegressive Integrated Moving Average)

**Tại sao cần?** Các mô hình san bằng số mũ mô tả dữ liệu bằng "mức - xu hướng - mùa vụ", nhưng nhiều chuỗi có cấu trúc tự tương quan phức tạp mà ba thành phần đó không bắt được. Box và Jenkins (1970) đưa ra khung ARIMA kết hợp ba thành phần: **AR** (tự hồi quy: giá trị hiện tại phụ thuộc giá trị quá khứ), **I** (sai phân - Integrated: lấy hiệu liên tiếp để biến chuỗi không dừng thành chuỗi dừng) và **MA** (phụ thuộc vào sai số dự báo quá khứ). Ký hiệu ARIMA$(p,d,q)$ với $p, d, q$ là bậc tương ứng. Chọn tham số thường dựa vào biểu đồ ACF/PACF hoặc thuật toán tự động (auto.arima trong R, pmdarima trong Python). Đòi hỏi kiến thức thống kê và chuỗi đủ dài.

#### Prophet (Meta/Facebook)

Công cụ mã nguồn mở (2017) dành cho dữ liệu kinh doanh có nhiều mùa vụ chồng chéo (theo tuần, theo năm), ngày lễ đặc biệt, chịu tốt dữ liệu thiếu và ngoại lệ; thiết kế để người không chuyên thống kê vẫn dùng được và điều chỉnh bằng kiến thức nghiệp vụ (ví dụ nhập danh sách ngày lễ, Tết).

#### Học máy: Random Forest, Gradient Boosting (XGBoost, LightGBM), mạng nơ-ron (LSTM)

Phù hợp khi có hàng nghìn SKU và nhiều biến đầu vào (giá, khuyến mãi, thời tiết, lịch sự kiện, dữ liệu vị trí) mà mô hình thống kê truyền thống khó xử lý đồng thời.

**Bằng chứng thực nghiệm (theo tổng kết công bố của ban tổ chức các cuộc thi; người đọc nên đối chiếu nguồn gốc)**: cuộc thi M4 (2018, 100.000 chuỗi) cho thấy các phương pháp học máy "thuần" kém hơn nhiều mô hình thống kê; đội thắng cuộc dùng mô hình lai (kết hợp san bằng số mũ với mạng nơ-ron) và các tổ hợp (ensemble) nhiều mô hình thống kê cũng rất mạnh. Cuộc thi M5 (2020, dữ liệu bán lẻ có phân cấp, có giá, khuyến mãi, sự kiện) lại cho thấy các mô hình học máy dựa trên cây quyết định tăng cường (LightGBM) dẫn đầu. Kết luận cân bằng: **ML thắng khi có nhiều dữ liệu và nhiều biến giải thích chất lượng tốt; phương pháp đơn giản vẫn cạnh tranh khi chuỗi ngắn, ít biến, hoặc nguồn lực kỹ thuật hạn chế**. Tổ hợp (trung bình) nhiều mô hình đơn giản thường là lựa chọn an toàn.

#### Dữ liệu thay thế (Alternative Data)

| Nguồn dữ liệu thay thế | Ứng dụng |
|---|---|
| Google Trends | Phát hiện sớm xu hướng tìm kiếm tăng/giảm cho sản phẩm/dịch vụ |
| Dữ liệu mạng xã hội (lượt đề cập, sentiment) | Dự báo xu hướng thời trang, sản phẩm viral |
| Dữ liệu thời tiết | Điều chỉnh dự báo cho sản phẩm nhạy cảm thời tiết (đồ uống, quần áo mùa) |
| Dữ liệu vệ tinh (lưu lượng bãi đỗ xe) | Ước lượng doanh số bán lẻ gần thời gian thực (thường dùng bởi các quỹ đầu tư) |
| Dữ liệu giao dịch thẻ tổng hợp | Ước lượng xu hướng tiêu dùng ngành gần thời gian thực |

#### Khi nào nên dừng đầu tư vào độ phức tạp?

Sai lầm phổ biến khi chuyển đổi số là cho rằng mô hình càng phức tạp càng chính xác. Cải thiện độ chính xác thường không tương xứng với chi phí và độ phức tạp tăng thêm, đặc biệt khi: (1) dữ liệu lịch sử ngắn (dưới 2-3 năm); (2) có hàng nghìn SKU mà không đủ nguồn lực tinh chỉnh từng mô hình; (3) thị trường có biến động cấu trúc thường xuyên khiến mô hình phức tạp dễ overfitting vào quá khứ không còn phù hợp. **Khuyến nghị**: SME bắt đầu với san bằng số mũ, Holt hoặc phân rã mùa vụ bằng Excel; chỉ đầu tư ML khi đã có nền tảng dữ liệu vững, đội ngũ duy trì được mô hình và đã chứng minh được lợi ích tài chính đo được bằng tiền (giảm tồn kho, giảm hết hàng).

### 2.11. So sánh ưu - nhược điểm các phương pháp

| Phương pháp | Ưu điểm | Nhược điểm | Độ phức tạp | Yêu cầu dữ liệu |
|---|---|---|---|---|
| Trung bình động | Đơn giản, dễ tính toán | Trễ khi có xu hướng, phải lưu lịch sử | Rất thấp | Vài kỳ gần nhất |
| San bằng số mũ đơn | Chỉ cần lưu 1 giá trị, dễ tự động hoá | Cần chọn $\alpha$; trễ khi có xu hướng; không xử lý mùa vụ | Thấp | Ngắn |
| Holt | Xử lý được xu hướng, Bias gần 0 | Cần chọn $\alpha, \beta$ và khởi tạo; không có mùa vụ | Thấp-Trung bình | Vài chục kỳ |
| Holt-Winters | Xử lý cả xu hướng và mùa vụ | Phức tạp hơn, cần 2-3 chu kỳ mùa vụ | Trung bình | 2-3 chu kỳ mùa vụ |
| Phân rã + hồi quy xu hướng | Dễ làm trong Excel, dễ giải thích với chủ doanh nghiệp | Xu hướng tuyến tính cố định; cần cập nhật định kỳ | Thấp-Trung bình | 2 chu kỳ trở lên |
| Hồi quy đa biến | Giải thích quan hệ nhân quả, trả lời câu hỏi "nếu...thì" | Cần dữ liệu biến độc lập, rủi ro overfitting | Trung bình-Cao | Biến độc lập đầy đủ, chất lượng |
| ARIMA | Bắt được cấu trúc tự tương quan | Cần chuyên môn chọn tham số | Cao | Chuỗi dài, tương đối ổn định |
| Machine Learning | Xử lý nhiều biến và nhiều SKU cùng lúc | Dễ overfitting, tốn hạ tầng, khó giải thích | Rất cao | Dữ liệu lớn, nhiều biến |
| Định tính (Delphi, chuyên gia) | Dùng được khi thiếu dữ liệu, tích hợp thông tin định tính | Chủ quan, tốn thời gian, khó lượng hoá độ tin cậy | Thấp | Không cần dữ liệu số |

**Dự báo tổng hợp vs chi tiết (theo Risk Pooling)**:

| Tiêu chí | Dự báo tổng hợp (Aggregate) | Dự báo chi tiết (từng SKU/khu vực) |
|---|---|---|
| Độ chính xác | Cao hơn (nhờ gộp rủi ro) | Thấp hơn, biến động lớn hơn |
| Mức độ chi tiết hữu ích | Thấp - phù hợp hoạch định tổng thể, năng lực | Cao - cần thiết cho đặt hàng, tồn kho cụ thể |
| Khuyến nghị | Dự báo tổng hợp trước, sau đó phân bổ (top-down) theo tỷ trọng lịch sử | Kết hợp dữ liệu POS thời gian thực để điều chỉnh |

---

## III. Case Studies thực tế

> **Lưu ý về nguồn số liệu**: Các case về doanh nghiệp thật (Case 1-4, 8) chỉ dùng thông tin mô tả khái quát ở mức công khai phổ biến; mọi con số tính toán trong các case này là **giả định minh họa** để giải thích kỹ thuật, không phải số liệu nội bộ của doanh nghiệp. Các case SME (Case 6, 7, 9) và case thất bại (Case 5) có số liệu tự thiết kế, tính toán đã kiểm tra bằng Python.

### Case 1: Walmart - Dự báo nhu cầu tích hợp thời tiết và sự kiện (quốc tế, thành công)

#### Bối cảnh
Walmart vận hành hàng nghìn cửa hàng với nhu cầu chịu ảnh hưởng mạnh bởi yếu tố bên ngoài: thời tiết (bão, nắng nóng), sự kiện thể thao, ngày lễ địa phương. Câu chuyện thường được kể (qua báo chí và sách về dữ liệu lớn; con số cụ thể chưa được kiểm chứng ở đây) là trước khi có bão, doanh số một số mặt hàng ăn liền như bánh Pop-Tarts tăng vọt bất thường - điều mà mô hình chuỗi thời gian thuần dựa trên lịch sử bán hàng không thể "nhìn thấy" trước.

#### Vấn đề kinh doanh
Dự báo chuỗi thời gian chỉ biết "tuần này giống các tuần trước", nên bỏ lỡ cú sốc nhu cầu do sự kiện bên ngoài. Cần mô hình nhân quả đưa các biến như cảnh báo bão, nhiệt độ, lịch sự kiện vào hồi quy (mục 2.5), và cần xác định *khi nào đáng để tăng tồn kho* khi bản thân dự báo thời tiết cũng bất định.

#### Phân tích định lượng minh họa (giả định minh họa)
Giả sử một cửa hàng bán trung bình 200 hộp bánh/ngày trong điều kiện bình thường. Khi có cảnh báo bão, mô hình hồi quy cho hệ số nhân nhu cầu 3.0 nên nhu cầu kỳ vọng nếu bão đổ bộ là $200 \times 3.0 = 600$ hộp, tức chênh $600 - 200 = 400$ hộp so với dự báo nền.
- **Chi phí thiếu hàng** (cho mỗi hộp bán thiếu): lợi nhuận gộp mất đi $0.45$ USD $\Rightarrow$ $C_u = 400 \times 0.45 = 180$ USD/cửa hàng/ngày.
- **Chi phí dư hàng** nếu bão không xảy ra (hàng tồn thừa, chiếm chỗ, giảm giá): $0.15$ USD mỗi hộp $\Rightarrow$ $C_o = 400 \times 0.15 = 60$ USD/cửa hàng.
- Gọi $p$ là xác suất bão thực sự đổ bộ (theo dự báo thời tiết). Nên tăng tồn kho khi chi phí kỳ vọng của việc không tăng lớn hơn chi phí kỳ vọng của việc tăng: $p \times 180 > (1-p) \times 60 \Rightarrow p > \dfrac{60}{180+60} = 0.25$.
- Với 500 cửa hàng trong vùng bão, thiếu hàng đồng loạt gây thất thoát khoảng $500 \times 180 = 90000$ USD/ngày.

#### Diễn giải kinh doanh
Kết quả cho thấy chỉ cần xác suất bão vượt 25% là nên chuẩn bị thêm, vì thiệt hại do thiếu hàng (180) gấp 3 lần thiệt hại do dư hàng (60). Dự báo vì thế không chỉ là "một con số kỳ vọng" mà còn gắn với *bất đối xứng chi phí* giữa dư và thiếu (cùng tư duy với mô hình Newsvendor ở file 04). Việc tích hợp dữ liệu bên ngoài cho từng cửa hàng thay vì một mô hình chung giúp khai thác khác biệt địa phương.

#### Bài học
1. Tích hợp biến nhân quả (thời tiết, sự kiện) vào mô hình khi chúng giải thích được biến động lớn mà lịch sử không giải thích được.
2. Quyết định đặt hàng phụ thuộc vào cả dự báo lẫn chi phí thiếu/dư, không chỉ độ chính xác điểm.
3. Mô hình chi tiết theo từng cửa hàng đòi hỏi hạ tầng dữ liệu mạnh; SME nên bắt đầu với vài biến quan trọng nhất.

### Case 2: Vinamilk - Dự báo mùa vụ ngắn hạn và dự báo dài hạn theo nhân khẩu học (Việt Nam, doanh nghiệp lớn)

#### Bối cảnh
Nhu cầu sữa và sản phẩm từ sữa biến động theo mùa (mùa hè tăng nhu cầu sữa chua, sữa lạnh, kem; dịp Tết tăng nhu cầu quà biếu) đồng thời chịu tác động dài hạn của nhân khẩu học (tỷ lệ sinh, đô thị hoá) và thu nhập. Đây là cấu trúc điển hình của một doanh nghiệp tiêu dùng nhanh: hai "chiếc đồng hồ" chạy ở hai tốc độ khác nhau. *(Mô tả khái quát; doanh nghiệp không công bố chi tiết mô hình nội bộ.)*

#### Vấn đề kinh doanh
Hai bài toán cần hai công cụ khác nhau: (1) lịch sản xuất và đặt nguyên liệu hàng tháng/quý cần dự báo *ngắn-trung hạn có mùa vụ* (Holt-Winters hoặc phân rã mùa vụ, mục 2.4 và 2.6); (2) quyết định đầu tư nhà máy cần dự báo *dài hạn* theo yếu tố vĩ mô (hồi quy, mục 2.5).

#### Phân tích định lượng minh họa (giả định minh họa)
**(a) Mùa vụ ngắn hạn.** Với dòng sản phẩm giải khát/sữa lạnh giả định ở mục 2.6 (3 năm dữ liệu quý), chỉ số mùa vụ là Q1 = 0.731, Q2 = 1.092, Q3 = 1.359, Q4 = 0.817. Dự báo năm 4: Q1 98.2; Q2 149.1; Q3 188.6; Q4 115.2 (nghìn thùng), tổng 551.1. Khoảng chênh giữa Q3 (đỉnh) và Q1 (đáy) là $188.6/98.2 = 1.92$ lần: nếu lập kế hoạch sản xuất đều theo trung bình $551.1/4 = 137.8$ nghìn thùng/quý thì Q3 thiếu $188.6 - 137.8 = 50.8$ nghìn thùng (phải dùng tồn kho tích sẵn từ Q1-Q2 hoặc tăng ca) còn Q1 dư $137.8 - 98.2 = 39.6$ nghìn thùng. Dự báo có mùa vụ cho phép lập kế hoạch tích trữ có chủ đích thay vì bị động.

**(b) Dài hạn theo vĩ mô.** Giả sử độ co giãn của nhu cầu sữa theo thu nhập bình quân là $0.8$ (nghĩa là thu nhập tăng 1% thì nhu cầu tăng 0.8%), GDP bình quân đầu người tăng 6%/năm, dân số tăng 0.9%/năm. Tăng trưởng nhu cầu ước tính $= 0.8 \times 6\% + 0.9\% = 5.7\%$/năm. Với chỉ số nhu cầu hiện tại là 100 và công suất 125 (tức đang sử dụng 80%), nếu quy định sử dụng tối đa 90% công suất ($112.5$) thì thời điểm cần có nhà máy mới: $100 \times 1.057^n = 112.5 \Rightarrow n = \ln(1.125)/\ln(1.057) = 2.12$ năm. Sau 5 năm nhu cầu đạt $100 \times 1.057^5 = 131.9$, tức tăng 31.9%.

#### Diễn giải kinh doanh
Nhà máy thường mất 18-30 tháng để xây dựng, nên mốc "2.1 năm" cho thấy cần quyết định đầu tư ngay bây giờ. Kết quả cũng chỉ ra độ nhạy: sai lệch nhỏ trong độ co giãn hoặc tăng trưởng thu nhập có thể dịch chuyển mốc đầu tư cả năm, vì vậy dự báo dài hạn nên chạy nhiều kịch bản (cơ sở, lạc quan, bi quan) thay vì một con số.

#### Bài học
- Phân tách rõ chân trời thời gian: mô hình mùa vụ cho vận hành, mô hình nhân quả vĩ mô cho đầu tư.
- Dự báo dài hạn nên có kịch bản và đánh giá độ nhạy, không nên chỉ một đường thẳng.

### Case 3: Coca-Cola - Dự báo theo khu vực kết hợp yếu tố kinh tế và sự kiện (quốc tế)

#### Bối cảnh
Coca-Cola hiện diện tại hơn 200 quốc gia và vùng lãnh thổ, nhu cầu chịu ảnh hưởng bởi khí hậu, thu nhập, thói quen văn hoá và các sự kiện thể thao lớn (World Cup, Olympic) mà hãng tài trợ. *(Mô tả khái quát; chi tiết mô hình nội bộ không được công bố.)*

#### Vấn đề kinh doanh
Một mô hình toàn cầu duy nhất không thể mô tả được cả thị trường nhiệt đới thu nhập thấp lẫn thị trường ôn đới thu nhập cao: quan hệ giữa nhiệt độ, thu nhập và tiêu thụ khác nhau. Cần mô hình hồi quy theo khu vực (regional model) cộng thêm điều chỉnh định tính từ đội ngũ thị trường địa phương.

#### Phân tích định lượng minh họa (giả định minh họa)
Giả sử mô hình hồi quy khu vực cho lượng tiêu thụ (lít/người/năm) là: $\hat{Y} = 5 + 1.2 \times \text{Nhiệt độ TB (°C)} + 0.002 \times \text{GDP bình quân (USD)}$.
- Thị trường A: 28°C, GDP bình quân 4000 USD: $5 + 1.2 \times 28 + 0.002 \times 4000 = 5 + 33.6 + 8 = 46.6$ lít/người/năm.
- Thị trường B: 12°C, GDP bình quân 40000 USD: $5 + 1.2 \times 12 + 0.002 \times 40000 = 5 + 14.4 + 80 = 99.4$ lít/người/năm.
- Sự kiện thể thao lớn làm tăng 8% nhu cầu trong năm đó ở thị trường A: $46.6 \times 1.08 = 50.3$ lít/người/năm.

#### Diễn giải kinh doanh
Ở A, yếu tố khí hậu đóng góp 33.6 trong 46.6 (72%), ở B thu nhập đóng góp 80 trong 99.4 (80%): *cùng một công thức, hai thị trường nhưng động lực khác nhau*, nên đội kế hoạch ở mỗi nơi cần theo dõi biến khác nhau. Cảnh báo: mô hình tuyến tính ngoại suy ngoài phạm vi dữ liệu (ví dụ GDP quá cao) dễ sai vì tiêu thụ có xu hướng bão hoà.

#### Bài học
1. Mô hình phân tán theo khu vực + biến địa phương thường chính xác hơn một mô hình chung.
2. Kết hợp dự báo định lượng với hiểu biết định tính của đội địa phương (sự kiện, văn hoá, khuyến mãi).
3. Cần kiểm tra ngoại suy: mô hình chỉ đáng tin trong vùng dữ liệu đã quan sát.

### Case 4: Grab - Dự báo nhu cầu di chuyển theo thời gian thực (khu vực, ứng dụng ML)

#### Bối cảnh
Nền tảng gọi xe có nhu cầu biến động cực nhanh theo giờ, thời tiết, sự kiện; thiếu xe cục bộ ở một khu vực trong khi nơi khác dư tài xế làm giảm trải nghiệm khách và thu nhập tài xế. *(Mô tả khái quát; không công bố chi tiết nội bộ.)*

#### Vấn đề kinh doanh
Cần dự báo ở độ phân giải không gian-thời gian rất cao (từng ô lưới địa lý nhỏ, theo từng khung 15-30 phút) và cập nhật gần thời gian thực. Với hàng nghìn ô lưới, mỗi ô nhiều biến đầu vào (lịch sử đặt xe, thời tiết, sự kiện, vị trí tài xế), phương pháp thủ công không khả thi nên dùng học máy (mục 2.10): đây là đúng loại bài toán có nhiều dữ liệu và nhiều biến mà ML phát huy ưu thế.

#### Phân tích định lượng minh họa (giả định minh họa, không phải công thức thực của Grab)
Một ô lưới trong khung giờ cao điểm: dự báo 120 yêu cầu/15 phút, nguồn cung 80 tài xế rảnh $\Rightarrow$ tỷ lệ cầu/cung $= 120/80 = 1.5$.
- Nếu sai số dự báo MAPE khoảng 15%, nhu cầu thực nằm khoảng $120 \times 0.85 = 102$ đến $120 \times 1.15 = 138$ yêu cầu, tương ứng tỷ lệ cầu/cung từ $102/80 = 1.275$ đến $138/80 = 1.725$.
- Giả sử một quy tắc định giá tăng đơn giản $m = 1 + 0.8 \times (\text{tỷ lệ} - 1)$: hệ số giá từ $1 + 0.8 \times 0.275 = 1.22$ đến $1 + 0.8 \times 0.725 = 1.58$.

#### Diễn giải kinh doanh
Ngay cả khi dự báo "khá tốt" (MAPE 15%), khoảng bất định về hệ số giá lớn (1.22 đến 1.58), nên hệ thống thực tế phải cập nhật liên tục theo thời gian thực và đặt giới hạn trên/dưới cho điều chỉnh. Độ chính xác dự báo không phải mục đích tự thân mà là cơ sở để cân bằng cung-cầu và thu nhập của tài xế.

#### Bài học
- ML phù hợp khi dữ liệu lớn, nhiều biến, cập nhật nhanh và có đội ngũ kỹ thuật duy trì mô hình.
- Luôn đi kèm biên độ sai số và cơ chế an toàn (giới hạn điều chỉnh).
- SME thường không có điều kiện này; nên áp dụng ý tưởng (chia nhỏ theo thời gian/khu vực, theo dõi cung-cầu) bằng công cụ đơn giản như bảng tính theo khung giờ.

### Case 5: Ngành bán lẻ thời trang truyền thống - Dự báo thất bại khi thị trường đổi cấu trúc (thất bại)

#### Bối cảnh
Nhiều nhà bán lẻ thời trang truyền thống dự báo hoàn toàn dựa trên lịch sử bán hàng (trung bình động, san bằng số mũ cơ bản) mà không tích hợp tín hiệu thị trường mới (mạng xã hội, thay đổi hành vi hậu COVID-19: chuyển từ cửa hàng sang online, xu hướng tiêu dùng bền vững).

#### Vấn đề kinh doanh
Khi xảy ra **biến động cấu trúc (Structural Break)** - nhu cầu nhảy sang một mức mới - mô hình lịch sử phải mất nhiều kỳ mới "học" mức mới. Trong thời gian đó doanh nghiệp tiếp tục đặt hàng theo mức cũ, gây tồn dư lớn.

#### Mô phỏng định lượng (giả định minh họa)
Một sản phẩm có nhu cầu ổn định quanh 1000 đơn vị/tháng trong 8 tháng, rồi đột ngột giảm xuống quanh 600 đơn vị (cú sốc mất 40% nhu cầu). Dùng SES với $\alpha=0.2$, $F_1 = Y_1 = 1000$.

| Tháng | Thực tế $Y$ | Dự báo $F$ | Sai số $e$ | $\sum e$ | MAD lũy kế | Tracking Signal |
|---|---|---|---|---|---|---|
| 2 | 1020 | 1000.0 | 20.0 | 20.0 | 20.0 | 1.00 |
| 3 | 985 | 1004.0 | -19.0 | 1.0 | 19.5 | 0.05 |
| 4 | 1010 | 1000.2 | 9.8 | 10.8 | 16.3 | 0.66 |
| 5 | 990 | 1002.2 | -12.2 | -1.4 | 15.2 | -0.09 |
| 6 | 1005 | 999.7 | 5.3 | 3.9 | 13.2 | 0.30 |
| 7 | 995 | 1000.8 | -5.8 | -1.9 | 12.0 | -0.16 |
| 8 | 1015 | 999.6 | 15.4 | 13.5 | 12.5 | 1.08 |
| **9** | **620** | 1002.7 | -382.7 | -369.2 | 58.8 | **-6.28** |
| 10 | 590 | 926.2 | -336.2 | -705.4 | 89.6 | -7.87 |
| 11 | 610 | 858.9 | -248.9 | -954.3 | 105.5 | -9.04 |
| 12 | 600 | 809.1 | -209.1 | -1163.4 | 114.9 | -10.12 |
| 13 | 615 | 767.3 | -152.3 | -1315.7 | 118.1 | -11.15 |
| 14 | 595 | 736.9 | -141.9 | -1457.6 | 119.9 | -12.16 |

#### Diễn giải kinh doanh
- Trong 7 tháng ổn định, Tracking Signal dao động quanh 0 (từ -0.16 đến +1.08): mô hình *hoạt động tốt*.
- Ngay tháng đầu tiên sau cú sốc, TS rơi xuống $-6.28$, vượt xa ngưỡng ±4: **chuông báo động reo ngay lập tức**. Nếu doanh nghiệp không theo dõi TS, họ sẽ thấy sai số lớn nhưng cho rằng "chỉ là một tháng xấu".
- Mô hình SES phục hồi chậm: sau 6 tháng dự báo vẫn là 736.9, cao hơn thực tế (595) khoảng 24%; dự báo tháng 15 vẫn 708.5. Tổng dư tích lũy 1457.6 đơn vị; với giá vốn giả định 200.000 đồng/đơn vị tương đương khoảng 291.5 triệu đồng hàng đặt thừa nếu đặt theo dự báo.
- Chữa: khi TS vượt ngưỡng, *đặt lại mô hình* (reset): lấy mức mới bằng trung bình vài tháng sau cú sốc (khoảng 600) thay vì chờ mô hình tự học dần.

#### Bài học
1. Dự báo định lượng thuần lịch sử có giới hạn nghiêm trọng khi có biến động cấu trúc.
2. Bắt buộc có Tracking Signal và quy trình phản ứng (ai quyết định reset, trong bao lâu).
3. Bổ sung tín hiệu định tính (xu hướng thị trường, phản hồi đội bán hàng, dữ liệu mạng xã hội) để phát hiện sớm sự thay đổi *trước khi* nó xuất hiện đầy đủ trong dữ liệu bán hàng.

### Case 6: Cửa hàng thời trang online (SME Việt Nam) - Đặt thử số lượng nhỏ và dự báo theo tốc độ bán 3 ngày đầu

#### Bối cảnh (giả định minh họa)
Một cửa hàng thời trang online 10 nhân viên ra khoảng 20 mẫu mới mỗi tháng theo xu hướng TikTok/Instagram. Dữ liệu lịch sử của từng mẫu gần như không có (mẫu mới mỗi tháng), nên trung bình động hay san bằng số mũ trên từng mẫu vô nghĩa. Trước đây cửa hàng đặt đều 120 sản phẩm mỗi mẫu.

#### Vấn đề kinh doanh
Nhu cầu tập trung vào ít mẫu "hot" và đa số mẫu bán chậm. Đặt đều 120 cái/mẫu thì mẫu hot hết hàng sớm (mất doanh thu), mẫu ế còn nằm kho (chôn vốn, phải xả lỗ).

#### Giải pháp: đặt thử + dự báo theo tốc độ bán (phương pháp định lượng đơn giản dựa trên tỷ lệ lịch sử)
1. Đặt thử 40 sản phẩm mỗi mẫu (tổng $20 \times 40 = 800$).
2. Theo dõi doanh số 3 ngày đầu. Lịch sử nhiều mẫu trước cho thấy trung bình 35% nhu cầu cả vòng đời của một mẫu xảy ra trong 3 ngày đầu. Dự báo nhu cầu cả vòng đời $= \dfrac{\text{Doanh số 3 ngày}}{0.35}$.
3. Quy tắc: mẫu hết hàng trong 3 ngày được coi là "hot" (nhu cầu bị cắt cụt do hết hàng nên không chia cho 0.35); đặt thêm đủ để có tổng 160 cái; mẫu có dự báo trên 100 thì đặt bổ sung đến mức dự báo; dưới 40 thì không đặt thêm.
4. Hàng đặt bổ sung về trong 5 ngày với giá vốn cao hơn do đặt gấp: 195.000 đồng so với 180.000 đồng (cao hơn 8.3%).

#### Phân tích định lượng (giả định minh họa)
Giả sử thực tế 20 mẫu chia thành: 4 mẫu hot (nhu cầu cả vòng đời 220 cái/mẫu), 6 mẫu trung bình (110 cái/mẫu), 10 mẫu ế (30 cái/mẫu). Giá bán 300.000 đồng, giá vốn 180.000 đồng, hàng tồn xả với giá 90.000 đồng.
- 3 ngày đầu: mẫu hot lẽ ra bán $220 \times 0.35 = 77$ cái nhưng chỉ có 40 nên hết hàng $\Rightarrow$ đặt thêm lên 160 cái. Mẫu trung bình bán $110 \times 0.35 = 38.5 \approx 38$ cái $\Rightarrow$ dự báo $38/0.35 = 108.6 \approx 110$, đặt thêm 70. Mẫu ế bán $30 \times 0.35 = 10.5 \approx 10$ cái $\Rightarrow$ dự báo $10/0.35 = 28.6 <40$, không đặt thêm.

| Chỉ tiêu | Cách cũ (đặt đều 120/mẫu) | Cách mới (đặt thử 40 + bổ sung) |
|---|---|---|
| Tổng đặt | $20 \times 120 = 2400$ | $800 + 900$ bổ sung $= 1700$ ($4 \times 160 + 6 \times 110 + 10 \times 40$) |
| Số bán được | $4 \times 120 + 6 \times 110 + 10 \times 30 = 1440$ | $4 \times 160 + 6 \times 110 + 10 \times 30 = 1600$ |
| Tồn dư cuối kỳ | $2400 - 1440 = 960$ (40%) | $1700 - 1600 = 100$ (5.9%) |
| Doanh thu | $1440 \times 300 = 432000$ nghìn | $1600 \times 300 = 480000$ nghìn |
| Giá trị xả tồn | $960 \times 90 = 86400$ nghìn | $100 \times 90 = 9000$ nghìn |
| Chi phí hàng | $2400 \times 180 = 432000$ nghìn | $800 \times 180 + 900 \times 195 = 319500$ nghìn |
| **Lợi nhuận gộp sau xả tồn** | $432000 + 86400 - 432000 = 86400$ nghìn (86.4 triệu) | $480000 + 9000 - 319500 = 169500$ nghìn (169.5 triệu) |

(Bổ sung cách mới: $4 \times 120 = 480$ cái của mẫu hot và $6 \times 70 = 420$ cái của mẫu trung bình, tổng 900.)

#### Diễn giải kinh doanh
Lợi nhuận gộp tăng 83.1 triệu đồng (+96%) trên 20 mẫu, dù giá vốn đặt gấp cao hơn 8.3%. Lý do: chi phí đặt gấp rẻ hơn rất nhiều so với chi phí *chôn vốn* vào mẫu ế (tồn dư giảm từ 960 xuống 100). Mẫu hot vẫn mất doanh thu ($4 \times (220-160) = 240$ cái) vì giới hạn đặt thêm ở 160: có thể cân nhắc nâng mức. Các con số này phụ thuộc giả định về phân bố mẫu hot/ế; con số cũ "giảm 30% tồn kho" trong bản nháp trước không có căn cứ tính toán nên đã được thay bằng tính toán minh họa này.

#### Bài học
1. Khi không có dữ liệu lịch sử từng mẫu, dùng "tỷ lệ trên toàn bộ danh mục" (35% trong 3 ngày) để dự báo từ quan sát sớm - tinh thần của dự báo định tính-định lượng kết hợp.
2. Đánh đổi: trả giá cao hơn cho đơn bổ sung nhanh còn tốt hơn bị tồn kho lớn.
3. Cần theo dõi lại tỷ lệ 35% định kỳ (nếu đổi thành 50% thì công thức dự báo sẽ đổi hẳn).

### Case 7: Nhà hàng buffet hải sản Đà Nẵng (SME dịch vụ) - Trung bình động có trọng số theo ngày trong tuần

#### Bối cảnh (giả định minh họa)
Một nhà hàng buffet hải sản ở Đà Nẵng cần đặt nguyên liệu tươi từ sáng sớm; hải sản không để lâu được. Lượng khách thứ Bảy là lớn nhất tuần và khó ước lượng. Trước đây chủ quán đặt hàng theo mức "cao nhất trong 4 tuần gần nhất cộng 10% cho chắc".

#### Vấn đề kinh doanh
Phải chọn lượng nguyên liệu mua cho thứ Bảy: mua thừa thì hải sản hỏng (thiệt hại 120.000 đồng nguyên liệu cho mỗi khách tương đương), mua thiếu thì hết món, mất khách (mất khoảng 150.000 đồng lợi nhuận gộp mỗi khách).

#### Giải pháp: WMA theo cùng ngày trong tuần
Dùng riêng chuỗi các ngày thứ Bảy (tránh trộn với ngày thường) và trọng số 0.4/0.3/0.2/0.1 cho 4 tuần gần nhất (mới nhất nặng nhất). Dữ liệu 12 tuần (số khách thứ Bảy): 300, 320, 310, 340, 335, 350, 330, 365, 360, 380, 370, 395.

Ví dụ tuần 5: $F_5 = 0.4 \times 340 + 0.3 \times 310 + 0.2 \times 320 + 0.1 \times 300 = 136 + 93 + 64 + 30 = 323$; thực tế 335, sai số $+12$.

| Tuần | Thực tế | Dự báo WMA | Sai số | Lượng mua cũ (max 4 tuần $\times$ 1.1) | Lượng mua mới (WMA $\times$ 1.05) |
|---|---|---|---|---|---|
| 5 | 335 | 323.0 | 12.0 | 374.0 | 339.2 |
| 6 | 350 | 330.0 | 20.0 | 374.0 | 346.5 |
| 7 | 330 | 339.5 | -9.5 | 385.0 | 356.5 |
| 8 | 365 | 338.0 | 27.0 | 385.0 | 354.9 |
| 9 | 360 | 348.5 | 11.5 | 401.5 | 365.9 |
| 10 | 380 | 354.5 | 25.5 | 401.5 | 372.2 |
| 11 | 370 | 366.0 | 4.0 | 418.0 | 384.3 |
| 12 | 395 | 370.5 | 24.5 | 418.0 | 389.0 |

- Độ chính xác WMA (8 tuần): MAD $= 134/8 = 16.75$ khách; MAPE $= 4.60\%$; Bias $= +14.38$ (dự báo thấp hơn thực tế do doanh số đang tăng). So sánh: MA4 có MAD 19.06, MAPE 5.22%, Bias +18.12; phương pháp Naive (lấy tuần trước) có MAD 16.88, MAPE 4.64%, Bias +6.88.
- Lượng mua: cách cũ mua tổng 3157 suất, dư 272 suất (8.62%); cách mới mua tổng 2909.5 suất, dư 50.85 suất (1.75%) nhưng thiếu 27.35 suất (0.95% nhu cầu 2885 suất).
- Giá trị: dư cũ $272 \times 120$ nghìn $= 32.64$ triệu; dư mới $50.85 \times 120$ nghìn $= 6.10$ triệu; thiếu mới $27.35 \times 150$ nghìn $= 4.10$ triệu. Tiết kiệm ròng $= 32.64 - 6.10 - 4.10 = 22.44$ triệu đồng trong 8 tuần (chỉ tính ngày thứ Bảy).
- Dự báo thứ Bảy tuần 13: $0.4 \times 395 + 0.3 \times 370 + 0.2 \times 380 + 0.1 \times 360 = 158 + 111 + 76 + 36 = 381$ khách; nếu dự báo thời tiết mưa (nhà hàng có không gian ngoài trời, hệ số điều chỉnh giả định 0.85): $381 \times 0.85 = 323.9 \approx 324$ khách.

#### Diễn giải kinh doanh
Điểm đáng chú ý: về *độ chính xác dự báo*, WMA không hơn đáng kể phương pháp Naive (MAPE 4.60% so với 4.64%) trong chuỗi đang tăng; lợi ích lớn đến từ *chính sách mua* dựa trên dự báo kèm đệm nhỏ 5% thay vì "cao nhất cộng 10%". Việc phân tách riêng từng ngày trong tuần mới là cải thiện cốt lõi. Bias dương cho thấy nên bổ sung điều chỉnh xu hướng (Holt) hoặc cộng thêm 4% nếu mùa cao điểm đang lên. Bản nháp cũ nêu "lãng phí từ 15% xuống dưới 5%"; số này không có căn cứ trong tài liệu nên được thay bằng tính toán minh họa ở trên (8.62% xuống 1.75%).

#### Bài học
- Phân tách chuỗi theo ngày trong tuần để xử lý mùa vụ tuần bằng công cụ rất đơn giản.
- Quyết định đặt hàng = dự báo + đệm an toàn dựa trên sai số; đệm cố định "cho chắc" (10%) thường quá lớn.
- Điều chỉnh định tính (thời tiết, sự kiện) bổ sung cho dự báo định lượng.

### Case 8: Dùng dự báo kinh tế vĩ mô làm biến đầu vào cho kế hoạch dài hạn

#### Bối cảnh
Các cơ quan thống kê và ngân hàng trung ương công bố định kỳ số liệu và dự báo vĩ mô (GDP, lạm phát, xuất nhập khẩu); doanh nghiệp có thể dùng các dự báo này làm biến độc lập trong mô hình dài hạn của mình. (Ví dụ chung; không khẳng định doanh nghiệp cụ thể nào đang dùng.)

#### Vấn đề kinh doanh
Một quyết định đầu tư công suất 5 năm phụ thuộc vào giả định tăng trưởng thu nhập, nhưng dự báo vĩ mô cũng bất định. Câu hỏi: kết quả nhạy đến mức nào nếu dự báo GDP sai?

#### Phân tích độ nhạy (giả định minh họa)
Dùng độ co giãn thu nhập 0.8 và tăng dân số 0.9%/năm như Case 2. Nếu dự báo GDP bình quân đầu người tăng 6.5%/năm thì tăng trưởng nhu cầu $= 0.8 \times 6.5 + 0.9 = 6.1\%$/năm, sau 5 năm chỉ số nhu cầu $= 100 \times 1.061^5 = 134.5$. Nếu GDP chỉ tăng 5.0% thì tăng trưởng nhu cầu $= 0.8 \times 5.0 + 0.9 = 4.9\%$, sau 5 năm $= 100 \times 1.049^5 = 127.0$.

#### Diễn giải kinh doanh
Chênh lệch giả định 1.5 điểm phần trăm GDP dẫn đến chênh lệch $134.5 - 127.0 = 7.5$ điểm chỉ số nhu cầu sau 5 năm, tương đương khoảng $7.5/125 = 6\%$ công suất của một nhà máy cỡ 125. Vì vậy kế hoạch nên được xây dựng theo kịch bản (cơ sở/lạc quan/bi quan) và đầu tư theo từng giai đoạn linh hoạt thay vì cam kết một lần.

#### Bài học
Với quyết định dài hạn, không chỉ dựa vào dữ liệu nội bộ mà tích hợp dự báo vĩ mô từ nguồn uy tín, đồng thời kiểm tra độ nhạy và để dành "quyền chọn" mở rộng.

### Case 9: Cơ sở rang xay cà phê "Mây Núi" (SME Việt Nam) - Chọn mô hình dự báo nhu cầu có xu hướng và mùa vụ (giả định minh họa)

> **Tên doanh nghiệp và toàn bộ số liệu là giả định minh họa** do tác giả thiết kế; các phép tính đã kiểm tra bằng Python.

#### Bối cảnh
"Mây Núi" là cơ sở rang xay cà phê nhỏ ở Lâm Đồng, 12 nhân viên, bán sỉ cho khoảng 80 quán cà phê và bán lẻ online. Nhu cầu có hai đặc điểm: (1) tăng đều theo số quán khách hàng; (2) mùa vụ rõ: cao điểm dịp Tết và cuối năm (tháng 11-12-1-2), thấp ở giữa năm (tháng 5-7). Cà phê rang xay có hạn dùng ngắn (khoảng 1-2 tháng sau rang) nên không tích trữ lâu được; nhân xanh phải đặt trước khoảng 1 tháng. Giá vốn giả định 150.000 đồng/kg; thiếu hàng mất khách sỉ, dư hàng thì xuống chất lượng và phải xả giá.

Doanh số 30 tháng gần nhất (kg/tháng), tháng 1 là tháng 1 của năm 1:

| Năm | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 | T11 | T12 | Tổng |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 474 | 472 | 412 | 380 | 381 | 392 | 385 | 438 | 474 | 503 | 538 | 594 | 5443 |
| 2 | 568 | 561 | 494 | 477 | 490 | 473 | 491 | 535 | 544 | 588 | 660 | 696 | 6577 |
| 3 (6 tháng đầu) | 664 | 670 | 584 | 580 | 562 | 545 | | | | | | | |

Tăng trưởng doanh số năm 2 so với năm 1: $6577/5443 = 1.208$ (+20.8%).

#### Vấn đề kinh doanh
Chủ cơ sở cần dự báo 6 tháng tới để (a) đặt nhân xanh trước 1 tháng; (b) lên kế hoạch ca rang; (c) giữ đủ tồn kho an toàn mà không bị hàng cũ. Câu hỏi: nên dùng mô hình nào, sai số bao nhiêu, và đặt tồn kho an toàn ở đâu?

#### Bước 1: Nhận diện thành phần chuỗi
Nhìn dữ liệu: cùng tháng năm 2 luôn cao hơn năm 1 (ví dụ T1: 568 so với 474; T12: 696 so với 594) $\Rightarrow$ có xu hướng tăng. Trong mỗi năm, T4-T7 thấp nhất (380-392 ở năm 1) còn T11-T12-T1 cao nhất (538-594) $\Rightarrow$ có mùa vụ lặp lại. Biên độ mùa vụ năm 2 cũng lớn hơn năm 1 (hiệu T12 và T6 là $696-473 = 223$ so với $594-392 = 202$) $\Rightarrow$ chọn **mô hình nhân** (mục 1.6). Như vậy chuỗi có cả xu hướng lẫn mùa vụ; các mô hình chỉ có mức (MA, SES) hoặc chỉ mức và xu hướng (Holt) sẽ thiếu thành phần.

#### Bước 2: Chia dữ liệu huấn luyện / kiểm tra (backtesting)
Dùng 24 tháng đầu (hai năm đầy đủ) để ước lượng; giấu 6 tháng của năm 3 (tháng 25-30: 664, 670, 584, 580, 562, 545) làm dữ liệu kiểm tra. Mọi mô hình dự báo 6 tháng đó và được chấm điểm bằng sai số.

#### Bước 3: Phân rã - hồi quy xu hướng - chỉ số mùa vụ (từng bước)
**3a. Hồi quy xu hướng thô trên 24 tháng.** $n=24$, $\sum X = 300$, $\sum Y = 12020$, $\sum XY = 160369$, $\sum X^2 = 4900$.
$$b = \frac{24 \times 160369 - 300 \times 12020}{24 \times 4900 - 300^2} = \frac{3848856 - 3606000}{117600 - 90000} = \frac{242856}{27600} = 8.799$$
$\bar{Y} = 12020/24 = 500.83$, $\bar{X} = 12.5$, $a = 500.83 - 8.799 \times 12.5 = 390.84$. Đường xu hướng thô: $T_t = 390.84 + 8.799\,t$.

**3b. Tỷ số $Y/T$ cho từng tháng và trung bình theo tháng trong năm.**

| Tháng | $Y$ năm 1 | $T$ năm 1 | $Y/T$ năm 1 | $Y$ năm 2 | $T$ năm 2 | $Y/T$ năm 2 | Trung bình | Chỉ số mùa vụ $S$ (chuẩn hoá) |
|---|---|---|---|---|---|---|---|---|
| 1 | 474 | 399.6 | 1.186 | 568 | 505.2 | 1.124 | 1.1551 | 1.155 |
| 2 | 472 | 408.4 | 1.156 | 561 | 514.0 | 1.091 | 1.1235 | 1.123 |
| 3 | 412 | 417.2 | 0.987 | 494 | 522.8 | 0.945 | 0.9661 | 0.966 |
| 4 | 380 | 426.0 | 0.892 | 477 | 531.6 | 0.897 | 0.8946 | 0.894 |
| 5 | 381 | 434.8 | 0.876 | 490 | 540.4 | 0.907 | 0.8914 | 0.891 |
| 6 | 392 | 443.6 | 0.884 | 473 | 549.2 | 0.861 | 0.8724 | 0.872 |
| 7 | 385 | 452.4 | 0.851 | 491 | 558.0 | 0.880 | 0.8654 | 0.865 |
| 8 | 438 | 461.2 | 0.950 | 535 | 566.8 | 0.944 | 0.9467 | 0.946 |
| 9 | 474 | 470.0 | 1.008 | 544 | 575.6 | 0.945 | 0.9767 | 0.976 |
| 10 | 503 | 478.8 | 1.050 | 588 | 584.4 | 1.006 | 1.0283 | 1.028 |
| 11 | 538 | 487.6 | 1.103 | 660 | 593.2 | 1.113 | 1.1079 | 1.107 |
| 12 | 594 | 496.4 | 1.197 | 696 | 602.0 | 1.156 | 1.1763 | 1.176 |
| **Tổng** | | | | | | | 12.0046 | 12.000 |

Tổng 12 tỷ số trung bình là 12.0046, hơi lệch 12; ta chuẩn hoá bằng cách nhân với $12/12.0046$ để tổng đúng bằng 12 (số kỳ trong chu kỳ). Diễn giải: tháng 12 và tháng 1 cao hơn mức xu hướng khoảng 17.6% và 15.5%; tháng 7 thấp hơn khoảng 13.5%. (Phép tính dùng chỉ số chưa làm tròn; các cột hiển thị làm tròn nên có sai lệch rất nhỏ nếu tính lại bằng tay.)

**3c. Gỡ mùa vụ và hồi quy lại.** Chia $Y$ cho $S$ của đúng tháng để có chuỗi đã gỡ mùa vụ (24 giá trị, từ 410.5 ở tháng 1 đến 591.9 ở tháng 24), rồi hồi quy xu hướng lần hai trên chuỗi đó: $\hat{Y}^{adj}_t = 398.30 + 8.175\,t$. Lý do làm hai lần: xu hướng thô ở bước 3a bị mùa vụ làm nhiễu (hai năm dữ liệu kết thúc ở mùa cao điểm nên kéo lệch độ dốc); chuỗi đã gỡ mùa vụ cho xu hướng sạch hơn.

**3d. Dự báo = xu hướng $\times$ chỉ số mùa vụ**, kiểm tra trên 6 tháng giấu:

| Tháng $t$ | Xu hướng $398.30 + 8.175t$ | Chỉ số $S$ | Dự báo $F$ | Thực tế $Y$ | Sai số $e = Y - F$ |
|---|---|---|---|---|---|
| 25 (T1) | 602.7 | 1.155 | 695.9 | 664 | -31.9 |
| 26 (T2) | 610.8 | 1.123 | 686.0 | 670 | -16.0 |
| 27 (T3) | 619.0 | 0.966 | 597.8 | 584 | -13.8 |
| 28 (T4) | 627.2 | 0.894 | 560.9 | 580 | +19.1 |
| 29 (T5) | 635.4 | 0.891 | 566.2 | 562 | -4.2 |
| 30 (T6) | 643.5 | 0.872 | 561.2 | 545 | -16.2 |

Ví dụ tháng 25: $398.30 + 8.175 \times 25 = 602.7$; $602.7 \times 1.155 = 696$ (tính chính xác với $S$ chưa làm tròn là 695.9).

#### Bước 4: Các mô hình đối chứng
- **MA3** (3 tháng cuối năm 2: 588, 660, 696): $F = (588+660+696)/3 = 648.0$ cho cả 6 tháng.
- **SES $\alpha=0.2$** chạy qua 24 tháng, $F = 581.9$ cho cả 6 tháng (không có xu hướng, không có mùa vụ nên dự báo là một đường phẳng).
- **Holt ($\alpha=0.3$, $\beta=0.1$)**, khởi tạo $L_1 = 474$, $T_1 = (594-474)/11 = 10.9$: dự báo 637.9; 650.0; 662.0; 674.1; 686.1; 698.2 (tăng đều, không có mùa vụ).

#### Bước 5: So sánh sai số trên 6 tháng kiểm tra

| Mô hình | MAD (kg) | RMSE (kg) | MAPE | Bias (kg) | Tracking Signal |
|---|---|---|---|---|---|
| MA3 | 59.83 | 67.66 | 10.43% | -47.17 | -4.73 |
| SES $\alpha=0.2$ | 38.50 | 52.08 | 6.09% | +18.96 | +2.95 |
| Holt ($\alpha=0.3$, $\beta=0.1$) | 82.59 | 95.65 | 14.45% | -67.22 | -4.88 |
| **Phân rã + hồi quy xu hướng** | **16.87** | **18.75** | **2.76%** | -10.50 | -3.73 |

Ví dụ tính chỉ số cho mô hình phân rã: $\sum|e| = 31.9+16.0+13.8+19.1+4.2+16.2 = 101.2$, MAD $= 101.2/6 = 16.87$; $\sum e^2 = 2108.9$ (làm tròn), MSE $= 351.5$, RMSE $= 18.75$; MAPE $= (4.80+2.39+2.36+3.29+0.75+2.97)/6 = 2.76\%$; $\sum e = -63$, Bias $= -10.5$, $TS = -63/16.87 = -3.73$. (Các chỉ số tính từ giá trị đã làm tròn 1 chữ số; tính bằng Python với số chưa làm tròn cho MAD 16.88, RMSE 18.76, các chỉ số khác không đổi sau làm tròn.)

#### Bước 6: Diễn giải kinh doanh
1. **Phân rã vượt trội**: MAD thấp hơn MA3 72% ($16.87$ so với $59.83$), MAPE 2.76% thuộc nhóm "rất chính xác" (< 10%). MA3 và Holt kém vì không có thành phần mùa vụ (MA3 dự báo 648 kg cho tháng 6 trong khi thực tế chỉ 545). Holt còn tệ hơn MA3 vì ngoại suy xu hướng tăng liên tục trong khi cả 6 tháng đầu năm 3 là giai đoạn thấp dần theo mùa.
2. **SES $\alpha=0.2$ "có vẻ khá" nhưng do may mắn**: mức san bằng 581.9 tình cờ nằm giữa vùng mùa cao điểm (T1-T2) và thấp điểm (T5-T6) nên sai số hai phía bù trừ. Nếu kiểm tra thêm 6 tháng cuối năm (mùa cao điểm), SES phẳng sẽ sai nặng. Bài học: không chọn mô hình chỉ vì một cửa sổ kiểm tra ngắn; nên kiểm tra trên đủ một chu kỳ mùa vụ.
3. **Tracking Signal của mô hình phân rã là $-3.73$**, gần ngưỡng $-4$: mô hình có xu hướng dự báo *cao hơn* thực tế 10.5 kg/tháng (khoảng 1.8%). Nguyên nhân hợp lý: xu hướng tăng năm 3 chậm lại so với hai năm đầu. Hành động: cập nhật hồi quy khi có thêm dữ liệu và giám sát TS hằng tháng; nếu vượt $-4$ thì xem lại độ dốc.
4. **Giá trị tiền**: sai số trung bình của MA3 là 59.83 kg/tháng (khoảng $59.83 \times 150{,}000 \approx 8.97$ triệu đồng hàng đặt thừa hoặc thiếu mỗi tháng) so với 16.87 kg (khoảng 2.53 triệu) của mô hình phân rã.

#### Bước 7: Từ dự báo đến quyết định đặt hàng và tồn kho an toàn
Dùng RMSE ngoài mẫu $= 18.75$ kg làm ước lượng độ lệch chuẩn sai số dự báo (thận trọng: RMSE trong mẫu chỉ 8.71, quá lạc quan). Mức dịch vụ 95% có $z = 1.65$:
$$SS = z \times \sigma_e = 1.65 \times 18.75 = 30.9 \text{ kg}$$
(Với chu kỳ đặt hàng mỗi tháng và thời gian chờ 1 tháng, ta bảo vệ cho 1 kỳ dự báo; nếu thời gian chờ $L$ kỳ thì nhân thêm $\sqrt{L}$, xem file 04.)
- Dự báo tháng 31 (tháng 7 năm 3): $t=31$: xu hướng $398.30 + 8.175 \times 31 = 651.7$; $S_7 = 0.865$; $F_{31} = 651.7 \times 0.865 = 563.8$ kg.
- Lượng tồn kho mục tiêu cho tháng 7: $563.8 + 30.9 \approx 595$ kg.
- Nếu dùng MA3 với RMSE $67.66$: $SS = 1.65 \times 67.66 = 111.6$ kg. Dự báo tốt hơn cho phép giảm tồn kho an toàn $111.6 - 30.9 = 80.7$ kg, tương đương khoảng $80.7 \times 150{,}000 \approx 12.1$ triệu đồng vốn lưu động và ít rủi ro nhân cũ.

Dự báo các tháng còn lại của năm 3 (từ mô hình): T7 563.8; T8 624.5; T9 652.3; T10 695.1; T11 758.0; T12 814.4 kg. Tổng cả năm 3 (gồm 6 tháng thực tế $= 3605$ và 6 tháng dự báo $= 4108$) khoảng 7713 kg, tăng khoảng 17.3% so với năm 2 (6577 kg).

#### Bài học và khuyến nghị
1. Nhìn dữ liệu trước, chọn mô hình sau: chuỗi có xu hướng + mùa vụ thì phải có thành phần mùa vụ.
2. Phân rã bằng Excel (hai lần hồi quy cộng chỉ số mùa vụ) đơn giản hơn Holt-Winters và hiệu quả khi chỉ có 24-30 tháng dữ liệu; Holt-Winters cần chọn 3 tham số và khởi tạo nhạy.
3. Luôn đánh giá bằng backtesting, báo cáo cả MAD, RMSE, MAPE, Bias và Tracking Signal.
4. Dùng RMSE ngoài mẫu để tính tồn kho an toàn; cập nhật mô hình mỗi tháng (thêm dữ liệu mới, tính lại chỉ số mùa vụ khi có thêm năm).
5. Hạn chế: chỉ hai năm huấn luyện nên mỗi chỉ số mùa vụ chỉ là trung bình của hai quan sát; nên cập nhật khi có năm thứ ba.

### Bảng tổng hợp bài học từ các case study

| Case | Phương pháp chính | Bài học chính |
|---|---|---|
| 1. Walmart | Hồi quy đa biến + dữ liệu thời tiết/sự kiện | Tích hợp dữ liệu bên ngoài; quyết định dựa trên bất đối xứng chi phí thiếu/dư (ngưỡng 25%) |
| 2. Vinamilk | Mùa vụ ngắn hạn + hồi quy vĩ mô dài hạn | Hai chân trời thời gian, hai công cụ; mốc đầu tư công suất tính được bằng tăng trưởng nhu cầu |
| 3. Coca-Cola | Hồi quy theo khu vực + điều chỉnh định tính | Mô hình phân tán theo khu vực, cẩn trọng ngoại suy |
| 4. Grab | ML dữ liệu thời gian thực theo ô lưới | ML phù hợp khi dữ liệu lớn nhiều biến; luôn kèm biên độ sai số |
| 5. Thời trang truyền thống (thất bại) | SES bị mù khi biến động cấu trúc | Tracking Signal báo động ngay tháng đầu ($-6.28$); cần reset mô hình |
| 6. Thời trang online (SME) | Đặt thử nhỏ + dự báo từ tốc độ bán 3 ngày | Không có lịch sử từng mẫu vẫn dự báo được; lợi nhuận gộp tăng minh họa +96% |
| 7. Nhà hàng Đà Nẵng (SME) | WMA theo ngày trong tuần | Chính sách đệm 5% thay vì 10%; dư giảm 8.62% xuống 1.75% |
| 8. Dự báo vĩ mô | Phân tích độ nhạy | Kịch bản và độ nhạy cho quyết định dài hạn |
| 9. Cà phê "Mây Núi" (SME, mới) | Phân rã + hồi quy + chỉ số mùa vụ | MAD 16.87 so với 59.83 của MA3; giảm tồn kho an toàn 80.7 kg |

---

## IV. Ứng dụng cho SME

### 4.1. Quy trình 7 bước xây dựng hệ thống dự báo

```
Bước 1: Xác định mục đích và tần suất dự báo
   │  Ngắn/trung/dài hạn? Theo SKU hay theo nhóm sản phẩm?
   ▼
Bước 2: Thu thập và làm sạch dữ liệu lịch sử
   │  Loại bỏ outlier bất thường (khuyến mãi đặc biệt, sự cố)
   ▼
Bước 3: Phân tích thành phần chuỗi thời gian
   │  Xác định có xu hướng, mùa vụ, chu kỳ hay không
   ▼
Bước 4: Lựa chọn phương pháp dự báo phù hợp
   │  Dựa trên đặc điểm dữ liệu (xem sơ đồ quyết định mục 5.4)
   ▼
Bước 5: Áp dụng mô hình & tính toán dự báo
   │  Sử dụng Excel/phần mềm chuyên dụng
   ▼
Bước 6: Đo lường sai số & Kiểm định mô hình
   │  MAD, RMSE, MAPE, Tracking Signal - backtesting trên dữ liệu giấu đi
   ▼
Bước 7: Giám sát & Điều chỉnh liên tục
      Cập nhật mô hình định kỳ, phát hiện tín hiệu cảnh báo sớm
```

### 4.2. So sánh mức độ áp dụng: SME và doanh nghiệp lớn

| Thành phần | SME | Doanh nghiệp lớn |
|---|---|---|
| Phương pháp chính | Trung bình động, san bằng số mũ, phân rã mùa vụ trên Excel | Holt-Winters, hồi quy đa biến, Machine Learning (ARIMA, Prophet, LSTM) |
| Dữ liệu đầu vào | Lịch sử bán hàng nội bộ | Tích hợp dữ liệu bên ngoài (thời tiết, mạng xã hội, kinh tế vĩ mô) |
| Tần suất cập nhật | Hàng tháng/hàng quý | Hàng ngày/thời gian thực (real-time) |
| Công cụ | Excel | Phần mềm dự báo chuyên dụng (SAP IBP, Oracle Demantra, Blue Yonder) |
| Nhân sự | Kiêm nhiệm | Đội ngũ Data Scientist/Demand Planner chuyên trách |

### 4.3. Chi phí đầu tư theo giai đoạn phát triển (ước tính)

| Giai đoạn | Công cụ dự báo | Chi phí ước tính (VNĐ) |
|---|---|---|
| Khởi nghiệp | Excel với công thức cơ bản | 0 - 5 triệu |
| Tăng trưởng | Google Sheets + Add-on dự báo, phần mềm bán hàng có module dự báo | 10 - 100 triệu/năm |
| Mở rộng | Phần mềm dự báo chuyên dụng vừa (Power BI + Python/R script) | 200 triệu - 1 tỷ/năm |
| Doanh nghiệp lớn | SAP IBP, Oracle Demantra, đội ngũ Data Science + Machine Learning | 2 - 20+ tỷ/năm |

### 4.4. Lộ trình khuyến nghị cho SME

1. Thu thập và tổ chức dữ liệu bán hàng lịch sử có cấu trúc (ít nhất 1-2 năm dữ liệu, tốt nhất 24-36 tháng để ước lượng mùa vụ).
2. Áp dụng phương pháp đơn giản (trung bình động, san bằng số mũ, phân rã mùa vụ) trên Excel trước khi đầu tư công cụ phức tạp.
3. Đo lường sai số dự báo (MAPE, MAD) định kỳ và theo dõi Tracking Signal.
4. Bổ sung thông tin định tính (xu hướng thị trường, phản hồi đội bán hàng) để điều chỉnh dự báo định lượng.
5. Khi quy mô đủ lớn, đầu tư phần mềm dự báo tích hợp và xem xét tuyển nhân sự chuyên trách phân tích dữ liệu; chỉ cân nhắc ML khi đã chứng minh được lợi ích đo bằng tiền (mục 2.10).

### 4.5. Các sai lầm thường gặp

| Sai lầm | Hậu quả | Cách phòng tránh |
|---|---|---|
| Dùng cùng 1 mô hình cho mọi sản phẩm | Độ chính xác kém cho sản phẩm có đặc tính khác biệt | Phân loại sản phẩm (theo Fisher Model ở file 03, ABC) trước khi chọn phương pháp |
| Dùng MA/SES đơn cho chuỗi có xu hướng | Dự báo luôn thấp hơn thực tế (Bias $\approx$ độ dốc $\times (n+1)/2$) | Dùng Holt hoặc hồi quy xu hướng; kiểm tra Bias |
| Bỏ qua mùa vụ khi có chu kỳ rõ ràng | Thiếu hàng ở cao điểm, dư ở thấp điểm (Case 9) | Tính chỉ số mùa vụ, dùng phân rã hoặc Holt-Winters |
| Không loại bỏ outlier trước khi dự báo | Mô hình bị méo bởi sự kiện một lần | Làm sạch dữ liệu, đánh dấu khuyến mãi, sự cố |
| Không đo lường sai số dự báo | Không biết mô hình tốt hay xấu, không cải tiến được | Luôn tính MAD/RMSE/MAPE và theo dõi Tracking Signal |
| Chọn mô hình theo sai số trong mẫu, không backtesting | Overfitting, "thắng" trên quá khứ nhưng kém ở tương lai | Giấu 1 chu kỳ dữ liệu gần nhất để kiểm tra |
| Chỉ dùng dự báo định lượng, bỏ qua định tính | Bỏ lỡ tín hiệu thay đổi thị trường (Case 5) | Kết hợp cả hai, đặc biệt cho sản phẩm mới/biến động |
| Dự báo quá chi tiết (từng SKU) khi dữ liệu không đủ | Sai số lớn do nhiễu | Dự báo tổng hợp trước, phân bổ xuống chi tiết theo tỷ trọng |
| Đặt đệm "cho chắc" cố định (ví dụ +10-20%) | Dư hàng, chôn vốn (Case 7) | Tính đệm từ RMSE và mức dịch vụ mong muốn |

### 4.6. Tự đánh giá năng lực dự báo của doanh nghiệp

Đánh dấu Có/Không cho từng mục:

- [ ] Có lưu trữ dữ liệu bán hàng lịch sử có cấu trúc (theo SKU, thời gian, khu vực) tối thiểu 2 năm?
- [ ] Có quy trình đo lường sai số dự báo (MAPE/MAD) định kỳ hàng tháng?
- [ ] Có phân công rõ trách nhiệm (ai cập nhật và theo dõi dự báo)?
- [ ] Có tích hợp thông tin định tính (khuyến mãi, sự kiện, đối thủ) vào điều chỉnh dự báo định lượng?
- [ ] Có sử dụng phần mềm/công cụ chuyên dụng thay vì hoàn toàn thủ công trên giấy?
- [ ] Có phân biệt phương pháp dự báo theo từng nhóm sản phẩm (ABC) thay vì một phương pháp cho tất cả?
- [ ] Có quy trình phản hồi (feedback loop) giữa bán hàng, sản xuất và bộ phận dự báo?
- [ ] Có đánh giá và cập nhật lại tham số mô hình (ví dụ hệ số $\alpha$) định kỳ?
- [ ] Có kế hoạch dự phòng (contingency plan) khi dự báo sai lệch lớn so với thực tế?
- [ ] Có đo lường được lợi ích tài chính cụ thể từ việc cải thiện độ chính xác dự báo?

**Chấm điểm**: đếm số mục "Có". 0-3 điểm: mức sơ khai, cần xây dựng nền tảng dữ liệu cơ bản. 4-6 điểm: mức trung bình, cần chuẩn hoá quy trình. 7-10 điểm: mức trưởng thành, có thể cân nhắc đầu tư mô hình nâng cao (ARIMA/ML).

---

## V. Tools & Templates

### 5.1. Bảng công cụ phần mềm hỗ trợ dự báo

| Công cụ | Chức năng | Chi phí ước tính | Phù hợp |
|---|---|---|---|
| Excel (FORECAST.LINEAR, TREND, SLOPE, INTERCEPT, RSQ, FORECAST.ETS) | Dự báo cơ bản, hồi quy, san bằng số mũ có mùa vụ | Có sẵn trong gói Office | SME nhỏ |
| Google Sheets + Add-on | Tương tự Excel (có FORECAST, TREND), cộng tác trực tuyến | Miễn phí | SME nhỏ-vừa |
| Python (statsmodels, Prophet) | Mô hình ARIMA, Holt-Winters, Machine Learning | Miễn phí (mã nguồn mở) | SME có nhân sự kỹ thuật |
| Power BI + Python script | Trực quan hoá + dự báo tích hợp | Vài triệu/tháng (ước tính) | SME vừa, doanh nghiệp lớn |
| SAP IBP, Oracle Demantra, Blue Yonder | Dự báo tích hợp ERP quy mô lớn | Hàng tỷ/năm (ước tính) | Doanh nghiệp lớn |

### 5.2. Template: Bảng tính dự báo và đo lường sai số

```
Kỳ | Thực tế (Y) | Dự báo (F) | Sai số (Y-F) | |Sai số| | Sai số² | %Sai số
---|-------------|------------|--------------|---------|---------|--------
 1 |             |            |              |         |         |
 2 |             |            |              |         |         |
 3 |             |            |              |         |         |

MAD  = Tổng |Sai số| / n = _______________
MSE  = Tổng Sai số² / n  = _______________
RMSE = Căn bậc hai của MSE = _______________
MAPE = Tổng %Sai số / n  = _______________
Bias = Tổng Sai số / n   = _______________
Tracking Signal = Tổng Sai số / MAD = _______________ (kiểm tra nằm trong ±4)
```

Công thức Excel gợi ý (giả sử $Y$ ở cột B, $F$ ở cột C, từ dòng 2): sai số `=B2-C2`; $|e|$ `=ABS(D2)`; $e^2$ `=D2^2`; %sai số `=ABS(D2)/B2`; MAD `=AVERAGE(E2:E13)`; RMSE `=SQRT(AVERAGE(F2:F13))`; MAPE `=AVERAGE(G2:G13)`; TS `=SUM(D2:D13)/AVERAGE(E2:E13)`. San bằng số mũ: ô dự báo kỳ sau `=$J$1*B2+(1-$J$1)*C2` với `J1` là ô chứa $\alpha$. Hồi quy xu hướng: `=FORECAST.LINEAR(13, B2:B13, A2:A13)` cho dự báo kỳ 13; `=RSQ(B2:B13, A2:A13)` cho $R^2$.

### 5.3. Mã Python tham khảo (đã chạy thử, chỉ dùng numpy)

```python
import numpy as np

def ses(y, alpha):
    """San bằng số mũ đơn. Trả về F[0..n]: F[0]=y[0]; F[n] là dự báo kỳ kế tiếp."""
    f = [y[0]]
    for t in range(len(y)):
        f.append(alpha * y[t] + (1 - alpha) * f[-1])
    return np.array(f)

def metrics(y, f):
    y, f = np.asarray(y, float), np.asarray(f, float)
    e = y - f
    mad = np.mean(np.abs(e))
    return {"MAD": mad, "RMSE": np.sqrt(np.mean(e**2)),
            "MAPE%": np.mean(np.abs(e) / y) * 100,
            "Bias": np.mean(e), "TS": e.sum() / mad}

y = [120,132,128,141,150,147,160,172,165,178,185,181]
f = ses(y, 0.3)
print(metrics(y[1:], f[1:len(y)]))   # đo từ tháng 2 đến tháng 12
print("Dự báo tháng 13:", round(f[-1], 2))
```
Kết quả: MAD 16.10, RMSE 17.27, MAPE 10.04%, Bias +16.10, TS 11.0; dự báo tháng 13 là 173.12, khớp với tính tay ở mục 2.2.

### 5.4. Sơ đồ quyết định lựa chọn phương pháp dự báo

```
                    Bắt đầu
                       │
        Có dữ liệu lịch sử đáng tin cậy (≥ 1-2 năm)?
                /                          \
              Có                          Không
               │                              │
   Dữ liệu có mùa vụ rõ?                PHƯƠNG PHÁP ĐỊNH TÍNH
      /            \                    (Delphi, ý kiến chuyên
    Có            Không                   gia, nghiên cứu thị trường)
     │              │
 Có xu hướng?     Có xu hướng?
  (thường có)       /      \
     │            Có       Không
 HOLT-WINTERS     │          │
 hoặc PHÂN RÃ  HOLT hoặc   SAN BẰNG SỐ MŨ ĐƠN /
 + HỒI QUY     HỒI QUY     TRUNG BÌNH ĐỘNG
               XU HƯỚNG
                  │
   Có yếu tố nhân quả rõ ràng (giá, quảng cáo, thời tiết)?
      → Thêm HỒI QUY ĐA BIẾN (Causal Model)
```

---

## VI. Bài tập thực hành

> Các bài 1-9 và 11 có đáp án tính toán đã kiểm tra bằng Python (xem phần "Hướng dẫn giải" ngay dưới mỗi bài). Nên tự làm trước khi xem đáp án.

**Bài 1 - Trung bình động và trung bình động có trọng số.** Doanh số 6 tháng: 50, 55, 53, 58, 60, 57. (a) Tính dự báo MA3 cho tháng 4, 5, 6, 7. (b) Tính WMA với trọng số 0.5/0.3/0.2 (kỳ gần nhất nặng nhất) cho cùng các tháng. (c) So sánh MAD trên tháng 4-6.
*Hướng dẫn giải*: (a) $F_4 = (50+55+53)/3 = 52.67$; $F_5 = (55+53+58)/3 = 55.33$; $F_6 = (53+58+60)/3 = 57.00$; $F_7 = (58+60+57)/3 = 58.33$. (b) $F_4 = 0.5 \times 53 + 0.3 \times 55 + 0.2 \times 50 = 26.5+16.5+10 = 53.0$; $F_5 = 0.5 \times 58 + 0.3 \times 53 + 0.2 \times 55 = 29+15.9+11 = 55.9$; $F_6 = 0.5 \times 60 + 0.3 \times 58 + 0.2 \times 53 = 30+17.4+10.6 = 58.0$; $F_7 = 0.5 \times 57 + 0.3 \times 60 + 0.2 \times 58 = 28.5+18+11.6 = 58.1$. (c) Sai số MA3: $5.33; 4.67; 0$ nên MAD $= 10/3 = 3.33$. Sai số WMA: $5; 4.1; -1$ nên MAD $= 10.1/3 = 3.37$. Hai phương pháp tương đương trên mẫu nhỏ; WMA dự báo tháng 7 cao hơn chút vì tin dữ liệu mới.

**Bài 2 - San bằng số mũ và tracking signal.** Dùng cùng chuỗi ở Bài 1, $\alpha = 0.4$, $F_1 = Y_1 = 50$. Tính $F_2 \dots F_7$, MAD, MSE, MAPE trên tháng 2-6 và Tracking Signal.
*Hướng dẫn giải*: $F_2 = 50$; $F_3 = 0.4 \times 55 + 0.6 \times 50 = 52.0$; $F_4 = 0.4 \times 53 + 0.6 \times 52 = 52.4$; $F_5 = 0.4 \times 58 + 0.6 \times 52.4 = 54.64$; $F_6 = 0.4 \times 60 + 0.6 \times 54.64 = 56.784$; $F_7 = 0.4 \times 57 + 0.6 \times 56.784 = 56.87$. Sai số tháng 2-6: $5; 1; 5.6; 5.36; 0.216$, tổng $= 17.176$. MAD $= 17.176/5 = 3.44$; MSE $= (25+1+31.36+28.73+0.05)/5 = 17.23$; MAPE $= (9.09+1.89+9.66+8.93+0.38)\%/5 = 5.99\%$; $TS = 17.176/3.435 = 5.0$ (vượt ±4: mô hình dự báo thấp có hệ thống vì chuỗi đang tăng; cân nhắc Holt).

**Bài 3 - Các chỉ số sai số.** Thực tế: 100, 110, 90, 120, 105, 115; Dự báo: 95, 108, 100, 110, 112, 100. Tính MAD, MSE, RMSE, MAPE, Bias, Tracking Signal và đánh giá theo bảng MAPE ở mục 2.7.
*Hướng dẫn giải*: sai số $e = 5, 2, -10, 10, -7, 15$. MAD $= 49/6 = 8.17$; MSE $= (25+4+100+100+49+225)/6 = 503/6 = 83.83$; RMSE $= 9.16$; MAPE $= (5.00+1.82+11.11+8.33+6.67+13.04)\%/6 = 7.66\%$ ("rất chính xác", dưới 10%); Bias $= 15/6 = 2.5$; $TS = 15/49 \times 6 = 1.84$ (trong ±4: không thiên lệch hệ thống). Lưu ý RMSE (9.16) lớn hơn MAD (8.17) vì có vài sai số lớn (15, 10, -10).

**Bài 4 - Hồi quy tuyến tính đơn.** Chi phí quảng cáo $X$ (triệu đồng): 2, 3, 4, 5, 6, 7; doanh số $Y$ (nghìn sản phẩm): 30, 34, 41, 43, 50, 52. Tìm $a$, $b$, $R^2$ và dự báo khi $X = 8$.
*Hướng dẫn giải*: $\sum X = 27$, $\sum Y = 250$, $\sum XY = 1205$, $\sum X^2 = 139$, $n=6$. $b = \dfrac{6 \times 1205 - 27 \times 250}{6 \times 139 - 27^2} = \dfrac{7230 - 6750}{834 - 729} = \dfrac{480}{105} = 4.571$; $a = 250/6 - 4.571 \times 4.5 = 41.667 - 20.571 = 21.095$. $SSE = 7.62$, $SST = 373.33$ nên $R^2 = 1 - 7.62/373.33 = 0.9796$. Dự báo $X=8$: $21.095 + 4.571 \times 8 = 57.67$ nghìn sản phẩm. Diễn giải: mỗi triệu đồng quảng cáo tăng thêm khoảng 4.57 nghìn sản phẩm trong khoảng dữ liệu 2-7 triệu; ngoại suy ra $X=8$ cần thận trọng vì có thể bão hoà.

**Bài 5 - Chỉ số mùa vụ.** Doanh số theo quý (nghìn thùng): năm 1: 60, 90, 120, 70; năm 2: 66, 99, 132, 77. (a) Tính chỉ số mùa vụ. (b) Nếu năm 3 dự kiến tăng 10% so với năm 2, dự báo từng quý.
*Hướng dẫn giải*: trung bình quý $= 63; 94.5; 126; 73.5$; trung bình chung $= 357/4 = 89.25$ (tổng hai năm 714, chia 8 quý). Chỉ số $S = 0.706; 1.059; 1.412; 0.824$ (tổng bằng 4). Tổng năm 2 $= 374$, tăng 10% $\Rightarrow 411.4$; mỗi quý $= 411.4/4 \times S = 102.85 \times S$ $\Rightarrow$ $72.6; 108.9; 145.2; 84.7$ (tổng $411.4$).

**Bài 6 - Holt một bước.** $L_{t-1} = 200$, $T_{t-1} = 10$, quan sát mới $Y_t = 215$, $\alpha = 0.4$, $\beta = 0.2$. Tính $L_t$, $T_t$, dự báo $F_{t+1}$ và $F_{t+3}$; so với dự báo trước đó cho kỳ $t$.
*Hướng dẫn giải*: dự báo trước đó $= 200+10 = 210$ (sai số $+5$). $L_t = 0.4 \times 215 + 0.6 \times 210 = 212.0$; $T_t = 0.2 \times (212 - 200) + 0.8 \times 10 = 10.4$; $F_{t+1} = 212 + 10.4 = 222.4$; $F_{t+3} = 212 + 3 \times 10.4 = 243.2$.

**Bài 7 - Tracking Signal.** Sai số 7 kỳ liên tiếp: $+3, -2, +4, +6, +5, +8, +7$. Tính TS sau mỗi kỳ và xác định kỳ mô hình vượt ngưỡng ±4.
*Hướng dẫn giải*: lũy kế $\sum e$: $3, 1, 5, 11, 16, 24, 31$; MAD lũy kế: $3, 2.5, 3, 3.75, 4, 4.67, 5$; TS $= 1.0; 0.4; 1.67; 2.93; 4.0; 5.14; 6.2$. TS chạm 4.0 ở kỳ 5 và *vượt ngưỡng* ở kỳ 6 (5.14): nên rà soát mô hình ở kỳ 5-6. Nguyên nhân thường gặp: sai số cùng dấu dương liên tục do nhu cầu tăng hoặc mô hình thiếu thành phần xu hướng.

**Bài 8 - Tồn kho an toàn từ sai số dự báo.** Một mã hàng có RMSE sai số dự báo hằng tuần là 25 đơn vị, thời gian chờ hàng 2 tuần, mức dịch vụ 95% ($z=1.65$). Tính tồn kho an toàn.
*Hướng dẫn giải*: $SS = z \times RMSE \times \sqrt{L} = 1.65 \times 25 \times \sqrt{2} = 58.3$ đơn vị (không nhân $\sqrt{L}$ thì chỉ là 41.25; sai số cộng dồn qua nhiều kỳ chờ). Nếu cải thiện dự báo làm RMSE giảm còn 15 thì $SS = 1.65 \times 15 \times \sqrt{2} = 35.0$, giảm 23.3 đơn vị.

**Bài 9 - Chọn mô hình.** Ba mô hình kiểm tra trên cùng 12 kỳ: A có MAPE 8%, Bias $-1$ (đơn vị), TS $= -0.8$; B có MAPE 6%, Bias $+9$, TS $= +7.2$; C có MAPE 7%, Bias $+1.5$, TS $= +1.5$. Chọn mô hình nào để dùng tiếp, vì sao?
*Hướng dẫn giải*: B có MAPE thấp nhất nhưng TS $= +7.2$ ngoài ngưỡng ±4 và Bias lớn: luôn dự báo thấp, nguy cơ thiếu hàng hệ thống. A và C cùng không bị lệch (TS trong ±4); C có MAPE thấp hơn A (7% so với 8%) nên chọn C (hoặc kết hợp trung bình A và C). Nguyên tắc: không chọn theo một chỉ số duy nhất; kết hợp độ lớn sai số và độ lệch.

**Bài 10 - Thiết kế khảo sát Delphi.** Thiết kế 3 vòng để dự báo nhu cầu một sản phẩm hoàn toàn mới: số chuyên gia (khuyến nghị 5-10, gồm bán hàng, sản xuất, người dùng), nội dung câu hỏi vòng 1 (ước lượng điểm và khoảng), thông tin phản hồi vòng 2 (trung vị, khoảng tứ phân vị, tóm tắt lý do), tiêu chí dừng (khoảng dao động thu hẹp dưới 15-20% trung vị hoặc không đổi giữa hai vòng). Dùng bảng ở mục 2.9 làm mẫu.

**Bài 11 - Phản ứng với biến động cấu trúc.** Chuỗi 6 tháng: 100, 100, 60, 60, 60, 60 (nhu cầu giảm đột ngột từ tháng 3). Dùng SES $\alpha = 0.5$, $F_1 = Y_1$. Sau bao nhiêu tháng thì dự báo nằm trong ±10% mức mới 60?
*Hướng dẫn giải*: $F_2 = 100$; $F_3 = 100$; $F_4 = 0.5 \times 60 + 0.5 \times 100 = 80$ (lệch 33%); $F_5 = 0.5 \times 60 + 0.5 \times 80 = 70$ (lệch 16.7%); $F_6 = 65$ (lệch 8.3%, đạt). Mất 3 tháng sau cú sốc (từ tháng 3 đến tháng 6) mới dự báo được trong ±10%; $\alpha$ cao hơn hội tụ nhanh hơn nhưng nhạy nhiễu hơn. Tương tự Case 5: reset mô hình nhanh hơn chờ tự học.

**Bài 12 - Tổng hợp thực hành.**
(a) Thu thập 12-24 tháng doanh số của một sản phẩm bạn quen thuộc; tính MA3, SES với $\alpha = 0.1, 0.3, 0.7$, so sánh MAPE và giải thích sự khác biệt.
(b) Xây dựng bảng tính Excel tự động tính dự báo san bằng số mũ và các chỉ số sai số (mục 5.2) cho chuỗi 24 tháng.
(c) Phân tích thành phần (xu hướng, mùa vụ) cho một ngành hàng có mùa vụ rõ (bánh Trung thu, đồ uống giải khát) bằng quy trình ở Case 9; so sánh với Holt không mùa vụ.
(d) Xác định giai đoạn vòng đời của một sản phẩm quen thuộc và đề xuất phương pháp theo bảng ở mục 1.5.
(e) Nghiên cứu một thất bại dự báo trong ngành thời trang hoặc thực phẩm tươi sống, đề xuất giải pháp kết hợp định tính-định lượng và cơ chế Tracking Signal.
(f) Đề xuất lộ trình nâng cấp hệ thống dự báo của một SME giả định từ Excel cơ bản lên phân rã/Holt-Winters: yêu cầu dữ liệu, công cụ, ngân sách (dùng bảng ở mục 4.3).
(g) So sánh kết quả giữa phương pháp đơn giản (SES) và phức tạp hơn (hồi quy đa biến) trên cùng bộ dữ liệu, rút ra kết luận về chi phí-lợi ích của độ phức tạp.

---

## PHỤ LỤC: CHECKLIST DỰ BÁO TỔNG HỢP

### A. Checklist trước khi dự báo và triển khai

**Dữ liệu**
- □ Đã thu thập dữ liệu lịch sử có cấu trúc (theo kỳ, SKU, khu vực), tối thiểu 24 tháng nếu cần ước lượng mùa vụ.
- □ Đã làm sạch dữ liệu: loại hoặc đánh dấu khuyến mãi lớn, sự cố, hết hàng (nhu cầu thật cao hơn doanh số bị cắt cụt).
- □ Đã phân tích thành phần chuỗi: xu hướng? mùa vụ? chu kỳ? nhiễu?

**Chọn mô hình**
- □ Đã chọn phương pháp theo đặc điểm dữ liệu (sơ đồ mục 5.4), không dùng một mô hình cho mọi sản phẩm.
- □ Với sản phẩm mới/không có lịch sử: đã có phương pháp định tính (Delphi, đặt thử, nghiên cứu thị trường).
- □ Đã thử ít nhất 2-3 mô hình đối chứng (MA, SES/Holt, phân rã) và backtesting trên dữ liệu giấu đi.

**Đo lường và giám sát**
- □ Đã tính MAD, RMSE, MAPE và Bias trên dữ liệu kiểm tra.
- □ Đã thiết lập Tracking Signal (ngưỡng ±4) và quy trình phản ứng (ai reset mô hình, trong bao lâu).
- □ Đã đặt kế hoạch cập nhật tham số ($\alpha$, $\beta$, chỉ số mùa vụ) định kỳ.

**Kết nối với vận hành**
- □ Đã dùng RMSE ngoài mẫu để tính tồn kho an toàn thay vì đệm cố định.
- □ Đã có điều chỉnh định tính (khuyến mãi, thời tiết, đối thủ, sự kiện) có ghi lại lý do.
- □ Đã có feedback loop giữa bán hàng - sản xuất - kế hoạch và đo được lợi ích tài chính (giảm tồn kho, giảm hết hàng).
- □ Đã có kế hoạch dự phòng khi dự báo sai lệch lớn.

### B. Bảng thuật ngữ (Glossary)

| Thuật ngữ | Giải thích |
|---|---|
| Time Series | Chuỗi thời gian - dữ liệu quan sát theo trình tự thời gian |
| Trend | Xu hướng tăng/giảm dài hạn của dữ liệu |
| Seasonality | Mùa vụ - biến động lặp lại theo chu kỳ cố định |
| Seasonal Index | Chỉ số mùa vụ - tỷ số giữa mức nhu cầu của kỳ đó và mức trung bình |
| Moving Average | Trung bình động - dự báo bằng trung bình các kỳ gần nhất |
| Exponential Smoothing | San bằng số mũ - dự báo với trọng số giảm dần theo độ cũ của dữ liệu |
| Holt / Holt-Winters | San bằng số mũ có xu hướng / có xu hướng và mùa vụ |
| MAD, MSE, RMSE, MAPE | Các thước đo sai số dự báo (mục 2.7) |
| Bias | Độ lệch trung bình; dương = dự báo thấp, âm = dự báo cao (khi $e = Y - F$) |
| Tracking Signal | Tín hiệu theo dõi phát hiện mô hình dự báo bị thiên lệch |
| Backtesting | Kiểm định ngược: dự báo phần dữ liệu đã biết nhưng bị giấu khi ước lượng |
| Overfitting | Mô hình khớp quá mức với dữ liệu quá khứ, kém trên dữ liệu mới |
| Delphi Method | Phương pháp dự báo định tính dựa trên ý kiến chuyên gia ẩn danh qua nhiều vòng |
| CPFR | Collaborative Planning, Forecasting and Replenishment |
| ARIMA | AutoRegressive Integrated Moving Average - mô hình dự báo thống kê nâng cao |
| Prophet | Công cụ dự báo mã nguồn mở của Meta, xử lý tốt dữ liệu nhiều mùa vụ |
| Alternative Data | Dữ liệu thay thế (Google Trends, mạng xã hội) bổ sung cho dữ liệu bán hàng truyền thống |
| Structural Break | Biến động cấu trúc thị trường khiến mô hình dự báo cũ không còn phù hợp |

### C. Bảng KPI dự báo

| KPI | Công thức | Mục tiêu tham khảo |
|---|---|---|
| MAPE | Trung bình $\lvert$ sai số % $\rvert$ | < 20% (tuỳ ngành) |
| Forecast Bias | Trung bình (Thực tế - Dự báo) | Gần 0 (không thiên lệch hệ thống) |
| Forecast Accuracy | $1 - MAPE$ | > 80% |
| Tracking Signal | Tổng sai số / MAD | Trong khoảng ±4 |

### D. Sổ tay rủi ro dự báo (Risk Register mẫu)

| Rủi ro | Xác suất | Tác động | Biện pháp giảm thiểu |
|---|---|---|---|
| Biến động cấu trúc thị trường (structural break) | Thấp | Cao | Giám sát Tracking Signal, bổ sung thông tin định tính, reset mô hình |
| Dữ liệu lịch sử không đủ hoặc kém chất lượng | Trung bình | Cao | Làm sạch dữ liệu, loại bỏ outlier, thu thập thêm |
| Sự kiện bất thường không lặp lại (khuyến mãi lớn) làm méo mô hình | Trung bình | Trung bình | Tách biệt và đánh dấu các sự kiện đặc biệt trong dữ liệu |
| Chọn sai phương pháp cho loại dữ liệu | Trung bình | Trung bình | Phân tích thành phần chuỗi trước khi chọn; backtesting |
| Overfitting khi dùng mô hình phức tạp/nhiều biến | Trung bình | Trung bình | Dùng $R^2$ hiệu chỉnh, kiểm tra ngoài mẫu, ưu tiên mô hình đơn giản |

### E. Bảng công thức tổng hợp

| Công thức | Ký hiệu | Ứng dụng |
|---|---|---|
| Trung bình động | $MA_n = \sum Y_i / n$ | Nhu cầu ổn định, không xu hướng |
| Trung bình động có trọng số | $WMA = \sum w_i Y_i, \sum w_i = 1$ | Cho trọng số cao hơn dữ liệu mới |
| San bằng số mũ đơn | $F_{t+1}=\alpha Y_t+(1-\alpha)F_t$ | Ngắn hạn, phản ứng nhanh với thay đổi gần đây |
| Holt | $L_t=\alpha Y_t+(1-\alpha)(L_{t-1}+T_{t-1})$; $T_t=\beta(L_t-L_{t-1})+(1-\beta)T_{t-1}$; $F_{t+h}=L_t+hT_t$ | Có xu hướng |
| Holt-Winters (nhân) | $F_{t+h}=(L_t+hT_t)\,s_{t+h-p}$ | Có xu hướng và mùa vụ |
| Hồi quy tuyến tính | $Y=a+bX$; $b=\frac{n\sum XY-\sum X\sum Y}{n\sum X^2-(\sum X)^2}$ | Dự báo theo thời gian hoặc biến nhân quả |
| Chỉ số mùa vụ | $S_q = \bar{Y}_q / \bar{Y}$ | Phân rã mùa vụ |
| MAD | $\sum\lvert Y_t-F_t\rvert/n$ | Sai số tuyệt đối trung bình |
| MSE / RMSE | $\sum(Y_t-F_t)^2/n$; $\sqrt{MSE}$ | Phạt sai số lớn; dùng cho tồn kho an toàn |
| MAPE | $\frac{1}{n}\sum\left\lvert\frac{Y_t-F_t}{Y_t}\right\rvert\times 100\%$ | Sai số tương đối, so sánh giữa các chuỗi |
| Tracking Signal | $TS=\sum(Y_t-F_t)/MAD$ | Phát hiện thiên lệch hệ thống |
| Tồn kho an toàn | $SS=z\,\sigma_e\sqrt{L}$ | Kết nối dự báo với tồn kho (file 04) |

### F. Liên kết chéo với các file khác trong bộ tài liệu

- **File 03 - Quản trị chuỗi cung ứng**: dự báo là nền tảng cho S&OP và CPFR, giảm hiệu ứng Bullwhip khi các bên cùng dùng một dự báo thống nhất.
- **File 04 - Quản trị tồn kho**: dự báo nhu cầu là đầu vào trực tiếp cho Safety Stock, ROP, EOQ và Newsvendor; sai số dự báo càng lớn thì tồn kho an toàn càng cao.
- **File 05 - Hoạch định năng lực**: dự báo dài hạn là cơ sở cho Aggregate Planning và quyết định đầu tư công suất (Lead/Lag/Match strategy).
- **File 06 - Quản trị dự án**: ước lượng PERT cũng là một dạng dự báo định tính có cấu trúc.
- **File 08 - Chiến lược bố trí mặt bằng**: dự báo tăng trưởng quy mô ảnh hưởng đến thiết kế layout linh hoạt, có khả năng mở rộng.

### G. Câu hỏi tự kiểm tra nhanh

1. Điểm khác biệt cốt lõi giữa dự báo định tính và định lượng là gì? *(Định tính dựa trên ý kiến khi thiếu dữ liệu; định lượng dựa trên dữ liệu số lịch sử.)*
2. Vì sao dự báo tổng hợp chính xác hơn dự báo chi tiết? *(Sai số ngẫu nhiên các thành phần bù trừ nhau - Risk Pooling.)*
3. Khi nào chuyển từ san bằng số mũ đơn sang Holt/Holt-Winters? *(Khi Bias một chiều và TS vượt ±4 vì xu hướng; khi có mùa vụ rõ và đủ 2-3 chu kỳ dữ liệu.)*
4. Tracking Signal phát hiện vấn đề gì? *(Sai số cộng dồn một chiều: mô hình thiên lệch hoặc thị trường đã đổi cấu trúc.)*
5. Vì sao Machine Learning không phải lúc nào cũng thắng? *(Cần dữ liệu lớn và nhiều biến; dễ overfitting; mô hình đơn giản và tổ hợp mô hình vẫn rất cạnh tranh ở chuỗi ngắn/ít biến.)*
6. Vì sao MA3 luôn dự báo thấp khi nhu cầu tăng? *(Độ trễ $\approx$ độ dốc $\times (n+1)/2$ kỳ.)*

---

## TÀI LIỆU THAM KHẢO

### Sách tham khảo
1. Hyndman, R. J. & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (3rd ed.). OTexts (miễn phí trực tuyến).
2. Chopra, S. & Meindl, P. (2019). *Supply Chain Management: Strategy, Planning, and Operation*. Pearson (chương Demand Forecasting).
3. Makridakis, S., Wheelwright, S. C., & Hyndman, R. J. (1998). *Forecasting: Methods and Applications*. Wiley.
4. Silver, E. A., Pyke, D. F., & Peterson, R. (1998). *Inventory Management and Production Planning and Scheduling*. Wiley.

### Bài báo gốc và nguồn nền tảng (nên đối chiếu khi trích dẫn)
1. Winters, P. R. (1960). Forecasting sales by exponentially weighted moving averages. *Management Science*, 6(3).
2. Holt, C. C. (1957; in lại 2004). Forecasting seasonals and trends by exponentially weighted moving averages. *International Journal of Forecasting*.
3. Box, G. E. P. & Jenkins, G. M. (1970). *Time Series Analysis: Forecasting and Control*. Holden-Day.
4. Dalkey, N. & Helmer, O. (1963). An experimental application of the Delphi method to the use of experts. *Management Science*, 9(3).
5. Hyndman, R. J. & Koehler, A. B. (2006). Another look at measures of forecast accuracy. *International Journal of Forecasting*.
6. Makridakis, S., Spiliotis, E., & Assimakopoulos, V. (2020, M4) và (2022, M5). Các bài tổng kết cuộc thi trên *International Journal of Forecasting*.
7. Taylor, S. J. & Letham, B. (2018). Forecasting at scale (Prophet). *The American Statistician*.

### Nguồn tài liệu trực tuyến bổ sung
1. Trang chủ cuộc thi M-Competitions (mofc.unic.ac.cy) - dữ liệu và kết quả so sánh các phương pháp dự báo trên quy mô lớn. Đây là nguồn thực nghiệm lớn và uy tín để so sánh hiệu quả giữa các phương pháp (M3, M4, M5).
2. Tài liệu hướng dẫn Facebook Prophet (facebook.github.io/prophet) - hướng dẫn triển khai mô hình dự báo mã nguồn mở.
3. Báo cáo thường niên của Tổng cục Thống kê Việt Nam (gso.gov.vn) - dữ liệu kinh tế vĩ mô tham chiếu cho dự báo dài hạn.

### Nguồn học trực tuyến
- Coursera: "Business Forecasting" - các trường đại học kinh doanh hàng đầu.
- Rob J. Hyndman's "Forecasting: Principles and Practice" (fpp3) - tài liệu mở trực tuyến, thực hành với ngôn ngữ R.
- ASCM CPIM - chứng chỉ có module về Demand Management và Forecasting.

### Liên kết nội bộ
- [File 03 - Quản trị chuỗi cung ứng](./03-supply-chain-management.md) - CPFR và mối liên hệ giữa dự báo hợp tác với hiệu ứng Bullwhip.
- [File 04 - Quản trị tồn kho](./04-inventory-management.md) - Dự báo là đầu vào cho EOQ, Safety Stock, Newsvendor Model.
- [File 05 - Hoạch định năng lực](./05-capacity-planning.md) - Dự báo dài hạn là bước đầu tiên trong quy trình hoạch định năng lực và Aggregate Planning.
- [File 06 - Quản trị dự án](./06-project-management.md) - Ước lượng PERT trong quản trị dự án cũng là một dạng dự báo định tính có cấu trúc.

*Tài liệu tham khảo: Người đọc nên ưu tiên tài liệu của Hyndman & Athanasopoulos (miễn phí, cập nhật, có mã nguồn R thực hành đi kèm) làm điểm khởi đầu, sau đó mở rộng sang các tài liệu chuyên sâu hơn về ứng dụng trong chuỗi cung ứng và quản trị vận hành cụ thể.*

*(Hết file 07 - Dự báo trong Quản trị Vận hành)*
