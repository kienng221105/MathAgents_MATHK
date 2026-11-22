# P0-L01 — Python Project & Runtime

## Nguyên lý

Repository chứa cả tài liệu, lab và mã nguồn; Python package `mathk` là phần có thể cài và import từ `src/mathk`. Src-layout giúp tránh vô tình import package trực tiếp từ thư mục gốc khi chưa cài, nên việc kiểm tra gần với cách người khác dùng package hơn.

`.python-version` chọn Python 3.12 cho `uv`; `requires-python` trong `pyproject.toml` khai báo phiên bản package hỗ trợ. `pyproject.toml` khai báo metadata, build backend và các dependency được phép. `uv.lock` ghi kết quả phân giải dependency của dự án để `uv sync --locked` tái sử dụng; `.venv` là môi trường cục bộ được tạo từ cấu hình đó, không đưa vào Git. Build backend được khai báo riêng trong `[build-system]` và không được khóa trong `uv.lock` này. Lockfile giúp tái lập môi trường nhưng không tự bảo đảm hành vi giống nhau trên mọi hệ điều hành.

## Thực hành

Tại gốc repository, dự đoán kết quả rồi chạy:

```sh
uv sync --locked
uv run python -c "import sys, mathk; print(sys.version); print(sys.executable); print(mathk.__file__)"
uv run python -m mathk
```

Quan sát Python 3.12, interpreter trong `.venv`, đường dẫn module và thông điệp Foundation. Đối chiếu với `python --version` bên ngoài `uv`: phiên bản đó có thể khác vì phụ thuộc môi trường máy. Xem `[project].dependencies` trong `pyproject.toml` và các package được khóa trong `uv.lock`.

## Câu hỏi tự trả lời

1. Repository và package `mathk` khác nhau thế nào? Vì sao đặt package dưới `src/`?
2. Khi đổi ràng buộc dependency trong `pyproject.toml`, vì sao cần cập nhật lockfile trước khi dùng `uv sync --locked`?
3. `python -m mathk` tìm và chạy file nào? Vì sao `.venv` không nên được đưa vào Git?
