from gui import PDFConverterGUI
from converter import extract_text_from_pdf
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, pyqtSignal

class MyApp(QApplication):
    def __init__(self, *args):
        super().__init__(*args)
        self.gui = PDFConverterGUI()
        self.gui.pdf_selected.connect(self.handle_pdf_selected)
        self.gui.show()

    def handle_pdf_selected(self, file_path):
        self.gui.label.setText("Processando...")
    
        self.worker = Worker(extract_text_from_pdf, file_path)
        self.worker.finished.connect(self.on_worker_finished)
        self.worker.start()

    def on_worker_finished(self, text):
        self.gui.display_text(text)
        self.gui.label.setText("Processamento concluído")

class Worker(QThread):
    finished = pyqtSignal(str)

    def __init__(self, func, *args):
        super().__init__()
        self.func = func
        self.args = args

    def run(self):
        result = self.func(*self.args)
        self.finished.emit(result)

if __name__ == '__main__':
    app = MyApp(sys.argv)
    sys.exit(app.exec_())