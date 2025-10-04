Perfect 👍 Here's the **updated and enhanced `README.md`** including the **command-line usage example** — making your project more professional and developer-friendly.

---

## 🖼️ Image Resizer Tool

### 📌 Overview

**Image Resizer Tool** is a Python-based automation script that resizes and converts multiple images in batch.
It uses the **Pillow (PIL)** library for image processing and supports multiple formats.
This tool is ideal for optimizing images, preparing datasets, or bulk conversions.

---

### 🧠 Objective

To automate image resizing and format conversion using Python and Pillow.

---

### 🧰 Tools & Technologies

* **Python 3.x**
* **Pillow (PIL)**
* **os** and **argparse** modules

---

### ⚙️ Features

✅ Resize multiple images in a folder
✅ Convert image formats (PNG → JPEG, etc.)
✅ High-quality resizing using **LANCZOS** filter
✅ Custom width, height, and format through CLI
✅ Automatically creates output directory
✅ Handles corrupted or invalid files gracefully

---

### 📁 Directory Structure

```
ImageResizerTool/
│
├── image_resizer.py           # Main Python script
│
├── images_input/              # Folder containing original images
│   ├── photo1.jpg
│   ├── image2.png
│   └── sample3.jpeg
│
└── images_resized/            # Automatically created for resized images
    ├── photo1.jpeg
    ├── image2.jpeg
    └── sample3.jpeg
```

---

### 🚀 How to Run

#### **1️⃣ Install dependencies**

```bash
pip install pillow
```

#### **2️⃣ Add input images**

Place your images in the `images_input/` folder.

#### **3️⃣ Run the script (Default mode)**

```bash
python image_resizer.py
```

#### **4️⃣ Run with custom options**

You can specify width, height, and output format dynamically:

```bash
python image_resizer.py --width 1024 --height 768 --format PNG
```

---

### ⚙️ Command-Line Arguments

| Argument   | Description                     | Default          |
| ---------- | ------------------------------- | ---------------- |
| `--input`  | Input folder path               | `images_input`   |
| `--output` | Output folder path              | `images_resized` |
| `--width`  | New image width                 | `800`            |
| `--height` | New image height                | `600`            |
| `--format` | Output format (JPEG, PNG, etc.) | `JPEG`           |

---

### 📦 Example Output

```
✔ photo1.jpg → images_resized/photo1.jpeg
✔ image2.png → images_resized/image2.jpeg
✔ sample3.jpeg → images_resized/sample3.jpeg

✅ Completed: 3 images resized | ⚠️ Failed: 0
```

---

### 🧩 Key Concepts

* File Handling
* Image Processing
* Automation
* Command-Line Interfaces (CLI)

---

### 🏁 Outcome

A powerful and flexible tool that automates image resizing and conversion tasks — useful for developers, designers, and data preprocessing workflows.

---

