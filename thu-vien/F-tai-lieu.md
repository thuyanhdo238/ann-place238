# F · Tài liệu Claude

[← Mục lục](README.md)

## F1
### Skills trong Claude Code · 📖
- **Ý chính:**
  - Skill = thư mục có `SKILL.md` (hướng dẫn) + file phụ (script, mẫu). Claude tự dùng khi hợp, hoặc gọi `/tên-skill`.
  - Chỉ phần mô tả luôn nạp; ruột skill nạp khi dùng → tài liệu dài nên tách thành skill thay vì nhồi vào `CLAUDE.md`.
  - Chuẩn mở **Agent Skills**: cùng skill chạy được với Claude, Codex, Gemini CLI, Copilot.
  - Tạo skill khi cứ phải dán đi dán lại cùng một hướng dẫn/quy trình.
- **Đặt skill ở đâu:**

| Nơi đặt | Dùng được ở |
|---|---|
| **Tài khoản claude.ai** | App điện thoại, claude.ai, Cowork, cloud, Claude Code khi đăng nhập — **hợp nhất với Thuy Anh** |
| `.claude/skills/` trong repo | Claude Code mở trong repo đó (kể cả phiên cloud), AI khác đọc repo |
| `~/.claude/skills/` trên máy | Chỉ Claude Code trên máy đó |

- **Nguồn:** https://code.claude.com/docs/en/skills

## F2
### Thư viện prompt Claude Code — 6 nguyên tắc · 📖
1. **Nói kết quả muốn có**, không chỉ từng bước.
2. **Cho cách tự kiểm** (chạy thử, so sánh, xác nhận) để Claude tự sửa tới khi đạt.
3. **Chỉ vào mẫu có sẵn** ("giống trang X").
4. **Đặt chỉ tiêu đo được** ("dưới 200KB", "5 tin").
5. **Đưa tài liệu thật** (lỗi, ảnh, file qua `@`).
6. **Nói dạng câu trả lời** (định dạng, độ dài, ai đọc).

Prompt dùng tốt → lưu thành skill; quy ước Claude học được → ghi vào `CLAUDE.md`. Việc lớn/rủi ro → dùng plan mode xem trước danh sách file sẽ sửa.
Phiếu việc của Ann Place đã theo nguyên tắc 1–4 (Việc · Đạt khi · tham khảo). Prompt mẫu áp dụng: [G-prompt.md](G-prompt.md).
- **Nguồn:** https://code.claude.com/docs/en/prompt-library · Khóa học miễn phí: https://academy.claude.com/courses/claude-code-in-action

## F3
### Hướng dẫn Claude Motion · 📖
- Hoạt hình ngắn tạo bằng code từ prompt (không phải mô hình video), sửa một chữ/số/thời lượng mà phần còn lại giữ nguyên; xuất MP4; lưu ở tab Artifacts; tính vào hạn mức gói.
- **Chỉ có ở gói Team/Enterprise (beta).** Tài khoản Thuy Anh (29/10/2026) chưa có — dùng HyperFrames ([B1](B-video.md#b1)).
- Mẹo: nói rõ ai xem, chiếu ở đâu, dài bao lâu; đính kèm dữ liệu/hình thật.
- **Nguồn:** https://support.claude.com (bài "Get started with Claude Motion")

## F4
### Knowledge-work-plugins (Anthropic) · 📖
- Kho ~15 plugin nghề: productivity ✓, design ✓ (đã có), marketing, data, bio-research, product-management, enterprise-search, engineering, operations, finance, legal, sales, customer-support, HR, small-business.
- Mỗi plugin = bộ skill gắn thêm cho Claude (không phải nhân viên riêng).
- **Hợp với Thuy Anh:** marketing (E1), data (D4), bio-research phần chọn đề tài + Consensus (D2, D3). Còn lại hầu như không cần.
- **Nguồn:** https://github.com/anthropics/knowledge-work-plugins
