# D · Nghiên cứu

[← Mục lục](README.md)

**Chuỗi gợi ý cho luận án & FISAT:** chọn câu hỏi (D2) → tìm bài báo (D3) → chép lời phỏng vấn trên máy (B4 VoiceStudio) → trích xuất có dẫn nguồn (D1) → thống kê, biểu đồ (D4).

## D1
### LangExtract (Google) + `/trich-xuat-tai-lieu` · ✅ skill Ann Place · đánh giá 29/10/2026
- **Là gì:** Thư viện Python dùng AI rút thông tin có cấu trúc từ văn bản dài; **mỗi thông tin trỏ về đúng câu gốc**, kèm file HTML tô sáng để kiểm. Xử lý tài liệu dài (chia đoạn, chạy song song). Apache 2.0.
- **Hợp với Ann Place:**
  - Luận án rồng Lý: bảng *hiện vật · niên đại · địa điểm · đặc điểm tạo hình · so sánh* từ sách, báo cáo khảo cổ, văn bia — có trích dẫn (chương 2).
  - FISAT: mã hóa phỏng vấn/khảo sát theo chủ đề, có trích nguyên văn.
- **Lưu ý:** Cần mô hình AI phía sau. Gemini (khóa Google AI Studio, bậc miễn phí — Google có thể dùng dữ liệu gửi lên) **hoặc Ollama trên máy** cho tư liệu chưa công bố/phỏng vấn. Ảnh/PDF scan phải OCR trước. Không đưa tư liệu chưa công bố lên repo công khai.
- **Cách dùng:** `/trich-xuat-tai-lieu lập bảng đặc điểm tạo hình rồng từ 3 file PDF này, chạy bằng Ollama`
- **File:** [`.claude/skills/trich-xuat-tai-lieu/SKILL.md`](../.claude/skills/trich-xuat-tai-lieu/SKILL.md) · **Nguồn:** https://github.com/google/langextract · Demo: https://google-langextract.hf.space/

## D2
### `/chon-de-tai-nghien-cuu` · ✅ đã cài
- **Là gì:** Skill của Anthropic (gốc tên `scientific-problem-selection`, plugin bio-research) dựa trên khung chọn đề tài của Fischbach & Walsh (Cell, 2024): trình bày ý tưởng → thử thách → đánh giá rủi ro → cây quyết định. Cách làm không gắn với sinh học.
- **Hợp với Ann Place:** Đề cương PhD RMIT; câu hỏi "chọn hướng digital heritage methodology" (hạn 15/11 trong `pipeline.md`).
- **Cách dùng:** `/chon-de-tai-nghien-cuu tôi đang phân vân giữa 3 hướng methodology cho luận án: …`
- **Nguồn:** https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/scientific-problem-selection

## D3
### Plugin Bio-research — connector Consensus, Wiley · 📦
- **Là gì:** Plugin cho nghiên cứu sinh học; phần dùng được cho ngành khác: **Consensus** (tìm bài báo mọi ngành), **Wiley** (có tạp chí design, văn hóa).
- **Lưu ý:** Các skill còn lại (RNA tế bào, nextflow, dữ liệu thiết bị lab) và PubMed/ChEMBL không liên quan.
- **Khi nào lấy ra:** lúc tổng hợp tài liệu chương 2.
- **Nguồn:** https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research

## D4
### Plugin Data · 📦 khi có số liệu FISAT
- **Là gì:** Thống kê mô tả, kiểm định, phát hiện ngoại lai, vẽ biểu đồ, dashboard, viết SQL.
- **Nguồn:** https://github.com/anthropics/knowledge-work-plugins/tree/main/data
