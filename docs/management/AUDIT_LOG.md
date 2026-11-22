# Pre-Implementation Audit — MATHK

**Trạng thái:** Đang kiểm tra; chưa đóng planning baseline.

| ID | Nội dung | Trạng thái |
|---|---|---|
| AUD-001–004 | Đồng bộ cấu trúc, dependency, công nghệ, tham chiếu | Đã cập nhật tài liệu |
| AUD-005 | Traceability Matrix 259 ID; MVP C/D; Ground Truth chỉ Evaluator | Đã khởi tạo; coverage từng ID chưa xác minh |
| AUD-006 | Mermaid static screening | Đã sàng lọc 227 sơ đồ; parser/render chưa chạy |

## Architecture Audit
Rà soát cấp thiết kế: giữ Modular Monolith, Lightweight Hexagonal, LangGraph, 5 Agent, controlled shared state và persistence hiện hành. Chưa có bằng chứng implementation.

| ID | Tiêu chí kiểm thử bắt buộc khi triển khai | Phase |
|---|---|---|
| ARCH-001 | Quyền cập nhật state; từ chối stale state version | 3 |
| ARCH-002 | Ngân sách chung với nested retry SDK/proxy/Gateway | 2–3 |
| ARCH-003 | Recovery khi gián đoạn giữa API call, DB commit và checkpoint | 3, 7 |

## Next Action
Kiểm tra Mermaid; ghi rõ giới hạn kiểm chứng render; hoàn thiện System Design baseline sau audit. Research 02 vẫn tạm hoãn. Chưa bắt đầu Phase 0.

## Mermaid screening
01:26; 03:140; 04:14; 05:12; 06:8; 07:13; 08:14. Tổng 227. Kiểm tra header loại sơ đồ, cặp dấu ngoặc kép theo số lượng, fence Markdown và block không rỗng; không phát hiện lỗi theo các phép kiểm tra này. UC03/06/15 có activity tương ứng ngay sau mô tả; thứ tự toàn bộ use case chưa audit. Không phải kiểm tra parser hoặc render thực tế. Đề xuất giao Codex task kiểm tra toàn bộ Mermaid bằng parser/renderer trước đóng baseline chính thức; báo file/section/lỗi và không tự sửa ngữ nghĩa. Research 02 ngoài phạm vi.
