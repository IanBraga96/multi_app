import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit, QHBoxLayout, QStackedWidget, QFormLayout
from PyQt5.QtCore import pyqtSignal
from converter import extract_text_from_pdf, convert_pdf_to_images, convert_image_to_text

class PDFConverterGUI(QWidget):
    pdf_selected = pyqtSignal(str)  # Define um sinal para emitir o caminho do PDF
    image_selected = pyqtSignal(str)  # Define um sinal para emitir o caminho da imagem

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Conversor de Arquivos')
        layout = QHBoxLayout()

        # Painel esquerdo para opções específicas
        self.options_panel = QStackedWidget()
        self.options_panel.addWidget(self.create_pdf_options())
        self.options_panel.addWidget(self.create_image_options())
        
        # Painel direito para seleção de tipo de arquivo
        self.file_type_panel = QWidget()
        file_type_layout = QVBoxLayout()
        
        self.pdf_button = QPushButton('PDF')
        self.pdf_button.clicked.connect(self.show_pdf_options)
        file_type_layout.addWidget(self.pdf_button)
        
        self.image_button = QPushButton('Imagem')
        self.image_button.clicked.connect(self.show_image_options)
        file_type_layout.addWidget(self.image_button)

        self.file_type_panel.setLayout(file_type_layout)

        # Layout principal
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.file_type_panel)
        main_layout.addWidget(self.options_panel)

        layout.addLayout(main_layout)
        self.setLayout(layout)

    def create_pdf_options(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        self.pdf_text_button = QPushButton('PDF para Texto')
        self.pdf_text_button.clicked.connect(self.open_file_dialog_pdf_text)
        layout.addWidget(self.pdf_text_button)

        self.pdf_image_button = QPushButton('PDF para Imagem')
        self.pdf_image_button.clicked.connect(self.open_file_dialog_pdf_image)
        layout.addWidget(self.pdf_image_button)

        widget.setLayout(layout)
        return widget

    def create_image_options(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        self.image_text_button = QPushButton('Imagem para Texto')
        self.image_text_button.clicked.connect(self.open_file_dialog_image_text)
        layout.addWidget(self.image_text_button)

        widget.setLayout(layout)
        return widget

    def show_pdf_options(self):
        self.options_panel.setCurrentIndex(0)  # Mostra opções para PDF

    def show_image_options(self):
        self.options_panel.setCurrentIndex(1)  # Mostra opções para imagem

    def open_file_dialog_pdf_text(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione o PDF", "", "PDF Files (*.pdf)", options=options)
        if file_path:
            self.label.setText(f"Arquivo PDF Selecionado: {file_path}")
            self.pdf_selected.emit(file_path)  # Emite o caminho do arquivo selecionado

    def open_file_dialog_pdf_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione o PDF", "", "PDF Files (*.pdf)", options=options)
        if file_path:
            output_folder = QFileDialog.getExistingDirectory(self, "Selecione o diretório para salvar as imagens")
            if output_folder:
                # Aqui você chamaria a função para converter PDF em imagens
                convert_pdf_to_images(file_path, output_folder)
                self.label.setText(f"PDF convertido para imagens e salvo em: {output_folder}")

    def open_file_dialog_image_text(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione a Imagem", "", "Image Files (*.png *.jpg *.bmp)", options=options)
        if file_path:
            text = convert_image_to_text(file_path)
            self.display_text(text)  # Atualiza a interface gráfica com o texto extraído da imagem

    def display_text(self, text):
        self.text_edit.setText(text)  # Atualiza o QTextEdit com o texto extraído

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PDFConverterGUI()
    window.show()
    sys.exit(app.exec_())
