To make your `README.md` look elegant and professional, you need to fix the formatting issues caused by the markdown content being compressed together in the current view. GitHub requires proper spacing (newlines) for markdown elements like lists and headers to render correctly.

Here is the cleaned-up, professionally formatted version. You can copy and paste this directly into your `README.md` file.

***

# PDF-to-Text Converter

A robust, cross-platform Python utility designed to convert PDF documents into plain text. This tool provides two distinct pathways: direct extraction for native text-based PDFs and OCR processing for scanned or image-based documents.

---

## 🚀 Key Features

* **Dual Extraction Modes:** Choose between fast direct extraction or high-accuracy OCR.
* **OCR Integration:** Leverages Tesseract for processing scanned PDFs.
* **Structure Preservation:** Includes clear page break markers (`--- Page X ---`) to maintain document context.
* **Cross-Platform:** Works seamlessly on Windows, macOS, and Linux.

---

## 🛠️ Quick Start

### 1. Installation

**Python Dependencies:**
```bash
pip install -r requirements.txt
```

**System Dependencies:**
* **macOS:** `brew install tesseract poppler`
* **Linux (Ubuntu/Debian):** `sudo apt-get install tesseract-ocr poppler-utils`
* **Windows:** Install [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) and [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/) (ensure the `bin` folder is added to your PATH).

### 2. Execution

| Mode | Command | Best For |
| :--- | :--- | :--- |
| **Simple Extraction** | `python simple_pdf_to_text.py` | Native text-based PDFs (Fast) |
| **Advanced OCR** | `python pdf_to_text.py` | Scanned/Image-based PDFs |

> **Note:** Edit the `input_file` variable within the scripts to process your custom files.

---

## 📂 Project Structure

```text
pdftoocr/
├── box.pdf               # Input sample
├── box.txt               # Output sample
├── simple_pdf_to_text.py # Direct extraction script
├── pdf_to_text.py        # OCR-based extraction script
├── requirements.txt      # Python dependencies
└── ...
```

---

## 💡 Troubleshooting

* **Poppler Issues:** Ensure `poppler/bin` is correctly added to your system PATH.
* **Tesseract Not Found:** Verify the installation path and ensure it is accessible from your command line.
* **Performance:** While direct extraction is near-instant, OCR processing speed varies based on PDF length and system hardware.

---

## 📄 License & Contributions

This project is open-source under the **MIT License**. We welcome issues and pull requests to help improve functionality!
