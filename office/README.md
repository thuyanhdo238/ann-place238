# Ann Place — nhận việc và bàn giao theo lịch

Brief thử: xây kênh Art Sympathy / SaLu tới 1.000 người theo dõi. Phạm vi chỉ art và inspiration. Nền tảng, thời hạn, cách tính KPI và số follow ban đầu chưa được quyết định. Không hứa chắc chắn đạt KPI.

## Cách vận hành

GitHub giữ nhiệm vụ, đầu ra và báo cáo. `controller.py` là chương trình điều phối **theo quy tắc**, không phải Claude hay một AI leader chạy ngầm. Nó không gọi API AI, không mở các ứng dụng, không gửi tin Discord, không dựng hoặc đăng video. Nó đọc chứng cứ bàn giao và tạo công việc tiếp theo.

Lịch GitHub dự kiến: 08:00, 10:00, 13:00, 17:00 giờ Việt Nam. Actions có thể chạy muộn, không phải đồng hồ đảm bảo đúng phút. Workflow hoạt động sau khi gộp vào nhánh mặc định; chạy thêm khi có thay đổi brief, cấu hình hoặc bàn giao. Không tự thêm lịch trong tài khoản AI của bạn.

Mỗi ứng dụng AI cần được đặt lịch riêng để:
1. Đọc `office/work-orders/<worker>.md` bản mới nhất trên main.
2. Chỉ làm nhiệm vụ `ready`; đọc đầu ra dependency trước. Không làm lại nhiệm vụ đã nộp.
3. Lưu tệp vào đúng `expected_output` và push GitHub; không chỉ báo trong chat.
4. Nộp biên nhận `office/submissions/<task_id>.json`. Nếu không làm được, báo `blocked` và lý do cụ thể.
5. Leader AI ở lịch riêng đọc `office/board.json`, báo cáo và brief; bổ sung phân tích/đề xuất, không giả định worker đã chạy chỉ vì đến giờ.

Kết nối GitHub với ứng dụng **không chứng minh** tác vụ định kỳ của ứng dụng có thể tự đọc/ghi repo. Phải kiểm chứng từng ứng dụng bằng một lần bàn giao thật trước khi bật `external_schedule_confirmed`.

## Phân công hiện tại

- `general`: điều phối và lập kế hoạch; script cũ chỉ báo cáo theo quy tắc.
- `radar`: nghiên cứu; RSS và báo cáo Grok hiện có không tự tính là hoàn thành brief này.
- `art`: nội dung; kho nội dung viết sẵn hiện có không phải video hoàn chỉnh.
- `chance`: script cũ chọn câu trích dẫn. Chưa tự đổi thành worker sản xuất.
- `opportunity`: script cũ đọc RSS cơ hội. Chưa tự đổi thành worker xuất bản.

Bước sản xuất, kiểm duyệt và xuất bản chưa phân công: sửa `stage_workers` khi đã xác nhận worker thực sự dùng được công cụ tương ứng. Có thể một worker nhận nhiều bước; `general` vẫn điều phối. Không cần tạo thêm nhân sự chỉ để đủ hình trên dashboard.

## Chuỗi công việc

Nghiên cứu → kế hoạch → kịch bản → video → kiểm duyệt → xuất bản → đo kết quả. Một vòng nội dung đang mở được giữ nguyên giữa các lần chạy; không tạo lại hàng loạt mỗi ngày. KPI kênh cần nhiều vòng thử, không phải một video là đạt 1.000 follow.

Các hạn trong board là mốc bàn giao nội bộ ban đầu, không phải cam kết ngày đạt KPI. Sau khi leader lập kế hoạch, điều chỉnh theo lịch được thống nhất.

Biên nhận ví dụ (thay id bằng mã nhiệm vụ thực tế):

```json
{
  "task_id": "salu-first-1000-research",
  "worker": "radar",
  "status": "completed",
  "submitted_at": "2026-10-29T09:00:00+07:00",
  "artifacts": ["office/artifacts/salu-first-1000-research/research.md"],
  "source_urls": ["https://example.org/source"]
}
```

Research phải ghi nguồn, thời điểm xuất bản, lý do hợp SaLu và đề xuất 3 thử nghiệm. Plan phải nêu nền tảng, giả thuyết, lịch nội dung, người phụ trách, chỉ số đo và điều kiện tiếp tục/dừng. Script phải có storyboard, lời thoại, caption, hướng dẫn hình và nguồn tư liệu. Video phải là tệp thật; biên nhận không tự dựng video. Không commit video lớn; thiết kế lưu trữ bên ngoài cần được thống nhất trước.

Review bắt buộc `review.json` với `content_pass`, `sources_checked`, `rights_checked`, `platform_checked` đều true. Đây là kiểm tra của worker, không phải chứng nhận pháp lý. Xuất bản chỉ được mở khi cấu hình nền tảng/kênh, quy tắc xuất bản và quyền thao tác đã được xác nhận; `published.json` cần link bài đã đăng. Metrics ghi số thực đo, thời điểm đo và link nguồn; không tạo số follow hoặc dự đoán thành số thực.

Báo bị chặn:

```json
{"task_id":"salu-first-1000-research","worker":"radar","status":"blocked","submitted_at":"2026-10-29T09:00:00+07:00","reason":"Không có quyền tìm web trong tác vụ định kỳ"}
```

## Quyết định và giới hạn

`office/campaign.json`: brief và các giá trị cần bạn quyết định. `office/config.json`: worker và quy tắc. Chỉ sửa các giá trị đã được bạn chấp thuận; không tự chi tiền. `office/decisions.json` dành cho lịch sử quyết định về sau, hiện không điều khiển tác vụ. Dashboard trên GitHub Pages chỉ đọc, không giả lập nút duyệt như thể đã ghi GitHub. Không đưa token/webhook vào các file công khai.

Thử tại máy: `python3 office/controller.py`. Kiểm tra: `python3 -m unittest discover -s tests`. Không chạy các script Discord cũ để thử bộ điều phối này.

Dashboard đọc board công khai từ main trên raw.githubusercontent.com để cập nhật theo lần bàn giao, không cần Pages build lại cho mỗi commit do GitHub Actions tạo. Nếu không truy cập được, dùng bản đệm theo lần build; xem thời điểm cập nhật trong trang Văn phòng AI. Các điểm thiếu về chiến lược nằm trong danh sách leader chuẩn bị; chỉ hiện yêu cầu bạn quyết định khi đã có kế hoạch bàn giao. Ngân sách khởi đầu 0 đồng, chi mới phải hỏi.

## Chuẩn 1.0 và kế hoạch kênh

Đọc `office/standards/WORKFLOW.md` và `office/standards/CHANNEL_PLAN.md`. `office/roster.json` là năm vai đích, chưa phải kết quả benchmark hay xác nhận năng lực công cụ. Không tự ghi Chance đã dựng video hoặc Opportunity đã đăng bài chỉ vì có tên trong roster. `sources.json` bắt buộc cho research; review cần reviewer độc lập, căn cứ quyền theo nền tảng và hash đúng video. Validator kiểm hồ sơ, không chứng thực nội dung nguồn hay kết luận pháp lý. Các mẫu trong `office/templates` là mẫu trống/minh họa, không phải bàn giao đã đạt.
