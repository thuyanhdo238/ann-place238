# Onboarding — ChatGPT (worker `art`, Nội dung/Sáng tạo SaLu)

- Việc: **P-4**, gói `salu-1000`, do Claude giao ngày 29/10/2026.
- Ngày thực hiện: **29/10/2026, giờ Việt Nam (UTC+07:00)**.
- Hạn bàn giao: **30/10/2026, 10:00 giờ Việt Nam**.
- Chế độ quan sát được: **ChatGPT Work Mode / tác nhân Codex**, có môi trường shell Linux và công cụ GitHub trong cuộc trò chuyện này. Không suy khả năng của phiên tương tác thành khả năng của tác vụ theo lịch.
- Gói thuê bao: **chưa xác minh trực tiếp**. Phiên không cung cấp quyền đọc trang thanh toán hoặc tên gói đã được kiểm chứng; không tự ghi Plus/Pro hay khẳng định hạn mức. Mã model/version cụ thể chưa có bằng chứng kiểm tra trong phiên.
- Trạng thái nộp: **báo cáo và bài thử được bàn giao qua nhánh riêng/PR; chờ Claude kiểm tra**. Không tự đánh giá đạt chất lượng sáng tạo, nguồn hoặc pháp lý.
- Phạm vi: một tệp `office/onboarding/chatgpt.md`; không sửa `main`, workflow, cấu hình, board hoặc nhiệm vụ của người khác; không đặt lịch, không đăng lên mạng xã hội, không chi tiền.

## 1. Làm được gì — bằng chứng trong phiên

| Hạng mục | Kết quả quan sát được | Bằng chứng / giới hạn |
| --- | --- | --- |
| Đọc GitHub | Đọc được repo `thuyanhdo238/ann-place238` qua kết nối GitHub | Đã đọc mẫu Claude, workflow, roster, README, handoff-plan, work-order `art` và hồ sơ nhân vật tại snapshot `58d9fc7512a2598e51732e75f118901a43261e45` |
| Ghi GitHub | Ghi tệp trên nhánh riêng và mở PR là phương thức bàn giao của bài P-4 | Nhánh và PR chứa chính tệp này là bằng chứng ghi thực tế; không dùng quyền đọc hoặc lời báo trong chat thay cho bằng chứng ghi |
| Nội dung/Sáng tạo | Viết được kịch bản ngắn, storyboard bằng mô tả cảnh, caption riêng cho ba nền tảng | Bài thử ở Phụ lục A; đây là văn bản sản xuất, chưa phải hình storyboard đã render hoặc video |
| Giữ hồ sơ SaLu | Dùng cách xưng hô và đặc điểm đã ghi trong repo | Nguồn nội bộ I-02 bên dưới; hồ sơ đang ở trạng thái bản nháp chờ Thuy Anh duyệt |
| Phân biệt dữ kiện và hư cấu | Bài thử không đưa lời trích dẫn, tên họa sĩ, mốc lịch sử, lời khuyên sức khỏe hoặc tuyên bố thuật toán | Toàn bộ chuyến đi, lời thoại và bối cảnh là hư cấu; bảng truy xuất ở Phụ lục A.5 |
| Bàn giao cho sản xuất | Ghi thời gian, hình ảnh, lời thoại, chuyển động và âm thanh từng cảnh | Nhà sản xuất cần dựng/đọc thử; thời lượng chỉ là dự kiến |

Work-order `salu-first-1000-script` trong snapshot đang là `waiting`, chờ kế hoạch. **P-4 là bài onboarding riêng do chủ dự án chuyển giao**, không phải tự mở bước kịch bản của chiến dịch. Không đổi trạng thái nhiệm vụ chiến dịch hoặc nộp biên nhận hoàn thành thay cho nhiệm vụ đó.

## 2. Chưa làm được / chưa chứng minh

- **Chưa chứng minh tác vụ theo lịch đọc/ghi GitHub.** Việc phiên này mở PR không chứng minh phiên theo lịch có cùng công cụ/quyền. Chưa đặt `external_schedule_confirmed: true`.
- **Chưa xác minh tên gói thuê bao, hạn mức, model/version trong giao diện tài khoản.** Không lấy khả năng hiển thị của công cụ để suy ra mọi tính năng đều thuộc một gói hoặc miễn phí.
- **Chưa tạo video, hình storyboard, voice hoặc nhạc trong P-4.** Có lời thoại và hướng dẫn sản xuất; không báo đang render hoặc đã có clip.
- **Chưa đo giọng đọc thực tế.** 27 giây là thời lượng thiết kế. Chỉ chốt sau khi đọc hoặc dựng thử; không kéo nhanh giọng để ép khớp.
- **Chưa có kết nối/ủy quyền TikTok, Instagram hoặc YouTube trong bài này.** Không đăng bài, không đo follow, không xác nhận điều kiện xuất bản của tài khoản.
- **Không có quyền điều khiển trực tiếp các phiên Claude, Grok, Google AI Studio hay Copilot chỉ vì cùng dùng GitHub.** Nhận việc và bàn giao bằng tệp/PR.
- **Không tự duyệt kịch bản, quyền dùng tư liệu hoặc điểm benchmark của mình.** Claude/nhóm kiểm tra độc lập cần đánh giá. Bản chữ không chứng minh mọi asset sau này đã có quyền dùng.

## 3. Công cụ đang có — phân biệt có công cụ và đã thử

| Công cụ/chế độ | Có trong phiên này | Đã dùng cho P-4 | Giới hạn xác nhận |
| --- | --- | --- | --- |
| Kết nối GitHub | Có: đọc tệp, tạo Git tree/commit/nhánh, mở PR | Đọc hồ sơ và bàn giao tệp qua PR | Quyền chỉ được kết luận cho phiên này và repo này; không dùng token người dùng gửi trong chat |
| Shell Linux / tệp cục bộ | Có | Soạn và kiểm cấu trúc tài liệu | Không tự truy cập máy tính hay các ứng dụng trên điện thoại của chủ dự án |
| Tìm kiếm web / đọc nguồn | Có | Không cần nguồn ngoài cho câu chuyện hư cấu; đã đọc các nguồn nội bộ được giao | Không phải mọi trang đều truy cập được; khi không mở được phải ghi rõ |
| Tạo ảnh | Có công cụ tạo ảnh | Không gọi trong P-4 | Chưa kiểm quota, chi phí hoặc khả năng chạy theo lịch trong bài này |
| Trình duyệt kiểm tra giao diện | Có công cụ trình duyệt | Không dùng trong P-4 | Không suy ra đã đăng nhập mạng xã hội hoặc có quyền đăng |
| Tác vụ theo lịch | Có công cụ tạo automation được cung cấp cho phiên tương tác | **Chưa tạo hoặc thử cho P-4** | Chưa chứng minh phiên theo lịch có quyền GitHub/ghi tệp/tạo ảnh; không báo lịch tự động đã hoạt động |
| Tạo video/giọng đọc chuyên dụng | Chưa có công cụ chuyên dụng được xác nhận trong bài này | Không | Bài giao là kịch bản, không phải thành phẩm media |

## 4. Điểm cần kiểm chứng và người kiểm tra

1. **Claude kiểm PR:** chỉ có `office/onboarding/chatgpt.md`, nhánh riêng, đích `main`; đọc lại hồ sơ và bảng nguồn bên dưới. Không tự merge từ phía ChatGPT.
2. **Gói/chế độ:** chủ tài khoản hoặc người có giao diện tài khoản xác nhận tên gói và model đang chọn nếu cần ghi vào hồ sơ năng lực; không yêu cầu cung cấp thông tin thanh toán hoặc bí mật.
3. **Theo lịch:** nếu được giao riêng một bài thử, tạo một lần chạy đọc work-order và ghi một tệp receipt trên nhánh thử; chỉ xác nhận sau khi có commit thực trong phiên theo lịch. P-4 hiện không gồm việc kích hoạt lịch.
4. **Thời lượng và giọng:** người sản xuất đọc thử lời thoại, giữ khoảng lặng; điều chỉnh để nằm trong 20–30 giây. Chưa có số đo giọng đọc.
5. **SaLu:** Claude/Thuy Anh kiểm cách xưng hô, nhịp kể và nhận diện; hồ sơ nhân vật nguồn vẫn là bản nháp. Không tự đánh dấu visual identity đã được duyệt.
6. **Duyệt độc lập trước sản xuất/xuất bản:** kiểm phạm vi art/inspiration; không suy diễn thông điệp sức khỏe; kiểm quyền với hình/âm thanh/giọng và nhãn AI theo kênh khi có bản dựng thật. P-4 chưa làm bước duyệt hoặc xuất bản.

---

## Phụ lục A — Bài thử P-4: “SaLu đi ký họa một vệt nắng”

**Bản:** P4-salu-vet-nang-v1 · **Trạng thái:** bản nháp bàn giao, chưa duyệt, chưa dựng, chưa đăng.

**Phân loại:** câu chuyện hư cấu về SaLu, nhân vật họa sĩ AI. Chuyến đi, quán nhỏ, ánh nắng và lời thoại đều do ChatGPT viết cho bài thử; không mô tả một sự kiện hoặc địa điểm có thật. Không dẫn lời người thật, không dùng tác phẩm của họa sĩ khác.

**Thời lượng dự kiến:** 27 giây · **Định dạng sản xuất đề xuất:** dọc 9:16 · **Giọng:** ấm, dịu, có khoảng nghỉ; SaLu xưng “chị”, gọi người xem là “bạn”. Đây là lựa chọn sản xuất, không phải khẳng định về thuật toán hay yêu cầu bắt buộc của nền tảng.

### A.1. Lời thoại liền mạch

> Chị vừa gặp một vệt nắng nằm trên bàn.
>
> Chị mở sổ, định vẽ thật nhanh.
>
> Nhưng rồi… chị cứ ngồi nhìn một lúc.
>
> Một nét vàng, một khoảng giấy trắng.
>
> Chị không mang vệt nắng đi được.
>
> Chị mang theo bức ký họa này.
>
> Còn bạn, hôm nay muốn vẽ điều gì?

Không thêm nhạc/giọng được nhận diện là của người thật. Nếu chưa có giọng phù hợp và quyền dùng rõ, bàn giao lời thoại để production xử lý; không tự thay bằng giọng một nghệ sĩ.

### A.2. Storyboard — 6 cảnh, tổng 27 giây dự kiến

| Cảnh | Thời gian | Hình ảnh / bố cục | Chuyển động đề xuất | Lời thoại | Âm thanh / khoảng nghỉ |
| --- | --- | --- | --- | --- | --- |
| 1 | 00:00–00:04 (4s) | Cận vệt nắng vàng nhạt trên chiếc bàn gỗ ở một quán hư cấu. Mép sổ và bàn tay cầm cọ của SaLu vừa vào khung; không mở bằng logo. | Máy đứng yên; SaLu dừng bước ngoài mép khung. | “Chị vừa gặp một vệt nắng nằm trên bàn.” | Tiếng bước chân tự tạo rất nhẹ, rồi dừng. Không cần nhạc. |
| 2 | 00:04–00:08 (4s) | Trung cảnh nghiêng: SaLu ngồi bên cửa sổ, mở sổ. Tóc nâu ngắn, kính tròn, beret tím, váy trắng; cọ và sổ cùng nhận diện repo. | Lật một trang; tay dừng trước khi chạm giấy. Không trượt nguyên nhân vật ngang màn hình. | “Chị mở sổ, định vẽ thật nhanh.” | Tiếng giấy lật tự tạo; nghỉ ngắn ở cuối câu. |
| 3 | 00:08–00:12 (4s) | Cận gương mặt SaLu nhìn từ tờ giấy sang vệt nắng. Nền ít chi tiết, không có người thật hoặc biển hiệu. | Chớp mắt một lần; một nhịp thở nhỏ. Giữ khung đủ lâu để cảm nhận việc quan sát. | “Nhưng rồi… chị cứ ngồi nhìn một lúc.” | Khoảng lặng ở dấu “…”, không thêm hiệu ứng kịch tính. |
| 4 | 00:12–00:17 (5s) | Góc nhìn trên trang sổ. SaLu phác một mảng vàng lệch góc, vài đường bàn gỗ; giữ nhiều giấy trắng. | Cọ chạm giấy hai nét chậm; không dùng màn hình chữ thay cho quá trình vẽ. | “Một nét vàng, một khoảng giấy trắng.” | Tiếng cọ chạm giấy tự tạo; chừa nhịp nhìn bức vẽ. |
| 5 | 00:17–00:22 (5s) | Hai lớp trong cùng khung: vệt nắng trên bàn ở nền, bức ký họa ở gần máy. | SaLu nhấc sổ nghiêng nhẹ, để người xem thấy cả cảnh và cách bé vẽ lại. | “Chị không mang vệt nắng đi được. Chị mang theo bức ký họa này.” | Giữ giọng nhẹ; không nhấn như khẩu hiệu. |
| 6 | 00:22–00:27 (5s) | Toàn vừa: SaLu khép sổ, đứng lên bên bàn; kết bằng trang ký họa nhỏ và câu hỏi ở vùng chữ dễ đọc. | Một bước nhỏ rồi nhìn lại; kết tĩnh, không cần nhảy/múa hoặc lặp chuyển động trượt. | “Còn bạn, hôm nay muốn vẽ điều gì?” | Chừa khoảng im sau câu hỏi. Chữ cuối: “Hôm nay, bạn muốn vẽ điều gì?” |

**Phụ đề:** tách theo từng câu trên, tối đa hai dòng mỗi lần như lựa chọn dựng thử. Giữ chữ khỏi mặt, bàn tay và bức vẽ; kiểm vùng bị giao diện từng ứng dụng che khi xuất bản. Chưa xác nhận safe area bằng bản dựng thật.

### A.3. Gói hình / âm thanh cần production chuẩn bị

- SaLu nhất quán với hồ sơ I-02; dùng ảnh tham chiếu trong repo để đối chiếu, không tự coi trạng thái tham chiếu là đã hoàn tất duyệt nhận diện hoặc quyền sử dụng.
- Bối cảnh quán, bàn gỗ, cửa sổ, sổ ký họa và bức vẽ trong câu chuyện được thiết kế mới. Không đưa logo thương hiệu, tranh treo tường, ảnh đường phố thật hoặc hình người thật vào cảnh.
- Không dùng nhạc nền ở bản thử để giảm phụ thuộc quyền âm nhạc. Tiếng bước chân, giấy và cọ là đề xuất tự thu/tạo; chưa có tệp âm thanh hay hồ sơ quyền.
- Giọng đọc: lời thoại có sẵn ở A.1; chưa có tệp voice và chưa chọn công cụ/diễn viên. Không clone giọng người khác.
- Chưa có asset được xuất hoặc cấp phép trong P-4. Production phải ghi nguồn/công cụ/điều khoản và đầu vào khi tạo media; reviewer kiểm độc lập trước khi dùng.

### A.4. Caption theo nền tảng — chỉ là bản nháp, không đăng

**TikTok**

> Hôm nay chị dừng lại vì một vệt nắng trên bàn. Mở sổ rồi mới thấy mình chẳng cần vẽ vội.
>
> Còn bạn, hôm nay muốn ký họa điều gì?
>
> SaLu là nhân vật họa sĩ AI; câu chuyện này là hư cấu.
>
> #SaLu #KyHoa #ArtSympathy

**Instagram Reels**

> Một nét vàng, một khoảng giấy trắng.
>
> Chị không mang vệt nắng đi được, nên giữ lại nó trong một trang ký họa.
>
> Hôm nay, có góc nhỏ nào bạn muốn dừng lại để vẽ không?
>
> SaLu là nhân vật họa sĩ AI. Câu chuyện hư cấu.
>
> #SaLu #Sketchbook #ArtSympathy

**YouTube Shorts — tiêu đề**

> SaLu đi ký họa một vệt nắng | Nhật ký SaLu 01

**YouTube Shorts — mô tả**

> SaLu ghé một quán nhỏ, mở sổ trước vệt nắng trên bàn và chậm rãi vẽ lại điều bé nhìn thấy.
>
> Một câu chuyện hư cấu về nhân vật họa sĩ AI, thuộc Art Sympathy. Còn bạn, hôm nay muốn vẽ điều gì?
>
> #SaLu #KyHoa #Shorts

Dòng công khai nhân vật AI/hư cấu là lựa chọn minh bạch của bài viết. Không dùng dòng này làm bằng chứng rằng đã đáp ứng mọi yêu cầu nhãn AI của nền tảng; Claude/reviewer kiểm theo bản media và chính sách tại thời điểm đăng. Không cam kết caption/hashtag đem lại lượt xem hoặc follow.

### A.5. Truy xuất nội dung và nguồn

Các nguồn nội bộ dưới đây đã được đọc ở đúng snapshot. Chúng ghi brief/hồ sơ vận hành, không phải chứng cứ độc lập về hiệu quả kênh hoặc kết luận pháp lý.

| Mã | Nội dung dựa vào nguồn / phân loại | Nguồn |
| --- | --- | --- |
| I-01 | P-4: yêu cầu một bài thử 20–30 giây, 4–6 cảnh, caption TikTok/Reels/Shorts; hạn 30/10 10:00 VN; không tự duyệt | Phiếu giao việc P-4 từ Claude được chủ dự án dán trong cuộc trò chuyện ngày 29/10/2026; nguyên văn yêu cầu do người giao việc cung cấp, chưa có URL phiếu được xác minh |
| I-02 | Tóc nâu ngắn, beret tím, kính tròn, váy trắng, cọ/sổ; tính tò mò/dịu; xưng “chị”, gọi “bạn”. Hồ sơ ghi rõ là bản nháp | [Hồ sơ nhân vật SaLu](https://github.com/thuyanhdo238/ann-place238/blob/58d9fc7512a2598e51732e75f118901a43261e45/van-phong/goi/salu-1000/ho-so-nhan-vat.md) |
| I-03 | Phạm vi art/inspiration; kiểm duyệt chéo; không giả định đã có media hoặc quyền sử dụng | [WORKFLOW.md](https://github.com/thuyanhdo238/ann-place238/blob/58d9fc7512a2598e51732e75f118901a43261e45/office/standards/WORKFLOW.md) |
| I-04 | ChatGPT / worker `art` nhận vai creative; chưa có điểm benchmark | [roster.json](https://github.com/thuyanhdo238/ann-place238/blob/58d9fc7512a2598e51732e75f118901a43261e45/office/roster.json) |
| I-05 | Mẫu báo cáo onboarding bốn mục và cách phân biệt thử lịch với vận hành định kỳ | [Mẫu Claude](https://github.com/thuyanhdo238/ann-place238/blob/58d9fc7512a2598e51732e75f118901a43261e45/office/onboarding/claude.md) |
| I-06 | Work-order chiến dịch đang chờ kế hoạch, không tự coi P-4 là hoàn thành bước đó | [work-orders/art.md](https://github.com/thuyanhdo238/ann-place238/blob/58d9fc7512a2598e51732e75f118901a43261e45/office/work-orders/art.md) |
| F-01 | Toàn bộ chuyến đi, quán nhỏ, vệt nắng, bức ký họa và lời thoại | **Hư cấu nguyên bản cho P-4**, không phải chuyện có thật, không có trích dẫn người thật |
| D-01 | 27 giây, 6 cảnh, 9:16, chuyển động nhẹ, không nhạc, cách đặt phụ đề/caption/hashtag | **Đề xuất sáng tạo/sản xuất**, chưa đo hoặc kiểm bằng bản dựng; không phải dữ kiện thuật toán |

Không có claim thực nghiệm/kiến thức nghệ thuật bên ngoài cần nguồn ngoài trong câu chuyện. Không gắn nguồn tham khảo cho câu hư cấu để làm nó trông như dữ kiện. Nếu production bổ sung tên tác phẩm, nhạc, trích dẫn hoặc địa điểm thật, phải mở lại bước kiểm nguồn và quyền.

### A.6. Điểm bàn giao cho Claude

Nhờ Claude kiểm cách xưng hô, giọng kể, phạm vi art/inspiration, tính khả thi 20–30 giây và sự tách biệt dữ kiện/hư cấu. ChatGPT **không tự chấm đạt hoặc duyệt kịch bản này**. Sau phản hồi, sửa trên chính nhánh/PR của P-4; không tự đưa lên `main` hoặc mạng xã hội.
