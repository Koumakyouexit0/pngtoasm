# 🖼 PNG to NASM Converter & Image Tools

A Python project that allows you to:
- **Convert PNG images** to `.inc` or `.asm` files containing image data for NASM assembly.
- **View `.inc` images** directly in the terminal using ANSI color.
- **Resize images** easily with preset resolutions.

---

## 📦 Features

1. **`main.py`** – Convert PNG → `.inc`/`.asm`
2. **`show.py`** – Display `.inc` images in terminal
3. **`rescale.py`** – Resize images

---

## 🛠 Requirements

- Python **3.x**
- Python library:
```bash
pip install pillow
```
- A terminal that supports **ANSI 24-bit color** (for best display results in `show.py`).

---

## 📂 Project Structure

```
.
├── main.py       # PNG → NASM converter
├── show.py       # Display .inc images
├── rescale.py    # Resize images
└── README.md     # Documentation
```

---

## 🚀 Usage

### 1️⃣ Convert PNG to NASM `.inc`

```bash
python3 main.py <input.png> <output.inc> [--format FORMAT] [--label LABEL] [--mode MODE]
```

**Options:**
- `--format`:
  - `rgb24` *(default)* – Each pixel stored as 3 RGB bytes.
  - `rgb565` – 16-bit color.
  - `rle` – RLE compression for RGB24.
- `--label` – Base variable name in the `.inc` file.
- `--mode`:
  - `bytes` *(default)* – output as `db`.
  - `words` – output as `dw` (for 16-bit only).

**Example:**
```bash
python3 main.py logo.png logo.inc --format rgb565 --label myimg --mode words
```
**Or:**
```bash
python3 main.py logo.png logo.inc
```

---

### 2️⃣ View `.inc` image in terminal

```bash
python3 show.py
```
- Select a `.inc` file from the list.
- The image will be displayed directly in the terminal using the `▀` character with foreground/background colors.

---

### 3️⃣ Resize an image

```bash
python3 rescale.py
```
- Choose a preset resolution: `720p`, `480p`, `360p`, `240p`, `144p`, `96p`
- Or select **Customize** to manually enter width and height.

---

## 📷 Example

**Command:**
```bash
python3 main.py cat.png cat.inc --format rgb24
python3 show.py
```
---

## 📜 License
Released under the **CC0 1.0 Universal (Public Domain Dedication)** – you may copy, modify, distribute, and use for any purpose without permission.

See details at: [https://creativecommons.org/publicdomain/zero/1.0/](https://creativecommons.org/publicdomain/zero/1.0/)

---
## Goodluck:)
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/64def9a1-41f2-48a3-9269-0a6e717986f5" />
