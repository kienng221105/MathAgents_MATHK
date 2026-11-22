# P0-L02 — Modular Architecture

## Nguyên lý

Trong một file nhỏ, xử lý và định dạng có thể nằm cùng nhau:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("MATHK"))
```

Khi trách nhiệm tăng, có thể tách định dạng sang module riêng. Trong ví dụ này, `demo.py` dùng hàm từ `formatter.py`; module định dạng không phụ thuộc vào chương trình gọi. Hàm `show` nhận formatter từ bên ngoài nên có thể thay cách trình bày mà không sửa `show`. Đây là ví dụ học tập độc lập, không phải kiến trúc production.

## Thực hành

Tại gốc repository:

```sh
uv run python labs/phase_00/02_modular_architecture/demo.py
```

Dự đoán và quan sát hai dòng kết quả. Xem hướng import trong `demo.py`, rồi thử truyền formatter khác vào `show` và so sánh kết quả. Không cần thay package `mathk` để chạy lab.

## Câu hỏi tự trả lời

1. Trong ví dụ một file và ví dụ hai module, trách nhiệm định dạng nằm ở đâu? Khi nào tách module có ích?
2. Nếu `formatter.py` import ngược `demo.py`, rủi ro circular import là gì?
3. Vì sao domain không nên import UI, và vì sao core không nên phụ thuộc vào lab?
4. Có thể thay implementation định dạng mà không sửa `show` bằng cách nào?
