# MATHK — Project Structure

**Phiên bản:** 0.2

**Trạng thái:** Đang thảo luận

Tham chiếu: [Requirements](01_REQUIREMENTS.md), [System Design v0.16.1](03_SYSTEM_DESIGN.md).

## 1. Nguyên tắc tổ chức mã nguồn

**Trạng thái: Đã chốt.**

- Một repository, Modular Monolith, Python src-layout (`src/mathk/`).
- Tổ chức theo module chức năng, mở rộng dần theo Phase; không tạo hàng loạt abstraction hoặc thư mục rỗng từ đầu.
- Mini Lab độc lập trong `labs/`; AI Core không phụ thuộc vào labs.
- Tích hợp kiểm thử ngay từ đầu.
- Learning by Building: nguyên lý trước framework, mini lab, tự triển khai, kiểm thử, giải thích, commit. Ma trận năng lực chi tiết sẽ thuộc 05_IMPLEMENTATION.md.

```mermaid
flowchart LR
 A["Learn"] --> B["Mini Lab"]
 B --> C["Implement in src/mathk"]
 C --> D["Test"]
 D --> E["Explain and Commit"]
```

## 2. Repository Structure

**Trạng thái: Đã chốt.**

### 2.1. Phase 0
```text
MathAgents_MATHK/
├── .github/workflows/ci.yml
├── configs/default.yaml
├── docs/
├── labs/phase_00/
├── src/mathk/
│   ├── __init__.py
│   ├── __main__.py
│   └── config.py
├── tests/
│   ├── __init__.py
│   └── test_config.py
├── .env.example
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```
Chỉ tạo khi triển khai; chưa cần LangGraph, SymPy, FAISS hay agents.

### 2.2. Python src-layout
Tách package khỏi repository root, hỗ trợ packaging/import/testing nhất quán. AI Core dùng chung cho CLI, Gradio, Benchmark Runner. Public API dự kiến MathEngine.

### 2.3. Foundation
__init__.py: package/public API; __main__.py: entry point; config.py: configuration; pyproject.toml: packaging/dependencies; uv.lock: lock; .python-version: Python version; .env.example: mẫu env; ci.yml: CI; test_config.py: unit test. Dùng uv.

### 2.4. Incremental structure
| Phase | Thư mục giới thiệu hoặc mở rộng |
|---|---|
| 0 Foundation | configs, docs, labs/phase_00, src/mathk, tests, .github |
| 1 Tools | tools, domain, labs/phase_01, tests/unit |
| 2 Single-Agent | agents, application, infrastructure, evaluation, labs/phase_02 |
| 3 Multi-Agent | orchestration, infrastructure/persistence, tests/integration, labs/phase_03 |
| 4 RAG | knowledge, data/knowledge, data/runtime/indexes, labs/phase_04 |
| 5 Verification | verification, uncertainty, labs/phase_05 |
| 6 Multimodal | multimodal, interfaces, data/runtime/assets, labs/phase_06 |
| 7 Research | experiments, data/datasets, data/experiments, tests/system, labs/phase_07 |
Các package chức năng nằm trong src/mathk.

### 2.5. Mini Labs
Theo phase và năng lực. Ví dụ labs/phase_03/README.md và 01_agent_loop, 02_shared_state, 03_orchestration, 04_langgraph, 05_routing, 06_guardrails, 07_checkpointing. Mỗi lab có lý thuyết, yêu cầu thực hành, test, câu hỏi kiểm tra; người học tự thử trước khi xem lời giải. Chi tiết Competency Matrix ở 05_IMPLEMENTATION.md.


## 3. Package & Module Structure

*Chưa chốt.*

## 4. Dependency Rules

*Chưa chốt.*

## 5. Configuration & Data Organization

*Chưa chốt.*

## 6. Testing & Mini Lab Structure

*Chưa chốt.*

## 7. Naming & Coding Conventions

*Chưa chốt.*

## 8. Cấu trúc mở rộng theo Phase

*Chưa chốt.*
