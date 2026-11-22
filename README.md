# MathAgents_MATHK

MATHK là dự án nghiên cứu hệ thống đa tác tử hỗ trợ suy luận toán học. Repository hiện có tài liệu thiết kế và Python Foundation với cấu hình được validate.

## Quick Start

Yêu cầu: [uv](https://docs.astral.sh/uv/getting-started/installation/) và Python 3.12. `uv` có thể tải Python 3.12 khi máy chưa có phiên bản phù hợp.

Tại thư mục gốc repository:

```sh
uv sync --locked
uv run python -c "import mathk"
uv run python -m mathk
```

Lệnh cuối in `MATHK Foundation is working.`. `uv sync --locked` cài package và các dependency được khóa vào môi trường `.venv` của dự án. Xem [P0-L01](labs/phase_00/01_python_runtime/README.md) để tìm hiểu runtime, src-layout và lockfile; xem [P0-L02](labs/phase_00/02_modular_architecture/README.md) để thực hành module và dependency.

## Cấu hình

`mathk.config.load_config("configs/default.yaml")` đọc cấu hình YAML và trả về `AppConfig` đã validate. Các giá trị trong file là ví dụ cho Foundation, không phải budget vận hành đã được chốt. Các trường bắt buộc gồm `model`, `timeout_seconds`, `max_llm_calls`, `allow_fallback`.

Thứ tự ưu tiên tăng dần: YAML → environment → `overrides` truyền trực tiếp cho `load_config`. Các biến tương ứng là `MATHK_MODEL`, `MATHK_TIMEOUT_SECONDS`, `MATHK_MAX_LLM_CALLS`, `MATHK_ALLOW_FALLBACK`; environment chỉ nhận các tên này. Timeout và số lần gọi phải dương; YAML và explicit overrides dùng đúng kiểu, environment được chuyển từ chuỗi rồi validate. Khóa không biết và giá trị không hợp lệ bị từ chối. Profiles chưa được triển khai.

`.env.example` chỉ liệt kê biến mẫu; loader không tự đọc `.env`. Không đặt secret trong YAML hoặc explicit overrides: loader này không đọc credentials. Xem [P0-L03](labs/phase_00/03_data_contracts/README.md) và [P0-L04](labs/phase_00/04_configuration/README.md) để thực hành. Chạy `uv run pytest` để kiểm tra contract.

Lab [P0-L05](labs/phase_00/05_llm_api_anatomy/README.md) minh họa request, response, usage và latency bằng mock offline, không cần API key.

## Giới hạn hiện tại

CLI chỉ xác nhận Foundation hoạt động và chưa sử dụng config. Chưa triển khai model gateway, agent, RAG, công cụ toán, API hay CI; không cần API key để chạy các lệnh trên.
