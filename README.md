# pngtonasm — Hiển thị ảnh từ file `.inc` trên terminal với NASM

`pngtonasm` cho phép hiển thị ảnh được lưu ở định dạng `.inc` (RGB pixel data) trực tiếp trên terminal bằng ký tự khối `▀` (mỗi ký tự = 2 pixel dọc).

## ⚙ Yêu cầu
- Python 3.8+
- Thư viện Pillow
```bash
pip install pillow
```
- Terminal hỗ trợ ANSI 24-bit color (TrueColor)

## 🚀 Chạy file .inc
1. Đặt `show.py` và các file `.inc` chung thư mục.
2. Mở terminal tại thư mục đó.
3. Chạy:
```bash
python show.py
```
4. Chọn số tương ứng với file `.inc` muốn hiển thị.
5. Ảnh sẽ in ra **nguyên kích thước gốc**.  
   - Nếu terminal không đủ rộng/dài → ảnh sẽ bị cắt/xé và cần **Ctrl + con lăn chuột** để xem hết.

## 📌 Ghi chú
- Mỗi ký tự `▀` hiển thị 2 pixel theo chiều dọc.
- Để ảnh hiển thị đầy đủ, terminal cần ít nhất:
  ```
  chiều rộng terminal (cột)  >= chiều rộng ảnh (pixel)
  chiều cao terminal (dòng) >= chiều cao ảnh / 2
  ```
- Nếu ảnh quá lớn so với terminal, hãy phóng to cửa sổ terminal hoặc dùng công cụ resize ảnh `.inc` trước khi in.

## 🖼 Ví dụ
```bash
python show.py
Chọn file .inc để hiển thị:
1. sample.inc
2. another.inc
Nhập số: 1
```
Ảnh `sample.inc` sẽ hiển thị đúng từng pixel gốc trên terminal.
```
Ảnh `sample.inc` sẽ hiển thị đúng từng pixel gốc trên terminal.
