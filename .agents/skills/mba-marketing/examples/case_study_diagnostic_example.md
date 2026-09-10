# Example: Strategic Diagnostic & Content Funnel Architecture for an F&B Startup

## Bối cảnh tình huống
Một chuỗi cà phê specialty tại Hà Nội đang gặp tình trạng chi phí cố định (mặt bằng, nhân sự) chiếm tới 62% doanh thu, trong khi tỷ lệ chuyển đổi bài post trên mạng xã hội thấp và không đo lường được hiệu quả nội dung.

## Bước 1: Khám phá & Định vị (Sử dụng 01_strategic_management & 07_sme_operations_playbook)
- **Chuẩn định mức F&B SME:**
  - Prime Cost (COGS + Nhân sự) chuẩn: `< 55%` doanh thu.
  - Hiện tại: `62%` -> Đang vượt ngưỡng an toàn nghiêm trọng.
- **Áp dụng Blue Ocean Strategy (ERRC Grid):**
  - **Eliminate:** Cắt bỏ menu đồ uống theo mùa phức tạp có hơn 15 nguyên liệu bảo quản ngắn ngày.
  - **Reduce:** Giảm diện tích không gian check-in rườm rà; chuyển dịch một phần sang takeaway/giao hàng văn phòng.
  - **Raise:** Chuẩn hóa tốc độ ra đồ peak hour `< 3 phút/cốc`.
  - **Create:** Gói Subscription cà phê tháng cho dân công sở lân cận (thu tiền trước).

## Bước 2: Mô hình hóa định lượng (Sử dụng calculate_metrics.py)
Chạy lệnh tính điểm hòa vốn:
```bash
python3 .agents/skills/mba-marketing/scripts/calculate_metrics.py bep \
  --fixed-costs 60000000 \
  --price 45000 \
  --variable-cost 15000
```
- **Kết quả:**
  - Đơn giá: 45,000 VND. Chi phí biến đổi: 15,000 VND.
  - Unit Contribution Margin: 30,000 VND (CM Ratio: 66.7%).
  - Sản lượng hòa vốn: `2,000 cốc/tháng` (tương đương ~67 cốc/ngày).
- **Trần ngân sách tiếp thị (CAC Ceiling):**
  - CAC tối đa cho khách hàng mới không được vượt quá `30,000 VND` để đảm bảo không lỗ ngay đơn hàng đầu tiên.

## Bước 3: Thiết kế Phễu Nội dung 3H (Sử dụng 02_strategy_architectures & 03_copywriting_creation)
- **Tỷ lệ phân bổ nội dung:**
  - **Hero (10%):** Chiến dịch "Thử mù hương vị Specialty Coffee" hợp tác cùng 2 micro-KOLs F&B.
  - **Hub (55%):** Chuỗi video TikTok hậu trường "1 ngày làm Barista tại xưởng rang", công thức pha cà phê tại nhà bằng bình Cold Brew. Sử dụng công thức Hook 3s + Body 20s + CTA.
  - **Help (25%):** Bài viết blog SEO và Infographic: "Phân biệt Robusta vs Arabica", "Top 5 lỗi khiến cà phê pha bị chua chát".
  - **Buffer (10%):** Bắt trend thời tiết Hà Nội (ngày mưa, lạnh) kết hợp ưu đãi giao hàng trong 15 phút.
