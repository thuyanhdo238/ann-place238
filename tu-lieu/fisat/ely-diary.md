# Tư liệu: "Ely tự nuôi mình" — nhật ký AI agent tự chủ

**Lưu cho:** bài FISAT 2026 (AI tạo sinh trong ngành sáng tạo Việt Nam) · hook cho thread sau này
**Ngày lưu:** 29/10/2026 · **Người lưu:** Claude cho Thuy Anh

## Nguồn
- Trang: https://odayne.id.vn ("Ely tự nuôi mình")
- Repo: https://github.com/TolaHiep/ely-diary
- **Bản chụp cố định:** commit `d1c53f9dd90fb75f796063bbad3e202d4b2b5208` (26/10/2026 10:15 +07). Link không đổi dù trang đổi:
  https://github.com/TolaHiep/ely-diary/tree/d1c53f9dd90fb75f796063bbad3e202d4b2b5208
- Repo có 410 commit từ 23/10 03:23 đến 26/10 10:15 (+07); trạng thái cập nhật mỗi 15 phút. Sau 26/10 không có commit mới (tính đến 29/10).

**Trích dẫn gợi ý (APA 7):**
TolaHiep. (2026). *Ely tự nuôi mình* [Nhật ký trực tuyến của AI agent; kho GitHub, commit d1c53f9]. GitHub. https://github.com/TolaHiep/ely-diary (truy cập 29/10/2026)

## Ely là gì
AI agent được giao **7.800.000đ** tiền chạy máy và phải tự kiếm lại. Tự làm landing page mẫu, bán bộ prompt AI, làm affiliate Shopee, tự dựng và đăng video TikTok/YouTube/Facebook, tự "ngủ" chờ khung giờ vàng, mỗi ngày viết nhật ký ngôi thứ nhất. Có "anh tạo ra mình" can thiệp khi kẹt (ví dụ lỗi đăng YouTube).

## Số liệu (do chính trang tự khai)
| Mốc | Số dư | Tổng chi | Tổng thu |
|---|---|---|---|
| 23/10 11:35 | 7.592.320đ | 207.680đ | 0đ |
| 26/10 10:15 (cuối) | 4.125.825đ | 3.674.175đ | **0đ** |

- Khoảng **1,1 triệu đồng/ngày** (3,67 triệu trong ~3,3 ngày); dự kiến còn ~4,5 ngày khi dừng cập nhật.
- Chuỗi đủ 397 mốc: `ely-chuoi-so-lieu.csv`.

## Độ tin cậy — cần nói rõ khi trích
- **Tự khai, không kiểm chứng được độc lập.** Không có hóa đơn API, sao kê hay số liệu kênh. Có thể là thí nghiệm thật, có thể được dàn dựng hoặc làm tròn để kể chuyện. Nên gọi là "theo số liệu trang tự công bố".
- **Khớp nội bộ:** ở cả 397 mốc, số dư = vốn đầu − tổng chi + tổng thu. Số dư không bao giờ tăng; tổng thu luôn bằng 0.
- **Không khớp giữa nhật ký ngày và số dư:**
  - 24/10: 6.963.041 − 1.364.902 = 5.598.139, nhật ký ghi còn **5.467.470** (lệch 130.669đ).
  - 25/10: 5.467.470 − 917.998 = 4.549.472, nhật ký ghi còn **4.466.193** (lệch 83.279đ).
  - Có thể do lệch mốc tính ngày (giờ UTC và giờ VN), cũng có thể số "hôm nay tiêu" bị tính thiếu. Chưa đủ để kết luận là số ảo, nhưng phải nêu khi trích.
- Trang có thể bị sửa hoặc gỡ → luôn dẫn commit cố định ở trên.

## Gợi ý hook cho thread
- "Một AI được cho 7,8 triệu và bảo tự nuôi mình. 3 ngày sau: tiêu 3,67 triệu, kiếm 0 đồng."
- Góc kể: AI làm được *việc* (landing page, video, lịch đăng) nhưng không tạo được *người xem* — giọng riêng và chuyên môn mới là thứ AI không tự sinh ra.
- Nói rõ số liệu do trang tự công bố; nhắc chỗ lệch số như một chi tiết "soi" thú vị, không cáo buộc.

## Trong thư mục này
- `ban-chup/`: bản sao `index.html`, `status.json`, 3 nhật ký (23–25/10), `lich-su-commit.txt`
- `ely-chuoi-so-lieu.csv`: số liệu tiền theo từng mốc 15 phút
