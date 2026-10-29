# Quy trình Ann Place 1.0

Trạng thái: bản chuẩn hóa để thử nghiệm, chưa kích hoạt workflow lên main. Áp dụng brief SaLu / Art Sympathy: art và inspiration; không tự chuyển sang tư vấn sức khỏe tinh thần. Mục tiêu tăng trưởng là giả thuyết cần thử và đo, không phải bảo đảm 1.000 follow.

## 1. Năm vị trí AI

| Vị trí | Mã worker trong repo | Trách nhiệm | Cách chọn AI/công cụ phù hợp | Đầu ra |
| --- | --- | --- | --- | --- |
| Leader | general | Chuyển brief thành mục tiêu đo được, kế hoạch, phân công, thu báo cáo và quyết định ưu tiên | Lập kế hoạch bám ràng buộc, đọc đủ hồ sơ, không tự báo xong khi thiếu bằng chứng | plan.md, phân công, báo cáo và đề xuất |
| Nghiên cứu | radar | Tìm xu hướng, khán giả, kênh tham khảo; xác minh dữ kiện và thời điểm | Thực sự truy cập/tìm được web, mở được nguồn gốc; độ chính xác hơn số lượng tin | research.md và sources.json |
| Sáng tạo | art | Concept, lời kể SaLu, storyboard, caption; giữ nhận diện và phạm vi | Chất lượng lời kể/hình ảnh, tính nhất quán SaLu, mức phù hợp brief | script.md, storyboard, shot list, caption |
| Sản xuất | chance | Dựng hình, motion, âm thanh, phụ đề, xuất đúng định dạng | Có công cụ thật để tạo/xuất video và tệp; không chọn chỉ vì viết prompt tốt | video.mp4, assets.json, thumbnail, phụ đề |
| Kiểm duyệt và xuất bản | opportunity | Độc lập kiểm tra nguồn, quyền sử dụng, chất lượng và quy định kênh; đăng đúng bản đã đạt; đo hiệu quả | Khả năng phát hiện sai/thiếu quyền, so sánh phiên bản, thao tác kênh được ủy quyền | review.json, published.json, metrics.json |

Đây là **vai đích**, chưa phải tuyên bố các script cũ đã có các năng lực ấy. Chance cũ chọn trích dẫn; Opportunity cũ đọc RSS. Chỉ xác nhận vai thực thi sau bài thử thực tế. Năm mã worker không chứng minh đã có năm ứng dụng AI đang chạy tự động.

Tên nhà cung cấp/model và phiên bản ghi trong bản đánh giá sau khi biết đúng các tài khoản/công cụ đang có. Không mặc định một thương hiệu mạnh nhất trong mọi nhiệm vụ. Một ứng dụng có thể đảm nhiệm hai vị trí bằng phiên/tác vụ riêng, nhưng reviewer phải khác worker sáng tạo và sản xuất; nếu dùng cùng model, mức độc lập hạn chế vẫn phải được ghi nhận.

## 2. Phân công dựa trên kết quả thử

Dùng cùng 3 bài mẫu art/inspiration cho các ứng viên, cùng đầu vào, cùng yêu cầu. Thử thêm một bài cài lỗi nguồn và một bài thiếu giấy phép. Đánh giá trước khi bật lịch; kiểm tra lại khi đổi model, công cụ hoặc phiên bản prompt.

| Vị trí | Trọng số đề xuất /100 |
| --- | --- |
| Leader | Đúng ràng buộc 30; kế hoạch làm được 30; bàn giao đúng 20; thời gian/tài nguyên 20 |
| Nghiên cứu | Dữ kiện đúng 35; nguồn gốc kiểm tra được 30; tính mới/phù hợp 25; thời gian 10 |
| Sáng tạo | Giữ SaLu 30; câu chuyện/hình ảnh 30; phù hợp brief 20; đúng dữ kiện/bàn giao 20 |
| Sản xuất | Video hoàn chỉnh dùng được 35; đúng storyboard 25; hình/âm thanh/phụ đề 25; thời gian 15 |
| Reviewer | Phát hiện lỗi cài sẵn 40; hồ sơ quyền đầy đủ 30; đúng phiên bản/kênh 20; thời gian 10 |

Ngưỡng nội bộ đề xuất: ít nhất 80/100, không có lỗi nghiêm trọng (bịa nguồn, giấy phép chưa rõ mà duyệt, sai SaLu, không xuất được tệp, đăng nhầm phiên bản). Không tự điền điểm khi chưa thử. Chi phí token chỉ ghi khi có số đo; không đổi giá quy đổi thành hóa đơn thật.

## 3. Cổng chất lượng và bàn giao

| Bước | Người chịu trách nhiệm | Điều kiện mở bước tiếp |
| --- | --- | --- |
| Nhận brief | Leader | KPI được định nghĩa; nền tảng/thời hạn còn thiếu được ghi thành giả định và việc leader phải nghiên cứu |
| Nghiên cứu | Research | Claims gắn nguồn, ngày đăng/ngày kiểm tra; không đánh dấu nguồn đã kiểm tra nếu chưa mở |
| Kế hoạch | Leader | Có lý do chọn nền tảng, nhóm khán giả, nhịp nội dung, giả thuyết, lịch, phân công và cách đo |
| Kịch bản | Creative | Mỗi dữ kiện có claim id; storyboard, asset list và caption cùng phiên bản |
| Sản xuất | Production | Video thật, phụ đề/âm lượng/tỷ lệ được xem thử; mọi asset có hồ sơ quyền |
| Kiểm duyệt | Reviewer | Đối chiếu nguồn độc lập; rights ledger đầy đủ; chính sách từng nền tảng được mở và ghi ngày; đúng hash của tệp |
| Đăng | Reviewer/publisher | Có kết nối thao tác kênh, quy tắc xuất bản được chấp thuận, bản kiểm duyệt đạt; lưu link và idempotency key |
| Đo/cải thiện | Reviewer thu số, Leader phân tích | Số thực đo 24h/72h/7 ngày theo điều kiện truy cập; leader quyết định thử nghiệm tiếp theo |

Trạng thái chuẩn: chờ đầu vào → sẵn sàng nhận việc → báo đang làm → có bàn giao → đang kiểm tra → đạt / cần sửa / bị chặn → đã đăng → đo kết quả. Bộ controller hiện chỉ xác thực sẵn sàng/chờ/bị chặn/bàn giao; không giả trạng thái đang làm khi thiếu biên nhận bắt đầu.

Thiếu đầu vào thì chờ, không bịa. Chạy lại không tạo bài trùng. Worker báo lỗi có mã nhiệm vụ, nguyên nhân, phần đã xong, hướng phục hồi. Tối đa 2 vòng sửa cho một lỗi; sau đó leader chọn phương án khác hoặc báo cần hỗ trợ. Chưa có kết nối công cụ thì ghi blocked, không ghi "đang render".

## 4. Kiểm tra nguồn

- `sources.json` tách **dữ kiện**, **diễn giải**, **đề xuất sáng tạo**. Lời kể hư cấu của SaLu phải rõ là hư cấu, không gán trải nghiệm thật cho người thật.
- Mỗi nguồn có URL trực tiếp, đơn vị xuất bản, tiêu đề, ngày đăng nếu biết, thời điểm mở, loại primary/secondary và vị trí bằng chứng trong trang. Không dùng snippet tìm kiếm thay cho đọc nguồn.
- Tin xu hướng có thời điểm và cửa sổ khảo sát. Một tin mới không tự chứng minh đang là trend; cần tín hiệu độc lập và ghi giới hạn mẫu. Deadline/sự kiện phải về trang ban tổ chức và kiểm tra thời hạn.
- Dữ kiện quan trọng ưu tiên nguồn gốc. Khi nguồn mâu thuẫn, ghi mâu thuẫn; chưa phân giải thì bỏ dữ kiện hoặc chặn đoạn phụ thuộc nó. Không coi hai trang chép cùng một thông cáo là hai xác nhận độc lập.
- Reviewer kiểm tra lại claim quan trọng và toàn bộ trích dẫn trực tiếp; lưu điểm bằng chứng ngắn, không lưu sao chép toàn bài. Code chỉ kiểm tra cấu trúc hồ sơ, **không xác nhận nội dung nguồn là đúng**.

## 5. Sàng lọc quyền và quy định xuất bản

Đây là quy trình sàng lọc vận hành, không phải ý kiến pháp lý cho mọi tình huống. Reviewer phải tra văn bản và điều khoản hiện hành tại ngày đăng, theo quốc gia/kênh/mục đích sử dụng. Không ghi "hợp pháp" chỉ từ một cờ true.

Mỗi hình, ảnh tham khảo đưa vào thành phẩm, nhạc, bản thu, font, footage, nhân vật và giọng có:
- Nguồn/chủ sở hữu, quyền dự kiến, căn cứ quyền dùng và bằng chứng (license/điều khoản/văn bản cho phép/nguồn xác nhận public domain).
- Phạm vi sửa đổi, thương mại, nền tảng, lãnh thổ, thời hạn và ghi công. Không suy từ một nền tảng sang tất cả nền tảng.
- Với asset AI: công cụ/model/ngày tạo, quyền với đầu vào và điều khoản đầu ra; không tự nhận độc quyền hoặc chắc chắn có bản quyền vì đã dùng AI.
- Tác phẩm hội họa gốc và ảnh chụp/bản scan/bản thu là các lớp cần kiểm tra riêng. Không suy "họa sĩ đã mất lâu" thành quyền dùng mọi tệp trên mạng.
- SaLu cosplay: nhận diện/thiết kế nhân vật cụ thể, nhãn hiệu và hình ảnh người thật cần được xem theo trường hợp. Chưa rõ thì chuyển sang costume nguyên bản hoặc asset đã có quyền; không tự mặc định parody/fair use.
- Không clone giọng hoặc dùng hình ảnh người thật chưa có căn cứ phù hợp. Không giả họ bảo trợ/đã nói câu do AI viết.
- Ghi quyết định công khai AI theo từng kênh. Không coi mọi animation dễ thương đều phải cùng một nhãn; đọc chính sách thực tế của nền tảng.

Màu rủi ro là quy tắc nội bộ: **xanh** có hồ sơ rõ và trong phạm vi; **vàng** thiếu/khó xác định — thay asset hoặc dừng để kiểm tra thêm; **đỏ** có dấu hiệu vi phạm/giả mạo — không xuất bản. Tình huống còn tranh chấp hoặc diễn giải pháp lý quan trọng cần người có chuyên môn; leader không tự vượt cổng để đạt KPI.

## 6. Lịch và vận hành không mua API giao tiếp

Lịch dự kiến: 08:00 leader giao/thu; 10:00 kiểm đầu ra; 13:00 cập nhật việc và vấn đề; 17:00 báo cáo cho chủ dự án. Mỗi ứng dụng worker cần lịch riêng đọc work-order và ghi bàn giao GitHub. GitHub không tự mở mọi ứng dụng và không bảo đảm đúng phút.

Mỗi lần chạy cần task id, worker id, model/tool/version nếu có, thời gian bắt đầu/kết thúc, đầu vào, đầu ra, lỗi, token/tài nguyên **thực đo nếu công cụ cung cấp**. Thiếu số thì ghi chưa đo. Dùng task+platform+content hash làm khóa chống đăng trùng; kiểm tra kênh trước khi retry upload.

Không gửi báo cáo Discord/email nếu chưa được yêu cầu riêng. Không mua dịch vụ hoặc tăng chi phí. Dashboard công khai không lưu token, lịch sử tài khoản hay hợp đồng/giấy phép riêng tư; hồ sơ riêng chỉ lưu bằng chứng tham chiếu an toàn.

## 7. Báo cáo cho bạn

Một trang: tiến độ KPI (theo định nghĩa đã thống nhất), tệp/link thành phẩm, việc chậm/chặn, bằng chứng nguồn và rights status, đề xuất kèm phương án và ảnh hưởng. Không giới thiệu chân dung nhân vật thay cho báo cáo công việc.

Thông tin chiến lược còn thiếu là việc leader chuẩn bị đề xuất, không phải một bảng câu hỏi bắt bạn tự làm kế hoạch. Chỉ hỏi quyết định khi đã có phương án cụ thể hoặc cần quyền/ngân sách bạn chưa giao.

## 8. Nguồn tham chiếu chính thức, kiểm tra 29/10/2026

- Cổng văn bản Chính phủ: Luật 131/2025/QH15 sửa đổi Luật SHTT, hiệu lực 01/04/2026: https://vanban.chinhphu.vn/default.aspx?docid=216511&pageid=27160
- Công báo: danh mục VBHN 160/2026/VBHN-LQ-VPQH ngày 29/09/2026: https://congbao.chinhphu.vn/van-ban-dang-cong-bao/van-phong-quoc-hoi-c47/trang-2.htm
- Nghị định 134/2026/NĐ-CP sửa NĐ 17/2023 về quyền tác giả/quyền liên quan, hiệu lực 09/04/2026: https://vanban.chinhphu.vn/?classid=1&docid=217833&orggroupid=2&pageid=27160
- Quyền đối với hình ảnh, Điều 32 BLDS, nguồn Quốc hội: https://vietlaw.quochoi.vn/Pages/vbpq-print.aspx?ItemID=27892
- YouTube AI disclosure: https://support.google.com/youtube/answer/14328491?hl=en
- YouTube Audio Library và yêu cầu ghi công: https://support.google.com/youtube/answer/3376882?hl=en
- TikTok AIGC: https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content (kết quả tìm kiếm chính thức có nội dung; lần mở đầy đủ bị robots chặn, reviewer phải đọc lại trước khi dùng làm căn cứ đăng).
- Meta AI info: https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/ (mô tả cách gắn nhãn, không thay toàn bộ điều khoản quyền sử dụng/đăng bài).

Danh sách này là điểm bắt đầu tra cứu; metadata văn bản không thay việc đọc điều khoản áp dụng. Không dùng riêng luật sửa đổi 2022 như thể đã bao gồm toàn bộ thay đổi đến 2026. Cập nhật hồ sơ chính sách khi đổi nền tảng hoặc có thay đổi; đọc lại tại lần duyệt trước khi đăng.
