from setuptools import setup, find_packages

setup(
    name="multi_app",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "PyQt5",
        "PyPDF2",
        "pdf2image",
        "pytesseract",
        "python-docx",
        "pandas",
        "reportlab",
        "Pillow"
    ],
    entry_points={
        'console_scripts': [
            'multi_app=multi_app.main:main',
        ],
    },
)