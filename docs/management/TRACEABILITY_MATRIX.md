# Traceability Matrix — MATHK

**Phiên bản:** 0.1

**Trạng thái:** Khởi tạo theo AUD-005; ánh xạ cấp nhóm sơ bộ, chưa xác minh từng dòng.

Nguồn: [Requirements](../01_REQUIREMENTS.md), [System Design](../03_SYSTEM_DESIGN.md), [Implementation](../05_IMPLEMENTATION.md), [Evaluation](../06_EVALUATION.md). ID và nội dung giữ nguyên từ Requirements; dấu — ở priority nghĩa là xem quy định nhóm tại nguồn. Module/phase là ánh xạ dự kiến cấp nhóm, không phải cam kết coverage từng yêu cầu. P1/P2 không bắt buộc trong MVP. MVP C hoàn thiện P0 chức năng engine, MVP D hoàn thiện P0 benchmark/nghiên cứu. Mỗi task phải tinh chỉnh module, phase, test và acceptance evidence theo yêu cầu thực tế; chỉ cập nhật PASS khi có bằng chứng. ChatGPT quản lý, Codex bổ sung trong scope.

| ID | Yêu cầu / quy tắc | Priority | Module dự kiến | Phase dự kiến | Task / Test / Evidence | Status |
|---|---|---|---|---|---|---|
| FR01.01 | Tiếp nhận đề toán dạng văn bản. | P0 | M01/M03/M06 | 2–6 | — | PLANNED |
| FR01.02 | Hỗ trợ biểu thức toán học và LaTeX. | P0 | M01/M03/M06 | 2–6 | — | PLANNED |
| FR01.03 | Tiếp nhận đề toán dạng hình ảnh. | P0 | M01/M03/M06 | 2–6 | — | PLANNED |
| FR01.04 | Tiếp nhận kết hợp văn bản và hình ảnh. | P0 | M01/M03/M06 | 2–6 | — | PLANNED |
| FR01.05 | Hỗ trợ nhiều hình ảnh trong một bài toán. | P0 | M01/M03/M06 | 2–6 | — | PLANNED |
| FR01.06 | Kiểm tra tính hợp lệ của đầu vào. | P0 | M01/M03/M06 | 2–6 | — | PLANNED |
| FR01.07 | Cho phép người dùng bổ sung hoặc chỉnh sửa dữ kiện. | P0 | M01/M03/M06 | 2–6 | — | PLANNED |
| FR01.08 | Hỗ trợ nhận dạng đề toán viết tay. | P1 | M01/M03/M06 | 2–6 | — | PLANNED |
| FR01.09 | Tiếp nhận tài liệu PDF. | P1 | M01/M03/M06 | 2–6 | — | PLANNED |
| FR01.10 | Phân tách nhiều bài toán trong cùng tài liệu. | P1 | M01/M03/M06 | 2–6 | — | PLANNED |
| FR02.01 | Trích xuất nội dung văn bản từ hình ảnh. | P0 | M08/M13 | 6 | — | PLANNED |
| FR02.02 | Nhận diện công thức và ký hiệu toán học. | P0 | M08/M13 | 6 | — | PLANNED |
| FR02.03 | Nhận diện các đối tượng hình học. | P0 | M08/M13 | 6 | — | PLANNED |
| FR02.04 | Nhận diện các quan hệ hình học. | P0 | M08/M13 | 6 | — | PLANNED |
| FR02.05 | Trích xuất dữ kiện từ đồ thị, biểu đồ và bảng số liệu. | P0 | M08/M13 | 6 | — | PLANNED |
| FR02.06 | Liên kết nhãn, ký hiệu và giá trị với đối tượng tương ứng. | P0 | M08/M13 | 6 | — | PLANNED |
| FR02.07 | Kết hợp thông tin văn bản và hình ảnh. | P0 | M08/M13 | 6 | — | PLANNED |
| FR02.08 | Chuẩn hóa dữ kiện thành biểu diễn toán học có cấu trúc. | P0 | M08/M13 | 6 | — | PLANNED |
| FR02.09 | Xác định nguồn gốc của từng dữ kiện. | P0 | M08/M13 | 6 | — | PLANNED |
| FR02.10 | Phát hiện dữ kiện trực quan không rõ ràng hoặc mâu thuẫn. | P0 | M08/M13 | 6 | — | PLANNED |
| FR02.11 | Liên kết dữ kiện giữa nhiều hình ảnh hoặc nhiều trang tài liệu. | P1 | M08/M13 | 6 | — | PLANNED |
| FR03.01 | Xác định mục tiêu và yêu cầu của bài toán. | P0 | M09 | 3–6 | — | PLANNED |
| FR03.02 | Phân loại bài toán theo miền kiến thức. | P0 | M09 | 3–6 | — | PLANNED |
| FR03.03 | Ước lượng độ phức tạp của bài toán. | P0 | M09 | 3–6 | — | PLANNED |
| FR03.04 | Phân rã bài toán phức tạp thành các nhiệm vụ nhỏ. | P0 | M09 | 3–6 | — | PLANNED |
| FR03.05 | Xác định quan hệ phụ thuộc giữa các nhiệm vụ. | P0 | M09 | 3–6 | — | PLANNED |
| FR03.06 | Xác định kiến thức, công thức và định lý cần thiết. | P0 | M09 | 3–6 | — | PLANNED |
| FR03.07 | Xác định nhu cầu sử dụng công cụ toán học. | P0 | M09 | 3–6 | — | PLANNED |
| FR03.08 | Xây dựng kế hoạch giải toán có cấu trúc. | P0 | M09 | 3–6 | — | PLANNED |
| FR03.09 | Điều chỉnh kế hoạch khi phát hiện lỗi hoặc hướng giải không phù hợp. | P0 | M09 | 3–6 | — | PLANNED |
| FR03.10 | Đề xuất và so sánh nhiều phương án giải. | P1 | M09 | 3–6 | — | PLANNED |
| FR04.01 | Xây dựng và quản lý kho tri thức toán học. | P0 | M10/M16 | 4 | — | PLANNED |
| FR04.02 | Chuẩn hóa tri thức thành các đơn vị có cấu trúc và metadata. | P0 | M10/M16 | 4 | — | PLANNED |
| FR04.03 | Truy xuất định nghĩa, công thức, định lý và phương pháp giải. | P0 | M10/M16 | 4 | — | PLANNED |
| FR04.04 | Xây dựng truy vấn dựa trên bài toán và nhiệm vụ hiện tại. | P0 | M10/M16 | 4 | — | PLANNED |
| FR04.05 | Lọc tri thức theo miền kiến thức và phạm vi chương trình. | P0 | M10/M16 | 4 | — | PLANNED |
| FR04.06 | Đánh giá mức độ liên quan của tri thức truy xuất. | P0 | M10/M16 | 4 | — | PLANNED |
| FR04.07 | Cung cấp điều kiện áp dụng của tri thức toán học. | P0 | M10/M16 | 4 | — | PLANNED |
| FR04.08 | Truy xuất bổ sung hoặc điều chỉnh truy vấn khi cần thiết. | P0 | M10/M16 | 4 | — | PLANNED |
| FR04.09 | Cung cấp nguồn tham chiếu của tri thức được sử dụng. | P0 | M10/M16 | 4 | — | PLANNED |
| FR04.10 | Cho phép cập nhật và mở rộng kho tri thức mà không huấn luyện lại LLM. | P0 | M10/M16 | 4 | — | PLANNED |
| FR04.11 | Kết hợp truy xuất đơn vị tri thức với đoạn văn bản tài liệu gốc. | P1 | M10/M16 | 4 | — | PLANNED |
| FR04.12 | Phát hiện và cảnh báo tri thức có dấu hiệu mâu thuẫn. | P1 | M10/M16 | 4 | — | PLANNED |
| FR05.01 | Thực hiện suy luận dựa trên dữ kiện và kế hoạch giải toán. | P0 | M11/M15 | 1–3 | — | PLANNED |
| FR05.02 | Giải quyết bài toán nhiều bước và nhiều nhiệm vụ phụ thuộc. | P0 | M11/M15 | 1–3 | — | PLANNED |
| FR05.03 | Áp dụng định nghĩa, công thức và định lý phù hợp. | P0 | M11/M15 | 1–3 | — | PLANNED |
| FR05.04 | Xác định khi nào cần sử dụng công cụ toán học. | P0 | M11/M15 | 1–3 | — | PLANNED |
| FR05.05 | Lựa chọn công cụ phù hợp với nhiệm vụ. | P0 | M11/M15 | 1–3 | — | PLANNED |
| FR05.06 | Chuyển đổi yêu cầu toán học thành tham số đầu vào của công cụ. | P0 | M11/M15 | 1–3 | — | PLANNED |
| FR05.07 | Thực thi công cụ và tiếp nhận kết quả có cấu trúc. | P0 | M11/M15 | 1–3 | — | PLANNED |
| FR05.08 | Tích hợp kết quả công cụ vào lời giải. | P0 | M11/M15 | 1–3 | — | PLANNED |
| FR05.09 | Xử lý lỗi, timeout và kết quả không hợp lệ từ công cụ. | P0 | M11/M15 | 1–3 | — | PLANNED |
| FR05.10 | Lưu trữ kết quả trung gian và quan hệ phụ thuộc giữa các bước giải. | P0 | M11/M15 | 1–3 | — | PLANNED |
| FR05.11 | Cung cấp lời giải có cấu trúc để hỗ trợ kiểm chứng. | P0 | M11/M15 | 1–3 | — | PLANNED |
| FR05.12 | Hỗ trợ đăng ký và mở rộng tập công cụ toán học. | P0 | M11/M15 | 1–3 | — | PLANNED |
| FR05.13 | Phối hợp nhiều công cụ trong cùng một nhiệm vụ suy luận. | P0 | M11/M15 | 1–3 | — | PLANNED |
| FR05.14 | Xây dựng nhiều lời giải bằng các phương pháp khác nhau. | P1 | M11/M15 | 1–3 | — | PLANNED |
| FR06.01 | Kiểm chứng sự nhất quán giữa lời giải và dữ kiện đầu vào. | P0 | M12/M07 | 5 | — | PLANNED |
| FR06.02 | Kiểm chứng điều kiện áp dụng kiến thức toán học. | P0 | M12/M07 | 5 | — | PLANNED |
| FR06.03 | Kiểm chứng tính hợp lệ của các bước lập luận. | P0 | M12/M07 | 5 | — | PLANNED |
| FR06.04 | Kiểm chứng phép tính và biến đổi bằng công cụ toán học khi có thể. | P0 | M12/M07 | 5 | — | PLANNED |
| FR06.05 | Kiểm chứng tính đúng và đầy đủ của đáp án. | P0 | M12/M07 | 5 | — | PLANNED |
| FR06.06 | Phát hiện và phân loại lỗi. | P0 | M12/M07 | 5 | — | PLANNED |
| FR06.07 | Xác định bước giải hoặc dữ kiện gây lỗi khi có thể. | P0 | M12/M07 | 5 | — | PLANNED |
| FR06.08 | Cung cấp phản hồi có cấu trúc để hỗ trợ sửa lỗi. | P0 | M12/M07 | 5 | — | PLANNED |
| FR06.09 | Thực hiện sửa lỗi hoặc lập lại kế hoạch giải toán. | P0 | M12/M07 | 5 | — | PLANNED |
| FR06.10 | Kiểm chứng lại lời giải sau khi sửa. | P0 | M12/M07 | 5 | — | PLANNED |
| FR06.11 | Giới hạn số vòng lặp kiểm chứng và sửa lỗi. | P0 | M12/M07 | 5 | — | PLANNED |
| FR06.12 | Lưu lại các phiên bản lời giải và kết quả kiểm chứng. | P0 | M12/M07 | 5 | — | PLANNED |
| FR06.13 | Hỗ trợ kiểm chứng bằng phương pháp giải độc lập. | P1 | M12/M07 | 5 | — | PLANNED |
| FR06.14 | Hỗ trợ tiếp nhận, chuẩn hóa và kiểm chứng lời giải do người dùng cung cấp, báo cáo lỗi và phạm vi kiểm chứng. | P1 | M12/M07 | 5 | — | PLANNED |
| FR07.01 | Quản lý danh mục Agent và năng lực của từng Agent. | P0 | M04–M07 | 3–6 | — | PLANNED |
| FR07.02 | Lựa chọn Agent dựa trên đặc điểm bài toán. | P0 | M04–M07 | 3–6 | — | PLANNED |
| FR07.03 | Xác định thứ tự thực thi và quan hệ phụ thuộc. | P0 | M04–M07 | 3–6 | — | PLANNED |
| FR07.04 | Cho phép bỏ qua các thành phần không cần thiết. | P0 | M04–M07 | 3–6 | — | PLANNED |
| FR07.05 | Quản lý trạng thái thực thi dùng chung. | P0 | M04–M07 | 3–6 | — | PLANNED |
| FR07.06 | Điều chỉnh tuyến xử lý trong quá trình suy luận. | P0 | M04–M07 | 3–6 | — | PLANNED |
| FR07.07 | Điều phối truy xuất tri thức và sử dụng công cụ theo nhu cầu. | P0 | M04–M07 | 3–6 | — | PLANNED |
| FR07.08 | Điều phối quá trình kiểm chứng và sửa lỗi. | P0 | M04–M07 | 3–6 | — | PLANNED |
| FR07.09 | Nâng mức độ suy luận khi chiến lược hiện tại không hiệu quả. | P0 | M04–M07 | 3–6 | — | PLANNED |
| FR07.10 | Kiểm soát số lượt gọi LLM, công cụ và vòng lặp. | P0 | M04–M07 | 3–6 | — | PLANNED |
| FR07.11 | Xác định điều kiện kết thúc quá trình suy luận. | P0 | M04–M07 | 3–6 | — | PLANNED |
| FR07.12 | Lưu lại tuyến xử lý và căn cứ ra quyết định điều phối. | P0 | M04–M07 | 3–6 | — | PLANNED |
| FR07.13 | Hỗ trợ cấu hình nhiều chiến lược điều phối để thực nghiệm. | P0 | M04–M07 | 3–6 | — | PLANNED |
| FR07.14 | Thực thi song song các nhiệm vụ độc lập. | P1 | M04–M07 | 3–6 | — | PLANNED |
| FR08.01 | Phát hiện và phân loại các nguồn gây không chắc chắn. | P0 | M13/M06 | 5–6 | — | PLANNED |
| FR08.02 | Phát hiện dữ kiện thiếu hoặc không đầy đủ. | P0 | M13/M06 | 5–6 | — | PLANNED |
| FR08.03 | Phát hiện dữ kiện mơ hồ hoặc mâu thuẫn. | P0 | M13/M06 | 5–6 | — | PLANNED |
| FR08.04 | Xác định dữ kiện hoặc bước giải chưa chắc chắn. | P0 | M13/M06 | 5–6 | — | PLANNED |
| FR08.05 | Đánh giá mức độ ảnh hưởng của sự không chắc chắn đến lời giải. | P0 | M13/M06 | 5–6 | — | PLANNED |
| FR08.06 | Tổng hợp các tín hiệu đánh giá từ những thành phần liên quan. | P0 | M13/M06 | 5–6 | — | PLANNED |
| FR08.07 | Tự xử lý sự không chắc chắn khi có đủ khả năng và tài nguyên. | P0 | M13/M06 | 5–6 | — | PLANNED |
| FR08.08 | Yêu cầu người dùng làm rõ hoặc bổ sung dữ kiện. | P0 | M13/M06 | 5–6 | — | PLANNED |
| FR08.09 | Tiếp tục suy luận sau khi người dùng xác nhận dữ kiện. | P0 | M13/M06 | 5–6 | — | PLANNED |
| FR08.10 | Cung cấp lời giải có điều kiện và nêu rõ giả thiết bổ sung. | P0 | M13/M06 | 5–6 | — | PLANNED |
| FR08.11 | Cho phép từ chối đưa ra kết luận khi không đủ căn cứ. | P0 | M13/M06 | 5–6 | — | PLANNED |
| FR08.12 | Phân biệt giới hạn của hệ thống với tính không hợp lệ của bài toán. | P0 | M13/M06 | 5–6 | — | PLANNED |
| FR08.13 | Cung cấp trạng thái bất định và căn cứ đánh giá. | P0 | M13/M06 | 5–6 | — | PLANNED |
| FR08.14 | Lưu lại quá trình phát hiện và xử lý sự không chắc chắn. | P0 | M13/M06 | 5–6 | — | PLANNED |
| FR08.15 | Đánh giá và hiệu chỉnh độ tin cậy định lượng thông qua thực nghiệm. | P1 | M13/M06 | 5–6 | — | PLANNED |
| FR09.01 | Tổng hợp kết quả từ các thành phần suy luận. | P0 | M02/M03/M21 | 2–6 | — | PLANNED |
| FR09.02 | Cung cấp kết quả toán học có cấu trúc thống nhất. | P0 | M02/M03/M21 | 2–6 | — | PLANNED |
| FR09.03 | Cung cấp đáp án cuối cùng khi đủ căn cứ. | P0 | M02/M03/M21 | 2–6 | — | PLANNED |
| FR09.04 | Cung cấp lời giải từng bước có căn cứ toán học. | P0 | M02/M03/M21 | 2–6 | — | PLANNED |
| FR09.05 | Hiển thị biểu thức toán học bằng LaTeX. | P0 | M02/M03/M21 | 2–6 | — | PLANNED |
| FR09.06 | Cung cấp nguồn tham chiếu của tri thức được sử dụng. | P0 | M02/M03/M21 | 2–6 | — | PLANNED |
| FR09.07 | Cung cấp trạng thái, phương pháp và phạm vi kiểm chứng. | P0 | M02/M03/M21 | 2–6 | — | PLANNED |
| FR09.08 | Hiển thị các giả thiết, điều kiện và thông tin chưa chắc chắn. | P0 | M02/M03/M21 | 2–6 | — | PLANNED |
| FR09.09 | Hỗ trợ nhiều mức độ chi tiết của kết quả. | P0 | M02/M03/M21 | 2–6 | — | PLANNED |
| FR09.10 | Hỗ trợ đầu ra có thể xử lý bằng chương trình. | P0 | M02/M03/M21 | 2–6 | — | PLANNED |
| FR09.11 | Bảo đảm tính nhất quán giữa các định dạng đầu ra. | P0 | M02/M03/M21 | 2–6 | — | PLANNED |
| FR09.12 | Cung cấp bản ghi thực thi phục vụ phân tích và nghiên cứu. | P0 | M02/M03/M21 | 2–6 | — | PLANNED |
| FR09.13 | Diễn giải lời giải phù hợp với trình độ người dùng. | P1 | M02/M03/M21 | 2–6 | — | PLANNED |
| FR09.14 | Hiển thị nhiều phương pháp giải khác nhau nếu có. | P1 | M02/M03/M21 | 2–6 | — | PLANNED |
| FR09.15 | Xuất lời giải dưới dạng PDF hoặc tài liệu. | P2 | M02/M03/M21 | 2–6 | — | PLANNED |
| FR10.01 | Quản lý và nạp tập dữ liệu benchmark. | P0 | M19–M21/M17 | 7 | — | PLANNED |
| FR10.02 | Hỗ trợ đánh giá bài toán theo miền kiến thức, độ khó và phương thức đầu vào. | P0 | M19–M21/M17 | 7 | — | PLANNED |
| FR10.03 | Thực thi benchmark tự động trên nhiều bài toán. | P0 | M19–M21/M17 | 7 | — | PLANNED |
| FR10.04 | Đánh giá tự động đáp án khi có phương pháp kiểm tra phù hợp. | P0 | M19–M21/M17 | 7 | — | PLANNED |
| FR10.05 | Hỗ trợ đánh giá lời giải bằng rubric và kiểm tra thủ công. | P0 | M19–M21/M17 | 7 | — | PLANNED |
| FR10.06 | Cấu hình các mô hình, Agent và chiến lược xử lý khác nhau. | P0 | M19–M21/M17 | 7 | — | PLANNED |
| FR10.07 | Hỗ trợ so sánh baseline và thực hiện Ablation Study. | P0 | M19–M21/M17 | 7 | — | PLANNED |
| FR10.08 | Ghi nhận quá trình thực thi của các Agent và công cụ. | P0 | M19–M21/M17 | 7 | — | PLANNED |
| FR10.09 | Theo dõi số lượt gọi mô hình, công cụ và lượng token tiêu thụ. | P0 | M19–M21/M17 | 7 | — | PLANNED |
| FR10.10 | Theo dõi thời gian thực thi và chi phí ước tính. | P0 | M19–M21/M17 | 7 | — | PLANNED |
| FR10.11 | Ghi nhận lỗi và kết quả kiểm chứng, sửa lỗi. | P0 | M19–M21/M17 | 7 | — | PLANNED |
| FR10.12 | Lưu cấu hình, phiên bản và kết quả thực nghiệm. | P0 | M19–M21/M17 | 7 | — | PLANNED |
| FR10.13 | Tổng hợp kết quả theo các chỉ số đánh giá. | P0 | M19–M21/M17 | 7 | — | PLANNED |
| FR10.14 | Xuất dữ liệu thực nghiệm dưới dạng JSON hoặc CSV. | P0 | M19–M21/M17 | 7 | — | PLANNED |
| FR10.15 | Hỗ trợ checkpoint và tiếp tục benchmark bị gián đoạn. | P0 | M19–M21/M17 | 7 | — | PLANNED |
| FR10.16 | Trực quan hóa và so sánh kết quả thực nghiệm. | P1 | M19–M21/M17 | 7 | — | PLANNED |
| FR10.17 | Hỗ trợ LLM-as-a-Judge đối với những bài toán khó đánh giá tự động. | P1 | M19–M21/M17 | 7 | — | PLANNED |
| NFR01.01 | Lời giải phải nhất quán với dữ kiện bài toán. | — | M11/M12/M20 | 1–7 | — | PLANNED |
| NFR01.02 | Công thức và định lý phải được sử dụng đúng điều kiện. | — | M11/M12/M20 | 1–7 | — | PLANNED |
| NFR01.03 | Kết quả tính toán phải được kiểm chứng bằng công cụ khi khả thi. | — | M11/M12/M20 | 1–7 | — | PLANNED |
| NFR01.04 | Không tự bổ sung giả thiết thiếu căn cứ. | — | M11/M12/M20 | 1–7 | — | PLANNED |
| NFR01.05 | Phải thể hiện rõ phạm vi kiểm chứng và giới hạn của lời giải. | — | M11/M12/M20 | 1–7 | — | PLANNED |
| NFR01.06 | Chất lượng toán học phải được đo lường thông qua benchmark. | — | M11/M12/M20 | 1–7 | — | PLANNED |
| NFR02.01 | Xử lý lỗi API, timeout và rate limit. | — | M07/M14/M17 | 0–7 | — | PLANNED |
| NFR02.02 | Không để lỗi của một thành phần làm mất toàn bộ kết quả thực thi đã lưu. | — | M07/M14/M17 | 0–7 | — | PLANNED |
| NFR02.03 | Phát hiện đầu ra không hợp lệ của Agent và công cụ. | — | M07/M14/M17 | 0–7 | — | PLANNED |
| NFR02.04 | Có cơ chế retry giới hạn và phục hồi phù hợp. | — | M07/M14/M17 | 0–7 | — | PLANNED |
| NFR02.05 | Không thực thi vòng lặp suy luận vô hạn. | — | M07/M14/M17 | 0–7 | — | PLANNED |
| NFR02.06 | Cung cấp trạng thái lỗi rõ ràng khi không thể hoàn thành nhiệm vụ. | — | M07/M14/M17 | 0–7 | — | PLANNED |
| NFR03.01 | Hạn chế độ trễ phát sinh không cần thiết giữa các thành phần. | — | M05/M07/M21 | 0–7 | — | PLANNED |
| NFR03.02 | Hỗ trợ cấu hình timeout cho từng loại tác vụ. | — | M05/M07/M21 | 0–7 | — | PLANNED |
| NFR03.03 | Đo lường thời gian thực thi toàn hệ thống và từng thành phần. | — | M05/M07/M21 | 0–7 | — | PLANNED |
| NFR03.04 | Tránh thực thi lại các nhiệm vụ đã hoàn thành khi kết quả vẫn hợp lệ. | — | M05/M07/M21 | 0–7 | — | PLANNED |
| NFR03.05 | Đánh giá hiệu năng theo độ phức tạp của bài toán. | — | M05/M07/M21 | 0–7 | — | PLANNED |
| NFR04.01 | Hạn chế các lượt gọi LLM không cần thiết. | — | M05/M07/M14 | 0–7 | — | PLANNED |
| NFR04.02 | Kiểm soát lượng token được truyền giữa các Agent. | — | M05/M07/M14 | 0–7 | — | PLANNED |
| NFR04.03 | Ưu tiên công cụ local đối với những nhiệm vụ tính toán phù hợp. | — | M05/M07/M14 | 0–7 | — | PLANNED |
| NFR04.04 | Cho phép cấu hình giới hạn tài nguyên cho mỗi phiên suy luận. | — | M05/M07/M14 | 0–7 | — | PLANNED |
| NFR04.05 | Theo dõi chi phí theo bài toán và phiên thực nghiệm. | — | M05/M07/M14 | 0–7 | — | PLANNED |
| NFR04.06 | Ưu tiên giải pháp không bắt buộc phát sinh chi phí hạ tầng thường xuyên. | — | M05/M07/M14 | 0–7 | — | PLANNED |
| NFR05.01 | Các thành phần có trách nhiệm rõ ràng. | — | M03/M04/M18 | 0–7 | — | PLANNED |
| NFR05.02 | Hạn chế phụ thuộc trực tiếp giữa các Agent. | — | M03/M04/M18 | 0–7 | — | PLANNED |
| NFR05.03 | Cho phép thay thế mô hình LLM mà không thay đổi toàn bộ hệ thống. | — | M03/M04/M18 | 0–7 | — | PLANNED |
| NFR05.04 | Tách biệt prompt, configuration và logic nghiệp vụ. | — | M03/M04/M18 | 0–7 | — | PLANNED |
| NFR05.05 | Hỗ trợ kiểm thử độc lập các thành phần. | — | M03/M04/M18 | 0–7 | — | PLANNED |
| NFR06.01 | Cho phép bổ sung Agent mới. | — | M04/M15/M16 | 1–7 | — | PLANNED |
| NFR06.02 | Cho phép bổ sung công cụ toán học mới. | — | M04/M15/M16 | 1–7 | — | PLANNED |
| NFR06.03 | Cho phép mở rộng kho tri thức. | — | M04/M15/M16 | 1–7 | — | PLANNED |
| NFR06.04 | Cho phép bổ sung chiến lược Routing và Verification. | — | M04/M15/M16 | 1–7 | — | PLANNED |
| NFR06.05 | Không giới hạn kiến trúc cốt lõi vào chương trình THCS. | — | M04/M15/M16 | 1–7 | — | PLANNED |
| NFR06.06 | Cho phép bổ sung giao thức tích hợp như MCP mà vẫn tái sử dụng logic toán học. | — | M04/M15/M16 | 1–7 | — | PLANNED |
| NFR07.01 | Quản lý phiên bản tập dữ liệu, prompt và kho tri thức. | — | M17–M21 | 0–7 | — | PLANNED |
| NFR07.02 | Lưu cấu hình mô hình và chiến lược thực nghiệm. | — | M17–M21 | 0–7 | — | PLANNED |
| NFR07.03 | Bảo toàn kết quả thực nghiệm gốc. | — | M17–M21 | 0–7 | — | PLANNED |
| NFR07.04 | Cho phép chạy lại benchmark theo cấu hình đã lưu. | — | M17–M21 | 0–7 | — | PLANNED |
| NFR07.05 | Ghi nhận các yếu tố có thể ảnh hưởng đến khả năng tái lập. | — | M17–M21 | 0–7 | — | PLANNED |
| NFR08.01 | Mỗi phiên suy luận có định danh riêng. | — | M21 | 0–7 | — | PLANNED |
| NFR08.02 | Có khả năng truy vết các sự kiện thực thi. | — | M21 | 0–7 | — | PLANNED |
| NFR08.03 | Ghi nhận lỗi theo thành phần và nhiệm vụ. | — | M21 | 0–7 | — | PLANNED |
| NFR08.04 | Ghi nhận metrics liên quan đến hiệu năng và tài nguyên. | — | M21 | 0–7 | — | PLANNED |
| NFR08.05 | Hỗ trợ phân tích kết quả trung gian và lỗi lan truyền. | — | M21 | 0–7 | — | PLANNED |
| NFR09.01 | Không hard-code API Key trong mã nguồn. | — | M01/M07/M14/M15 | 0–7 | — | PLANNED |
| NFR09.02 | Không lưu API Key hoặc thông tin xác thực trong log. | — | M01/M07/M14/M15 | 0–7 | — | PLANNED |
| NFR09.03 | Kiểm tra và giới hạn dữ liệu đầu vào. | — | M01/M07/M14/M15 | 0–7 | — | PLANNED |
| NFR09.04 | Không cho phép Agent thực thi mã tùy ý. | — | M01/M07/M14/M15 | 0–7 | — | PLANNED |
| NFR09.05 | Kiểm tra tham số và giới hạn tài nguyên của công cụ. | — | M01/M07/M14/M15 | 0–7 | — | PLANNED |
| NFR09.06 | Xử lý nội dung đầu vào và tài liệu truy xuất như dữ liệu không đáng tin cậy. | — | M01/M07/M14/M15 | 0–7 | — | PLANNED |
| NFR09.07 | Hạn chế lưu trữ và truyền tải dữ liệu cá nhân không cần thiết. | — | M01/M07/M14/M15 | 0–7 | — | PLANNED |
| NFR09.08 | Minh bạch việc gửi đề bài hoặc hình ảnh đến nhà cung cấp LLM bên ngoài. | — | M01/M07/M14/M15 | 0–7 | — | PLANNED |
| NFR10.01 | Giao diện tiếp nhận đề toán đơn giản. | — | M01–M03 | 2–6 | — | PLANNED |
| NFR10.02 | Hỗ trợ hiển thị công thức rõ ràng. | — | M01–M03 | 2–6 | — | PLANNED |
| NFR10.03 | Thông báo lỗi bằng ngôn ngữ dễ hiểu. | — | M01–M03 | 2–6 | — | PLANNED |
| NFR10.04 | Cho phép bổ sung dữ kiện khi hệ thống yêu cầu. | — | M01–M03 | 2–6 | — | PLANNED |
| NFR10.05 | Phân biệt kết quả đã kiểm chứng và chưa kiểm chứng. | — | M01–M03 | 2–6 | — | PLANNED |
| NFR11.01 | Hỗ trợ triển khai trên máy tính cá nhân. | — | M18 | 0–7 | — | PLANNED |
| NFR11.02 | Quản lý phiên bản thư viện và môi trường thực thi. | — | M18 | 0–7 | — | PLANNED |
| NFR11.03 | Hạn chế phụ thuộc vào phần cứng chuyên dụng. | — | M18 | 0–7 | — | PLANNED |
| NFR11.04 | Cung cấp tài liệu cấu hình và hướng dẫn khởi chạy. | — | M18 | 0–7 | — | PLANNED |
| NFR12.01 | Hỗ trợ benchmark trên nhiều bài toán. | — | M07/M14/M19 | 0–7 | — | PLANNED |
| NFR12.02 | Cho phép cấu hình số lượng tác vụ đồng thời. | — | M07/M14/M19 | 0–7 | — | PLANNED |
| NFR12.03 | Kiểm soát rate limit của nhà cung cấp API. | — | M07/M14/M19 | 0–7 | — | PLANNED |
| NFR12.04 | Có khả năng mở rộng tải xử lý trong tương lai. | — | M07/M14/M19 | 0–7 | — | PLANNED |
| BR01.01 | Không tự ý thay đổi dữ kiện được cho trong đề bài. | — | M06/M08 | 2–6 | — | PLANNED |
| BR01.02 | Phân biệt dữ kiện gốc, dữ kiện quan sát, dữ kiện suy ra và giả thiết bổ sung. | — | M06/M08 | 2–6 | — | PLANNED |
| BR01.03 | Không suy ra quan hệ hình học chỉ từ tỷ lệ hoặc hình dáng minh họa. | — | M06/M08 | 2–6 | — | PLANNED |
| BR01.04 | Khi văn bản và hình ảnh mâu thuẫn, phải ghi nhận mâu thuẫn thay vì tự ý chọn dữ kiện. | — | M06/M08 | 2–6 | — | PLANNED |
| BR01.05 | Dữ kiện bổ sung từ người dùng phải được ghi nhận nguồn gốc. | — | M06/M08 | 2–6 | — | PLANNED |
| BR01.06 | Khi dữ kiện thay đổi, các kết quả phụ thuộc phải được đánh giá lại. | — | M06/M08 | 2–6 | — | PLANNED |
| BR02.01 | Tri thức áp dụng phải phù hợp với nhiệm vụ hiện tại. | — | M10/M12 | 4–5 | — | PLANNED |
| BR02.02 | Các điều kiện áp dụng định lý phải được thỏa mãn hoặc chứng minh. | — | M10/M12 | 4–5 | — | PLANNED |
| BR02.03 | Không tự tạo nguồn tham chiếu không tồn tại. | — | M10/M12 | 4–5 | — | PLANNED |
| BR02.04 | Tri thức truy xuất không được mặc định là chính xác chỉ vì có độ tương đồng cao. | — | M10/M12 | 4–5 | — | PLANNED |
| BR02.05 | Khi phát hiện tri thức mâu thuẫn, không được sử dụng một cách thiếu căn cứ. | — | M10/M12 | 4–5 | — | PLANNED |
| BR03.01 | Các bước giải phải dựa trên dữ kiện hoặc kết quả trung gian hợp lệ. | — | M11/M12/M15 | 1–5 | — | PLANNED |
| BR03.02 | Phải bảo toàn điều kiện xác định trong quá trình biến đổi. | — | M11/M12/M15 | 1–5 | — | PLANNED |
| BR03.03 | Phải phân biệt phép biến đổi tương đương và phép suy ra một chiều. | — | M11/M12/M15 | 1–5 | — | PLANNED |
| BR03.04 | Phải xét các trường hợp cần thiết để bảo đảm tính đầy đủ. | — | M11/M12/M15 | 1–5 | — | PLANNED |
| BR03.05 | Không sử dụng kết quả cần chứng minh làm giả thiết nếu không có căn cứ hợp lệ. | — | M11/M12/M15 | 1–5 | — | PLANNED |
| BR03.06 | Phải bảo toàn đơn vị đo và miền giá trị liên quan. | — | M11/M12/M15 | 1–5 | — | PLANNED |
| BR04.01 | Chỉ được thực thi các công cụ đã đăng ký. | — | M07/M15 | 1–2 | — | PLANNED |
| BR04.02 | Tham số phải được kiểm tra trước khi thực thi. | — | M07/M15 | 1–2 | — | PLANNED |
| BR04.03 | Kết quả công cụ phải được diễn giải đúng ngữ nghĩa toán học. | — | M07/M15 | 1–2 | — | PLANNED |
| BR04.04 | Không coi kết quả công cụ là bằng chứng cho toàn bộ lời giải. | — | M07/M15 | 1–2 | — | PLANNED |
| BR04.05 | Kết quả thực thi thất bại không được sử dụng như kết quả hợp lệ. | — | M07/M15 | 1–2 | — | PLANNED |
| BR04.06 | Không được thực thi mã tùy ý do LLM hoặc người dùng cung cấp. | — | M07/M15 | 1–2 | — | PLANNED |
| BR05.01 | Lời giải phải trải qua cơ chế kiểm chứng phù hợp trước khi được đánh dấu VERIFIED. | — | M12 | 5 | — | PLANNED |
| BR05.02 | Kiểm chứng phải xét cả tính đúng và tính đầy đủ khi phù hợp. | — | M12 | 5 | — | PLANNED |
| BR05.03 | Không đánh dấu VERIFIED nếu còn lỗi ảnh hưởng đến kết quả chưa được giải quyết. | — | M12 | 5 | — | PLANNED |
| BR05.04 | Kết quả kiểm chứng phải gắn với phiên bản lời giải tương ứng. | — | M12 | 5 | — | PLANNED |
| BR05.05 | Kiểm chứng một phần không đồng nghĩa với kiểm chứng toàn bộ. | — | M12 | 5 | — | PLANNED |
| BR05.06 | Đánh giá bằng LLM không được mô tả là chứng minh hình thức bằng máy. | — | M12 | 5 | — | PLANNED |
| BR06.01 | Mọi sửa đổi phải hướng đến giải quyết lỗi đã phát hiện hoặc cải thiện lời giải có căn cứ. | — | M06/M12 | 5 | — | PLANNED |
| BR06.02 | Phải đánh giá lại các bước phụ thuộc vào bước được sửa. | — | M06/M12 | 5 | — | PLANNED |
| BR06.03 | Lời giải sau khi sửa phải được kiểm chứng lại. | — | M06/M12 | 5 | — | PLANNED |
| BR06.04 | Không vượt quá giới hạn số vòng sửa lỗi đã cấu hình. | — | M06/M12 | 5 | — | PLANNED |
| BR06.05 | Phải bảo toàn thông tin cần thiết để đối chiếu phiên bản trước và sau khi sửa. | — | M06/M12 | 5 | — | PLANNED |
| BR07.01 | Chỉ được điều phối đến các Agent và năng lực hợp lệ. | — | M04–M07 | 3–5 | — | PLANNED |
| BR07.02 | Không thực thi nhiệm vụ khi các điều kiện phụ thuộc bắt buộc chưa được đáp ứng. | — | M04–M07 | 3–5 | — | PLANNED |
| BR07.03 | Không bỏ qua các bước kiểm chứng bắt buộc chỉ để tiết kiệm chi phí. | — | M04–M07 | 3–5 | — | PLANNED |
| BR07.04 | Không vượt quá giới hạn tài nguyên đã cấu hình. | — | M04–M07 | 3–5 | — | PLANNED |
| BR07.05 | Khi đạt giới hạn tài nguyên, phải kết thúc hoặc chuyển sang cơ chế xử lý bất định phù hợp. | — | M04–M07 | 3–5 | — | PLANNED |
| BR07.06 | Quyết định điều phối phải có khả năng truy vết. | — | M04–M07 | 3–5 | — | PLANNED |
| BR08.01 | Không tự ý lựa chọn dữ kiện mơ hồ nếu sự lựa chọn ảnh hưởng đến đáp án. | — | M13 | 5–6 | — | PLANNED |
| BR08.02 | Giả thiết bổ sung phải được trình bày rõ ràng. | — | M13 | 5–6 | — | PLANNED |
| BR08.03 | Không khẳng định bài toán vô nghiệm chỉ vì hệ thống không tìm được lời giải. | — | M13 | 5–6 | — | PLANNED |
| BR08.04 | Phải phân biệt bài toán thiếu dữ kiện với bài toán có nhiều nghiệm hợp lệ. | — | M13 | 5–6 | — | PLANNED |
| BR08.05 | Không biểu diễn độ tự tin chưa hiệu chỉnh thành xác suất đúng. | — | M13 | 5–6 | — | PLANNED |
| BR08.06 | Khi không đủ căn cứ, phải làm rõ, trả lời có điều kiện hoặc từ chối kết luận. | — | M13 | 5–6 | — | PLANNED |
| BR09.01 | Các định dạng đầu ra phải sử dụng chung kết quả toán học chuẩn hóa. | — | M02/M03 | 2–6 | — | PLANNED |
| BR09.02 | Việc định dạng không được làm thay đổi nội dung toán học. | — | M02/M03 | 2–6 | — | PLANNED |
| BR09.03 | Không che giấu lỗi, giả thiết hoặc giới hạn kiểm chứng có ảnh hưởng đến đáp án. | — | M02/M03 | 2–6 | — | PLANNED |
| BR09.04 | Không nâng trạng thái kiểm chứng khi chưa thực hiện kiểm chứng bổ sung. | — | M02/M03 | 2–6 | — | PLANNED |
| BR09.05 | Lời giải phải phù hợp với yêu cầu và phạm vi kiến thức của bài toán. | — | M02/M03 | 2–6 | — | PLANNED |
| BR10.01 | Các cấu hình so sánh phải sử dụng điều kiện thực nghiệm phù hợp và được ghi nhận. | — | M19/M20/M21 | 7 | — | PLANNED |
| BR10.02 | Không sử dụng đáp án chuẩn của tập test làm dữ kiện đầu vào cho quá trình giải toán. | — | M19/M20/M21 | 7 | — | PLANNED |
| BR10.03 | Không điều chỉnh hệ thống dựa trên kết quả tập test cuối cùng rồi tiếp tục coi đó là đánh giá độc lập. | — | M19/M20/M21 | 7 | — | PLANNED |
| BR10.04 | Không tự ý thay đổi dữ liệu kết quả thực nghiệm gốc. | — | M19/M20/M21 | 7 | — | PLANNED |
| BR10.05 | Phải ghi nhận trường hợp lỗi, timeout và abstention trong kết quả đánh giá. | — | M19/M20/M21 | 7 | — | PLANNED |
| BR10.06 | Khi tiếp tục benchmark, phải bảo đảm cấu hình và phiên bản dữ liệu tương thích. | — | M19/M20/M21 | 7 | — | PLANNED |
| BR10.07 | Không trình bày số liệu giả lập hoặc ước lượng như kết quả thực nghiệm thực tế. | — | M19/M20/M21 | 7 | — | PLANNED |
| BR11.01 | Không đưa thông tin xác thực vào mã nguồn, prompt hoặc log. | — | M07/M14/M15 | 0–7 | — | PLANNED |
| BR11.02 | Nội dung đề bài và tài liệu truy xuất không được phép ghi đè chính sách thực thi của hệ thống. | — | M07/M14/M15 | 0–7 | — | PLANNED |
| BR11.03 | Không gửi dữ liệu không cần thiết đến nhà cung cấp dịch vụ bên ngoài. | — | M07/M14/M15 | 0–7 | — | PLANNED |
| BR11.04 | Không cho phép Agent tự mở rộng quyền thực thi công cụ. | — | M07/M14/M15 | 0–7 | — | PLANNED |
