# Phase 0 — Foundation: Planning Baseline

**Trạng thái:** APPROVED bởi Owner (2026-11-22); triển khai theo từng task, không tự mở rộng.
**Nguồn:** [Implementation §4](../05_IMPLEMENTATION.md), [Project Structure §2.1](../04_PROJECT_STRUCTURE.md), [System Design v1.0](../03_SYSTEM_DESIGN.md).
**Mục tiêu:** Python 3.12, uv, src-layout, config/contracts, lab API và 9Router, testing/CI, Foundation chạy được. 8 mini labs P0-L01–L08, ước tính 8–12 giờ; thời gian không phải cam kết.
**Learning:** SYS01, SYS03, MOD03, EVA05 mục tiêu L2, chỉ đánh dấu khi Owner thể hiện được bằng evidence.

| Task | Scope | Labs | Acceptance Criteria | Trạng thái |
|---|---|---|---|---|
| P0-01 | Python Foundation & Project Skeleton: Python 3.12, uv, src-layout, packaging, CLI tối thiểu, README hướng dẫn chạy | P0-L01–L02 | Import package; `uv sync --locked`; `uv run python -m mathk`; không thêm framework ngoài Phase 0 | COMPLETED — Engineering + Learning L2 cơ bản + Checkpoint |
| P0-02 | Data Contracts & Configuration: Pydantic, YAML/env, config validation và secrets | P0-L03–L04 | Valid config chạy; invalid/missing bị từ chối; không lộ key | COMPLETED — Engineering + Learning L2 cơ bản + Checkpoint |
| P0-03 | LLM API Anatomy lab: request/response/model ID/usage/latency | P0-L05 | Demo/mock, missing usage được ghi nhận; không giả API metrics | PLANNED |
| P0-04 | 9Router Connectivity lab, quan sát quota/errors, không production Gateway | P0-L06 | Cấu hình provider độc lập; auth/quota failure rõ; API thật chỉ khi Owner cho phép | PLANNED |
| P0-05 | Testing, Failure Handling & CI: fake model, timeout, pytest, Ruff, mypy, Actions | P0-L07–L08 | Tests/lint/type/CI chạy; lỗi có evidence | PLANNED |
| P0-06 | Foundation Integration & Review | Tổng kết | Reproduce từ môi trường sạch, docs/test/CI/checkpoint, Engineering + Learning + Checkpoint Gates | PLANNED |

## P0-01 Task Contract
**Mục tiêu:** Skeleton tối thiểu có thể chạy, package import đúng, không thêm business logic hoặc công cụ phase sau.

**Scope:** `pyproject.toml`, `uv.lock`, `.python-version`, `src/mathk/__init__.py`, `src/mathk/__main__.py`, `README.md` phần Quick Start, `.gitignore` khi cần, lab P0-L01/L02 ở mức tài liệu/mini demo nhỏ. Không bắt buộc tạo config.py, YAML, CI, test_config.py, .env.example ở task này vì thuộc P0-02/P0-05; toàn bộ deliverables của Phase 0 phải có trước P0-06.

**AC:**
- AC01: Python 3.12 và uv được sử dụng; package installable theo src-layout, lockfile được tạo và commit.
- AC02: `uv sync --locked` thành công từ lockfile; `uv run python -c "import mathk"` thành công.
- AC03: `uv run python -m mathk` chạy, in thông điệp CLI foundation rõ ràng, không gọi API.
- AC04: Không có import phụ thuộc vào LangGraph, SymPy, FAISS, Agent/RAG hoặc SDK model.
- AC05: README nêu cách cài/khởi chạy/kiểm tra và giới hạn task.
- AC06: Lab P0-L01/L02 có giải thích ngắn, ví dụ/quan sát và câu hỏi để Owner tự trả lời; không tự đánh dấu Learning Gate.
- AC07: Báo cáo file thay đổi, lệnh/test output, Git status, lỗi/hạn chế; không commit/push trừ khi Owner cho phép riêng.

**Ràng buộc:** Kiểm tra trạng thái Git trước khi làm; giữ nguyên tài liệu baseline, không ghi đè thay đổi khác; không dùng API trả phí, không lưu secrets, không tạo hàng loạt file rỗng. Nếu Python/uv thiếu hoặc xung đột môi trường, báo rõ; không tự thay đổi máy vượt scope. Codex chỉ làm P0-01 và chờ review.

## Gates
Engineering Gate: functionality/tests/CI tương ứng scope; Learning Gate: Owner giải thích nguyên lý và evidence; Checkpoint Gate: GitHub docs/task/evidence và commit đã kiểm chứng. P0-01 có thể ACCEPTED kỹ thuật trước khi COMPLETED theo cả ba gate.
