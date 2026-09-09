#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tạo file Excel "Khung Prompt AI Tổng Quát - Đa Ngành Nghề"
Tổng quát hóa từ file Thu_Vien_Prompt_AI_BatDongSan.xlsx và Phần C.2.2 + Phần F/G
của tài liệu 10-TAI-LIEU-GOP-MODULE-4-5-6-SEO-DO-LUONG-AI.md, bỏ toàn bộ yếu tố
riêng ngành bất động sản, thay bằng placeholder [NGÀNH NGHỀ]/[SẢN PHẨM-DỊCH VỤ]/
[PERSONA KHÁCH HÀNG] để bất kỳ ngành nghề nào cũng áp dụng được ngay.

Gồm 5 sheet:
  0. Huong Dan Su Dung     - Cách dùng file, chú giải màu, quy tắc vàng, các bước tùy biến
                             cho ngành nghề của bạn
  1. So Sanh Framework     - Bảng so sánh 5 framework prompt phổ biến (R-T-F-C, RACE,
                             CO-STAR, TAG, APE) + gợi ý chọn framework theo tình huống
  2. Thu Vien Prompt       - Thư viện prompt mẫu TỔNG QUÁT theo nhóm công việc (áp dụng
                             mọi ngành), có AutoFilter + Dropdown lọc theo Nhóm công việc /
                             Giai đoạn hành trình khách hàng / Công cụ AI
  3. Prompt Builder RTFC   - Mẫu điền sẵn: nhập Role/Task/Format/Context vào ô vàng,
                             cột bên phải TỰ ĐỘNG ghép thành 1 prompt hoàn chỉnh
  4. Ho So Nganh Cua Ban   - Nơi điền 1 lần các thông tin đặc thù ngành nghề của bạn
                             (ngành, sản phẩm/dịch vụ, persona, tông giọng, điều cấm kỵ)
                             để tra cứu và dán nhanh vào các prompt ở Sheet 2 & 3
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation

OUT_PATH = "/Users/phamvannam/Documents/GitHub/hello-affiliate/content-marketing/code/Khung_Prompt_AI_Da_Nganh_Tong_Quat.xlsx"

HEADER_BLUE = "1F4E78"
LIGHT_BLUE = "D9E1F2"
GREEN = "375623"
LIGHT_GREEN = "E2EFDA"
ORANGE = "833C00"
LIGHT_ORANGE = "FCE4D6"
WHITE = "FFFFFF"
YELLOW = "FFF2CC"
GREY_TEXT = "7F7F7F"


def fill(color):
    return PatternFill("solid", fgColor=color)


def font(bold=False, size=10, color="000000", italic=False):
    return Font(bold=bold, size=size, color=color, italic=italic)


def border():
    side = Side(style="thin", color="BFBFBF")
    return Border(left=side, right=side, top=side, bottom=side)


def center():
    return Alignment(horizontal="center", vertical="center", wrap_text=True)


def left():
    return Alignment(horizontal="left", vertical="center", wrap_text=True)


def title_row(ws, row, text, span, bg=HEADER_BLUE, fg=WHITE, size=13):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=span)
    c = ws.cell(row=row, column=1, value=text)
    c.font = font(bold=True, size=size, color=fg)
    c.fill = fill(bg)
    c.alignment = center()
    ws.row_dimensions[row].height = 24


def header_row(ws, row, headers, bg=HEADER_BLUE, fg=WHITE):
    for i, h in enumerate(headers, start=1):
        c = ws.cell(row=row, column=i, value=h)
        c.font = font(bold=True, color=fg)
        c.fill = fill(bg)
        c.alignment = center()
        c.border = border()


def set_widths(ws, widths):
    for col, w in widths.items():
        ws.column_dimensions[col].width = w


# ============================================================
# DU LIEU: BANG SO SANH FRAMEWORK (tong quat, khong rieng nganh nao)
# ============================================================
FRAMEWORKS = [
    ("R-T-F-C", "Role - Task - Format - Context (Vai trò - Nhiệm vụ - Định dạng - Bối cảnh)",
     "Tác vụ sáng tạo nội dung nói chung (bài viết, caption, kịch bản, email) - dùng được cho 80% công việc hàng ngày",
     "Trung bình"),
    ("RACE", "Role - Action - Context - Expectation (Vai trò - Hành động - Bối cảnh - Kỳ vọng đầu ra)",
     "Khi cần AI hiểu rõ 'tiêu chuẩn thành công' cụ thể của kết quả đầu ra",
     "Trung bình"),
    ("CO-STAR", "Context - Objective - Style - Tone - Audience - Response format",
     "Khi cần kiểm soát chặt giọng văn/phong cách cho nội dung thương hiệu, nhiều người viết cùng dùng chung 1 khung",
     "Cao"),
    ("TAG", "Task - Action - Goal (Nhiệm vụ - Hành động cụ thể - Mục tiêu cuối)",
     "Tác vụ ngắn gọn, cần nhanh (ví dụ: sửa 1 câu, rút gọn 1 đoạn văn)",
     "Thấp"),
    ("APE", "Action - Purpose - Expectation (Hành động - Mục đích - Kỳ vọng)",
     "Khi giao việc nhanh cho AI như giao việc cho 1 trợ lý cá nhân",
     "Thấp"),
]

# ============================================================
# DU LIEU PROMPT TONG QUAT (ap dung moi nganh nghe)
# Cau truc: (STT, Nhom cong viec, Giai doan hanh trinh KH, Ten Prompt,
#            Noi dung prompt (dung placeholder tong quat), Cong cu AI goi y,
#            Framework ap dung, Ghi chu/rui ro can kiem soat)
# ============================================================
PROMPTS = [
    (1, "Phan tich du lieu", "Tat ca giai doan",
     "Phân tích báo cáo số liệu định kỳ (web/mạng xã hội/bán hàng)",
     'Bạn là chuyên gia phân tích dữ liệu marketing cho ngành [NGÀNH NGHỀ CỦA BẠN].\n\n'
     'NHIỆM VỤ: Phân tích file dữ liệu tôi vừa tải lên (số liệu truy cập/tương tác/bán hàng '
     'kỳ này của [SẢN PHẨM/DỊCH VỤ]).\n\n'
     'Hãy trả lời theo đúng cấu trúc:\n'
     '1. Kênh/nguồn nào đang dẫn đầu, chiếm bao nhiêu % tổng số?\n'
     '2. Chỉ số nào có dấu hiệu bất thường (tăng/giảm quá 20% so với kỳ trước)?\n'
     '3. Đưa ra 3 giả thuyết (hypothesis) giải thích nguyên nhân cho các điểm bất thường đó.\n'
     '4. Đề xuất 2 hành động cụ thể nên làm trong kỳ tới.\n\n'
     'Trình bày dạng bảng cho câu 1-2, dạng danh sách đánh số cho câu 3-4.\n'
     'Nếu dữ liệu không đủ để trả lời chính xác câu nào, hãy nói rõ "không đủ dữ liệu" '
     'thay vì suy đoán.',
     "ChatGPT/Claude/Gemini (Data Analysis)", "R-T-F-C",
     "Đối chiếu lại insight AI đưa ra với hiểu biết thực tế của bạn, không copy 100%"),

    (2, "Phan tich du lieu", "Tat ca giai doan",
     "Kiểm tra tính hợp lý số liệu trước khi đưa vào báo cáo",
     'Đây là bảng số liệu tôi vừa tổng hợp cho kỳ báo cáo này: [dán bảng số liệu]\n\n'
     'Hãy kiểm tra giúp tôi:\n'
     '1. Có con số nào bất thường/phi logic không (ví dụ: tỷ lệ > 100%, số âm không hợp lý)?\n'
     '2. Có phép tính cộng/chia nào trong bảng có thể bị sai không? Chỉ ra cụ thể ô nào.\n'
     '3. Không tự sửa số liệu - chỉ liệt kê nghi vấn để tôi tự kiểm tra lại nguồn.',
     "ChatGPT/Claude", "TAG",
     "AI chỉ được liệt kê nghi vấn, KHÔNG được tự ý sửa số liệu"),

    (3, "Phan tich du lieu", "Chuyen doi/Ban hang",
     "Tính ROI/hiệu quả chiến dịch nhanh",
     'Tôi có số liệu sau cho 1 chiến dịch marketing trong [KHOẢNG THỜI GIAN]:\n'
     '- Tổng chi phí: [X]\n'
     '- Tổng lead/khách hàng tiềm năng thu được: [Y]\n'
     '- Tỷ lệ chuyển đổi thành khách mua/ký hợp đồng: [Z%]\n'
     '- Giá trị trung bình 1 đơn hàng/hợp đồng: [H]\n\n'
     'Hãy tính giúp tôi: số khách chuyển đổi, tổng doanh thu, chi phí trên mỗi lead (CPL), '
     'chi phí trên mỗi khách hàng (CAC), và ROI (%).\n'
     'Trình bày từng bước tính (Chain of Thought) để tôi kiểm tra lại logic, không chỉ đưa '
     'kết quả cuối cùng.',
     "ChatGPT/Claude", "R-T-F-C",
     "Luôn tự tay đối chiếu lại công thức tính trước khi báo cáo cấp trên"),

    (4, "Noi dung Text", "Nhan biet (TOFU)",
     "Viết outline bài blog/bài viết chuẩn SEO",
     'Bạn là chuyên gia content marketing/SEO ngành [NGÀNH NGHỀ CỦA BẠN].\n\n'
     'NHIỆM VỤ: Xây dựng outline (dàn ý) cho 1 bài viết nhắm từ khóa chính '
     '"[TỪ KHÓA CHÍNH]".\n\n'
     'YÊU CẦU:\n'
     '- Xác định Search Intent (ý định tìm kiếm) của từ khóa này trước khi viết outline.\n'
     '- Outline gồm: 1 tiêu đề H1 hấp dẫn, tối thiểu 5 heading H2, mỗi H2 có 2-3 gạch đầu dòng ý chính.\n'
     '- Đoạn mở đầu phải trả lời trực tiếp câu hỏi ngay trong 2-3 câu đầu (tối ưu cho AI Search/GEO).\n'
     '- Gợi ý 3 vị trí nên chèn số liệu/dẫn chứng để tăng độ tin cậy.\n'
     '- Đề xuất 3 từ khóa phụ (long-tail) nên lồng ghép tự nhiên trong bài.',
     "ChatGPT/Gemini", "R-T-F-C",
     "Người biên tập phải kiểm tra lại số liệu/tính chính xác trước khi đăng (rủi ro AI Hallucination)"),

    (5, "Noi dung Text", "Can nhac/Chuyen doi",
     "Viết nhiều phiên bản caption/bài đăng để A/B Test",
     'Viết 5 phiên bản caption cho cùng 1 thông điệp: "[MÔ TẢ THÔNG ĐIỆP/ƯU ĐÃI CẦN TRUYỀN TẢI]".\n\n'
     'Mỗi phiên bản áp dụng 1 công thức khác nhau để tôi so sánh A/B Test:\n'
     '1. Công thức PAS (Problem-Agitate-Solution)\n'
     '2. Công thức AIDA\n'
     '3. Công thức kể chuyện (Storytelling) - góc nhìn khách hàng đã trải nghiệm\n'
     '4. Công thức đặt câu hỏi mở đầu\n'
     '5. Công thức con số/thống kê gây chú ý\n\n'
     'Mỗi phiên bản tối đa 100 từ, đối tượng đọc là [PERSONA KHÁCH HÀNG], có 1 CTA rõ ràng ở cuối.\n'
     'Đánh số rõ phiên bản nào theo công thức nào để tôi dễ so sánh khi lên lịch A/B Test.',
     "ChatGPT", "R-T-F-C",
     "Ghi lại kết quả A/B Test thực tế để tối ưu dần, không chỉ dùng 1 lần rồi bỏ"),

    (6, "Noi dung Text", "Can nhac/Cham soc",
     "Viết chuỗi email/tin nhắn chăm sóc khách hàng tiềm năng",
     'Bạn là chuyên gia Email/CRM Marketing ngành [NGÀNH NGHỀ CỦA BẠN].\n\n'
     'Viết chuỗi 3 email/tin nhắn chăm sóc cho khách hàng đã để lại thông tin nhưng chưa '
     'hành động tiếp, gửi cách nhau 3 ngày/lần:\n\n'
     'Lần 1 (gửi ngay sau khi để lại thông tin): Cảm ơn + cung cấp thêm 1 tài liệu/thông tin hữu ích.\n'
     'Lần 2 (3 ngày sau, nếu chưa phản hồi): Nhấn mạnh yếu tố khan hiếm/ưu đãi có thời hạn, '
     'kèm 1 câu hỏi mời phản hồi.\n'
     'Lần 3 (6 ngày sau, nếu vẫn chưa phản hồi): Đổi góc tiếp cận - mời tham gia 1 sự kiện/tư '
     'vấn miễn phí thay vì mời mua ngay (giảm áp lực).\n\n'
     'Mỗi email/tin nhắn: tiêu đề tối đa 8 từ, nội dung tối đa 150 từ, có 1 CTA rõ ràng.',
     "ChatGPT", "R-T-F-C",
     "Người quản lý phải duyệt nội dung trước khi gửi hàng loạt, tránh cam kết sai (case Air Canada)"),

    (7, "Noi dung Video", "Nhan biet (TOFU)",
     "Viết kịch bản video ngắn (TikTok/Reels/Shorts) theo timing",
     'Bạn là chuyên gia sản xuất video ngắn ngành [NGÀNH NGHỀ CỦA BẠN].\n\n'
     'NHIỆM VỤ: Viết kịch bản chi tiết cho video ngắn 30 giây, chủ đề: "[CHỦ ĐỀ VIDEO]"\n\n'
     'YÊU CẦU ĐỊNH DẠNG: Trình bày dạng bảng 5 cột: Thời gian | Hình ảnh/Hành động quay | '
     'Lời thoại/Voice over | Chữ trên màn hình | Gợi ý nhạc nền.\n\n'
     'RÀNG BUỘC:\n'
     '- 3 giây đầu phải có Hook mạnh (cảnh báo/con số/câu hỏi bất ngờ).\n'
     '- Giây cuối cùng phải có CTA rõ ràng, chỉ 1 hành động duy nhất.\n'
     '- Lời thoại viết theo văn nói tự nhiên, không văn viết trang trọng.\n'
     '- Độ dài lời thoại mỗi đoạn phải khớp với thời lượng (khoảng 2,5 từ/giây khi đọc bình thường).',
     "ChatGPT + CapCut AI", "R-T-F-C",
     "Kiểm tra lại thông tin/số liệu nêu trong video trước khi đăng công khai"),

    (8, "Noi dung Video", "Can nhac",
     "Viết kịch bản cho AI Avatar (video người ảo)",
     'Viết kịch bản 45 giây cho video AI Avatar (nhân vật ảo) đóng vai chuyên gia tư vấn '
     'ngành [NGÀNH NGHỀ CỦA BẠN], giải thích chủ đề: "[CHỦ ĐỀ CẦN GIẢI THÍCH]"\n\n'
     'YÊU CẦU:\n'
     '- Văn phong: nói chuyện trực tiếp với người xem (dùng "bạn"), tốc độ vừa phải vì '
     'Avatar AI đọc chậm hơn người thật khoảng 10-15%.\n'
     '- Chia thành các câu ngắn (dưới 20 từ/câu) để AI Avatar phát âm tự nhiên, tránh câu '
     'quá dài gây đọc vấp/nghe máy móc.\n'
     '- Kết thúc bằng lời mời để lại thông tin liên hệ.\n'
     '- Không dùng từ viết tắt/tiếng lóng vì công cụ AI Avatar có thể đọc sai.',
     "HeyGen/Synthesia", "R-T-F-C",
     "Phù hợp khi không có thời gian/nhân sự quay mặt thật"),

    (9, "Noi dung Video", "Tat ca giai doan",
     "Tạo prompt hình ảnh AI minh họa (tiếng Anh)",
     'Hãy viết 3 prompt bằng tiếng Anh (vì đa số công cụ AI tạo ảnh hiểu tiếng Anh tốt hơn) '
     'để tạo hình ảnh minh họa cho bài viết chủ đề "[CHỦ ĐỀ]" thuộc ngành [NGÀNH NGHỀ CỦA BẠN], '
     'phong cách: [MÔ TẢ PHONG CÁCH MONG MUỐN, ví dụ: hiện đại, tông màu ấm, ánh sáng tự nhiên], '
     'không có người thật trong ảnh (tránh vi phạm bản quyền hình ảnh người), kích thước phù '
     'hợp làm ảnh bìa 1200x630px.',
     "Midjourney/Canva AI/Adobe Firefly", "TAG",
     "Tránh dùng ảnh có người thật để không vi phạm bản quyền hình ảnh"),

    (10, "Noi dung Voice", "Tat ca giai doan",
     "Tối ưu kịch bản cho Text-to-Speech (TTS)",
     'Viết lại đoạn văn sau thành kịch bản voice-over phù hợp để đưa vào công cụ '
     'Text-to-Speech (ElevenLabs/Google TTS):\n\n'
     '[Dán đoạn văn gốc]\n\n'
     'YÊU CẦU CHỈNH SỬA:\n'
     '- Viết số ra chữ đầy đủ thay vì số (ví dụ: "hai triệu năm trăm nghìn" thay vì "2.5 triệu").\n'
     '- Viết tắt/ký hiệu chuyển thành chữ đầy đủ.\n'
     '- Thêm dấu phẩy/dấu chấm ở những chỗ cần AI ngắt hơi tự nhiên khi đọc.\n'
     '- Câu không quá 25 từ để tránh AI đọc dồn dập, mất tự nhiên.',
     "ElevenLabs/Google TTS/CapCut Voice", "TAG",
     "Luôn nghe lại bản audio trước khi dùng chính thức"),

    (11, "Noi dung Voice", "Tat ca giai doan",
     "Chọn tông giọng phù hợp nội dung",
     'Tôi có 1 đoạn kịch bản voice-over cho video "[MÔ TẢ VIDEO]". Đối tượng người nghe '
     'là "[PERSONA KHÁCH HÀNG]".\n'
     'Hãy gợi ý: (1) nên chọn giọng nam hay nữ, (2) tốc độ đọc nên nhanh/chậm/vừa, '
     '(3) cảm xúc giọng đọc nên là gì (ấm áp/chuyên nghiệp/hào hứng) - giải thích ngắn '
     'gọn lý do cho mỗi lựa chọn.',
     "ElevenLabs", "APE",
     "Kết hợp với Persona khách hàng đã xây dựng trước đó"),

    (12, "Tuong tac/Cham soc", "Trung thanh",
     "Gợi ý trả lời bình luận/tin nhắn khách hàng",
     'Khách hàng bình luận: "[DÁN NGUYÊN VĂN BÌNH LUẬN/TIN NHẮN CỦA KHÁCH]"\n\n'
     'Hãy gợi ý cho tôi 2 cách trả lời:\n'
     '1. Trả lời ngắn gọn, thân thiện, mời khách nhắn tin riêng (inbox) để tư vấn kỹ hơn.\n'
     '2. Trả lời có thêm 1 thông tin hữu ích liên quan đến câu hỏi của khách.\n'
     'Không tự ý cam kết giá cả/ưu đãi/kết quả cụ thể nếu tôi chưa cung cấp thông tin đó trong prompt.',
     "ChatGPT (mobile)", "APE",
     "Chỉ là GỢI Ý - nhân viên vẫn phải tự đọc lại trước khi gửi"),

    (13, "Toi uu da kenh", "Tat ca giai doan",
     "Rút gọn/viết lại nội dung theo nhiều độ dài cho đa kênh",
     'Đây là bài viết gốc: [dán bài viết]\n\n'
     'Hãy viết lại thành 3 phiên bản độ dài khác nhau để đăng đa kênh:\n'
     '1. Bản 300 từ cho bài viết dài (blog/Facebook).\n'
     '2. Bản 60 từ cho caption ngắn (Instagram/TikTok).\n'
     '3. Bản 3 gạch đầu dòng cho tin nhắn/thông báo ngắn (Zalo OA/SMS/App).\n'
     'Giữ nguyên thông điệp cốt lõi và CTA ở cả 3 bản.',
     "ChatGPT/Claude", "TAG",
     "Áp dụng kỹ thuật Content Repurposing (tái sử dụng nội dung)"),

    (14, "Kiem tra tuan thu", "Chuyen doi",
     "Rà soát sơ bộ nội dung quảng cáo có vi phạm/cam kết quá mức",
     'Đọc giúp tôi đoạn quảng cáo sau: [dán nội dung]\n\n'
     'Hãy chỉ ra các từ ngữ có nguy cơ bị xem là cam kết/quảng cáo quá mức (ví dụ: cam '
     'kết kết quả tuyệt đối, dùng "duy nhất/số 1/tốt nhất" mà không có căn cứ, so sánh '
     'trực tiếp đối thủ theo cách có thể vi phạm) theo quy định quảng cáo của ngành '
     '[NGÀNH NGHỀ CỦA BẠN].\n'
     'Đây chỉ là bước rà soát sơ bộ bằng AI - tôi vẫn sẽ cho bộ phận pháp lý/quản lý '
     'kiểm tra lại trước khi đăng chính thức.',
     "ChatGPT/Claude", "TAG",
     "KHÔNG thay thế tư vấn pháp lý - chỉ là bước lọc sơ bộ"),

    (15, "Bao cao", "Tat ca giai doan",
     "Tóm tắt báo cáo cuối ngày/cuối tuần gửi cấp trên",
     'Tóm tắt các số liệu và công việc sau thành 5 dòng báo cáo cuối ngày/cuối tuần gửi '
     'cấp trên: [dán số liệu/công việc trong kỳ]',
     "ChatGPT", "TAG",
     "Kiểm tra lại số liệu trước khi gửi, AI chỉ hỗ trợ diễn đạt"),

    (16, "Len ke hoach", "Tat ca giai doan",
     "Brainstorm ý tưởng nội dung theo từng giai đoạn hành trình khách hàng",
     'Dựa trên hiệu quả các nội dung đã đăng kỳ này [dán tóm tắt], hãy đề xuất 5 ý tưởng '
     'nội dung cho kỳ tới, sắp xếp theo giai đoạn hành trình khách hàng: Nhận biết - '
     'Cân nhắc - Chuyển đổi - Trung thành.',
     "ChatGPT (Chain of Thought)", "R-T-F-C",
     "Đối chiếu với chiến lược nội dung/Content Pillar đã xây dựng trước khi chốt"),

    (17, "Noi dung Text (nang cao)", "Chuyen doi",
     "Kịch bản video theo mô hình StoryBrand SB7",
     'Viết kịch bản video 60 giây theo mô hình StoryBrand SB7, trong đó khách hàng '
     '[PERSONA KHÁCH HÀNG] là nhân vật chính đang gặp vấn đề [NỖI ĐAU CHÍNH], và thương '
     'hiệu [TÊN THƯƠNG HIỆU CỦA BẠN] đóng vai người dẫn đường đưa ra kế hoạch 3 bước để '
     'giải quyết.',
     "ChatGPT/Claude", "CO-STAR",
     "Điền đầy đủ Persona trước khi dùng, tránh nội dung chung chung"),

    (18, "Noi dung Text (nang cao)", "Can nhac",
     "Bài viết đầy đủ theo R-T-F-C + Persona + Content Pillar",
     'Vai trò: Bạn là chuyên gia content marketing ngành [NGÀNH NGHỀ CỦA BẠN], giọng văn '
     '[TÔNG GIỌNG THƯƠNG HIỆU, ví dụ: thân thiện, đáng tin cậy].\n'
     'Nhiệm vụ: Viết 1 bài viết chuẩn SEO (800-1000 từ) cho giai đoạn khách hàng đang '
     'cân nhắc (đã biết sản phẩm/dịch vụ nhưng chưa quyết định).\n'
     'Định dạng: Có H2/H3, có 1 đoạn FAQ cuối bài, giọng văn theo công thức PAS '
     '(Problem-Agitate-Solve).\n'
     'Bối cảnh:\n'
     '- Persona: [MÔ TẢ PERSONA - độ tuổi, nghề nghiệp, thu nhập, nỗi đau lớn nhất]\n'
     '- Chủ đề nội dung cốt lõi liên quan: [TÊN CONTENT PILLAR/CHỦ ĐỀ LỚN]\n'
     '- Từ khóa chính cần lồng ghép tự nhiên: [TỪ KHÓA 1], [TỪ KHÓA 2]\n'
     'Sau khi viết xong, hãy tự chấm điểm bài viết theo 4C (Clear - Concise - '
     'Compelling - Credible) và chỉ ra điểm cần sửa nếu có.',
     "ChatGPT/Claude", "CO-STAR",
     "Ví dụ mẫu cho thấy vì sao phải mang theo dữ liệu Persona/Content Pillar vào prompt"),

    (19, "Phan tich du lieu", "Tat ca giai doan",
     "Phân tích đối thủ cạnh tranh (Competitor Audit) sơ bộ",
     'Bạn là chuyên gia phân tích chiến lược nội dung ngành [NGÀNH NGHỀ CỦA BẠN].\n\n'
     'Dưới đây là danh sách 3-5 nội dung/bài đăng của đối thủ [TÊN ĐỐI THỦ] mà tôi đã '
     'tổng hợp: [dán tiêu đề/link/mô tả ngắn từng bài]\n\n'
     'Hãy phân tích: (1) chủ đề/góc tiếp cận chung của đối thủ là gì, (2) điểm mạnh trong '
     'cách trình bày/CTA của họ, (3) khoảng trống nội dung (content gap) mà tôi có thể '
     'khai thác mà đối thủ chưa làm tốt.\n'
     'Không suy đoán số liệu thật (lượt xem/tương tác) nếu tôi không cung cấp - chỉ phân '
     'tích dựa trên nội dung/cấu trúc bài viết.',
     "ChatGPT/Claude", "R-T-F-C",
     "Chỉ dùng để tham khảo hướng đi, không sao chép nguyên văn ý tưởng đối thủ"),

    (20, "Len ke hoach", "Tat ca giai doan",
     "Xây khung lịch nội dung (content calendar) 1 tuần/1 tháng",
     'Bạn là chuyên gia lập kế hoạch content marketing ngành [NGÀNH NGHỀ CỦA BẠN].\n\n'
     'NHIỆM VỤ: Đề xuất khung lịch nội dung cho [1 TUẦN/1 THÁNG], mục tiêu chính là '
     '[MỤC TIÊU, ví dụ: tăng nhận diện thương hiệu/tăng lead/tăng doanh số].\n\n'
     'YÊU CẦU: Với mỗi ngày đăng, liệt kê: (1) chủ đề nội dung, (2) định dạng '
     '(bài viết/video/hình ảnh/livestream), (3) giai đoạn hành trình khách hàng nhắm tới '
     '(Nhận biết/Cân nhắc/Chuyển đổi/Trung thành), (4) 1 gợi ý CTA phù hợp.\n'
     'Trình bày dạng bảng, đảm bảo tỷ lệ nội dung hợp lý giữa các giai đoạn hành trình '
     '(không dồn quá nhiều vào 1 giai đoạn).',
     "ChatGPT/Claude", "R-T-F-C",
     "Đối chiếu lại với nguồn lực sản xuất thực tế (nhân sự/ngân sách) trước khi chốt lịch"),
]

NHOM_LIST = sorted(set(p[1] for p in PROMPTS))
GIAIDOAN_LIST = sorted(set(p[2] for p in PROMPTS))
CONGCU_LIST = sorted(set(p[5] for p in PROMPTS))


# ============================================================
# SHEET 0: HUONG DAN SU DUNG
# ============================================================
def build_huongdan_sheet(wb):
    ws = wb.active
    ws.title = "0. Huong Dan"
    set_widths(ws, {"A": 4, "B": 46, "C": 74})

    title_row(ws, 1, "KHUNG PROMPT AI TỔNG QUÁT - DÙNG ĐƯỢC CHO MỌI NGÀNH NGHỀ", 3, size=14)
    ws.cell(row=2, column=1, value=(
        "File này tổng quát hóa từ tài liệu 10-TAI-LIEU-GOP-MODULE-4-5-6-SEO-DO-LUONG-AI.md "
        "(Phần C.2.2, Phần F, Phần G) và file Thư viện Prompt AI Bất động sản, loại bỏ các "
        "yếu tố đặc thù ngành bất động sản, thay bằng placeholder tổng quát "
        "[NGÀNH NGHỀ]/[SẢN PHẨM-DỊCH VỤ]/[PERSONA KHÁCH HÀNG] để bất kỳ ngành nghề nào "
        "(giáo dục, F&B, thời trang, y tế, tài chính, du lịch, B2B...) đều áp dụng được ngay."))
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=3)
    ws.cell(row=2, column=1).font = font(italic=True, size=9, color=GREY_TEXT)
    ws.cell(row=2, column=1).alignment = left()
    ws.row_dimensions[2].height = 48

    r = 4
    ws.cell(row=r, column=1, value="4 BƯỚC TÙY BIẾN FILE NÀY CHO NGÀNH NGHỀ CỦA BẠN").font = font(
        bold=True, size=11, color=HEADER_BLUE)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
    r += 1
    steps = [
        "1. Điền Sheet '4. Ho So Nganh Cua Ban' TRƯỚC TIÊN (ngành nghề, sản phẩm/dịch vụ, "
        "persona khách hàng, tông giọng thương hiệu, điều cấm kỵ khi quảng cáo).",
        "2. Sang Sheet '2. Thu Vien Prompt', chọn prompt phù hợp nhu cầu, copy nội dung, "
        "dán đè các thông tin ở Sheet 4 vào từng chỗ [TRONG NGOẶC VUÔNG] tương ứng.",
        "3. Nếu không có prompt mẫu nào phù hợp, dùng Sheet '3. Prompt Builder RTFC' để "
        "tự ghép 1 prompt mới theo đúng khung Role-Task-Format-Context.",
        "4. Dán prompt hoàn chỉnh vào ChatGPT/Claude/Gemini, luôn đọc và biên tập lại kết "
        "quả AI trước khi sử dụng chính thức (Human-in-the-loop).",
    ]
    for s in steps:
        c = ws.cell(row=r, column=1, value=s)
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
        c.alignment = left()
        c.font = font(size=9.5)
        ws.row_dimensions[r].height = 30
        r += 1

    r += 1
    ws.cell(row=r, column=1, value="CÁC SHEET TRONG FILE NÀY").font = font(bold=True, size=11, color=HEADER_BLUE)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
    r += 1
    sheets_info = [
        ("1. So Sanh Framework", "Bảng so sánh 5 khung prompt phổ biến (R-T-F-C, RACE, CO-STAR, TAG, APE) "
                                  "và gợi ý nên dùng khung nào cho từng loại tình huống."),
        ("2. Thu Vien Prompt", "20 prompt mẫu tổng quát theo nhóm công việc, có AutoFilter + Dropdown lọc "
                                "theo Nhóm công việc / Giai đoạn hành trình khách hàng / Công cụ AI ở hàng "
                                "tiêu đề. Bôi đen ô cột E (Nội dung prompt) → Ctrl+C → dán vào ChatGPT/"
                                "Claude/Gemini."),
        ("3. Prompt Builder RTFC", "Điền vào 4 ô màu vàng (Role - Task - Format - Context), ô màu xanh lá "
                                    "bên dưới TỰ ĐỘNG ghép thành 1 prompt hoàn chỉnh - dùng khi thư viện "
                                    "có sẵn chưa đúng ý bạn."),
        ("4. Ho So Nganh Cua Ban", "Điền 1 LẦN DUY NHẤT các thông tin đặc thù ngành nghề/thương hiệu của "
                                    "bạn để tra cứu nhanh khi cần dán vào chỗ [TRONG NGOẶC VUÔNG] ở các "
                                    "sheet khác."),
    ]
    for name, desc in sheets_info:
        ws.cell(row=r, column=1, value="").fill = fill(LIGHT_BLUE)
        c2 = ws.cell(row=r, column=2, value=name)
        c2.font = font(bold=True, size=10)
        c2.alignment = left()
        c2.fill = fill(LIGHT_BLUE)
        c2.border = border()
        c3 = ws.cell(row=r, column=3, value=desc)
        c3.alignment = left()
        c3.border = border()
        ws.row_dimensions[r].height = 48
        r += 1

    r += 1
    ws.cell(row=r, column=1, value="CHÚ GIẢI MÀU SẮC").font = font(bold=True, size=11, color=HEADER_BLUE)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
    r += 1
    legend = [
        (YELLOW, "Ô cần TỰ NHẬP (input) - điền thông tin ngành nghề/persona/số liệu thật của bạn"),
        (LIGHT_GREEN, "Ô TỰ ĐỘNG ghép bằng công thức Excel - không cần sửa tay"),
        (LIGHT_ORANGE, "Cảnh báo rủi ro / lưu ý bắt buộc kiểm soát con người (Human-in-the-loop)"),
    ]
    for color, desc in legend:
        ws.cell(row=r, column=1).fill = fill(color)
        ws.cell(row=r, column=1).border = border()
        c2 = ws.cell(row=r, column=2, value=desc)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        c2.alignment = left()
        c2.font = font(size=9)
        r += 1

    r += 1
    ws.cell(row=r, column=1, value="QUY TẮC VÀNG (áp dụng cho mọi ngành nghề)").font = font(
        bold=True, size=11, color=ORANGE)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
    r += 1
    rules = [
        "1. Luôn thay đủ các phần [TRONG NGOẶC VUÔNG] bằng thông tin thật của ngành nghề/"
        "thương hiệu bạn trước khi gửi AI.",
        "2. AI hỗ trợ soạn nháp/phân tích sơ bộ - bước biên tập cuối, kiểm tra pháp lý/số "
        "liệu/cam kết, và quyết định đăng bài LUÔN phải là con người.",
        "3. Không hỏi AI những số liệu thị trường thời sự mà AI không thể biết chắc chắn "
        "(nguy cơ AI Hallucination - AI bịa thông tin nghe có vẻ đúng).",
        "4. Mọi prompt sáng tạo nội dung nên mang theo Persona khách hàng + Giai đoạn hành "
        "trình + Chủ đề nội dung cốt lõi (điền ở Sheet 4) để tránh nội dung chung chung.",
        "5. Với ngành có quy định quảng cáo riêng (y tế, tài chính, bất động sản, thực phẩm "
        "chức năng...), luôn dùng thêm prompt Rà soát tuân thủ (Sheet 2, STT 14) trước khi đăng.",
    ]
    for rule in rules:
        c = ws.cell(row=r, column=1, value=rule)
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
        c.alignment = left()
        c.font = font(size=9.5)
        ws.row_dimensions[r].height = 28
        r += 1


# ============================================================
# SHEET 1: SO SANH FRAMEWORK PROMPT
# ============================================================
def build_framework_sheet(wb):
    ws = wb.create_sheet("1. So Sanh Framework")
    set_widths(ws, {"A": 12, "B": 46, "C": 60, "D": 14})

    title_row(ws, 1, "SO SÁNH CÁC FRAMEWORK (KHUNG) VIẾT PROMPT PHỔ BIẾN", 4)
    ws.row_dimensions[1].height = 22
    header_row(ws, 2, ["Framework", "Cấu trúc", "Phù hợp nhất cho", "Độ phức tạp"])

    r = 3
    for name, structure, use_case, complexity in FRAMEWORKS:
        ws.cell(row=r, column=1, value=name).font = font(bold=True, size=10)
        ws.cell(row=r, column=2, value=structure).alignment = left()
        ws.cell(row=r, column=3, value=use_case).alignment = left()
        ws.cell(row=r, column=4, value=complexity)
        for col in (1, 2, 3, 4):
            ws.cell(row=r, column=col).border = border()
            if col == 1:
                ws.cell(row=r, column=col).alignment = center()
            if col == 4:
                ws.cell(row=r, column=col).alignment = center()
        ws.row_dimensions[r].height = 40
        r += 1

    r += 1
    ws.cell(row=r, column=1, value=(
        "⚠️ Lưu ý: Không cần học thuộc cả 5 framework. Chỉ cần thành thạo R-T-F-C cho phần "
        "lớn công việc hàng ngày, và biết thêm CO-STAR cho các tình huống cần kiểm soát chặt "
        "giọng văn thương hiệu (ví dụ: nội dung pháp lý, thông cáo báo chí, nội dung nhạy cảm "
        "ngành y tế/tài chính).")).font = font(italic=True, size=9.5, color=ORANGE)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
    ws.cell(row=r, column=1).alignment = left()
    ws.row_dimensions[r].height = 36

    r += 2
    ws.cell(row=r, column=1, value="MASTER PROMPT TEMPLATE - KHUNG PROMPT VẠN NĂNG (R-T-F-C)").font = font(
        bold=True, size=11, color=HEADER_BLUE)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
    r += 1
    master_template = (
        "Bạn là [VAI TRÒ CHUYÊN GIA CỤ THỂ, ví dụ: \"chuyên gia content marketing ngành "
        "[NGÀNH NGHỀ] 10 năm kinh nghiệm\"].\n\n"
        "NHIỆM VỤ: [Mô tả chính xác việc cần làm, 1-2 câu, có động từ hành động rõ ràng: "
        "viết/tóm tắt/phân tích/dịch/liệt kê].\n\n"
        "DỮ LIỆU ĐẦU VÀO (nếu có):\n[Dán dữ liệu thô: số liệu, bài viết cũ, thông tin sản "
        "phẩm/dịch vụ...]\n\n"
        "YÊU CẦU ĐỊNH DẠNG ĐẦU RA:\n"
        "- Độ dài: [ví dụ: tối đa 100 từ / bảng 5 dòng / 3 phương án]\n"
        "- Cấu trúc: [ví dụ: đánh số, có tiêu đề in đậm, dạng bảng]\n"
        "- Ngôn ngữ/giọng văn: [ví dụ: tiếng Việt, thân thiện, không dùng từ chuyên ngành phức tạp]\n\n"
        "BỐI CẢNH THÊM (Context):\n"
        "- Đối tượng đọc: [persona khách hàng cụ thể]\n"
        "- Điều CẦN có: [ví dụ: phải có số liệu cụ thể, phải có CTA]\n"
        "- Điều CẦN TRÁNH (Negative Prompt): [ví dụ: không cam kết kết quả tuyệt đối vì vi "
        "phạm quy định quảng cáo ngành [NGÀNH NGHỀ], không dùng từ \"tốt nhất/số 1\" nếu "
        "không có căn cứ]\n\n"
        "Sau khi trả lời, hãy tự hỏi lại tôi 1 câu nếu thông tin tôi cung cấp chưa đủ để "
        "bạn làm tốt nhiệm vụ này."
    )
    c = ws.cell(row=r, column=1, value=master_template)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
    c.alignment = left()
    c.fill = fill("F2F2F2")
    c.font = font(size=9.5)
    c.border = border()
    ws.row_dimensions[r].height = 340

    r += 1
    ws.cell(row=r, column=1, value=(
        "📘 Kỹ thuật nâng cao 'hãy tự hỏi lại tôi...' ở cuối template gọi là Clarifying "
        "Question Prompting: thay vì để AI đoán mò khi thiếu thông tin (dễ dẫn đến "
        "hallucination), ta chủ động yêu cầu AI hỏi lại.")).font = font(
        italic=True, size=9, color=GREY_TEXT)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
    ws.cell(row=r, column=1).alignment = left()
    ws.row_dimensions[r].height = 30


# ============================================================
# SHEET 2: THU VIEN PROMPT (co AutoFilter + Dropdown)
# ============================================================
def build_library_sheet(wb):
    ws = wb.create_sheet("2. Thu Vien Prompt")
    set_widths(ws, {"A": 6, "B": 22, "C": 18, "D": 34, "E": 72, "F": 24, "G": 12, "H": 42})

    title_row(ws, 1, "THƯ VIỆN PROMPT AI TỔNG QUÁT - COPY DÁN DÙNG NGAY (thay phần [TRONG NGOẶC VUÔNG])", 8)
    ws.row_dimensions[1].height = 22

    headers = ["STT", "Nhóm công việc", "Giai đoạn hành trình KH", "Tên Prompt",
               "Nội dung Prompt đầy đủ", "Công cụ AI gợi ý", "Framework", "Ghi chú / Rủi ro cần kiểm soát"]
    header_row(ws, 2, headers)
    ws.row_dimensions[2].height = 20

    start_row = 3
    for i, p in enumerate(PROMPTS):
        row = start_row + i
        stt, nhom, giaidoan, ten, noidung, congcu, framework, ghichu = p
        values = [stt, nhom, giaidoan, ten, noidung, congcu, framework, ghichu]
        for col, val in enumerate(values, start=1):
            c = ws.cell(row=row, column=col, value=val)
            c.border = border()
            c.alignment = left() if col in (4, 5, 8) else center()
            c.font = font(size=9.5)
            if col == 5:
                c.fill = fill("F2F2F2")
            if col == 8:
                c.font = font(size=9, italic=True, color=ORANGE)
        n_lines = noidung.count("\n") + 1
        ws.row_dimensions[row].height = max(20, min(15 * n_lines, 320))

    last_row = start_row + len(PROMPTS) - 1

    ws.auto_filter.ref = f"A2:H{last_row}"
    ws.freeze_panes = "A3"

    dv_nhom = DataValidation(type="list", formula1=f'"{",".join(NHOM_LIST)}"', allow_blank=True)
    dv_nhom.error = "Vui long chon 1 gia tri trong danh sach"
    dv_nhom.prompt = "Chon nhom cong viec de loc"
    ws.add_data_validation(dv_nhom)
    dv_nhom.add(f"B3:B{last_row}")

    dv_giaidoan = DataValidation(type="list", formula1=f'"{",".join(GIAIDOAN_LIST)}"', allow_blank=True)
    dv_giaidoan.prompt = "Chon giai doan hanh trinh khach hang de loc"
    ws.add_data_validation(dv_giaidoan)
    dv_giaidoan.add(f"C3:C{last_row}")

    note_row = last_row + 2
    ws.cell(row=note_row, column=1, value=(
        "💡 Cách lọc nhanh: bấm mũi tên ở hàng tiêu đề (dòng 2) cột 'Nhóm công việc' hoặc "
        "'Giai đoạn hành trình KH' để chỉ hiện các prompt liên quan (AutoFilter)."))
    ws.merge_cells(start_row=note_row, start_column=1, end_row=note_row, end_column=8)
    ws.cell(row=note_row, column=1).font = font(italic=True, size=9, color=GREY_TEXT)
    ws.cell(row=note_row, column=1).alignment = left()

    return start_row, last_row


# ============================================================
# SHEET 3: PROMPT BUILDER THEO KHUNG R-T-F-C (co cong thuc ghep)
# ============================================================
def build_prompt_builder_sheet(wb):
    ws = wb.create_sheet("3. Prompt Builder RTFC")
    set_widths(ws, {"A": 26, "B": 90})

    title_row(ws, 1, "PROMPT BUILDER - TỰ GHÉP PROMPT THEO KHUNG R-T-F-C", 2)
    ws.cell(row=2, column=1, value=(
        "Điền vào 4 ô màu vàng bên dưới (dùng thông tin đã điền ở Sheet '4. Ho So Nganh Cua "
        "Ban'). Ô màu xanh lá ở cuối sẽ TỰ ĐỘNG ghép thành 1 prompt hoàn chỉnh - bôi đen, "
        "Ctrl+C, dán thẳng vào ChatGPT/Claude/Gemini."))
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=2)
    ws.cell(row=2, column=1).font = font(italic=True, size=9, color=GREY_TEXT)
    ws.cell(row=2, column=1).alignment = left()
    ws.row_dimensions[2].height = 34

    fields = [
        ("ROLE (Vai trò AI cần đóng)", "chuyên gia content marketing ngành [NGÀNH NGHỀ CỦA BẠN] "
         "10 năm kinh nghiệm, chuyên viết cho phân khúc [PHÂN KHÚC KHÁCH HÀNG]"),
        ("TASK (Nhiệm vụ cụ thể, có động từ hành động)", "Viết 1 bài đăng giới thiệu ưu đãi/"
         "chương trình mới của [TÊN SẢN PHẨM/DỊCH VỤ]"),
        ("FORMAT (Yêu cầu định dạng đầu ra)", "Tối đa 100 từ, có 3-4 emoji phù hợp, kết thúc "
         "bằng 1 câu CTA rõ ràng, không dùng từ chuyên ngành phức tạp"),
        ("CONTEXT (Bối cảnh: đối tượng đọc, điều cần có, điều cần tránh)", "Đối tượng: [MÔ TẢ "
         "PERSONA KHÁCH HÀNG]. Cần có: 1 con số/dẫn chứng cụ thể. Cần tránh: không cam kết "
         "kết quả tuyệt đối, không dùng từ 'duy nhất/số 1/tốt nhất' nếu không có căn cứ"),
    ]

    r = 4
    input_rows = []
    for label, placeholder in fields:
        lbl = ws.cell(row=r, column=1, value=label)
        lbl.font = font(bold=True, size=9.5)
        lbl.fill = fill(LIGHT_BLUE)
        lbl.alignment = left()
        lbl.border = border()
        val = ws.cell(row=r, column=2, value=placeholder)
        val.fill = fill(YELLOW)
        val.alignment = left()
        val.border = border()
        val.font = font(size=10)
        ws.row_dimensions[r].height = 46
        input_rows.append(r)
        r += 1

    role_row, task_row, format_row, context_row = input_rows

    r += 1
    ws.cell(row=r, column=1, value="PROMPT HOÀN CHỈNH (tự động ghép - copy ô bên phải)").font = font(
        bold=True, size=10, color=WHITE)
    ws.cell(row=r, column=1).fill = fill(GREEN)
    ws.cell(row=r, column=1).alignment = left()
    ws.cell(row=r, column=1).border = border()
    r += 1
    formula = (
        f'="Bạn là "&B{role_row}&".\n\nNHIỆM VỤ: "&B{task_row}&".\n\n'
        f'YÊU CẦU ĐỊNH DẠNG ĐẦU RA: "&B{format_row}&".\n\n'
        f'BỐI CẢNH THÊM: "&B{context_row}&".\n\n'
        f'"&"Sau khi trả lời, hãy tự hỏi lại tôi 1 câu nếu thông tin tôi cung cấp chưa đủ '
        f'để bạn làm tốt nhiệm vụ này."'
    )
    result_cell = ws.cell(row=r, column=2, value=formula)
    result_cell.fill = fill(LIGHT_GREEN)
    result_cell.alignment = left()
    result_cell.border = border()
    result_cell.font = font(size=10)
    ws.row_dimensions[r].height = 160
    ws.cell(row=r, column=1, value="👉 Copy ô này").font = font(italic=True, size=9, color=GREY_TEXT)
    ws.cell(row=r, column=1).alignment = left()

    r += 3
    ws.cell(row=r, column=1, value=(
        "📘 Ghi nhớ: đây chính là khung R-T-F-C ở Sheet '1. So Sanh Framework'. Với các tác "
        "vụ cần kiểm soát chặt giọng văn (VD: nội dung pháp lý, y tế, tài chính), tham khảo "
        "thêm khung CO-STAR cũng ở Sheet đó.")).font = font(italic=True, size=9, color=GREY_TEXT)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
    ws.cell(row=r, column=1).alignment = left()
    ws.row_dimensions[r].height = 30


# ============================================================
# SHEET 4: HO SO NGANH CUA BAN (dien 1 lan, tra cuu de dan vao cho khac)
# ============================================================
def build_industry_profile_sheet(wb):
    ws = wb.create_sheet("4. Ho So Nganh Cua Ban")
    set_widths(ws, {"A": 34, "B": 70})

    title_row(ws, 1, "HỒ SƠ NGÀNH NGHỀ / THƯƠNG HIỆU CỦA BẠN - ĐIỀN 1 LẦN, DÙNG LẠI NHIỀU LẦN", 2)
    ws.cell(row=2, column=1, value=(
        "Điền vào cột B các thông tin đặc thù ngành nghề/thương hiệu của bạn. Sau đó mỗi khi "
        "gặp placeholder [TRONG NGOẶC VUÔNG] ở Sheet 2 hoặc Sheet 3, quay lại đây copy đúng "
        "thông tin tương ứng để dán vào."))
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=2)
    ws.cell(row=2, column=1).font = font(italic=True, size=9, color=GREY_TEXT)
    ws.cell(row=2, column=1).alignment = left()
    ws.row_dimensions[2].height = 36

    fields = [
        ("[NGÀNH NGHỀ CỦA BẠN]", "Ví dụ: giáo dục/đào tạo online, F&B, thời trang, y tế/thẩm "
         "mỹ, tài chính/bảo hiểm, du lịch/lữ hành, phần mềm B2B..."),
        ("[TÊN THƯƠNG HIỆU CỦA BẠN]", "Ví dụ: tên công ty/thương hiệu bạn đang làm content"),
        ("[SẢN PHẨM/DỊCH VỤ]", "Ví dụ: tên dòng sản phẩm/dịch vụ chính đang cần quảng bá"),
        ("[PERSONA KHÁCH HÀNG]", "Mô tả 1 nhóm khách hàng mục tiêu cụ thể: độ tuổi, nghề "
         "nghiệp, thu nhập, nỗi đau/mong muốn lớn nhất"),
        ("[PHÂN KHÚC KHÁCH HÀNG]", "Ví dụ: phổ thông/trung cấp/cao cấp, hoặc theo ngành dọc "
         "cụ thể nếu là B2B"),
        ("[TÔNG GIỌNG THƯƠNG HIỆU]", "Ví dụ: thân thiện - gần gũi / chuyên nghiệp - đáng tin "
         "cậy / trẻ trung - hài hước"),
        ("[TÊN CONTENT PILLAR/CHỦ ĐỀ LỚN]", "Các chủ đề nội dung cốt lõi thương hiệu bạn "
         "thường xuyên khai thác"),
        ("[TỪ KHÓA CHÍNH THƯỜNG DÙNG]", "Các từ khóa SEO quan trọng nhất của ngành/sản phẩm bạn"),
        ("[ĐIỀU CẤM KỴ KHI QUẢNG CÁO]", "Quy định/luật quảng cáo riêng của ngành bạn (nếu có), "
         "ví dụ: không cam kết hiệu quả tuyệt đối, không so sánh trực tiếp đối thủ, không dùng "
         "hình ảnh minh họa gây hiểu lầm..."),
        ("[TÊN ĐỐI THỦ CHÍNH]", "1-3 đối thủ cạnh tranh trực tiếp cần theo dõi nội dung"),
    ]

    r = 4
    header_row(ws, 3, ["Placeholder cần thay", "Ghi chú gợi ý (điền thông tin thật vào cột bên "
                        "phải mỗi dòng, ngay dưới ô gợi ý)"])
    for label, hint in fields:
        lbl = ws.cell(row=r, column=1, value=label)
        lbl.font = font(bold=True, size=10)
        lbl.fill = fill(LIGHT_BLUE)
        lbl.alignment = left()
        lbl.border = border()
        hint_cell = ws.cell(row=r, column=2, value=hint)
        hint_cell.font = font(italic=True, size=9, color=GREY_TEXT)
        hint_cell.alignment = left()
        hint_cell.border = border()
        ws.row_dimensions[r].height = 30
        r += 1
        input_cell = ws.cell(row=r, column=1, value="👉 Điền thông tin thật tại đây:")
        input_cell.font = font(italic=True, size=9, color=GREY_TEXT)
        input_cell.alignment = left()
        val_cell = ws.cell(row=r, column=2, value="")
        val_cell.fill = fill(YELLOW)
        val_cell.border = border()
        val_cell.alignment = left()
        ws.row_dimensions[r].height = 24
        r += 1

    r += 1
    ws.cell(row=r, column=1, value=(
        "⚠️ Sau khi điền xong sheet này, mọi prompt ở Sheet 2 & 3 chỉ mất 1-2 phút để tùy "
        "biến vì bạn chỉ cần copy-paste từ đây, không phải nghĩ lại từ đầu mỗi lần.")).font = font(
        italic=True, size=9.5, color=ORANGE, bold=True)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
    ws.cell(row=r, column=1).alignment = left()
    ws.row_dimensions[r].height = 32


def main():
    wb = openpyxl.Workbook()
    build_huongdan_sheet(wb)
    build_framework_sheet(wb)
    build_library_sheet(wb)
    build_prompt_builder_sheet(wb)
    build_industry_profile_sheet(wb)

    wb.save(OUT_PATH)
    print(f"Da tao file: {OUT_PATH}")
    print(f"Tong so prompt trong thu vien: {len(PROMPTS)}")


if __name__ == "__main__":
    main()
