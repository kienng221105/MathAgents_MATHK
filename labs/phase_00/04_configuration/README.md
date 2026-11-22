# P0-L04 — Configuration-driven System

## Nguyên lý

`load_config` đọc YAML rồi áp dụng biến môi trường được hỗ trợ và explicit overrides, sau đó validate một lần. Giá trị ưu tiên cao hơn không được bỏ qua validation. Loader chỉ xử lý các trường cấu hình không bí mật; nó không tự đọc `.env`, không đọc API key và không in giá trị đầu vào khi báo lỗi.

## Thực hành

Trong PowerShell tại gốc repository, chạy lần lượt:

```powershell
uv run python -c "from mathk.config import load_config; print(load_config('configs/default.yaml'))"
$env:MATHK_TIMEOUT_SECONDS = '12'
uv run python -c "from mathk.config import load_config; print(load_config('configs/default.yaml').timeout_seconds)"
$env:MATHK_TIMEOUT_SECONDS = '-1'
uv run python -c "from mathk.config import load_config; print(load_config('configs/default.yaml'))"
Remove-Item Env:MATHK_TIMEOUT_SECONDS
```

Quan sát timeout mặc định, giá trị override và lỗi khi giá trị âm. Thử tương tự với `MATHK_MODEL`, `MATHK_MAX_LLM_CALLS`, `MATHK_ALLOW_FALLBACK`. Xem `.env.example` để biết tên biến; file đó là tài liệu mẫu, không được loader tự nạp. Không đưa key thật vào YAML, code hoặc lệnh in ra màn hình.

## Câu hỏi tự trả lời

1. Nếu YAML đặt timeout 30, environment đặt 12 và explicit override đặt 2, kết quả là bao nhiêu?
2. Vì sao `-1` bị từ chối dù đến từ nguồn ưu tiên cao hơn?
3. Vì sao `.env` không được commit và loader không nên dump toàn bộ environment?
