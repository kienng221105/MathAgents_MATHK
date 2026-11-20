# 03 — SYSTEM DESIGN

**Dự án:** MATHK  
**Phiên bản:** 0.4  
**Trạng thái:** Đang thảo luận  
**Requirements Baseline:** v1.0 (558b25e2d1789f0ae526a4d1211be2febd0eadd6); tài liệu trực quan v1.1 (29cf094b81ae8f81bb69ba6c05e6cd0987183140)

## 1. Architecture Drivers — Cơ sở thiết kế

### 1.1. Mục tiêu kiến trúc

MATHK là AI Mathematical Reasoning Engine, không phải chatbot giải toán đơn thuần. Engine hoạt động độc lập với giao diện, hỗ trợ sử dụng từ Python và tích hợp ứng dụng trong tương lai. Kiến trúc cần đủ linh hoạt để điều chỉnh theo kết quả nghiên cứu sau này.


```mermaid
flowchart TD
 UI["Demo UI"] --> E["MATHK Reasoning Engine"]
 APP["Python application"] --> E
 E --> K["Knowledge Base"]
 B["Evaluation System"] --> E
 E --> O["Structured Output"]
```

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


```mermaid
flowchart TD
 A["Agents"] -->|Structured updates| O["Orchestrator"]
 O -->|Validated updates| S["Shared State"]
 S -->|Relevant context| A
 S --> R["Storage / Repository"]
 R --> D[("Shared Database")]
 R -.->|Optional| V[("Specialized store")]
```


```mermaid
flowchart LR
 A["Static config"] --> E["Same MATHK Engine"]
 B["Rule-based config"] --> E
 C["Hybrid config"] --> E
 E --> R["Comparable results and traces"]
```

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

## 2. Architecture Style — Phong cách kiến trúc

### 2.1. Phân loại kiến trúc

Phân biệt Deployment Architecture (đóng gói và triển khai), Internal Architecture (tổ chức mã nguồn và phụ thuộc), Execution Architecture (phối hợp thực thi Agent) và Data Architecture (tổ chức và chia sẻ dữ liệu). Các lựa chọn thuộc những khía cạnh khác nhau có thể kết hợp.

### 2.2. Deployment Architecture

| Tiêu chí | Traditional Monolith | Modular Monolith | Microservices |
|---|---|---|---|
| Triển khai local | Đơn giản | Đơn giản | Phức tạp hơn |
| Modularity | Tùy thiết kế | Cao | Cao |
| Kiểm thử độc lập | Tùy thiết kế | Tốt | Tốt |
| Giao tiếp nội bộ | Function | Interface/Function | Network |
| Shared State | Dễ | Dễ | Phức tạp hơn |
| Chi phí hạ tầng | Thấp | Thấp | Tùy triển khai |
| Mở rộng độc lập khi chạy | Hạn chế | Hạn chế | Tốt |
| Phù hợp MVP | Khá | Rất tốt | Thấp |

Chọn Modular Monolith: module có trách nhiệm và interface rõ ràng, cùng thuộc một hệ thống triển khai; ưu tiên lời gọi hàm Python thay cho HTTP nội bộ. Multi-Agent không đòi hỏi Microservices; Agent có thể cùng chạy trong một tiến trình.


```mermaid
flowchart TD
 subgraph App ["Modular Monolith"]
 O["Orchestrator"] --> A["Agents"]
 O --> T["Tools"]
 O --> K["Retrieval"]
 O --> V["Verification"]
 end
 App --> R["Repository"]
 R --> D[("Shared Database")]
```

### 2.3. Internal Architecture

Layered Architecture phân chia trách nhiệm theo tầng; Clean Architecture bảo vệ logic nghiệp vụ bằng quan hệ phụ thuộc hướng vào lõi; Hexagonal Architecture sử dụng Ports & Adapters để tách lõi khỏi hạ tầng.

Chọn Lightweight Hexagonal Architecture: áp dụng Ports & Adapters có chọn lọc, tránh trừu tượng hóa quá mức. Core gồm orchestration, Agent Logic, Domain Models và Business Rules. Demo, CLI và Benchmark sử dụng Input Port; LLM, Math Tools, Retrieval và Storage được tích hợp qua interface và adapter phù hợp. Core không phụ thuộc trực tiếp vào SDK của LLM Provider. Interface cụ thể chưa chốt.


```mermaid
flowchart TD
 I["Demo / CLI / Benchmark"] --> P["Input Port"]
 P --> C["Core: orchestration, rules, models"]
 C --> M["Model Port"]
 C --> T["Tool Port"]
 C --> K["Retrieval Port"]
 C --> S["Storage Port"]
 MA["Model Adapter"] -.->|implements| M
 TA["Math Tool Adapter"] -.->|implements| T
 KA["Retrieval Adapter"] -.->|implements| K
 SA["Storage Adapter"] -.->|implements| S
```

### 2.4. Execution Architecture

| Tiêu chí | Sequential | Supervisor | State Graph |
|---|---|---|---|
| Luồng cố định | Tốt | Có thể | Tốt |
| Điều phối thích ứng | Hạn chế | Tốt | Tốt |
| Vòng lặp sửa lỗi | Cần bổ sung | Tốt | Tốt |
| Kiểm soát chuyển tiếp | Cao | Tùy Supervisor | Cao |
| Truy vết | Dễ | Tùy thiết kế | Tốt |
| Độ phức tạp | Thấp | Trung bình | Trung bình |
| Vai trò trong MATHK | Baseline | Hỗ trợ | Kiến trúc chính |

Chọn State Graph kết hợp Hybrid Orchestration. Node là Agent hoặc tác vụ xác định; Edge là chuyển tiếp; Conditional Edge phụ thuộc điều kiện hoặc Routing; State chứa dữ liệu hiện tại; Termination Condition kiểm soát kết thúc và dừng an toàn.

Orchestrator sử dụng Shared State, quy tắc xác định và LLM khi cần; không bắt buộc Supervisor LLM riêng cho mỗi quyết định. Hỗ trợ tuyến tuần tự, rút gọn, có điều kiện và vòng sửa lỗi giới hạn. Ví dụ khái niệm: Input → Perception → Routing → Lightweight hoặc Structured → Reasoning → Verification → Output hoặc Correction và kiểm chứng lại. Đây chưa phải workflow chính thức. Framework chưa được chọn.


```mermaid
flowchart TD
 I["Input"] --> P["Perception"]
 P --> R{"Routing"}
 R -->|Lightweight| L["Reasoning"]
 R -->|Structured| S["Planning and retrieval as needed"]
 S --> L
 L --> V["Verification"]
 V -->|Correction needed and allowed| C["Correction"]
 C --> R
 V -->|Accept or safe stop| O["Output"]
```

### 2.5. Kiến trúc kết hợp

Graph-orchestrated Modular Monolith with Ports & Adapters:
- Deployment: Modular Monolith.
- Internal: Lightweight Hexagonal Architecture.
- Execution: State Graph & Hybrid Orchestration.
- Data: Shared Database by Default, quyền sở hữu dữ liệu theo module, hỗ trợ lưu trữ chuyên biệt.

Tên gọi mô tả tổ hợp kiến trúc, không tuyên bố Architecture Pattern mới.

### 2.6. Architecture Decision Records

| ID | Quyết định | Lý do chính |
|---|---|---|
| ADR001 | Modular Monolith | Phù hợp Local-first và nguồn lực cá nhân. |
| ADR002 | Lightweight Hexagonal | Giảm phụ thuộc framework và Provider. |
| ADR003 | State Graph & Hybrid Orchestration | Hỗ trợ Adaptive Routing và Verification. |
| ADR004 | Shared Database by Default | Đơn giản hóa quản lý dữ liệu và tính nhất quán. |

ADR lưu trong System Design, chưa cần file riêng.

### 2.7. Đánh đổi

| Hạn chế | Hướng xử lý |
|---|---|
| Module chia sẻ tiến trình | Kiểm soát lỗi và timeout từng tác vụ. |
| Hạn chế scale độc lập từng Agent | Duy trì interface để có thể tách module về sau. |
| State Graph có thể phức tạp | Giới hạn chuyển tiếp và chia subgraph khi cần. |
| Shared Database có nguy cơ phụ thuộc schema | Repository Layer và quyền sở hữu dữ liệu. |
| Ports & Adapters tăng lượng mã | Chỉ tạo interface tại ranh giới cần thiết. |

Kiểm soát timeout không đồng nghĩa với cô lập lỗi tiến trình hoàn toàn.

## 3. High-Level Architecture — Kiến trúc tổng thể

### 3.1. System Context


```mermaid
flowchart TD
 U["Học sinh / Giáo viên"] --> M["MATHK"]
 D["Developer"] --> M
 R["Researcher"] --> M
 M --> L["External LLM Provider"]
 M -.->|Future integration| T["External Tool Provider"]
```


SymPy, Calculator, Knowledge Base và Agents thuộc phạm vi nội bộ. External Tool Provider không bắt buộc trong MVP.

### 3.2. Kiến trúc tổng thể


```mermaid
flowchart TD
 subgraph I ["Interface Layer"]
 M01["Input Processing"]
 M02["Output Presentation"]
 M03["Application Interface"]
 end
 subgraph O ["Orchestration Layer"]
 M04["Reasoning Engine"]
 M05["Adaptive Router"]
 M06["State Manager"]
 M07["Execution Guard"]
 end
 subgraph C ["Reasoning Capability Layer"]
 M08["Perception"]
 M09["Planning"]
 M10["Retrieval"]
 M11["Reasoning"]
 M12["Verification and Correction"]
 M13["Uncertainty"]
 end
 subgraph A ["Infrastructure and Adapters"]
 M14["Model Gateway"]
 M15["Math Tool System"]
 M16["Knowledge Store"]
 M17["Persistence"]
 M18["Configuration"]
 end
 subgraph R ["Research and Observability"]
 M19["Benchmark"]
 M20["Evaluation"]
 M21["Tracing"]
 end
 M03 --> M01 --> M04
 M04 --> M02
 O --> C
 C --> A
 M19 --> M04
 M04 -.->|Events| M21
 M19 --> M20
```


Năm vùng trách nhiệm logic, không phải năm service hoặc thứ tự phụ thuộc mã nguồn bắt buộc. Core định nghĩa interface, Adapter triển khai interface. Research & Observability xuyên suốt hệ thống; mũi tên mô tả tương tác logic.

### 3.3. Danh sách module

| ID | Vùng | Module | Trách nhiệm |
|---|---|---|---|
| M01 | Interface | Input Processing | Tiếp nhận, kiểm tra, chuẩn hóa đầu vào |
| M02 | Interface | Output Presentation | Render Markdown, LaTeX, JSON |
| M03 | Interface | Application Interface | Demo UI, CLI, Python API |
| M04 | Orchestration | Reasoning Engine | Điều phối workflow và giao diện giải toán |
| M05 | Orchestration | Adaptive Router | Chọn tuyến và mức suy luận |
| M06 | Orchestration | State Manager | Quản lý Shared State và cập nhật |
| M07 | Orchestration | Execution Guard | Kiểm soát hành động, timeout, tài nguyên, dừng |
| M08 | Capability | Multimodal Perception | Hiểu đề và dữ kiện trực quan |
| M09 | Capability | Problem Analysis & Planning | Phân tích, phân loại, lập kế hoạch |
| M10 | Capability | Knowledge Retrieval | Truy xuất tri thức toán học |
| M11 | Capability | Mathematical Reasoning | Suy luận và dùng công cụ |
| M12 | Capability | Verification & Correction | Kiểm chứng, phát hiện lỗi, hỗ trợ sửa lỗi |
| M13 | Capability | Uncertainty Management | Tổng hợp tín hiệu và đề xuất xử lý bất định |
| M14 | Adapter | Model Gateway | Interface và adapter LLM/VLM |
| M15 | Adapter | Mathematical Tool System | Registry, validation, thực thi công cụ |
| M16 | Adapter | Knowledge Store | Lưu trữ, indexing, tìm kiếm |
| M17 | Adapter | Persistence | Repository, database, checkpoint |
| M18 | Adapter | Configuration | Cấu hình, prompt, tham số |
| M19 | Research | Benchmark Runner | Thực thi dataset và cấu hình thực nghiệm |
| M20 | Research | Evaluation | Tính metrics, đánh giá |
| M21 | Research | Execution Tracing | Sự kiện, tuyến xử lý, lỗi, chi phí |

21 module logic, không phải 21 service, package hoặc Agent bắt buộc. Python API không đồng nghĩa REST API hoặc SDK riêng. Verification & Correction có thể dùng Verifier và Reasoner thay vì Corrector Agent riêng.


```mermaid
flowchart TD
 R["Adaptive Router"] -->|Proposed action| G["Execution Guard"]
 G -->|Valid action| O["Orchestrator"]
 G -->|Rejected| F["Safe fallback or stop"]
 O --> E["Execute task"]
 E --> S["State Manager"]
 S --> R
```



### 3.4. Control Plane và Execution Plane


```mermaid
flowchart TD
 subgraph CP ["Control Plane"]
 O["Orchestrator"]
 R["Router"]
 S["State Manager"]
 G["Execution Guard"]
 end
 subgraph EP ["Execution Plane"]
 P["Perception and Planning"]
 K["Retrieval"]
 T["Reasoning and Tools"]
 V["Verification and Correction"]
 end
 CP -->|Authorized tasks| EP
 EP -->|Structured results| CP
 U["Uncertainty Management"] -.->|Signals| CP
 U -.->|Signals| EP
```


Phân chia logic, không yêu cầu hai hệ thống triển khai riêng.

### 3.5. Luồng xử lý tổng thể


```mermaid
flowchart TD
 I["Problem Input"] --> N["Input Processing"]
 N --> P["Perception"]
 P --> R{"Adaptive Routing"}
 R -->|Lightweight| L["Direct Reasoning"]
 R -->|Structured| S["Planning / RAG / Reasoning"]
 L --> V["Verification"]
 S --> V
 V --> E{"Evaluate Status"}
 E -->|Correction allowed| C["Correction"]
 C --> R
 E -->|Accept| O["Structured Output"]
 E -->|Uncertainty or limit| U["Uncertainty Handling"]
 P -.->|Missing or unclear facts| U
 U -->|Clarify| H["User clarification"]
 H --> N
 U -->|Conditional answer or abstain| O
 U -->|Self resolve if allowed| R
```


Luồng khái niệm, không phải workflow chính thức. Cả hai tuyến có thể dùng công cụ. Bất định có thể xuất hiện ở mọi giai đoạn. Kết quả Verification có thể tác động Routing, Planning và Retrieval. Mọi vòng lặp chịu giới hạn thực thi; bảo toàn trạng thái liên quan khi tiếp tục sau clarification.

### 3.6. Module Traceability

| Requirement | Module chính |
|---|---|
| FR01 | M01, M03 |
| FR02 | M08 |
| FR03 | M09 |
| FR04 | M10, M16 |
| FR05 | M11, M15 |
| FR06 | M12, M11, M15 |
| FR07 | M04, M05, M06, M07 |
| FR08 | M13, M04 |
| FR09 | M02, M04 |
| FR10 | M19, M20, M21 |

M14, M17, M18 hỗ trợ xuyên suốt. Đây là truy vết cấp module, không thay thế RTM chi tiết.

### 3.7. Ranh giới phụ thuộc

| ID | Quy tắc |
|---|---|
| AR01 | Interface gọi Engine, không tự tổ chức workflow. |
| AR02 | Agent không tự gọi Agent khác tùy ý ngoài điều phối. |
| AR03 | Router đề xuất hành động; Orchestrator kiểm soát thực thi. |
| AR04 | Agent nhận trạng thái cần thiết, trả cập nhật có cấu trúc. |
| AR05 | Kết nối LLM Provider qua Model Gateway. |
| AR06 | Thực thi công cụ qua Tool Registry và validation. |
| AR07 | Truy cập dữ liệu bền vững qua Repository hoặc Storage Interface. |
| AR08 | Evaluation không đưa đáp án tham chiếu vào phiên suy luận. |

### 3.8. Kiến trúc theo MVP


```mermaid
flowchart LR
 A["MVP-A: Core Reasoning"] --> B["MVP-B: Grounded Multi-Agent"]
 B --> C["MVP-C: Adaptive Multimodal"]
 C --> D["MVP-D: Research Validation"]
```


| Giai đoạn | Năng lực |
|---|---|
| MVP-A | Input, Engine, Reasoning, Model Gateway, Math Tools, Output, benchmark và tracing cơ bản |
| MVP-B | Planning, Retrieval, Verification, Correction, Shared State |
| MVP-C | Perception, Adaptive Router, Uncertainty Handling, toàn bộ P0 |
| MVP-D | Đánh giá, baseline, ablation, phân tích lỗi |

Kiểm soát tài nguyên, cấu hình và ghi log ở mức tối thiểu từ MVP-A, mở rộng dần.

## 4. Technology Stack

**Trạng thái: Đã chốt.** Công nghệ phục vụ kiến trúc đã duyệt, Local-first và máy phát triển 16 GB RAM. Ưu tiên chiều sâu AI, khả năng kiểm soát thực nghiệm và đơn giản hóa hạ tầng. Không cố định phiên bản dependency cụ thể ngoài dòng phiên bản đã chọn trước kiểm thử tương thích.

### 4.1. Tổng hợp công nghệ

| Nhóm | Lựa chọn |
|---|---|
| Language & Environment | Python 3.12, uv, pyproject.toml, uv.lock |
| Agent Orchestration | LangGraph + Custom Agent Logic |
| Model Integration | LiteLLM + Custom Model Gateway; Native SDK Adapter khi cần |
| Validation | Pydantic v2 |
| Symbolic & Numerical Math | SymPy, NumPy, math, decimal, fractions |
| Multimodal | Pillow + VLM qua Model Gateway |
| Retrieval | BM25, Sentence Transformers, FAISS, RRF |
| Embedding | Embedding Gateway; BGE-M3 là ứng viên |
| Persistence | SQLite, SQLAlchemy 2.x, Alembic, sqlite3 |
| Interface | Python API, CLI, Gradio |
| Testing | pytest, Hypothesis, unittest.mock, pytest-cov |
| Evaluation | Custom Python, pandas, NumPy, Matplotlib |
| Observability | Python logging, JSONL, psutil |
| Code Quality | Ruff, mypy |
| CI | GitHub Actions |
| Containerization | Docker tùy chọn |

### 4.2. Programming Language & Environment

Python 3.12 là mục tiêu tương thích. uv quản lý Python, môi trường và dependency; commit pyproject.toml và uv.lock để tái lập môi trường. Ruff phục vụ lint/format, mypy kiểm tra kiểu. Poetry và pip + venv không chọn làm workflow chính. Kiểm tra tương thích Windows và thư viện native trước khi khóa dependency.

### 4.3. Agent Orchestration

LangGraph được chọn thay AutoGen, CrewAI và tự viết toàn bộ runtime vì phù hợp State Graph, conditional edges, bounded loops, checkpoint và interrupt/resume. Không phụ thuộc Agent dựng sẵn để quyết định phương pháp nghiên cứu.

| LangGraph | MATHK |
|---|---|
| Graph execution, nodes, edges | Agent Logic và Adaptive Routing Policy |
| State runtime | Mathematical Representation và quy tắc cập nhật state |
| Checkpoint, interrupt/resume | Resource Guard, Verification và Correction Strategy |
| Conditional transitions | Knowledge Retrieval Strategy |

```mermaid
flowchart TD
 E["MATHK Reasoning Engine"] --> G["LangGraph Runtime"]
 G --> S["Shared State"]
 G --> R["MATHK Adaptive Router"]
 G --> A["MATHK Agent Logic"]
 G --> C["Checkpointing"]
 A --> T["Mathematical Tools"]
 A --> M["Model Gateway"]
 A --> V["Verification Logic"]
```

LangGraph là framework thực thi, không phải đóng góp nghiên cứu. Router và guard vẫn tuân thủ AR01–AR08.

### 4.4. LLM Integration

Custom Model Gateway chuẩn hóa request, response, structured output, tool calls, lỗi, token usage và metadata. LiteLLM là adapter chính; Native SDK Adapter là đường mở rộng khi chức năng provider không tương thích. Model cụ thể và provider đầu tiên sẽ chọn sau thử nghiệm. Không bắt buộc dùng nhiều provider.

```mermaid
flowchart TD
 A["MATHK Agents"] --> G["Model Gateway"]
 G --> I["Model Port"]
 I --> L["LiteLLM Adapter"]
 L --> O["OpenAI"]
 L --> P["Google Gemini"]
 L --> R["OpenRouter"]
 L --> X["Other Providers"]
 I --> N["Native SDK Adapter khi cần"]
```

Model Profiles: DEFAULT (suy luận thông thường), MULTIMODAL (văn bản và hình ảnh), ADVANCED (suy luận hoặc sửa lỗi phức tạp), EMBEDDING (vector, qua Embedding Gateway). Các profile có thể dùng chung model; giữ model cố định khi cần cô lập biến thực nghiệm. LLM/VLM qua API bên ngoài trong MVP.

### 4.5. Data Validation

Pydantic v2 kiểm tra dữ liệu tại ranh giới module và structured output. Schema khái niệm: ProblemInput, ProblemRepresentation, ReasoningPlan, ReasoningStep, ToolRequest, ToolResult, VerificationReport, UncertaintyReport, ReasoningState, SolutionOutput, ExperimentConfig. Thiết kế schema chính thức ở các mục sau.

```mermaid
flowchart LR
 I["Raw Input"] --> P["Pydantic Validation"]
 P --> S["Structured Model"]
 S --> A["Agent or Tool"]
 A --> V["Output Validation"]
 V --> R["Structured Result"]
```

### 4.6. Mathematical Computation

SymPy và Calculator là năng lực P0, dùng NumPy và thư viện chuẩn Python cho tính số khi phù hợp. SciPy là tùy chọn khi cần. Direct Function Calling, Tool Registry, validation và bounded execution. Không thực thi mã Python tùy ý; không dùng eval/exec hoặc parse_expr/sympify trên chuỗi không kiểm soát. Giới hạn biểu thức, độ phức tạp và thời gian tính toán.

```mermaid
flowchart TD
 A["Reasoner or Verifier"] --> T["Tool Registry"]
 T --> V["Parameter Validation"]
 V --> E["Execution Guard"]
 E --> S["SymPy"]
 E --> C["Calculator"]
 E --> N["Numerical Tools khi cần"]
 S --> R["Structured Tool Result"]
 C --> R
 N --> R
```

### 4.7. Multimodal Processing

VLM-first, Pillow để đọc, kiểm tra và resize ảnh. OpenCV tùy nhu cầu, PyMuPDF ứng viên P1 cho PDF, OCR engine chọn khi xây baseline. Không bắt buộc huấn luyện detector hình học riêng.

```mermaid
flowchart TD
 I["Text and Images"] --> P["Pillow Image Validation"]
 P --> V["VLM via Model Gateway"]
 V --> S["Structured Problem Representation"]
```

Đầu vào chỉ văn bản không cần qua xử lý ảnh.

### 4.8. Knowledge Retrieval & Agentic RAG

BM25 làm sparse retrieval; Sentence Transformers và FAISS cho dense retrieval; RRF cho fusion. BGE-M3 là ứng viên, không mặc định tối ưu cho toán tiếng Việt. Embedding Gateway hỗ trợ chạy local hoặc API. Index và query phải dùng embedding tương thích; đổi model cần xây lại index tương ứng. Agentic Retrieval Logic do MATHK xây dựng, quyết định truy xuất và kiểm tra applicability trong giới hạn. Không đồng nhất Hybrid Retrieval với Agentic RAG.

```mermaid
flowchart TD
 Q["Knowledge Query"] --> F["Metadata Filtering"]
 F --> B["BM25"]
 F --> D["Embedding Gateway"]
 D --> V["FAISS"]
 B --> R["RRF"]
 V --> R
 R --> K["Relevant Knowledge"]
 K --> A["Applicability Checking"]
 A --> O["Knowledge References"]
```

```mermaid
flowchart TD
 subgraph OFF ["Offline Indexing"]
 K["Knowledge Base"] --> B["Embedding Provider"]
 B --> V[("FAISS Index")]
 end
 subgraph ON ["Online Reasoning"]
 Q["Knowledge Query"] --> E["Compatible Embedding Provider"]
 E --> S["Vector Search"]
 Q --> M["BM25"]
 V --> S
 S --> R["Hybrid Fusion"]
 M --> R
 R --> A["Reasoning Engine"]
 end
```

### 4.9. Database & Storage

Chốt SQLite + FAISS thay PostgreSQL + pgvector để giảm quản trị và phù hợp MVP local. SQLAlchemy 2.x quản lý persistence, Alembic quản lý schema migration, sqlite3 là driver. SQLite là nguồn dữ liệu chính cho metadata và dữ liệu nghiệp vụ; FAISS là index có thể xây dựng lại; file lớn, ảnh, dataset, trace/export dùng local file storage. Repository Interface giữ ranh giới module. Không lưu hai trạng thái nghiệp vụ độc lập thiếu đồng bộ. SQLite có giới hạn ghi đồng thời; PostgreSQL là lựa chọn tương lai nếu cần, việc chuyển đổi cần kiểm thử và migration.

```mermaid
flowchart TD
 E["MATHK Engine"] --> R["Repository Interfaces"]
 R --> ORM["SQLAlchemy"]
 ORM --> DB[("SQLite")]
 R --> F[("FAISS Index")]
 R --> FS["Local File Storage"]
 DB --> S["Sessions and Checkpoints"]
 DB --> K["Knowledge and Metadata"]
 DB --> X["Experiment Metadata"]
 F --> V["Knowledge Embeddings"]
 FS --> D["Images and Datasets"]
 FS --> L["Logs and Reports"]
```

Checkpoint chi tiết và cơ chế phối hợp persistence của LangGraph sẽ chốt ở State Management và Data & Storage Design.

### 4.10. Application Interface

Python API là giao diện cốt lõi, CLI cho chạy bài toán và thực nghiệm, Gradio làm demo văn bản/ảnh và lời giải toán học. FastAPI chỉ thêm khi cần HTTP. Streamlit và Next.js chưa triển khai. UI chỉ gọi Engine qua interface, không chứa logic suy luận.

### 4.11. Testing & Code Quality

pytest cho unit/integration, Hypothesis cho property-based testing, unittest.mock cho mock, pytest-cov cho coverage, Ruff/mypy cho chất lượng mã, GitHub Actions cho CI. Property testing không thay thế chứng minh toán học. Test provider bằng mock khi phù hợp để kiểm soát chi phí.

### 4.12. Evaluation & Observability

Custom Benchmark Runner và Evaluator, SymPy + custom mathematical evaluation, pandas/NumPy, SciPy nếu cần, Matplotlib, logging và JSONL, SQLite metadata, JSON/CSV export. LLM-as-Judge P1, Langfuse/LangSmith tùy chọn. Ground truth không đưa vào Engine.

```mermaid
flowchart TD
 D["Benchmark Dataset"] --> B["Benchmark Runner"]
 C["Experiment Config"] --> B
 B --> E["MATHK Engine"]
 E --> R["Solution and Execution Trace"]
 R --> V["Mathematical Evaluator"]
 G["Ground Truth"] --> V
 V --> M["Metrics"]
 M --> S[("Experiment Storage")]
 R --> S
 S --> O["Reports and Charts"]
```

Benchmark Runner chỉ chuyển dữ liệu đề bài được phép tới Engine, không chuyển nhãn ground truth.

### 4.13. Technology Stack Overview

```mermaid
flowchart TD
 I["Gradio / CLI / Python API"]
 C["Python 3.12 / LangGraph / Pydantic v2"]
 A["Model Gateway / LiteLLM / VLM"]
 T["SymPy / NumPy / Calculator"]
 K["BM25 / Sentence Transformers / FAISS / SQLite"]
 R["pytest / pandas / Ruff / uv / GitHub Actions"]
 I --> C
 C --> A
 C --> T
 C --> K
 R -.->|Research and engineering support| C
```

Sơ đồ nhóm trách nhiệm, không phải dependency graph bắt buộc.

### 4.14. Resource Management & Deployment Constraints

Máy phát triển 16 GB RAM. LLM qua API, local-first cho các thành phần khác. Lazy Loading, Shared Model Instance trong một tiến trình, Embedding Gateway, Configurable Concurrency, Bounded State và Resource Monitoring bằng psutil. Benchmark tuần tự hoặc giới hạn đồng thời; Docker tùy chọn, không bắt buộc chạy Docker Desktop trong phát triển. Embedding index tính trước và lưu; embedding truy vấn dùng model tương thích. Giữ BGE-M3 là ứng viên, cân nhắc embedding nhẹ hoặc API nếu RAM/latency không phù hợp.

Ước tính trước kiểm thử: Core không RAG khoảng 0,5–1 GB; full stack với embedding API khoảng 0,8–1,8 GB; BGE-M3 local khoảng 3–5,5 GB RAM riêng ứng dụng, benchmark có thể cao hơn. Đây không phải benchmark hoặc giới hạn cam kết, chưa gồm hệ điều hành/IDE/browser/Docker. Kiểm tra tiêu thụ thực tế ở MVP-A và khi tích hợp Retrieval; không cộng cơ học RAM các thư viện cùng tiến trình.

Các dependency, phiên bản model, cấu hình concurrency và ngưỡng tài nguyên cụ thể sẽ khóa sau kiểm thử. Không mở rộng sang PostgreSQL, vector database server, MCP, hạ tầng phân tán hoặc GPU server bắt buộc trong MVP.

**Quyết định:** Chấp thuận toàn bộ stack bảng 4.1 và nguyên tắc quản lý tài nguyên.

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
