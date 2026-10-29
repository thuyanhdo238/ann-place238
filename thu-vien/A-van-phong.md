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
