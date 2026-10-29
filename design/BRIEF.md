# 🖥️ BRIEF: Design Agent — ChatGPT

**Người giao việc:** Thuy Anh (chủ dự án Ann Place)  
**AI thực hiện:** ChatGPT (OpenAI) — chuyên frontend, UI/UX, CSS  
**Nhánh làm việc:** `design` (KHÔNG push lên `main`)  
**Lịch review:** Thuy Anh review cuối tuần, merge nếu OK

---

## 🎯 Nhiệm vụ

Cải thiện **giao diện** của Ann Place (`index.html`), làm việc trong **DESIGN ZONE** được đánh dấu.

---

## 📐 Giới hạn làm việc

### ✅ ĐƯỢC PHÉP chỉnh sửa (trong DESIGN ZONE):
```html
<!-- ╔══════════════════════════════════════════════════════╗
     ║  🎨 DESIGN ZONE — ChatGPT chỉnh sửa trong này      ║
     ╚══════════════════════════════════════════════════════╝ -->
<style>
  /* TẤT CẢ CSS ở đây */
</style>
<!-- END DESIGN ZONE -->
```

Bao gồm:
- ✅ Màu sắc (CSS variables)
- ✅ Font size, spacing, padding
- ✅ Animation (keyframes, transitions)
- ✅ Hover effects
- ✅ Mobile responsive
- ✅ Dark mode (nếu muốn thêm)

### ❌ KHÔNG ĐƯỢC đổi (LOGIC ZONE):
```html
<!-- ⚙️ LOGIC ZONE — Claude quản lý -->
<script>...</script>
<!-- END LOGIC ZONE -->
```
- ❌ Tên class, id
- ❌ Cấu trúc HTML
- ❌ JavaScript logic
- ❌ Modal data

---

## 🎨 Design Direction

**Phong cách hiện tại:** Warm parchment, scholarly, cozy office

**Palette hiện có:**
```css
--bg: #f0ebe0;        /* nền trang */
--card: #fdfaf4;      /* thẻ agent */  
--accent: #8b6914;    /* màu vàng đất */
--text: #3d2b1f;      /* chữ chính */
--muted: #6b5240;     /* chữ phụ */
--border: #d4c4a8;    /* viền */
```

**Fonts:** Inter (body), Nunito (headings)

**Có thể đề xuất:**
- Cải thiện animation entrance cho cards
- Thêm micro-interactions (button press, icon bounce)
- Cải thiện modal appearance
- Thêm scrollbar styling
- Status dot animation cho agents

---

## 📋 Workflow

1. **Pull** nhánh `design` từ GitHub
2. Chỉnh sửa CSS trong DESIGN ZONE của `index.html`
3. **Commit** với message: `design: [mô tả ngắn]`
4. **Push** lên nhánh `design`
5. Thuy Anh sẽ review và merge nếu ổn

---

## ⚠️ Lưu ý quan trọng

- **KHÔNG** đổi bất cứ thứ gì ngoài `<style>` block trong DESIGN ZONE
- **KHÔNG** push lên `main` — chỉ nhánh `design`
- Nếu muốn thêm font mới: đề xuất trong commit message, đừng tự sửa `<head>`
- Test xem modal vẫn mở được trước khi push

---

## 🔗 GitHub

```
Repo: https://github.com/thuyanhdo238/ann-place238
Branch: design
File: index.html (DESIGN ZONE only)
```
