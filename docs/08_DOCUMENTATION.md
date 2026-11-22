# MATHK — Documentation

**Phiên bản:** 1.1

**Trạng thái:** Đã phê duyệt

## 1. Project Management & Agent Collaboration

**Trạng thái: Đã chốt.**

Project Owner (người học) giữ quyền quyết định cuối cùng, thiết kế và học tập; ChatGPT là Project Manager & Technical Lead, quản lý context, chia task, soạn prompt, review và hướng dẫn; Codex là Software Engineer, triển khai code, test, sửa lỗi và báo cáo. Owner chuyển tiếp prompt và báo cáo giữa hai agent. GitHub là Single Source of Truth.

```mermaid
flowchart TD
 A["ChatGPT đọc trạng thái"] --> B["Phân tích và giao task"]
 B --> C["Owner chuyển prompt"]
 C --> D["Codex triển khai và test"]
 D --> E["Owner chuyển báo cáo"]
 E --> F["ChatGPT review"]
 F --> G{"Đạt yêu cầu?"}
 G -->|Không| B
 G -->|Có| H["Learning Gate và checkpoint"]
 H --> A
```

Prompt tiếng Việt: Task ID, Context, Objective, References, Scope, Requirements, Constraints, Acceptance Criteria, Testing, Deliverables, Report Format. Codex không tự đổi kiến trúc, thêm dependency, vượt scope hoặc phase; báo cáo file thay đổi, test results, quyết định, lỗi và vấn đề tồn tại; dừng báo cáo mâu thuẫn. ChatGPT đối chiếu báo cáo với yêu cầu và đọc code/diff khi cần, không mặc định báo cáo đúng.

Task lifecycle: PLANNED → ASSIGNED → IN_PROGRESS → IN_REVIEW → ACCEPTED → COMPLETED; NEEDS_REVISION quay lại triển khai. COMPLETED cần Engineering Gate, Learning Gate và Checkpoint Gate. Owner giữ quyền phê duyệt quyết định quan trọng.

Quản lý dài hạn: AGENTS.md; docs/management/WORKFLOW.md, TASK_BOARD.md, DECISION_LOG.md; docs/progress/CURRENT_STATUS.md và phase_00.md, các phase tiếp theo theo nhu cầu. Checkpoint sau từng task nghiệm thu, không chờ context gần đầy. CURRENT_STATUS ghi phase, task, kết quả, vấn đề mở và bước tiếp theo. Các file bổ sung sẽ được tạo theo nhu cầu, chưa mặc định tồn tại.

Trọng tâm học: system/model/data thinking, cost optimization, research methodology, technical review; Codex đảm nhiệm phần lớn code. ChatGPT giao việc bằng prompt cho Owner chuyển tiếp, không tuyên bố điều khiển trực tiếp Codex.

## 2. Documentation Strategy

**Trạng thái: Đã chốt.**

### 2.1. Mục tiêu
DO01 nhất quán kiến trúc; DO02 khôi phục context; DO03 hướng dẫn coding agent; DO04 tiến độ/năng lực; DO05 quyết định kỹ thuật; DO06 tái lập nghiên cứu; DO07 bàn giao/vận hành.

### 2.2. Phân loại
Design (8 tài liệu), Management (task/workflow/decisions), Agent (AGENTS.md), Learning (labs/competency), Technical (API/schema/interface), Research (benchmark/experiment/paper), Operational (setup/vận hành/lỗi).

### 2.3. Single Source of Truth
```mermaid
flowchart TD
 A["GitHub Repository"] --> B["Design Baseline"]
 A --> C["Task and Progress"]
 A --> D["Source Code and Tests"]
 A --> E["Research Artifacts"]
 B --> F["ChatGPT Manager"]
 C --> F
 D --> F
 B --> G["Codex Engineer"]
 C --> G
 F --> H["Task Assignment"]
 H --> G
 G --> I["Implementation Report"]
 I --> F
 F --> J["Review and Checkpoint"]
 J --> A
```
Owner chuyển tiếp prompt/report; đọc trạng thái GitHub trước khi giao task trong phiên mới. Artifacts lớn hoặc riêng tư lưu ngoài Git, manifest và tham chiếu version hóa theo tài liệu 04/06.

### 2.4. Principles
Docs-first, Single Source of Truth, Living Documentation, Traceability (Requirement → Design → Task → Code → Test), Incremental Documentation, Context-efficient, Vietnamese-first.

### 2.5. Quyền quản lý
ChatGPT đề xuất thiết kế, Owner phê duyệt; ChatGPT quản lý task và kiểm tra nhất quán; Codex cập nhật tài liệu kỹ thuật theo code trong scope; ChatGPT và Owner cập nhật learning checkpoint. Codex không tự sửa baseline để hợp thức hóa code sai. Documentation-driven Development + AI-assisted Project Management.


## 3. Documentation Structure

**Trạng thái: Đã chốt.**

### 3.1. Cấu trúc
```text
MathAgents_MATHK/
├── README.md
├── AGENTS.md
├── docs/
│   ├── 01_REQUIREMENTS.md
│   ├── 02_RESEARCH.md
│   ├── 03_SYSTEM_DESIGN.md
│   ├── 04_PROJECT_STRUCTURE.md
│   ├── 05_IMPLEMENTATION.md
│   ├── 06_EVALUATION.md
│   ├── 07_DEPLOYMENT.md
│   ├── 08_DOCUMENTATION.md
│   ├── management/
│   │   ├── WORKFLOW.md
│   │   ├── TASK_BOARD.md
│   │   ├── TRACEABILITY_MATRIX.md
│   │   └── DECISION_LOG.md
│   ├── progress/
│   │   ├── CURRENT_STATUS.md
│   │   └── phase_00.md ...
│   ├── guides/
│   │   ├── DEVELOPER_GUIDE.md
│   │   ├── USER_GUIDE.md
│   │   └── TROUBLESHOOTING.md
│   ├── technical/
│   │   ├── API_REFERENCE.md
│   │   └── DATA_CONTRACTS.md
│   └── research/
│       ├── EXPERIMENT_LOG.md
│       ├── RESULTS_ANALYSIS.md
│       └── PAPER_DRAFT.md
└── labs/
    └── phase_00/ ...
```

### 3.2. Ownership
ChatGPT: AGENTS, WORKFLOW, TASK_BOARD, DECISION_LOG, CURRENT_STATUS; ChatGPT + Owner: phase_XX; Codex: API_REFERENCE, DATA_CONTRACTS theo scope và review.

### 3.3. Context
```mermaid
flowchart TD
 A["Phiên mới"] --> B["CURRENT_STATUS.md"]
 B --> C["TASK_BOARD.md"]
 C --> D["Task hiện tại"]
 D --> E["Tài liệu thiết kế liên quan"]
 E --> F["Code và kết quả cần thiết"]
 F --> G["Tiếp tục quản lý dự án"]
```

### 3.4. Thời điểm
Trước Phase 0: AGENTS, WORKFLOW, TASK_BOARD, CURRENT_STATUS, DECISION_LOG. Phase 0–1: README, Developer Guide, Mini Labs. Phase 2–3: API Reference, Data Contracts. Phase 4–6: User Guide, Troubleshooting. Phase 7: Experiment Log, Results Analysis, Paper Draft.

### 3.5. Nguyên tắc
Không tạo file rỗng hàng loạt; tránh sao chép, dùng liên kết Markdown; mỗi thông tin một nguồn chính thức; cập nhật sau từng task/quyết định quan trọng. Ưu tiên bộ tài liệu quản lý agent trước Phase 0.


## 4. Project README

**Trạng thái: Đã chốt.**

### 4.1. Mục tiêu
Trang giới thiệu kỹ thuật và nghiên cứu cho giảng viên, nhà tuyển dụng, nhà nghiên cứu và developer; không chỉ giới thiệu ứng dụng giải toán.

### 4.2. Cấu trúc
Project Overview, Problem Statement, Research Objectives, Key Features, System Architecture, Technology Stack, Demo, Quick Start, Project Structure, Evaluation Results, Development Roadmap, Documentation, Limitations, References & License.

### 4.3. Sơ đồ tổng quan
```mermaid
flowchart TD
 A["Text / Image Input"] --> B["Adaptive Orchestration"]
 B --> C["Perception Agent"]
 B --> D["Planning Agent"]
 B --> E["Retrieval Agent"]
 B --> F["Reasoning Agent"]
 B --> G["Verification Agent"]
 E --> H["Mathematical Knowledge Base"]
 F --> I["SymPy / Calculator"]
 G --> I
 G -->|Correction required| B
 B --> J["Solution & Verification Report"]
 B --> K["Model Gateway"]
 K --> L["External Model APIs"]
```
Sơ đồ tổng quan, không quy định thứ tự thực thi cố định; các kết nối logic tuân thủ gateway/guard/interface trong System Design.

### 4.4. Cập nhật theo milestone
Phase 0: giới thiệu, mục tiêu, môi trường, roadmap. MVP A: Quick Start và ví dụ Text Solver. MVP B: Multi-Agent và Retrieval. MVP C: demo, Adaptive Routing, Verification. MVP D: benchmark, ablation, kết quả và giới hạn.

### 4.5. Nguyên tắc
Phân biệt tính năng thực tế/dự kiến; không công bố benchmark giả lập như kết quả thật, không khẳng định novelty chưa kiểm chứng. Liên kết System Design thay sao chép. Tiếng Việt, giữ thuật ngữ tiếng Anh; README_EN.md P1 khi công bố hoặc ứng tuyển.

### 4.6. Ownership
ChatGPT định hướng; Codex cập nhật lệnh/ví dụ thực tế; ChatGPT và Owner xác minh kết quả; Owner phê duyệt công bố.


## 5. Developer Guide

**Trạng thái: Đã chốt.**

### 5.1. Mục tiêu
docs/guides/DEVELOPER_GUIDE.md hướng dẫn Owner, Codex và developer phát triển hệ thống, không dạy Python từ đầu.

### 5.2. Cấu trúc
Development Environment, Getting Started, Architecture Overview, Coding Standards, Dependency Management, Extension Guide, Testing Guide, Debugging Guide, Git Workflow, Contribution Rules.

### 5.3. Extension Guide
| Mở rộng | Thành phần |
|---|---|
| LLM Provider | Model Gateway |
| Agent | Agent Contract, Orchestrator |
| Math Tool | Tool Registry, Execution Guard |
| Retrieval | Retrieval Interface |
| Routing | Adaptive Router |
| Verification | Verification Interface |
| Metric | Evaluation Framework |
| UI | Application Interface |

Mỗi hướng dẫn gồm mục đích, module, data contract, sơ đồ luồng, ví dụ triển khai và kiểm thử.

### 5.4. Workflow
```mermaid
flowchart TD
 A["Task từ ChatGPT"] --> B["Đọc tài liệu và contracts"]
 B --> C["Xác định scope"]
 C --> D["Codex triển khai"]
 D --> E["Local Testing"]
 E --> F["Implementation Report"]
 F --> G["ChatGPT Review"]
 G --> H{"Đạt yêu cầu?"}
 H -->|Không| D
 H -->|Có| I["Commit / Push / CI"]
 I --> J{"CI Passed?"}
 J -->|Không| D
 J -->|Có| K["Learning và Checkpoint"]
```
Owner chuyển tiếp prompt/report.

### 5.5. Quy tắc
Tuân thủ Modular Monolith và Dependency Rules; tái sử dụng interface, tránh abstraction thừa; dependency mới cần lý do/phê duyệt; thay đổi hành vi cần test; không bypass Execution Guard, không vượt scope; cập nhật tài liệu kỹ thuật khi interface đổi.

### 5.6. Developer Guide và AGENTS.md
Developer Guide giải thích kiến trúc, ví dụ, hướng dẫn mở rộng cho người và agent, cập nhật theo phase. AGENTS.md ngắn gọn, có tính chỉ thị, quy định hành vi và ràng buộc cho coding agent, cập nhật khi quy trình thay đổi.

### 5.7. Ownership
ChatGPT định hướng/review; Codex bổ sung theo implementation thực tế; Owner dùng tài liệu để học và đánh giá quyết định. Phát triển dần theo phase, ưu tiên Extension Guide và System Thinking.


## 6. AI Agent Instructions — AGENTS.md

**Trạng thái: Đã chốt.**

### 6.1. Phân tầng chỉ thị
AGENTS.md → Approved Design Documents → Task Prompt → Implementation Decisions. Đây là thứ tự quy tắc nội bộ dự án, không thay thế chỉ thị cấp hệ thống hoặc quyền hạn thực tế của agent. Mâu thuẫn phải dừng và báo cáo.

### 6.2. Cấu trúc
Project Context, Agent Role, Source of Truth, Architecture Rules, Coding Standards, Task Execution Protocol, Testing Requirements, Security Rules, Reporting Protocol, Git Rules, Context Management.

### 6.3. Quyền hạn
Tự triển khai code/test/sửa lỗi trong scope, đọc repo, cập nhật tài liệu kỹ thuật liên quan. Cần phê duyệt dependency mới, đổi kiến trúc, public interface ngoài task, chi phí ngoài budget. Commit/push theo task prompt; không tự xóa dữ liệu hoặc force push.

### 6.4. Task Execution Protocol
```mermaid
flowchart TD
 A["Nhận Task Prompt"] --> B["Đọc AGENTS.md và tài liệu liên quan"]
 B --> C["Kiểm tra repository"]
 C --> D["Phân tích yêu cầu"]
 D --> E{"Có mâu thuẫn hoặc trở ngại?"}
 E -->|Có| F["Dừng và báo cáo"]
 E -->|Không| G["Triển khai trong Scope"]
 G --> H["Chạy Tests"]
 H --> I["Self Review"]
 I --> J["Implementation Report"]
 J --> K["ChatGPT Review"]
 K --> L{"Đạt yêu cầu?"}
 L -->|Không| G
 L -->|Có| M["Nghiệm thu"]
```
Owner chuyển tiếp prompt/report.

### 6.5. Implementation Report
Task ID; Status (Completed/Partial/Blocked); Summary; Changed Files và lý do; Technical Decisions; Test Results (lệnh và kết quả thật); Acceptance Criteria (PASS/FAIL/NOT_RUN); Resource Usage (API/token/cost nếu có); Known Issues; Git Status (branch/commit/push); Learning Notes. ChatGPT review trước nghiệm thu.

### 6.6. Learning-aware Coding
Comment tiếng Việt tại logic quan trọng, giải thích lý do lựa chọn; dễ hiểu/test/mở rộng; Mini Lab có tham số thực nghiệm; nêu trade-off model/data/architecture/accuracy/cost; không comment từng dòng hoặc dạy cú pháp cơ bản.

### 6.7. Context Optimization
AGENTS.md mỗi phiên; CURRENT_STATUS khi bắt đầu/khôi phục; Task Prompt mỗi task; design sections liên quan; code module và dependencies; previous reports khi tiếp tục/sửa. AGENTS.md ngắn gọn, dẫn liên kết chi tiết.

### 6.8. Ownership
ChatGPT soạn/quản lý AGENTS.md, Codex không tự sửa nội quy. Codex tự chủ implementation trong scope, không tự quyết mục tiêu/kiến trúc/acceptance. Tạo AGENTS.md chính thức sau tài liệu 08, trước task đầu Phase 0.


## 7. Learning Documentation

**Trạng thái: Đã chốt.**

### 7.1. Mục tiêu
Gắn với 73 Mini Labs và 40 năng lực trong Implementation Roadmap; hiểu, thiết kế và đánh giá hệ thống thay vì viết code từng dòng.

### 7.2. Mini Lab
Ví dụ labs/phase_00/06_model_gateway/ gồm README.md (lý thuyết, sơ đồ, mục tiêu, hướng dẫn), exercise.py (code Codex), test_exercise.py (kiểm chứng), notes.md (kết quả và nhận xét). Chỉ tạo file cần thiết.

### 7.3. Learning Content Template
Problem, Core Concepts, Architecture, Code Walkthrough theo khối logic, Experiment, Trade-offs, Knowledge Check, MATHK Integration.

### 7.4. Learning Workflow
```mermaid
flowchart TD
 A["ChatGPT giải thích"] --> B["Owner phân tích và dự đoán"]
 B --> C["ChatGPT giao task"]
 C --> D["Codex xây dựng Mini Lab"]
 D --> E["Owner chạy và quan sát"]
 E --> F["ChatGPT phân tích kết quả"]
 F --> G["Owner giải thích và đề xuất thiết kế"]
 G --> H{"Learning Gate"}
 H -->|Chưa đạt| A
 H -->|Đạt| I["Cập nhật Competency"]
 I --> J["Tích hợp MATHK"]
```
Owner chuyển tiếp prompt/report; không bắt buộc viết lab từ đầu.

### 7.5. Competency Tracking
L0 chưa học; L1 hiểu/giải thích; L2 đọc code/dự đoán/thực nghiệm; L3 thiết kế/giao việc/review; L4 phân tích trade-off/debug/vận dụng. Đánh giá dựa trên bằng chứng, không số dòng code hoặc số lab đã chạy.

### 7.6. Learning Checkpoint
Sau lab/task ghi kiến thức và competency, thực nghiệm, kết quả/nhận xét của Owner, điểm chưa hiểu, quyết định áp dụng, mức đạt và bằng chứng, bước học tiếp. Lưu docs/progress/phase_XX.md và cập nhật CURRENT_STATUS.md.

### 7.7. Ownership
ChatGPT thiết kế bài học, giải thích, đánh giá năng lực và lưu checkpoint; Codex viết code thực nghiệm; Owner + Codex chạy, Owner + ChatGPT phân tích. System-first, AI-assisted, Experiment-driven, Competency-based; quản lý song song tiến độ kỹ thuật và học tập.


## 8. Architecture & API Documentation

**Trạng thái: Đã chốt.**

### 8.1. Phân loại
03_SYSTEM_DESIGN: thiết kế; 04_PROJECT_STRUCTURE: cấu trúc/dependency rules; technical/API_REFERENCE.md: interface thực tế; technical/DATA_CONTRACTS.md: schema thực tế; code: implementation; tests: kiểm chứng.

### 8.2. Sơ đồ
Mermaid component, sequence, state, flowchart, ER, dependency graph; tham chiếu sơ đồ thiết kế hiện có thay vì sao chép.

### 8.3. API Reference
Python Interface chính, không mặc định REST. Mô tả Application API (solve/resume/cancel/trace), Model Gateway, Agent Contract, Math Tools, Retrieval, Verification, Persistence, Evaluation; mỗi interface nêu mục đích, input/output, ví dụ, lỗi và ràng buộc.

### 8.4. Data Contracts
```mermaid
flowchart LR
 A["Input Schema"] --> B["Validation"]
 B --> C["Module Interface"]
 C --> D["Structured Output"]
 D --> E["Validation"]
 E --> F["Consumer"]
```
Pydantic schema trong code là nguồn chính thức của hợp đồng thực tế; tài liệu giải thích ý nghĩa, cách dùng, quan hệ, không duy trì định nghĩa trùng lặp. ProblemInput, AgentResult, ToolRequest, VerificationReport, SolveResult theo phase.

### 8.5. Traceability
```mermaid
flowchart TD
 A["Requirement"] --> B["System Design"]
 B --> C["Task ID"]
 C --> D["Module / Interface"]
 D --> E["Test Cases"]
 E --> F["Acceptance Evidence"]
```

### 8.6. Công nghệ
Markdown, Mermaid, Pydantic, Python docstrings, JSON Schema export khi cần; documentation website P1; chưa cần MkDocs/Sphinx/Swagger trong MVP.

### 8.7. Ownership
Codex cập nhật kỹ thuật theo code; ChatGPT review nhất quán kiến trúc/contracts/code/tests. Báo cáo sai lệch trước khi sửa baseline. Lightweight Architecture Documentation + Code-first API Contracts + Requirements Traceability.


## 9. Research Documentation

**Trạng thái: Đã chốt.**

### 9.1. Mục tiêu
Quản lý bằng chứng nghiên cứu từ phase đầu, không đợi Phase 7.

### 9.2. Tổ chức
02_RESEARCH.md: literature/gap/RQ; 06_EVALUATION.md: phương pháp; docs/research/EXPERIMENT_LOG.md, RESULTS_ANALYSIS.md, PAPER_DRAFT.md; experiments/configs, results, exports. Artifacts lớn/riêng tư không commit, quản lý manifest theo 04/06.

### 9.3. Experiment Documentation
Experiment ID, Objective, Hypothesis, Configuration, Controlled Variables, Dataset Version, Metrics, Results, Analysis, Limitations, Conclusion, Reproducibility (commit/config/artifact). Tham chiếu manifest thay sao chép metadata.

### 9.4. Workflow
```mermaid
flowchart TD
 A["Research Question"] --> B["Hypothesis"]
 B --> C["Experiment Design"]
 C --> D["ChatGPT giao Task"]
 D --> E["Codex triển khai và chạy"]
 E --> F["Raw Results"]
 F --> G["ChatGPT và Owner phân tích"]
 G --> H["Research Evidence"]
 H --> I["Results Analysis"]
 I --> J["Paper Draft"]
```

### 9.5. Paper
Abstract, Introduction, Related Work, Methodology, Experimental Setup, Results, Discussion, Limitations, Conclusion, References. Bản thảo tiếng Việt; bản công bố quốc tế tiếng Anh.

### 9.6. Research Integrity
Không giả kết quả/cherry-pick/khẳng định novelty chưa kiểm chứng; phân biệt giả thuyết, quan sát và kết luận; bảo toàn reproducibility và ground truth isolation.

### 9.7. Ownership
ChatGPT + Owner: research design, literature review, error analysis, scientific writing. Codex: experiment implementation/execution. ChatGPT + Codex: statistical analysis. Owner phê duyệt kết luận.

### 9.8. Thời điểm
P0–2 model/prompt/tool; P3–4 multi-agent/retrieval/context; P5–6 adaptive routing/verification/correction/multimodal; P7 benchmark chính thức/baseline/ablation/statistics/paper. Phân biệt dev experiments với held-out; research hypotheses chưa duyệt vẫn chưa được coi là baseline. Evidence-driven, Reproducible, Incremental.


## 10. User & Deployment Guide

**Trạng thái: Đã chốt.**

### 10.1. Mục tiêu
Người dùng mới có thể cài đặt, sử dụng và đánh giá MATHK độc lập, không cần sửa source code.

### 10.2. Phân chia
README: Quick Start; 07_DEPLOYMENT: chiến lược; guides/USER_GUIDE.md: sử dụng; guides/TROUBLESHOOTING.md: sự cố; .env.example: mẫu biến môi trường; configs/: cấu hình.

### 10.3. User Guide
System Requirements, Installation (Python/uv), Configuration (API key/profile/budget), Quick Start, Student Mode, Research Mode (trace/verification/cost), Multimodal Input, Session Management, Benchmark Usage, Limitations.

### 10.4. User Workflow
```mermaid
flowchart TD
 A["Cài đặt MATHK"] --> B["Thiết lập API Key"]
 B --> C["Chọn Runtime Profile"]
 C --> D["Khởi chạy CLI hoặc Gradio"]
 D --> E["Nhập bài toán"]
 E --> F["MATHK xử lý"]
 F --> G["Lời giải và Verification Report"]
 G --> H["Xem kết quả"]
 G --> I["Phân tích Execution Trace"]
```
Mặc định laptop 8 GB RAM, Full API Inference, Lightweight Profile.

### 10.5. Troubleshooting
Invalid API Key, rate limit/quota, model capability, RAM cao, index không tương thích, budget exhausted, interrupted execution, verification failed, installation failed. Mỗi mục: triệu chứng → nguyên nhân có thể → kiểm tra → xử lý; không vượt guard/budget.

### 10.6. Trực quan
Ảnh Gradio thực tế, Mermaid, ví dụ input/output, CLI/config, video demo ngắn MVP C/D. Không dùng minh họa làm bằng chứng tính năng hoàn thành.

### 10.7. Ownership
ChatGPT thiết kế/review/nghiệm thu; Codex xác minh lệnh và viết hướng dẫn theo implementation; Owner kiểm tra usability.

### 10.8. Acceptance
Người mới tái dựng môi trường, cấu hình API, chạy bài mẫu, đọc kết quả, xử lý lỗi phổ biến không sửa source. Local-first, đơn giản, tái lập, bám implementation thực tế.


## 11. Context & Progress Management

**Trạng thái: Đã chốt.**

### 11.1. Persistent Project Memory
GitHub là nguồn bộ nhớ dài hạn chính thức. Project: 01–08; agent: AGENTS.md; management: WORKFLOW.md; task: TASK_BOARD.md; decision: DECISION_LOG.md; working: CURRENT_STATUS.md; learning: phase_XX.md; research: EXPERIMENT_LOG.md; implementation: code/tests/Git history.

### 11.2. CURRENT_STATUS.md
Current Phase, Milestone, Lab, Active Task, Engineering Progress, Learning Progress, Latest Verified Implementation Commit, Pending Decisions, Blockers, Next Action, Relevant Context (links), Last Checkpoint. Chỉ giữ trạng thái hiện tại, không tích lũy lịch sử.

### 11.3. Task Lifecycle
```mermaid
flowchart TD
 A["PLANNED"] --> B["ASSIGNED"]
 B --> C["IN_PROGRESS"]
 C --> D["IN_REVIEW"]
 D --> E["NEEDS_REVISION"]
 E --> C
 D --> F["ACCEPTED"]
 F --> G["COMPLETED"]
```
ACCEPTED: nghiệm thu kỹ thuật. COMPLETED: Engineering Gate + Learning Gate + Checkpoint Gate.

### 11.4. Checkpoint Strategy
Bắt buộc khi chốt thiết kế, giao task, nghiệm thu, hoàn thành lab/phase; khi nhận báo cáo lưu trạng thái và bằng chứng; trước chuyển phiên nếu có thể; chủ động lưu định kỳ khi hội thoại dài. Không thể đo chính xác context còn lại, nên lưu sớm và thường xuyên.

### 11.5. Context Recovery
```mermaid
flowchart TD
 A["Phiên mới"] --> B["CURRENT_STATUS.md"]
 B --> C["TASK_BOARD.md"]
 C --> D["Active Task"]
 D --> E["Quyết định và thiết kế liên quan"]
 E --> F["Code và Git history"]
 F --> G["Learning Context"]
 G --> H["Tiếp tục công việc"]
```
Prompt khôi phục: Tiếp tục quản lý dự án MATHK. Đọc checkpoint mới nhất trên GitHub và tiếp tục công việc đang thực hiện.

### 11.6. Just-in-Time Context
Chỉ đọc phần thiết kế, cấu hình, code và bằng chứng cần cho task hiện tại; không nạp toàn bộ tám tài liệu mỗi lần.

### 11.7. Nguyên tắc
Phân biệt đề xuất/đã duyệt/implementation; không hoàn thành thiếu bằng chứng; lưu lịch sử quyết định; không lưu secrets/dữ liệu nhạy cảm; xác minh commit và nội dung sau push; theo dõi song song kỹ thuật và học tập. Persistent Project Memory + Event-driven Checkpoint + Just-in-Time Context + Dual Progress Tracking.


## 12. Documentation Maintenance

**Trạng thái: Đã chốt.**

### 12.1. Mục tiêu
Living Documentation đồng bộ thiết kế, implementation và tiến độ.

### 12.2. Chính sách cập nhật
Yêu cầu → 01; kiến trúc → 03 và Decision Log; cấu trúc → 04; roadmap → 05; đánh giá → 06; môi trường → 07; quản lý → 08 và AGENTS.md; interface → API Reference/Data Contracts; task → Task Board/Current Status; lab → Learning Checkpoint; experiment → Experiment Log. Chỉ cập nhật tài liệu bị ảnh hưởng.

### 12.3. Versioning
v0.x thảo luận; v1.0 baseline đầu tiên; v1.1 bổ sung nhỏ; v1.1.1 sửa lỗi; v2.0 thay đổi lớn. Độc lập phiên bản phần mềm.

### 12.4. Change Management
```mermaid
flowchart TD
 A["Nhu cầu thay đổi"] --> B["ChatGPT phân tích tác động"]
 B --> C["Đề xuất"]
 C --> D{"Owner phê duyệt?"}
 D -->|Không| E["Giữ baseline"]
 D -->|Có| F["Decision Log"]
 F --> G["Cập nhật tài liệu"]
 G --> H["Giao task Codex"]
 H --> I["Implementation và Testing"]
 I --> J["Review nhất quán"]
 J --> K["Commit và Checkpoint"]
```
Codex không tự sửa thiết kế để hợp thức hóa sai lệch.

### 12.5. Quality Checklist
- Nội dung đúng quyết định duyệt.
- Không mâu thuẫn liên tài liệu.
- Không trùng lặp không cần thiết.
- Interface/schema phù hợp implementation.
- Mermaid đúng cú pháp và luồng.
- Lệnh cài đặt/chạy được kiểm chứng.
- Kết quả nghiên cứu có bằng chứng.
- Không secrets/dữ liệu nhạy cảm.
- Liên kết hợp lệ.
- Version/status cập nhật.

### 12.6. Review
Task-level sau task; phase-level cuối phase; milestone MVP A/B/C/D; full audit trước release/công bố.

### 12.7. Ownership
Owner phê duyệt thay đổi quan trọng; ChatGPT kiểm soát nhất quán/version/decisions/checkpoint; Codex cập nhật technical docs trong scope.

### 12.8. Definition of Done
Nội dung duyệt, đồng bộ tài liệu liên quan, sơ đồ cần thiết, commit GitHub và xác minh sau push. Các kiểm chứng phụ thuộc implementation thực hiện khi có implementation; cross-document audit và kiểm tra render còn là bước tiếp theo.

### 12.9. Bước tiếp theo
Cross-document audit (02 Research vẫn tạm hoãn), khởi tạo AGENTS.md, WORKFLOW.md, TASK_BOARD.md, DECISION_LOG.md, CURRENT_STATUS.md; chốt planning baseline; Phase 0 Foundation.


### 12.10. Traceability Matrix — AUD-005
Owner đã duyệt docs/management/TRACEABILITY_MATRIX.md: theo dõi toàn bộ 259 FR/NFR/BR, module, phase, task, test và evidence; ánh xạ ban đầu cấp nhóm, tinh chỉnh từng ID theo task, không coi PLANNED là coverage đã kiểm chứng. ChatGPT quản lý, Codex bổ sung trong scope. MVP C hoàn thiện P0 chức năng engine; MVP D hoàn thiện P0 benchmark/nghiên cứu. Chỉ Evaluator tiếp nhận ground truth.
