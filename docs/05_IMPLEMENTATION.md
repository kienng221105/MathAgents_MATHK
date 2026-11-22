# MATHK — Implementation Roadmap

**Phiên bản:** 0.1

**Trạng thái:** Đang thảo luận

Tham chiếu: [Requirements](01_REQUIREMENTS.md), [System Design](03_SYSTEM_DESIGN.md), [Project Structure v1.0](04_PROJECT_STRUCTURE.md).

## 1. Phương pháp học và triển khai

**Trạng thái: Đã chốt.**

### 1.1. Learning by Building và Scaffolding
Theory → Mini Lab → Framework (khi cần) → Integration → Mastery. Tăng dần độ phức tạp; kiểm tra nhanh kiến thức đã biết, không ép đủ mọi tầng.
```mermaid
flowchart LR
 T["Theory"] --> L["Mini Lab"]
 L --> F["Framework"]
 F --> I["Integration"]
 I --> M["Mastery"]
```

### 1.2. Ví dụ Orchestration
1. Python functions tuần tự, không LLM/framework.
2. Shared State bằng dictionary có cấu trúc.
3. Conditional routing bằng if/else.
4. Generate/Verify correction loop với budget và termination.
5. Chuyển sang LangGraph nodes, edges, conditional edges, state.
6. Thay fake functions bằng agent qua Model Gateway.
7. Tích hợp Orchestrator, Router, State, Guard vào MATHK.
```mermaid
flowchart TD
 G["Generate"] --> V["Verify"]
 V --> C{"Correct?"}
 C -->|Yes| F["Finish"]
 C -->|No| B{"Budget remains?"}
 B -->|Yes| G
 B -->|No| S["Stop"]
```

### 1.3. Chuỗi học theo năng lực
- Tool Calling: function → schema → registry → LLM chọn tool → guard → MATHK.
- Agent: API → structured output → tool calling → agent loop → single-agent.
- RAG: text search → BM25 → dense → hybrid → applicability → agentic retrieval.
- Guardrails: validation → permission → budget → tool safety → workflow guard.
- Routing: if/else → rule-based → state-aware → verification-guided → hybrid.
- Multimodal: đọc ảnh → VLM → facts → structured representation → fusion → agent.
- Checkpoint: JSON state → restore → SQLite → LangGraph checkpointer → resume.
Các guard bắt buộc phải có trước khi cho phép thực thi thật.

### 1.4. Mini Lab
Basic: một khái niệm ít dependency; Intermediate: kết hợp, framework; Advanced: lỗi, edge cases, integration. Chỉ tăng mức khi hiểu nền tảng; có thể bỏ qua phần đã thành thạo sau kiểm tra.

### 1.5. Phiên học
Linh hoạt 45/90/120 phút; gợi ý 10% ôn, 20% lý thuyết/ví dụ, 40% tự lab, 20% review/integration, 10% tổng kết/checkpoint. Lab khó có thể nhiều buổi.

### 1.6. Mentor
H1 câu hỏi gợi mở; H2 thuật toán/hướng giải; H3 pseudocode/skeleton; H4 lời giải đầy đủ kèm giải thích. Mặc định H1–H2 khi gặp khó; AI hỗ trợ trực tiếp boilerplate/CI/Git không phải năng lực trọng tâm.

### 1.7. Ôn tập
Concept, Implementation, Debugging, Design; ôn kiến thức liên quan đầu phase. Engineering Gate và Learning Gate theo tài liệu 04.

### 1.8. Tiến độ
docs/progress/ lưu năng lực, phase, mức L0–L4, minh chứng lab/test/integration/commit, phần chưa xong và bước tiếp theo. Checkpoint thường xuyên, GitHub là nguồn chuẩn.

## 2. Kiến thức tiên quyết

*Chưa chốt.*

## 3. AI Agent Competency Matrix

*Chưa chốt.*

## 4. Phase 0 — Foundation

*Chưa chốt.*

## 5. Phase 1 — Mathematical Tool System

*Chưa chốt.*

## 6. Phase 2 — Single-Agent Solver

*Chưa chốt.*

## 7. Phase 3 — Multi-Agent Orchestration

*Chưa chốt.*

## 8. Phase 4 — Agentic RAG

*Chưa chốt.*

## 9. Phase 5 — Verification & Adaptive Routing

*Chưa chốt.*

## 10. Phase 6 — Multimodal Reasoning

*Chưa chốt.*

## 11. Phase 7 — Research & Evaluation

*Chưa chốt.*

## 12. Quản lý tiến độ và đánh giá năng lực

*Chưa chốt.*
