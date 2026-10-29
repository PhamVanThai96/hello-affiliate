# Kỹ năng dùng chung của team (skills/*.yaml)

Mỗi file YAML là một "kho kỹ năng" tự khai báo áp dụng cho ai: `agents: [id…]` hoặc `["*"]` (mọi agent), `rooms: [tên phòng]`, `exclude: [id]`.
Các mục (`sections`) được agent tra nhanh bằng công cụ `skill_search`; phần nội dung được nạp vào prompt (nén lại khi quá dài).

- Thêm kiến thức: tạo `skills/NN-ten.yaml` (xem `00-quy-tac-lam-viec.yaml`), không cần sửa code hay `agents.json`.
- Agent **không được** tự sửa thư mục này (bị chặn ở `access.js`); chỉ người dùng chỉnh.
- Kinh nghiệm agent tự học (từ đánh giá 👍/👎 của CEO và từ người duyệt) nằm riêng ở `data/agents/<id>.json`, xem/sửa trong "Cấu hình → Trí nhớ & kỹ năng agent".

## Bộ skill tài chính cho agent Financial Expert (`skills/finance-*.yaml`)
Sinh tự động từ bộ gốc `mba-quan-tri-doanh-nghiep/3-financial-management/finance-agent-skill` (nguồn chính, ~1 MB, 11 module, 286 công thức, 85 thuật ngữ, 11 playbook, mẫu báo cáo):

    python3 scripts/import_finance_skill.py      # cần pyyaml; chạy lại mỗi khi sửa bộ gốc (ghi đè skills/finance-*.yaml)

- `finance-00-core.yaml`: luôn nạp vào prompt (vai trò, nguyên tắc, quy trình trả lời, bảng định tuyến câu hỏi → module).
- `finance-mNN-*.yaml`: tự nạp phần tổng quan của module khi yêu cầu có từ khoá liên quan (khoá `when`, lấy từ bộ định tuyến gốc); `body_max` giới hạn phần vào prompt.
- `finance-playbooks / report-templates / glossary / formulas-index`: chỉ tra cứu bằng `skill_search` (khoá `when` không bao giờ khớp).
- Toàn bộ nội dung (≈1.770 mục: khái niệm, công thức, quy trình, ví dụ có lời giải, lỗi thường gặp, checklist…) tra được bằng `skill_search`, vd `m03_wacc`, `pb_wacc`, `DuPont`.
- Chỉ agent `financial_expert` dùng các skill này (khoá `agents`).

