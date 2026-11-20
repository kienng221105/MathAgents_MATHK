# 02 — RESEARCH

**Dự án:** MATHK  
**Phiên bản:** 0.1  
**Trạng thái:** Đang thảo luận  
**Requirements Baseline:** v1.0 (558b25e2d1789f0ae526a4d1211be2febd0eadd6)

## 1. Research Background — Bối cảnh nghiên cứu

### 1.1. Định hướng nghiên cứu

Tên đề tài dự kiến: **Adaptive Neuro-Symbolic Multi-Agent System for Multimodal Mathematical Reasoning** (Hệ thống đa tác tử thần kinh–ký hiệu thích ứng cho suy luận toán học đa phương thức).

MATHK nằm tại giao điểm của Mathematical Reasoning, Multimodal Understanding, Neuro-Symbolic AI, Multi-Agent Systems, Adaptive Routing, Agentic RAG và Verification.

Phân biệt Established (nhận định có căn cứ nghiên cứu), Hypothesis (giả thuyết cần kiểm chứng) và Proposed (phương pháp đề xuất). Không coi việc kết hợp các kỹ thuật hiện có là bằng chứng cho tính mới.

### 1.2. Các hướng tiếp cận

| Hướng | Đặc điểm |
|---|---|
| Symbolic Mathematics | Thuật toán và quy tắc tính toán, biến đổi và giải phương trình. |
| Neural Mathematical Reasoning | Mạng neural và LLM hiểu đề bài và sinh lời giải. |
| Structured Reasoning | Phân rã, lập kế hoạch và khám phá hướng giải. |
| Neuro-Symbolic Reasoning | Kết hợp LLM với công cụ và suy luận ký hiệu. |
| Multimodal Mathematical Reasoning | Khai thác văn bản, hình ảnh, đồ thị, biểu đồ và ký hiệu. |
| Agentic Mathematical Reasoning | Tổ chức suy luận bằng Agent, công cụ, truy xuất, kiểm chứng và điều phối. |

Các hướng có thể kết hợp, không nhất thiết thay thế nhau theo thời gian. MATHK hướng đến ba nhóm cuối.

### 1.3. Vấn đề nghiên cứu và căn cứ ban đầu

- **P01 — Multimodal Understanding:** OCR không đồng nghĩa với hiểu dữ kiện trực quan. MathVista [REF001] và MathVerse [REF002] cung cấp benchmark và động lực nghiên cứu khả năng hiểu hình ảnh. Ví dụ, tam giác có hai cạnh 3 và 4 chỉ cho phép kết luận cạnh còn lại bằng 5 theo Pythagoras khi có giả thiết góc vuông giữa hai cạnh.
- **P02 — Multi-step Reasoning và P03 — Mathematical Computation:** PAL [REF003] minh họa cách chuyển một phần tác vụ tính toán sang môi trường thực thi chương trình. MATHK đề xuất công cụ toán học đăng ký trước, kiểm soát tham số và Direct Function Calling thay vì thực thi mã tùy ý.
- **P04 — Knowledge Grounding:** Truy xuất công thức, định lý, điều kiện áp dụng và nguồn tham chiếu. RAG [REF004] là nền tảng tham khảo; hiệu quả của Agentic RAG đối với tri thức toán học cần thực nghiệm.
- **P05 — Verification & Self-correction:** Các nghiên cứu [REF005–REF007] cho thấy hạn chế của tự sửa lỗi không có phản hồi đáng tin cậy và tầm quan trọng của phát hiện, định vị lỗi. MATHK đề xuất Hybrid Verification kết hợp Symbolic Feedback và Semantic Feedback, Dependency-aware Correction và kiểm chứng lại.
- **P06 — Reasoning Efficiency:** Nhiều Agent và vòng kiểm chứng có thể tăng chi phí. RouteLLM [REF008] là công trình tham khảo về cân bằng chất lượng và chi phí thông qua Model Routing. MATHK đề xuất Agent Routing (lựa chọn tác tử/nhiệm vụ/tuyến suy luận), không bắt buộc nhiều mô hình. Ba mức Lightweight, Structured và Corrective theo Requirements; Corrective có thể được kích hoạt khi phát hiện lỗi.
- **P07 — Uncertainty Awareness:** UMWP [REF009] là hướng tham khảo về đề toán không thể trả lời. Phân biệt bài toán vô nghiệm, thiếu dữ kiện, mâu thuẫn, nhiều nghiệm và giới hạn suy luận của hệ thống. Đề xuất Evidence-based Uncertainty Handling.

### 1.4. Tổng hợp động lực

| Vấn đề | Hướng đề xuất |
|---|---|
| P01 | Structured Multimodal Representation |
| P02 | Planning & Multi-Agent Reasoning |
| P03 | Neuro-Symbolic Tool Use |
| P04 | Agentic RAG |
| P05 | Hybrid Verification & Dependency-aware Correction |
| P06 | Adaptive Agent Routing |
| P07 | Evidence-based Uncertainty Handling |

### 1.5. Định vị nghiên cứu đề xuất

| Tầng | Vai trò |
|---|---|
| 1 — Ứng viên đóng góp trọng tâm | Adaptive Routing & Verification-guided Reasoning: điều phối theo đặc điểm bài toán, trạng thái thực thi, kết quả kiểm chứng và giới hạn tài nguyên. |
| 2 — Phương pháp hỗ trợ | Multimodal Understanding, Agentic RAG, Uncertainty Handling. |
| 3 — Nền tảng kỹ thuật | LLM, Multi-Agent, SymPy, Tool Calling, Shared State. |

Giữ nguyên bảy vấn đề P01–P07 và toàn bộ Research Objectives đã phê duyệt. Adaptive Routing kết hợp Verification-guided Reasoning chỉ là ứng viên đóng góp trọng tâm, chưa xác nhận tính mới cho đến khi hoàn thành Literature Review và Research Gap.

### 1.6. Tài liệu tham khảo ban đầu

| ID | Công trình | Nơi công bố |
|---|---|---|
| REF001 | [MathVista](https://arxiv.org/abs/2310.02255) | ICLR 2024 |
| REF002 | [MathVerse](https://arxiv.org/abs/2403.14624) | ECCV 2024 |
| REF003 | [PAL: Program-aided Language Models](https://arxiv.org/abs/2211.10435) | ICML 2023 |
| REF004 | [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) | NeurIPS 2020 |
| REF005 | [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) | ICLR 2024 |
| REF006 | [When Can LLMs Actually Correct Their Own Mistakes?](https://doi.org/10.1162/tacl_a_00713) | TACL 2024 |
| REF007 | [LLMs Cannot Find Reasoning Errors, but Can Correct Them Given the Error Location](https://aclanthology.org/2024.findings-acl.826.pdf) | Findings of ACL 2024 |
| REF008 | [RouteLLM](https://arxiv.org/abs/2406.18665) | ICLR 2025 |
| REF009 | [Benchmarking Hallucination in LLMs Based on Unanswerable Math Word Problem](https://aclanthology.org/2024.lrec-main.196.pdf) | LREC-COLING 2024 |

Danh sách khảo sát sơ bộ, chưa thẩm định toàn văn từng bài. Cần kiểm tra lại metadata, liên kết và bổ sung công trình 2025–2026 tại Literature Review trước khi xác định Research Gap.

## 2. Research Questions

*Chưa chốt.*

## 3. Literature Review

*Chưa chốt.*

## 4. Comparative Analysis

*Chưa chốt.*

## 5. Research Gap

*Chưa chốt.*

## 6. Proposed Method

*Chưa chốt.*

## 7. Research Novelty

*Chưa chốt.*

## 8. Research Hypotheses

*Chưa chốt.*

## 9. Research Methodology

*Chưa chốt.*

## 10. Expected Contributions

*Chưa chốt.*

## 11. Research Limitations

*Chưa chốt.*

## 12. References

*Chưa chốt; xem danh sách ban đầu tại mục 1.6.*
