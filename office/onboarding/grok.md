# Báo cáo onboarding Grok (Research / radar) — Ann Place / SaLu

**Ứng dụng**: Grok (xAI)  
**Phân vai**: Research — xu hướng, khán giả, nội dung tham khảo, kiểm nguồn cho kênh SaLu (art & inspiration)  
**Worker id**: radar  
**Ngày kiểm tra**: 29/10/2026  
**Nhánh thực hiện**: `onboarding/grok-2026-10-29` (từ `office-scheduled-handoffs`)  
**Tuân thủ**: `office/standards/WORKFLOW.md`, `office/standards/CHANNEL_PLAN.md`, `office/roster.json`  

---

## 1. Đã đọc tài liệu chuẩn

- `office/standards/WORKFLOW.md` (raw trên nhánh `office-scheduled-handoffs`, kiểm tra 29/10/2026): Grok = Research; bắt buộc claims gắn nguồn + ngày đăng/ngày mở; `sources.json` tách **dữ kiện / diễn giải / đề xuất**; không tin trend chỉ vì có trên X; reviewer (Claude) đối chiếu nguồn quan trọng.
- `office/standards/CHANNEL_PLAN.md`: SaLu = art & inspiration; series thử “SaLu đi ký họa”, “Nhìn một chi tiết đẹp”, “SaLu hóa trang nghệ thuật”; nền tảng khảo sát TikTok / Instagram Reels / YouTube Shorts; KPI 1.000 follow là giả thuyết thử, không cam kết.
- `office/roster.json`: worker `radar` = Grok; status `proposed_not_benchmarked`; owns trend_research, source_ledger, audience_research.
- `office/README.md`: lịch bàn giao dự kiến 08:00 / 10:00 / 13:00 / 17:00 VN; mỗi worker phải thử 1 vòng nhận việc → ghi tệp → biên nhận trước khi đánh dấu sẵn sàng tự động.

---

## 2. Kiểm tra khả năng công cụ (bài đầu tiên)

| Khả năng | Kết quả | Chi tiết / bằng chứng | Trạng thái |
|----------|---------|-----------------------|------------|
| **Tìm web** | OK | `web_search`, `open_page`, `open_page_with_find` hoạt động. Đã mở raw.githubusercontent.com, API GitHub, Creative Bloq, Accio, Street Art View, Similarweb, MHomeVietnam (29/10/2026). | Pass |
| **Đọc GitHub** | OK | Repo public. Đọc được tree `office-scheduled-handoffs`, raw WORKFLOW/CHANNEL_PLAN/roster/README, API branches. | Pass |
| **Ghi / push GitHub + mở PR** | **Pass (sau khi được cấp token)** | Token PAT được cung cấp trong phiên. Clone thành công, tạo branch `onboarding/grok-2026-10-29`, ghi `office/onboarding/grok.md`, commit + push. | Pass |
| **Chạy theo lịch** | Chưa xác nhận | Grok không có recurring task native tương đương Claude Cowork. Cần platform/host (xAI hoặc GitHub Actions + webhook) gọi lại theo lịch. WORKFLOW yêu cầu thử 1 vòng bàn giao thật trước khi `external_schedule_confirmed`. | Pending |

**Ghi chú bảo mật**: Token chỉ dùng trong phiên này để hoàn thành onboarding. Không lưu token vào file repo, không commit credential.

---

## 3. Ba đề tài phù hợp SaLu (art & inspiration)

Phân biệt rõ theo WORKFLOW:
- **Dữ kiện** = thông tin có URL + ngày.
- **Suy luận** = liên hệ với series SaLu / khán giả giả thuyết.
- **Đề xuất** = ý tưởng thử, chưa phải kế hoạch sản xuất.

### Đề tài 1 — SaLu đi ký họa góc phố / ánh sáng đời thường
- **Dữ kiện**: Gen Z đang quay lại anatomy, gesture và plein-air painting; nhiều người 20 tuổi tham gia life-drawing và outdoor groups; một số document session trên TikTok (time-lapse + lo-fi). Nguồn: Creative Bloq, Tom May, 22/12/2025 — https://www.creativebloq.com/art/why-gen-z-artists-are-rediscovering-anatomy-gesture-and-plein-air-painting-in-2026 (mở 29/10/2026). Urban sketching digital (Procreate) vẫn phổ biến.
- **Suy luận**: Phù hợp series “SaLu đi ký họa” trong CHANNEL_PLAN; chi tiết ánh nắng / bóng / góc phố sau mưa dễ mở bằng visual hook ~2 giây.
- **Đề xuất**: 1 video master 25–40s: SaLu ngồi ký họa một chi tiết nhỏ (cốc, bóng lá, vỉa hè), payoff là bản vẽ hoàn chỉnh. Biến thể TikTok (opening chi tiết nét) / Shorts (title mô tả đúng cảnh). Quyền: chỉ dùng nét/hình SaLu gốc + public domain / asset tự vẽ.

### Đề tài 2 — Nhìn một chi tiết đẹp: “imperfect / hand-drawn / proof of hand”
- **Dữ kiện**: Xu hướng 2026 “Imperfect by Design”, “Naive Design”, “hand-drawn & imperfect elements”; nhiều nguồn trích Adobe data ~30% tăng tìm kiếm hand-drawn/imperfect; phản ứng chống “AI polish / AI slop”. Nguồn: Accio Graphic Design Trends 2026 (28/10/2026) https://www.accio.com/business/graphic-design-trends-for-2026; Studio 2am “Proof of Hand” (11/04/2026) https://studio2am.co/blogs/news/proof-of-hand-why-designers-are-reaching-for-imperfection-in-2026; Creative Bloq illustration trends 2026 (27/12/2025).
- **Suy luận**: SaLu là nhân vật AI gốc nhưng series “Nhìn một chi tiết đẹp” có thể nhấn mạnh nét tay, texture, đường cong “có lỗi” để tạo cảm giác ấm / authentic — đúng brief art/inspiration.
- **Đề xuất**: Video so sánh cùng một cảnh với hai bảng màu / hai kiểu nét (sạch vs hơi run); hỏi “bạn thích nét nào hơn?”. Đo save/share. Không dùng ảnh người thật chưa có quyền.

### Đề tài 3 — SaLu hóa trang / cảm hứng từ họa tiết organic & bio-philic
- **Dữ kiện**: Xu hướng họa tiết 2026 mạnh nhóm Bio-philic & Organic (thiên nhiên, leaf, organic curve); AI generative dùng để explore pattern nhưng designer làm curator. Nguồn: MHomeVietnam “Top 50+ Họa tiết đẹp trang trí xu hướng 2026” (27/10/2026) https://mhomevietnam.vn/vn/hoa-tiet-dep-trang-tri.html.
- **Suy luận**: Series “SaLu hóa trang nghệ thuật” trong CHANNEL_PLAN cho phép costume nguyên bản lấy cảm hứng bảng màu / họa tiết; tránh cosplay nhân vật có bản quyền.
- **Đề xuất**: SaLu mặc costume lấy cảm hứng họa tiết lá / đường cong organic (tự thiết kế), kể ngắn “mình thấy họa tiết này trên tường / vải”; visual payoff là chuyển động họa tiết. Kiểm quyền: chỉ asset gốc SaLu + pattern public-domain hoặc tự tạo.

---

## 4. Biên nhận nhiệm vụ onboarding

```json
{
  "task_id": "salu-onboarding-grok-2026-10-29",
  "worker": "radar",
  "application": "Grok",
  "status": "completed",
  "submitted_at": "2026-10-29T12:35:00+07:00",
  "artifacts": ["office/onboarding/grok.md"],
  "source_urls": [
    "https://raw.githubusercontent.com/thuyanhdo238/ann-place238/office-scheduled-handoffs/office/standards/WORKFLOW.md",
    "https://raw.githubusercontent.com/thuyanhdo238/ann-place238/office-scheduled-handoffs/office/standards/CHANNEL_PLAN.md",
    "https://www.creativebloq.com/art/why-gen-z-artists-are-rediscovering-anatomy-gesture-and-plein-air-painting-in-2026",
    "https://www.accio.com/business/graphic-design-trends-for-2026",
    "https://studio2am.co/blogs/news/proof-of-hand-why-designers-are-reaching-for-imperfection-in-2026",
    "https://mhomevietnam.vn/vn/hoa-tiet-dep-trang-tri.html"
  ],
  "notes": "Web search + GitHub read/write (sau token) pass. Lịch tự chạy chưa xác nhận. Ba đề tài đã gắn nguồn và phân biệt dữ kiện/suy luận/đề xuất."
}
```

---

## 5. Điểm còn mở cho Leader

1. Lịch tự chạy: cần xác nhận runner (GitHub Actions webhook / xAI schedule / tool khác) trước khi đánh dấu `external_schedule_confirmed`.
2. Ưu tiên đề tài nào trong 3 đề tài trên để Research đào sâu `sources.json` + tín hiệu khán giả (nếu có dữ liệu Insights sau này).
3. Token PAT đã dùng một lần cho onboarding; nên revoke hoặc scope hẹp sau khi PR merge nếu không còn cần.

Không sửa `main`. Không mua dịch vụ. Không coi tin trên X là đã xác minh.
