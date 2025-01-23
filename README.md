# MULTI_APP

Um aplicativo Python para manipulação e conversão de diferentes tipos de arquivos, com interface gráfica construída em PyQt5.

---

## Funcionalidades

O aplicativo permite:

- **PDF**

  - Extrair texto de arquivos PDF
  - Converter PDFs em imagens
  - Remover páginas específicas de PDFs
  - Converter Word para PDF

- **Imagens**

  - Extrair texto de imagens (OCR)

- **Word**

  - Extrair texto de documentos Word
  - Converter para PDF

- **Excel**
  - Extrair texto de planilhas Excel

---

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto
- **PyQt5**: Interface gráfica
- **PyPDF2**: Manipulação de PDFs
- **pdf2image**: Conversão PDF para imagem
- **PIL (Pillow)**: Manipulação de imagens
- **pytesseract**: OCR em imagens
- **python-docx**: Manipulação de documentos Word
- **pandas**: Manipulação de dados tabulares
- **reportlab**: Geração de PDFs
- **PyInstaller**: Empacotamento do aplicativo

---

## Estrutura do Projeto

```
multi_app/
│
├── pyproject.toml         # Configurações do projeto
├── requirements.txt       # Dependências
├── setup.py              # Configuração de instalação
├── src/
│   └── multi_app/
│       ├── __init__.py
│       ├── __main__.py   # Ponto de entrada
│       ├── gui.py        # Interface gráfica
│       └── converter.py  # Funções de conversão
│
└── scripts/
    ├── build_appimage.sh
    └── build_executable.sh
```

## Instalação

### Dependências do Sistema

```bash
# Ubuntu/Debian
sudo apt-get install python3-dev libpoppler-qt5-dev tesseract-ocr
```

### Configuração do Ambiente

```bash
# Clone o repositório
git clone https://github.com/IanBraga96/multi_app.git
cd multi_app

# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```

## Execução

### Desenvolvimento

```bash
# No diretório raiz do projeto
python -m multi_app
```

### Criar Executável

```bash
# Gerar executável standalone
./scripts/build_executable.sh
```

### Criar AppImage (Linux)

```bash
# Gerar AppImage para distribuição
./scripts/build_appimage.sh
```

## Uso

1. Execute o aplicativo
2. Selecione o tipo de arquivo desejado no painel lateral
3. Escolha a operação desejada
4. Selecione o arquivo de entrada
5. Aguarde o processamento
6. O resultado será exibido na interface ou salvo no local especificado

   ```

   ```

---

## Próximos Passos

O projeto está em fase inicial e ainda estou aprendendo as funcionalidades que planejo adicionar ao longo do tempo, como:

- Melhorar a interface gráfica.
- Implementar mais formatos de conversão.
- Implementar melhorias de desempenho e experiência do usuário.

---

## Contribuição

Sinta-se à vontade para contribuir com ideias ou melhorias! Você pode abrir uma issue ou enviar um pull request.

Este projeto é parte do meu aprendizado e evolução no desenvolvimento de aplicativos em Python. Vou adicionar mais funcionalidades e documentações à medida que o projeto for
tomando forma.
