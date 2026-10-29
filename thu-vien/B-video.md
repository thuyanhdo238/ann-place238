# B · Video & chuyển động

[← Mục lục](README.md)

**Quy trình gợi ý cho kênh:** Claude viết kịch bản → VoiceStudio đọc thuyết minh (B4) → Gemini / Editable Design làm hình (C1) → HyperFrames + Motion Library dựng (B1, B3) → xuất MP4. Gói gọn trong skill `/video-kenh` (B6).

## B1
### HyperFrames · ✅ đã cài 4 skill · đánh giá 29/10/2026
- **Là gì:** Framework của HeyGen: viết video bằng HTML/CSS (chữ, hình, video nền, nhạc, chuyển động, phụ đề) rồi xuất MP4, kết quả lặp lại y hệt mỗi lần. Làm riêng cho AI agent. Apache 2.0, chạy trên máy, cần **Node.js 22+** và Chrome/Chromium.
- **Hợp với Ann Place:** Video dọc cho SaLu và kênh rồng Lý, làm hàng loạt từ mẫu, giữ nhận diện; miễn phí → đúng luật không chi tiền. Art director điều khiển từng khung hình.
- **Lưu ý:** Không tự sinh hình/nhân vật như AI video — chỉ lắp ghép những gì đưa vào. Skill `media-use` có lựa chọn dịch vụ **HeyGen trả phí** → chỉ dùng công cụ miễn phí trên máy. Bản trong repo là bản chụp; cập nhật bằng `npx hyperframes skills update`.
- **Cách dùng:** Claude Code trong repo → `/hyperframes làm intro 10 giây dọc 9:16 "SaLu · Art Sympathy", chữ hiện dần, nền giấy`.
- **Cài cho máy khác:** `claude plugin marketplace add heygen-com/hyperframes` rồi `claude plugin install hyperframes@hyperframes`.
- **Nguồn:** https://github.com/heygen-com/hyperframes · Docs: https://hyperframes.heygen.com

## B2
### HyperFrames Launches · 📦
- **Là gì:** ~20 video quảng cáo thật của HeyGen (có video giới thiệu bài báo Claude, tích hợp Figma…), mỗi video là dự án mở được kèm `STORYBOARD.md` từng cảnh.
- **Hợp với Ann Place:** Học cách dựng nhịp, chuyển cảnh; lấy một dự án làm khung rồi thay nội dung. Tư liệu dạy môn motion cũng tốt.
- **Lưu ý:** Tài sản (video, nhạc, font) lưu bằng Git LFS — tải nặng. Lấy riêng một thư mục: `GIT_LFS_SKIP_SMUDGE=1 git clone …` rồi `git lfs pull --include="<thư-mục>/assets/*"`.
- **Nguồn:** https://github.com/heygen-com/hyperframes-launches

## B3
### HyperFrames Motion Library (栗噔噔) · 📦 lấy ra khi làm video kênh
- **Là gì:** 27 mẫu đồ họa thông tin động dựng trên HyperFrames, thay chữ/số/màu là ra video mới; 4 phong cách (đen–cam, **giấy biên tập**, ghi chú vẽ tay, hình học); bàn làm việc trên trình duyệt để xem trước và xuất hàng loạt. MIT.
- **Mẫu hợp kênh rồng Lý:** `timeline-scan` (dòng thời gian), `source-citation-card` & `quote-card` (trích nguồn, văn bia), `myth-fact-swap` (hiểu lầm vs sự thật), `concept-spotlight`, `chapter-title`, `keyword-blast`.
- **Lưu ý:** Mới 2 mẫu có khổ dọc 9:16 (`chapter-title`, `donut-progress`); font mặc định tiếng Trung → đổi font có dấu tiếng Việt; hướng dẫn viết tiếng Trung (Claude đọc được).
- **Cách dùng:** `git clone https://github.com/nutllwhy/hyperframes-motion-library` → nhờ Claude: "chuyển mẫu `timeline-scan` sang 9:16, tiếng Việt, phong cách giấy".
- **Nguồn:** https://github.com/nutllwhy/hyperframes-motion-library · Demo: https://nutllwhy.github.io/hyperframes-motion-library/

## B4
### VoiceStudio · 🟢 tải app
- **Là gì:** App giọng nói AI **chạy trên máy**: nhân bản giọng, thiết kế giọng bằng mô tả, lồng tiếng video, chép lời, đọc sách nói; 646 ngôn ngữ (có tiếng Việt). Mac (Apple Silicon), Windows, Linux, bản thử cho điện thoại; có MCP để Claude điều khiển. AGPL-3.0.
- **Hợp với Ann Place:** Thuyết minh video kênh bằng giọng của chính Thuy Anh; **chép lời phỏng vấn FISAT trên máy** (dữ liệu không lên mạng) → đưa sang LangExtract (D1); lồng tiếng Anh để vươn ra quốc tế.
- **Lưu ý:** Cần máy mạnh (chip M hoặc card NVIDIA). **Chỉ nhân bản giọng của mình** hoặc người đồng ý bằng văn bản; gắn nhãn nội dung AI trên TikTok. Nghe thử chất lượng tiếng Việt trước khi đăng.
- **Nguồn:** https://github.com/debpalash/VoiceStudio · https://voicestudio.sh

## B5
### Claude Motion · ⛔ chỉ gói Team / Enterprise (beta)
- **Là gì:** Tính năng của Claude tạo hoạt hình ngắn (giải thích, biểu đồ động, hướng dẫn) bằng code, sửa từng chi tiết, xuất MP4. Không dùng mô hình tạo video → không có cảnh quay/người thật.
- **Hợp với Ann Place:** Cùng nguyên lý với HyperFrames (B1) — dùng B1 thay thế. Nếu UIFA mua Claude Team/Enterprise cho giảng viên thì sẽ có, tiện cho dạy học.
- **Hướng dẫn:** xem [F3](F-tai-lieu.md#f3).

## B6
### `/video-kenh` · ✅ skill Ann Place
- **Là gì:** Quy trình 5 bước làm video dọc cho SaLu / kênh rồng Lý: kịch bản có nguồn → thuyết minh → hình → dựng HyperFrames → tự kiểm, xuất MP4 + ảnh bìa + chú thích bài đăng. Không tự đăng, không dùng dịch vụ trả phí.
- **Cách dùng:** `/video-kenh kênh rồng Lý, chủ đề "3 đặc điểm nhận diện rồng thời Lý", tài liệu @tai-lieu.pdf`
- **File:** [`.claude/skills/video-kenh/SKILL.md`](../.claude/skills/video-kenh/SKILL.md)

## B7
### Musee (musee.socialboxy.com) · ⛔ không khuyên dùng · đánh giá 29/10/2026
- **Là gì:** App Windows (giao diện tiếng Việt) chạy hàng loạt prompt tạo video trên dịch vụ **Muse AI**: dán danh sách prompt, chạy **nhiều tài khoản Muse song song**, mỗi tài khoản một proxy, tự chạy lại khi lỗi, gắn nhân vật bằng `@tên`. Không phải sản phẩm của Muse AI; trang không ghi tên nhà phát triển, chỉ có Zalo/Telegram.
- **Giá:** dùng thử 3 ngày, sau đó **99.000đ/tháng** (chuyển khoản QR) — chưa kể tiền tài khoản Muse.
- **Vì sao không dùng:**
  - Trái luật Ann Place: tốn tiền hằng tháng.
  - Chạy nhiều tài khoản + proxy riêng để lách giới hạn thường **vi phạm điều khoản** của dịch vụ AI → dễ bị khóa tài khoản.
  - Phải giao **cookie đăng nhập** các tài khoản cho một app không rõ chủ (dù nói mã hóa trên máy).
  - Video mẫu thiên về quảng cáo sản phẩm, KOL — không hợp kênh nghệ thuật, di sản.
- **Thay thế:** HyperFrames ([B1](#b1)) + `/video-kenh` ([B6](#b6)) — miễn phí, kiểm soát từng khung hình; cần cảnh AI thật thì dùng tài khoản chính chủ của công cụ AI video.
- **Nguồn:** https://musee.socialboxy.com
