---
name: video-kenh
description: Làm video ngắn dọc 9:16 cho kênh SaLu (Art Sympathy) hoặc kênh rồng thời Lý của Thuy Anh — kịch bản, thuyết minh, hình, dựng bằng HyperFrames, xuất MP4. Dùng khi được nhờ làm video/clip/TikTok/Reels cho kênh, hoặc /video-kenh.
---

# Video kênh — quy trình Ann Place

Một video = một gói nhỏ. Làm theo thứ tự, mỗi bước có sản phẩm thật.

## 0. Hỏi tối đa 3 điều nếu thiếu
Kênh nào (SaLu / rồng Lý) · chủ đề · tài liệu nguồn. Còn lại tự quyết: độ dài mặc định 15–30 giây, khổ 1080×1920.

## 1. Kịch bản (`kich-ban.md`)
- Câu mở 2 giây đầu phải giữ người xem (câu hỏi, so sánh, hình bất ngờ).
- Mỗi cảnh: thời lượng · lời thuyết minh · chữ trên hình (≤ 7 từ) · hình cần.
- **Kênh rồng Lý là kênh kiến thức:** mỗi khẳng định phải có nguồn (sách, bài báo, hiện vật, bảo tàng). Không có nguồn thì bỏ, không bịa. Ghi nguồn ở cảnh cuối hoặc chú thích bài đăng.
- Không dùng hình có bản quyền của người khác; hình hiện vật ghi rõ nguồn/bảo tàng.

## 2. Thuyết minh (tùy chọn)
- Ưu tiên giọng thật của Thuy Anh, hoặc giọng AI từ **VoiceStudio** chạy trên máy (chỉ nhân bản giọng của chính chị).
- Không có file giọng thì làm bản chỉ chữ + nhạc.

## 3. Hình
- Nhân vật SaLu / minh họa: lấy từ `assets/` hoặc phiếu cho Gemini (dùng skill `giao-phieu`).
- Card thông tin tĩnh: skill `editable-design`.

## 4. Dựng video
- Dùng skill `hyperframes` (đọc trước), khổ 1080×1920, chữ tiếng Việt dùng font có dấu chuẩn (Be Vietnam Pro, hoặc trong font kit: Space Grotesk, Fraunces, Unbounded, Roboto Condensed, Noto Sans).
- Chừa vùng an toàn: trên 250px, dưới 350px (giao diện TikTok che).
- Mẫu chuyển động gợi ý (thư viện `nutllwhy/hyperframes-motion-library`): `timeline-scan`, `source-citation-card`, `quote-card`, `myth-fact-swap`, `concept-spotlight`, `chapter-title`, `keyword-blast`. Phong cách "giấy biên tập" hợp kênh di sản.
- Chỉ dùng công cụ miễn phí chạy trên máy; **không** dùng dịch vụ trả phí (kể cả HeyGen) khi chưa có duyệt trong `van-phong/CAN-ANH.md`.

## 5. Tự kiểm rồi mới giao
- Xem lại từng cảnh: chữ có bị che, sai dấu, tràn khung không; tiếng và chữ có khớp không.
- Xuất MP4 + 1 ảnh bìa + **chú thích bài đăng** (≤ 150 chữ, 3–5 hashtag, nguồn, nhãn "có sử dụng AI" nếu có giọng/hình AI).
- Không tự đăng. Ghi tiến độ vào `van-phong/goi/<gói>/tien-do.md`.
