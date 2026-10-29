# 📡 BRIEF: Radar Agent — Grok

**Người giao việc:** Thuy Anh (chủ dự án Ann Place)  
**AI thực hiện:** Grok (xAI) — chuyên real-time web, X/Twitter trends  
**Lịch chạy:** Mỗi ngày 7:00 SA (Vietnam time = 0:00 UTC)

---

## 🎯 Nhiệm vụ

Quét tin tức mới nhất mỗi sáng trong các lĩnh vực Thuy Anh quan tâm:
- **AI & công nghệ sáng tạo** — tool mới, trend mới, release đáng chú ý
- **Art & Digital Heritage** — triển lãm, hội thảo, call for submissions
- **Design** — xu hướng UI/UX, visual culture, typography
- **Vietnam cultural tech** — bất kỳ tin nào liên quan đến VN, Đông Nam Á

---

## 📋 Cách làm

1. Tìm kiếm web (DeepSearch) với các từ khóa:
   - `"AI art" OR "generative art" site:theartnewspaper.com OR site:hyperallergic.com` (hôm nay)
   - `"digital heritage" conference 2024 2025 call for papers`
   - `AI design tools new release this week`
   - `Vietnam art exhibition digital`

2. Tóm tắt **5–8 tin** quan trọng nhất, mỗi tin:
   - Tiêu đề (tiếng Anh hoặc dịch sang tiếng Việt)
   - 1–2 câu tóm tắt
   - Link nguồn
   - Tag: [AI] / [Heritage] / [Design] / [Cơ hội]

3. Lưu kết quả vào file `output/output.md` trong folder này

---

## 📁 Output format

Lưu vào: `agents/radar/output/output.md`

```markdown
# Radar Report — [Ngày tháng năm]

## 🔥 Tin nổi bật hôm nay

### [AI] Tiêu đề tin 1
> Tóm tắt 1-2 câu bằng tiếng Việt
🔗 [Link nguồn](url)

### [Heritage] Tiêu đề tin 2
> ...

## 📅 Cơ hội / Deadline sắp tới
- ...

---
*Radar by Grok — cập nhật lúc [giờ UTC]*
```

---

## ⚠️ Lưu ý

- Chỉ tin trong **7 ngày gần nhất**
- Ưu tiên **cơ hội có deadline** (call for papers, grants, exhibitions)
- **Không** tóm tắt tin cũ đã có tuần trước
- Commit file lên GitHub nhánh `main`, path: `agents/radar/output/output.md`

---

## 🔗 GitHub repo

`https://github.com/thuyanhdo238/ann-place238` → folder `agents/radar/output/`
