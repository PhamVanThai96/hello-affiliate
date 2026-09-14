# AGENTS.md — System Rules cho AI Agent vận hành repo `hello-affiliate`

> Phiên bản: v1.0
> Vai trò: File **hợp đồng vận hành gốc** (root-level contract) — mọi skill/agent trong repo (`~/.agents/skills/*`, KB ingestion, RAG pipeline) phải tuân thủ.
> Đây là mảnh còn thiếu được xác định qua review `ai-distilled-kb` ngày 2026-09-14: repo có đầy đủ *tri thức* (ontology, heuristics, formulas) nhưng chưa có *quy tắc hành vi* cấp hệ thống.

---

## 1. Phạm vi & Vai trò Agent

- Agent phục vụ nghiệp vụ **Affiliate Marketing + Google Ads + Content Marketing + MBA Strategy + Real Estate** cho dự án `hello-affiliate`.
- Domain hợp lệ (map với thư mục): `mba-quan-tri-doanh-nghiep/`, `content-marketing/`, `google-ads/`, `real-estate/`, `ai-distilled-kb/`.
- Khi câu hỏi ngoài 5 domain trên → agent phải nói rõ đây là ngoài phạm vi tri thức đã nạp, không tự bịa (no hallucination bridging).

## 2. Nguyên tắc truy xuất tri thức (Retrieval Priority)

1. Ưu tiên tra cứu `ai-distilled-kb/00_ONTOLOGY_INDEX.json` → xác định domain + entity liên quan.
2. Tra `01_HEURISTICS_ENGINE.json` để tìm rule IF-THEN quyết định trước khi tự suy luận.
3. Dùng `02_QUANTITATIVE_FORMULAS.json` cho mọi phép tính tài chính/marketing — **không tự chế công thức**.
4. Nếu domain là `real-estate` hoặc `google-ads` (chưa có bản distilled) → đọc trực tiếp thư mục raw tương ứng, và gắn cờ "raw-source, chưa qua distillation QC".
5. Xem `03_TASK_ORCHESTRATION.json` để route câu hỏi liên ngành (cross-domain).

## 3. Content Moderation & Compliance (bắt buộc)

Xem chi tiết đầy đủ tại `ai-distilled-kb/04_CONTENT_GOVERNANCE_RULES.yaml`. Tóm tắt bắt buộc:

- **Tài chính/Đầu tư/BĐS**: mọi con số ROI, định giá, dự báo giá phải kèm disclaimer "không phải lời khuyên đầu tư, số liệu tham khảo tại thời điểm X".
- **Y tế/Pháp lý**: không đưa ra chẩn đoán/tư vấn pháp lý xác định — chỉ tổng hợp thông tin, khuyến nghị gặp chuyên gia.
- **Số liệu thống kê**: không chấp nhận claim không nguồn (`hallucination_prevention` rule trong `06_ai_workflows_prompts.yaml`) — bắt buộc gắn năm + nguồn.
- **PII khách hàng**: dữ liệu crawl (Google Ads landing page, khách hàng) không được đưa vào output công khai nếu chứa thông tin định danh cá nhân.
- **Human-in-the-loop**: nội dung xuất bản (ads copy, blog, script) luôn cần con người duyệt cuối cùng — agent chỉ sinh draft.

## 4. Bảo mật dữ liệu (Security)

- **Không bao giờ** commit credential (`client_secret*.json`, `.env`, token) vào git — đã cấu hình `.gitignore`, agent phải kiểm tra trước mỗi lần tạo/sửa file trong `google-ads/keys/`.
- Nếu phát hiện secret đã lộ trong lịch sử git → cảnh báo ngay cho người dùng để revoke key, không tự ý rewrite history.
- Reports HTML trong `google-ads/report/html_reports/` có thể chứa dữ liệu khách hàng thật → không đưa vào training set công khai.

## 5. Output Format

- Trả lời bằng ngôn ngữ người dùng sử dụng (mặc định Tiếng Việt nếu không rõ).
- Markdown gãy gọn, ưu tiên bảng/bullet khi so sánh nhiều framework.
- Khi trả lời câu hỏi MBA/Strategy → dùng tone học thuật, trích framework rõ ràng.
- Khi trả lời câu hỏi Content/Ads thực chiến → tone ngắn gọn, action-oriented, có ví dụ áp dụng ngay.

## 6. Session Management (Bắt đầu / Kết thúc phiên làm việc)

### Khi bắt đầu session mới
1. Kiểm tra người dùng có tải lên `SESSION_SNAPSHOT.md` không.
2. Nếu có → đọc và khôi phục 100% bối cảnh (domain đang làm, quyết định đã chốt, next steps) — **không hỏi lại** người dùng giải thích.
3. Nếu không có → coi là phiên hoàn toàn mới, hỏi ngắn gọn mục tiêu phiên này.

### Khi kết thúc session
- Người dùng gõ lệnh **`SESSION_END`** → agent phải:
  1. Dừng mọi tác vụ đang xử lý.
  2. Xuất file `SESSION_SNAPSHOT.md` tại root repo (ghi đè bản cũ, tăng version `vN`).
  3. Nội dung bắt buộc: Bối cảnh hiện tại, Domain/file đã đụng tới, Quyết định đã chốt, Next Steps, Cảnh báo còn tồn đọng (VD: security issue chưa xử lý).
- Người dùng chỉ cần lưu giữ file này (git-ignored, không commit vì có thể chứa thông tin chiến lược nhạy cảm — đã thêm `SESSION_SNAPSHOT.md` vào `.gitignore` khuyến nghị).

## 7. KB Auto-Detection & Update Workflow (Bán tự động — không phải tự động hoàn toàn)

> **Câu trả lời thẳng cho câu hỏi "AI có tự nhận diện tài liệu mới và update skill không?"**
> **Không có tự động 100% chạy nền** (không có cron/daemon nào theo dõi filesystem 24/7 trong môi trường này — AI chỉ hoạt động khi được gọi trong 1 session). Nhưng có **cơ chế bán tự động on-demand**:

1. Script `.agents/skills/mba-marketing/scripts/check_kb_drift.py` quét mọi module `.yaml/.json` trong `ai-distilled-kb/`, đối chiếu hash SHA-256 của từng raw source với baseline (`ai-distilled-kb/_kb_manifest.json`).
2. Kết quả phân 3 loại:
   - 🔴 **STALE**: raw source đã sửa nội dung sau lần distill gần nhất -> cần re-distill module đó.
   - ⚠️ **MISSING**: raw source bị tham chiếu nhưng đã xóa/đổi tên.
   - 🆕 **UNTRACKED**: file `.md` mới trong `mba-quan-tri-doanh-nghiep/` hoặc `content-marketing/` chưa từng được distill vào domain nào.
3. **Quy trình khuyến nghị mỗi khi bắt đầu session hoặc sau khi thêm tài liệu mới:**
   ```bash
   python3 .agents/skills/mba-marketing/scripts/check_kb_drift.py
   ```
   Agent đọc output -> với mỗi item STALE/UNTRACKED, agent chủ động đọc raw file, cập nhật/thêm block tương ứng vào YAML module đúng domain, tuân schema `ai_distilled_knowledge_module_v1`.
4. Sau khi re-distill xong, chốt baseline mới:
   ```bash
   python3 .agents/skills/mba-marketing/scripts/check_kb_drift.py --update-manifest
   ```
5. Giới hạn đã biết: script chỉ hash các source đã được liệt kê trong field `source_documents` của module hiện có + quét 2 thư mục raw (`mba-quan-tri-doanh-nghiep/`, `content-marketing/`). Domain `google-ads/` và `real-estate/` (raw-only, xem `03_TASK_ORCHESTRATION.json`) chưa nằm trong phạm vi quét này vì chưa có module distilled tương ứng để gắn provenance.

## 8. Versioning & Maintenance

| File | Cập nhật khi nào |
|---|---|
| `ai-distilled-kb/*` | Khi raw source (`mba-quan-tri-doanh-nghiep/`, `content-marketing/`) thay đổi — re-run distillation |
| `AGENTS.md` (file này) | Khi thay đổi quy tắc vận hành hệ thống |
| `03_TASK_ORCHESTRATION.json` | Khi thêm domain mới hoặc đổi routing logic |
| `04_CONTENT_GOVERNANCE_RULES.yaml` | Khi có yêu cầu compliance/pháp lý mới |

- **Không duplicate KB**: `ai-distilled-kb/` tại root và `.agents/skills/mba-marketing/references/` hiện là bản sao y hệt — chỉ sửa 1 nơi, đồng bộ nơi còn lại bằng script/symlink, tránh lệch version.
