# MathAgents_MATHK

MATHK là dự án nghiên cứu hệ thống đa tác tử hỗ trợ suy luận toán học. Repository hiện có tài liệu thiết kế và Python Foundation tối thiểu của P0-01.

## Quick Start

Yêu cầu: [uv](https://docs.astral.sh/uv/getting-started/installation/) và Python 3.12. `uv` có thể tải Python 3.12 khi máy chưa có phiên bản phù hợp.

Tại thư mục gốc repository:

```sh
uv sync --locked
uv run python -c "import mathk"
uv run python -m mathk
```

Lệnh cuối in `MATHK Foundation is working.`. `uv sync --locked` cài package và các dependency được khóa vào môi trường `.venv` của dự án. Xem [P0-L01](labs/phase_00/01_python_runtime/README.md) để tìm hiểu runtime, src-layout và lockfile; xem [P0-L02](labs/phase_00/02_modular_architecture/README.md) để thực hành module và dependency.

## Giới hạn hiện tại

CLI chỉ xác nhận Foundation hoạt động. P0-01 chưa triển khai cấu hình chính thức, model gateway, agent, RAG, công cụ toán, API hay CI; không cần API key để chạy các lệnh trên.
