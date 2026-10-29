# G · Prompt mẫu

[← Mục lục](README.md)

Copy, thay phần trong `<…>`, dán vào Claude. Viết theo 6 nguyên tắc ở [F2](F-tai-lieu.md#f2). Prompt nào dùng nhiều → đóng thành skill.

## Mục lục prompt

| Mã | Tên | Nhóm | Dùng với |
|---|---|---|---|
| [G1](#g1) | Đánh giá một repo/công cụ AI mới | Chung | Claude |
| [G2](#g2) | Giao phiếu việc | Điều phối | Claude (`/giao-phieu`) |
| [G3](#g3) | Báo cáo tuần Ann Place | Điều phối | Claude |
| [G4](#g4) | Chép lại "Đang dở" trước khi dừng | Điều phối | Mọi AI |
| [G5](#g5) | Video dọc cho kênh rồng Lý | Video | Claude (`/video-kenh`) |
| [G6](#g6) | Lịch nội dung SaLu 1 tháng | Marketing | Claude |
| [G7](#g7) | Social card SaLu | Thiết kế | Claude (`/editable-design`) |
| [G8](#g8) | Radar cơ hội học thuật | Nghiên cứu | Grok |
| [G9](#g9) | Bảng tổng hợp tài liệu có trích dẫn | Nghiên cứu | Claude (`/trich-xuat-tai-lieu`) |
| [G10](#g10) | Thử thách câu hỏi nghiên cứu | Nghiên cứu | Claude (`/chon-de-tai-nghien-cuu`) |
| [G11](#g11) | Sơ đồ phương pháp chỉnh sửa được | Nghiên cứu | Claude |
| [G12](#g12) | Review PR trước khi merge | Kỹ thuật | Copilot / Claude |

---

## G1
**Đánh giá một repo/công cụ AI mới**
```text
Xem repo <link>: nó là gì, có an toàn không (đọc mã, tìm chỗ gửi dữ liệu ra ngoài, chỗ cần trả tiền), giấy phép gì.
Rồi đánh giá có hợp với Ann Place không (kênh SaLu, kênh rồng Lý, luận án PhD, bài FISAT, luật không chi tiền).
Trả lời ngắn cho màn hình điện thoại: là gì · hợp chỗ nào · lưu ý · nên dùng ngay hay để dành.
Nếu đáng giữ, thêm thẻ vào thu-vien/ đúng nhóm và cập nhật mục lục.
```

## G2
**Giao phiếu việc**
```text
/giao-phieu giao <Grok|Gemini|ChatGPT|Copilot> <việc>. Người xem/mục đích: <…>. Tham khảo: <file/link>. Đạt khi: <…>.
```

## G3
**Báo cáo tuần Ann Place**
```text
Đọc pipeline.md, van-phong/CAN-ANH.md, mọi hòm thư trong van-phong/hop-thu/ và mục "Đang dở" của các gói.
Viết báo cáo tuần ≤ 15 dòng, kết luận trước: xong gì (kèm link), đang nghẽn ở đâu, phiếu nào quá 7 ngày chưa đóng,
câu nào trong CAN-ANH đang chờ tôi quyết (liệt kê lựa chọn). Không bịa tiến độ không có trong file.
```

## G4
**Chép lại "Đang dở" trước khi dừng**
```text
Trước khi dừng, ghi đè mục "Đang dở" trong van-phong/goi/<gói>/tien-do.md: bạn là ai, đang làm gì, còn gì, bước kế tiếp, file liên quan.
Đủ để một phiên mới không có lịch sử chat đọc là làm tiếp được.
```

## G5
**Video dọc cho kênh rồng Lý**
```text
/video-kenh Làm video dọc 9:16, 15–30 giây, "<chủ đề>" cho TikTok, người xem là học sinh, sinh viên.
Dựa vào @<tài liệu>, mỗi khẳng định có nguồn. Phong cách giấy biên tập, giống assets/salu-kol.png.
Chữ tiếng Việt đọc rõ trên điện thoại. Xuất MP4, tự xem lại từng cảnh, sửa nếu chữ bị che hoặc sai dấu,
rồi gửi kèm chú thích bài đăng ≤ 150 chữ, 3–5 hashtag.
```

## G6
**Lịch nội dung SaLu 1 tháng**
```text
Lập lịch nội dung tháng <tháng> cho kênh SaLu (Art Sympathy — nghệ thuật và cảm hứng), mục tiêu 1.000 người theo dõi, không chạy quảng cáo.
Mỗi tuần ≥ 3 bài; mỗi bài: ngày, định dạng (video/ảnh/carousel), chủ đề, câu mở 2 giây, hình cần, ai làm (Gemini/Claude/ChatGPT).
Lấy ý từ agents/radar/output/output.md mục "Cho SaLu". Lưu thành van-phong/goi/salu-1000/ke-hoach-thang-<n>.md.
```

## G7
**Social card SaLu**
```text
/editable-design Social card 4:5 (1080×1350) cho SaLu, chủ đề "<…>". Người xem: người yêu nghệ thuật Việt, xem trên điện thoại.
Dùng hình <assets/…>, font có dấu tiếng Việt, nhiều khoảng thở. Xuất PNG + bản chỉnh sửa được. Không bịa số liệu, tên, ngày.
```

## G8
**Radar cơ hội học thuật** (dán cho Grok, kèm van-phong/PHIEU-MO-DAU.md)
```text
Tìm call for papers, hội thảo, triển lãm, học bổng về digital heritage, Southeast Asian art history, communication design, AI in creative industries,
còn hạn nộp từ <ngày> đến <ngày>. Mỗi mục: tên, đơn vị, hạn nộp, hình thức, link chính thức. Chỉ nguồn chính thức, không tin cũ hơn 30 ngày.
Xếp theo hạn gần nhất. Cuối cùng viết khối **Kết quả** 1–3 dòng.
```

## G9
**Bảng tổng hợp tài liệu có trích dẫn**
```text
/trich-xuat-tai-lieu Từ các file @<…>, lập bảng: hiện vật, niên đại, địa điểm, đặc điểm tạo hình (thân, vảy, chân, mào, râu, ngọc), so sánh với rồng <Tống/Trần>.
Mỗi dòng có trích nguyên văn và tên tài liệu. Chạy bằng <Ollama|Gemini>. Tự kiểm 10 dòng ngẫu nhiên, báo tỉ lệ đúng.
```

## G10
**Thử thách câu hỏi nghiên cứu**
```text
/chon-de-tai-nghien-cuu Đây là câu hỏi nghiên cứu và 2–3 hướng phương pháp tôi đang cân nhắc: <…>.
Hãy phản biện như người hướng dẫn khó tính: rủi ro, dữ liệu cần, khả năng hoàn thành trong 3 năm, đóng góp mới.
Kết thúc bằng bảng so sánh các hướng và 3 câu hỏi tôi cần trả lời trước 15/11.
```

## G11
**Sơ đồ phương pháp chỉnh sửa được**
```text
Từ đoạn mô tả phương pháp này: <…>, vẽ sơ đồ quy trình nghiên cứu một trang, phong cách học thuật tối giản, chữ tiếng <Anh|Việt>,
xuất PowerPoint chỉnh sửa được (mỗi khối, mũi tên chọn riêng được). Tự mở lại file kiểm chữ không tràn khung.
```

## G12
**Review PR trước khi merge**
```text
Review PR #<n> của ann-place238: có chạm main trực tiếp không, có lộ webhook/khóa không, ChatGPT có sửa ngoài DESIGN ZONE không,
workflow cron có bị đổi không. Kết luận trước: merge được / cần sửa (liệt kê). Không tự merge.
```
