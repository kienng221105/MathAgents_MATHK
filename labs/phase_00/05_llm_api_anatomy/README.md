# P0-L05 — LLM API Anatomy

## Mục tiêu

Quan sát request → mock client → response → metrics mà không cần mạng, API key hoặc trả phí. Lab minh họa cấu trúc dữ liệu, không mô phỏng hành vi hay chất lượng của một model thật và không triển khai Model Gateway.

- **Request:** model ID được yêu cầu, messages (role/content), temperature và giới hạn output. Đây là dữ liệu ví dụ.
- **Response:** model ID mock được trả về, content và finish reason do mock cố định. Model được yêu cầu và model được báo về là hai trường riêng.
- **Usage:** input/output/total tokens chỉ có khi response cung cấp. `None` nghĩa là không có thông tin, không phải 0. Các số trong trường hợp thứ hai là **fixture giả lập**, không phải token thực tế hoặc ước lượng.
- **Latency:** `time.perf_counter()` đo thời gian trôi qua quanh lời gọi mock cục bộ, đổi sang milliseconds. Giá trị này có thể thay đổi giữa các lần chạy; không phải latency mạng, provider hay model thật.

## Thực hành

Tại gốc repository, sau `uv sync --locked`:

```powershell
uv run python labs/phase_00/05_llm_api_anatomy/demo.py
uv run pytest labs/phase_00/05_llm_api_anatomy/test_demo.py
```

Đọc request và hai response: response đầu thiếu usage, response sau chứa usage giả lập. Thay một tham số request và dự đoán output mock: response vẫn cố định. Thử một request sai, ví dụ `max_output_tokens=0`, và quan sát Pydantic từ chối. Không nhập thông tin cá nhân hoặc secret vào ví dụ.

## Câu hỏi Learning Gate

1. Model ID trong request và trong response có vai trò gì? Vì sao cần ghi nhận cả hai?
2. Vì sao không được thay `usage=None` bằng 0 hoặc tự suy ra token từ độ dài văn bản?
3. Giá trị latency của lab đo khoảng nào, và điều gì cần thay đổi để đo một API thật?
4. `finish_reason` và response content giúp người gọi hiểu điều gì? Validation có bảo đảm nội dung toán học đúng không?
