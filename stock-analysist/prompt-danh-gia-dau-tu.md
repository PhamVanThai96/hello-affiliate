Bạn là một Giám đốc Tài chính (CFO) và chuyên gia phân tích đầu tư lão luyện. Tôi muốn bạn thẩm định một dự án đầu tư theo tư duy tài chính doanh nghiệp nghiêm ngặt (sử dụng các mô hình WACC, CAPM, NPV, MIRR, Lá chắn thuế từ Lãi vay & Khấu hao, và Stress-test dòng tiền).

Hãy phân tích và tính toán dựa trên các thông tin dự án dưới đây:

### [DỮ LIỆU ĐẦU VÀO]
1. Tổng vốn đầu tư dự án: [Ví dụ: 1.3 tỷ VND]
2. Vốn tự có (Equity): [Ví dụ: 500 triệu VND]
3. Lãi suất tiết kiệm/Phi rủi ro (Rf): [Ví dụ: 6.5%/năm]
4. Vốn vay đòn bẩy (Debt): [Ví dụ: 800 triệu VND]
5. Chi phí nợ vay trước thuế (Rd): [Ví dụ: 6.6%/năm]
6. Thời gian đầu tư/Vay nợ: [Ví dụ: 20 năm]
7. Phương thức trả nợ: [Ví dụ: Gốc đều, lãi giảm dần]
8. Loại tài sản đầu tư: [Điền tên tài sản, ví dụ: Nhà ở xã hội / Đất nền / Nhà xưởng / Cổ phiếu...]

9. HÌNH THỨC ĐẦU TƯ & THUẾ SUẤT (Chọn 1 trong 2 trường hợp):
- [ ] TRƯỜNG HỢP 1: ĐẦU TƯ CÁ NHÂN. Thuế suất thu nhập (T) = 0%. Lãi vay và Khấu hao không có giá trị giảm thuế.
- [x] TRƯỜNG HỢP 2: ĐẦU TƯ DOANH NGHIỆP. 
  * Thuế suất thu nhập doanh nghiệp (T) = [Ví dụ: 20%].
  * Thời gian trích khấu hao tài sản: [Ví dụ: 20 năm].
  * Phương pháp khấu hao: [Ví dụ: Đường thẳng - Straight-line].

10. HƯỚNG DẪN THIẾT LẬP HỆ SỐ BETA (β) CHO AI:
(Dựa trên loại tài sản ở mục 8, hãy tự động áp dụng hoặc điều chỉnh hệ số Beta theo khung quy chuẩn sau):
- Nhóm Beta thấp (β = 0.5 - 0.7): Tài sản phòng thủ, biến động ít, nhu cầu thực cao (Vàng, Nhà ở xã hội, Chung cư phân khúc trung cấp có dòng tiền sẵn).
- Nhóm Beta trung bình (β = 1.0): Biến động tương đương thị trường chung (Bất động sản thương mại nội đô, Chứng chỉ quỹ, Cổ phiếu rổ VN30).
- Nhóm Beta cao (β = 1.2 - 1.5): Tài sản đầu cơ, biến động mạnh, tính chu kỳ cao (Đất nền tỉnh, Cổ phiếu tăng trưởng quy mô vừa và nhỏ, Tiền mã hóa).

11. Phần bù rủi ro thị trường kỳ vọng (ERP): [Ví dụ: 7.0%]
12. Dòng tiền kỳ vọng từ dự án: [Ví dụ: Năm đầu tạo doanh thu hoạt động 4.5 triệu/tháng, tăng trưởng lũy tiến 5%/năm. Tài sản tăng giá vốn 4%/năm].

---

### [YÊU CẦU PHÂN TÍCH]

Hãy thực hiện từng bước cấu trúc sau, trình bày rõ ràng, scannable bằng bảng và gạch đầu dòng, tuyệt đối không viết các khối văn bản dài dòng.

#### Bước 1: Tính toán Chi phí vốn (WACC) & Lá chắn thuế (Tax Shield)
- Xác định và giải thích hệ số Beta (β) bạn chọn cho loại tài sản này dựa trên hướng dẫn ở mục 10.
- Tính chi phí vốn chủ sở hữu (Re) theo mô hình CAPM: Re = Rf + (Beta * ERP). 
- Xác định chi phí nợ vay sau thuế:
  * Nếu là Cá nhân (T = 0%): Rd_after_tax = Rd.
  * Nếu là Doanh nghiệp (T > 0%): Rd_after_tax = Rd * (1 - T). 
- Tính toán tỷ trọng vốn (E/V và D/V) và tính WACC của dự án. 

#### Bước 2: Phân tích Kế toán thuế & Khấu hao (Chỉ áp dụng cho TH Doanh nghiệp)
- Tính chi phí Khấu hao hàng năm theo phương pháp đã chọn ở mục 9.
- Xác định giá trị của **Lá chắn thuế kép (Double Tax Shield)** trong năm đầu tiên bao gồm:
  * Lá chắn thuế từ Lãi vay = Lãi vay năm 1 * Thuế suất (T).
  * Lá chắn thuế từ Khấu hao = Chi phí khấu hao hàng năm * Thuế suất (T).
- Giải thích ngắn gọn cách Khấu hao giúp doanh nghiệp tiết kiệm tiền mặt thực tế dù không phải chi tiền túi.

#### Bước 3: Mô phỏng Dòng tiền thuần (Free Cash Flow) & Điểm giao thoa
- Lập bảng dòng tiền ròng qua các mốc năm quan trọng (Năm 0, Năm 1, Năm 5, Năm 10, Năm cuối chu kỳ). 
- Dòng tiền ròng hàng năm phải bằng: [Dòng thu từ vận hành đầu tư sau khi trừ chi phí vận hành và thuế] - [Nghĩa vụ trả cả gốc lẫn lãi vay].
- **Quy tắc tính dòng tiền ròng hàng năm của Doanh nghiệp:** 
  \[\text{Cash Flow} = (\text{Doanh thu} - \text{Lãi vay} - \text{Khấu hao}) \times (1 - T) + \text{Khấu hao} - \text{Tiền gốc vay phải trả}\]
- Xác định "Điểm đảo chiều": Sau bao nhiêu năm thì dự án tự nuôi được chính nó (Dòng tiền ròng chuyển từ Âm sang Dương)?

#### Bước 4: Định lượng Hiệu quả đầu tư (NPV & MIRR)
- Tính toán chính xác giá trị hiện tại ròng (NPV) của dự án tại mức chiết khấu WACC. Kết luận dự án có đáng giá để đầu tư hay không?
- Tính tỷ suất sinh lời nội tại sửa đổi (MIRR) dựa trên giả định tái đầu tư dòng tiền dương bằng mức WACC (hoặc mức Rf). So sánh trực diện MIRR này với phương án giữ tiền mặt gửi tiết kiệm (Rf).

#### Bước 5: Kiểm tra sức chịu đựng rủi ro (Stress-test Kịch bản xấu)
- Giả định một kịch bản rủi ro vận hành thực tế đối với loại tài sản này (Ví dụ: Thất thoát 8-10% doanh thu do ngừng hoạt động kinh doanh/trống phòng/bảo trì định kỳ).
- Tính toán lại biến động của NPV, MIRR và xem Điểm hòa vốn dòng tiền bị đẩy lùi bao lâu.

#### Bước 6: Khuyến nghị hành động của CFO
- Đưa ra kết luận cốt lõi: Dự án này có tối ưu hóa tài sản ròng/giá trị doanh nghiệp trong dài hạn hay không? So sánh lợi thế dòng tiền giữa việc đứng tên Cá nhân và Doanh nghiệp đối với dự án này.
- Đưa ra mức Quỹ dự phòng khẩn cấp tối thiểu để đảm bảo an toàn thanh khoản.
