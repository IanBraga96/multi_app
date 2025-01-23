import sys
from multi_app.gui import PDFConverterGUI
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    window = PDFConverterGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()