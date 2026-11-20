# 03 — SYSTEM DESIGN

**Dự án:** MATHK  
**Phiên bản:** 0.1  
**Trạng thái:** Đang thảo luận  
**Requirements Baseline:** v1.0 (558b25e2d1789f0ae526a4d1211be2febd0eadd6)

## 1. Architecture Drivers — Cơ sở thiết kế

### 1.1. Mục tiêu kiến trúc

MATHK là AI Mathematical Reasoning Engine, không phải chatbot giải toán đơn thuần. Engine hoạt động độc lập với giao diện, hỗ trợ sử dụng từ Python và tích hợp ứng dụng trong tương lai. Kiến trúc cần đủ linh hoạt để điều chỉnh theo kết quả nghiên cứu sau này.

### 1.2. Functional Drivers

| ID | Architecture Driver | Nguồn |
|---|---|---|
| FD01 | Tiếp nhận và chuẩn hóa đầu vào | FR01 |
| FD02 | Biểu diễn dữ kiện đa phương thức | FR02 |
| FD03 | Phân tích và lập kế hoạch | FR03 |
| FD04 | Truy xuất tri thức thích ứng | FR04 |
| FD05 | Suy luận kết hợp công cụ toán học | FR05 |
| FD06 | Kiểm chứng và tự sửa lỗi | FR06 |
| FD07 | Điều phối Agent động | FR07 |
| FD08 | Phát hiện và xử lý bất định | FR08 |
| FD09 | Đầu ra có cấu trúc | FR09 |
| FD10 | Thực nghiệm và đánh giá | FR10 |

Các driver không nhất thiết tương ứng với Agent hoặc service riêng; ưu tiên module thông thường khi phù hợp.

### 1.3. Quality Attribute Drivers

| Nhóm | Thuộc tính |
|---|---|
| A — Chi phối kiến trúc cốt lõi | NFR01 Mathematical Correctness, NFR02 Reliability, NFR03 Performance, NFR04 Cost Efficiency, NFR05 Modifiability, NFR06 Extensibility |
| B — Xuyên suốt | NFR07 Reproducibility, NFR08 Observability, NFR09 Security & Privacy |
| C — Hỗ trợ sử dụng và mở rộng | NFR10 Usability, NFR11 Portability, NFR12 Scalability |

Không thay đổi mức ưu tiên P0/P1 trong Requirements.

### 1.4. Architecture Principles

| ID | Nguyên tắc | Ý nghĩa |
|---|---|---|
| AP01 | Local-first | Ưu tiên chạy trên máy cá nhân. |
| AP02 | Modularity | Module có trách nhiệm rõ ràng. |
| AP03 | Separation of Concerns | Tách suy luận, giao diện, dữ liệu và thực nghiệm. |
| AP04 | Loose Coupling | Hạn chế phụ thuộc trực tiếp. |
| AP05 | Interface-first | Giao tiếp qua interface và schema rõ ràng. |
| AP06 | Deterministic-first | Ưu tiên thuật toán xác định; dùng LLM khi cần. |
| AP07 | State-driven Execution | Điều phối theo trạng thái thực thi có cấu trúc. |
| AP08 | Model Independence | Không phụ thuộc cứng vào một LLM Provider. |
| AP09 | Tool Extensibility | Bổ sung công cụ mà không sửa toàn bộ Agent. |
| AP10 | Bounded Execution | Giới hạn vòng lặp, timeout và tài nguyên. |
| AP11 | Verification-aware | Kết quả kiểm chứng có thể ảnh hưởng điều phối. |
| AP12 | Configuration-driven | Tách prompt, tham số, mô hình và chiến lược khỏi logic nghiệp vụ. |
| AP13 | Research-first Observability | Ghi nhận thông tin thực nghiệm từ đầu. |
| AP14 | Secure by Design | Kiểm soát dữ liệu, API key và quyền thực thi công cụ. |
| AP15 | Incremental Development | Phát triển theo MVP-A đến MVP-D. |
| AP16 | Shared Database by Default | Mặc định dùng database chung; phân chia quyền sở hữu dữ liệu theo trách nhiệm module; truy cập qua Storage/Repository Layer; cho phép lưu trữ riêng hoặc chuyên biệt khi có nhu cầu. |

Deterministic-first: dùng Python cho validation, giới hạn tài nguyên, tính chi phí và metrics; SymPy cho tính toán ký hiệu phù hợp; LLM/VLM cho hiểu đề, lập kế hoạch, suy luận ngữ nghĩa kết hợp quy tắc. Không biến mọi module thành Agent.

State-driven Execution: Agent đọc phần dữ liệu cần thiết từ Shared State, trả về cập nhật có cấu trúc; Orchestrator áp dụng cập nhật hợp lệ và quyết định bước tiếp theo.

Configuration-driven: sử dụng cùng Engine với cấu hình mô hình, Routing, Verification, Tools và Retrieval có thể thay đổi để thực nghiệm. Schema cấu hình chưa chốt.

Shared Database: Shared State là trạng thái logic của phiên suy luận, không đồng nghĩa với database. Có thể phân nhóm dữ liệu Sessions, Problems, Planning, Reasoning, Verification, Knowledge, Execution và Evaluation. Agent không truy cập tùy ý trực tiếp vào database. Có thể sử dụng Vector Store chuyên biệt phục vụ RAG hoặc database riêng khi có nhu cầu; chưa chốt schema và công nghệ lưu trữ.

### 1.5. Kiến trúc không ưu tiên trong MVP

Không yêu cầu Microservices phân tán, Kubernetes, Message Broker, GPU Server chuyên dụng, Agent cho mọi tác vụ, frontend phức tạp hoặc huấn luyện LLM từ đầu. Không bắt buộc database riêng cho từng Agent; áp dụng AP16. Đây không phải lệnh cấm mở rộng về sau.

### 1.6. Thứ tự ưu tiên khi đánh đổi thiết kế

1. Mathematical Correctness & Reliability.
2. Research Reproducibility.
3. Performance & Cost Efficiency.
4. Modifiability & Extensibility.
5. Usability & Portability.
6. Large-scale Scalability.

Thứ tự trên không phải trọng số định lượng. Security & Privacy là ràng buộc bắt buộc xuyên suốt, không đánh đổi để giảm chi phí hay tăng hiệu năng.

## 2. Architecture Style

*Chưa chốt.*

## 3. High-Level Architecture

*Chưa chốt.*

## 4. Technology Stack

*Chưa chốt.*

## 5. Agent Design

*Chưa chốt.*

## 6. State Management

*Chưa chốt.*

## 7. Adaptive Routing

*Chưa chốt.*

## 8. Multimodal Processing

*Chưa chốt.*

## 9. Knowledge Base & Agentic RAG

*Chưa chốt.*

## 10. Neuro-Symbolic Tool System

*Chưa chốt.*

## 11. Verification & Self-correction

*Chưa chốt.*

## 12. Uncertainty Handling

*Chưa chốt.*

## 13. Data & Storage Design

*Chưa chốt.*

## 14. Interface & API Design

*Chưa chốt.*

## 15. Evaluation & Observability

*Chưa chốt.*

## 16. Security, Reliability & Resource Management

*Chưa chốt.*
