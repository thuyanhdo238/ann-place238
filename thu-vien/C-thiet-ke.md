# C · Thiết kế

[← Mục lục](README.md)

## C1
### Editable Design · ✅ đã cài · đánh giá 29/10/2026
- **Là gì:** Skill (kèm bài báo arXiv 2609.04034) tạo poster, bìa, infographic, ảnh chiến dịch, social card dưới dạng HTML **chữ thật, lớp tách rời**, kèm trình chỉnh sửa bằng chuột, ảnh PNG, file phân lớp động và "Design Replay" ghi lại quá trình agent thiết kế. Apache 2.0.
- **Hợp với Ann Place:** Card và poster cho SaLu mà art director sửa tiếp được từng lớp. Design Replay là tư liệu hay cho nghiên cứu AI trong thiết kế (bài FISAT).
- **Đã thử 29/10/2026:** chạy được ngoài Codex; kiểm tra môi trường đạt sau khi chỉ đường Chromium. Font kit có **6 font hỗ trợ tiếng Việt**: Fraunces, Space Grotesk, Unbounded, Roboto Condensed, Noto Sans SC, Noto Serif SC.
- **Lưu ý:** Viết cho Codex trước; phần tạo ảnh minh họa phụ thuộc nền tảng — không có thì chỉ dùng chữ, hình khối và ảnh mình đưa vào. Design Replay có thể chứa prompt và đường dẫn file — xem lại trước khi chia sẻ.
- **Cài lần đầu trên máy:** trong `.claude/skills/editable-design/` chạy `npm ci --prefix scripts`, `scripts/install-font-kit.sh`, `scripts/doctor.sh` (Node 22.12+). Không thấy Chrome thì đặt `EDITABLE_DESIGN_BROWSER=/đường/dẫn/chrome`.
- **Cách dùng:** `/editable-design làm social card 4:5 cho SaLu, chủ đề "Hoa văn sóng nước thời Lý", nền giấy, dùng hình assets/salu-kol.png`
- **Nguồn:** https://github.com/yejy53/Editable-Design

## C2
### Paper Fig · ⛔ cần Codex
- **Là gì:** Skill biến đoạn mô tả phương pháp thành sơ đồ quy trình cho bài báo, xuất PowerPoint chỉnh được.
- **Hợp với Ann Place:** Rất hợp sơ đồ phương pháp cho đề cương PhD và bài FISAT.
- **Lưu ý:** Cần bộ công cụ nội bộ của Codex (`@oai/artifact-tool`) + tạo ảnh OpenAI → chỉ chạy trong Codex/ChatGPT trả phí. **Thay thế:** nhờ Claude dựng sơ đồ dạng PowerPoint (skill pptx) hoặc artifact.
- **Nguồn:** https://github.com/yejy53/Editable-Design/tree/main/skills/paper-fig

## C3
### html-to-pptx · 📦
- **Là gì:** Chuyển thiết kế HTML (kể cả từ Editable Design) sang PowerPoint, mỗi phần tử chọn riêng được.
- **Khi nào lấy ra:** khi cần đưa poster/card vào bài giảng PowerPoint để chỉnh tiếp.
- **Nguồn:** https://github.com/yejy53/Editable-Design/tree/main/skills/html-to-pptx

## C4
### Plugin Design (Anthropic) · 🟢 đã có trong tài khoản
- **Là gì:** Skill phê bình thiết kế, design system, UX copy, kiểm tra accessibility (WCAG), handoff cho lập trình, tổng hợp nghiên cứu người dùng (research-synthesis).
- **Cách dùng:** trong chat Claude: "review thiết kế này", "audit accessibility trang index.html".
- **Nguồn:** https://github.com/anthropics/knowledge-work-plugins/tree/main/design
