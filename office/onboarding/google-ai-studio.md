# Báo Cáo Onboarding & Kiểm Toán Năng Lực: Google AI Studio

**Ứng dụng**: Google AI Studio (Môi trường AI Studio Build / Container Runtime)  
**Phân vai trong Ann Place**: Sản xuất hình ảnh & media cho SaLu (Worker ứng viên: `chance` / Hỗ trợ kỹ thuật Media)  
**Ngày kiểm toán**: 29/10/2026  
**Nhánh thực hiện**: `office-scheduled-handoffs`  
**Tuân thủ quy chuẩn**: `office/standards/WORKFLOW.md`, `office/standards/CHANNEL_PLAN.md`, `office/roster.json`  

---

## 1. Nhận Diện Nhân Vật SaLu (Visual Canon & Consistency)

Theo đúng tư liệu gốc đã được xác lập trong kho lưu trữ (`assets/salu-kol.png`, `assets/salu-walking.webp`):

- **Nhân dạng bất biến**:
  - Bé gái tuổi thiếu niên với vóc dáng nhỏ nhắn, nụ cười nhẹ nhàng, mộc mạc.
  - **Mái tóc**: Nâu hạt dẻ, uốn lượn sóng tự nhiên ngang vai.
  - **Phụ kiện đặc trưng**: Mũ nồi màu tím (signature purple beret) đội lệch; mắt kính tròn gọng đen/nâu mảnh tạo nét quan sát thông thái, tỉ mỉ.
  - **Trang phục**: Váy trắng suông viền đen tối giản, có biểu tượng trái tim đỏ ấm áp trước ngực; giày búp bê màu xanh rêu (sage green).
  - **Vật bất ly thân**: Bảng vẽ kỹ thuật số (digital sketchpad / drawing tablet) cầm trên tay khi đi dạo.
- **Định vị & Tinh thần nội dung (Brand Persona)**:
  - Dự án: *Art Sympathy · SaLu* (`office/campaign.json`).
  - Phạm vi: Nghệ thuật, ký họa đời thường và cảm hứng cuộc sống. SaLu lang thang góc phố, ngắm nhìn nhịp sống và ghi lại cảm xúc qua tranh vẽ.
  - **Giới hạn đạo đức & an toàn**: Tuyệt đối không đóng vai bác sĩ tâm lý, không đưa ra lời khuyên chẩn đoán hay cam kết chữa lành bệnh lý.
  - **Quy tắc nhất quán**: Mọi sản phẩm truyền thông hình ảnh/video phải kế thừa tư liệu này, không tự ý thay đổi màu tóc, bỏ mũ nồi tím hoặc đổi nhân vật khác.

---

## 2. Kiểm Toán Năng Lực Tài Khoản Hiện Tại (Account & Runtime Audit)

Thực hiện kiểm chứng thực nghiệm trên môi trường, không giả định bất kỳ quyền hạn nào chưa được cấp:

| Nhóm năng lực | Trạng thái thực tế | Chi tiết kiểm chứng & Giới hạn |
| :--- | :---: | :--- |
| **1. Tạo hình (Image Gen)** | **BỊ CHẶN (Generative AI)**<br>✅ **KHẢ DỤNG (Xử lý đồ họa)** | • Lệnh gọi `imagen-3.0-generate-002` qua `@google/genai` bị từ chối (`code: 404/403: Only supported by Vertex AI / Gemini Enterprise Platform`).<br>• Không có quota tạo ảnh Imagen miễn phí trên API key hiện tại.<br>• **Tuân thủ chỉ thị**: Báo rõ bị chặn, không mua gói trả phí, không bật thanh toán.<br>• **Khả năng xử lý đồ họa**: Môi trường có Python, Node.js, SVG/Canvas và FFmpeg để biên tập, cắt ghép, chuẩn hóa layout từ tư liệu gốc có sẵn (`assets/salu-kol.png`). |
| **2. Âm thanh (Audio / TTS)** | **BỊ CHẶN (Generative TTS)**<br>✅ **KHẢ DỤNG (Xử lý âm thanh)** | • Không có công cụ Text-to-Speech (TTS) AI tạo giọng nói tích hợp sẵn trong phiên làm việc.<br>• Các API sinh giọng nói thương mại yêu cầu thẻ thanh toán/API key riêng (chưa kích hoạt).<br>• **Khả năng kỹ thuật**: `/usr/bin/ffmpeg` có đầy đủ codec AAC/MP3, bộ lọc âm lượng, fade in/out, trích xuất và phối trộn nhiều luồng âm thanh nếu có tệp giọng đọc hoặc nhạc nền hợp lệ được cung cấp. |
| **3. Video (Video Gen & Assembly)** | **BỊ CHẶN (Text-to-Video)**<br>✅ **KHẢ DỤNG (Dựng video kỹ thuật)** | • Không có mô hình AI tạo video trực tiếp (Sora/Veo/Runway). Báo rõ bị chặn, tuyệt đối không báo ảo "đang render".<br>• **Khả năng dựng kỹ thuật (Technical Assembly)**: Đã kiểm chứng xuất video thực tế qua FFmpeg (`libx264`, `aac`), định dạng chuẩn 9:16 (720x1280 và 1080x1920), tốc độ 25/30fps, tạo chuyển động phóng to/thu nhỏ (Ken Burns pan & zoom) từ tranh ký họa của SaLu, chèn phụ đề và hiệu ứng đồ họa. |
| **4. Xuất tệp (File Export)** | ✅ **HOẠT ĐỘNG HOÀN TOÀN** | • Hệ thống tệp Linux hỗ trợ ghi đọc đa định dạng: `.mp4`, `.png`, `.svg`, `.json`, `.md`, `.csv`.<br>• Hỗ trợ tính toán mã băm SHA256 để phục vụ kiểm thử tính toàn vẹn theo chuẩn `tests/test_quality.py`. |
| **5. Ghi GitHub (GitHub Integration)** | ✅ **HOẠT ĐỘNG HOÀN TOÀN** | • Token GitHub API xác thực thành công với quyền `repo` và `workflow`.<br>• Đã kiểm chứng tạo nhánh, đọc/ghi tệp, nộp commit và pull request trực tiếp lên kho lưu trữ `thuyanhdo238/ann-place238`. |
| **6. Chạy theo lịch (Native Scheduling)** | ❌ **CHƯA CÓ LỊCH NATIVE ĐỘC LẬP** | • Phiên làm việc của Google AI Studio là môi trường tương tác (interactive container). Container sẽ ngủ hoặc giải phóng tài nguyên khi phiên đóng.<br>• Không thể tự động thức dậy lúc 08:00, 10:00, 13:00, 17:00 VN nếu không có tác nhân bên ngoài gọi tới.<br>• **Khuyến nghị vận hành**: Cần phối hợp với **GitHub Actions** (`.github/workflows/office_handoffs.yml` hoặc webhook) để trigger phiên làm việc đúng lịch bàn giao. |

---

## 3. Tệp Kiểm Chứng Thực Tế (Pilot Test Artifact)

Để Claude (Leader) và ChatGPT (Art / Creative) kiểm tra tính xác thực và chất lượng đầu ra, một bài thử nhỏ trong năng lực kỹ thuật đã được thực hiện và lưu trực tiếp vào kho lưu trữ:

- **Tệp video thực tế**: [`office/artifacts/salu-onboarding-sample/salu-motion-test.mp4`](../artifacts/salu-onboarding-sample/salu-motion-test.mp4)
- **Tệp thông số kiểm định**: [`office/artifacts/salu-onboarding-sample/sample-metadata.json`](../artifacts/salu-onboarding-sample/sample-metadata.json)

### Thông số kỹ thuật của bài thử:
1. **Nguồn hình ảnh**: Trích xuất từ `assets/salu-kol.png` (bảo toàn 100% nhân dạng SaLu).
2. **Định dạng video**: MP4 (H.264 High Profile, yuv420p).
3. **Độ phân giải & Khung hình**: 720 × 1280 (Tỷ lệ 9:16 dọc — chuẩn TikTok, Instagram Reels, YouTube Shorts).
4. **Tốc độ khung hình**: 25.0 fps.
5. **Thời lượng**: 5.0 giây.
6. **Âm thanh**: Luồng âm thanh tổng hợp tần số mẫu 44.1 kHz, AAC mono, có hiệu ứng fade-out âm lượng.
7. **Dung lượng tệp**: `133.370 bytes`.
8. **Mã băm SHA256**: `16ce07381da605937a4417445834fa842f7d7057ce2291e9c7bf999aba753f3b`.

---

## 4. Đề Xuất Quy Trình Phối Hợp (Handoff Workflow)

Dựa trên kết quả kiểm toán, Google AI Studio đề xuất vai trò tối ưu trong chuỗi sản xuất của Ann Place:

```
[Radar (Grok)] -> Tìm tư liệu / Trend
       ↓
[General (Claude)] -> Duyệt kế hoạch & Kịch bản khung
       ↓
[Art (ChatGPT)] -> Hoàn thiện kịch bản chi tiết, phân cảnh & lời thoại
       ↓
[Production (Google AI Studio)] -> NHẬN VIỆC DỰNG:
       • Nhận kịch bản và asset ký họa từ Art
       • Dựng motion video (9:16 Shorts/Reels) bằng FFmpeg
       • Chèn phụ đề, ghép âm thanh lồng tiếng được cấp
       • Xuất file .mp4 thật và nộp commit lên GitHub
       ↓
[QA & Review (Claude / Reviewer)] -> Kiểm duyệt bản quyền, hash SHA256 & duyệt đăng
```

- **Khi chưa có công cụ AI tạo giọng / tạo video tự động**: Khâu sản xuất tập trung vào dựng kỹ thuật (motion graphics, kinetic typography, pan & zoom tranh ký họa của SaLu) trên nền tư liệu gốc của repo.
- **Khi bị thiếu công cụ hoặc quota**: Luôn báo trạng thái `blocked` kèm nguyên nhân cụ thể trong biên nhận nhiệm vụ, tuyệt đối không báo giả là đang render.
