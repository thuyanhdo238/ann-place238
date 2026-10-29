---
name: trich-xuat-tai-lieu
description: Rút thông tin có cấu trúc kèm trích dẫn nguyên văn từ tài liệu dài (sách, bài báo, báo cáo khảo cổ, văn bia, bản ghi phỏng vấn) bằng Google LangExtract, cho luận án rồng thời Lý và bài FISAT. Dùng khi cần lập bảng tổng hợp tài liệu, mã hóa phỏng vấn, hoặc /trich-xuat-tai-lieu.
---

# Trích xuất tài liệu có dẫn nguồn — LangExtract

Mục tiêu: một **bảng dữ liệu** (CSV/JSONL) mà mỗi dòng trỏ về **đúng đoạn gốc**, cộng một file **HTML tô sáng** để Thuy Anh kiểm lại. Không bịa: thông tin không tìm thấy nguyên văn trong tài liệu thì bỏ.

## 1. Chuẩn bị văn bản
- PDF có chữ: rút text (pdftotext/pypdf). PDF scan, ảnh văn bia: OCR trước (tesseract `-l vie+eng`), báo Thuy Anh những trang OCR kém.
- Mỗi tài liệu một file `.txt` UTF-8, giữ tên gốc để dẫn nguồn.

## 2. Chọn mô hình (hỏi nếu chưa rõ)
- **Tư liệu chưa công bố, phỏng vấn có thông tin cá nhân → Ollama trên máy** (miễn phí, dữ liệu không rời máy).
- Tài liệu đã công bố → Gemini qua khóa Google AI Studio (bậc miễn phí). Khóa đặt trong biến môi trường `LANGEXTRACT_API_KEY`, **không bao giờ** ghi vào file hay commit.
- Không mua API, không bật thanh toán.

## 3. Định nghĩa việc trích
`pip install langextract`. Viết prompt + **1–2 ví dụ mẫu lấy nguyên văn từ chính tài liệu**. Lược đồ gợi ý:

**Luận án — rồng thời Lý**
| Lớp | Thuộc tính |
|---|---|
| `hien_vat` | loại, chất liệu, địa điểm phát hiện, nơi lưu giữ |
| `nien_dai` | triều đại, năm/khoảng năm, độ chắc chắn |
| `dac_diem_tao_hinh` | bộ phận (thân, vảy, chân, mào, râu, ngọc), mô tả |
| `so_sanh` | đối tượng so sánh (rồng Tống, rồng Trần…), điểm giống/khác |
| `luan_diem` | tác giả, ý chính |

**FISAT — phỏng vấn/khảo sát về AI trong ngành sáng tạo**
| Lớp | Thuộc tính |
|---|---|
| `chu_de` | mã chủ đề (lợi ích, lo ngại, kỹ năng, đạo đức, bản quyền, việc làm…) |
| `cong_cu_ai` | tên công cụ, cách dùng |
| `cam_nhan` | tích cực / tiêu cực / trung lập |

## 4. Chạy và kiểm
- `lx.extract(...)`, lưu `ket-qua.jsonl`, `lx.visualize(...)` ra `ket-qua.html`, xuất thêm `bang-tong-hop.csv` (cột: tài liệu, lớp, trích nguyên văn, thuộc tính, vị trí).
- Tự kiểm 10 dòng ngẫu nhiên đối chiếu bản gốc; báo tỉ lệ đúng.

## 5. Giao
- Lưu trong thư mục nghiên cứu (không đưa tư liệu chưa công bố lên repo công khai).
- Báo Thuy Anh: số tài liệu, số dòng, tỉ lệ kiểm đúng, chỗ cần chị xem lại.
