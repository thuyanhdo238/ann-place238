# SaLu — nghiên cứu phân phối và kế hoạch thử nghiệm 30 ngày

Phiên bản 1.0 · nghiên cứu ngày 29/10/2026 · **đề xuất, chưa bật chiến dịch/đăng bài**.

Ba nền tảng đề xuất để khảo sát đầu: TikTok, Instagram Reels, YouTube Shorts. Chưa tự coi các tài khoản đã tồn tại hoặc đã được cấp quyền đăng. Facebook/Threads là mở rộng sau, chưa tốn công vận hành riêng trong giai đoạn đầu.

## 1. Điều đã biết và điều cần thử

| Nền tảng | Điều có căn cứ chính thức | Áp dụng cho SaLu — giả thuyết thử | Không được suy diễn |
| --- | --- | --- | --- |
| TikTok | For You dùng tương tác (xem hết/bỏ qua, thích/chia sẻ/bình luận), thông tin nội dung và người dùng; thời gian xem thường có trọng số cao hơn các nhóm khác. Search còn xét độ khớp truy vấn. [T1] | Mở bằng chi tiết ký họa hoặc câu hỏi thị giác rõ; cho người xem thấy thay đổi của bức vẽ; mô tả chủ đề cụ thể thay vì nhồi hashtag | Không biết trọng số đầy đủ; không có bảo đảm giờ vàng/hashtag nào khiến video viral |
| Instagram | Meta công bố cá nhân hóa và phối hợp nhiều dự đoán, trong đó có chia sẻ; không có một tín hiệu duy nhất đủ quyết định. Best Practices trong professional dashboard có hướng dẫn và gợi ý theo tài khoản. [I1,I2] | Thử những khoảnh khắc muốn gửi cho bạn bè; cover/series dễ nhận ra; ghi share/save và reach người chưa follow nếu Insights cung cấp | Không biến mô tả chung Meta thành trọng số riêng Reels; các trang Reels chi tiết đang bị 429 nên chưa xác minh đầy đủ thông số hiện hành |
| YouTube Shorts | Cá nhân hóa và hiệu quả xem: chọn xem/bỏ qua, thời lượng xem trung bình, tỷ lệ xem trung bình, thích và khảo sát sau xem. Chủ đề, cạnh tranh, mùa vụ cũng ảnh hưởng. Không đòi nhịp đăng tối thiểu. [Y1] | Đưa lời hứa của câu chuyện lên sớm, payoff hình ảnh rõ, đặt tên gợi đúng nội dung; xây series để có lý do subscribe | Không lấy CTR thumbnail video dài làm chỉ số chính của Shorts feed; không dùng một ngưỡng retention cho mọi độ dài |

TikTok: đọc được trích xuất chính thức trong tìm kiếm; mở toàn trang bị chuyển hướng không truy cập được. Instagram ranking chi tiết bị 429; phần tài liệu chung Meta và Best Practices đã đọc. Reviewer cần mở lại các phần còn thiếu trước khi duyệt triển khai theo quy định kênh. Đây là giới hạn nghiên cứu, không được ghi thành "đã xác minh toàn bộ thuật toán".

Không biết thuật toán nội bộ đầy đủ. Tín hiệu công bố không phải công thức bảo đảm phân phối; không gán trọng số phần trăm khi nền tảng không công bố. Kế hoạch dưới đây là thiết kế thử nghiệm của Ann Place, không phải quy định của nền tảng.

## 2. KPI và giả định cần leader đề xuất rõ

- KPI gốc: 1.000 người theo dõi. Đề xuất thử: tổng số follow/subscriber của ba kênh đạt 1.000; báo riêng từng kênh. Đây **không phải 1.000 người duy nhất** vì có thể trùng người giữa nền tảng. Chưa coi định nghĩa này đã được chủ dự án chốt.
- Chưa biết baseline. Leader lấy số thực trước khi đăng, không mặc định 0. Số tăng cần đạt = max(0, 1.000 − tổng baseline), nếu chọn mục tiêu tổng.
- 30 ngày là chu kỳ thử và đánh giá, không cam kết ngày đạt 1.000. Không tăng ngân sách để bù KPI. Ngân sách khởi đầu 0 đồng; chi mới phải hỏi.
- Khán giả giả thuyết: người nói tiếng Việt thích hình ảnh, ký họa và câu chuyện đời thường; người học/làm sáng tạo là nhóm cần khảo sát, chưa coi đã xác nhận. SaLu là nhân vật AI gốc; chỉ art/inspiration.
- Ngôn ngữ đề xuất: lời kể Việt; phụ đề Việt rõ. Phụ đề Anh là biến thể thử khi quy trình đã ổn, không chèn quá nhiều chữ lên cùng một khung.

Kịch bản tính để kiểm tra tính khả thi, **không phải dự báo**: nếu cần thêm 1.000 follow và quy đổi đo được là 5 / 10 / 20 follow mỗi 1.000 lượt xem thì cần khoảng 200.000 / 100.000 / 50.000 lượt xem. Nếu baseline khác hoặc tỷ lệ thực khác phải tính lại. Không cộng lượt xem ba nền tảng rồi coi là cùng một loại reach; số đếm có thể khác định nghĩa và có lượt xem lặp.

## 3. Các series thử

| Series | Số ý tưởng gốc trong tháng | Ví dụ giả định, không phải trend đã xác nhận | Điều muốn đo |
| --- | --- | --- | --- |
| SaLu đi ký họa | 9 | Ánh nắng trên một chiếc cốc; góc phố sau mưa; bóng lá trên tường | Giữ người xem và tạo lý do theo dõi chuyến đi tiếp |
| Nhìn một chi tiết đẹp | 4 | Một đường cong làm bố cục thay đổi; cùng cảnh với hai bảng màu | Lưu/chia sẻ và chất lượng tương tác về nghệ thuật |
| SaLu hóa trang nghệ thuật | 2 | Costume nguyên bản lấy cảm hứng bảng màu; trường hợp tác phẩm cụ thể phải qua kiểm tra quyền | Nhận diện nhân vật và chuyển đổi follow |

Không bắt SaLu nhảy theo mọi trend. Research chấm đề tài theo mức hợp art/inspiration, chứng cứ nhu cầu, khả năng tạo hình, quyền dùng tư liệu và công sức. Đề tài nhiều view nhưng lệch nhân vật hoặc quyền chưa rõ bị loại.

## 4. Lộ trình và phân công

Ứng dụng phụ trách: Leader = Claude; Research = Grok; Creative = ChatGPT; Production ứng viên = Google AI Studio; Engineering/QA = GitHub Copilot. Kiểm duyệt nội dung/quyền cuối do Claude chịu trách nhiệm, có Grok/ChatGPT đối chiếu, Copilot kiểm kỹ thuật. Đây là phân vai dự kiến; chưa xác nhận runner production và xuất bản.

| Thời gian tương đối | Công việc | Owner | Đầu ra/điều kiện |
| --- | --- | --- | --- |
| Ngày 1–2 | Kiểm công cụ/tài khoản, baseline; bài thử năng lực 5 vai; kiểm chính sách | Leader + từng worker; reviewer chấm độc lập | Roster có bằng chứng, danh sách chặn và kết quả benchmark; chưa có quyền thì không tự mở kênh/đăng |
| Ngày 2–3 | Nghiên cứu 15 bài tham khảo gần đây, 5 mỗi nền tảng; ít nhất 3 nhóm kênh khác nhau mỗi nền tảng | Research | URL, ngày, độ dài, opening, payoff, chỉ số công khai và giới hạn mẫu; không giả có retention/follow của đối thủ |
| Ngày 3 | Chốt đề xuất định vị, nền tảng ưu tiên, KPI, 3 series và kế hoạch thử | Leader | plan.md; các giả định và quyết định cần chủ dự án được trình bằng phương án cụ thể |
| Ngày 4–7 | Làm 3 video gốc, mỗi video có biến thể phù hợp ba kênh | Creative → Production → Reviewer | Tối đa 9 lượt đăng khi đủ điều kiện. Một master không tự trở thành ba bài đã đăng |
| Tuần 2 | Làm 4 video gốc; thử 2 kiểu opening qua các đề tài mới tương đương | Creative + Production; Leader thiết kế thử | Cùng nhóm chủ đề/độ dài; không đổi mọi yếu tố cùng lúc |
| Tuần 3 | Làm 4 video gốc; ưu tiên series có dấu hiệu tốt; thử nhịp/độ dài | Leader quyết định theo số thực | Giữ biến thể tốt qua nhiều bài, không kết luận từ một bài viral |
| Tuần 4 | Làm 4 video gốc; củng cố series, tối ưu lời mời theo dõi và đường dẫn hồ sơ | Toàn nhóm | Tổng tối đa 15 video gốc / 45 bản xuất bản; giảm nhịp nếu chất lượng/quota không đáp ứng |
| Ngày 30 | Tổng hợp KPI, quyền sử dụng, nguồn, công sức và vấn đề | Leader, reviewer đối chiếu dữ liệu | Giữ / sửa / dừng từng series; đề xuất vòng 30 ngày sau |

Số video là ngân sách sản xuất đề xuất. Nếu công cụ hiện có không xuất được video hoặc không có lịch chạy thật, leader giảm scope/chuyển định dạng, không tự coi pipeline đã hoạt động. Livestream nằm sau pilot vì cần năng lực phát trực tiếp và kiểm soát tương tác riêng.

## 5. Biến thể theo nền tảng

- Một bộ hình/video master nguyên bản; caption, cover, phần mở và metadata tùy kênh. Xuất tệp sạch, không mang watermark giao diện nền tảng khác. Không lấy bài của người khác làm master.
- TikTok: lời kể/caption nêu chủ đề cụ thể để kiểm tra nhu cầu tìm kiếm; test opening bằng chi tiết tranh so với câu hỏi. Nhạc chỉ dùng trong đúng phạm vi quyền.
- Instagram: bố cục/cover nhất quán SaLu, thử câu chuyện có giá trị chia sẻ hoặc lưu; khảo sát Insights và Best Practices của chính tài khoản. Carousel là thử nghiệm phụ, không dùng số đo carousel để kết luận hiệu quả Reels.
- Shorts: title phản ánh đúng câu chuyện; quan sát chọn xem/bỏ qua, average view duration và average percentage viewed cùng subscribers. Không suy view nhiều đồng nghĩa chuyển đổi tốt.
- Nhạc trong thư viện một nền tảng không mặc định có quyền đem sang nền tảng khác. Reviewer ghi căn cứ riêng cho mỗi bản xuất.

Các mức 20–30 giây so với 35–50 giây và mở rõ ý trong khoảng 2 giây là **giả thuyết dựng thử**, không phải điều kiện thuật toán. Nội dung cần thời gian cảm nhận có thể dài hơn nếu dữ liệu cho thấy phù hợp. Không kéo hoặc cắt chỉ để theo một con số.

## 6. Nhịp vận hành trong ngày — đề xuất

- 08:00 VN: Leader đọc bàn giao, cập nhật ưu tiên và giao nhiệm vụ. Research nhận các điểm còn thiếu.
- 10:00: Thu nghiên cứu/kịch bản; ghi nguồn và lỗi, mở bước đủ đầu vào.
- 13:00: Thu bản dựng; reviewer kiểm nguồn/quyền và xem video.
- 17:00: Leader ghi báo cáo ngắn, phương án và lịch xuất bản; việc chưa đạt chuyển sửa/chờ, không ép đăng để đủ lịch.
- Giờ đăng là thí nghiệm riêng: bắt đầu đối chiếu hai cửa sổ 12:00–13:00 và 19:00–21:00 VN, phân bổ luân phiên theo ngày/chủ đề. Đây không phải giờ vàng đã được chứng minh. Sau khi có dữ liệu người xem của kênh mới điều chỉnh; không đổi giờ chỉ vì một bài thấp view.
- Reviewer/publisher ghi link ngay khi đăng thành công; nếu lỗi, kiểm tra bài có thực sự tồn tại trước khi retry. Thu metrics tại 24h, 72h và 7 ngày khi đã có dữ liệu; giờ leader thu khác giờ bài đăng nên không được so các bài khác tuổi.

## 7. Đo và quyết định

| Mục tiêu | Dữ liệu cần | Quy tắc sử dụng |
| --- | --- | --- |
| Có người chọn xem | Chỉ số native: chose-to-view/swipe của Shorts; các chỉ số tương ứng nếu TikTok/Instagram cung cấp | Thiếu chỉ số ghi null, không ghi 0; không trộn định nghĩa |
| Giữ người xem | Average watch time, completion/percentage viewed, retention nếu được cung cấp | So trong cùng nền tảng, độ dài và tuổi bài tương đương |
| Giá trị chia sẻ | Shares/saves trên reach hoặc views tùy nguồn | Ghi rõ mẫu số; không gọi cả hai là một tỷ lệ |
| Tăng người theo dõi | Follow/subs do bài mang lại nếu nền tảng cung cấp; tổng net follow tài khoản theo ngày | Nếu chỉ có tăng theo ngày, không gán toàn bộ cho một bài |
| Làm được đều | Thời gian thực hiện, số vòng sửa, số tệp đạt, quota nếu đo được | Đừng tối đa lượt đăng mà bỏ chất lượng/nguồn/quyền |

Nội bộ đề xuất: sau ít nhất 3 bài tương đương cho một hướng và 72h mỗi bài, xem trung vị thay vì chỉ bài tốt nhất. Nếu quá ít reach hoặc thiếu số đo, đánh dấu chưa đủ dữ liệu, không xóa bài vội. Ưu tiên hướng tăng chuyển đổi follow đồng thời giữ chất lượng xem; share cao mà follow thấp có thể cần cải thiện lời hứa series/hồ sơ. Đây là chẩn đoán giả thuyết, không kết luận nhân quả.

Không dùng follow mua, tương tác giả hoặc spam để đủ KPI. Không tự đăng lại cùng nội dung hàng loạt để thử opening. Mỗi vòng thử dùng ý tưởng gốc mới, ghi rõ thay đổi và giới hạn so sánh.

## 8. Bản ghi thí nghiệm

Mỗi video có content_id, series, hypothesis, platform, variant, duration, opening, CTA, worker/model/prompt version, nguồn, assets, review/hash, published_url và mốc metrics. Leader đọc cùng mẫu này để quyết định; mỗi báo cáo phải trả lời: biết gì, chưa biết gì, thay gì, ai làm, hạn nào, cần bạn quyết định gì.

## 9. Nguồn và phạm vi đọc

- [T1] TikTok Help, How TikTok recommends content: https://support.tiktok.com/en/using-tiktok/exploring-videos/how-tiktok-recommends-content — trích xuất chính thức trong tìm kiếm, mở toàn trang chưa thành công. Không coi toàn bộ chính sách đã đọc.
- [I1] Meta, How AI Influences What You See on Facebook and Instagram (2023): https://about.fb.com/news/2023/06/how-ai-ranks-content-on-facebook-and-instagram/ — đã đọc, mô tả chung hệ thống, không phải bảng trọng số Reels hiện hành.
- [I2] Meta, Best Practices education hub (2024): https://about.fb.com/news/2024/10/best-practices-education-hub-creators-instagram/ — nguồn chính thức có mô tả gợi ý theo tài khoản.
- [I3] Instagram Ranking Explained: https://about.instagram.com/blog/announcements/instagram-ranking-explained — 429, chưa đọc được trực tiếp, không dùng làm chứng cứ cho trọng số hiện tại.
- [Y1] YouTube Help, Search & discovery tips — Shorts: https://support.google.com/youtube/answer/11914225?co=YOUTUBE._YTVideoType%3Dshorts&hl=en — đã đọc.
- [Y2] YouTube Shorts analytics: https://support.google.com/youtube/answer/12942217?co=YOUTUBE._YTVideoType%3Dshorts&hl=en — trích xuất theo tab Shorts; URL không có tham số có thể hiện tab Video dài, không lấy CTR của tab đó để áp cho Shorts feed.
- [Y3] YouTube, Prioritizing original content on Shorts: https://support.google.com/youtube/blog/470890423/prioritizing-original-content-on-shorts?hl=en-JE — tài liệu chính thức tìm thấy, nội dung gốc và khác biệt, không chỉ sửa template.

Người thực thi phải kiểm tra lại khi tài liệu/định nghĩa metrics thay đổi. Chưa nghiên cứu đối thủ, hashtag, âm thanh thịnh hành hoặc hành vi người xem của chính tài khoản; đó là nhiệm vụ Research, không phải dữ liệu có sẵn trong bản kế hoạch này.
