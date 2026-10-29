# Nội quy Ann Place

Luật chung cho cả 5 AI. Mỗi chủ đề một luật. Sửa luật phải được Thuy Anh duyệt và ghi vào QUYET-DINH.md.

## 1. Ranh giới — luôn hỏi Thuy Anh trước
- Ghi vào `CAN-ANH.md` và **chờ** với các việc: chi tiền hay mua API (mặc định là **không**); đăng hay gửi gì ra ngoài lần đầu; nộp hồ sơ, gửi email thay Thuy Anh; xóa file hay dữ liệu thật; merge vào `main`; đổi luật trong file này.
- Việc khác trong phạm vi phiếu đã giao thì tự quyết rồi báo kết quả. Không hỏi lại "chị chọn a/b/c" cho việc nhỏ.
- **Không bao giờ ghi đè `main`.** Mỗi AI làm trên nhánh riêng; Thuy Anh review rồi merge.
- Không dán khóa, mật khẩu, link webhook vào chat, commit hay tin nhắn.

## 2. Xong là có bằng chứng
- Chỉ báo "xong" khi có **file thật trong repo hoặc link thật** mở được. Không có thì ghi "chưa kiểm chứng".
- Trạng thái 4 mức: bản nháp → tự kiểm → Claude duyệt → Thuy Anh duyệt/đăng.
- Nội dung có số liệu, trích dẫn, tên người hay sự kiện phải kèm nguồn.

## 3. Đội và quyền
- Thứ bậc: Thuy Anh → Claude (Trưởng nhóm) → các AI chuyên môn (xem `CAP-BAC.md`).
- **Mỗi mảng một gói, một chủ.** Gói do Claude viết. Người làm chỉ đánh dấu đạt, thêm bằng chứng và ghi chú.
- Mỗi lỗi sửa tối đa 3 lần. Lần 3 vẫn hỏng thì dừng, ghi đã thử gì và báo Claude.

## 4. Nhận và trả việc — hòm thư
- Việc tới qua phiếu trong `hop-thu/<vai>.md`, mỗi phiếu có mã `P-<số>`.
- Một phiếu một việc, một người nhận, tối đa 10 dòng, câu đầu là việc cần làm.
- Làm xong: đổi `[ ]` thành `[x]`, điền **Kết quả** (1 dòng + link/file). Phiếu trùng hay hết hiệu lực cũng đóng, ghi lý do.
- Cần người khác làm tiếp thì báo Claude để Claude ra phiếu mới. Không gửi tin chỉ để báo.
- Bị chặn thì ghi `[CHẶN]` ở đầu phần Kết quả, kèm cần ai gỡ.

## 5. File chung — mỗi lúc một người
- Trước khi sửa file chung (`index.html`, `office.html`, `pipeline.md`, workflow trong `.github/`), ghi tên vào `LUOT.md`. Xong thì xóa dòng đó.
- ChatGPT chỉ sửa trong DESIGN ZONE của `index.html` (xem `design/BRIEF.md`).

## 6. Tiết kiệm và ghi chép
- Đọc đúng phần cần đọc. Không dán log hay bài dài vào phiếu; để trong file rồi dẫn link.
- Trước khi dừng một phiên: ghi "Đang dở" vào `goi/<gói>/tien-do.md` (đang làm gì, còn gì, bước kế).
- Lỗi mới mất ≥ 20 phút: thêm một dòng vào `BAI-HOC.md`, kèm cách chặn lần sau.

## 7. Báo cáo cho Thuy Anh
- Kết luận trước, câu ngắn, tiếng Việt. Trả lời 4 ý: làm được gì (link); còn gì hỏng; ai lo tiếp; cần chị quyết gì.
- Từ chuyên môn mới thì giải thích một lần và ghi vào `TU-DIEN.md`.
