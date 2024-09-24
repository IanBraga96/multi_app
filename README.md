# MULTI_APP

---

Este projeto é um modelo de aplicativo que estou desenvolvendo para estudar e aprender funcionalidades do Python, com foco em manipulação de arquivos, conversão de arquivos e
extração de texto. Estou criando uma interface gráfica simples com **PyQt5** para tornar essas funcionalidades acessíveis.

---

## Funcionalidades Implementadas

Atualmente, o aplicativo permite:

- Extrair texto de arquivos PDF.
- Converter PDFs em imagens.
- Extrair texto de imagens (OCR - Optical Character Recognition).

---

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **PyPDF2**: Para leitura de PDFs.
- **pdf2image**: Para converter PDFs em imagens.
- **PIL (Pillow)**: Para manipulação de imagens.
- **pytesseract**: Para realizar OCR em imagens.
- **PyQt5**: Para a criação da interface gráfica.
- **python-docx**: Para manipulação de documentos do Word.
- **pandas**: Para manipulação de dados em tabelas.
- **openpyxl**: Para trabalhar com arquivos Excel.

---

## Como Usar

1. Clone este repositório:

   ```bash
   git clone https://github.com/IanBraga96/multi_app.git
   cd multi_app

   ```

2. Crie um ambiente virtual e instale as dependências:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate      # Windows
   pip install -r requirements.txt
   ```

3. Execute o aplicativo:
   ```bash
   python main.py
   ```

---

## Próximos Passos

O projeto está em fase inicial e ainda estou aprendendo as funcionalidades que planejo adicionar ao longo do tempo, como:

- Melhorar a interface gráfica.
- Adicionar opções para mais tipos de arquivos.
- Implementar melhorias de desempenho e experiência do usuário.

---

## Contribuindo

Sinta-se à vontade para contribuir com ideias ou melhorias! Você pode abrir uma issue ou enviar um pull request.

Este projeto é parte do meu aprendizado e evolução no desenvolvimento de aplicativos em Python. Vou adicionar mais funcionalidades e documentações à medida que o projeto for
tomando forma.
