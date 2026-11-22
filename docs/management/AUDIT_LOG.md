# Pre-Implementation Audit — MATHK

**Trạng thái:** Đang kiểm tra; chưa đóng planning baseline.

| ID | Nội dung | Trạng thái |
|---|---|---|
| AUD-001–004 | Đồng bộ cấu trúc, dependency, công nghệ, tham chiếu | Đã cập nhật tài liệu |
| AUD-005 | Traceability Matrix 259 ID; MVP C/D; Ground Truth chỉ Evaluator | Đã khởi tạo; coverage từng ID chưa xác minh |
| AUD-006 | Mermaid parser/render 227 sơ đồ | PASS theo báo cáo Codex PRE-001; chưa kiểm tra SVG trực quan |

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

## PRE-001 — Mermaid Validation
Owner đã phê duyệt giao task kiểm chứng. Trạng thái ASSIGNED (prompt đã cung cấp cho Owner chuyển tiếp; chưa xác nhận Codex chạy). Phạm vi 7 tài liệu, 227 sơ đồ dự kiến, loại trừ 02 Research. Trích xuất file/heading/dòng, dùng parser và renderer thực tế, ghi tool versions/lệnh/kết quả từng file và từng lỗi, review UC03/06/15. Không sửa thiết kế, không thêm dependency chính thức, không commit/push, không bắt đầu Phase 0. AC: đầy đủ extraction/count/parse/render attempt/error evidence/semantic review/repo integrity/report. Chờ Owner chuyển báo cáo Codex để ChatGPT review. Sau nghiệm thu mới chốt System Design và khởi tạo bộ quản lý.

## PRE-001 — Technical Lead Review (2026-11-22)
**Kết luận:** ACCEPTED theo báo cáo Codex; đính chính bảng báo cáo dòng 05_IMPLEMENTATION.md: Render PASS phải là 12, NOT_RUN là 0 (tổng 227/227). AC01–AC08 PASS theo báo cáo. Mermaid 12.3.0, CLI 12.2.0, Node 24.14.0, Chrome headless 157; mỗi sơ đồ gọi mermaid.parse() và mermaid.render() trong Chrome, 227 SVG không rỗng, kiểm tra tuần tự ~2m37s. UC03/06/15 được review; ghi nhận diễn đạt UC03 có thể làm rõ sau, không chặn nghiệm thu. Codex báo Git main sạch tại 93268719cafdc62abd612681af98697e56aa12a1, không commit/push. Không kiểm chứng độc lập SVG vì file tạm đã xóa; không coi render PASS là semantic/visual audit. Research 02 ngoài scope. Tiếp theo: chốt System Design baseline theo quyết định Owner, khởi tạo tài liệu quản lý, sau đó Phase 0.
