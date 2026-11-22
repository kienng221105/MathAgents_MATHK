# Task Board — MATHK

**Trạng thái:** Khởi tạo trước Phase 0. Không có task lập trình đang triển khai.

| Task | Nội dung | Phase | Trạng thái | Bằng chứng / Ghi chú |
|---|---|---|---|---|
| PRE-001 | Mermaid Validation 227 sơ đồ | Pre-Implementation | COMPLETED | [AUDIT_LOG](AUDIT_LOG.md): ACCEPTED theo báo cáo Codex; đính chính bảng 05 Implementation 12 Render PASS |
| PRE-002 | Chốt System Design v1.0 và khởi tạo quản lý | Pre-Implementation | COMPLETED | [System Design](../03_SYSTEM_DESIGN.md), AGENTS, WORKFLOW, TASK_BOARD, DECISION_LOG, CURRENT_STATUS |
| P0-PLAN | Phân rã Phase 0 Foundation thành task và lab | Phase 0 (planning) | PLANNED | Chưa giao Codex; cần Owner duyệt scope và AC |
| P0-IMPL | Triển khai Foundation | Phase 0 | NOT_STARTED | Chỉ lập sau khi P0-PLAN được duyệt |

## Backlog kiểm thử kiến trúc
- ARCH-001: kiểm thử quyền cập nhật state và stale state version (Phase 3).
- ARCH-002: ngân sách chung khi SDK/proxy/Gateway cùng retry (Phase 2–3).
- ARCH-003: recovery khi gián đoạn API call / DB commit / checkpoint (Phase 3, 7).

Chi tiết tại [AUDIT_LOG](AUDIT_LOG.md). Requirement traceability 259 ID đang là [bản sơ bộ](TRACEABILITY_MATRIX.md); không đánh dấu coverage PASS trước bằng chứng test.
