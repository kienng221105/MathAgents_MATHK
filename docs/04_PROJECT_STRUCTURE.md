# MATHK — Project Structure

**Phiên bản:** 0.1

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

*Chưa chốt.*

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
