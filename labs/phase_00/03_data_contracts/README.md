# P0-L03 — Data Contracts & Pydantic

## Nguyên lý

Type hint giúp công cụ kiểm tra tĩnh, nhưng không tự kiểm tra dữ liệu khi chương trình chạy. `AppConfig` dùng Pydantic để kiểm tra dữ liệu ở ranh giới: model không rỗng, timeout và số lần gọi dương, fallback là boolean. Các con số trong YAML là ví dụ học tập, chưa phải budget vận hành đã duyệt.

## Thực hành

Từ gốc repository, chạy ví dụ hợp lệ rồi thay từng giá trị để dự đoán kết quả:

```powershell
uv run python -c "from mathk.config import AppConfig; print(AppConfig(model='demo', timeout_seconds=5, max_llm_calls=2, allow_fallback=False))"
```

Thử `max_llm_calls=0`, `max_llm_calls='2'`, hoặc bỏ `timeout_seconds`. Mỗi trường hợp phải bị từ chối; chú ý sự khác nhau giữa sai kiểu, ngoài giới hạn và thiếu trường. Có thể chạy `uv run pytest tests/test_config.py` để xem thêm các trường hợp.

## Câu hỏi tự trả lời

1. Type hint và validation runtime khác nhau thế nào?
2. Vì sao chuỗi `'2'` không giống số nguyên `2` trong contract này?
3. Một cấu hình đúng schema có chứng minh budget đó phù hợp vận hành không?
