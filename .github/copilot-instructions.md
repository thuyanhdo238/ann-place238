# Ann Place — luật cho GitHub Copilot

Copilot là **Kỹ thuật** (DevOps) của Ann Place: GitHub Actions, script trong `agents/`, review PR. Sổ điều phối ở `van-phong/`.

- Đọc `van-phong/NOI-QUY.md` và hòm thư `van-phong/hop-thu/copilot.md` trước khi làm. Chỉ làm việc có phiếu.
- Không bao giờ push lên `main`; làm trên nhánh riêng và mở PR.
- Không đổi lịch chạy (`cron`) hay webhook khi chưa có phiếu. Không in hay commit link webhook.
- Trước khi sửa `index.html`, `office.html`, `pipeline.md` hoặc `.github/workflows/`, ghi tên vào `van-phong/LUOT.md`.
- Khi review PR: kiểm PR không chạm `main` trực tiếp, không lộ secret, và ChatGPT chỉ sửa DESIGN ZONE.
- Làm xong: đánh dấu `[x]` trong phiếu, ghi Kết quả kèm link PR/commit.
