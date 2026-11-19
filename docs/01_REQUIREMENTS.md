# 01 — REQUIREMENTS

**Dự án:** MATHK  
**Phiên bản:** 1.0  
**Trạng thái:** Approved — Requirements Baseline

## 1. Bối cảnh và đặt vấn đề

MATHK hướng tới giải quyết các hạn chế của hệ thống AI dựa trên mô hình ngôn ngữ lớn (LLM) trong quá trình hiểu, phân tích, suy luận và giải quyết các bài toán đa phương thức.

### 1.1. Các vấn đề cốt lõi

| ID | Vấn đề | Mô tả |
|---|---|---|
| P01 | Multimodal Understanding | Hiểu sai hoặc bỏ sót dữ kiện từ văn bản, hình ảnh, hình học, đồ thị và ký hiệu toán học. |
| P02 | Multi-step Reasoning | Sai sót trong lập kế hoạch, suy luận logic và giải toán nhiều bước. |
| P03 | Mathematical Computation | Sai sót trong tính toán số học, biến đổi biểu thức và xử lý các phép toán. |
| P04 | Knowledge Grounding | Sử dụng sai hoặc thiếu căn cứ khi áp dụng định nghĩa, công thức và định lý toán học. |
| P05 | Verification & Self-correction | Thiếu khả năng kiểm chứng kết quả, phát hiện lỗi và tự sửa lời giải. |
| P06 | Reasoning Efficiency | Chi phí tính toán, chi phí sử dụng mô hình và độ trễ tăng trong quá trình suy luận. |
| P07 | Uncertainty Awareness | Không nhận biết được dữ kiện thiếu, mâu thuẫn, mơ hồ hoặc thông tin chưa đủ tin cậy. |

### 1.2. Định hướng giải quyết

| ID | Hướng giải quyết dự kiến |
|---|---|
| P01 | Multimodal Perception & Understanding |
| P02 | Planning & Multi-Agent Reasoning |
| P03 | Tool Calling & Neuro-Symbolic Reasoning |
| P04 | Knowledge Retrieval & Agentic RAG |
| P05 | Verification & Self-correction |
| P06 | Adaptive Agent Routing |
| P07 | Uncertainty Estimation, Human-in-the-loop & Abstention |

Các vấn đề trên là cơ sở xác định yêu cầu hệ thống, câu hỏi nghiên cứu và thiết kế thực nghiệm.

Các phương pháp giải quyết mới ở mức định hướng. Hiệu quả thực tế cần được kiểm chứng thông qua nghiên cứu và thực nghiệm.

## 2. Tầm nhìn sản phẩm

MATHK là hệ thống AI chuyên sâu về suy luận toán học (AI Mathematical Reasoning Engine), hướng tới khả năng xử lý đa phương thức, sử dụng công cụ toán học và phối hợp nhiều tác tử.

Giải toán và giáo dục là các lĩnh vực ứng dụng của hệ thống, không phải giới hạn của kiến trúc cốt lõi.

## 3. Mục tiêu dự án

### 3.1. Mục tiêu sản phẩm (Product Objectives)

| ID | Mục tiêu |
|---|---|
| PO01 | Hiểu đề toán đa phương thức. |
| PO02 | Giải quyết bài toán nhiều bước. |
| PO03 | Cung cấp lời giải có căn cứ toán học. |
| PO04 | Kiểm chứng kết quả và tự sửa lỗi khi phát hiện sai sót. |
| PO05 | Nhận biết bài toán thiếu hoặc mâu thuẫn dữ kiện. |
| PO06 | Có khả năng mở rộng sang các miền toán học khác. |

### 3.2. Mục tiêu nghiên cứu (Research Objectives)

| ID | Câu hỏi nghiên cứu |
|---|---|
| RO01 | Multi-Agent có cải thiện chất lượng giải toán so với Single-Agent không? |
| RO02 | Việc kết hợp công cụ tính toán ký hiệu có cải thiện độ chính xác không? |
| RO03 | Agentic RAG có cải thiện khả năng áp dụng kiến thức toán học không? |
| RO04 | Cơ chế kiểm chứng và tự sửa lỗi cải thiện chất lượng lời giải đến mức nào? |
| RO05 | Adaptive Routing có giảm chi phí và độ trễ mà vẫn duy trì chất lượng không? |
| RO06 | Khai thác thông tin trực quan có cải thiện kết quả so với phương pháp chỉ sử dụng văn bản hoặc OCR không? |
| RO07 | Hệ thống có nhận biết và xử lý tốt các bài toán thiếu hoặc mâu thuẫn dữ kiện không? |

Các câu hỏi nghiên cứu cần được trả lời thông qua thực nghiệm có kiểm soát, không mặc định các phương pháp đề xuất sẽ vượt trội hơn baseline.

### 3.3. Mục tiêu kỹ thuật (Technical Objectives)

| ID | Mục tiêu |
|---|---|
| TO01 | Xây dựng kiến trúc Multi-Agent có khả năng mở rộng. |
| TO02 | Xây dựng cơ chế điều phối tác tử thích nghi. |
| TO03 | Tích hợp các công cụ toán học thông qua giao diện chuẩn hóa. |
| TO04 | Xây dựng hệ thống truy xuất tri thức toán học. |
| TO05 | Quản lý trạng thái và ngữ cảnh trong quá trình suy luận. |
| TO06 | Theo dõi, ghi nhận và phân tích quá trình thực thi của các Agent. |
| TO07 | Xây dựng pipeline đánh giá tự động và có khả năng tái lập thực nghiệm. |
| TO08 | Cho phép thay thế mô hình AI mà không phải thiết kế lại toàn bộ hệ thống. |

## 4. Đối tượng sử dụng

### 4.1. Các nhóm người dùng

**U01 — Học sinh**

- Gửi đề toán bằng văn bản hoặc hình ảnh.
- Nhận lời giải từng bước.
- Tìm hiểu công thức và định lý được áp dụng.

**U02 — Giáo viên và gia sư**

- Tham khảo phương pháp giải.
- Kiểm tra tính chính xác của lời giải.
- Sử dụng kết quả để hỗ trợ giảng dạy.

**U03 — Nhà phát triển phần mềm**

- Tích hợp MATHK Core vào ứng dụng khác.
- Mở rộng công cụ và năng lực suy luận.
- Sử dụng API hoặc SDK của hệ thống trong tương lai.

**U04 — Nhà nghiên cứu AI**

- Thực hiện benchmark.
- So sánh mô hình và kiến trúc Agent.
- Phân tích lỗi, chi phí và hiệu quả suy luận.
- Tái lập kết quả thực nghiệm.

### 4.2. Thứ tự ưu tiên

| Đối tượng | Ưu tiên | Giai đoạn |
|---|---|---|
| U01 — Học sinh | P0 | MVP |
| U02 — Giáo viên, gia sư | P1 | MVP hỗ trợ cơ bản |
| U03 — Nhà phát triển | P1 | MVP hỗ trợ cơ bản |
| U04 — Nhà nghiên cứu | P0 | MVP |

P0: Ưu tiên bắt buộc.

P1: Ưu tiên thứ cấp.

### 4.3. Định hướng phục vụ người dùng

Các nhóm người dùng sử dụng chung năng lực suy luận của MATHK Core thông qua các giao diện phù hợp như giao diện giải toán, giao diện tích hợp và môi trường thực nghiệm.

MVP không tập trung vào quản lý lớp học, quản lý điểm số, phân quyền giáo viên hay cá nhân hóa lộ trình học tập.

## 5. Phạm vi bài toán

### 5.1. Phạm vi toán học

**Phương án C — General-purpose Mathematical Reasoning Engine.**

- Thiết kế hệ thống suy luận toán học theo hướng tổng quát.
- MVP tập trung vào chương trình toán THCS từ lớp 6 đến lớp 9.
- Benchmark và thực nghiệm ban đầu tập trung vào phạm vi toán THCS.
- Kiến trúc cốt lõi không bị giới hạn bởi một cấp học cụ thể.
- Hướng tới khả năng mở rộng sang toán THPT và các miền toán học khác trong tương lai.

### 5.2. Phạm vi đa phương thức

**Level 2 — Multimodal Reasoning.**

MATHK không chỉ đọc chữ mà còn hiểu hình học, đồ thị, ký hiệu góc, quan hệ song song, vuông góc và các dữ kiện trực quan. Hệ thống kết hợp thông tin hình ảnh với văn bản để suy luận.

Các năng lực nằm trong phạm vi:

- Tiếp nhận đề toán dưới dạng văn bản, hình ảnh hoặc kết hợp cả hai.
- Nhận diện nội dung, biểu thức và ký hiệu toán học.
- Nhận diện các đối tượng hình học.
- Hiểu các ký hiệu góc, độ dài và quan hệ hình học.
- Khai thác thông tin từ đồ thị và sơ đồ toán học.
- Kết hợp dữ kiện trực quan với giả thiết bằng văn bản.
- Sử dụng thông tin đa phương thức trong quá trình suy luận và giải toán.

Level 1 (Multimodal Input) là năng lực nền tảng nhưng không phải mục tiêu cuối cùng của hệ thống.

Level 3 (Multimodal Reasoning & Generation) chưa thuộc phạm vi đã cam kết của MVP.

## 6. Yêu cầu chức năng (FR)

### 6.1. Quy ước mức độ ưu tiên

- P0: Bắt buộc trong MVP.
- P1: Hướng tới triển khai trong MVP, sau khi hoàn thành P0.
- P2: Phát triển trong giai đoạn mở rộng.

### 6.2. FR01 — Tiếp nhận và xử lý đầu vào

| ID | Yêu cầu chức năng | Ưu tiên |
|---|---|---|
| FR01.01 | Tiếp nhận đề toán dạng văn bản. | P0 |
| FR01.02 | Hỗ trợ biểu thức toán học và LaTeX. | P0 |
| FR01.03 | Tiếp nhận đề toán dạng hình ảnh. | P0 |
| FR01.04 | Tiếp nhận kết hợp văn bản và hình ảnh. | P0 |
| FR01.05 | Hỗ trợ nhiều hình ảnh trong một bài toán. | P0 |
| FR01.06 | Kiểm tra tính hợp lệ của đầu vào. | P0 |
| FR01.07 | Cho phép người dùng bổ sung hoặc chỉnh sửa dữ kiện. | P0 |
| FR01.08 | Hỗ trợ nhận dạng đề toán viết tay. | P1 |
| FR01.09 | Tiếp nhận tài liệu PDF. | P1 |
| FR01.10 | Phân tách nhiều bài toán trong cùng tài liệu. | P1 |

#### Đơn vị xử lý

MATHK Core sử dụng Single-problem Reasoning làm đơn vị suy luận cơ bản.

- Mỗi phiên suy luận xử lý một bài toán logic.
- Một bài toán có thể chứa nhiều câu hỏi nhỏ có liên quan.
- Hệ thống hỗ trợ tiếp nhận tài liệu chứa nhiều bài toán thông qua chức năng phân tách đầu vào.
- Chữ viết tay, PDF và phân tách bài toán được định hướng triển khai ngay trong giai đoạn MVP.

### 6.3. FR02 — Nhận thức đa phương thức

| ID | Yêu cầu chức năng | Ưu tiên |
|---|---|---|
| FR02.01 | Trích xuất nội dung văn bản từ hình ảnh. | P0 |
| FR02.02 | Nhận diện công thức và ký hiệu toán học. | P0 |
| FR02.03 | Nhận diện các đối tượng hình học. | P0 |
| FR02.04 | Nhận diện các quan hệ hình học. | P0 |
| FR02.05 | Trích xuất dữ kiện từ đồ thị, biểu đồ và bảng số liệu. | P0 |
| FR02.06 | Liên kết nhãn, ký hiệu và giá trị với đối tượng tương ứng. | P0 |
| FR02.07 | Kết hợp thông tin văn bản và hình ảnh. | P0 |
| FR02.08 | Chuẩn hóa dữ kiện thành biểu diễn toán học có cấu trúc. | P0 |
| FR02.09 | Xác định nguồn gốc của từng dữ kiện. | P0 |
| FR02.10 | Phát hiện dữ kiện trực quan không rõ ràng hoặc mâu thuẫn. | P0 |
| FR02.11 | Liên kết dữ kiện giữa nhiều hình ảnh hoặc nhiều trang tài liệu. | P1 |

#### Biểu diễn thông tin

Sử dụng Hybrid Representation, kết hợp:

- Original Context: văn bản và hình ảnh gốc.
- Structured Context: các đối tượng, dữ kiện, quan hệ, mục tiêu và thông tin chưa chắc chắn được biểu diễn có cấu trúc.

Các thành phần suy luận có thể sử dụng dữ kiện có cấu trúc và đối chiếu lại thông tin gốc khi cần thiết.

#### Nguyên tắc nhận thức

- Phân biệt dữ kiện được cho, dữ kiện quan sát và dữ kiện suy ra.
- Không khẳng định quan hệ hình học chỉ dựa trên hình dáng hoặc tỷ lệ minh họa.
- Không tự bổ sung giả thiết toán học thiếu căn cứ.
- Bảo toàn nguồn gốc của dữ kiện để hỗ trợ kiểm chứng.

### 6.4. FR03 — Phân tích và lập kế hoạch

| ID | Yêu cầu chức năng | Ưu tiên |
|---|---|---|
| FR03.01 | Xác định mục tiêu và yêu cầu của bài toán. | P0 |
| FR03.02 | Phân loại bài toán theo miền kiến thức. | P0 |
| FR03.03 | Ước lượng độ phức tạp của bài toán. | P0 |
| FR03.04 | Phân rã bài toán phức tạp thành các nhiệm vụ nhỏ. | P0 |
| FR03.05 | Xác định quan hệ phụ thuộc giữa các nhiệm vụ. | P0 |
| FR03.06 | Xác định kiến thức, công thức và định lý cần thiết. | P0 |
| FR03.07 | Xác định nhu cầu sử dụng công cụ toán học. | P0 |
| FR03.08 | Xây dựng kế hoạch giải toán có cấu trúc. | P0 |
| FR03.09 | Điều chỉnh kế hoạch khi phát hiện lỗi hoặc hướng giải không phù hợp. | P0 |
| FR03.10 | Đề xuất và so sánh nhiều phương án giải. | P1 |

#### Phân loại bài toán

Hệ thống phân tích bài toán theo các chiều:

- Mathematical Domain: miền kiến thức toán học.
- Task Type: loại nhiệm vụ cần giải quyết.
- Input Modality: phương thức đầu vào.
- Complexity: mức độ phức tạp.
- Knowledge Requirement: nhu cầu sử dụng tri thức.
- Tool Requirement: nhu cầu sử dụng công cụ.
- Data Sufficiency: mức độ đầy đủ của dữ kiện.

#### Chiến lược lập kế hoạch

Áp dụng Adaptive Planning, lựa chọn mức độ lập kế hoạch phù hợp với đặc điểm và độ phức tạp của bài toán.

- Bài toán đơn giản: sử dụng Direct Planning hoặc Light Planning.
- Bài toán phức tạp: sử dụng Structured Planning, phân rã nhiệm vụ và xác định quan hệ phụ thuộc.
- Khi phát hiện lỗi: cho phép Replanning trong giới hạn tài nguyên.

#### Lộ trình triển khai

1. Static Planning: xây dựng pipeline lập kế hoạch và thực thi cơ bản.
2. Bounded Replanning: hỗ trợ điều chỉnh kế hoạch với số vòng lặp giới hạn.
3. Adaptive Planning: lựa chọn chiến lược lập kế hoạch dựa trên đặc điểm bài toán.

Không xây dựng bộ nhớ tái sử dụng chiến lược giải toán trong phạm vi hiện tại.

Không yêu cầu huấn luyện mô hình Planner riêng hoặc sử dụng Reinforcement Learning để hoàn thành MVP.

### 6.5. FR04 — Truy xuất tri thức toán học

| ID | Yêu cầu chức năng | Ưu tiên |
|---|---|---|
| FR04.01 | Xây dựng và quản lý kho tri thức toán học. | P0 |
| FR04.02 | Chuẩn hóa tri thức thành các đơn vị có cấu trúc và metadata. | P0 |
| FR04.03 | Truy xuất định nghĩa, công thức, định lý và phương pháp giải. | P0 |
| FR04.04 | Xây dựng truy vấn dựa trên bài toán và nhiệm vụ hiện tại. | P0 |
| FR04.05 | Lọc tri thức theo miền kiến thức và phạm vi chương trình. | P0 |
| FR04.06 | Đánh giá mức độ liên quan của tri thức truy xuất. | P0 |
| FR04.07 | Cung cấp điều kiện áp dụng của tri thức toán học. | P0 |
| FR04.08 | Truy xuất bổ sung hoặc điều chỉnh truy vấn khi cần thiết. | P0 |
| FR04.09 | Cung cấp nguồn tham chiếu của tri thức được sử dụng. | P0 |
| FR04.10 | Cho phép cập nhật và mở rộng kho tri thức mà không huấn luyện lại LLM. | P0 |
| FR04.11 | Kết hợp truy xuất đơn vị tri thức với đoạn văn bản tài liệu gốc. | P1 |
| FR04.12 | Phát hiện và cảnh báo tri thức có dấu hiệu mâu thuẫn. | P1 |

#### Biểu diễn tri thức

Áp dụng Hybrid Mathematical Knowledge:

- Structured Knowledge Units: đơn vị tri thức có cấu trúc.
- Original Knowledge Context: nội dung từ tài liệu gốc.

Ưu tiên triển khai Structured Knowledge Units trước, bảo toàn liên kết với nguồn gốc của tri thức. Truy xuất trực tiếp đoạn văn bản tài liệu gốc thuộc P1.

Đơn vị tri thức có thể bao gồm tên, loại, miền toán học, cấp học, nội dung, công thức, điều kiện áp dụng và nguồn tham chiếu.

Không bắt buộc xây dựng hai hệ thống RAG độc lập.

#### Chiến lược Agentic RAG

- Truy xuất tri thức theo nhu cầu của bài toán và từng nhiệm vụ.
- Đánh giá mức độ liên quan và đầy đủ của kết quả truy xuất.
- Điều chỉnh truy vấn hoặc truy xuất bổ sung trong giới hạn xác định.
- Cho phép bỏ qua RAG khi không cần thiết.
- Kiểm tra điều kiện áp dụng của công thức và định lý trước khi sử dụng.

#### Phạm vi triển khai

Ưu tiên tri thức toán THCS bằng tiếng Việt, tập trung vào các chủ đề đại diện.

Quy mô 200–500 đơn vị tri thức là ước lượng ban đầu, không phải tiêu chí nghiệm thu.

BM25 và Dense Retrieval là các hướng baseline dự kiến khảo sát. Không bắt buộc fine-tuning embedding, xây dựng Knowledge Graph hoặc tích hợp Web Search Agent trong MVP.

### 6.6. FR05 — Suy luận và sử dụng công cụ

| ID | Yêu cầu chức năng | Ưu tiên |
|---|---|---|
| FR05.01 | Thực hiện suy luận dựa trên dữ kiện và kế hoạch giải toán. | P0 |
| FR05.02 | Giải quyết bài toán nhiều bước và nhiều nhiệm vụ phụ thuộc. | P0 |
| FR05.03 | Áp dụng định nghĩa, công thức và định lý phù hợp. | P0 |
| FR05.04 | Xác định khi nào cần sử dụng công cụ toán học. | P0 |
| FR05.05 | Lựa chọn công cụ phù hợp với nhiệm vụ. | P0 |
| FR05.06 | Chuyển đổi yêu cầu toán học thành tham số đầu vào của công cụ. | P0 |
| FR05.07 | Thực thi công cụ và tiếp nhận kết quả có cấu trúc. | P0 |
| FR05.08 | Tích hợp kết quả công cụ vào lời giải. | P0 |
| FR05.09 | Xử lý lỗi, timeout và kết quả không hợp lệ từ công cụ. | P0 |
| FR05.10 | Lưu trữ kết quả trung gian và quan hệ phụ thuộc giữa các bước giải. | P0 |
| FR05.11 | Cung cấp lời giải có cấu trúc để hỗ trợ kiểm chứng. | P0 |
| FR05.12 | Hỗ trợ đăng ký và mở rộng tập công cụ toán học. | P0 |
| FR05.13 | Phối hợp nhiều công cụ trong cùng một nhiệm vụ suy luận. | P0 |
| FR05.14 | Xây dựng nhiều lời giải bằng các phương pháp khác nhau. | P1 |

#### Neuro-Symbolic Reasoning

Kết hợp:

- Neural Reasoning: LLM hiểu bài toán, lựa chọn phương pháp, suy luận logic và diễn giải kết quả.
- Symbolic Computation: thực hiện các phép tính và biến đổi toán học bằng công cụ.

SymPy và Calculator là các công cụ chính trong MVP.

#### Phạm vi công cụ

| Công cụ logic | Ưu tiên |
|---|---|
| calculate | P0 |
| simplify | P0 |
| expand | P0 |
| factor | P0 |
| solve_equation | P0 |
| solve_system | P0 |
| solve_inequality | P0 |
| check_equivalence | P0 |
| substitute | P0 |
| compute_statistics | P1 |
| geometry_compute | P1 |

#### Tích hợp công cụ

Sử dụng phương án A — Direct Function Calling trong MVP.

- Quản lý công cụ thông qua Tool Registry.
- Chuẩn hóa giao diện đầu vào và đầu ra.
- Kiểm tra tham số trước khi thực thi.
- Giới hạn thời gian thực thi và xử lý ngoại lệ.
- Chỉ cho phép thực hiện các thao tác đã được đăng ký.
- Tách biệt logic toán học khỏi cơ chế tích hợp công cụ.

MCP được đưa sang giai đoạn mở rộng, không phải điều kiện hoàn thành MVP.

Không yêu cầu xây dựng hệ thống đại số máy tính riêng, hệ thống chứng minh hình học tổng quát, Formal Proof Engine hoặc hạ tầng thực thi công cụ phân tán.

Không cho phép Agent thực thi mã Python tùy ý.

### 6.7. FR06 — Kiểm chứng và tự sửa lỗi

| ID | Yêu cầu chức năng | Ưu tiên |
|---|---|---|
| FR06.01 | Kiểm chứng sự nhất quán giữa lời giải và dữ kiện đầu vào. | P0 |
| FR06.02 | Kiểm chứng điều kiện áp dụng kiến thức toán học. | P0 |
| FR06.03 | Kiểm chứng tính hợp lệ của các bước lập luận. | P0 |
| FR06.04 | Kiểm chứng phép tính và biến đổi bằng công cụ toán học khi có thể. | P0 |
| FR06.05 | Kiểm chứng tính đúng và đầy đủ của đáp án. | P0 |
| FR06.06 | Phát hiện và phân loại lỗi. | P0 |
| FR06.07 | Xác định bước giải hoặc dữ kiện gây lỗi khi có thể. | P0 |
| FR06.08 | Cung cấp phản hồi có cấu trúc để hỗ trợ sửa lỗi. | P0 |
| FR06.09 | Thực hiện sửa lỗi hoặc lập lại kế hoạch giải toán. | P0 |
| FR06.10 | Kiểm chứng lại lời giải sau khi sửa. | P0 |
| FR06.11 | Giới hạn số vòng lặp kiểm chứng và sửa lỗi. | P0 |
| FR06.12 | Lưu lại các phiên bản lời giải và kết quả kiểm chứng. | P0 |
| FR06.13 | Hỗ trợ kiểm chứng bằng phương pháp giải độc lập. | P1 |
| FR06.14 | Hỗ trợ tiếp nhận, chuẩn hóa và kiểm chứng lời giải do người dùng cung cấp, báo cáo lỗi và phạm vi kiểm chứng. | P1 |

#### Phạm vi kiểm chứng

| Lớp | Trách nhiệm |
|---|---|
| V1 — Input Verification | Kiểm chứng dữ kiện đầu vào. |
| V2 — Knowledge Verification | Kiểm chứng công thức, định lý và điều kiện áp dụng. |
| V3 — Reasoning Verification | Kiểm chứng lập luận và biến đổi toán học. |
| V4 — Computational Verification | Kiểm chứng phép tính bằng công cụ. |
| V5 — Answer Verification | Kiểm chứng tính đúng và đầy đủ của đáp án. |

Năm lớp kiểm chứng là các nhóm trách nhiệm, không yêu cầu năm Agent độc lập.

#### Hybrid Verification

Kết hợp LLM-based Verification và Symbolic Verification.

Ưu tiên công cụ toán học đối với những nội dung có thể kiểm chứng bằng thuật toán. Sử dụng LLM đối với các nhiệm vụ cần hiểu ngữ cảnh, lập luận hoặc đánh giá tính đầy đủ.

Kết quả đánh giá của LLM không tương đương với chứng minh hình thức bằng máy.

#### Adaptive Correction

Lựa chọn phạm vi và phương pháp sửa lỗi dựa trên nguyên nhân, vị trí và mức độ ảnh hưởng.

| Lỗi | Hành động |
|---|---|
| Sai phép tính | Tính lại bằng công cụ. |
| Sai biến đổi | Sửa bước sai và các bước phụ thuộc. |
| Sai công thức | Truy xuất lại tri thức. |
| Sai hướng giải | Replanning. |
| Đọc sai đầu vào | Đối chiếu lại dữ kiện gốc. |
| Thiếu dữ kiện | Yêu cầu làm rõ. |
| Không thể xác minh | Báo cáo trạng thái chưa kiểm chứng. |

Lời giải sau khi sửa phải được kiểm chứng lại. Số vòng lặp được giới hạn và có thể cấu hình.

#### Trạng thái kiểm chứng

| Trạng thái | Ý nghĩa |
|---|---|
| VERIFIED | Các nội dung cần kiểm chứng đã vượt qua những kiểm tra phù hợp. |
| PARTIALLY_VERIFIED | Chỉ kiểm chứng được một phần lời giải. |
| UNVERIFIED | Chưa đủ khả năng hoặc căn cứ xác minh. |
| FAILED | Phát hiện lỗi chưa được khắc phục. |

Trạng thái kiểm chứng phải đi kèm phương pháp và phạm vi kiểm chứng.

MVP ưu tiên một Verifier Agent chính, tái sử dụng bộ công cụ FR05. Không bắt buộc huấn luyện Verifier riêng, triển khai Formal Proof Engine hoặc Multi-Agent Debate.

### 6.8. FR07 — Điều phối tác tử thích nghi

| ID | Yêu cầu chức năng | Ưu tiên |
|---|---|---|
| FR07.01 | Quản lý danh mục Agent và năng lực của từng Agent. | P0 |
| FR07.02 | Lựa chọn Agent dựa trên đặc điểm bài toán. | P0 |
| FR07.03 | Xác định thứ tự thực thi và quan hệ phụ thuộc. | P0 |
| FR07.04 | Cho phép bỏ qua các thành phần không cần thiết. | P0 |
| FR07.05 | Quản lý trạng thái thực thi dùng chung. | P0 |
| FR07.06 | Điều chỉnh tuyến xử lý trong quá trình suy luận. | P0 |
| FR07.07 | Điều phối truy xuất tri thức và sử dụng công cụ theo nhu cầu. | P0 |
| FR07.08 | Điều phối quá trình kiểm chứng và sửa lỗi. | P0 |
| FR07.09 | Nâng mức độ suy luận khi chiến lược hiện tại không hiệu quả. | P0 |
| FR07.10 | Kiểm soát số lượt gọi LLM, công cụ và vòng lặp. | P0 |
| FR07.11 | Xác định điều kiện kết thúc quá trình suy luận. | P0 |
| FR07.12 | Lưu lại tuyến xử lý và căn cứ ra quyết định điều phối. | P0 |
| FR07.13 | Hỗ trợ cấu hình nhiều chiến lược điều phối để thực nghiệm. | P0 |
| FR07.14 | Thực thi song song các nhiệm vụ độc lập. | P1 |

#### Hybrid Adaptive Routing

Kết hợp Rule-based Routing và LLM-based Routing.

- Ưu tiên sử dụng quy tắc xác định khi đủ căn cứ.
- Sử dụng quyết định của LLM đối với tình huống cần khả năng thích nghi cao hơn.
- Kiểm tra tính hợp lệ của hành động trước khi thực thi.
- Không bắt buộc mỗi quyết định điều phối phải phát sinh một lượt gọi LLM riêng.

Routing dựa trên đặc điểm bài toán, trạng thái thực thi, kết quả kiểm chứng và tài nguyên còn lại.

#### Shared Structured State

Các Agent phối hợp thông qua trạng thái dùng chung có cấu trúc, bao gồm:

- Problem Context.
- Execution Plan.
- Retrieved Knowledge.
- Intermediate Results.
- Verification Feedback.
- Resource Usage.

Agent đọc và cập nhật các phần trạng thái liên quan đến nhiệm vụ của mình.

Không yêu cầu sử dụng Redis, Kafka hoặc Message Queue trong MVP.

#### Cơ chế Escalation

| Mức | Chiến lược |
|---|---|
| L1 — Lightweight Reasoning | Suy luận trực tiếp, sử dụng công cụ và kiểm chứng cơ bản. |
| L2 — Structured Reasoning | Lập kế hoạch chi tiết, phân rã nhiệm vụ và kích hoạt các năng lực cần thiết. |
| L3 — Corrective Reasoning | Phân tích lỗi, sửa lời giải, truy xuất bổ sung hoặc lập lại kế hoạch. |

Các mức suy luận không bắt buộc sử dụng các LLM khác nhau.

Khi vượt quá giới hạn tài nguyên hoặc không thể tiếp tục suy luận đáng tin cậy, chuyển sang cơ chế xử lý sự không chắc chắn của FR08.

#### Lộ trình triển khai

1. Static Multi-Agent Pipeline.
2. Rule-based Routing.
3. State-aware Routing.
4. Hybrid Adaptive Routing.
5. Evaluation & Optimization.

Không yêu cầu Reinforcement Learning Router, huấn luyện mô hình Router riêng hoặc hệ thống Agent phân tán.

### 6.9. FR08 — Nhận thức và xử lý sự không chắc chắn

| ID | Yêu cầu chức năng | Ưu tiên |
|---|---|---|
| FR08.01 | Phát hiện và phân loại các nguồn gây không chắc chắn. | P0 |
| FR08.02 | Phát hiện dữ kiện thiếu hoặc không đầy đủ. | P0 |
| FR08.03 | Phát hiện dữ kiện mơ hồ hoặc mâu thuẫn. | P0 |
| FR08.04 | Xác định dữ kiện hoặc bước giải chưa chắc chắn. | P0 |
| FR08.05 | Đánh giá mức độ ảnh hưởng của sự không chắc chắn đến lời giải. | P0 |
| FR08.06 | Tổng hợp các tín hiệu đánh giá từ những thành phần liên quan. | P0 |
| FR08.07 | Tự xử lý sự không chắc chắn khi có đủ khả năng và tài nguyên. | P0 |
| FR08.08 | Yêu cầu người dùng làm rõ hoặc bổ sung dữ kiện. | P0 |
| FR08.09 | Tiếp tục suy luận sau khi người dùng xác nhận dữ kiện. | P0 |
| FR08.10 | Cung cấp lời giải có điều kiện và nêu rõ giả thiết bổ sung. | P0 |
| FR08.11 | Cho phép từ chối đưa ra kết luận khi không đủ căn cứ. | P0 |
| FR08.12 | Phân biệt giới hạn của hệ thống với tính không hợp lệ của bài toán. | P0 |
| FR08.13 | Cung cấp trạng thái bất định và căn cứ đánh giá. | P0 |
| FR08.14 | Lưu lại quá trình phát hiện và xử lý sự không chắc chắn. | P0 |
| FR08.15 | Đánh giá và hiệu chỉnh độ tin cậy định lượng thông qua thực nghiệm. | P1 |

#### Phân loại sự không chắc chắn

| ID | Loại |
|---|---|
| UC01 | Input Uncertainty |
| UC02 | Semantic Ambiguity |
| UC03 | Insufficient Data |
| UC04 | Contradictory Data |
| UC05 | Reasoning Uncertainty |
| UC06 | Verification Uncertainty |

Phân biệt các vấn đề thuộc về dữ kiện bài toán và các giới hạn trong khả năng của hệ thống.

#### Evidence-based Hybrid Detection

Kết hợp quy tắc xác định, đánh giá bằng LLM và các tín hiệu từ những thành phần hiện có.

Ưu tiên đánh giá dựa trên căn cứ và trạng thái định tính. Không biểu diễn mức độ tự tin của LLM thành xác suất đúng nếu chưa thực hiện hiệu chỉnh phù hợp.

Không bắt buộc xây dựng Uncertainty Agent độc lập.

#### Cơ chế xử lý

| Hành động | Mục đích |
|---|---|
| CONTINUE | Tiếp tục khi bất định không ảnh hưởng đến kết quả. |
| SELF_RESOLVE | Tự xử lý thông qua truy xuất, đối chiếu, tính toán hoặc lập lại kế hoạch. |
| CLARIFY | Yêu cầu người dùng xác nhận hoặc bổ sung dữ kiện. |
| CONDITIONAL_ANSWER | Cung cấp lời giải theo giả thiết được nêu rõ. |
| ABSTAIN | Không đưa ra kết luận khi không đủ căn cứ. |

#### Human-in-the-loop

Cho phép người dùng tham gia xác nhận và bổ sung dữ kiện.

Hệ thống bảo toàn trạng thái xử lý có liên quan và tiếp tục suy luận sau khi nhận được thông tin bổ sung.

Không yêu cầu hệ thống hội thoại dài hạn hoặc quản lý tài khoản để triển khai Human-in-the-loop trong MVP.

### 6.10. FR09 — Tổng hợp và xuất kết quả

| ID | Yêu cầu chức năng | Ưu tiên |
|---|---|---|
| FR09.01 | Tổng hợp kết quả từ các thành phần suy luận. | P0 |
| FR09.02 | Cung cấp kết quả toán học có cấu trúc thống nhất. | P0 |
| FR09.03 | Cung cấp đáp án cuối cùng khi đủ căn cứ. | P0 |
| FR09.04 | Cung cấp lời giải từng bước có căn cứ toán học. | P0 |
| FR09.05 | Hiển thị biểu thức toán học bằng LaTeX. | P0 |
| FR09.06 | Cung cấp nguồn tham chiếu của tri thức được sử dụng. | P0 |
| FR09.07 | Cung cấp trạng thái, phương pháp và phạm vi kiểm chứng. | P0 |
| FR09.08 | Hiển thị các giả thiết, điều kiện và thông tin chưa chắc chắn. | P0 |
| FR09.09 | Hỗ trợ nhiều mức độ chi tiết của kết quả. | P0 |
| FR09.10 | Hỗ trợ đầu ra có thể xử lý bằng chương trình. | P0 |
| FR09.11 | Bảo đảm tính nhất quán giữa các định dạng đầu ra. | P0 |
| FR09.12 | Cung cấp bản ghi thực thi phục vụ phân tích và nghiên cứu. | P0 |
| FR09.13 | Diễn giải lời giải phù hợp với trình độ người dùng. | P1 |
| FR09.14 | Hiển thị nhiều phương pháp giải khác nhau nếu có. | P1 |
| FR09.15 | Xuất lời giải dưới dạng PDF hoặc tài liệu. | P2 |

#### Structured Solution

Áp dụng nguyên tắc Single Source of Truth.

Sử dụng một kết quả toán học có cấu trúc thống nhất làm nguồn cho các định dạng đầu ra.

Kết quả bao gồm những thành phần liên quan:

- Problem Summary.
- Given Facts.
- Objectives.
- Assumptions.
- Solution Steps.
- Knowledge References.
- Computation Results.
- Final Answer.
- Verification Status.
- Uncertainty Report.

Hỗ trợ đầu ra dành cho con người thông qua Markdown và LaTeX, đồng thời cung cấp đầu ra có cấu trúc cho chương trình và benchmark.

#### Chế độ hiển thị

| Chế độ | Mục đích | Ưu tiên |
|---|---|---|
| Quick Answer | Cung cấp đáp án ngắn gọn. | P0 |
| Detailed Solution | Giải thích lời giải từng bước. | P0 |
| Technical Output | Cung cấp dữ liệu kỹ thuật và bản ghi thực thi. | P0 |

Technical Output bao gồm thao tác, dữ kiện, công cụ, kết quả và căn cứ kiểm chứng mà hệ thống ghi nhận, không yêu cầu suy nghĩ nội bộ của LLM.

#### Hybrid Output Formatting

Ưu tiên định dạng kết quả bằng code và template.

Sử dụng LLM để diễn giải bổ sung khi cần thiết, thuộc phạm vi P1.

Không bắt buộc xây dựng Synthesis Agent riêng.

#### Nguyên tắc xuất kết quả

- Mathematical Consistency: bảo toàn nội dung toán học khi định dạng.
- Grounded Explanation: không tạo kiến thức hoặc nguồn tham chiếu thiếu căn cứ.
- Verification Preservation: bảo toàn trạng thái kiểm chứng.
- Uncertainty Transparency: công khai thông tin chưa chắc chắn và giả thiết bổ sung.
- Curriculum Awareness: ưu tiên phương pháp phù hợp với phạm vi chương trình.

Không tự ý thay đổi đáp án hoặc biểu thức toán học đã được kiểm chứng. Nếu nội dung toán học thay đổi, cần kiểm chứng lại.

Sinh hình vẽ toán học mới, video lời giải, Voice Tutor và hệ thống quản lý học tập không thuộc MVP hiện tại.

### 6.11. FR10 — Thực nghiệm và theo dõi hệ thống

| ID | Yêu cầu chức năng | Ưu tiên |
|---|---|---|
| FR10.01 | Quản lý và nạp tập dữ liệu benchmark. | P0 |
| FR10.02 | Hỗ trợ đánh giá bài toán theo miền kiến thức, độ khó và phương thức đầu vào. | P0 |
| FR10.03 | Thực thi benchmark tự động trên nhiều bài toán. | P0 |
| FR10.04 | Đánh giá tự động đáp án khi có phương pháp kiểm tra phù hợp. | P0 |
| FR10.05 | Hỗ trợ đánh giá lời giải bằng rubric và kiểm tra thủ công. | P0 |
| FR10.06 | Cấu hình các mô hình, Agent và chiến lược xử lý khác nhau. | P0 |
| FR10.07 | Hỗ trợ so sánh baseline và thực hiện Ablation Study. | P0 |
| FR10.08 | Ghi nhận quá trình thực thi của các Agent và công cụ. | P0 |
| FR10.09 | Theo dõi số lượt gọi mô hình, công cụ và lượng token tiêu thụ. | P0 |
| FR10.10 | Theo dõi thời gian thực thi và chi phí ước tính. | P0 |
| FR10.11 | Ghi nhận lỗi và kết quả kiểm chứng, sửa lỗi. | P0 |
| FR10.12 | Lưu cấu hình, phiên bản và kết quả thực nghiệm. | P0 |
| FR10.13 | Tổng hợp kết quả theo các chỉ số đánh giá. | P0 |
| FR10.14 | Xuất dữ liệu thực nghiệm dưới dạng JSON hoặc CSV. | P0 |
| FR10.15 | Hỗ trợ checkpoint và tiếp tục benchmark bị gián đoạn. | P0 |
| FR10.16 | Trực quan hóa và so sánh kết quả thực nghiệm. | P1 |
| FR10.17 | Hỗ trợ LLM-as-a-Judge đối với những bài toán khó đánh giá tự động. | P1 |

#### Benchmarking

Quản lý và thực thi benchmark trên các nhóm bài toán thuộc phạm vi hỗ trợ của MATHK.

Tập dữ liệu benchmark cần bảo toàn nội dung bài toán, đáp án tham chiếu, nguồn dữ liệu và metadata phục vụ phân tích kết quả.

Phương pháp đánh giá được lựa chọn phù hợp với từng dạng bài toán:

- So sánh giá trị và biểu thức toán học.
- Kiểm tra tính tương đương bằng công cụ toán học.
- So sánh tập nghiệm và điều kiện xác định.
- Đánh giá lời giải bằng rubric và kiểm tra thủ công.
- Đánh giá trạng thái xử lý đối với bài toán thiếu hoặc mâu thuẫn dữ kiện.

Ưu tiên đánh giá tự động bằng thuật toán xác định khi có thể. LLM-as-a-Judge thuộc phạm vi P1.

#### Research Observability

Ghi nhận quá trình thực thi thông qua Execution Trace, bao gồm:

- Agent và trạng thái thực thi.
- Tuyến xử lý và quyết định điều phối.
- Lượt gọi LLM và lượng token tiêu thụ.
- Công cụ, tham số và kết quả thực thi.
- Truy vấn và kết quả truy xuất tri thức.
- Kết quả kiểm chứng và các lỗi được phát hiện.
- Quá trình sửa lỗi.
- Thời gian thực thi và chi phí ước tính.

Execution Trace phản ánh các sự kiện thực thi quan sát được, không yêu cầu truy xuất suy nghĩ nội bộ của LLM.

#### Experimentation

Cho phép cấu hình các thành phần và chiến lược xử lý phục vụ thực nghiệm mà không phải thay đổi logic cốt lõi của hệ thống.

Hỗ trợ so sánh baseline và Ablation Study tương ứng với các mục tiêu nghiên cứu RO01–RO07.

| Mục tiêu | Hướng thực nghiệm |
|---|---|
| RO01 | Single-Agent và Multi-Agent. |
| RO02 | Có và không sử dụng công cụ toán học. |
| RO03 | No RAG, Static RAG và Agentic RAG. |
| RO04 | Các phương pháp kiểm chứng và tự sửa lỗi. |
| RO05 | Static, Rule-based và Hybrid Adaptive Routing. |
| RO06 | Text/OCR-only và Multimodal Reasoning. |
| RO07 | Có và không có cơ chế xử lý sự không chắc chắn. |

Không bắt buộc thực nghiệm trên toàn bộ tổ hợp cấu hình có thể có.

#### Các nhóm chỉ số đánh giá

| Nhóm | Chỉ số dự kiến |
|---|---|
| Mathematical Quality | Answer Accuracy, Solution Correctness. |
| Retrieval Quality | Recall@K, Precision@K, MRR. |
| Verification Quality | Error Detection F1, Correction Success Rate. |
| Uncertainty Quality | Detection F1, Coverage, False Abstention Rate. |
| Efficiency | Latency, Token Consumption, API Calls, Cost per Problem. |

Phương pháp tính, điều kiện áp dụng và ngưỡng đánh giá cụ thể được xác định trong tài liệu Evaluation.

Các chỉ số truy xuất tri thức yêu cầu dữ liệu tham chiếu phù hợp.

#### Reproducibility

Mỗi phiên thực nghiệm cần lưu các thông tin liên quan:

- Experiment ID.
- Dataset Version.
- Model Identifier và Model Parameters.
- Prompt Version.
- Knowledge Base Version.
- Agent Configuration.
- Git Commit.
- Execution Time.
- Evaluation Version.

Mục tiêu là bảo toàn điều kiện thực nghiệm và khả năng đối chiếu kết quả, không cam kết LLM API luôn tạo ra đầu ra giống hệt nhau.

#### Checkpoint & Resume

Hỗ trợ lưu tiến độ benchmark và tiếp tục thực nghiệm sau khi bị gián đoạn.

Hạn chế thực thi lại những bài toán đã hoàn thành hợp lệ trong cùng cấu hình thực nghiệm.

#### Phạm vi triển khai

- Ưu tiên hệ thống benchmarking, logging và đánh giá chạy local.
- Tự xây dựng các thành phần đánh giá cơ bản trước.
- Hỗ trợ xuất kết quả dưới dạng JSON hoặc CSV.
- Không bắt buộc tích hợp Langfuse, MLflow hoặc LangSmith trong MVP.
- Không yêu cầu hạ tầng benchmark phân tán hoặc giám sát hệ thống production theo thời gian thực.

Công nghệ lưu trữ, schema, quy mô benchmark và quy trình thực nghiệm chi tiết sẽ được xác định trong các tài liệu thiết kế liên quan.

## 7. Yêu cầu phi chức năng (Non-functional Requirements)

### 7.1. Các thuộc tính chất lượng

| ID | Quality Attribute | Ưu tiên |
|---|---|---|
| NFR01 | Mathematical Correctness | P0 |
| NFR02 | Reliability | P0 |
| NFR03 | Performance | P0 |
| NFR04 | Cost Efficiency | P0 |
| NFR05 | Modifiability | P0 |
| NFR06 | Extensibility | P0 |
| NFR07 | Reproducibility | P0 |
| NFR08 | Observability | P0 |
| NFR09 | Security & Privacy | P0 |
| NFR10 | Usability | P1 |
| NFR11 | Portability | P1 |
| NFR12 | Scalability | P1 |

Ưu tiên chất lượng toán học, độ tin cậy, hiệu quả suy luận và khả năng phục vụ nghiên cứu.

Security & Privacy là ràng buộc bắt buộc xuyên suốt hệ thống.

### 7.2. NFR01 — Tính đúng đắn toán học

| ID | Yêu cầu |
|---|---|
| NFR01.01 | Lời giải phải nhất quán với dữ kiện bài toán. |
| NFR01.02 | Công thức và định lý phải được sử dụng đúng điều kiện. |
| NFR01.03 | Kết quả tính toán phải được kiểm chứng bằng công cụ khi khả thi. |
| NFR01.04 | Không tự bổ sung giả thiết thiếu căn cứ. |
| NFR01.05 | Phải thể hiện rõ phạm vi kiểm chứng và giới hạn của lời giải. |
| NFR01.06 | Chất lượng toán học phải được đo lường thông qua benchmark. |

### 7.3. NFR02 — Độ tin cậy

| ID | Yêu cầu |
|---|---|
| NFR02.01 | Xử lý lỗi API, timeout và rate limit. |
| NFR02.02 | Không để lỗi của một thành phần làm mất toàn bộ kết quả thực thi đã lưu. |
| NFR02.03 | Phát hiện đầu ra không hợp lệ của Agent và công cụ. |
| NFR02.04 | Có cơ chế retry giới hạn và phục hồi phù hợp. |
| NFR02.05 | Không thực thi vòng lặp suy luận vô hạn. |
| NFR02.06 | Cung cấp trạng thái lỗi rõ ràng khi không thể hoàn thành nhiệm vụ. |

### 7.4. NFR03 — Hiệu năng

| ID | Yêu cầu |
|---|---|
| NFR03.01 | Hạn chế độ trễ phát sinh không cần thiết giữa các thành phần. |
| NFR03.02 | Hỗ trợ cấu hình timeout cho từng loại tác vụ. |
| NFR03.03 | Đo lường thời gian thực thi toàn hệ thống và từng thành phần. |
| NFR03.04 | Tránh thực thi lại các nhiệm vụ đã hoàn thành khi kết quả vẫn hợp lệ. |
| NFR03.05 | Đánh giá hiệu năng theo độ phức tạp của bài toán. |

### 7.5. NFR04 — Hiệu quả chi phí

| ID | Yêu cầu |
|---|---|
| NFR04.01 | Hạn chế các lượt gọi LLM không cần thiết. |
| NFR04.02 | Kiểm soát lượng token được truyền giữa các Agent. |
| NFR04.03 | Ưu tiên công cụ local đối với những nhiệm vụ tính toán phù hợp. |
| NFR04.04 | Cho phép cấu hình giới hạn tài nguyên cho mỗi phiên suy luận. |
| NFR04.05 | Theo dõi chi phí theo bài toán và phiên thực nghiệm. |
| NFR04.06 | Ưu tiên giải pháp không bắt buộc phát sinh chi phí hạ tầng thường xuyên. |

### 7.6. NFR05 — Khả năng sửa đổi

| ID | Yêu cầu |
|---|---|
| NFR05.01 | Các thành phần có trách nhiệm rõ ràng. |
| NFR05.02 | Hạn chế phụ thuộc trực tiếp giữa các Agent. |
| NFR05.03 | Cho phép thay thế mô hình LLM mà không thay đổi toàn bộ hệ thống. |
| NFR05.04 | Tách biệt prompt, configuration và logic nghiệp vụ. |
| NFR05.05 | Hỗ trợ kiểm thử độc lập các thành phần. |

### 7.7. NFR06 — Khả năng mở rộng chức năng

| ID | Yêu cầu |
|---|---|
| NFR06.01 | Cho phép bổ sung Agent mới. |
| NFR06.02 | Cho phép bổ sung công cụ toán học mới. |
| NFR06.03 | Cho phép mở rộng kho tri thức. |
| NFR06.04 | Cho phép bổ sung chiến lược Routing và Verification. |
| NFR06.05 | Không giới hạn kiến trúc cốt lõi vào chương trình THCS. |
| NFR06.06 | Cho phép bổ sung giao thức tích hợp như MCP mà vẫn tái sử dụng logic toán học. |

### 7.8. NFR07 — Khả năng tái lập thực nghiệm

| ID | Yêu cầu |
|---|---|
| NFR07.01 | Quản lý phiên bản tập dữ liệu, prompt và kho tri thức. |
| NFR07.02 | Lưu cấu hình mô hình và chiến lược thực nghiệm. |
| NFR07.03 | Bảo toàn kết quả thực nghiệm gốc. |
| NFR07.04 | Cho phép chạy lại benchmark theo cấu hình đã lưu. |
| NFR07.05 | Ghi nhận các yếu tố có thể ảnh hưởng đến khả năng tái lập. |

### 7.9. NFR08 — Khả năng theo dõi

| ID | Yêu cầu |
|---|---|
| NFR08.01 | Mỗi phiên suy luận có định danh riêng. |
| NFR08.02 | Có khả năng truy vết các sự kiện thực thi. |
| NFR08.03 | Ghi nhận lỗi theo thành phần và nhiệm vụ. |
| NFR08.04 | Ghi nhận metrics liên quan đến hiệu năng và tài nguyên. |
| NFR08.05 | Hỗ trợ phân tích kết quả trung gian và lỗi lan truyền. |

### 7.10. NFR09 — Bảo mật và quyền riêng tư

| ID | Yêu cầu |
|---|---|
| NFR09.01 | Không hard-code API Key trong mã nguồn. |
| NFR09.02 | Không lưu API Key hoặc thông tin xác thực trong log. |
| NFR09.03 | Kiểm tra và giới hạn dữ liệu đầu vào. |
| NFR09.04 | Không cho phép Agent thực thi mã tùy ý. |
| NFR09.05 | Kiểm tra tham số và giới hạn tài nguyên của công cụ. |
| NFR09.06 | Xử lý nội dung đầu vào và tài liệu truy xuất như dữ liệu không đáng tin cậy. |
| NFR09.07 | Hạn chế lưu trữ và truyền tải dữ liệu cá nhân không cần thiết. |
| NFR09.08 | Minh bạch việc gửi đề bài hoặc hình ảnh đến nhà cung cấp LLM bên ngoài. |

### 7.11. NFR10 — Khả năng sử dụng

| ID | Yêu cầu |
|---|---|
| NFR10.01 | Giao diện tiếp nhận đề toán đơn giản. |
| NFR10.02 | Hỗ trợ hiển thị công thức rõ ràng. |
| NFR10.03 | Thông báo lỗi bằng ngôn ngữ dễ hiểu. |
| NFR10.04 | Cho phép bổ sung dữ kiện khi hệ thống yêu cầu. |
| NFR10.05 | Phân biệt kết quả đã kiểm chứng và chưa kiểm chứng. |

### 7.12. NFR11 — Khả năng chuyển đổi môi trường

| ID | Yêu cầu |
|---|---|
| NFR11.01 | Hỗ trợ triển khai trên máy tính cá nhân. |
| NFR11.02 | Quản lý phiên bản thư viện và môi trường thực thi. |
| NFR11.03 | Hạn chế phụ thuộc vào phần cứng chuyên dụng. |
| NFR11.04 | Cung cấp tài liệu cấu hình và hướng dẫn khởi chạy. |

### 7.13. NFR12 — Khả năng mở rộng tải xử lý

| ID | Yêu cầu |
|---|---|
| NFR12.01 | Hỗ trợ benchmark trên nhiều bài toán. |
| NFR12.02 | Cho phép cấu hình số lượng tác vụ đồng thời. |
| NFR12.03 | Kiểm soát rate limit của nhà cung cấp API. |
| NFR12.04 | Có khả năng mở rộng tải xử lý trong tương lai. |

Không đặt mục tiêu phục vụ số lượng lớn người dùng đồng thời trong MVP. Không bắt buộc Microservices, Kubernetes hoặc hạ tầng phân tán.

### 7.14. Chiến lược xác định chỉ tiêu chất lượng

Áp dụng phương án Hybrid Targets:

- Xác định trước các ràng buộc kỹ thuật có thể kiểm soát.
- Xác định giới hạn vòng lặp, timeout và tài nguyên tại giai đoạn System Design.
- Đánh giá baseline trước khi xác định mục tiêu cải thiện chất lượng, chi phí và độ trễ.
- Xác định chỉ tiêu nghiên cứu trên tập phát triển trước khi đánh giá tập test cuối cùng.
- Không lựa chọn ngưỡng chất lượng dựa trên kết quả của tập test cuối cùng.
- Không cam kết trước mức cải thiện khi chưa có đủ căn cứ thực nghiệm.

## 8. Quy tắc nghiệp vụ (Business Rules)

### 8.1. Tổng quan

Business Rules quy định các nguyên tắc mà hệ thống suy luận toán học phải tuân thủ, độc lập với mô hình LLM, Agent Framework và công cụ được lựa chọn.

| ID | Nhóm quy tắc | Số lượng |
|---|---|---:|
| BR01 | Dữ kiện và giả thiết | 6 |
| BR02 | Tri thức toán học | 5 |
| BR03 | Suy luận toán học | 6 |
| BR04 | Sử dụng công cụ | 6 |
| BR05 | Kiểm chứng | 6 |
| BR06 | Tự sửa lỗi | 5 |
| BR07 | Điều phối và tài nguyên | 6 |
| BR08 | Xử lý sự không chắc chắn | 6 |
| BR09 | Xuất kết quả | 5 |
| BR10 | Thực nghiệm | 7 |
| BR11 | Bảo mật và quyền riêng tư | 4 |
| | **Tổng** | **62** |

### 8.2. BR01 — Dữ kiện và giả thiết

| ID | Quy tắc |
|---|---|
| BR01.01 | Không tự ý thay đổi dữ kiện được cho trong đề bài. |
| BR01.02 | Phân biệt dữ kiện gốc, dữ kiện quan sát, dữ kiện suy ra và giả thiết bổ sung. |
| BR01.03 | Không suy ra quan hệ hình học chỉ từ tỷ lệ hoặc hình dáng minh họa. |
| BR01.04 | Khi văn bản và hình ảnh mâu thuẫn, phải ghi nhận mâu thuẫn thay vì tự ý chọn dữ kiện. |
| BR01.05 | Dữ kiện bổ sung từ người dùng phải được ghi nhận nguồn gốc. |
| BR01.06 | Khi dữ kiện thay đổi, các kết quả phụ thuộc phải được đánh giá lại. |

### 8.3. BR02 — Tri thức toán học

| ID | Quy tắc |
|---|---|
| BR02.01 | Tri thức áp dụng phải phù hợp với nhiệm vụ hiện tại. |
| BR02.02 | Các điều kiện áp dụng định lý phải được thỏa mãn hoặc chứng minh. |
| BR02.03 | Không tự tạo nguồn tham chiếu không tồn tại. |
| BR02.04 | Tri thức truy xuất không được mặc định là chính xác chỉ vì có độ tương đồng cao. |
| BR02.05 | Khi phát hiện tri thức mâu thuẫn, không được sử dụng một cách thiếu căn cứ. |

### 8.4. BR03 — Suy luận toán học

| ID | Quy tắc |
|---|---|
| BR03.01 | Các bước giải phải dựa trên dữ kiện hoặc kết quả trung gian hợp lệ. |
| BR03.02 | Phải bảo toàn điều kiện xác định trong quá trình biến đổi. |
| BR03.03 | Phải phân biệt phép biến đổi tương đương và phép suy ra một chiều. |
| BR03.04 | Phải xét các trường hợp cần thiết để bảo đảm tính đầy đủ. |
| BR03.05 | Không sử dụng kết quả cần chứng minh làm giả thiết nếu không có căn cứ hợp lệ. |
| BR03.06 | Phải bảo toàn đơn vị đo và miền giá trị liên quan. |

### 8.5. BR04 — Sử dụng công cụ

| ID | Quy tắc |
|---|---|
| BR04.01 | Chỉ được thực thi các công cụ đã đăng ký. |
| BR04.02 | Tham số phải được kiểm tra trước khi thực thi. |
| BR04.03 | Kết quả công cụ phải được diễn giải đúng ngữ nghĩa toán học. |
| BR04.04 | Không coi kết quả công cụ là bằng chứng cho toàn bộ lời giải. |
| BR04.05 | Kết quả thực thi thất bại không được sử dụng như kết quả hợp lệ. |
| BR04.06 | Không được thực thi mã tùy ý do LLM hoặc người dùng cung cấp. |

### 8.6. BR05 — Kiểm chứng

| ID | Quy tắc |
|---|---|
| BR05.01 | Lời giải phải trải qua cơ chế kiểm chứng phù hợp trước khi được đánh dấu VERIFIED. |
| BR05.02 | Kiểm chứng phải xét cả tính đúng và tính đầy đủ khi phù hợp. |
| BR05.03 | Không đánh dấu VERIFIED nếu còn lỗi ảnh hưởng đến kết quả chưa được giải quyết. |
| BR05.04 | Kết quả kiểm chứng phải gắn với phiên bản lời giải tương ứng. |
| BR05.05 | Kiểm chứng một phần không đồng nghĩa với kiểm chứng toàn bộ. |
| BR05.06 | Đánh giá bằng LLM không được mô tả là chứng minh hình thức bằng máy. |

### 8.7. BR06 — Tự sửa lỗi

| ID | Quy tắc |
|---|---|
| BR06.01 | Mọi sửa đổi phải hướng đến giải quyết lỗi đã phát hiện hoặc cải thiện lời giải có căn cứ. |
| BR06.02 | Phải đánh giá lại các bước phụ thuộc vào bước được sửa. |
| BR06.03 | Lời giải sau khi sửa phải được kiểm chứng lại. |
| BR06.04 | Không vượt quá giới hạn số vòng sửa lỗi đã cấu hình. |
| BR06.05 | Phải bảo toàn thông tin cần thiết để đối chiếu phiên bản trước và sau khi sửa. |

### 8.8. BR07 — Điều phối và tài nguyên

| ID | Quy tắc |
|---|---|
| BR07.01 | Chỉ được điều phối đến các Agent và năng lực hợp lệ. |
| BR07.02 | Không thực thi nhiệm vụ khi các điều kiện phụ thuộc bắt buộc chưa được đáp ứng. |
| BR07.03 | Không bỏ qua các bước kiểm chứng bắt buộc chỉ để tiết kiệm chi phí. |
| BR07.04 | Không vượt quá giới hạn tài nguyên đã cấu hình. |
| BR07.05 | Khi đạt giới hạn tài nguyên, phải kết thúc hoặc chuyển sang cơ chế xử lý bất định phù hợp. |
| BR07.06 | Quyết định điều phối phải có khả năng truy vết. |

### 8.9. BR08 — Xử lý sự không chắc chắn

| ID | Quy tắc |
|---|---|
| BR08.01 | Không tự ý lựa chọn dữ kiện mơ hồ nếu sự lựa chọn ảnh hưởng đến đáp án. |
| BR08.02 | Giả thiết bổ sung phải được trình bày rõ ràng. |
| BR08.03 | Không khẳng định bài toán vô nghiệm chỉ vì hệ thống không tìm được lời giải. |
| BR08.04 | Phải phân biệt bài toán thiếu dữ kiện với bài toán có nhiều nghiệm hợp lệ. |
| BR08.05 | Không biểu diễn độ tự tin chưa hiệu chỉnh thành xác suất đúng. |
| BR08.06 | Khi không đủ căn cứ, phải làm rõ, trả lời có điều kiện hoặc từ chối kết luận. |

### 8.10. BR09 — Xuất kết quả

| ID | Quy tắc |
|---|---|
| BR09.01 | Các định dạng đầu ra phải sử dụng chung kết quả toán học chuẩn hóa. |
| BR09.02 | Việc định dạng không được làm thay đổi nội dung toán học. |
| BR09.03 | Không che giấu lỗi, giả thiết hoặc giới hạn kiểm chứng có ảnh hưởng đến đáp án. |
| BR09.04 | Không nâng trạng thái kiểm chứng khi chưa thực hiện kiểm chứng bổ sung. |
| BR09.05 | Lời giải phải phù hợp với yêu cầu và phạm vi kiến thức của bài toán. |

### 8.11. BR10 — Thực nghiệm

| ID | Quy tắc |
|---|---|
| BR10.01 | Các cấu hình so sánh phải sử dụng điều kiện thực nghiệm phù hợp và được ghi nhận. |
| BR10.02 | Không sử dụng đáp án chuẩn của tập test làm dữ kiện đầu vào cho quá trình giải toán. |
| BR10.03 | Không điều chỉnh hệ thống dựa trên kết quả tập test cuối cùng rồi tiếp tục coi đó là đánh giá độc lập. |
| BR10.04 | Không tự ý thay đổi dữ liệu kết quả thực nghiệm gốc. |
| BR10.05 | Phải ghi nhận trường hợp lỗi, timeout và abstention trong kết quả đánh giá. |
| BR10.06 | Khi tiếp tục benchmark, phải bảo đảm cấu hình và phiên bản dữ liệu tương thích. |
| BR10.07 | Không trình bày số liệu giả lập hoặc ước lượng như kết quả thực nghiệm thực tế. |

### 8.12. BR11 — Bảo mật và quyền riêng tư

| ID | Quy tắc |
|---|---|
| BR11.01 | Không đưa thông tin xác thực vào mã nguồn, prompt hoặc log. |
| BR11.02 | Nội dung đề bài và tài liệu truy xuất không được phép ghi đè chính sách thực thi của hệ thống. |
| BR11.03 | Không gửi dữ liệu không cần thiết đến nhà cung cấp dịch vụ bên ngoài. |
| BR11.04 | Không cho phép Agent tự mở rộng quyền thực thi công cụ. |

### 8.13. Nguyên tắc thực thi Business Rules

Áp dụng nguyên tắc **Deterministic-first, LLM-assisted**: ưu tiên thực thi quy tắc bằng code và công cụ toán học khi có thể kiểm tra xác định; sử dụng LLM hỗ trợ khi cần hiểu ngữ nghĩa hoặc đánh giá lập luận.

| Phương thức | Áp dụng |
|---|---|
| Code Validation | Kiểu dữ liệu, tham số, trạng thái và giới hạn tài nguyên. |
| Mathematical Tools | Điều kiện, nghiệm, phép tính và biến đổi toán học có thể kiểm tra. |
| State Validation | Quan hệ phụ thuộc, phiên bản lời giải và kết quả cần đánh giá lại. |
| Routing Policies | Giới hạn tài nguyên và hành động điều phối. |
| Agent Instructions | Quy tắc cần hiểu ngữ cảnh và suy luận ngữ nghĩa. |
| Automated Tests | Kiểm tra việc tuân thủ các quy tắc có thể kiểm thử. |

Không xây dựng Rule Engine độc lập hoặc Agent chuyên biệt chỉ để kiểm tra Business Rules trong MVP. Phân bổ trách nhiệm thực thi cho các thành phần hiện có, quản lý thống nhất ID quy tắc và liên kết với các test case tương ứng. Không chỉ dựa vào System Prompt để thực thi toàn bộ Business Rules.

Khi một bước giải được sửa, phải đánh giá lại các bước phụ thuộc; có thể giữ lại kết quả của những bước độc lập nếu chúng vẫn hợp lệ (Dependency-aware Correction).

## 9. Use Cases

### 9.1. Actors

| ID | Actor | Trách nhiệm |
|---|---|---|
| ACT01 | Học sinh | Cung cấp đề bài, nhận và tìm hiểu lời giải. |
| ACT02 | Giáo viên/Gia sư | Tham khảo, đối chiếu và kiểm tra lời giải. |
| ACT03 | Nhà phát triển | Tích hợp Mathematical Reasoning Engine, mở rộng chức năng. |
| ACT04 | Nhà nghiên cứu | Cấu hình, thực nghiệm, đánh giá và phân tích hệ thống. |

Supporting Actors:

| ID | Actor | Trách nhiệm |
|---|---|---|
| ACT05 | LLM Provider | Cung cấp năng lực xử lý đa phương thức và suy luận. |
| ACT06 | External Tool Provider | Cung cấp công cụ bên ngoài khi mở rộng hệ thống. |

ACT06 không bắt buộc trong MVP. SymPy, Calculator, Knowledge Base và Agent nội bộ thuộc phạm vi hệ thống, không phải Actor bên ngoài.

### 9.2. Danh sách Use Cases

#### Nhóm A — Mathematical Reasoning

| ID | Use Case | Ưu tiên |
|---|---|---|
| UC01 | Giải bài toán dạng văn bản | P0 |
| UC02 | Giải bài toán đa phương thức | P0 |
| UC03 | Bổ sung hoặc làm rõ dữ kiện | P0 |
| UC04 | Xem lời giải chi tiết và căn cứ toán học | P0 |
| UC05 | Xem kết quả kiểm chứng và thông tin bất định | P0 |
| UC06 | Kiểm tra lời giải do người dùng cung cấp | P1 |
| UC07 | Giải bài toán từ tài liệu PDF hoặc đề viết tay | P1 |
| UC08 | Xem nhiều phương pháp giải | P1 |

#### Nhóm B — Integration & Extensibility

| ID | Use Case | Ưu tiên |
|---|---|---|
| UC09 | Gọi Mathematical Reasoning Engine từ chương trình khác | P0 |
| UC10 | Đăng ký và mở rộng công cụ toán học | P0 |
| UC11 | Cập nhật và mở rộng kho tri thức | P0 |
| UC12 | Thay thế mô hình và cấu hình Agent | P0 |

#### Nhóm C — Research & Evaluation

| ID | Use Case | Ưu tiên |
|---|---|---|
| UC13 | Quản lý tập dữ liệu benchmark | P0 |
| UC14 | Cấu hình phiên thực nghiệm | P0 |
| UC15 | Thực thi benchmark tự động | P0 |
| UC16 | So sánh cấu hình và Ablation Study | P0 |
| UC17 | Phân tích quá trình suy luận và lỗi | P0 |
| UC18 | Phân tích hiệu năng và chi phí | P0 |
| UC19 | Khôi phục benchmark bị gián đoạn | P0 |
| UC20 | Xuất kết quả thực nghiệm | P0 |

Tổng cộng 20 Use Cases (17 P0, 3 P1). UC09 yêu cầu giao diện lập trình ổn định, không bắt buộc REST API public hoặc SDK riêng.

### 9.3. Quan hệ Actor và Use Case

| Actor | Use Cases chính |
|---|---|
| ACT01 | UC01–UC08 |
| ACT02 | UC01–UC08 |
| ACT03 | UC09–UC12 |
| ACT04 | UC13–UC20 |
| ACT05 | Hỗ trợ các phiên suy luận cần LLM. |
| ACT06 | Hỗ trợ sử dụng công cụ bên ngoài khi mở rộng. |

### 9.4. Đặc tả các Use Case có luồng phức tạp

#### UC02 — Giải bài toán đa phương thức (P0)

- Primary Actor: Học sinh, Giáo viên/Gia sư.
- Trigger: Người dùng gửi đề bài.
- Tiền điều kiện: Đầu vào thuộc định dạng được hỗ trợ.
- Hậu điều kiện: Trả về kết quả có cấu trúc hoặc trạng thái chưa thể kết luận.
- Related FR: FR01–FR09.

Luồng chính:

1. Người dùng cung cấp đề toán.
2. Hệ thống kiểm tra đầu vào.
3. Trích xuất và chuẩn hóa dữ kiện đa phương thức.
4. Phân tích bài toán và lựa chọn chiến lược suy luận.
5. Truy xuất tri thức khi cần thiết.
6. Thực hiện suy luận và gọi công cụ toán học khi cần thiết.
7. Kiểm chứng và sửa lỗi nếu phát hiện sai sót.
8. Tổng hợp và trả về kết quả.

| Ngoại lệ | Hành động |
|---|---|
| Đầu vào không hợp lệ | Yêu cầu cung cấp lại. |
| Dữ kiện không rõ ràng | Chuyển UC03. |
| Bài toán đơn giản | Sử dụng tuyến Lightweight. |
| Phát hiện lỗi toán học | Corrective Reasoning. |
| Vượt giới hạn tài nguyên | Kết thúc an toàn, thông báo giới hạn. |
| Không đủ căn cứ kết luận | Conditional Answer hoặc Abstention. |

#### UC03 — Bổ sung hoặc làm rõ dữ kiện (P0)

- Primary Actor: Người dùng.
- Trigger: Hệ thống phát hiện bất định cần người dùng giải quyết.
- Tiền điều kiện: Có phiên suy luận đang xử lý.
- Hậu điều kiện: Dữ kiện được cập nhật hoặc phiên suy luận kết thúc.
- Related FR: FR01, FR02, FR07, FR08.

Hệ thống yêu cầu làm rõ dữ kiện; người dùng cung cấp hoặc xác nhận thông tin; hệ thống ghi nhận nguồn gốc, đánh giá lại các kết quả phụ thuộc và tiếp tục phiên suy luận nếu có đủ căn cứ. Nếu không thể làm rõ, hệ thống trả lời có điều kiện hoặc từ chối kết luận phù hợp với FR08. Không bắt buộc xử lý lại toàn bộ từ đầu.

#### UC06 — Kiểm tra lời giải do người dùng cung cấp (P1)

- Primary Actor: Học sinh, Giáo viên/Gia sư.
- Trigger: Người dùng cung cấp đề bài và lời giải cần kiểm tra.
- Tiền điều kiện: Đầu vào hợp lệ.
- Hậu điều kiện: Báo cáo kiểm chứng, lỗi phát hiện và phản hồi có căn cứ; nêu rõ phạm vi kiểm chứng.
- Related FR: FR06.14 và các năng lực kiểm chứng FR06.

Tiếp nhận và chuẩn hóa lời giải bên ngoài, tái sử dụng Verifier Agent để kiểm tra tính nhất quán với đề bài, điều kiện, lập luận và phép tính. Thông báo vị trí lỗi khi có thể, đề xuất sửa lỗi hoặc nêu giới hạn kiểm chứng. Không mặc định phải giải lại toàn bộ bài toán.

#### UC15 — Thực thi benchmark tự động (P0)

- Primary Actor: Nhà nghiên cứu.
- Tiền điều kiện: Dataset và cấu hình thực nghiệm hợp lệ.
- Hậu điều kiện: Kết quả, metrics và log được lưu.
- Related FR: FR10.

Luồng chính: nạp Dataset và Experiment Config, chạy Benchmark Runner, gọi Mathematical Reasoning Engine, đánh giá kết quả, ghi metrics và execution logs, tổng hợp Experiment Results. Lặp lại cho các bài toán trong benchmark. Khi gặp lỗi API, timeout hoặc rate limit, lưu trạng thái cần thiết để tiếp tục mà không đánh mất các kết quả hợp lệ đã hoàn thành (UC19).

#### UC16 — So sánh cấu hình và Ablation Study (P0)

- Primary Actor: Nhà nghiên cứu.
- Related FR: FR10.
- Mục tiêu: Đánh giá đóng góp của từng thành phần bằng các cấu hình thực nghiệm phù hợp.

Nhà nghiên cứu lựa chọn cấu hình (Multi-Agent, Symbolic Tools, Agentic RAG, Verification, Adaptive Routing), thực thi benchmark theo điều kiện so sánh được ghi nhận, tổng hợp và đối chiếu các chỉ số như Accuracy, Solution Correctness, Latency, Token Usage và Cost per Problem. Tổ hợp cấu hình hợp lệ được xác định trong System Design; phương pháp đánh giá chi tiết tại 06_EVALUATION.md.

### 9.5. Nguyên tắc đặc tả

Chỉ đặc tả chi tiết các Use Case có luồng nghiệp vụ phức tạp. Các hoạt động phân tích đề bài, lập kế hoạch, lựa chọn Agent, truy xuất tri thức, gọi SymPy, kiểm chứng trung gian và tự sửa lỗi là quy trình nội bộ được mô tả thông qua Functional Requirements và System Design, không phải các Use Case độc lập.

### 9.6. Giới hạn phạm vi

Không đưa đăng ký tài khoản, quản lý lớp học, chấm điểm học sinh, quản lý bài tập, cá nhân hóa lộ trình học hoặc thanh toán dịch vụ vào MVP. Tập trung vào Mathematical Reasoning Engine và thực nghiệm nghiên cứu.

## 10. Ràng buộc và giả định

### 10.1. Ràng buộc nguồn lực

Dự án phải phù hợp với khả năng triển khai, thời gian và ngân sách của một sinh viên phát triển cá nhân.

### 10.2. Ràng buộc triển khai và nghiên cứu (Constraints)

| ID | Ràng buộc |
|---|---|
| C01 | Ưu tiên chiều sâu nghiên cứu AI thay vì độ phức tạp hạ tầng. |
| C02 | Ưu tiên phát triển và thực nghiệm trên máy cá nhân (Local-first). |
| C03 | Không yêu cầu thuê GPU Server hoặc máy chủ chuyên dụng để hoàn thành MVP. |
| C04 | Có thể sử dụng API mô hình AI bên ngoài trong giới hạn ngân sách. |
| C05 | Ưu tiên công cụ mã nguồn mở và giải pháp lưu trữ có chi phí thấp. |
| C06 | Không bắt buộc triển khai hạ tầng phân tán, Kubernetes hoặc Microservices. |
| C07 | Không yêu cầu huấn luyện mô hình nền tảng từ đầu. |
| C08 | Kiểm soát ngân sách API, số lần gọi mô hình và số vòng lặp suy luận. |
| C09 | Không đặt mục tiêu phục vụ người dùng quy mô lớn trong MVP. |
| C10 | Ưu tiên hoàn thành và đánh giá các chức năng P0 trước khi mở rộng P1 và P2. |
| C11 | Phạm vi đánh giá chính tập trung vào toán THCS lớp 6–9. |
| C12 | Dữ liệu nghiên cứu phải có nguồn gốc rõ ràng và quyền sử dụng phù hợp. |
| C13 | Không phụ thuộc bắt buộc vào duy nhất một nhà cung cấp LLM. |
| C14 | Các mô hình và phương pháp thực nghiệm phải phù hợp với nguồn lực thực tế của dự án. |

C07 không loại trừ Fine-tuning hoặc sử dụng mô hình mã nguồn mở nếu cần thiết cho nghiên cứu. C13 không yêu cầu tích hợp nhiều nhà cung cấp ngay từ đầu; kiến trúc cần cho phép thay thế nhà cung cấp.

Ngân sách cụ thể chưa cần xác định tại giai đoạn Requirements. Việc phân bổ ngân sách sẽ được xem xét trong quá trình thiết kế, triển khai và xây dựng thực nghiệm.

### 10.3. Giả định (Assumptions)

Các giả định cần được kiểm chứng trong quá trình phát triển.

| ID | Giả định |
|---|---|
| A01 | Có thể tiếp cận ít nhất một LLM hỗ trợ Multimodal Understanding và Tool Calling. |
| A02 | Có kết nối Internet khi cần sử dụng API mô hình bên ngoài. |
| A03 | Máy tính cá nhân đủ khả năng chạy các thành phần xử lý local. |
| A04 | Có thể thu thập hoặc xây dựng tập dữ liệu benchmark toán THCS phù hợp. |
| A05 | Có thể xây dựng kho tri thức toán học với nguồn tham chiếu đáng tin cậy. |
| A06 | Các công cụ Symbolic Mathematics đáp ứng phần lớn nhu cầu tính toán trong phạm vi MVP. |
| A07 | Người dùng có thể bổ sung dữ kiện khi cần Human-in-the-loop. |
| A08 | Có thể thực hiện kiểm tra thủ công đối với một phần dữ liệu và lời giải thực nghiệm. |
| A09 | Nhà cung cấp LLM duy trì khả năng truy cập API trong thời gian thực nghiệm. |
| A10 | Có thể tiếp cận tài liệu nghiên cứu để xây dựng baseline và đối chiếu phương pháp. |

### 10.4. Rủi ro và phương án xử lý

| Rủi ro | Phương án xử lý |
|---|---|
| Chi phí API quá cao | Adaptive Routing, giới hạn token, giảm số lượt gọi không cần thiết. |
| API thay đổi hoặc ngừng hoạt động | Model Adapter, thay thế Provider. |
| Thiếu dataset phù hợp | Xây dựng benchmark có kiểm soát. |
| Thiếu dữ liệu đa phương thức | Thu thập và chú thích hình ảnh có chọn lọc. |
| LLM suy luận hình học kém | Structured Representation và Verification. |
| SymPy không kiểm chứng được chứng minh | Hybrid Verification, rubric, đánh giá thủ công. |
| Thời gian phát triển không đủ | Hoàn thành P0, trì hoãn P1/P2. |
| Kết quả nghiên cứu không vượt baseline | Phân tích nguyên nhân và báo cáo giới hạn trung thực. |

Không cam kết kết quả vượt baseline trước thực nghiệm.

### 10.5. Định hướng triển khai Local-first

Ưu tiên chạy giao diện, Mathematical Reasoning Engine, Agents, Routing, Shared State, Knowledge Retrieval, SymPy/Calculator, Evaluation, Logs và Benchmark trên máy tính cá nhân khi khả thi. Chỉ sử dụng dịch vụ LLM bên ngoài khi cần thiết, trong giới hạn tài nguyên và quyền riêng tư đã quy định.

Không yêu cầu duy trì máy chủ 24/7. Technology Stack cụ thể được quyết định tại System Design; ngân sách cụ thể được xem xét trong thiết kế, triển khai và thực nghiệm.

## 11. Phạm vi MVP và mở rộng (MVP Scope & Future Extensions)

### 11.1. Định nghĩa MVP

MVP là nguyên mẫu nghiên cứu AI Mathematical Reasoning Engine có khả năng tiếp nhận và hiểu đề toán đa phương thức; phân tích và lập kế hoạch; truy xuất tri thức theo nhu cầu; suy luận nhiều bước kết hợp công cụ toán học; kiểm chứng và tự sửa lỗi; điều phối Agent thích ứng; xử lý sự không chắc chắn; cung cấp lời giải có cấu trúc; thực hiện benchmark và so sánh phương pháp phục vụ Research Objectives.

Phạm vi chức năng hiện tại gồm 132 Functional Requirements: 115 P0 bắt buộc, 16 P1 mở rộng khi nguồn lực cho phép và 1 P2 định hướng tương lai.

### 11.2. Phạm vi kiến thức toán học

| ID | Miền kiến thức | Năng lực nghiên cứu |
|---|---|---|
| MD01 | Số học | Tính toán chính xác. |
| MD02 | Biểu thức đại số | Symbolic Reasoning. |
| MD03 | Phương trình và hệ phương trình | Tool Use. |
| MD04 | Bất phương trình | Điều kiện và kiểm chứng nghiệm. |
| MD05 | Hàm số và đồ thị | Multimodal Reasoning. |
| MD06 | Hình học phẳng | Visual Understanding, Knowledge Grounding. |
| MD07 | Thống kê và xác suất cơ bản | Phân tích bảng, biểu đồ. |
| MD08 | Bài toán thực tế | Multi-step Reasoning, Planning. |

Lựa chọn các dạng toán đại diện trong chương trình THCS lớp 6–9. Không cam kết bao phủ tất cả dạng bài nâng cao hoặc chứng minh hình học phức tạp. Phạm vi chi tiết theo dạng toán được xác định khi xây dựng benchmark.

### 11.3. Các giai đoạn phát triển MVP

| Giai đoạn | Mục tiêu | Phạm vi |
|---|---|---|
| MVP-A — Core Reasoning | Nền tảng suy luận toán học | Đề toán văn bản, Planning, Reasoning, Direct Function Calling, SymPy, đầu ra có cấu trúc và baseline đầu tiên. |
| MVP-B — Grounded Multi-Agent Reasoning | Suy luận có căn cứ và kiểm chứng | Multi-Agent, Agentic RAG, Hybrid Verification, Correction, Shared State. |
| MVP-C — Adaptive Multimodal Reasoning | Năng lực nghiên cứu trọng tâm | Hiểu hình ảnh, Adaptive Routing, Uncertainty Handling, Human-in-the-loop và hoàn thiện yêu cầu P0. |
| MVP-D — Research Validation | Hoàn thiện và đánh giá khoa học | Benchmark, baselines, Ablation Study, phân tích lỗi, độ chính xác, chi phí, độ trễ, khả năng kiểm chứng và báo cáo nghiên cứu. |

Xây dựng Benchmark Runner, logging và kiểm thử từ MVP-A, mở rộng xuyên suốt các giai đoạn. Bốn mốc là định hướng phân chia phạm vi, chưa phải lịch triển khai chính thức.

### 11.4. Chức năng P1

| Nhóm | Functional Requirements | Số lượng |
|---|---|---:|
| Đầu vào mở rộng | FR01.08–FR01.10, FR02.11 | 4 |
| Suy luận nâng cao | FR03.10, FR05.14, FR06.13 | 3 |
| Knowledge Retrieval | FR04.11–FR04.12 | 2 |
| Verification | FR06.14 | 1 |
| Routing | FR07.14 | 1 |
| Uncertainty | FR08.15 | 1 |
| Output | FR09.13–FR09.14 | 2 |
| Evaluation | FR10.16–FR10.17 | 2 |
| | **Tổng** | **16** |

Sau khi hoàn thành P0, ưu tiên các P1 có giá trị nghiên cứu: kiểm chứng độc lập, hiệu chỉnh độ tin cậy định lượng, trực quan hóa thực nghiệm và LLM-as-a-Judge có đối chiếu thủ công. Tiếp theo là các chức năng tăng khả năng sử dụng và P1 còn lại. Viết tay, PDF và phân tách bài toán vẫn là mục tiêu mở rộng trong MVP. Không thay đổi mức ưu tiên chính thức.

### 11.5. Phạm vi ngoài MVP

| Chức năng | Định hướng |
|---|---|
| Toán THPT và đại học | Mở rộng miền kiến thức. |
| MCP Integration | Mở rộng giao thức công cụ. |
| Formal Proof Engine | Kiểm chứng chứng minh hình thức. |
| Multimodal Generation | Sinh hình vẽ, đồ thị minh họa. |
| Fine-tuning chuyên biệt | Nghiên cứu bổ sung nếu cần. |
| Reinforcement Learning Router | Tối ưu chiến lược điều phối. |
| Public API và SDK | Mở rộng khả năng tích hợp. |
| Xuất lời giải PDF | FR09.15 — P2. |
| Distributed Architecture | Khi có nhu cầu mở rộng thực tế. |
| Education Platform | Phát triển ứng dụng dựa trên MATHK. |

Đây là hướng mở rộng, không phải cam kết triển khai.

### 11.6. Sản phẩm bàn giao MVP

| ID | Deliverable |
|---|---|
| D01 | Mathematical Reasoning Engine hoạt động được. |
| D02 | Giao diện demo tối giản hỗ trợ văn bản và hình ảnh. |
| D03 | Bộ công cụ toán học và Tool Registry. |
| D04 | Kho tri thức toán học có cấu trúc. |
| D05 | Tập dữ liệu benchmark. |
| D06 | Evaluation Pipeline và Benchmark Runner. |
| D07 | Các cấu hình baseline và ablation. |
| D08 | Kết quả thực nghiệm và phân tích lỗi. |
| D09 | Mã nguồn và tài liệu kỹ thuật. |
| D10 | Báo cáo nghiên cứu hoặc bản thảo bài báo. |

Việc bài báo được chấp nhận tại hội nghị quốc tế không phải tiêu chí nghiệm thu bắt buộc; mục tiêu là tạo sản phẩm nghiên cứu đủ nghiêm túc để có cơ hội gửi bài.

## 12. Tiêu chí nghiệm thu (Acceptance Criteria)

### 12.1. Chiến lược nghiệm thu

Áp dụng Hybrid Targets theo mục 7.14. Nghiệm thu theo bốn nhóm: Functional Acceptance, Technical Acceptance, Research Acceptance và Deliverable Acceptance.

### 12.2. Functional Acceptance Criteria

| ID | Nhóm FR | Điều kiện nghiệm thu |
|---|---|---|
| FAC01 | FR01 | Tiếp nhận, kiểm tra và cập nhật được đề toán văn bản, hình ảnh và đầu vào kết hợp. |
| FAC02 | FR02 | Trích xuất và chuẩn hóa dữ kiện toán học, bao gồm dữ kiện trực quan và nguồn gốc. |
| FAC03 | FR03 | Xác định mục tiêu, phân tích và lập kế hoạch giải toán có cấu trúc. |
| FAC04 | FR04 | Truy xuất tri thức phù hợp, cung cấp nguồn và điều kiện áp dụng. |
| FAC05 | FR05 | Giải toán nhiều bước, gọi và tích hợp kết quả công cụ toán học. |
| FAC06 | FR06 | Kiểm chứng lời giải, phát hiện lỗi, sửa lỗi và kiểm chứng lại trong giới hạn cho phép. |
| FAC07 | FR07 | Điều phối Agent thích ứng, quản lý Shared State và giới hạn tài nguyên. |
| FAC08 | FR08 | Phát hiện bất định, yêu cầu làm rõ, trả lời có điều kiện hoặc từ chối kết luận phù hợp. |
| FAC09 | FR09 | Cung cấp lời giải có cấu trúc, đáp án, căn cứ, trạng thái kiểm chứng và thông tin bất định. |
| FAC10 | FR10 | Thực hiện benchmark tự động, cấu hình thí nghiệm, ghi log và xuất kết quả. |

- Toàn bộ 115 Functional Requirements P0 phải được triển khai và có bằng chứng kiểm thử phù hợp.
- P1 được nghiệm thu riêng đối với chức năng đã triển khai; P2 không phải điều kiện nghiệm thu MVP.
- Cả 62 Business Rules phải được xem xét khi kiểm thử chức năng tương ứng.
- Không coi yêu cầu hoàn thành chỉ vì mã nguồn tương ứng tồn tại. Test case chi tiết được xây dựng trong triển khai.

### 12.3. Technical Acceptance Criteria

| ID | Tiêu chí | Phương pháp xác minh |
|---|---|---|
| TAC01 | Có thể cài đặt và chạy hệ thống trên máy tính cá nhân | Installation Test |
| TAC02 | Các thành phần có interface và trách nhiệm rõ ràng | Architecture Review |
| TAC03 | Có khả năng thay thế LLM thông qua interface thống nhất | Integration Test |
| TAC04 | Kiểm tra đầu vào, đầu ra và tham số công cụ | Validation Test |
| TAC05 | Không có vòng lặp suy luận hoặc sửa lỗi vô hạn | Boundary Test |
| TAC06 | Kiểm soát timeout, retry, rate limit và giới hạn tài nguyên | Fault Injection Test |
| TAC07 | Không cho phép thực thi mã hoặc công cụ ngoài quyền hạn | Security Test |
| TAC08 | Không đưa thông tin xác thực vào mã nguồn hoặc log | Security Review |
| TAC09 | Có khả năng truy vết phiên suy luận và quyết định điều phối | Execution Trace Review |
| TAC10 | Bảo toàn kết quả hợp lệ khi benchmark bị gián đoạn | Recovery Test |
| TAC11 | Lưu phiên bản dữ liệu, mô hình, prompt và cấu hình thực nghiệm | Reproducibility Review |
| TAC12 | Các định dạng đầu ra nhất quán về nội dung toán học | Consistency Test |

Giới hạn vòng lặp, timeout và tài nguyên cụ thể được xác định tại System Design. Khi đạt giới hạn sửa lỗi, hệ thống phải dừng sửa lỗi, ghi nhận lỗi chưa giải quyết và xử lý bất định phù hợp; lời giải đã sửa phải được kiểm chứng lại.

### 12.4. Research Acceptance Criteria

#### A. Thực nghiệm theo Research Objectives

| ID | Research Objective | So sánh thực nghiệm |
|---|---|---|
| RAC01 | RO01 — Multi-Agent | Single-Agent và Multi-Agent |
| RAC02 | RO02 — Symbolic Tools | Có và không sử dụng công cụ toán học |
| RAC03 | RO03 — Agentic RAG | No RAG, Static RAG, Agentic RAG |
| RAC04 | RO04 — Verification | Có và không kiểm chứng, tự sửa lỗi |
| RAC05 | RO05 — Adaptive Routing | Static, Rule-based và Hybrid Routing |
| RAC06 | RO06 — Multimodal | Text/OCR-based và Multimodal Reasoning |
| RAC07 | RO07 — Uncertainty | Có và không có cơ chế xử lý bất định |

Không bắt buộc thử nghiệm mọi tổ hợp thành phần; thiết kế thí nghiệm phù hợp để trả lời các câu hỏi nghiên cứu.

#### B. Chỉ số đánh giá

| Khía cạnh | Metrics đề xuất |
|---|---|
| Độ chính xác | Answer Accuracy, Mathematical Equivalence |
| Chất lượng lời giải | Solution Correctness |
| Truy xuất tri thức | Recall@K, Precision@K, MRR |
| Kiểm chứng | Error Detection F1 |
| Tự sửa lỗi | Correction Success Rate |
| Xử lý bất định | Detection F1, Coverage, False Abstention Rate |
| Hiệu năng | Latency |
| Tài nguyên | Token Usage, LLM Calls, Tool Calls |
| Chi phí | Cost per Problem |

Các metric cần nhãn tham chiếu phải có dữ liệu tham chiếu phù hợp để đánh giá đáng tin cậy.

#### C. Xác định ngưỡng chất lượng

Áp dụng Hybrid Targets: xây dựng dataset và phân tách Development/Test; đánh giá baseline trên Development Set; xác định mục tiêu chất lượng, chi phí và độ trễ; phát triển và tối ưu trên Development Set; đánh giá cuối cùng trên Held-out Test Set.

Không áp đặt ngưỡng chất lượng hoặc mức cải thiện khi chưa có căn cứ baseline. Các ngưỡng phải được xác định trước khi đánh giá trên tập test cuối cùng.

#### D. Tiêu chí hoàn thành nghiên cứu

| ID | Tiêu chí |
|---|---|
| RAC08 | Có benchmark với nguồn gốc và phương pháp xây dựng rõ ràng. |
| RAC09 | Có phương pháp đánh giá và metric phù hợp với từng câu hỏi nghiên cứu. |
| RAC10 | Có baseline hợp lý và điều kiện so sánh được kiểm soát. |
| RAC11 | Hoàn thành các thí nghiệm và Ablation Study đã thống nhất. |
| RAC12 | Báo cáo đầy đủ kết quả tích cực, tiêu cực, lỗi và giới hạn hệ thống. |
| RAC13 | Không sử dụng đáp án tập test để tối ưu quá trình giải toán. |
| RAC14 | Có khả năng chạy lại thí nghiệm theo cấu hình đã lưu. |
| RAC15 | Có báo cáo nghiên cứu hoặc bản thảo bài báo trình bày phương pháp và kết quả. |

Nếu phương pháp không vượt baseline thì mục tiêu cải thiện chất lượng có thể chưa đạt, nhưng quá trình nghiên cứu vẫn có thể được nghiệm thu nếu thí nghiệm hợp lệ và kết quả được báo cáo trung thực.

### 12.5. Deliverable Acceptance Criteria

| Deliverable | Điều kiện bàn giao |
|---|---|
| D01 — Reasoning Engine | Chạy được pipeline suy luận từ đầu đến cuối. |
| D02 — Demo | Thực hiện được các Use Case P0 dành cho người dùng cuối. |
| D03 — Math Tools | Có Tool Registry, interface, validation và kiểm thử. |
| D04 — Knowledge Base | Có tri thức có cấu trúc, metadata, nguồn tham chiếu. |
| D05 — Benchmark Dataset | Có dữ liệu, nhãn đánh giá và tài liệu mô tả. |
| D06 — Evaluation Pipeline | Chạy tự động, lưu và khôi phục kết quả. |
| D07 — Baseline & Ablation | Có cấu hình thực nghiệm và hướng dẫn chạy. |
| D08 — Experiment Results | Có số liệu thực tế, metrics và phân tích lỗi. |
| D09 — Source Code & Docs | Có mã nguồn, quản lý phiên bản và hướng dẫn sử dụng. |
| D10 — Research Report | Có phương pháp, thực nghiệm, kết quả và giới hạn nghiên cứu. |

### 12.6. Requirements Traceability Matrix

Truy vết từ Research Objectives (RO), Product Objectives (PO), Technical Objectives (TO) đến FR, NFR và Business Rules, tiếp theo là Acceptance Criteria, Test Cases và Test Results/Research Evidence.

| Requirement | Business Rule | Acceptance | Test Case dự kiến |
|---|---|---|---|
| FR05.07 | BR04.02 | FAC05, TAC04 | TC-TOOL-001 |
| FR06.11 | BR06.04 | FAC06, TAC05 | TC-VER-001 |
| FR07.10 | BR07.04 | FAC07, TAC05 | TC-ROUTE-001 |
| FR08.11 | BR08.06 | FAC08 | TC-UNC-001 |
| FR10.15 | BR10.06 | FAC10, TAC10 | TC-EVAL-001 |

Các ID test case là minh họa, chưa phải danh sách kiểm thử chính thức. Ma trận truy vết được xây dựng dần trong thiết kế và triển khai.

### 12.7. Definition of Done

- [ ] Hoàn thành và kiểm thử toàn bộ Functional Requirements P0.
- [ ] Đáp ứng các NFR bắt buộc với tiêu chí đã xác định.
- [ ] Có bằng chứng tuân thủ các Business Rules liên quan.
- [ ] Đáp ứng Functional và Technical Acceptance Criteria.
- [ ] Hoàn thành benchmark, baseline và Ablation Study.
- [ ] Có đầy đủ sản phẩm bàn giao D01–D10.
- [ ] Lưu mã nguồn, cấu hình và kết quả thực nghiệm.
- [ ] Báo cáo rõ các giới hạn và chức năng chưa hoàn thành.

Checklist là tiêu chí nghiệm thu dự kiến, không phản ánh tiến độ triển khai thực tế.

