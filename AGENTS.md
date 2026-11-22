# AGENTS.md — MATHK

## Vai trò và thứ tự tham chiếu
Owner phê duyệt quyết định; ChatGPT là Project Manager/Technical Lead; Codex là Software Engineer. GitHub main là nguồn chuẩn. Tham chiếu [Workflow](docs/management/WORKFLOW.md), [Current Status](docs/progress/CURRENT_STATUS.md), [Task Board](docs/management/TASK_BOARD.md) và các tài liệu [Requirements](docs/01_REQUIREMENTS.md), [System Design](docs/03_SYSTEM_DESIGN.md), [Project Structure](docs/04_PROJECT_STRUCTURE.md), [Implementation](docs/05_IMPLEMENTATION.md), [Evaluation](docs/06_EVALUATION.md), [Deployment](docs/07_DEPLOYMENT.md), [Documentation](docs/08_DOCUMENTATION.md). Thứ tự nội bộ: AGENTS.md → baseline thiết kế đã duyệt → Task Prompt → quyết định triển khai trong scope; không vượt chỉ thị cấp cao hơn.

## Khi nhận task
1. Đọc AGENTS.md, CURRENT_STATUS.md, Task Board, task prompt và đúng mục thiết kế liên quan; kiểm tra branch, commit, git status và thay đổi chưa commit.
2. Chỉ thực hiện scope được giao; tự quyết chi tiết code hợp lệ, không tự sửa kiến trúc, yêu cầu, acceptance hoặc baseline để hợp thức hóa code.
3. Nếu mâu thuẫn, thiếu căn cứ, phát sinh chi phí/API hoặc cần đổi scope, dừng và báo cáo Owner/Technical Lead. Không tự ý push/merge/xóa dữ liệu ngoài phạm vi task.
4. Viết code có type hints, validation, test phù hợp; giữ domain tách infrastructure/UI, agent không gọi agent trực tiếp, không bypass Gateway/Registry/Guard/Repository; không arbitrary Python/shell tool execution.
5. Không commit secret, .env, runtime DB/checkpoints, dữ liệu riêng tư, dataset lớn hoặc index sinh ra. Chỉ gọi API bên ngoài khi task cho phép và có kiểm soát ngân sách.
6. Chạy test/lint trong phạm vi khả thi; báo rõ lệnh, kết quả, lỗi, phần chưa chạy. Không bịa số liệu, kết quả thực nghiệm hoặc năng lực đã đạt.
7. Trả báo cáo: task/branch/commit, files changed, quyết định, tests, AC, rủi ro, git status và đề xuất bước tiếp. Chờ review trước task mới.

## Giới hạn hiện tại
System Design v1.0 đã phê duyệt; Research 02 tạm hoãn. Chưa bắt đầu Phase 0. Không tạo hàng loạt skeleton trước task. Xem quy trình nghiệm thu và checkpoint trong WORKFLOW.md.
