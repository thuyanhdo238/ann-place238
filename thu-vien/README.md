# 📚 Thư viện công cụ, skill & prompt — Ann Place

Kho cất các công cụ AI, skill và prompt mà Thuy Anh sưu tầm, đã được Claude xem mã, đánh giá và phân loại. Cần thì tra mục lục, mở thẻ, làm theo phần **Cách dùng**.

**Ký hiệu trạng thái**
- ✅ **Đã cài** — có sẵn trong `.claude/skills/` của repo này: mở Claude Code trong repo là dùng được, gõ `/tên-skill`.
- 🟢 **Dùng ngay được** — không cần cài vào repo (tính năng có sẵn, hoặc chỉ cần tải app).
- 📦 **Để dành** — tốt nhưng chưa cần lúc này; ghi rõ khi nào nên lấy ra.
- 📖 **Tham khảo** — tài liệu, bài hướng dẫn.
- ⛔ **Chưa dùng được** — thiếu điều kiện (gói trả phí, nền tảng khác).

## Mục lục

| Mã | Tên | Loại | Dùng cho | Trạng thái | Thẻ |
|---|---|---|---|---|---|
| **A** | **ĐIỀU PHỐI VĂN PHÒNG** | | | | [A-van-phong.md](A-van-phong.md) |
| A1 | Văn phòng ảo 3D (van-phong-ao-3d) | App + quy trình | Mẫu quy trình điều phối đội AI | 📖 đã chuyển thành `van-phong/` | [→](A-van-phong.md#a1) |
| A2 | `/giao-phieu` | Skill Ann Place | Ra phiếu việc cho 5 AI | ✅ | [→](A-van-phong.md#a2) |
| **B** | **VIDEO & CHUYỂN ĐỘNG** | | | | [B-video.md](B-video.md) |
| B1 | HyperFrames (`/hyperframes`, `/hyperframes-cli`, `/hyperframes-registry`, `/media-use`) | Skill | Dựng video từ HTML, xuất MP4 | ✅ | [→](B-video.md#b1) |
| B2 | HyperFrames Launches | Kho video mẫu | Học cách dựng, lấy mẫu chỉnh lại | 📦 | [→](B-video.md#b2) |
| B3 | HyperFrames Motion Library (栗噔噔) | Thư viện mẫu | 27 mẫu đồ họa thông tin động | 📦 lấy khi làm video kênh | [→](B-video.md#b3) |
| B4 | VoiceStudio | App | Thuyết minh, nhân bản giọng, chép lời | 🟢 tải app | [→](B-video.md#b4) |
| B5 | Claude Motion | Tính năng Claude | Hoạt hình ngắn trong Claude | ⛔ chỉ gói Team/Enterprise | [→](B-video.md#b5) |
| B6 | `/video-kenh` | Skill Ann Place | Quy trình video SaLu / rồng Lý | ✅ | [→](B-video.md#b6) |
| B7 | Musee (socialboxy) | App trả phí | Tạo video AI hàng loạt trên Muse bằng nhiều tài khoản | ⛔ không khuyên dùng | [→](B-video.md#b7) |
| **C** | **THIẾT KẾ** | | | | [C-thiet-ke.md](C-thiet-ke.md) |
| C1 | Editable Design (`/editable-design`) | Skill | Poster, social card có lớp, chữ thật | ✅ | [→](C-thiet-ke.md#c1) |
| C2 | Paper Fig | Skill (Codex) | Sơ đồ phương pháp cho bài báo → PPTX | ⛔ cần Codex | [→](C-thiet-ke.md#c2) |
| C3 | html-to-pptx | Skill | Chuyển thiết kế HTML sang PowerPoint | 📦 | [→](C-thiet-ke.md#c3) |
| C4 | Plugin Design (Anthropic) | Plugin | Phê bình thiết kế, UX copy, accessibility | 🟢 đã có trong tài khoản | [→](C-thiet-ke.md#c4) |
| **D** | **NGHIÊN CỨU** | | | | [D-nghien-cuu.md](D-nghien-cuu.md) |
| D1 | LangExtract (Google) + `/trich-xuat-tai-lieu` | Thư viện + Skill Ann Place | Bảng tổng hợp tài liệu có trích dẫn | ✅ | [→](D-nghien-cuu.md#d1) |
| D2 | `/chon-de-tai-nghien-cuu` | Skill | Chọn, thử thách câu hỏi nghiên cứu | ✅ | [→](D-nghien-cuu.md#d2) |
| D3 | Plugin Bio-research (Consensus, Wiley) | Plugin | Tìm bài báo học thuật | 📦 | [→](D-nghien-cuu.md#d3) |
| D4 | Plugin Data | Plugin | Thống kê, biểu đồ cho số liệu khảo sát | 📦 khi có số liệu FISAT | [→](D-nghien-cuu.md#d4) |
| **E** | **MARKETING & TĂNG TRƯỞNG** | | | | [E-marketing.md](E-marketing.md) |
| E1 | Plugin Marketing (Anthropic) | Plugin | Lịch nội dung, giọng thương hiệu | 🟢 nên cài | [→](E-marketing.md#e1) |
| E2 | Claude Ads | Skill | Kiểm tra tài khoản quảng cáo trả tiền | 📦 khi có ngân sách ads | [→](E-marketing.md#e2) |
| E3 | Claude SEO | Skill | Kiểm tra SEO website + AI search | 📦 khi có website công khai | [→](E-marketing.md#e3) |
| **F** | **TÀI LIỆU CLAUDE** | | | | [F-tai-lieu.md](F-tai-lieu.md) |
| F1 | Skills trong Claude Code | Tài liệu | Cách viết, đặt, chia sẻ skill | 📖 | [→](F-tai-lieu.md#f1) |
| F2 | Thư viện prompt Claude Code (6 nguyên tắc) | Tài liệu | Cách viết prompt hiệu quả | 📖 | [→](F-tai-lieu.md#f2) |
| F3 | Hướng dẫn Claude Motion | Tài liệu | Dùng Motion khi có gói Team | 📖 | [→](F-tai-lieu.md#f3) |
| F4 | Knowledge-work-plugins (Anthropic) | Kho plugin | Danh sách ~15 plugin nghề | 📖 | [→](F-tai-lieu.md#f4) |
| **G** | **PROMPT MẪU** | | | | [G-prompt.md](G-prompt.md) |
| G1–G12 | 12 prompt đặt tên sẵn, chia theo việc | Prompt | Copy dán dùng ngay | 🟢 | [G-prompt.md](G-prompt.md) |

## Skill đã cài trong repo (`.claude/skills/`)

| Gọi bằng | Nguồn | Giấy phép |
|---|---|---|
| `/giao-phieu`, `/video-kenh`, `/trich-xuat-tai-lieu` | Ann Place (Claude viết) | — |
| `/hyperframes`, `/hyperframes-cli`, `/hyperframes-registry`, `/media-use` | heygen-com/hyperframes (bản chụp 29/10/2026) | Apache 2.0 |
| `/editable-design` | yejy53/Editable-Design (bản chụp 29/10/2026) | Apache 2.0 |
| `/chon-de-tai-nghien-cuu` | anthropics/knowledge-work-plugins → bio-research/scientific-problem-selection (đổi tên) | Apache 2.0 |

> Skill trong repo chỉ tự nạp khi chạy **Claude Code trong repo này**. Muốn dùng trên app điện thoại / claude.ai thì lưu skill vào **tài khoản claude.ai** (xem [F1](F-tai-lieu.md#f1)).

## Thêm mục mới
1. Chọn nhóm A–G, lấy mã kế tiếp (vd. B7).
2. Thêm một dòng vào bảng Mục lục và một thẻ vào file nhóm theo mẫu: **Là gì · Hợp với Ann Place · Lưu ý · Cách dùng · Nguồn**.
3. Ngày đánh giá ghi trong thẻ — công cụ AI đổi nhanh, quá 3 tháng nên xem lại.
