# MATHK — Deployment

**Phiên bản:** 0.7

**Trạng thái:** Đang thảo luận

**Cấu trúc:** Đã duyệt 10 mục; nội dung từng mục chờ duyệt.

**Giả định đã chốt:** Full API Inference + Local-first Deployment. Laptop 8 GB RAM; LLM/VLM/embedding/reranker (nếu dùng) qua API. Cloud thuê tạm thời qua SSH với RAM giả định 16 GB chỉ là phương án tùy chọn khi cần tài nguyên bổ sung, không phụ thuộc GPU hoặc provider cụ thể. Quyết định này thay thế giả định laptop 16 GB và local model inference mặc định trước đây; cần đồng bộ tài liệu liên quan.

## 1. Deployment Strategy

**Trạng thái: Đã chốt.**

Full API Inference + Local-first Deployment. LLM, VLM, embedding và reranker nếu dùng qua API; LangGraph, routing, SymPy/Calculator, BM25/FAISS, SQLite, Gradio và evaluation chạy local. Không load model AI lớn local trong cấu hình chính. GPU cloud không bắt buộc, chỉ tùy chọn thuê tạm qua SSH khi có nhu cầu thực nghiệm riêng. Laptop 8 GB là mục tiêu chạy lightweight cần kiểm chứng bằng đo RAM thực tế. Giữ Modular Monolith và các guard/verification bắt buộc; không đồng nhất full API inference với microservices.

```mermaid
flowchart TD
 U["CLI / Gradio"] --> E["MATHK Engine - Local"]
 E --> T["Math Tools"]
 E --> K["BM25 / FAISS / SQLite"]
 E --> G["Model Gateway"]
 G --> A["LLM / VLM / Embedding API"]
```

Ưu tiên local development, testing, benchmark và demo; public demo tùy chọn. Free-first trong development, research pin model và cấu hình; chi phí/token/quota được ghi nhận. Docker tùy chọn. Nếu thuê máy tạm, dựng lại môi trường, đồng bộ và xác minh artifacts trước giải phóng tài nguyên. Không Kubernetes, microservices hoặc GPU server thường trực.


## 2. Deployment Architecture

**Trạng thái: Đã chốt.**

### 2.1. Kiến trúc
```mermaid
flowchart TD
 subgraph L["Laptop - 8 GB RAM"]
 A["Gradio / CLI / Benchmark"] --> B["MATHK Engine"]
 B --> C["LangGraph / Agents"]
 C --> D["Model Gateway"]
 C --> E["SymPy / Calculator"]
 C --> F["BM25 / FAISS"]
 C --> G["SQLite / Checkpoint"]
 end
 subgraph R["External APIs"]
 H["LLM API"]
 I["VLM API"]
 J["Embedding API"]
 end
 D --> H
 D --> I
 D --> J
```

### 2.2. Runtime Profiles
| Thuộc tính | Lightweight | Standard | Research |
|---|---|---|---|
| RAM mục tiêu | 8 GB | 16 GB | 8–16 GB |
| Inference và embedding | API | API | API |
| Concurrency | 1 | Giới hạn | Cố định theo thí nghiệm |
| Retrieval | BM25/Hybrid | Hybrid | Configurable |
| Trace | Cơ bản | Chi tiết | Đầy đủ metadata |
| Fallback | Cho phép | Cho phép | Mặc định tắt |
Không bỏ guard hoặc verification bắt buộc.

### 2.3. Hạ tầng
Modular Monolith; không cần thuê GPU, CUDA, PyTorch/Transformers cho local inference hoặc Docker Desktop trong phát triển. Cloud 16 GB dự phòng khi cần tài nguyên bổ sung.

### 2.4. Rủi ro
Rate limit: bounded retry; outage: configurable fallback; cost: execution budget; mất mạng: checkpoint/resume; model miễn phí thay đổi: gateway; thiếu RAM: sequential execution/lazy loading. Đồng bộ giả định Full API và RAM 8 GB vào tài liệu trước.


## 3. Environment & Dependencies

**Trạng thái: Đã chốt.**

### 3.1. Môi trường
Windows 11, Linux remote khi cần, laptop 8 GB RAM, Python 3.12, uv, VS Code, Codex, Git/GitHub, Full API inference; không yêu cầu CUDA.

### 3.2. Dependencies
| Nhóm | Thư viện |
|---|---|
| Core | Pydantic, PyYAML |
| Model Integration | OpenAI SDK, HTTPX |
| Orchestration | LangGraph |
| Mathematics | SymPy, NumPy |
| Retrieval | rank-bm25, faiss-cpu |
| Persistence | SQLAlchemy, Alembic |
| Multimodal | Pillow |
| Interface | Gradio |
| Evaluation | pandas, NumPy, Matplotlib |
| Monitoring | psutil |
| Testing | pytest, Hypothesis |
| Code Quality | Ruff, mypy |
SciPy, LiteLLM, OpenCV khi cần; không PyTorch, Transformers, Sentence Transformers hoặc GPU inference dependencies mặc định.

### 3.3. Quản lý
```mermaid
flowchart TD
 A["pyproject.toml"] --> B["uv Dependency Resolution"]
 B --> C["uv.lock"]
 C --> D["uv sync --locked"]
 D --> E["Virtual Environment"]
 E --> F["MATHK Runtime"]
```
pyproject.toml và uv.lock là nguồn chính; không duy trì requirements.txt song song nếu không cần.

### 3.4. Theo Phase
P0 Pydantic/pytest/Ruff/mypy; P1 SymPy/NumPy; P2 OpenAI SDK/HTTPX; P3 LangGraph/SQLAlchemy; P4 rank-bm25/faiss-cpu; P5 theo nhu cầu; P6 Pillow/Gradio; P7 pandas/Matplotlib/SciPy tùy chọn. Bổ sung theo nhu cầu, không cài tất cả từ đầu.

### 3.5. Resource Management
Lazy loading, sequential lightweight, không load AI model local, bounded context/state, giải phóng ảnh và dữ liệu trung gian, đo RAM bằng psutil.

### 3.6. Acceptance
Dựng lại từ uv.lock; kiểm chứng chạy trên laptop 8 GB; Windows/Linux trong phạm vi hỗ trợ; không cần GPU/CUDA; dependencies theo nhu cầu.


## 4. Model Provider & Gateway

**Trạng thái: Đã chốt.**

### 4.1. Kiến trúc
```mermaid
flowchart TD
 A["MATHK Agents"] --> B["Model Gateway"]
 K["Retrieval Pipeline"] --> B
 B --> C["Model Policy"]
 C --> D["9Router Adapter"]
 C --> E["Direct Provider Adapter"]
 D --> F["9Router"]
 F --> G["LLM / VLM Providers"]
 E --> G
 E --> H["Embedding API"]
 B --> I["Usage / Cost Tracker"]
```
Ưu tiên thử 9Router cho LLM/VLM; embedding trực tiếp nếu proxy không đáp ứng.

### 4.2. Model Profiles
MP01 Lightweight (phân loại/routing/tác vụ đơn giản); MP02 Reasoning (đa bước); MP03 Advanced (khó/correction); MP04 Vision; MP05 Embedding. Vai trò logic, không bắt buộc năm model riêng.

### 4.3. Trách nhiệm
Gateway: model profile, request/response normalization, ngân sách tổng, reasoning escalation, execution trace. 9Router: kết nối provider, provider routing, operational fallback, quota/API monitoring nếu hỗ trợ. Có thể thay proxy không sửa agent logic.

### 4.4. API policy
Development free-first, paid chỉ nếu cho phép, bounded fallback, model linh hoạt. Research theo cấu hình/ngân sách, fallback mặc định tắt, pin model khi có thể, xác minh actual model để so sánh theo model. Usage tracking cả hai; metadata thiếu ghi unknown.

### 4.5. Provider selection
P0 mathematical reasoning, structured output, tool calling, vision cho VLM, embedding quality cho embedding, stability, token cost/quota (theo capability cần thiết). P1 latency/context window. Không chọn chỉ theo parameter count hoặc benchmark công bố.

### 4.6. API failure
```mermaid
flowchart TD
 A["API Request"] --> B{"Thành công?"}
 B -->|Có| C["Validate Output"]
 B -->|Không| D{"Retry hợp lệ và còn budget?"}
 D -->|Có| E["Bounded Backoff"]
 E --> A
 D -->|Không| F{"Fallback hợp lệ và còn budget?"}
 F -->|Có| G["Alternative Provider"]
 G --> A
 F -->|Không| H["Structured Failure / Checkpoint"]
```
Retry/fallback cùng budget; giới hạn số lần và deadline; tránh retry lồng SDK/proxy/MATHK.

### 4.7. Model selection
Chưa chốt model cụ thể. P0 connectivity; P2 LLM; P4 embedding API; P5 routing; P6 VLM; P7 freeze research config. Custom Model Gateway + OpenAI-compatible SDK + 9Router Adapter + Direct Provider Adapter khi cần.


## 5. Configuration & Secrets

**Trạng thái: Đã chốt.**

### 5.1. Mục tiêu
Thay model/provider/budget/workflow/experiment config không sửa code; bảo vệ secrets.

### 5.2. Tổ chức
configs/default.yaml, configs/profiles/{lightweight,standard,research}.yaml, experiments/configs/, .env, .env.example, .gitignore. Git lưu YAML và mẫu env; không lưu .env thật.

### 5.3. Priority
```mermaid
flowchart TD
 A["Default Configuration"] --> B["Runtime Profile"]
 B --> C["Environment Variables"]
 C --> D["Explicit Runtime / Experiment Overrides"]
 D --> E["Pydantic Validation"]
 E --> F["Validated Configuration"]
 F --> G["MATHK Runtime"]
```
Tầng sau ghi đè tầng trước, ngoại trừ guard bắt buộc.

### 5.4. Nhóm cấu hình
models (ID/provider/params), gateway (endpoint/timeout/retry), agents (profile/capability), routing, retrieval (embedding API/top-k/hybrid), verification, budget, storage, logging, evaluation.

### 5.5. Secrets
Ví dụ .env.example:
```dotenv
MATHK_LLM_API_KEY=
MATHK_VLM_API_KEY=
MATHK_EMBEDDING_API_KEY=
MATHK_9ROUTER_API_KEY=
```
Không hard-code hoặc lưu key trong YAML/prompt/log/trace. GitHub Actions Secrets chỉ khi CI cần API; secrets riêng khi thuê máy; thu hồi và tạo lại key bị lộ. Không Vault/Cloud Secrets Manager MVP.

### 5.6. Validation
Thiếu key cần thiết: báo lỗi rõ; capability không phù hợp: từ chối hoặc fallback hợp lệ; budget sai: không chạy; path sai: báo lỗi hoặc khởi tạo an toàn; fallback trái policy: từ chối; research config thay đổi: phiên bản experiment mới. Kiểm thử capability thực tế ngoài YAML validation.

### 5.7. Reproducibility
Lưu snapshot cấu hình hiệu lực đã loại secrets, config hash, model ID, prompt version và Git commit mỗi benchmark. YAML + Pydantic Settings + .env + GitHub Secrets khi cần.


## 6. Data & Persistence

**Trạng thái: Đã chốt.**

### 6.1. Storage
SQLite cho session/problem/solution/KB; LangGraph SQLite checkpoint; FAISS vector index; JSONL trace; JSON/JSONL dataset; JSONL/JSON/CSV experiment results; local files cho ảnh.

### 6.2. Kiến trúc
```mermaid
flowchart TD
 A["MATHK Engine"] --> B["Repository Interfaces"]
 B --> C["SQLAlchemy"]
 C --> D[("mathk.sqlite")]
 A --> E["LangGraph Checkpointer"]
 E --> F[("checkpoints.sqlite")]
 A --> G["Local File Storage"]
 G --> H["Assets / Traces"]
 A --> I["Retrieval Pipeline"]
 I --> J["Embedding API"]
 I --> K[("FAISS Index")]
 I --> D
```

### 6.3. Cấu trúc
```text
data/
  knowledge/
    sources/
    processed/
  datasets/
    raw/
    processed/
  runtime/
    mathk.sqlite
    checkpoints.sqlite
    assets/
    indexes/
    traces/
experiments/
  configs/
  results/
  exports/
```
Theo 04_PROJECT_STRUCTURE.md.

### 6.4. Embedding Index
```mermaid
flowchart TD
 A["Knowledge Base"] --> B["Batch Processing"]
 B --> C["Embedding API"]
 C --> D["Vector Validation"]
 D --> E["Build FAISS Index"]
 E --> F["Validate and Save"]
 F --> G["Index + Manifest"]
 G --> H["Runtime Retrieval"]
```
Rebuild khi KB hoặc embedding config thay đổi; không embed toàn KB mỗi lần startup. Manifest gồm model ID, dimension, normalization, KB version, checksum và metadata theo System Design.

### 6.5. Backup
GitHub cho code; versioned KB backup; consistent SQLite backup; FAISS backup/rebuild; experiment backup theo ID; checkpoint theo workflow; dọn temp. Xác minh artifacts đã đồng bộ trước giải phóng cloud thuê.

### 6.6. RAM 8 GB
Không load toàn dataset; bounded embedding batches; load index cần thiết; JSONL tuần tự; lịch sử SQLite, bounded shared state; cách ly ground truth.

### 6.7. Stack
SQLite, SQLAlchemy, Alembic, FAISS CPU, local files, Embedding API. Không vector DB server, Redis, PostgreSQL, MongoDB, cloud storage bắt buộc trong MVP. Giữ hybrid retrieval và agentic RAG, không load embedding model local.


## 7. Application Deployment

*Chưa chốt.*

## 8. CI/CD & Release Management

*Chưa chốt.*

## 9. Monitoring & Maintenance

*Chưa chốt.*

## 10. Deployment Checklist

*Chưa chốt.*
