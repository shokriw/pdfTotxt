#!/usr/bin/env python3
"""
Simple PDF to Text Converter
Tries multiple methods to extract text from PDF
"""

import os
import PyPDF2

def try_pypdf2_extraction(pdf_path):
    """Try extracting text using PyPDF2"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf = PyPDF2.PdfReader(file)
            text = ""
            for page_num, page in enumerate(pdf.pages, 1):
                page_text = page.extract_text()
                if page_text.strip():
                    text += f"\n--- Page {page_num} ---\n{page_text}\n"
            return text
    except Exception as e:
        return f"PyPDF2 extraction failed: {e}"

def main():
    input_file = "file.pdf"
    output_file = "file.txt"

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found!")
        return

    print(f"Converting {input_file} to {output_file}...")

    # Try PyPDF2 extraction first
    text = try_pypdf2_extraction(input_file)

    if text and not text.startswith("PyPDF2 extraction failed"):
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Success! Text extracted using PyPDF2")
        print(f"Saved to: {output_file}")
    else:
        print("Text extraction failed. This appears to be a scanned PDF.")
        print("You'll need to install OCR dependencies:")
        print("1. Run setup.bat to install Python packages")
        print("2. Install Tesseract OCR")
        print("3. Install poppler for Windows")

if __name__ == "__main__":
    main()