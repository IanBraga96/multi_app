#!/bin/bash
python -m PyInstaller --onefile \
    --add-data "src/multi_app/resources:resources" \
    --hidden-import PyQt5 \
    --hidden-import PyPDF2 \
    --hidden-import pdf2image \
    --hidden-import pytesseract \
    --hidden-import python-docx \
    --hidden-import pandas \
    --hidden-import reportlab \
    src/multi_app/main.py \
    --name multi_app