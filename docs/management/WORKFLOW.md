# Workflow — MATHK

**Trạng thái:** Đã khởi tạo theo Documentation v1.1; trước Phase 0.

## Phân công
- **Owner:** quyết định mục tiêu, kiến trúc, thay đổi scope, nghiệm thu quan trọng; học, phản biện, chuyển prompt và báo cáo.
- **ChatGPT (PM/Technical Lead):** lập kế hoạch, tạo task và AC, quản lý traceability/decision/status, review evidence, hướng dẫn kiến thức.
- **Codex (Software Engineer):** thực hiện đúng task, code/test/document trong scope, báo cáo kết quả, không tự duyệt thay đổi baseline.

## Task Lifecycle
`PLANNED → ASSIGNED → IN_PROGRESS → IN_REVIEW → ACCEPTED → COMPLETED`. Nếu chưa đạt: `NEEDS_REVISION → IN_PROGRESS`. `ACCEPTED` là nghiệm thu kỹ thuật; `COMPLETED` cần đủ Engineering Gate, Learning Gate và Checkpoint Gate. Task kiểm tra tài liệu trước Phase 0 có thể hoàn tất mà không yêu cầu minh chứng học lập trình; ghi rõ ngoại lệ theo scope.

## Chu kỳ làm việc
1. Đọc CURRENT_STATUS, TASK_BOARD, DECISION_LOG, AGENTS và tài liệu baseline liên quan từ main; kiểm tra commit thực tế.
2. PM đề xuất scope, mục tiêu, requirement IDs, AC, test, constraints, deliverables và learning goal. Owner duyệt các thay đổi quan trọng.
3. Owner chuyển prompt cho Codex; Codex xác minh Git, thực thi, test, báo cáo; không tự ý mở rộng phạm vi.
4. PM đối chiếu bằng chứng và AC; ghi rõ điểm chưa kiểm chứng. Nếu cần, yêu cầu sửa với tiêu chí cụ thể.
5. Sau nghiệm thu, cập nhật Task Board, Traceability Matrix theo evidence thật, Decision Log nếu có quyết định, CURRENT_STATUS và phase log. Commit/push, đọc lại nội dung để xác minh.
6. Chỉ chuyển Phase khi Engineering, Learning và Checkpoint Gates đạt. Không suy diễn PASS từ PLANNED hoặc báo cáo chưa xác minh.

## Quy tắc
- GitHub main là Single Source of Truth. Không ghi đè thay đổi chưa commit của Owner; không tự động merge/push nếu task không cho phép.
- Giữ ngôn ngữ tài liệu tiếng Việt, thuật ngữ kỹ thuật tiếng Anh khi cần.
- Bảo vệ secrets, dữ liệu cá nhân và chi phí API; ưu tiên mock/offline test, bounded retries.
- 8 GB RAM, Full API Inference; local orchestration, tools và storage; theo Deployment.
- Không sửa baseline khi chưa được Owner phê duyệt. 02_RESEARCH.md tạm hoãn.
- Tài liệu ngắn gọn, dẫn link thay vì lặp nội dung. Checkpoint sau mỗi task được nghiệm thu và quyết định quan trọng.
