# Task Board — MATHK

**Trạng thái:** Phase 0 planning đã được Owner phê duyệt. P0-01 đã giao qua prompt, chờ Codex thực hiện.

| Task | Nội dung | Phase | Trạng thái | Bằng chứng / Ghi chú |
|---|---|---|---|---|
| PRE-001 | Mermaid Validation 227 sơ đồ | Pre-Implementation | COMPLETED | [AUDIT_LOG](AUDIT_LOG.md): ACCEPTED theo báo cáo Codex; đính chính bảng 05 Implementation 12 Render PASS |
| PRE-002 | Chốt System Design v1.0 và khởi tạo quản lý | Pre-Implementation | COMPLETED | [System Design](../03_SYSTEM_DESIGN.md), AGENTS, WORKFLOW, TASK_BOARD, DECISION_LOG, CURRENT_STATUS |
| P0-PLAN | Phân rã Phase 0 Foundation thành task và lab | Phase 0 (planning) | COMPLETED | [Planning Baseline](PHASE_00_PLAN.md) đã được Owner duyệt |
| P0-01 | Python Foundation & Project Skeleton | Phase 0 | ASSIGNED | [Task Contract](PHASE_00_PLAN.md#p0-01-task-contract); chờ báo cáo Codex |
| P0-02 | Data Contracts & Configuration | Phase 0 | PLANNED | P0-L03–L04 |
| P0-03 | LLM API Anatomy | Phase 0 | PLANNED | P0-L05 |
| P0-04 | 9Router Connectivity Lab | Phase 0 | PLANNED | P0-L06 |
| P0-05 | Testing, Failure Handling & CI | Phase 0 | PLANNED | P0-L07–L08 |
| P0-06 | Foundation Integration & Review | Phase 0 | PLANNED | Phase 0 completion gates |

## Backlog kiểm thử kiến trúc
- ARCH-001: kiểm thử quyền cập nhật state và stale state version (Phase 3).
- ARCH-002: ngân sách chung khi SDK/proxy/Gateway cùng retry (Phase 2–3).
- ARCH-003: recovery khi gián đoạn API call / DB commit / checkpoint (Phase 3, 7).

Chi tiết tại [AUDIT_LOG](AUDIT_LOG.md). Requirement traceability 259 ID đang là [bản sơ bộ](TRACEABILITY_MATRIX.md); không đánh dấu coverage PASS trước bằng chứng test.
