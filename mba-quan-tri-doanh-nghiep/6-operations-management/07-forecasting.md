# 07. Dự báo Nhu cầu (Demand Forecasting)

> File thuộc bộ kiến thức Quản trị Vận hành (Operations Management) - MBA Knowledge Base
> Liên kết: [04-inventory-management.md](./04-inventory-management.md) | [05-capacity-planning.md](./05-capacity-planning.md) | [08-layout-strategy.md](./08-layout-strategy.md)

---

## I. Tổng quan & Lý thuyết nền tảng

### 1.1. Định nghĩa và vai trò của Dự báo trong Quản trị Vận hành

**Dự báo (Forecasting)** là quá trình ước lượng các sự kiện tương lai bằng cách phân tích dữ liệu lịch sử và các yếu tố liên quan, nhằm hỗ trợ ra quyết định về hoạch định nhu cầu, tồn kho, năng lực, nhân sự và tài chính.

Dự báo là đầu vào nền tảng cho hầu hết các quyết định vận hành đã phân tích ở các file trước: công thức EOQ và Safety Stock (file 04) cần dự báo nhu cầu và độ biến động; hoạch định năng lực (file 05) cần dự báo tăng trưởng dài hạn; quản trị dự án (file 06) cần ước lượng thời gian dựa trên dữ liệu lịch sử.

**Nguyên lý cơ bản của dự báo**:
1. Dự báo hầu như luôn sai (không có dự báo nào hoàn hảo) - mục tiêu là giảm thiểu sai số, không phải loại bỏ hoàn toàn.
2. Dự báo cho nhóm sản phẩm/khu vực tổng hợp chính xác hơn dự báo cho từng SKU/khu vực riêng lẻ (nguyên lý Risk Pooling đã đề cập ở file 04).
3. Dự báo ngắn hạn chính xác hơn dự báo dài hạn.
4. Dự báo nên đi kèm với đo lường sai số (forecast error) để đánh giá độ tin cậy.

### 1.2. Phân loại dự báo theo thời gian

| Loại dự báo | Khoảng thời gian | Mục đích sử dụng |
|---|---|---|
| Ngắn hạn (Short-term) | Dưới 3 tháng | Lập lịch sản xuất, đặt hàng, phân bổ nhân sự hàng ngày/tuần |
| Trung hạn (Medium-term) | 3 tháng - 2 năm | Hoạch định tổng hợp (Aggregate Planning), ngân sách |
| Dài hạn (Long-term) | Trên 2 năm | Hoạch định năng lực, đầu tư nhà máy, chiến lược sản phẩm mới |

### 1.3. Phân loại phương pháp dự báo: Định tính vs Định lượng

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

**Khi nào dùng phương pháp định tính**: khi thiếu dữ liệu lịch sử (sản phẩm mới, thị trường mới), hoặc khi cần tích hợp thông tin định tính quan trọng (thay đổi chính sách, xu hướng công nghệ đột phá) mà mô hình số không nắm bắt được.

**Khi nào dùng phương pháp định lượng**: khi có đủ dữ liệu lịch sử đáng tin cậy và mối quan hệ giữa các biến tương đối ổn định theo thời gian.

### 1.4. Các thành phần của chuỗi thời gian (Time Series Components)

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

Bốn thành phần cơ bản của một chuỗi thời gian:
1. **Xu hướng (Trend - T)**: hướng tăng/giảm dài hạn của dữ liệu.
2. **Mùa vụ (Seasonality - S)**: biến động lặp lại theo chu kỳ cố định (ngày, tuần, tháng, quý, năm).
3. **Chu kỳ (Cyclical - C)**: dao động dài hạn không cố định về thời gian, thường gắn với chu kỳ kinh tế vĩ mô (khác mùa vụ ở chỗ không có tần suất cố định).
4. **Biến động ngẫu nhiên (Random/Irregular - R)**: nhiễu không thể dự đoán, do các sự kiện bất thường.

**Mô hình phân rã (Decomposition Model)**:
- Mô hình cộng (Additive): $Y = T + S + C + R$ (phù hợp khi biến động mùa vụ có biên độ ổn định theo thời gian)
- Mô hình nhân (Multiplicative): $Y = T \times S \times C \times R$ (phù hợp khi biến động mùa vụ tỷ lệ thuận với quy mô xu hướng)

---

## II. Phân tích chi tiết các công cụ/kỹ thuật

### 2.1. Phương pháp trung bình động (Moving Average)

$$MA_n = \frac{\sum_{i=1}^{n} Y_{t-i+1}}{n}$$

Trong đó $n$ là số kỳ được lấy trung bình. $n$ càng lớn, đường dự báo càng mượt (giảm nhiễu ngẫu nhiên) nhưng phản ứng chậm hơn với thay đổi xu hướng thực sự.

**Ví dụ**: Dự báo trung bình động 3 tháng cho tháng 4 dựa trên doanh số tháng 1,2,3 lần lượt là 100, 120, 110:

$$MA_3 = \frac{100+120+110}{3} = 110 \text{ đơn vị}$$

**Trung bình động có trọng số (Weighted Moving Average)**: gán trọng số cao hơn cho dữ liệu gần đây, phản ánh tốt hơn xu hướng mới nhất:

$$WMA = \sum w_i \times Y_{t-i+1}, \quad \sum w_i = 1$$

### 2.2. San bằng số mũ (Exponential Smoothing)

Đây là phương pháp phổ biến nhất trong thực tế nhờ tính đơn giản và hiệu quả, chỉ cần lưu trữ giá trị dự báo kỳ trước thay vì toàn bộ lịch sử dữ liệu.

$$F_{t+1} = \alpha \times Y_t + (1-\alpha) \times F_t$$

Trong đó:
- $F_{t+1}$ = Dự báo cho kỳ tiếp theo
- $Y_t$ = Giá trị thực tế kỳ hiện tại
- $F_t$ = Dự báo của kỳ hiện tại
- $\alpha$ = Hệ số san bằng (Smoothing constant), $0 < \alpha < 1$

**Ý nghĩa của $\alpha$**: $\alpha$ cao (gần 1) khiến dự báo phản ứng nhanh với thay đổi gần đây nhưng nhạy cảm với nhiễu; $\alpha$ thấp (gần 0) tạo dự báo mượt hơn nhưng phản ứng chậm với xu hướng mới.

**San bằng số mũ có điều chỉnh xu hướng (Holt's Method - Double Exponential Smoothing)**: mở rộng công thức cơ bản để xử lý dữ liệu có xu hướng tăng/giảm rõ ràng, sử dụng thêm hệ số $\beta$ để làm mượt thành phần xu hướng.

**San bằng số mũ ba tham số (Holt-Winters Method - Triple Exponential Smoothing)**: mở rộng thêm để xử lý cả yếu tố mùa vụ, sử dụng thêm hệ số $\gamma$ cho thành phần mùa vụ - đây là phương pháp toàn diện nhất trong nhóm san bằng số mũ, phù hợp với dữ liệu có cả xu hướng và mùa vụ rõ ràng (ví dụ doanh số bán lẻ theo quý).

### 2.3. Phân tích hồi quy (Regression Analysis)

**Hồi quy tuyến tính đơn (Simple Linear Regression)** mô hình hoá mối quan hệ giữa biến phụ thuộc (nhu cầu) và một biến độc lập (thời gian hoặc yếu tố khác):

$$Y = a + bX$$

Trong đó $a$ là hệ số chặn (intercept), $b$ là hệ số góc (slope) thể hiện mức thay đổi của $Y$ khi $X$ tăng 1 đơn vị, được ước lượng bằng phương pháp bình phương nhỏ nhất (Ordinary Least Squares - OLS):

$$b = \frac{n\sum XY - \sum X \sum Y}{n\sum X^2 - (\sum X)^2}, \quad a = \bar{Y} - b\bar{X}$$

**Hồi quy đa biến (Multiple Regression)**: mở rộng với nhiều biến độc lập (giá bán, chi phí quảng cáo, chỉ số kinh tế vĩ mô, thời tiết...), cho phép mô hình hoá dự báo nhân quả (causal forecasting) phức tạp hơn:

$$Y = a + b_1X_1 + b_2X_2 + ... + b_kX_k$$

**Hệ số xác định $R^2$ (Coefficient of Determination)**: đo lường % biến động của $Y$ được giải thích bởi mô hình hồi quy, $R^2$ càng gần 1 mô hình càng phù hợp với dữ liệu (tuy nhiên cần cẩn trọng với hiện tượng overfitting khi có quá nhiều biến độc lập).

### 2.4. Đo lường sai số dự báo (Forecast Error Measurement)

| Chỉ số | Công thức | Ý nghĩa |
|---|---|---|
| MAD (Mean Absolute Deviation) | $\frac{\sum \lvert Y_t - F_t \rvert}{n}$ | Sai số tuyệt đối trung bình, cùng đơn vị với dữ liệu gốc |
| MSE (Mean Squared Error) | $\frac{\sum (Y_t - F_t)^2}{n}$ | Phạt nặng các sai số lớn (do bình phương) |
| MAPE (Mean Absolute Percentage Error) | $\frac{1}{n}\sum \left\lvert \frac{Y_t-F_t}{Y_t} \right\rvert \times 100\%$ | Sai số theo %, dễ so sánh giữa các sản phẩm/quy mô khác nhau |
| Bias (Độ lệch trung bình) | $\frac{\sum (Y_t - F_t)}{n}$ | Phát hiện xu hướng dự báo thừa/thiếu hệ thống (không chỉ độ lớn sai số) |

**Bảng đánh giá nhanh độ chính xác dựa trên MAPE**:

| MAPE | Đánh giá |
|---|---|
| < 10% | Dự báo rất chính xác |
| 10-20% | Dự báo tốt |
| 20-50% | Dự báo chấp nhận được |
| > 50% | Dự báo kém, cần xem xét lại phương pháp/dữ liệu |

### 2.5. Tín hiệu theo dõi (Tracking Signal)

Công cụ giám sát liên tục để phát hiện khi mô hình dự báo bắt đầu mất độ chính xác (do thay đổi cấu trúc thị trường):

$$TS = \frac{\sum (Y_t - F_t)}{MAD}$$

Nếu $TS$ vượt ra ngoài khoảng kiểm soát thường dùng (±4), đây là tín hiệu cảnh báo cần xem xét lại hoặc điều chỉnh mô hình dự báo đang sử dụng.

### 2.6. Phương pháp Delphi (Delphi Method)

Đối với sản phẩm hoàn toàn mới không có dữ liệu lịch sử, phương pháp Delphi thu thập ý kiến từ một nhóm chuyên gia độc lập qua nhiều vòng khảo sát, mỗi vòng đều tổng hợp và phản hồi lại ý kiến chung ẩn danh cho đến khi đạt được sự đồng thuận tương đối - tránh hiệu ứng "tư duy nhóm" (groupthink) khi các chuyên gia thảo luận trực tiếp.

### 2.7. Hoạch định hợp tác dự báo (Collaborative Forecasting - CPFR)

Đã đề cập ở file 03, CPFR mở rộng dự báo ra ngoài phạm vi nội bộ doanh nghiệp, tích hợp dữ liệu và nhận định từ đối tác chuỗi cung ứng (nhà bán lẻ, nhà phân phối) để có dự báo chính xác hơn dự báo đơn lẻ từng bên.

---

## III. Ưu điểm & Nhược điểm

### 3.1. Bảng ưu nhược điểm các phương pháp dự báo

| Phương pháp | Ưu điểm | Nhược điểm |
|---|---|---|
| Trung bình động | Đơn giản, dễ tính toán | Phản ứng chậm với thay đổi xu hướng, cần lưu trữ lịch sử |
| San bằng số mũ | Chỉ cần lưu 1 giá trị, phản ứng nhanh, dễ tự động hoá | Cần chọn đúng hệ số $\alpha$, không xử lý tốt mùa vụ nếu dùng bản cơ bản |
| Holt-Winters | Xử lý tốt cả xu hướng và mùa vụ | Phức tạp hơn, cần đủ dữ liệu lịch sử (tối thiểu 2-3 chu kỳ mùa vụ) |
| Hồi quy | Giải thích được mối quan hệ nhân quả, dự báo dựa trên yếu tố tác động | Cần dữ liệu về các biến độc lập, rủi ro overfitting |
| Định tính (Delphi, chuyên gia) | Phù hợp khi thiếu dữ liệu lịch sử, tích hợp thông tin định tính | Chủ quan, tốn thời gian, khó lượng hoá độ tin cậy |

### 3.2. So sánh dự báo tập trung vs dự báo phân tán (theo Risk Pooling)

| Tiêu chí | Dự báo tổng hợp (Aggregate) | Dự báo chi tiết (Disaggregate - từng SKU/khu vực) |
|---|---|---|
| Độ chính xác | Cao hơn (nhờ hiệu ứng gộp rủi ro) | Thấp hơn, biến động lớn hơn |
| Mức độ chi tiết hữu ích | Thấp - phù hợp hoạch định tổng thể, năng lực | Cao - cần thiết cho đặt hàng, tồn kho cụ thể |
| Khuyến nghị thực hành | Dự báo tổng hợp trước, sau đó phân bổ (top-down disaggregation) theo tỷ trọng lịch sử | Kết hợp với dữ liệu POS thời gian thực để điều chỉnh |

### 3.3. Bảng ưu nhược điểm dự báo định tính vs định lượng theo giai đoạn vòng đời sản phẩm

| Giai đoạn vòng đời sản phẩm | Phương pháp phù hợp | Lý do |
|---|---|---|
| Giới thiệu (Introduction) | Định tính (Delphi, nghiên cứu thị trường) | Chưa có dữ liệu lịch sử |
| Tăng trưởng (Growth) | Kết hợp định tính + định lượng đơn giản | Dữ liệu bắt đầu tích luỹ nhưng còn ít, xu hướng thay đổi nhanh |
| Trưởng thành (Maturity) | Định lượng (Holt-Winters, hồi quy) | Dữ liệu lịch sử đầy đủ, xu hướng và mùa vụ ổn định |
| Suy thoái (Decline) | Định lượng kết hợp giám sát xu hướng giảm | Cần phát hiện sớm tốc độ suy giảm để điều chỉnh sản xuất/tồn kho |

---

## IV. Case study thực tiễn

### 4.1. Case study quốc tế lớn: Walmart - Dự báo nhu cầu tích hợp dữ liệu thời tiết và sự kiện

**Bối cảnh**: Walmart vận hành hàng nghìn cửa hàng với nhu cầu bị ảnh hưởng mạnh bởi các yếu tố bên ngoài như thời tiết (bão, nắng nóng), sự kiện thể thao, ngày lễ địa phương.

**Ứng dụng**: Walmart nổi tiếng với case study "trước cơn bão, doanh số bánh Pop-Tarts tăng vọt" - phát hiện qua phân tích dữ liệu lịch sử kết hợp dự báo thời tiết, từ đó điều chỉnh tồn kho các mặt hàng liên quan trước khi bão đổ bộ. Walmart tích hợp mô hình hồi quy đa biến với hàng trăm biến số (thời tiết, lịch sự kiện, xu hướng tìm kiếm) để dự báo chính xác hơn cho từng cửa hàng cụ thể thay vì áp dụng một mô hình chung cho toàn hệ thống.

**Kết quả**: Cải thiện đáng kể độ chính xác dự báo tại cấp độ cửa hàng, giảm tình trạng hết hàng hoặc dư thừa tồn kho trong các sự kiện bất thường.

### 4.2. Case study Việt Nam lớn: Vinamilk - Dự báo nhu cầu theo mùa vụ và yếu tố nhân khẩu học

**Bối cảnh**: Nhu cầu sữa và sản phẩm từ sữa của Vinamilk biến động theo mùa (mùa hè tiêu thụ nước giải khát từ sữa tăng, dịp Tết tăng nhu cầu quà biếu), đồng thời chịu ảnh hưởng bởi yếu tố nhân khẩu học dài hạn (tỷ lệ sinh, thu nhập bình quân).

**Giải pháp**: Áp dụng mô hình Holt-Winters cho dự báo ngắn-trung hạn theo mùa vụ sản phẩm, kết hợp với mô hình hồi quy dài hạn dựa trên các chỉ số nhân khẩu học và kinh tế vĩ mô (GDP bình quân đầu người, tỷ lệ đô thị hoá) để hoạch định đầu tư năng lực sản xuất dài hạn.

**Kết quả**: Cân đối tốt giữa sản xuất và nhu cầu theo mùa, đồng thời có cơ sở khoa học để quyết định đầu tư mở rộng nhà máy dài hạn.

### 4.3. Case study SME Việt Nam: Cửa hàng thời trang online dự báo nhu cầu theo xu hướng mạng xã hội

**Bối cảnh**: Một cửa hàng thời trang online với 10 nhân viên gặp khó khăn trong dự báo nhu cầu do thời trang chịu ảnh hưởng mạnh bởi xu hướng mạng xã hội (TikTok, Instagram) thay đổi rất nhanh, dữ liệu lịch sử truyền thống không đủ để dự báo chính xác.

**Giải pháp**: Kết hợp phương pháp định lượng đơn giản (trung bình động cho sản phẩm ổn định - áo thun cơ bản, quần jean) với phương pháp định tính (theo dõi xu hướng tìm kiếm Google Trends, lượng tương tác trên mạng xã hội cho sản phẩm theo trend) để điều chỉnh dự báo linh hoạt. Áp dụng chiến lược đặt hàng thử nghiệm số lượng nhỏ (small batch test order) cho sản phẩm mới, sau đó dựa vào tốc độ bán thực tế trong 3-5 ngày đầu để dự báo và đặt hàng bổ sung nhanh chóng (tương tự mô hình phản hồi nhanh của Zara).

**Kết quả**: Giảm đáng kể tồn kho hàng lỗi mốt (giảm 30% so với trước đây), tăng khả năng đáp ứng nhanh các sản phẩm hot trend.

### 4.4. Case study quốc tế - thất bại: Ngành bán lẻ thời trang dự báo sai theo dữ liệu lịch sử thuần tuý

**Bối cảnh**: Nhiều nhà bán lẻ thời trang truyền thống áp dụng mô hình dự báo hoàn toàn dựa trên dữ liệu bán hàng lịch sử (trung bình động, san bằng số mũ cơ bản) mà không tích hợp các tín hiệu thị trường mới (mạng xã hội, thay đổi hành vi tiêu dùng hậu COVID-19).

**Vấn đề**: Khi hành vi tiêu dùng thay đổi đột ngột (như giai đoạn COVID-19 chuyển từ mua sắm tại cửa hàng sang online, hoặc xu hướng thời trang bền vững tăng nhanh), các mô hình dự báo dựa hoàn toàn vào dữ liệu lịch sử không thể bắt kịp, dẫn đến dự báo sai lệch nghiêm trọng, gây tồn kho dư thừa hoặc thiếu hụt lớn.

**Bài học**: Dự báo định lượng thuần tuý dựa vào dữ liệu lịch sử có giới hạn nghiêm trọng khi thị trường có biến động cấu trúc (structural break). Cần kết hợp giám sát liên tục (tracking signal) và bổ sung thông tin định tính về thay đổi hành vi thị trường để phát hiện sớm khi mô hình cũ không còn phù hợp.

### 4.5. Case study Việt Nam SME - dịch vụ: Nhà hàng dự báo lượng khách theo ngày trong tuần và thời tiết

**Bối cảnh**: Một nhà hàng buffet hải sản tại Đà Nẵng gặp khó khăn trong việc dự báo lượng khách hàng ngày để chuẩn bị nguyên liệu tươi sống (hải sản không thể lưu trữ lâu), dẫn đến tình trạng hoặc thiếu nguyên liệu vào cuối tuần đông khách, hoặc dư thừa lãng phí vào ngày thường.

**Giải pháp**: Xây dựng mô hình dự báo đơn giản dựa trên dữ liệu lịch sử lượng khách theo từng ngày trong tuần (thứ 2-CN) kết hợp yếu tố mùa du lịch (cao điểm hè, các kỳ nghỉ lễ) và dự báo thời tiết (ngày mưa lượng khách giảm đáng kể với nhà hàng có không gian ngoài trời). Sử dụng phương pháp trung bình động có trọng số theo ngày trong tuần tương ứng của 4 tuần gần nhất.

**Kết quả**: Giảm đáng kể lãng phí nguyên liệu hải sản tươi sống (từ 15% xuống dưới 5% giá trị nhập hàng), đồng thời giảm tình trạng thiếu món ăn vào cuối tuần đông khách.

### 4.6. Bảng tổng hợp bài học từ các case study

| Case study | Phương pháp áp dụng | Bài học chính |
|---|---|---|
| Walmart | Hồi quy đa biến + dữ liệu thời tiết/sự kiện | Tích hợp dữ liệu bên ngoài giúp dự báo chính xác hơn nhiều so với chỉ dùng lịch sử bán hàng |
| Vinamilk | Holt-Winters + hồi quy nhân khẩu học | Kết hợp dự báo ngắn hạn theo mùa và dài hạn theo yếu tố vĩ mô cho các quyết định khác nhau |
| Cửa hàng thời trang online | Kết hợp định lượng + định tính (mạng xã hội) | Ngành có tốc độ thay đổi nhanh cần bổ sung tín hiệu thị trường thời gian thực |
| Ngành thời trang truyền thống (thất bại) | (Bài học từ thất bại) | Dự báo thuần dữ liệu lịch sử thất bại khi có biến động cấu trúc thị trường |
| Nhà hàng Đà Nẵng | Trung bình động có trọng số theo ngày/tuần | SME có thể áp dụng công cụ dự báo đơn giản hiệu quả cho bài toán cụ thể (hàng tươi sống) |

### 4.7. Case study bổ sung quốc tế: Coca-Cola - Dự báo nhu cầu tích hợp yếu tố kinh tế vĩ mô và xã hội

**Bối cảnh**: Coca-Cola vận hành tại hơn 200 quốc gia, đối mặt với việc dự báo nhu cầu chịu ảnh hưởng bởi rất nhiều yếu tố khác nhau giữa các thị trường: khí hậu, thu nhập bình quân, thói quen tiêu dùng văn hoá, các sự kiện thể thao lớn (World Cup, Olympic).

**Giải pháp**: Áp dụng mô hình hồi quy đa biến kết hợp phân tích theo từng khu vực địa lý (regional model), sử dụng các biến số như nhiệt độ trung bình, GDP bình quân đầu người, lịch các sự kiện thể thao lớn được tài trợ. Đồng thời xây dựng đội ngũ phân tích thị trường địa phương tại từng quốc gia để bổ sung yếu tố định tính đặc thù văn hoá.

**Kết quả**: Mô hình dự báo phân tán theo khu vực kết hợp yếu tố toàn cầu giúp Coca-Cola tối ưu hoá sản xuất và phân phối tại từng thị trường, đồng thời chuẩn bị tốt cho các đợt tăng vọt nhu cầu trong các sự kiện thể thao lớn được tài trợ toàn cầu.

### 4.8. Case study bổ sung Việt Nam: Tổng cục Thống kê và dự báo kinh tế vĩ mô

**Bối cảnh**: Ở cấp độ vĩ mô, việc dự báo các chỉ số kinh tế quốc gia (GDP, lạm phát, xuất nhập khẩu) đóng vai trò quan trọng để doanh nghiệp lớn hoạch định chiến lược dài hạn, dựa trên các báo cáo và mô hình dự báo do các cơ quan như Tổng cục Thống kê, Ngân hàng Nhà nước công bố định kỳ.

**Ứng dụng cho doanh nghiệp**: Các doanh nghiệp lớn (như Vinamilk đã đề cập ở mục 4.2) thường tích hợp các chỉ số dự báo kinh tế vĩ mô này vào mô hình dự báo nội bộ dài hạn của mình, thay vì chỉ dựa vào dữ liệu bán hàng lịch sử đơn thuần, giúp việc hoạch định đầu tư nhà máy, mở rộng thị trường có cơ sở khoa học vững chắc hơn.

**Bài học**: Đối với các quyết định dài hạn (đầu tư năng lực, mở rộng thị trường), doanh nghiệp không nên chỉ dựa vào dữ liệu nội bộ mà cần tích hợp các dự báo kinh tế vĩ mô từ nguồn uy tín để có bức tranh toàn diện hơn về triển vọng thị trường.

---

## V. Phương pháp triển khai từng bước

### 5.1. Quy trình 7 bước xây dựng hệ thống dự báo

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
   │  Dựa trên đặc điểm dữ liệu (xem sơ đồ quyết định Mục VII.3)
   ▼
Bước 5: Áp dụng mô hình & tính toán dự báo
   │  Sử dụng Excel/phần mềm chuyên dụng
   ▼
Bước 6: Đo lường sai số & Kiểm định mô hình
   │  MAD, MAPE, Tracking Signal - so sánh với dữ liệu thực tế đã biết (backtesting)
   ▼
Bước 7: Giám sát & Điều chỉnh liên tục
      Cập nhật mô hình định kỳ, phát hiện tín hiệu cảnh báo sớm
```

### 5.2. Bảng các sai lầm thường gặp

| Sai lầm | Hậu quả | Cách phòng tránh |
|---|---|---|
| Dùng cùng 1 mô hình cho mọi sản phẩm | Độ chính xác kém cho sản phẩm có đặc tính khác biệt | Phân loại sản phẩm (theo Fisher Model ở file 03) trước khi chọn phương pháp |
| Không loại bỏ outlier trước khi dự báo | Mô hình bị méo bởi các sự kiện bất thường một lần | Làm sạch dữ liệu, tách biệt sự kiện đặc biệt khỏi xu hướng chung |
| Không đo lường sai số dự báo | Không biết mô hình đang tốt hay xấu, không cải tiến được | Luôn tính MAD/MAPE và theo dõi Tracking Signal định kỳ |
| Chỉ dùng dự báo định lượng, bỏ qua thông tin định tính | Bỏ lỡ tín hiệu thay đổi thị trường quan trọng | Kết hợp cả định lượng và định tính, đặc biệt cho sản phẩm mới/biến động |
| Dự báo quá chi tiết (từng SKU) khi dữ liệu không đủ | Sai số lớn do nhiễu ở cấp độ chi tiết | Dự báo tổng hợp trước, phân bổ xuống chi tiết theo tỷ trọng lịch sử |

---

## VI. Quy mô áp dụng – SME vs Doanh nghiệp lớn

### 6.1. Bảng so sánh mức độ áp dụng

| Thành phần | SME | Doanh nghiệp lớn |
|---|---|---|
| Phương pháp chính | Trung bình động, san bằng số mũ cơ bản trên Excel | Holt-Winters, hồi quy đa biến, Machine Learning (ARIMA, Prophet, LSTM) |
| Dữ liệu đầu vào | Lịch sử bán hàng nội bộ | Tích hợp dữ liệu bên ngoài (thời tiết, mạng xã hội, kinh tế vĩ mô) |
| Tần suất cập nhật | Hàng tháng/hàng quý | Hàng ngày/thời gian thực (real-time) |
| Công cụ | Excel | Phần mềm dự báo chuyên dụng (SAP IBP, Oracle Demantra, Blue Yonder) |
| Nhân sự | Kiêm nhiệm | Đội ngũ Data Scientist/Demand Planner chuyên trách |

### 6.2. Chi phí đầu tư theo giai đoạn phát triển

| Giai đoạn | Công cụ dự báo | Chi phí ước tính (VNĐ) |
|---|---|---|
| Khởi nghiệp | Excel với công thức cơ bản | 0 - 5 triệu |
| Tăng trưởng | Google Sheets + Add-on dự báo, phần mềm bán hàng có module dự báo | 10 - 100 triệu/năm |
| Mở rộng | Phần mềm dự báo chuyên dụng vừa (Power BI + Python/R script) | 200 triệu - 1 tỷ/năm |
| Doanh nghiệp lớn | SAP IBP, Oracle Demantra, đội ngũ Data Science + Machine Learning | 2 - 20+ tỷ/năm |

### 6.3. Lộ trình khuyến nghị cho SME

1. Bắt đầu với việc thu thập và tổ chức dữ liệu bán hàng lịch sử có cấu trúc (ít nhất 1-2 năm dữ liệu).
2. Áp dụng phương pháp đơn giản (trung bình động, san bằng số mũ) trên Excel trước khi đầu tư công cụ phức tạp.
3. Đo lường sai số dự báo (MAPE) định kỳ để đánh giá hiệu quả mô hình đang dùng.
4. Bổ sung thông tin định tính (xu hướng thị trường, phản hồi từ đội bán hàng) để điều chỉnh dự báo định lượng.
5. Khi quy mô đủ lớn, đầu tư phần mềm dự báo tích hợp và xem xét tuyển dụng nhân sự chuyên trách phân tích dữ liệu.

### 6.4. Checklist tự đánh giá năng lực dự báo của doanh nghiệp

Sử dụng checklist sau để tự đánh giá mức độ trưởng thành của hệ thống dự báo trong doanh nghiệp bạn (đánh dấu Có/Không cho từng mục):

- [ ] Doanh nghiệp có lưu trữ dữ liệu bán hàng lịch sử có cấu trúc (theo SKU, thời gian, khu vực) tối thiểu 2 năm?
- [ ] Có quy trình đo lường sai số dự báo (MAPE/MAD) định kỳ hàng tháng?
- [ ] Có phân công rõ trách nhiệm (ai chịu trách nhiệm cập nhật và theo dõi dự báo)?
- [ ] Có tích hợp thông tin định tính (khuyến mãi, sự kiện, đối thủ) vào điều chỉnh dự báo định lượng?
- [ ] Có sử dụng phần mềm/công cụ chuyên dụng thay vì hoàn toàn thủ công trên giấy?
- [ ] Có phân biệt phương pháp dự báo theo từng nhóm sản phẩm (ABC) thay vì áp dụng một phương pháp cho tất cả?
- [ ] Có quy trình phản hồi (feedback loop) giữa bộ phận bán hàng, sản xuất và bộ phận dự báo?
- [ ] Có đánh giá và cập nhật lại tham số mô hình (ví dụ hệ số alpha trong san bằng số mũ) định kỳ?
- [ ] Có kế hoạch dự phòng (contingency plan) khi dự báo sai lệch lớn so với thực tế?
- [ ] Có đo lường được lợi ích tài chính cụ thể từ việc cải thiện độ chính xác dự báo?

**Cách chấm điểm**: Đếm số mục "Có". 0-3 điểm: mức sơ khai, cần xây dựng nền tảng dữ liệu cơ bản. 4-6 điểm: mức trung bình, cần chuẩn hoá quy trình. 7-10 điểm: mức trưởng thành, có thể cân nhắc đầu tư vào mô hình nâng cao (ARIMA/ML).

---

## VII. Công cụ & Templates hỗ trợ

### 7.1. Bảng công cụ phần mềm hỗ trợ dự báo

| Công cụ | Chức năng | Chi phí ước tính | Phù hợp |
|---|---|---|---|
| Excel (FORECAST, TREND functions) | Dự báo cơ bản | Miễn phí | SME nhỏ |
| Google Sheets + Add-on | Tương tự Excel, cộng tác trực tuyến | Miễn phí | SME nhỏ-vừa |
| Python (statsmodels, Prophet) | Mô hình ARIMA, Holt-Winters, Machine Learning | Miễn phí (mã nguồn mở) | SME có nhân sự kỹ thuật |
| Power BI + Python script | Trực quan hoá + dự báo tích hợp | Vài triệu/tháng | SME vừa, doanh nghiệp lớn |
| SAP IBP, Oracle Demantra | Dự báo tích hợp ERP quy mô lớn | Hàng tỷ/năm | Doanh nghiệp lớn |

### 7.2. Template: Bảng tính dự báo và đo lường sai số

```
Kỳ | Thực tế (Y) | Dự báo (F) | Sai số (Y-F) | |Sai số| | Sai số² | %Sai số
---|-------------|------------|--------------|---------|---------|--------
 1 |             |            |              |         |         |
 2 |             |            |              |         |         |
 3 |             |            |              |         |         |

MAD = Tổng |Sai số| / n = _______________
MSE = Tổng Sai số² / n = _______________
MAPE = Tổng %Sai số / n = _______________
Tracking Signal = Tổng Sai số / MAD = _______________ (kiểm tra nằm trong ±4)
```

### 7.3. Sơ đồ quyết định lựa chọn phương pháp dự báo

```
                    Bắt đầu
                       │
        Có dữ liệu lịch sử đáng tin cậy (≥ 1-2 năm)?
                /                          \
              Có                          Không
               │                              │
   Dữ liệu có xu hướng và mùa vụ rõ?    PHƯƠNG PHÁP ĐỊNH TÍNH
          /            \                (Delphi, ý kiến chuyên
        Có             Không              gia, nghiên cứu thị trường)
         │                │
   HOLT-WINTERS      Có yếu tố nhân quả rõ ràng
   (xử lý cả xu       (giá, quảng cáo, thời tiết)?
    hướng + mùa vụ)         /        \
                          Có          Không
                           │            │
                    HỒI QUY ĐA BIẾN   SAN BẰNG SỐ MŨ /
                    (Causal Model)     TRUNG BÌNH ĐỘNG
```

---

## VIII. Bài tập thực hành

1. Thu thập dữ liệu bán hàng lịch sử 12 tháng của một sản phẩm/dịch vụ, tính dự báo bằng trung bình động 3 tháng và so sánh với dữ liệu thực tế.
2. Áp dụng san bằng số mũ với 3 giá trị $\alpha$ khác nhau (0.1, 0.3, 0.7) cho cùng bộ dữ liệu, so sánh MAPE và giải thích sự khác biệt.
3. Xây dựng mô hình hồi quy tuyến tính đơn giản giữa doanh số và một biến độc lập (chi phí quảng cáo, giá bán), tính $R^2$ và giải thích ý nghĩa.
4. Tính MAD, MSE, MAPE cho một bộ dự báo giả định, đánh giá mức độ chính xác theo bảng phân loại MAPE ở Mục 2.4.
5. Tính Tracking Signal cho một chuỗi dự báo giả định, xác định thời điểm mô hình bắt đầu "lệch" khỏi khoảng kiểm soát.
6. Phân tích thành phần chuỗi thời gian (xu hướng, mùa vụ) cho dữ liệu doanh số của một ngành hàng có tính mùa vụ rõ ràng (bánh Trung thu, đồ uống giải khát).
7. Thiết kế một khảo sát Delphi đơn giản (3 vòng) để dự báo nhu cầu cho một sản phẩm hoàn toàn mới.
8. Nghiên cứu case study về thất bại dự báo trong ngành thời trang, đề xuất giải pháp kết hợp định tính-định lượng để tránh lặp lại sai lầm tương tự.
9. Xây dựng bảng tính Excel tự động tính dự báo san bằng số mũ và các chỉ số sai số cho một chuỗi dữ liệu 24 tháng.
10. Đề xuất lộ trình nâng cấp hệ thống dự báo cho một SME giả định từ Excel cơ bản lên mô hình Holt-Winters, bao gồm yêu cầu dữ liệu và công cụ cần thiết.
11. So sánh kết quả dự báo giữa phương pháp đơn giản (san bằng số mũ) và phương pháp phức tạp hơn (hồi quy đa biến) cho cùng một bộ dữ liệu, rút ra kết luận về chi phí-lợi ích của độ phức tạp.
12. Xác định giai đoạn vòng đời của một sản phẩm/dịch vụ thực tế bạn quen thuộc, đề xuất phương pháp dự báo phù hợp theo bảng ở Mục 3.3.

---

## IX. Phụ lục

### 9.1. Bảng thuật ngữ (Glossary)

| Thuật ngữ | Giải thích |
|---|---|
| Time Series | Chuỗi thời gian - dữ liệu quan sát theo trình tự thời gian |
| Trend | Xu hướng tăng/giảm dài hạn của dữ liệu |
| Seasonality | Mùa vụ - biến động lặp lại theo chu kỳ cố định |
| Moving Average | Trung bình động - phương pháp dự báo đơn giản dựa trên trung bình các kỳ gần nhất |
| Exponential Smoothing | San bằng số mũ - phương pháp dự báo dựa trên trọng số giảm dần theo thời gian |
| Holt-Winters | San bằng số mũ ba tham số xử lý cả xu hướng và mùa vụ |
| MAPE | Mean Absolute Percentage Error - sai số phần trăm tuyệt đối trung bình |
| Tracking Signal | Tín hiệu theo dõi phát hiện mô hình dự báo mất độ chính xác |
| Delphi Method | Phương pháp dự báo định tính dựa trên ý kiến chuyên gia qua nhiều vòng |
| CPFR | Collaborative Planning, Forecasting and Replenishment |
| ARIMA | AutoRegressive Integrated Moving Average - mô hình dự báo thống kê nâng cao |
| Prophet | Công cụ dự báo mã nguồn mở của Meta, xử lý tốt dữ liệu nhiều mùa vụ |
| Alternative Data | Dữ liệu thay thế (Google Trends, mạng xã hội) bổ sung cho dữ liệu bán hàng truyền thống |
| Structural Break | Biến động cấu trúc thị trường khiến mô hình dự báo cũ không còn phù hợp |

### 9.2. Bảng đo lường KPI dự báo

| KPI | Công thức | Mục tiêu tham khảo |
|---|---|---|
| MAPE | Trung bình |sai số %| | < 20% (tuỳ ngành) |
| Forecast Bias | Trung bình (Thực tế - Dự báo) | Gần 0 (không thiên lệch hệ thống) |
| Forecast Accuracy | 1 - MAPE | > 80% |
| Tracking Signal | Tổng sai số / MAD | Trong khoảng ±4 |

### 9.3. Sổ tay rủi ro dự báo (Risk Register mẫu)

| Rủi ro | Xác suất | Tác động | Biện pháp giảm thiểu |
|---|---|---|---|
| Biến động cấu trúc thị trường (structural break) | Thấp | Cao | Giám sát Tracking Signal, bổ sung thông tin định tính |
| Dữ liệu lịch sử không đủ hoặc kém chất lượng | Trung bình | Cao | Làm sạch dữ liệu, loại bỏ outlier trước khi dự báo |
| Sự kiện bất thường không lặp lại (khuyến mãi lớn) làm méo mô hình | Trung bình | Trung bình | Tách biệt và đánh dấu các sự kiện đặc biệt trong dữ liệu |
| Chọn sai phương pháp dự báo cho loại dữ liệu | Trung bình | Trung bình | Phân tích thành phần chuỗi thời gian trước khi chọn phương pháp |

### 9.4. Bảng tham chiếu nhanh các công thức cốt lõi

| Công thức | Ký hiệu | Ứng dụng |
|---|---|---|
| Trung bình động | $MA_n = \sum Y_i / n$ | Dự báo ngắn hạn, dữ liệu ổn định |
| San bằng số mũ | $F_{t+1}=\alpha Y_t+(1-\alpha)F_t$ | Dự báo ngắn hạn có phản ứng nhanh với thay đổi gần đây |
| MAD | $MAD=\sum|Y_t-F_t|/n$ | Đo sai số tuyệt đối trung bình |
| MSE | $MSE=\sum(Y_t-F_t)^2/n$ | Đo sai số bình phương, phạt nặng sai số lớn |
| MAPE | $MAPE=\sum|(Y_t-F_t)/Y_t|/n \times 100\%$ | Đo sai số tương đối, dễ so sánh giữa các chuỗi |
| Tracking Signal | $TS=\sum(Y_t-F_t)/MAD$ | Phát hiện thiên lệch hệ thống của mô hình |
| Hồi quy tuyến tính | $Y=a+bX$ | Dự báo dựa trên biến độc lập có tương quan |

### 9.5. Ghi chú bổ sung về tài liệu tham khảo

Ngoài các tài liệu đã liệt kê ở Mục X, người đọc quan tâm sâu hơn về ứng dụng Machine Learning trong dự báo nhu cầu có thể tham khảo thêm các bài báo khoa học công bố tại hội nghị M-Competitions (M3, M4, M5) - đây là nguồn dữ liệu thực nghiệm lớn và uy tín nhất hiện nay để so sánh hiệu quả giữa các phương pháp dự báo khác nhau trên hàng chục nghìn chuỗi thời gian thực tế từ nhiều ngành khác nhau.

---

## X. Tài liệu tham khảo

### Sách tham khảo
1. Hyndman, R. J. & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice*. OTexts (miễn phí trực tuyến).
2. Chopra, S. & Meindl, P. (2019). *Supply Chain Management: Strategy, Planning, and Operation*. Pearson (chương Demand Forecasting).
3. Makridakis, S., Wheelwright, S. C., & Hyndman, R. J. (1998). *Forecasting: Methods and Applications*. Wiley.
4. Silver, E. A., Pyke, D. F., & Peterson, R. (1998). *Inventory Management and Production Planning and Scheduling*. Wiley.

### Nguồn tài liệu trực tuyến bổ sung
1. Trang chủ cuộc thi M-Competitions (mofc.unic.ac.cy) - dữ liệu và kết quả so sánh các phương pháp dự báo trên quy mô lớn.
2. Tài liệu hướng dẫn Facebook Prophet (facebook.github.io/prophet) - hướng dẫn triển khai mô hình dự báo mã nguồn mở.
3. Báo cáo thường niên của Tổng cục Thống kê Việt Nam (gso.gov.vn) - dữ liệu kinh tế vĩ mô tham chiếu cho dự báo dài hạn.

### Liên kết nội bộ
- Xem thêm [File 03 - Quản trị chuỗi cung ứng](./03-supply-chain-management.md) để hiểu vai trò của dự báo trong CPFR.
- Xem thêm [File 04 - Quản trị tồn kho](./04-inventory-management.md) để hiểu ứng dụng dự báo trong tính Safety Stock.
- Xem thêm [File 05 - Hoạch định năng lực](./05-capacity-planning.md) để hiểu vai trò dự báo trong Aggregate Planning.

### Liên kết nội bộ (Internal Cross-links)
- [04-inventory-management.md](./04-inventory-management.md) - Dự báo là đầu vào cho công thức EOQ, Safety Stock, Newsvendor Model.
- [05-capacity-planning.md](./05-capacity-planning.md) - Dự báo dài hạn là bước đầu tiên trong quy trình hoạch định năng lực.
- [03-supply-chain-management.md](./03-supply-chain-management.md) - CPFR và mối liên hệ giữa dự báo hợp tác với hiệu ứng Bullwhip.
- [06-project-management.md](./06-project-management.md) - Ước lượng PERT trong quản trị dự án cũng là một dạng dự báo định tính có cấu trúc.

### Nguồn học trực tuyến
- Coursera: "Business Forecasting" - các trường đại học kinh doanh hàng đầu.
- Rob J. Hyndman's "Forecasting: Principles and Practice" (fpp3) - tài liệu mở trực tuyến, thực hành với ngôn ngữ R.
- ASCM CPIM - chứng chỉ có module về Demand Management và Forecasting.

### Ghi chú cuối phần tài liệu tham khảo

Người đọc nên ưu tiên tài liệu của Hyndman & Athanasopoulos (miễn phí, cập nhật, có mã nguồn R thực hành đi kèm) làm điểm khởi đầu, sau đó mở rộng sang các tài liệu chuyên sâu hơn về ứng dụng trong chuỗi cung ứng và quản trị vận hành cụ thể.

---

## Phụ lục bổ sung: Dự báo trong kỷ nguyên Machine Learning và Dữ liệu lớn

### A.1. Mô hình ARIMA (AutoRegressive Integrated Moving Average)

ARIMA là mô hình thống kê nâng cao kết hợp ba thành phần: tự hồi quy (AR - giá trị hiện tại phụ thuộc vào giá trị quá khứ), sai phân (I - Integrated, xử lý dữ liệu không dừng/non-stationary), và trung bình động (MA - phụ thuộc vào sai số dự báo quá khứ). Mô hình được ký hiệu ARIMA(p,d,q) với p, d, q là các tham số bậc tương ứng.

ARIMA phù hợp với dữ liệu chuỗi thời gian phức tạp hơn các phương pháp san bằng số mũ truyền thống, nhưng đòi hỏi kiến thức thống kê chuyên sâu hơn để lựa chọn tham số phù hợp (thường dùng biểu đồ ACF/PACF hoặc thuật toán tự động như auto.arima).

### A.2. Mô hình Prophet (Facebook/Meta)

Prophet là công cụ dự báo mã nguồn mở do Meta (Facebook) phát triển, được thiết kế đặc biệt để xử lý dữ liệu kinh doanh có nhiều mùa vụ chồng chéo (theo tuần, theo năm), ngày lễ đặc biệt, và có khả năng chống chịu tốt với dữ liệu thiếu hoặc outlier - phù hợp cho người dùng không chuyên sâu về thống kê nhưng vẫn cần độ chính xác cao.

### A.3. Học máy trong dự báo: Random Forest, XGBoost, LSTM

Với sự phát triển của Machine Learning, các thuật toán như Random Forest, Gradient Boosting (XGBoost) và mạng nơ-ron hồi quy (LSTM - Long Short-Term Memory) ngày càng được ứng dụng trong dự báo nhu cầu quy mô lớn, đặc biệt khi có nhiều biến số đầu vào phức tạp (hàng nghìn SKU, dữ liệu từ nhiều nguồn khác nhau) mà các mô hình thống kê truyền thống khó xử lý hiệu quả.

**Lưu ý quan trọng**: Machine Learning không phải luôn tốt hơn phương pháp thống kê truyền thống - nhiều nghiên cứu thực nghiệm (như cuộc thi dự báo M4, M5 Competition) cho thấy các phương pháp đơn giản (san bằng số mũ, ARIMA) vẫn cạnh tranh tốt với Machine Learning phức tạp trong nhiều trường hợp thực tế, đặc biệt khi dữ liệu lịch sử không đủ lớn.

### A.4. Dự báo nhu cầu dựa trên dữ liệu thay thế (Alternative Data Forecasting)

Xu hướng hiện đại là bổ sung dữ liệu truyền thống (lịch sử bán hàng) bằng các nguồn dữ liệu thay thế để cải thiện độ chính xác dự báo:

| Nguồn dữ liệu thay thế | Ứng dụng |
|---|---|
| Google Trends | Phát hiện sớm xu hướng tìm kiếm tăng/giảm cho sản phẩm/dịch vụ |
| Dữ liệu mạng xã hội (lượt đề cập, sentiment) | Dự báo xu hướng thời trang, sản phẩm viral |
| Dữ liệu thời tiết | Điều chỉnh dự báo cho sản phẩm nhạy cảm thời tiết (đồ uống, quần áo mùa) |
| Dữ liệu vệ tinh (traffic bãi đỗ xe) | Ước lượng doanh số bán lẻ theo thời gian thực (dùng bởi các quỹ đầu tư) |
| Dữ liệu giao dịch thẻ tín dụng tổng hợp | Ước lượng xu hướng tiêu dùng ngành theo thời gian gần thực |

### A.5. Ghi chú kết thúc file

File này trình bày một phổ đầy đủ các phương pháp dự báo, từ đơn giản (trung bình động, san bằng số mũ - phù hợp SME) đến nâng cao (Holt-Winters, hồi quy đa biến, ARIMA, Machine Learning - phù hợp doanh nghiệp lớn có nguồn lực dữ liệu và kỹ thuật). Nguyên tắc quan trọng nhất cần ghi nhớ: không có mô hình dự báo nào hoàn hảo, và giá trị thực sự nằm ở việc đo lường sai số liên tục, kết hợp thông tin định tính-định lượng, và điều chỉnh mô hình linh hoạt theo biến động thực tế của thị trường.

### A.6. Case study bổ sung: Grab - Dự báo nhu cầu di chuyển theo thời gian thực

**Bối cảnh**: Grab vận hành dịch vụ gọi xe tại nhiều thành phố Đông Nam Á, trong đó có Việt Nam, với nhu cầu biến động cực kỳ nhanh theo giờ trong ngày, thời tiết, sự kiện đặc biệt (giờ tan tầm, ngày mưa, lễ hội).

**Thách thức**: Dự báo nhu cầu di chuyển không chỉ cần chính xác mà còn cần theo thời gian thực (real-time) ở cấp độ từng khu vực nhỏ (quận, phường) để phân bổ tài xế hợp lý, tránh tình trạng thiếu xe cục bộ trong khi khu vực khác dư thừa.

**Giải pháp áp dụng**: Grab sử dụng mô hình Machine Learning kết hợp dữ liệu thời gian thực (vị trí GPS tài xế, lịch sử đặt xe theo khung giờ, dữ liệu thời tiết, sự kiện lớn tại khu vực) để dự báo nhu cầu ở độ phân giải không gian-thời gian rất cao (theo từng ô lưới địa lý nhỏ, theo từng khung 15-30 phút). Hệ thống định giá linh động (dynamic/surge pricing) cũng dựa trực tiếp trên chênh lệch giữa dự báo cung và cầu tại từng khu vực.

**Kết quả**: Cải thiện đáng kể tỷ lệ đáp ứng yêu cầu đặt xe thành công, giảm thời gian chờ trung bình của khách hàng, đồng thời tối ưu hoá thu nhập cho tài xế nhờ phân bổ hợp lý theo khu vực có nhu cầu cao.

### A.7. Bảng so sánh nhanh độ phức tạp và độ chính xác giữa các phương pháp dự báo

| Phương pháp | Độ phức tạp triển khai | Yêu cầu dữ liệu | Độ chính xác điển hình | Chi phí triển khai |
|---|---|---|---|---|
| Trung bình động | Rất thấp | Vài kỳ dữ liệu gần nhất | Trung bình | Miễn phí |
| San bằng số mũ đơn | Thấp | Không cần lưu lịch sử dài | Trung bình-khá | Miễn phí |
| Holt-Winters | Trung bình | 2-3 chu kỳ mùa vụ | Khá-tốt | Thấp (phần mềm cơ bản) |
| Hồi quy đa biến | Trung bình-cao | Dữ liệu biến độc lập đầy đủ, chất lượng cao | Tốt (nếu chọn đúng biến) | Trung bình |
| ARIMA | Cao | Dữ liệu chuỗi thời gian dài, ổn định | Tốt | Trung bình (cần chuyên môn) |
| Machine Learning (XGBoost, LSTM) | Rất cao | Dữ liệu lớn, nhiều biến, hạ tầng tính toán | Tốt-rất tốt (tuỳ bài toán) | Cao |

### A.8. Bài học thực hành: Khi nào nên dừng đầu tư vào độ phức tạp của mô hình dự báo

Một sai lầm phổ biến của doanh nghiệp khi bắt đầu chuyển đổi số là cho rằng mô hình càng phức tạp (Machine Learning) càng chính xác hơn mô hình đơn giản. Trên thực tế, nhiều nghiên cứu thực nghiệm (điển hình là cuộc thi dự báo M4 Competition năm 2018 với hơn 100,000 chuỗi thời gian thực tế) cho thấy sự cải thiện độ chính xác giữa mô hình phức tạp và mô hình đơn giản thường không tương xứng với chi phí và độ phức tạp tăng thêm, đặc biệt khi:

- Dữ liệu lịch sử không đủ dài (dưới 2-3 năm).
- Có nhiều SKU cần dự báo riêng lẻ (hàng nghìn SKU) mà không đủ nguồn lực để tinh chỉnh mô hình phức tạp cho từng SKU.
- Thị trường có biến động cấu trúc thường xuyên khiến mô hình phức tạp dễ bị overfitting vào dữ liệu lịch sử không còn phù hợp.

**Khuyến nghị thực hành**: SME và doanh nghiệp vừa nên bắt đầu với phương pháp đơn giản (san bằng số mũ, Holt-Winters), chỉ đầu tư vào Machine Learning khi đã có nền tảng dữ liệu vững chắc, đội ngũ kỹ thuật đủ năng lực duy trì mô hình, và đã chứng minh được lợi ích tài chính rõ ràng từ việc cải thiện độ chính xác dự báo (ví dụ: giảm chi phí tồn kho, giảm tỷ lệ hết hàng có thể lượng hoá được bằng tiền).

### A.9. Liên kết chéo với các file khác trong bộ tài liệu

Dự báo (Forecasting) là đầu vào quan trọng cho nhiều nội dung khác trong bộ tài liệu Quản trị Vận hành này:

- **File 03 - Quản trị chuỗi cung ứng**: Dự báo là nền tảng cho S&OP (Sales & Operations Planning) và CPFR, giúp giảm hiệu ứng Bullwhip khi các bên trong chuỗi cung ứng chia sẻ cùng một dự báo thống nhất.
- **File 04 - Quản trị tồn kho**: Dự báo nhu cầu là đầu vào trực tiếp để tính Safety Stock, ROP và EOQ; sai số dự báo càng lớn thì mức tồn kho an toàn cần thiết càng cao.
- **File 05 - Hoạch định năng lực**: Dự báo dài hạn là cơ sở cho Aggregate Planning và quyết định đầu tư năng lực sản xuất (Lead/Lag/Match strategy).
- **File 08 - Chiến lược bố trí mặt bằng**: Dự báo tăng trưởng quy mô kinh doanh ảnh hưởng đến quyết định thiết kế layout linh hoạt có khả năng mở rộng.

### A.10. Tổng kết chương

Dự báo không phải là một hoạt động một lần mà là một quy trình liên tục: đo lường, học hỏi, điều chỉnh. Doanh nghiệp thành công trong dự báo không phải là doanh nghiệp có mô hình toán học phức tạp nhất, mà là doanh nghiệp xây dựng được văn hoá tổ chức coi trọng dữ liệu, đo lường sai số một cách kỷ luật, và sẵn sàng điều chỉnh phương pháp khi bối cảnh thị trường thay đổi.

### A.11. Câu hỏi tự kiểm tra nhanh cuối chương

1. Điểm khác biệt cốt lõi giữa dự báo định tính và định lượng là gì?
2. Vì sao dự báo tổng hợp (aggregate) thường chính xác hơn dự báo chi tiết (disaggregate)?
3. Khi nào nên chuyển từ san bằng số mũ đơn sang Holt-Winters?
4. Tracking Signal dùng để phát hiện vấn đề gì trong mô hình dự báo?
5. Vì sao mô hình Machine Learning không phải lúc nào cũng vượt trội hơn mô hình thống kê truyền thống?

*(Hết file 07 - Dự báo trong Quản trị Vận hành)*
