# Đề xuất phân công và lịch bàn giao — pilot SaLu (art & inspiration)

Leader: Claude · Lập 29/10/2026 · **Đề xuất, chờ chủ dự án duyệt.** Không bật đăng bài, không chi tiền, không ghi `main`.
Giữ nguyên năm vai trong `office/roster.json`; lịch dưới đây chi tiết hóa Ngày 1–7 của `CHANNEL_PLAN.md` §4.

## 1. Nguyên tắc bàn giao chung

- Mỗi AI làm trên **nhánh riêng** `office-<worker>-<task>` tách từ `office-scheduled-handoffs`, mở PR vào `office-scheduled-handoffs`. Chỉ báo xong khi có tệp/PR thật.
- Mỗi việc có biên nhận `office/submissions/<task_id>.json` (`completed` hoặc `blocked` + lý do).
- Giờ VN: **08:00** Claude giao việc · **10:00** nộp nghiên cứu/kịch bản · **13:00** nộp bản dựng + kiểm chéo · **17:00** Claude tổng hợp, báo cáo cho bạn.
- Nếu một AI không có lịch tự chạy được kiểm chứng, bạn (hoặc Claude nhắc) mở ứng dụng đó thủ công theo khung giờ trên; vẫn nộp qua GitHub.

## 2. Bước 0 — Onboarding cả nhóm (bắt buộc trước mọi việc)

Mỗi AI nộp `office/onboarding/<app>.md` cùng cấu trúc báo cáo của Claude: làm được gì, chưa làm được, công cụ, điểm cần kiểm chứng; kèm một lần thử đọc–ghi GitHub và một lần thử lịch.

| AI | Tệp | Việc thử bắt buộc | Hạn |
| --- | --- | --- | --- |
| Claude | `claude.md` | Push nhánh + lịch chạy 13:00 ghi receipt | 29/10 13:30 (**đã nộp, chờ receipt**) |
| Grok | `grok.md` | Grok Automation đọc `work-orders/radar.md`, commit một tệp thử | 30/10 10:00 |
| ChatGPT | `chatgpt.md` | Đọc work-order `art`, ghi tệp qua kết nối GitHub (nếu tài khoản có); ghi rõ chế độ dùng | 30/10 10:00 |
| Google AI Studio | `google-ai-studio.md` | Xuất được **một tệp media thật** (hình/âm thanh/clip ngắn) + ghi model/quota hiển thị; thử sync GitHub của Build mode | 30/10 13:00 |
| GitHub Copilot | `copilot.md` | Xác nhận có/không cloud agent trong gói hiện tại; nếu có, nhận một issue nhỏ và tạo PR; nếu chỉ có chat, ghi rõ | 30/10 13:00 |

Claude tổng hợp kết quả vào `office/onboarding/summary.md` lúc 30/10 17:00, đề xuất sửa `config.json` → `stage_workers` (video/review/publish) theo năng lực thật.

## 3. Lịch bàn giao Ngày 1–7

| Ngày | Giờ | Ai | Việc / task_id | Đầu ra | Ai kiểm chéo |
| --- | --- | --- | --- | --- | --- |
| T5 29/10 | 17:00 | Claude | Bài thử năng lực: 3 brief mẫu + 1 bài cài lỗi nguồn + 1 bài thiếu giấy phép | `office/benchmark/` (đề bài, thang điểm WORKFLOW §2) | Copilot kiểm schema |
| T6 30/10 | 10:00–13:00 | 4 AI | Onboarding (mục 2) | `office/onboarding/*.md` | Claude |
| T6 30/10 | 17:00 | Claude | Tổng hợp onboarding, đề xuất `stage_workers` | `summary.md` + PR sửa config (chờ bạn duyệt) | Copilot chạy test |
| T7 31/10 | 10:00 | Grok | `salu-first-1000-research`: 15 bài tham khảo (5/nền tảng), audience, đề tài | `artifacts/salu-first-1000-research/research.md` + `sources.json` | Claude mở lại nguồn quan trọng |
| T7 31/10 | 13:00 | Claude | Kiểm nguồn; trả "cần sửa" tối đa 2 vòng | review note trong PR | — |
| CN 1/11 | 17:00 | Claude | `salu-first-1000-plan`: định vị, nền tảng ưu tiên, KPI, 3 series, lịch 30 ngày | `artifacts/salu-first-1000-plan/plan.md` | Grok đối chiếu dữ kiện |
| T2 2/11 | 10:00 | ChatGPT | `salu-first-1000-script`: 3 kịch bản + storyboard + caption ×3 nền tảng, mỗi dữ kiện có claim id | `artifacts/salu-first-1000-script/` | Claude duyệt nội dung |
| T2 2/11 | 13:00 | Copilot | Validator cho script/asset ledger/hash; test | PR code + kết quả test | Claude đọc kết quả |
| T3 3/11 | 13:00 | Google AI Studio | `salu-first-1000-video` (nếu onboarding đạt): video/asset master + asset ledger | tệp media (lưu ngoài repo, chỉ commit link + hash) | ChatGPT đối chiếu SaLu; Claude duyệt quyền |
| T4 4/11 | 13:00 | Claude (+Grok, ChatGPT, Copilot) | `salu-first-1000-review`: nguồn, quyền, chính sách nền tảng, hash | `review.json` | Theo WORKFLOW §3 |
| T4 4/11 | 17:00 | Claude | Báo cáo một trang; trình quyết định đăng | báo cáo trong `office/reports/` | — |
| Sau duyệt | — | (chưa có runner) | `salu-first-1000-publish` | `published.json` + link | **Bị chặn tới khi có quyền tài khoản** |

Nếu bạn không làm cuối tuần, dời toàn bộ từ 31/10 sang T2 2/11 (+2 ngày).

## 4. Quyết định cần bạn (đã có phương án)

1. **Định nghĩa KPI** — đề xuất: tổng follow ba kênh = 1.000, báo riêng từng kênh (không phải 1.000 người duy nhất).
2. **Baseline và tài khoản** — bạn cho biết kênh SaLu đã có chưa và số follow hiện tại; nếu chưa có, ai tạo tài khoản (Claude không tạo được).
3. **Lịch lặp cho Claude** — đề xuất 2 lần/ngày 08:00 và 17:00 VN (sau khi receipt 13:00 đạt). Khung 10:00/13:00 do worker nộp, Claude đọc ở 17:00.
4. **Lưu trữ video** — repo không chứa video lớn; chọn nơi lưu (Drive/YouTube unlisted…) trước 3/11.

## 5. Rủi ro đã biết

- Production (Google AI Studio) chưa xác nhận xuất video → nếu không đạt onboarding, pilot chuyển sang hình tĩnh/carousel hoặc giảm scope, không ghi "đang render".
- Publish không có runner → đến 4/11 chỉ tới bước review.
- `office_handoffs.yml` chỉ chạy trên `main`; trước khi gộp, controller cần chạy tay để cập nhật board.
