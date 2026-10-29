# A · Điều phối văn phòng

[← Mục lục](README.md)

## A1
### Văn phòng ảo 3D — `van-phong-ao-3d` · 📖 · đánh giá 29/10/2026
- **Là gì:** Web chạy trên máy, biến mỗi phiên Claude Code/Codex thành robot trong văn phòng 3D, kèm bộ sổ điều phối (hòm thư, "Cần anh", lượt DEV, nội quy, bài học, chấm điểm, chi phí token). MIT, không thư viện ngoài, chỉ đọc log trên máy.
- **Hợp với Ann Place:** Phần 3D chỉ thấy Claude Code/Codex trên máy, không thấy ChatGPT/Grok/Gemini web. **Phần đáng giá là quy trình** → đã chuyển thành thư mục [`van-phong/`](../van-phong/README.md) (Markdown, cả 5 AI dùng được).
- **Lưu ý:** Link Facebook dẫn tới bản sao `marketingjuliancongdanh79-pixel/…`; bản gốc là `vinaichatbot-rgb/van-phong-ao-3d`.
- **Cách dùng (nếu muốn cảnh 3D):** cài Node 18+ và Claude Code trên máy, mở Claude Code trong thư mục dự án, dán:
  > Cài văn phòng ảo cho dự án này theo hướng dẫn ở https://github.com/vinaichatbot-rgb/van-phong-ao-3d (đọc file HUONG-DAN-CHO-AGENT.md)
- **Nguồn:** https://github.com/vinaichatbot-rgb/van-phong-ao-3d

## A2
### `/giao-phieu` · ✅ skill Ann Place
- **Là gì:** Biến câu giao việc ngắn ("nhờ Gemini vẽ 3 hướng nhân vật SaLu") thành phiếu việc chuẩn trong `van-phong/hop-thu/<vai>.md`, đánh số tự động, có "Đạt khi", đủ ngữ cảnh để dán cho AI trên web.
- **Cách dùng:** Claude Code trong repo → `/giao-phieu giao Grok tìm 5 call for papers digital heritage hạn trước tháng 3/2027`.
- **File:** [`.claude/skills/giao-phieu/SKILL.md`](../.claude/skills/giao-phieu/SKILL.md)

## A3
### Ely tự nuôi mình — `TolaHiep/ely-diary` · 📖 · đánh giá 29/10/2026
- **Là gì:** Trang nhật ký công khai (odayne.id.vn) của một **AI agent tự chủ tên Ely**, được giao 7,8 triệu đồng tiền chạy máy và phải tự kiếm lại: tự làm landing page, bán bộ prompt, làm affiliate Shopee, tự dựng và đăng video TikTok/YouTube, tự "ngủ" chờ khung giờ vàng, mỗi ngày viết nhật ký. Repo chỉ có trang web và nhật ký, **không có mã của agent**.
- **Số liệu (26/10/2026):** đã tiêu ~3,67 triệu, **kiếm được 0đ**, còn đủ chạy ~4,5 ngày.
- **Bài học cho Ann Place:** đúng là lý do cho luật "không chi tiền" và "Thuy Anh duyệt trước khi đăng". Agent làm được nhiều việc, nhưng nội dung đại trà (affiliate, mẫu landing page) không tự sinh ra người xem hay doanh thu. Một kênh cần giọng riêng và chuyên môn thật, như SaLu và kênh rồng Lý.
- **Giá trị nghiên cứu:** tư liệu sơ cấp hiếm cho bài **FISAT** về AI tạo sinh trong ngành sáng tạo Việt Nam (agent tự làm nội dung, chi phí và hiệu quả thật, nhật ký tiếng Việt). Đã lưu ghi chú nguồn 29/10/2026: [`tu-lieu/fisat/ely-diary.md`](../tu-lieu/fisat/ely-diary.md).
- **Nguồn:** https://github.com/TolaHiep/ely-diary · https://odayne.id.vn
