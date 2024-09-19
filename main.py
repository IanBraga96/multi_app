from gui import PDFConverterGUI
from converter import extract_text_from_pdf
import sys
from PyQt5.QtWidgets import QApplication

class MyApp(QApplication):
    def __init__(self, *args):
        super().__init__(*args)
        self.gui = PDFConverterGUI()
        self.gui.pdf_selected.connect(self.handle_pdf_selected)
        self.gui.show()

    def handle_pdf_selected(self, file_path):
        # Aqui chamamos as funções de conversão
        text = extract_text_from_pdf(file_path)
        self.gui.display_text(text)  # Atualiza a interface gráfica com o texto extraído

if __name__ == '__main__':
    app = MyApp(sys.argv)
    sys.exit(app.exec_())
