from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QTextEdit, QHBoxLayout, QStackedWidget, QInputDialog, QMessageBox, QLabel
from PyQt5.QtCore import pyqtSignal
from converter import convert_pdf_to_images, convert_image_to_text, convert_word_to_text, convert_excel_to_text, remove_pdf_pages
import sys

class PDFConverterGUI(QWidget):
    pdf_selected = pyqtSignal(str)  # Define um sinal para emitir o caminho do PDF
    image_selected = pyqtSignal(str)  # Define um sinal para emitir o caminho da imagem

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Multi-App')
        layout = QHBoxLayout()

        # Adiciona um QLabel para exibir mensagens
        self.label = QLabel()  # Cria o QLabel
        layout.addWidget(self.label)  # Adiciona ao layout

        # Painel esquerdo para opções específicas
        self.options_panel = QStackedWidget()
        self.options_panel.addWidget(self.create_pdf_options())
        self.options_panel.addWidget(self.create_image_options())
        self.options_panel.addWidget(self.create_word_options())
        self.options_panel.addWidget(self.create_excel_options())
        
        # Painel direito para seleção de tipo de arquivo
        self.file_type_panel = QWidget()
        file_type_layout = QVBoxLayout()
        
        self.pdf_button = QPushButton('PDF')
        self.pdf_button.clicked.connect(self.show_pdf_options)
        file_type_layout.addWidget(self.pdf_button)
        
        self.image_button = QPushButton('Imagem')
        self.image_button.clicked.connect(self.show_image_options)
        file_type_layout.addWidget(self.image_button)

        self.word_button = QPushButton('Word')
        self.word_button.clicked.connect(self.show_word_options)
        file_type_layout.addWidget(self.word_button)

        self.excel_button = QPushButton('Excel')
        self.excel_button.clicked.connect(self.show_excel_options)
        file_type_layout.addWidget(self.excel_button)

        self.file_type_panel.setLayout(file_type_layout)

        # Layout principal
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.file_type_panel)
        main_layout.addWidget(self.options_panel)

        layout.addLayout(main_layout)

        # Adiciona um QTextEdit para exibir o texto
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)  # Define como somente leitura
        layout.addWidget(self.text_edit)

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

        self.pdf_edit_button = QPushButton('Editar Páginas do PDF')
        self.pdf_edit_button.clicked.connect(self.open_file_dialog_edit_pdf)
        layout.addWidget(self.pdf_edit_button)

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

    def open_file_dialog_edit_pdf(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione o PDF", "", "PDF Files (*.pdf)", options=options)
        if file_path:
            text, ok = QInputDialog.getText(self, 'Remover Páginas', 'Digite os números das páginas a remover (separados por vírgula):')
            if ok:
                try:
                    pages_to_remove = [int(num.strip()) - 1 for num in text.split(',') if num.strip().isdigit()]
                    output_path, _ = QFileDialog.getSaveFileName(self, "Salvar PDF Editado", "", "PDF Files (*.pdf)")
                    if output_path:
                        remove_pdf_pages(file_path, pages_to_remove, output_path)
                        QMessageBox.information(self, 'Sucesso', 'Páginas removidas com sucesso e PDF salvo!')
                except Exception as e:
                    QMessageBox.critical(self, 'Erro', f'Ocorreu um erro: {str(e)}')

    def open_file_dialog_image_text(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione a Imagem", "", "Image Files (*.png *.jpg *.bmp)", options=options)
        if file_path:
            text = convert_image_to_text(file_path)
            self.display_text(text)  # Atualiza a interface gráfica com o texto extraído da imagem

    def display_text(self, text):
        self.text_edit.setText(text)  # Atualiza o QTextEdit com o texto extraído

    def create_word_options(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.word_text_button = QPushButton('Word para Texto')
        self.word_text_button.clicked.connect(self.open_file_dialog_word_text)  # Dialog para abrir arquivo Word
        layout.addWidget(self.word_text_button)

        widget.setLayout(layout)
        return widget
    
    def create_excel_options(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.excel_text_button = QPushButton('Excel para Texto')
        self.excel_text_button.clicked.connect(self.open_file_dialog_excel_text)  # Dialog para abrir arquivo Excel
        layout.addWidget(self.excel_text_button)

        widget.setLayout(layout)
        return widget
    
    def show_word_options(self):
        self.options_panel.setCurrentIndex(2)  # Mostra opções de Word

    def show_excel_options(self):
        self.options_panel.setCurrentIndex(3)  # Mostra opções de Excel

    def open_file_dialog_word_text(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione o Word", "", "Word Files (*.docx)", options=options)
        if file_path:
            text = convert_word_to_text(file_path)  # Converte o Word para texto
            self.display_text(text)

    def open_file_dialog_excel_text(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione o Excel", "", "Excel Files (*.xlsx)", options=options)
        if file_path:
            text = convert_excel_to_text(file_path)  # Converte o Excel para texto
            self.display_text(text)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PDFConverterGUI()
    window.show()
    sys.exit(app.exec_())
