#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tạo file Excel Content Calendar (phiên bản THEO TUẦN) + Content Pillar theo mô hình 3H
Khác biệt so với bản gốc: Mỗi TUẦN trong tháng được gán cho 1 Content Pillar duy nhất
(luân phiên 4 Pillar / 4-5 tuần), thay vì mỗi Pillar trải dài cả tháng.
Thương hiệu mẫu: "Xanh Garden" - Rau củ hữu cơ giao tận nhà
Dựa trên Module 2 - Chiến lược Nội dung (calendar-3H.md)
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.comments import Comment
import datetime
import calendar
from collections import defaultdict

# ============================================================
# 0. CẤU HÌNH CHUNG
# ============================================================

OUT_PATH = "/Users/phamvannam/Documents/GitHub/hello-affiliate/content-marketing/code/Content_Calendar_3H_TheoTuan_XanhGarden.xlsx"

YEAR = 2026
MONTH = 9

PILLAR_SHEETS = [
    "Pillar 1 - An toan TP",
    "Pillar 2 - Meo nau an",
    "Pillar 3 - Nong trai",
    "Pillar 4 - San pham",
]

PILLAR_TITLES = {
    "Pillar 1 - An toan TP": "PILLAR 1: An toàn thực phẩm cho gia đình",
    "Pillar 2 - Meo nau an": "PILLAR 2: Mẹo nấu ăn nhanh cho mẹ bận rộn",
    "Pillar 3 - Nong trai": "PILLAR 3: Câu chuyện nông trại",
    "Pillar 4 - San pham": "PILLAR 4: Sản phẩm & Ưu đãi Xanh Garden",
}

PILLAR_COLORS = {
    "Pillar 1 - An toan TP": "C6E0B4",
    "Pillar 2 - Meo nau an": "FFE699",
    "Pillar 3 - Nong trai": "BDD7EE",
    "Pillar 4 - San pham": "F8CBAD",
}

PILLAR_HEADER_COLORS = {
    "Pillar 1 - An toan TP": "548235",
    "Pillar 2 - Meo nau an": "BF8F00",
    "Pillar 3 - Nong trai": "2E75B6",
    "Pillar 4 - San pham": "C55A11",
}

H3_COLORS = {"Hero": "FF0000", "Hub": "2E75B6", "Hygiene": "70AD47"}
H3_FILL = {"Hero": "FFC7CE", "Hub": "BDD7EE", "Hygiene": "E2EFDA"}

CHANNELS = ["Facebook", "Zalo OA", "Website", "TikTok", "Email"]
FUNNEL = ["TOFU", "MOFU", "BOFU"]
STATUS_LIST = ["Draft", "Review", "Approved", "Published"]
H3_LIST = ["Hero", "Hub", "Hygiene"]
PERSONA = "Chị Lan - Mẹ bỉm sữa quan tâm sức khỏe gia đình"

# ============================================================
# 1. DỮ LIỆU CONTENT CLUSTER (giữ nguyên nội dung, CHƯA gán ngày cụ thể)
# Ngày đăng sẽ được TÍNH LẠI theo nguyên tắc: mỗi Pillar chỉ đăng trong
# đúng 1 tuần của tháng (luân phiên Pillar 1->Tuần 1, Pillar 2->Tuần 2, ...)
# ============================================================

PILLAR_DATA_RAW = {
    "Pillar 1 - An toan TP": [
        dict(ten="3 dấu hiệu rau ngậm hóa chất mẹ cần biết", loai="Hygiene", funnel="TOFU",
             tukhoa="rau ngậm hóa chất, cách nhận biết rau bẩn", tone="Gần gũi, tin cậy, có dẫn chứng khoa học",
             do_dai="500-700 từ", outline="Hook: câu chuyện mẹ đi chợ lo lắng -> 3 dấu hiệu nhận biết (màu sắc, mùi, độ giòn) -> lời khuyên chọn rau an toàn",
             cta="Đăng ký nhận rau kiểm định VietGAP", kenh="Facebook", status="Published"),
        dict(ten="Rau VietGAP là gì? Vì sao Xanh Garden chọn chuẩn này", loai="Hygiene", funnel="MOFU",
             tukhoa="rau VietGAP là gì, chuẩn rau an toàn", tone="Chuyên nghiệp, dễ hiểu, không dùng thuật ngữ khó",
             do_dai="700-900 từ", outline="Định nghĩa VietGAP -> So sánh với rau thường -> Quy trình kiểm định của Xanh Garden",
             cta="Xem chứng nhận VietGAP của Xanh Garden", kenh="Website", status="Published"),
        dict(ten="Câu chuyện truy xuất nguồn gốc qua mã QR", loai="Hub", funnel="MOFU",
             tukhoa="truy xuất nguồn gốc rau, QR code thực phẩm", tone="Minh bạch, tin cậy, có tính giáo dục",
             do_dai="600-800 từ + video ngắn", outline="Demo quét mã QR trên bao bì -> Thông tin hiển thị (ngày thu hoạch, nông trại) -> Cam kết minh bạch",
             cta="Trải nghiệm quét QR trên đơn hàng tiếp theo", kenh="TikTok", status="Published"),
        dict(ten="Thử thách: Mẹ nào phân biệt được rau sạch bằng mắt thường?", loai="Hub", funnel="TOFU",
             tukhoa="phân biệt rau sạch, rau organic", tone="Vui vẻ, tương tác, khuyến khích comment",
             do_dai="Video ngắn 30-60s", outline="Đưa ra 2 loại rau (sạch/không rõ nguồn) -> Đố người xem đoán -> Reveal đáp án + giải thích",
             cta="Comment dự đoán để nhận ưu đãi", kenh="TikTok", status="Approved"),
        dict(ten="Giấy chứng nhận an toàn thực phẩm - Xanh Garden có gì khác biệt?", loai="Hygiene", funnel="BOFU",
             tukhoa="chứng nhận an toàn thực phẩm, rau sạch có giấy tờ", tone="Chuyên nghiệp, minh bạch",
             do_dai="500-600 từ", outline="Danh sách chứng nhận hiện có -> Quy trình audit định kỳ -> Cam kết hoàn tiền nếu phát hiện vi phạm",
             cta="Xem đầy đủ hồ sơ chứng nhận", kenh="Website", status="Approved"),
        dict(ten="Mẹ có biết: Rửa rau đúng cách để loại bỏ tối đa dư lượng?", loai="Hygiene", funnel="TOFU",
             tukhoa="cách rửa rau sạch, loại bỏ dư lượng thuốc trừ sâu", tone="Hữu ích, thân thiện, dễ áp dụng",
             do_dai="400-600 từ", outline="3 bước rửa rau chuẩn -> Sai lầm thường gặp -> Mẹo ngâm nước muối/baking soda",
             cta="Lưu bài để áp dụng ngay", kenh="Facebook", status="Draft"),
        dict(ten="Đối thoại với chuyên gia dinh dưỡng: Rau củ nào tốt nhất cho trẻ nhỏ", loai="Hero", funnel="MOFU",
             tukhoa="rau củ tốt cho trẻ nhỏ, dinh dưỡng cho bé", tone="Tin cậy, chuyên môn cao nhưng gần gũi",
             do_dai="Video 5-7 phút, phát trên nhiều kênh", outline="Phỏng vấn chuyên gia dinh dưỡng -> Top 5 loại rau tốt cho bé -> Liên hệ sản phẩm Xanh Garden",
             cta="Đặt combo rau củ cho bé ưu đãi tháng này", kenh="Facebook", status="Draft"),
    ],
    "Pillar 2 - Meo nau an": [
        dict(ten="Thực đơn 15 phút cho bé tuần này", loai="Hub", funnel="MOFU",
             tukhoa="thực đơn nhanh cho bé, nấu ăn 15 phút", tone="Gần gũi, thực tế, tiết kiệm thời gian",
             do_dai="600-800 từ + hình ảnh từng bước", outline="3 món ăn 15 phút -> Nguyên liệu có sẵn trong combo Xanh Garden -> Mẹo sơ chế nhanh",
             cta="Đặt hàng nguyên liệu trong bài", kenh="Zalo OA", status="Published"),
        dict(ten="Công thức súp rau củ dinh dưỡng cho bé ăn dặm", loai="Hub", funnel="MOFU",
             tukhoa="súp rau củ cho bé ăn dặm, công thức ăn dặm", tone="Ấm áp, chăm chút, chuyên môn dinh dưỡng",
             do_dai="500-700 từ", outline="Nguyên liệu cần chuẩn bị -> 4 bước nấu súp -> Lưu ý dinh dưỡng theo độ tuổi bé",
             cta="Xem trọn bộ thực đơn ăn dặm trên Website", kenh="Website", status="Published"),
        dict(ten="Cách bảo quản rau tươi lâu hơn trong tủ lạnh", loai="Hygiene", funnel="TOFU",
             tukhoa="bảo quản rau tươi trong tủ lạnh, mẹo giữ rau lâu", tone="Hữu ích, dễ áp dụng ngay",
             do_dai="400-500 từ", outline="Sai lầm thường gặp khi bảo quản -> 5 mẹo giữ rau tươi 7 ngày -> Loại hộp/túi nên dùng",
             cta="Lưu bài lại để áp dụng", kenh="Facebook", status="Published"),
        dict(ten="Series: Vào bếp cùng Xanh Garden - Tập 1 Canh chua thanh mát", loai="Hub", funnel="MOFU",
             tukhoa="công thức canh chua, nấu ăn cùng Xanh Garden", tone="Vui vẻ, gần gũi như bạn bè chia sẻ",
             do_dai="Video 3-5 phút", outline="Giới thiệu nguyên liệu combo tuần -> Hướng dẫn nấu từng bước -> Kêu gọi đón tập tiếp theo",
             cta="Theo dõi để xem tập tiếp theo", kenh="TikTok", status="Approved"),
        dict(ten="5 sai lầm khi sơ chế rau khiến mất chất dinh dưỡng", loai="Hygiene", funnel="TOFU",
             tukhoa="sơ chế rau đúng cách, giữ dinh dưỡng khi nấu", tone="Hữu ích, có căn cứ khoa học",
             do_dai="600-700 từ", outline="5 sai lầm phổ biến (cắt quá nhỏ, ngâm quá lâu...) -> Cách khắc phục -> Mẹo giữ vitamin",
             cta="Chia sẻ bài cho bạn bè cùng biết", kenh="Facebook", status="Approved"),
        dict(ten="Thực đơn 1 tuần cân bằng dinh dưỡng cho cả nhà", loai="Hero", funnel="MOFU",
             tukhoa="thực đơn 1 tuần cho gia đình, thực đơn dinh dưỡng", tone="Chuyên môn, đầu tư kỹ, hình ảnh đẹp",
             do_dai="E-book/Infographic dài, đầu tư thiết kế cao", outline="Thực đơn chi tiết 7 ngày -> Danh sách nguyên liệu theo combo Xanh Garden -> Ưu đãi đặt trọn combo tuần",
             cta="Đặt combo thực đơn 1 tuần - giảm 15%", kenh="Website", status="Draft"),
        dict(ten="Mẹo giữ màu xanh đẹp mắt khi luộc rau", loai="Hygiene", funnel="TOFU",
             tukhoa="luộc rau không bị vàng, giữ màu rau xanh", tone="Ngắn gọn, hữu ích tức thời",
             do_dai="300-400 từ", outline="Nguyên nhân rau bị vàng khi luộc -> 3 mẹo giữ màu xanh -> Áp dụng thử ngay",
             cta="Thử ngay và feedback cho Xanh Garden", kenh="Zalo OA", status="Draft"),
    ],
    "Pillar 3 - Nong trai": [
        dict(ten="Ghé thăm nông trại đối tác tại Đà Lạt", loai="Hub", funnel="TOFU",
             tukhoa="nông trại rau organic Đà Lạt, tham quan nông trại", tone="Chân thực, ấm áp, có tính kể chuyện",
             do_dai="Video 4-6 phút", outline="Hành trình đến nông trại -> Quy trình canh tác hữu cơ -> Gặp gỡ người nông dân",
             cta="Theo dõi để xem tập tiếp theo", kenh="Facebook", status="Published"),
        dict(ten="Người nông dân đứng sau lô rau của bạn", loai="Hub", funnel="MOFU",
             tukhoa="câu chuyện nông dân, người trồng rau hữu cơ", tone="Cảm xúc, chân thành, tôn trọng người lao động",
             do_dai="600-800 từ + ảnh chân dung", outline="Chân dung 1 nông dân cụ thể -> Câu chuyện gắn bó với nghề -> Cam kết thu mua công bằng",
             cta="Đọc thêm câu chuyện nông trại khác", kenh="Website", status="Published"),
        dict(ten="Quy trình thu hoạch - đóng gói trong 24h", loai="Hygiene", funnel="MOFU",
             tukhoa="quy trình đóng gói rau sạch, rau giao trong ngày", tone="Chuyên nghiệp, minh bạch",
             do_dai="500-600 từ", outline="Timeline từ thu hoạch đến giao hàng -> Tiêu chuẩn đóng gói giữ tươi -> Cam kết giao trong 24h",
             cta="Đặt hàng để nhận rau tươi trong ngày", kenh="Website", status="Published"),
        dict(ten="Một ngày làm nông dân cùng Xanh Garden (Trải nghiệm KOL)", loai="Hero", funnel="TOFU",
             tukhoa="trải nghiệm nông trại, KOL trải nghiệm nông nghiệp hữu cơ", tone="Thú vị, chân thực, lan tỏa cảm hứng",
             do_dai="Video 7-10 phút, đầu tư sản xuất cao, hợp tác KOL", outline="KOL trải nghiệm trồng/thu hoạch rau -> Cảm nhận thật về quy trình hữu cơ -> Giới thiệu chiến dịch Trung Thu Xanh Garden",
             cta="Tham gia minigame nhận combo rau miễn phí", kenh="TikTok", status="Approved"),
        dict(ten="Mùa nào rau nào? Lịch thu hoạch theo mùa vụ", loai="Hygiene", funnel="TOFU",
             tukhoa="rau theo mùa, lịch mùa vụ rau củ", tone="Hữu ích, giáo dục nhẹ nhàng",
             do_dai="500-600 từ + infographic", outline="Bảng mùa vụ các loại rau chính -> Vì sao nên ăn rau theo mùa -> Gợi ý combo theo mùa hiện tại",
             cta="Đặt combo rau đúng mùa tháng này", kenh="Facebook", status="Approved"),
        dict(ten="Cam kết không hóa chất - Xanh Garden kiểm tra đất và nước ra sao?", loai="Hub", funnel="MOFU",
             tukhoa="kiểm tra đất trồng hữu cơ, quy trình kiểm định nông trại", tone="Chuyên môn, minh bạch, tạo niềm tin",
             do_dai="600-700 từ", outline="Quy trình kiểm tra đất/nước định kỳ -> Đối tác kiểm định độc lập -> Kết quả gần nhất",
             cta="Xem báo cáo kiểm định mới nhất", kenh="Website", status="Draft"),
        dict(ten="Video ngắn: Bình minh trên nông trại hữu cơ", loai="Hygiene", funnel="TOFU",
             tukhoa="nông trại hữu cơ, video thư giãn nông trại", tone="Nhẹ nhàng, thư giãn, aesthetic",
             do_dai="Video ngắn 15-30s", outline="Cảnh bình minh + thu hoạch sớm -> Nhạc nền nhẹ nhàng -> Caption ngắn gợi cảm xúc trong lành",
             cta="Lưu video để xem lại lúc căng thẳng", kenh="TikTok", status="Draft"),
    ],
    "Pillar 4 - San pham": [
        dict(ten="Ra mắt combo Trung Thu: Rau củ quả biếu tặng cao cấp", loai="Hero", funnel="MOFU",
             tukhoa="combo rau củ Trung Thu, quà biếu Trung Thu sức khỏe", tone="Sang trọng, ấm áp, gắn với mùa vụ",
             do_dai="Chiến dịch đa kênh: video + bài viết + KOL", outline="Giới thiệu bộ combo Trung Thu -> Thông điệp 'món quà sức khỏe' -> Ưu đãi đặt trước",
             cta="Đặt combo Trung Thu ngay - ưu đãi 20% đặt sớm", kenh="Facebook", status="Published"),
        dict(ten="So sánh chi phí: Mua rau Xanh Garden vs đi chợ truyền thống", loai="Hygiene", funnel="MOFU",
             tukhoa="chi phí mua rau online vs chợ, so sánh giá rau sạch", tone="Khách quan, có số liệu cụ thể",
             do_dai="600-800 từ + bảng so sánh", outline="Bảng so sánh giá theo từng loại rau -> Chi phí ẩn khi đi chợ (thời gian, xăng xe) -> Kết luận khách quan",
             cta="Tính thử chi phí tiết kiệm với Xanh Garden", kenh="Website", status="Published"),
        dict(ten="Đánh giá từ khách hàng thật: 3 tháng dùng Xanh Garden", loai="Hub", funnel="BOFU",
             tukhoa="review Xanh Garden, đánh giá khách hàng rau sạch", tone="Chân thực, không seeding, có hình ảnh thật",
             do_dai="500-700 từ + testimonial video ngắn", outline="Phỏng vấn 3 khách hàng thân thiết -> Trải nghiệm thực tế trước/sau -> Lý do tiếp tục sử dụng",
             cta="Đăng ký trải nghiệm 7 ngày đầu ưu đãi", kenh="Facebook", status="Approved"),
        dict(ten="Chính sách đổi trả trong 30 phút - Cam kết của Xanh Garden", loai="Hygiene", funnel="BOFU",
             tukhoa="chính sách đổi trả rau, đổi trả nhanh 30 phút", tone="Rõ ràng, đáng tin cậy, giảm lo lắng khi mua online",
             do_dai="400-500 từ", outline="Quy trình đổi trả 3 bước -> Trường hợp được áp dụng -> Hotline ưu tiên khung giờ nấu ăn 17h-19h",
             cta="Lưu số hotline CSKH ưu tiên", kenh="Zalo OA", status="Approved"),
        dict(ten="Ưu đãi thành viên tháng: Tích điểm đổi combo miễn phí", loai="Hub", funnel="BOFU",
             tukhoa="chương trình thành viên Xanh Garden, tích điểm đổi quà", tone="Hào hứng, tạo động lực mua lại",
             do_dai="400-600 từ", outline="Giới thiệu cơ chế tích điểm -> Bảng đổi điểm -> Deadline ưu đãi trong tháng",
             cta="Kiểm tra điểm tích lũy của bạn ngay", kenh="Zalo OA", status="Draft"),
        dict(ten="Hậu trường: Vì sao giá rau Xanh Garden như hiện tại?", loai="Hygiene", funnel="MOFU",
             tukhoa="giá rau hữu cơ vì sao đắt, minh bạch giá thành", tone="Minh bạch, thẳng thắn, xây dựng niềm tin",
             do_dai="500-600 từ", outline="Phân tích cấu thành chi phí -> So sánh với rau không rõ nguồn gốc -> Cam kết giá trị nhận được",
             cta="Đặt hàng để tự trải nghiệm giá trị", kenh="Website", status="Draft"),
        dict(ten="FAQ: Khu vực nào Xanh Garden giao hàng trong 2 giờ?", loai="Hygiene", funnel="BOFU",
             tukhoa="khu vực giao hàng Xanh Garden, giao rau trong 2 giờ", tone="Ngắn gọn, thực tế",
             do_dai="300 từ", outline="Bản đồ khu vực giao nhanh -> Phí giao hàng theo khu vực -> Link kiểm tra khu vực của bạn",
             cta="Kiểm tra khu vực giao hàng của bạn", kenh="Website", status="Draft"),
    ],
}

# ============================================================
# 2. TÍNH LỊCH THEO TUẦN (mỗi tuần = 1 Pillar, luân phiên)
# ============================================================

first_weekday, num_days = calendar.monthrange(YEAR, MONTH)  # first_weekday: 0=Mon

# Xác định các "tuần lịch" trong tháng: mỗi tuần bắt đầu từ Thứ 2 và kết thúc Chủ Nhật,
# gồm cả các ngày đầu/cuối tháng thuộc tuần giao (dùng để chia cột calendar), nhưng khi
# gán Pillar cho tuần, ta chỉ tính theo "tuần chứa ngày nào trong tháng" theo thứ tự xuất hiện.
weeks = []  # list of list-of-day-numbers (chỉ ngày thuộc tháng)
current_week = []
for day in range(1, num_days + 1):
    wd = (first_weekday + (day - 1)) % 7  # 0=Mon..6=Sun
    current_week.append(day)
    if wd == 6 or day == num_days:  # Chủ nhật hoặc ngày cuối tháng -> đóng tuần
        weeks.append(current_week)
        current_week = []

num_weeks = len(weeks)
print(f"Tháng {MONTH}/{YEAR} có {num_days} ngày, chia thành {num_weeks} tuần lịch.")
for i, w in enumerate(weeks, start=1):
    print(f"  Tuần {i}: ngày {w[0]}-{w[-1]} ({len(w)} ngày)")

# Gán Pillar cho từng tuần theo thứ tự luân phiên (nếu số tuần > số pillar thì lặp lại)
week_to_pillar = {}
for i in range(num_weeks):
    week_to_pillar[i + 1] = PILLAR_SHEETS[i % len(PILLAR_SHEETS)]

# Với mỗi Pillar, lấy danh sách ngày thuộc (các) tuần được gán cho pillar đó,
# rồi trải đều các cluster của pillar vào các ngày đó (ưu tiên các ngày làm việc T2-T7,
# CN dùng cho Hero/nghỉ nếu cần), cách nhau hợp lý.
pillar_to_weeks = defaultdict(list)
for wk_num, pillar in week_to_pillar.items():
    pillar_to_weeks[pillar].append(wk_num)

def workdays_first(day_list):
    """Sắp xếp ngày trong tuần ưu tiên các ngày không phải Chủ nhật trước, để phân bài đều,
    Chủ nhật để dành cho Hero/nghỉ nếu số bài không cần dùng hết."""
    def sort_key(day):
        wd = (first_weekday + (day - 1)) % 7
        return (1 if wd == 6 else 0, day)
    return sorted(day_list, key=sort_key)

PILLAR_DATA = {}
cluster_registry = []

RESP_CYCLE = ["Writer A", "Writer B", "Designer C", "Writer A", "Content Lead", "Writer B", "Designer C", "Writer A"]
KPI_BY_3H = {
    "Hero": "Reach > 50,000; Brand Lift +10%; Share of Voice",
    "Hub": "Engagement rate > 5%; Returning visitor +; Watch time",
    "Hygiene": "Organic traffic; Time on page > 1'30\"; Giảm câu hỏi CSKH",
}

for pillar in PILLAR_SHEETS:
    items = PILLAR_DATA_RAW[pillar]
    assigned_weeks = pillar_to_weeks[pillar]
    # Gom toàn bộ ngày thuộc các tuần được gán cho pillar này
    all_days = []
    for wk in assigned_weeks:
        all_days.extend(weeks[wk - 1])
    all_days = workdays_first(all_days)

    n = len(items)
    if len(all_days) >= n:
        chosen_days = sorted(all_days[:n]) if n <= len(all_days) else sorted(all_days)
        # Trải đều thay vì dồn liền: lấy n ngày cách đều trong all_days (đã ưu tiên workday)
        # Cách đơn giản & ổn định: chọn theo bước nhảy đều trên danh sách toàn bộ ngày (sorted theo ngày thực)
        sorted_all = sorted(all_days)
        step = len(sorted_all) / n
        chosen_days = sorted({sorted_all[min(int(i * step), len(sorted_all) - 1)] for i in range(n)})
        # Nếu do trùng lặp mà thiếu ngày, bổ sung từ các ngày chưa dùng
        if len(chosen_days) < n:
            remaining = [d for d in sorted_all if d not in chosen_days]
            for d in remaining:
                chosen_days.add(d)
                if len(chosen_days) == n:
                    break
        chosen_days = sorted(chosen_days)
    else:
        # Nhiều bài hơn số ngày trong tuần -> cho phép nhiều bài/ngày, lặp vòng qua all_days
        sorted_all = sorted(all_days) if all_days else [1]
        chosen_days = [sorted_all[i % len(sorted_all)] for i in range(n)]

    new_items = []
    for idx, item in enumerate(items):
        day_num = chosen_days[idx] if idx < len(chosen_days) else chosen_days[-1]
        ngay = datetime.date(YEAR, MONTH, day_num)
        new_item = dict(item)
        new_item["ngay"] = ngay
        new_items.append(new_item)
    PILLAR_DATA[pillar] = new_items

# ============================================================
# 3. STYLE HELPERS
# ============================================================

THIN = Side(style="thin", color="B7B7B7")
BORDER_ALL = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
THICK_BLACK = Side(style="medium", color="404040")

TITLE_FONT = Font(name="Calibri", size=16, bold=True, color="FFFFFF")
HEADER_FONT = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
NORMAL_FONT = Font(name="Calibri", size=10)
BOLD_FONT = Font(name="Calibri", size=10, bold=True)

WRAP_TOP = Alignment(wrap_text=True, vertical="top", horizontal="left")
CENTER = Alignment(wrap_text=True, vertical="center", horizontal="center")

def style_header_row(ws, row, ncols, fill_hex):
    fill = PatternFill("solid", fgColor=fill_hex)
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = HEADER_FONT
        cell.fill = fill
        cell.alignment = CENTER
        cell.border = BORDER_ALL

def autofit(ws, widths):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w

# ============================================================
# 4. TẠO WORKBOOK
# ============================================================

wb = openpyxl.Workbook()
wb.remove(wb.active)

PILLAR_COLUMNS = [
    ("Mã Cluster", 12),
    ("Tên bài/Chủ đề", 34),
    ("Loại 3H", 10),
    ("Mục tiêu phễu\n(TOFU/MOFU/BOFU)", 14),
    ("Persona mục tiêu", 26),
    ("Từ khóa chính", 26),
    ("Tone giọng điệu", 26),
    ("Độ dài mong muốn", 20),
    ("Outline/Dàn ý chính", 40),
    ("CTA mong muốn", 26),
    ("Kênh đăng", 12),
    ("Tuần đăng", 10),
    ("Ngày đăng", 12),
    ("Deadline", 12),
    ("Người phụ trách", 16),
    ("Trạng thái", 12),
    ("KPI dự kiến", 22),
]

# ------------------------------------------------------------
# 4.1 Tạo 4 sheet Content Pillar
# ------------------------------------------------------------
for sheet_name in PILLAR_SHEETS:
    ws = wb.create_sheet(sheet_name)
    header_color = PILLAR_HEADER_COLORS[sheet_name]
    light_color = PILLAR_COLORS[sheet_name]
    assigned_weeks = pillar_to_weeks[sheet_name]
    weeks_label = ", ".join(f"Tuần {w}" for w in assigned_weeks)

    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(PILLAR_COLUMNS))
    title_cell = ws.cell(row=1, column=1, value=PILLAR_TITLES[sheet_name])
    title_cell.font = TITLE_FONT
    title_cell.fill = PatternFill("solid", fgColor=header_color)
    title_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 28

    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=len(PILLAR_COLUMNS))
    sub_cell = ws.cell(row=2, column=1,
        value=f"Persona: {PERSONA}  |  Thương hiệu: Xanh Garden  |  Tháng: {MONTH}/{YEAR}  |  Pillar này đăng vào: {weeks_label}")
    sub_cell.font = Font(italic=True, size=10, color="404040")
    sub_cell.alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[2].height = 18

    header_row = 3
    for c, (name, width) in enumerate(PILLAR_COLUMNS, start=1):
        ws.cell(row=header_row, column=c, value=name)
    style_header_row(ws, header_row, len(PILLAR_COLUMNS), header_color)
    ws.row_dimensions[header_row].height = 32

    autofit(ws, [w for _, w in PILLAR_COLUMNS])
    ws.freeze_panes = ws.cell(row=header_row + 1, column=3).coordinate

    items = PILLAR_DATA[sheet_name]
    for idx, item in enumerate(items, start=1):
        r = header_row + idx
        ma_cluster = f"{sheet_name.split(' ')[1]}-{idx:02d}"
        ngay = item["ngay"]
        deadline = ngay - datetime.timedelta(days=2)
        responsible = RESP_CYCLE[(idx - 1) % len(RESP_CYCLE)]
        kpi = KPI_BY_3H[item["loai"]]
        # Xác định tuần thực tế của ngày đăng
        wk_of_day = next(w for w in range(1, num_weeks + 1) if ngay.day in weeks[w - 1])

        row_values = [
            ma_cluster, item["ten"], item["loai"], item["funnel"], PERSONA,
            item["tukhoa"], item["tone"], item["do_dai"], item["outline"], item["cta"],
            item["kenh"], f"Tuần {wk_of_day}", ngay, deadline, responsible, item["status"], kpi,
        ]
        for c, val in enumerate(row_values, start=1):
            cell = ws.cell(row=r, column=c, value=val)
            cell.font = NORMAL_FONT
            cell.alignment = WRAP_TOP
            cell.border = BORDER_ALL
            if c in (13, 14):
                cell.number_format = "dd/mm/yyyy"

        row_fill = PatternFill("solid", fgColor=light_color)
        for c in range(1, len(PILLAR_COLUMNS) + 1):
            if c != 3:
                ws.cell(row=r, column=c).fill = row_fill

        h3_cell = ws.cell(row=r, column=3)
        h3_cell.fill = PatternFill("solid", fgColor=H3_FILL[item["loai"]])
        h3_cell.font = Font(bold=True, color=H3_COLORS[item["loai"]], size=10)
        h3_cell.alignment = CENTER

        cluster_registry.append({
            "pillar_sheet": sheet_name, "pillar_title": PILLAR_TITLES[sheet_name],
            "row": r, "ma_cluster": ma_cluster, "ten": item["ten"], "loai": item["loai"],
            "kenh": item["kenh"], "ngay": ngay, "funnel": item["funnel"], "status": item["status"],
            "week": wk_of_day,
        })

    dv_3h = DataValidation(type="list", formula1='"Hero,Hub,Hygiene"', allow_blank=False)
    dv_kenh = DataValidation(type="list", formula1=f'"{",".join(CHANNELS)}"', allow_blank=False)
    dv_status = DataValidation(type="list", formula1=f'"{",".join(STATUS_LIST)}"', allow_blank=False)
    dv_funnel = DataValidation(type="list", formula1=f'"{",".join(FUNNEL)}"', allow_blank=False)
    last_row = header_row + len(items)
    ws.add_data_validation(dv_3h); ws.add_data_validation(dv_kenh)
    ws.add_data_validation(dv_status); ws.add_data_validation(dv_funnel)
    dv_3h.add(f"C{header_row+1}:C{last_row}")
    dv_kenh.add(f"K{header_row+1}:K{last_row}")
    dv_status.add(f"P{header_row+1}:P{last_row}")
    dv_funnel.add(f"D{header_row+1}:D{last_row}")

    status_col = "P"
    ws.conditional_formatting.add(f"{status_col}{header_row+1}:{status_col}{last_row}",
        CellIsRule(operator="equal", formula=['"Published"'], fill=PatternFill("solid", fgColor="C6EFCE"), font=Font(color="006100", bold=True)))
    ws.conditional_formatting.add(f"{status_col}{header_row+1}:{status_col}{last_row}",
        CellIsRule(operator="equal", formula=['"Draft"'], fill=PatternFill("solid", fgColor="FFEB9C"), font=Font(color="9C6500", bold=True)))
    ws.conditional_formatting.add(f"{status_col}{header_row+1}:{status_col}{last_row}",
        CellIsRule(operator="equal", formula=['"Approved"'], fill=PatternFill("solid", fgColor="DDEBF7"), font=Font(color="2E75B6", bold=True)))
    ws.conditional_formatting.add(f"{status_col}{header_row+1}:{status_col}{last_row}",
        CellIsRule(operator="equal", formula=['"Review"'], fill=PatternFill("solid", fgColor="FCE4D6"), font=Font(color="C55A11", bold=True)))

    ws.sheet_view.showGridLines = False

print(f"Đã tạo {len(PILLAR_SHEETS)} sheet Content Pillar, tổng {len(cluster_registry)} content cluster.")

# ============================================================
# 5. SHEET CONTENT CALENDAR — DẠNG LƯỚI THEO TUẦN x THỨ (mỗi tuần = 1 Pillar)
# ============================================================

ws_cal = wb.create_sheet("Content Calendar", 0)
ws_cal.sheet_view.showGridLines = False

weekday_names_vn = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "CN"]
n_cols = 1 + 7  # cột A = nhãn Tuần/Pillar, cột B..H = Thứ 2..CN
last_col_idx = n_cols

# Title
ws_cal.merge_cells(start_row=1, start_column=1, end_row=1, end_column=last_col_idx)
t = ws_cal.cell(row=1, column=1,
    value=f"CONTENT CALENDAR THÁNG {MONTH}/{YEAR} — XANH GARDEN (Mỗi tuần tập trung 1 Content Pillar)")
t.font = Font(size=15, bold=True, color="FFFFFF")
t.fill = PatternFill("solid", fgColor="375623")
t.alignment = Alignment(horizontal="center", vertical="center")
ws_cal.row_dimensions[1].height = 30

# Header thứ trong tuần (row 2)
header_row_cal = 2
ws_cal.cell(row=header_row_cal, column=1, value="Tuần / Pillar")
for c in range(1, n_cols + 1):
    cell = ws_cal.cell(row=header_row_cal, column=c)
    if c > 1:
        wd_idx = c - 2
        is_weekend = wd_idx == 6
        cell.value = weekday_names_vn[wd_idx]
        cell.fill = PatternFill("solid", fgColor="F2F2F2" if not is_weekend else "FCE4D6")
        cell.font = Font(bold=True, color="000000" if not is_weekend else "C00000")
    else:
        cell.fill = PatternFill("solid", fgColor="D9D9D9")
        cell.font = BOLD_FONT
    cell.alignment = CENTER
    cell.border = BORDER_ALL
ws_cal.row_dimensions[header_row_cal].height = 22

ws_cal.freeze_panes = ws_cal.cell(row=header_row_cal + 1, column=2).coordinate

# Build map ngày -> list cluster entries
day_map = defaultdict(list)
for c in cluster_registry:
    day_map[c["ngay"].day].append(c)

# Vẽ từng tuần: 1 dòng "band" pillar label (merge dọc 2 dòng: ngày số + nội dung) + 1 dòng ngày-số + 1 dòng nội dung
row_cursor = header_row_cal + 1
week_row_ranges = []  # (start_row, end_row, pillar) để merge cột A
for wk_idx, day_list in enumerate(weeks, start=1):
    pillar = week_to_pillar[wk_idx]
    header_color = PILLAR_HEADER_COLORS[pillar]
    light_color = PILLAR_COLORS[pillar]

    row_daynum = row_cursor
    row_content = row_cursor + 1

    # Cột A: nhãn Tuần + Pillar (merge 2 dòng)
    ws_cal.merge_cells(start_row=row_daynum, start_column=1, end_row=row_content, end_column=1)
    label_cell = ws_cal.cell(row=row_daynum, column=1,
        value=f"TUẦN {wk_idx}\n{PILLAR_TITLES[pillar].replace('PILLAR ', 'P')}")
    label_cell.font = Font(bold=True, size=10, color="FFFFFF")
    label_cell.fill = PatternFill("solid", fgColor=header_color)
    label_cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    label_cell.border = BORDER_ALL

    # map thứ (0=Mon..6=Sun) -> day number trong tuần này
    day_by_wd = {}
    for day in day_list:
        wd = (first_weekday + (day - 1)) % 7
        day_by_wd[wd] = day

    for wd in range(7):
        col = 2 + wd
        day_cell = ws_cal.cell(row=row_daynum, column=col)
        content_cell = ws_cal.cell(row=row_content, column=col)
        day_cell.border = BORDER_ALL
        content_cell.border = BORDER_ALL

        if wd in day_by_wd:
            day_num = day_by_wd[wd]
            day_cell.value = day_num
            day_cell.font = Font(bold=True, size=9, color="595959")
            day_cell.alignment = CENTER
            day_cell.fill = PatternFill("solid", fgColor=light_color)

            entries = day_map.get(day_num, [])
            if entries:
                ref = entries[0]
                texts = [f"[{e['loai'][:2].upper()}] {e['ten']}" for e in entries]
                content_cell.value = "\n".join(texts)
                content_cell.fill = PatternFill("solid", fgColor=H3_FILL[ref["loai"]])
                content_cell.font = Font(size=8, bold=True, color=H3_COLORS[ref["loai"]])
                content_cell.alignment = WRAP_TOP
                content_cell.hyperlink = f"#'{ref['pillar_sheet']}'!A{ref['row']}"
                content_cell.comment = Comment(
                    f"Mã: {ref['ma_cluster']}\nKênh: {ref['kenh']}\nPhễu: {ref['funnel']}\nTrạng thái: {ref['status']}\n(Click để mở chi tiết trong sheet Pillar)",
                    "Content Calendar")
            else:
                content_cell.fill = PatternFill("solid", fgColor="FFFFFF")
        else:
            # Ngày không thuộc tháng (đầu/cuối tuần giao tháng)
            day_cell.fill = PatternFill("solid", fgColor="F2F2F2")
            content_cell.fill = PatternFill("solid", fgColor="F2F2F2")

    ws_cal.row_dimensions[row_daynum].height = 16
    ws_cal.row_dimensions[row_content].height = 60
    week_row_ranges.append((row_daynum, row_content, pillar))
    row_cursor = row_content + 1

# Column widths
ws_cal.column_dimensions["A"].width = 22
for c in range(2, n_cols + 1):
    ws_cal.column_dimensions[get_column_letter(c)].width = 20

# Legend
legend_row = row_cursor + 1
ws_cal.cell(row=legend_row, column=1, value="CHÚ GIẢI (LEGEND)").font = Font(bold=True, size=11)
legend_row += 1
legend_items = [("Hero (HE)", H3_FILL["Hero"], H3_COLORS["Hero"]),
                ("Hub (HU)", H3_FILL["Hub"], H3_COLORS["Hub"]),
                ("Hygiene (HY)", H3_FILL["Hygiene"], H3_COLORS["Hygiene"])]
for i, (label, fill_hex, font_hex) in enumerate(legend_items):
    cell = ws_cal.cell(row=legend_row + i, column=1, value=label)
    cell.fill = PatternFill("solid", fgColor=fill_hex)
    cell.font = Font(bold=True, color=font_hex)
    cell.border = BORDER_ALL
    ws_cal.cell(row=legend_row + i, column=2,
        value="Click vào ô nội dung để mở chi tiết Content Brief tương ứng trong sheet Pillar.").font = Font(italic=True, size=9, color="595959")

legend_row2 = legend_row + len(legend_items) + 1
ws_cal.cell(row=legend_row2, column=1,
    value="Màu dải mỗi Tuần tương ứng màu tiêu đề sheet Pillar được gán cho tuần đó (xem cột A).").font = Font(italic=True, size=9, color="595959")
legend_row3 = legend_row2 + 1
pillar_week_summary = "; ".join(f"Tuần {w}: {PILLAR_TITLES[p].split(': ')[1]}" for w, p in week_to_pillar.items())
ws_cal.cell(row=legend_row3, column=1, value="Phân bổ: " + pillar_week_summary).font = Font(italic=True, size=9, color="595959")
ws_cal.merge_cells(start_row=legend_row3, start_column=1, end_row=legend_row3, end_column=last_col_idx)

# ============================================================
# 6. SHEET DASHBOARD (đếm số lượng theo Pillar/Tuần & 3H)
# ============================================================

ws_dash = wb.create_sheet("Dashboard Can Bang", 1)
ws_dash.sheet_view.showGridLines = False

ws_dash.merge_cells("A1:F1")
t2 = ws_dash.cell(row=1, column=1, value="DASHBOARD KIỂM TRA CÂN BẰNG NỘI DUNG — THÁNG " + f"{MONTH}/{YEAR} (Theo Tuần)")
t2.font = Font(size=14, bold=True, color="FFFFFF")
t2.fill = PatternFill("solid", fgColor="203864")
t2.alignment = Alignment(horizontal="center", vertical="center")
ws_dash.row_dimensions[1].height = 26

ws_dash.cell(row=3, column=1, value="Tuần").font = HEADER_FONT
ws_dash.cell(row=3, column=2, value="Pillar được gán").font = HEADER_FONT
ws_dash.cell(row=3, column=3, value="Số Content Cluster").font = HEADER_FONT
ws_dash.cell(row=3, column=4, value="Đạt tối thiểu 3-5 bài?").font = HEADER_FONT
for c in (1, 2, 3, 4):
    ws_dash.cell(row=3, column=c).fill = PatternFill("solid", fgColor="4472C4")
    ws_dash.cell(row=3, column=c).font = HEADER_FONT
    ws_dash.cell(row=3, column=c).alignment = CENTER
    ws_dash.cell(row=3, column=c).border = BORDER_ALL

for i, wk_num in enumerate(sorted(week_to_pillar.keys())):
    r = 4 + i
    pillar = week_to_pillar[wk_num]
    ws_dash.cell(row=r, column=1, value=f"Tuần {wk_num}").border = BORDER_ALL
    ws_dash.cell(row=r, column=1).alignment = CENTER
    ws_dash.cell(row=r, column=2, value=PILLAR_TITLES[pillar]).border = BORDER_ALL
    ws_dash.cell(row=r, column=2).fill = PatternFill("solid", fgColor=PILLAR_COLORS[pillar])
    ws_dash.cell(row=r, column=3, value=f"=COUNTA('{pillar}'!B4:B100)").border = BORDER_ALL
    ws_dash.cell(row=r, column=3).alignment = CENTER
    ws_dash.cell(row=r, column=4, value=f'=IF(C{r}>=3,"✓ Đạt","✗ Cần bổ sung")').border = BORDER_ALL
    ws_dash.cell(row=r, column=4).alignment = CENTER

last_wk_row = 3 + num_weeks
ws_dash.conditional_formatting.add(f"D4:D{last_wk_row}",
    FormulaRule(formula=['D4="✓ Đạt"'], fill=PatternFill("solid", fgColor="C6EFCE")))

dash2_row = last_wk_row + 2
ws_dash.cell(row=dash2_row, column=1, value="Loại 3H").font = HEADER_FONT
ws_dash.cell(row=dash2_row, column=2, value="Số lượng").font = HEADER_FONT
ws_dash.cell(row=dash2_row, column=3, value="Tỷ lệ %").font = HEADER_FONT
ws_dash.cell(row=dash2_row, column=4, value="Khung đề xuất (SME)").font = HEADER_FONT
for c in (1, 2, 3, 4):
    ws_dash.cell(row=dash2_row, column=c).fill = PatternFill("solid", fgColor="4472C4")
    ws_dash.cell(row=dash2_row, column=c).font = HEADER_FONT
    ws_dash.cell(row=dash2_row, column=c).alignment = CENTER
    ws_dash.cell(row=dash2_row, column=c).border = BORDER_ALL

total_items = len(cluster_registry)
h3_counts = {k: sum(1 for c in cluster_registry if c["loai"] == k) for k in H3_LIST}
h3_baseline = {"Hero": "5-10%", "Hub": "40-50%", "Hygiene": "40-55%"}
for i, h3 in enumerate(H3_LIST):
    r = dash2_row + 1 + i
    ws_dash.cell(row=r, column=1, value=h3).border = BORDER_ALL
    ws_dash.cell(row=r, column=1).fill = PatternFill("solid", fgColor=H3_FILL[h3])
    ws_dash.cell(row=r, column=1).font = Font(bold=True, color=H3_COLORS[h3])
    ws_dash.cell(row=r, column=2, value=h3_counts[h3]).border = BORDER_ALL
    ws_dash.cell(row=r, column=2).alignment = CENTER
    ws_dash.cell(row=r, column=3, value=f"=B{r}/{total_items}").border = BORDER_ALL
    ws_dash.cell(row=r, column=3).number_format = "0.0%"
    ws_dash.cell(row=r, column=3).alignment = CENTER
    ws_dash.cell(row=r, column=4, value=h3_baseline[h3]).border = BORDER_ALL
    ws_dash.cell(row=r, column=4).alignment = CENTER

ws_dash.cell(row=dash2_row + len(H3_LIST) + 1, column=1,
    value=f"Tổng số Content Cluster trong tháng: {total_items}  |  Số tuần lịch: {num_weeks}").font = Font(bold=True, italic=True)

autofit(ws_dash, [16, 40, 16, 20])

# ============================================================
# 7. SHEET HƯỚNG DẪN SỬ DỤNG
# ============================================================
ws_guide = wb.create_sheet("Huong Dan", 2)
ws_guide.sheet_view.showGridLines = False
ws_guide.column_dimensions["A"].width = 110

guide_lines = [
    ("HƯỚNG DẪN SỬ DỤNG — CONTENT CALENDAR THEO TUẦN (MỖI TUẦN 1 PILLAR) — XANH GARDEN", True, 14, "203864"),
    ("", False, 10, None),
    ("ĐIỂM KHÁC BIỆT SO VỚI BẢN GỐC:", True, 11, "C00000"),
    ("   Bản này chia lịch theo TUẦN: mỗi tuần trong tháng chỉ tập trung đăng nội dung của 1 Content Pillar duy nhất,", False, 10, None),
    ("   luân phiên lần lượt 4 Pillar qua các tuần (Tuần 1->Pillar 1, Tuần 2->Pillar 2, Tuần 3->Pillar 3, Tuần 4->Pillar 4, ...).", False, 10, None),
    ("   Khác với bản gốc (mỗi Pillar trải đều suốt cả tháng, xen kẽ ngày), bản này giúp mỗi tuần có 1 'chủ đề tuần' rõ ràng,", False, 10, None),
    ("   dễ truyền thông nội bộ và dễ lên kịch bản sản xuất theo lô (batch content) cho từng Pillar.", False, 10, None),
    ("", False, 10, None),
    ("1. Sheet 'Content Calendar': Lưới theo TUẦN (hàng) x THỨ TRONG TUẦN (cột: Thứ 2 -> CN).", True, 11, None),
    ("   - Cột A merge theo từng tuần, hiển thị 'TUẦN n' + tên Pillar được gán cho tuần đó, tô màu theo Pillar.", False, 10, None),
    ("   - Mỗi tuần có 2 dòng: dòng số ngày (nhỏ) và dòng nội dung (to, wrap text) tô màu theo loại 3H.", False, 10, None),
    ("   - Click vào ô nội dung để nhảy tới dòng chi tiết Content Brief trong sheet Pillar tương ứng.", False, 10, None),
    ("   - Rê chuột vào ô để xem chú thích nhanh: Mã cluster, Kênh, Phễu, Trạng thái.", False, 10, None),
    ("", False, 10, None),
    ("2. 4 sheet 'Pillar 1-4': Mỗi dòng là 1 Content Cluster theo mẫu Content Brief chuẩn (Module 2 - mục 2.6),", True, 11, None),
    ("   có thêm cột 'Tuần đăng' để biết cluster thuộc tuần nào. Dropdown: Loại 3H, Kênh, Trạng thái, Mục tiêu phễu.", False, 10, None),
    ("   Trạng thái tự đổi màu: Draft (vàng), Review (cam), Approved (xanh dương nhạt), Published (xanh lá).", False, 10, None),
    ("", False, 10, None),
    ("3. Sheet 'Dashboard Can Bang': Đếm số Content Cluster theo từng Tuần/Pillar (công thức COUNTA tự cập nhật)", True, 11, None),
    ("   và tỷ lệ % Hero/Hub/Hygiene toàn tháng, đối chiếu khung tỷ lệ đề xuất chuẩn (Hero 5-10%, Hub 40-50%, Hygiene 40-55%).", False, 10, None),
    ("", False, 10, None),
    ("4. Lưu ý cân bằng khi dùng mô hình 'mỗi tuần 1 Pillar': Nguyên tắc mục 2.5 tài liệu Module 2 khuyến nghị KHÔNG", True, 11, "C00000"),
    ("   dồn hết vào 1 chủ đề trong 1 khoảng thời gian dài. Cách chia theo tuần này đánh đổi giữa tính rõ ràng theo chủ đề tuần", False, 10, None),
    ("   và rủi ro 'lệch cân bằng' nếu khách theo dõi trong đúng 1 tuần chỉ thấy 1 Pillar. Nên bổ sung 1-2 bài Hygiene", False, 10, None),
    ("   'xen ngang' từ Pillar khác trong tuần nếu cần duy trì cảm giác đa dạng nội dung khi khách hàng xem lại nhiều lần/tuần.", False, 10, None),
    ("", False, 10, None),
    ("5. Nguồn tham chiếu chiến lược: Module 2 - Chiến lược Nội dung (calendar-3H.md) - Content Pillar, Topic Cluster,", True, 11, None),
    ("   Mô hình 3H (Hero-Hub-Hygiene), Content Calendar, Content Brief. Case mẫu: thương hiệu 'Xanh Garden' (mục 9 tài liệu).", False, 10, None),
]
for i, (text, bold, size, color) in enumerate(guide_lines, start=1):
    cell = ws_guide.cell(row=i, column=1, value=text)
    cell.font = Font(bold=bold, size=size, color=color if color else "000000")
    cell.alignment = Alignment(wrap_text=True, vertical="top")

# Thứ tự sheet
desired_order = ["Huong Dan", "Content Calendar", "Dashboard Can Bang"] + PILLAR_SHEETS
wb._sheets = [wb[name] for name in desired_order]
wb.active = 0
wb.save(OUT_PATH)
print(f"Đã lưu file: {OUT_PATH}")
