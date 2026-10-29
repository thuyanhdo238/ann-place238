# Onboarding — Claude (worker `general`, Leader)

Ngày kiểm tra: 29/10/2026, 12:20–12:40 giờ VN · Phiên: Claude (Opus 5.5) trong ứng dụng Claude, môi trường cloud có shell + git.
Trạng thái tổng: **GitHub đọc/ghi: đạt** · **Chạy theo lịch: đạt (lần thử một lần 13:00 VN, 29/10)** · Chưa đánh dấu `external_schedule_confirmed`.

## 1. Đã làm được (có bằng chứng)

| Hạng mục | Kết quả | Bằng chứng |
| --- | --- | --- |
| Đọc repo | Clone `thuyanhdo238/ann-place238`, đọc nhánh `office-scheduled-handoffs` (commit `5a48472`) | Đã đọc `office/standards/WORKFLOW.md`, `CHANNEL_PLAN.md`, `office/roster.json`, `README.md`, `config.json`, `campaign.json`, `board.json`, work-orders |
| Quyền repo | API trả `push: true`, `admin: true` cho phiên này | `gh api repos/thuyanhdo238/ann-place238` |
| Ghi repo | Tạo nhánh riêng `office-onboarding-claude` từ `office-scheduled-handoffs`, commit và push tệp này | Chính commit/PR chứa tệp này |
| Mở PR | PR vào `office-scheduled-handoffs`, **không vào main** | Link PR (xem mô tả PR) |
| Chạy test | `python3 -m unittest discover -s tests` → 12 test, OK | Chạy tại phiên |
| Chạy theo lịch | Tác vụ một lần `trig_01Y73kHzovsEbyMGzvDjk1d8` chạy trong phiên mới lúc 13:00:22–13:00:28 VN, đọc `board.json` (7 task, khớp board) và tự push | Commit `a874862` · `office/onboarding/claude-schedule-receipt.json`, `status: completed`, `error: null` |

## 2. Chưa làm được / chưa chứng minh

- **Lịch mới thử một lần.** Lần chạy 13:00 đạt; chưa chứng minh lịch lặp ổn định nhiều ngày. Theo dõi 3 ngày đầu sau khi bật lịch lặp.
- **Không có mặt định kỳ 08:00/10:00/13:00/17:00 cho Claude.** Chưa tạo lịch lặp; chờ chủ dự án duyệt sau khi lần thử đạt. Lịch lặp tối thiểu theo giờ; có thể bị trễ vài phút.
- **Không thao tác tài khoản mạng xã hội.** Không có kết nối TikTok/Instagram/YouTube; không lấy được baseline follow; không đăng bài.
- **Không gọi ứng dụng AI khác.** Claude không mở được ChatGPT, Grok, Google AI Studio hay Copilot; chỉ giao việc qua work-order/GitHub.
- **Không dựng video.** Có thể tạo kịch bản, storyboard, tài liệu, hình tĩnh/HTML; không có công cụ tạo video AI trong phiên này.
- **`gh` GraphQL bị chặn** trong phiên; dùng REST API (đủ cho PR, file, nhánh).
- **Không thể tự duyệt** đầu ra do chính mình tạo (theo WORKFLOW §1).

## 3. Công cụ đang có trong phiên này

- Shell Linux + git + `gh` (REST) với quyền push repo này.
- Tìm kiếm web và đọc trang web (WebSearch/WebFetch) — đọc nguồn để kiểm chứng, một số trang có thể chặn.
- Tạo tác vụ theo lịch (một lần hoặc lặp) và nhắc lại trong chính phiên này.
- Tạo tài liệu/artifact (Docs, Slides, Sheets, trang HTML) để báo cáo.
- Kết nối đang gắn: Vercel, Wix, Claude Docs (chưa dùng; không dùng tới khi có việc cụ thể và được duyệt).
- Không có: API trả phí của bên thứ ba, connector mạng xã hội, Discord/email.

## 4. Điểm cần kiểm chứng

1. ~~Receipt 13:00~~ — **đạt**, commit `a874862`; `board_status` khớp `board.json`.
2. ~~Phiên theo lịch có quyền push~~ — **đạt** (phiên mới, không có người duyệt, vẫn push được).
3. Sau khi đạt: chủ dự án chấp thuận lịch lặp 08:00 / 17:00 VN cho Claude (đề xuất ở `handoff-plan.md`); khi đó mới đặt `external_schedule_confirmed: true` cho `general`.
4. Workflow `office_handoffs.yml` chỉ chạy trên `main` — nhánh thử nghiệm không kích hoạt controller. Bàn giao trên nhánh này cần chạy `python3 office/controller.py` thủ công để kiểm.
5. Các hạn trong `board.json` (plan 29/10 10:00) đã qua; cần cập nhật theo lịch mới khi được duyệt.

## 5. Ghi chú vận hành

Không mua API, không chi tiền, không ghi vào `main`, không gửi Discord/email. Mọi số liệu follow/metrics chưa đo được ghi `null`.
