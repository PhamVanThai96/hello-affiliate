## Cai dat Node.js - MACOS
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.8/install.sh | bash

\. "$HOME/.nvm/nvm.sh"

nvm install 24

node -v

nvm -v

## Chạy

```bash
cd /home/worker/DEMO-agency-office
npm start            # chế độ MOCK (không cần API key)
# mở http://localhost:3000
```

## Dùng CLI đã đăng nhập (không cần API key) REAL MODE

Server gọi trực tiếp `claude` / `codex` / `gemini` đã đăng nhập trên máy bạn.

1. Cài và đăng nhập một lần: `claude auth login` (hoặc chạy `claude`), `codex login`, hoặc chạy `gemini` rồi đăng nhập Google.
2. Kiểm tra: `claude --version` (hoặc `codex --version`, `gemini --version`) chạy được trong terminal.
3. Trong `config.json`: `"MODE": "REAL"`, `"CONNECTION": "CLI"`, `"AI_PROVIDER": "claude"`. Nếu lệnh không nằm trong PATH, đặt `"CLI": {"claude": "/đường/dẫn/claude"}`.
4. Khởi động lại `npm start`; dòng trạng thái hiển thị `CLI claude/...`. CLI không tìm thấy thì tự dùng MOCK và báo lý do.

Lưu ý:
- Biến `*_API_KEY` bị gỡ khi gọi CLI để dùng đúng tài khoản đăng nhập.
- Mỗi lần gọi là một tiến trình mới trong thư mục tạm rỗng, chậm hơn API; công cụ `read_file`/`list_dir` được gọi qua giao thức văn bản (JSON) và vẫn qua hộp xác nhận quyền.
- Tính năng chỉ kiểm thử với CLI giả lập, **chưa thử với CLI thật**; cờ dòng lệnh có thể khác theo phiên bản.
- Điều khoản dịch vụ của nhà cung cấp về việc tự động hoá gói thuê bao chưa được xác minh; hãy tự kiểm tra.

## Sử dụng
1. Nhập yêu cầu vào ô "Ra lệnh cho Quản Lí…" rồi bấm **Giao**. Agent Quản Lí lập kế hoạch, chia task cho các agent; các agent bàn giao/hỏi đáp lẫn nhau và báo cáo về Quản Lí. Quản Lí gửi báo cáo cuối cho CEO ở khung "Báo cáo gửi CEO".
2. Muốn giao thẳng cho một agent, thêm `/id` đầu câu, ví dụ `/secretary đặt lịch hẹn 10h sáng mai` (id mặc định: manager, secretary, reviewer, rag, analyst, designer, dev, tester).
3. Quan sát đường nối giữa các agent để biết ai đang nói chuyện với ai; xem chú giải màu ở đầu trang và chi tiết ở [docs/SOCIAL-COLLAB-LOOP.md](docs/SOCIAL-COLLAB-LOOP.md). Mỗi lần chỉ chạy một yêu cầu.

**Lưu ý:** phải mở trang do `npm start` phục vụ (kể cả qua proxy cổng của code-server). Mở file `index.html` trực tiếp hoặc bằng server tĩnh khác (Live Server, `python -m http.server`) sẽ báo "Unsupported method POST" và văn phòng trống.

## Tính năng cập nhật từ agent-office (2026-10-29)

Đã đưa các phần dùng chung của `agent-office` sang đây (không kèm phần riêng của content marketing: Enzy, insight khách hàng, Trend & Idea, video, khu vườn mèo).

- **Cấu hình AI + xác thực bằng tài khoản đã đăng nhập trên máy:** `Cấu hình → Cấu hình AI → Kết nối "CLI" → Đăng nhập / xác thực`. Server dùng `claude` / `codex` đã đăng nhập (không cần API key); xác thực xong tự bật REAL qua CLI. Có đăng nhập CLI ngay trên giao diện, hiển thị model đang dùng. Mẫu cấu hình: `config.example.json`.
- **Harness (điều phối):** agent *duyệt* (`"gate": true` trong `agents.json`, mặc định là `reviewer`) kết luận "YÊU CẦU SỬA" thì việc được trả về agent trước đó sửa lại (tối đa 1 vòng); mỗi agent chỉ một việc một lúc; công cụ `run_command` (đọc/tìm file, chẩn đoán lỗi) qua hộp xác nhận quyền; đính kèm file bằng kéo thả; ngân sách công cụ và agent `lean`/`tools` để tiết kiệm token; hộp suy nghĩ có chi tiết.
- **Bộ nhớ dài hạn:** `memory.js` (kết quả các lần làm trước, chỉ nạp phần liên quan, cắt gọn) + sổ tay kinh nghiệm riêng từng agent (`data/agents/<id>.json`, tự nén khi đủ dài) + digest kỹ năng. Xem/sửa ở `Cấu hình → Trí nhớ & kỹ năng agent`.
- **Tự học & kỹ năng:** sau mỗi yêu cầu agent tự hợp nhất bài học (từ người duyệt "YÊU CẦU SỬA" và từ đánh giá 👍/👎 + nhận xét của CEO ở khung "Báo cáo gửi CEO"). Kỹ năng dùng chung là YAML trong `skills/` (xem `skills/README.md`); agent tra bằng công cụ `skill_search`.
- **Khác:** đăng nhập Admin bảo vệ sửa/xoá agent và đổi cấu hình (`node scripts/set-admin.mjs` hoặc tạo trên giao diện từ máy chạy server); dashboard giám sát token theo model/yêu cầu/tháng + hạn mức tháng; báo cáo tải nhiều file (.zip) và xoá; bảng cấu hình agent có công cụ/gate/lean/AI riêng.
- **Lưu ý:** `.gitignore` mới bỏ qua `config.json`, `data/` (có hash mật khẩu Admin), `memory.json`, `permissions.json`. `config.json` và `permissions.json` hiện còn trỏ tới thư mục cũ `DEMO-agency-office`: hãy đổi `SOURCE_DIR` và quyền sang thư mục này nếu muốn agent đọc/ghi file ở đây.

### Agent Financial Expert (Phòng nghiên cứu)
Chuyên gia tài chính doanh nghiệp dùng bộ skill `finance-agent-skill` (xem `skills/README.md`). Yêu cầu có từ khoá tài chính (NPV/IRR, WACC, cơ cấu vốn, phân tích báo cáo tài chính, vốn lưu động, cổ tức, định giá, M&A…) tự được định tuyến `Financial Expert → Rà soát` (quy trình `finance` trong `workflows.json`); hoặc giao thẳng bằng `/financial_expert <yêu cầu>`. Agent tra công thức bằng `skill_search`, tính bằng `run_command` (python, qua hộp xác nhận quyền) và kiểm tra chéo trước khi kết luận.

