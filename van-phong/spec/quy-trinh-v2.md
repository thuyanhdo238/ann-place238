# SPEC · Quy trình v2 — pilot SaLu (một tuần)

**Trạng thái:** nháp, chờ Thuy Anh xem · **Ngày:** 29/10/2026

## Mục tiêu
Thử quy trình Claude làm leader → các AI nhận việc qua GitHub → nộp bài → kiểm tra chéo → Claude tổng hợp → dashboard báo. Chỉ thử với kênh SaLu, không chi tiền.

## Quyết định đã chốt (Thuy Anh)
- Chỉ dùng công cụ **miễn phí**. Việc trả phí API để sau **24/12/2026**, xem lại lúc đó.
- Pilot với SaLu, được duyệt.
- Concept A "Sổ ký họa của SaLu" chạy cả 4 tuần. Concept B "Hoa văn một phút" **để sau 24/12**.

## Phạm vi pilot
- **Concept A** chạy 4 tuần, mỗi tuần 3 bài.
- Việc giao: hình nhân vật (Gemini), kịch bản và chú thích (Claude), tin và ý tưởng từ Radar (Grok, qua mục "Cho SaLu"), kiểm tra chéo.
- Grok và ChatGPT không có API miễn phí phù hợp → **Thuy Anh dán tay** phiếu vào chat và dán kết quả về, theo `PHIEU-MO-DAU.md`.

## Đạt khi (kết thúc một tuần pilot)
- Có ít nhất 3 bài nộp, mỗi bài có người duyệt chéo.
- Dashboard hiện trạng thái từng việc (giao / nộp / duyệt / xong).
- Số người theo dõi được ghi mỗi Thứ Hai trong `goi/salu-1000/tien-do.md`.

## Không làm
- Không mua API, không đăng bài tự động, không thay đổi `main` trực tiếp.
- Chưa làm dashboard đầy đủ: bản đầu là một trang tĩnh đọc `status.json`.

## Concept (chỉ A chạy trong pilot)
**A · Sổ ký họa của SaLu.** Mỗi tuần SaLu vẽ một thứ quanh mình (góc phố, một cây, một món đồ), kèm một dòng nhật ký. Dùng được ngay hình `salu-walking.webp` và sổ ký họa đã có.
*Hợp với:* nhận diện nhân vật, dễ ra bài đều. *Rủi ro:* dễ nhàm nếu thiếu ý.

**B · Hoa văn một phút.** Mỗi bài giải thích một họa tiết truyền thống Việt (sóng nước, rồng thời Lý, hoa sen) trong 30 giây, kèm nguồn.
*Hợp với:* nội dung có chiều sâu, nối với kênh rồng Lý và luận án. *Rủi ro:* phải kiểm nguồn kỹ, nên làm chậm hơn.

**C · Một góc làm việc.** Cảnh SaLu làm việc trong "văn phòng" Ann Place, lấy đúng câu slogan của trang: "Một góc làm việc. Nhiều điều đang lớn lên." Mỗi bài là một việc vừa làm xong của đội.
*Hợp với:* kể chuyện hậu trường, người xem thấy quá trình. *Rủi ro:* phụ thuộc có việc thật để kể.

Đã chốt: chỉ chạy A. B và C để sau 24/12.

## Lịch pilot
| Tuần | Concept | Bài | Ai làm |
|---|---|---|---|
| 1 | A | 3 | Gemini vẽ, Claude viết chú thích, Grok gợi ý ý tưởng |
| 2 | A | 3 | Như tuần 1, kiểm tra chéo đầy đủ |
| 3 | A | 3 | Như tuần 1 |
| 4 | A | 3 | Tổng kết, ghi số liệu |
