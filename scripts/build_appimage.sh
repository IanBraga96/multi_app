#!/bin/bash

# Criar diretório AppDir
mkdir -p AppDir/usr/bin
mkdir -p AppDir/usr/share/applications
mkdir -p AppDir/usr/share/icons/hicolor/256x256/apps

# Copiar o executável
cp dist/multi_app AppDir/usr/bin/

# Criar arquivo .desktop
cat > AppDir/usr/share/applications/multi_app.desktop << EOF
[Desktop Entry]
Name=Multi App
Exec=multi_app
Icon=multi_app
Type=Application
Categories=Office;
EOF

# Criar AppImage
appimagetool AppDir/