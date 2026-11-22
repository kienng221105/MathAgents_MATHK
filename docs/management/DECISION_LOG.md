# Decision Log — MATHK

**Quy tắc:** Chỉ ghi quyết định Owner đã phê duyệt. Không coi giả thuyết hoặc đề xuất là quyết định.

| ID | Quyết định | Trạng thái | Căn cứ |
|---|---|---|---|
| DEC-001 | Modular Monolith Python 3.12, LangGraph, 5 Agent; Gateway/Guard/Repository và controlled shared state | APPROVED | [System Design v1.0](../03_SYSTEM_DESIGN.md) |
| DEC-002 | Máy mục tiêu 8 GB RAM, Full API Inference; orchestration/math tools/storage local | APPROVED | [Deployment](../07_DEPLOYMENT.md) |
| DEC-003 | Phát triển Phase 0–7; MVP C hoàn thiện P0 chức năng engine, MVP D hoàn thiện P0 benchmark/nghiên cứu | APPROVED | [Implementation](../05_IMPLEMENTATION.md), [System Design](../03_SYSTEM_DESIGN.md) |
| DEC-004 | Ground Truth chỉ Evaluator tiếp nhận; Engine/Agent/Verifier không nhận đáp án benchmark | APPROVED | [System Design](../03_SYSTEM_DESIGN.md) |
| DEC-005 | Owner–ChatGPT–Codex phối hợp theo Documentation; GitHub main là nguồn chuẩn; checkpoint sau task | APPROVED | [Documentation](../08_DOCUMENTATION.md) |
| DEC-006 | 02_RESEARCH.md tạm hoãn; không tự ý hoàn thiện hoặc dùng làm baseline đã duyệt | APPROVED | Quyết định Owner trong giai đoạn audit |
| DEC-007 | System Design v1.0 được phê duyệt sau PRE-001; khởi tạo bộ quản lý trước Phase 0 | APPROVED | [AUDIT_LOG](AUDIT_LOG.md), Owner phê duyệt |

## Chưa chốt
- Chi tiết Task và Acceptance Criteria Phase 0.
- Mapping test/evidence cho từng ID của Traceability Matrix; hiện chỉ ánh xạ cấp nhóm.
- Hiệu quả nghiên cứu và novelty phải đánh giá thực nghiệm, không suy ra từ thiết kế.
