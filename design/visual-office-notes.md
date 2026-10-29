# Bàn giao giao diện văn phòng — 29/10/2026

Theo yêu cầu trực tiếp của Thuy Anh: trang chính có văn phòng cao khoảng 2/3 màn hình điện thoại; phải thấy Van Gogh và SaLu cầm cọ đi; dữ liệu đóng/mở thay cho lưới thẻ. Đây là sửa giao diện, không kích hoạt bộ workflow trong PR #2.

- `assets/office-portrait.webp`: nền dọc 5 nhân vật đầy đủ, không có SaLu để tránh lặp.
- `assets/salu-walk-cycle.webp`: 4 ô sprite SaLu nền trong, CSS đổi khung và di chuyển ngắn trong lối đi.
- `dashboard.js`: home/office dùng cùng hoạt cảnh, canvas chuyển động nhỏ ở bàn tay; dữ liệu là native details/summary, lưu trạng thái đóng/mở tại trình duyệt.
- `dashboard.css`: khung mobile 66svh, đủ nền dọc, có pause/collapse và tôn trọng reduced motion đến khi bật rõ ràng.
- `index.html`: đổi phiên bản cache CSS/JS sang visual6.

Đã xem desktop và iframe 390x844, mở/đóng mục Công việc/Báo cáo, tải báo cáo thật; JavaScript syntax pass. Animation chỉ minh họa, không suy từ ảnh thành trạng thái AI đang chạy.

Các sổ van-phong/, pipeline/, thư viện và workflow mới trên main của Claude được giữ nguyên. Các link chuẩn cũ trong UI đang dẫn nhánh chuẩn bị; cần leader thống nhất nguồn chuẩn với van-phong/spec hiện hành trước khi nối dữ liệu thật. Không tự nhận PR #2 đã được merge hoặc bật lịch.
