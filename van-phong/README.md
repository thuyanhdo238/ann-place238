# Văn phòng Ann Place — sổ điều phối

Bộ sổ này phỏng theo workflow của dự án mã nguồn mở [van-phong-ao-3d](https://github.com/vinaichatbot-rgb/van-phong-ao-3d), chỉnh lại cho đội 5 AI của Ann Place. Đội không dùng chung một máy, nên mọi trao đổi đi qua **file trong repo này**, không qua trí nhớ của từng AI.

> **Chat sẽ quên, chỉ file là còn.** Việc chưa ghi vào sổ coi như chưa giao. Việc chưa có file hay link thật coi như chưa xong.

## Đội

| Vai | AI | Phòng | Làm gì |
|---|---|---|---|
| Trưởng nhóm | Claude | Phòng Điều hành | Lên kế hoạch, giao việc, tổng hợp, duyệt bản cuối |
| Radar | Grok | Phòng Radar | Quét tin, cơ hội, deadline mỗi sáng |
| Họa sĩ SaLu | Gemini (Google AI Studio) | Phòng Art | Hình ảnh, nhân vật, nội dung hình cho SaLu |
| Thiết kế | ChatGPT | Phòng Design | Giao diện, CSS (nhánh `design`, chỉ DESIGN ZONE) |
| Kỹ thuật | GitHub Copilot | Phòng DevOps | Workflow, script, review PR |

Chi tiết ở [DOI-NGU.md](DOI-NGU.md). Quyền ở [CAP-BAC.md](CAP-BAC.md). Luật ở [NOI-QUY.md](NOI-QUY.md).

## Vòng làm việc (một ngày của văn phòng)

1. **Thuy Anh** ghi việc ưu tiên vào [`../pipeline.md`](../pipeline.md). Đây là nguồn duy nhất cho thứ tự việc.
2. **Claude** đọc pipeline, chia việc lớn thành **gói** (`goi/<tên-gói>/`), rồi bỏ **phiếu việc** vào hòm thư của người làm (`hop-thu/<vai>.md`).
3. **Người làm** mở hòm thư của mình, làm việc, rồi trả kết quả kèm **file hoặc link thật**, đánh dấu phiếu là xong.
4. Việc chỉ Thuy Anh quyết được (tiền, đăng công khai, xóa, đổi luật, merge vào `main`) thì ghi vào [CAN-ANH.md](CAN-ANH.md). Không ai tự quyết thay.
5. Trước khi dừng: ghi **"Đang dở"** vào `goi/<gói>/tien-do.md` để phiên sau đọc là làm tiếp được.
6. Hỏng mất ≥ 20 phút thì ghi một dòng vào [BAI-HOC.md](BAI-HOC.md).
7. Bot Điều phối (`agents/general.py`) báo tuần lên Discord #general mỗi Thứ Hai.

## AI trên web đọc sổ thế nào

ChatGPT, Grok và Gemini không tự mở repo được như Claude Code hay Copilot. Thuy Anh làm "người đưa thư":

- Mở hòm thư của vai đó, ví dụ `hop-thu/grok.md`.
- Copy **phiếu việc** (mỗi phiếu đã viết sẵn đủ ngữ cảnh) và dán vào chat với AI đó. Lần đầu dán thêm [PHIEU-MO-DAU.md](PHIEU-MO-DAU.md).
- Dán câu trả lời của AI vào phần **Kết quả** của phiếu, hoặc nhờ Claude ghi giúp.

Claude Code và Copilot tự đọc luật ở `CLAUDE.md` và `.github/copilot-instructions.md` của repo.

## Các sổ

| Sổ | Để làm gì | Ai ghi |
|---|---|---|
| `../pipeline.md` | Việc ưu tiên, trạng thái `[ ] [>] [?] [x] [!]` | Thuy Anh, Claude |
| `hop-thu/<vai>.md` | Phiếu việc giao cho từng AI | Claude giao, người làm trả |
| `goi/<gói>/viec.md` | Danh sách mục của một mảng việc, mỗi mục có "đạt khi" | Claude |
| `goi/<gói>/tien-do.md` | Nhật ký tiến độ + mục "Đang dở" | Người làm |
| `CAN-ANH.md` | Câu hỏi chờ Thuy Anh quyết | Ai cũng hỏi được, Thuy Anh trả lời |
| `QUYET-DINH.md` | Quyết định đã chốt, ghi nguyên văn | Claude ghi lại lời Thuy Anh |
| `LUOT.md` | Ai đang giữ file chung nào (tránh hai AI sửa cùng một file) | Người sửa |
| `BAI-HOC.md` | Lỗi đã gặp và cách chặn | Ai gặp thì ghi |
| `VIEC-LAM-SAU.md` | Ý tưởng và việc hoãn | Ai cũng ghi |
| `TU-DIEN.md` | Từ chuyên môn giải thích bằng tiếng Việt thường | Ai dùng từ mới thì ghi |
| `spec/` | Mô tả việc lớn trước khi làm: mục tiêu, phạm vi, đạt khi, không làm | Claude |
