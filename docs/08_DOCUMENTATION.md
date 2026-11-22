# MATHK — Documentation

**Phiên bản:** 0.1

**Trạng thái:** Đang thảo luận

## 1. Project Management & Agent Collaboration

**Trạng thái: Đã chốt.**

Project Owner (người học) giữ quyền quyết định cuối cùng, thiết kế và học tập; ChatGPT là Project Manager & Technical Lead, quản lý context, chia task, soạn prompt, review và hướng dẫn; Codex là Software Engineer, triển khai code, test, sửa lỗi và báo cáo. Owner chuyển tiếp prompt và báo cáo giữa hai agent. GitHub là Single Source of Truth.

```mermaid
flowchart TD
 A["ChatGPT đọc trạng thái"] --> B["Phân tích và giao task"]
 B --> C["Owner chuyển prompt"]
 C --> D["Codex triển khai và test"]
 D --> E["Owner chuyển báo cáo"]
 E --> F["ChatGPT review"]
 F --> G{"Đạt yêu cầu?"}
 G -->|Không| B
 G -->|Có| H["Learning Gate và checkpoint"]
 H --> A
```

Prompt tiếng Việt: Task ID, Context, Objective, References, Scope, Requirements, Constraints, Acceptance Criteria, Testing, Deliverables, Report Format. Codex không tự đổi kiến trúc, thêm dependency, vượt scope hoặc phase; báo cáo file thay đổi, test results, quyết định, lỗi và vấn đề tồn tại; dừng báo cáo mâu thuẫn. ChatGPT đối chiếu báo cáo với yêu cầu và đọc code/diff khi cần, không mặc định báo cáo đúng.

Task lifecycle: PLANNED → ASSIGNED → IN_PROGRESS → IN_REVIEW → ACCEPTED → COMPLETED; NEEDS_REVISION quay lại triển khai. COMPLETED cần Engineering Gate, Learning Gate và Checkpoint Gate. Owner giữ quyền phê duyệt quyết định quan trọng.

Quản lý dài hạn: AGENTS.md; docs/management/WORKFLOW.md, TASK_BOARD.md, DECISION_LOG.md; docs/progress/CURRENT_STATUS.md và phase_00.md, các phase tiếp theo theo nhu cầu. Checkpoint sau từng task nghiệm thu, không chờ context gần đầy. CURRENT_STATUS ghi phase, task, kết quả, vấn đề mở và bước tiếp theo. Các file bổ sung sẽ được tạo theo nhu cầu, chưa mặc định tồn tại.

Trọng tâm học: system/model/data thinking, cost optimization, research methodology, technical review; Codex đảm nhiệm phần lớn code. ChatGPT giao việc bằng prompt cho Owner chuyển tiếp, không tuyên bố điều khiển trực tiếp Codex.

## 2. Documentation Strategy

*Chưa chốt.*

## 3. Documentation Structure

*Chưa chốt.*

## 4. Project README

*Chưa chốt.*

## 5. Developer Guide

*Chưa chốt.*

## 6. AI Agent Instructions

*Chưa chốt.*

## 7. Learning Documentation

*Chưa chốt.*

## 8. Architecture & API Documentation

*Chưa chốt.*

## 9. Research Documentation

*Chưa chốt.*

## 10. User & Deployment Guide

*Chưa chốt.*

## 11. Context & Progress Management

*Chưa chốt.*

## 12. Documentation Maintenance

*Chưa chốt.*
