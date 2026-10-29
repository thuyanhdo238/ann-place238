---
name: giao-phieu
description: Giao việc cho một AI trong văn phòng Ann Place (Claude, Grok, Gemini, ChatGPT, Copilot) bằng phiếu việc đủ ngữ cảnh. Dùng khi Thuy Anh nói "giao cho…", "nhờ Grok/Gemini/ChatGPT/Copilot…", "ra phiếu", hoặc /giao-phieu.
---

# Giao phiếu việc — Ann Place

Biến một câu giao việc ngắn của Thuy Anh thành **phiếu việc** đúng chuẩn, ghi vào hòm thư của người nhận trong repo `thuyanhdo238/ann-place238`, thư mục `van-phong/`.

## Bước làm

1. **Xác định người nhận** theo vai (xem `van-phong/DOI-NGU.md`):
   - Grok = Radar (tin, cơ hội, deadline) · Gemini = Họa sĩ SaLu (hình, nhân vật) · ChatGPT = Thiết kế (CSS, DESIGN ZONE, nhánh `design`) · Copilot = Kỹ thuật (Actions, script, review PR) · Claude = Trưởng nhóm.
   - Việc không khớp vai nào thì hỏi lại một câu.
2. **Lấy số phiếu kế tiếp:** tìm số `P-<n>` lớn nhất trong mọi file `van-phong/hop-thu/*.md`, cộng 1.
3. **Viết phiếu** theo mẫu dưới. Ba nguyên tắc:
   - **Việc** = kết quả muốn có, không liệt kê từng bước. Một phiếu một việc, tối đa 10 dòng.
   - **Đạt khi** = kiểm được bằng mắt hoặc bằng số: file nào, link nào, bao nhiêu mục.
   - **Đủ ngữ cảnh để dán thẳng** cho AI trên web, vì nó không đọc được repo: nêu tài liệu tham khảo, giọng văn, khổ hình, người xem.
4. **Gắn với gói** nếu việc thuộc một mục trong `van-phong/goi/<gói>/viec.md`; ghi mã mục (vd. S1).
5. **Thêm phiếu vào cuối** `van-phong/hop-thu/<vai>.md`. Xóa dòng "_(Chưa có phiếu.)_" nếu có.
6. Nếu việc cần Thuy Anh quyết (tiền, đăng ra ngoài, nộp hồ sơ, xóa, merge `main`, đổi luật) thì **không ra phiếu**: thêm dòng `CHỜ` vào `van-phong/CAN-ANH.md`.
7. Commit trên nhánh riêng (không bao giờ `main`), rồi báo lại: số phiếu, người nhận, và **nguyên văn phiếu** để Thuy Anh copy dán cho AI trên web (kèm nhắc dán `van-phong/PHIEU-MO-DAU.md` nếu là chat mới).

## Mẫu phiếu

```markdown
---

### [ ] P-<n> · <dd/mm/yyyy> · từ Claude · gói `<gói hoặc —>`
**Việc:** <kết quả muốn có, 1–3 câu>
**Bối cảnh:** <người xem / mục đích / tài liệu tham khảo / phong cách>
**Đạt khi:** <kiểm được: file, link, số lượng>
**Luật:** không chi tiền, không đăng công khai, không sửa `main`.
**Kết quả:** 
```
