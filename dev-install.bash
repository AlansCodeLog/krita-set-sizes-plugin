#!/usr/bin/env bash

cp -r actions/* ~/.local/share/krita/actions/

rm -rf ~/.local/share/krita/pykrita/TenBrushSizesPlugin/
cp TenBrushSizesPlugin.desktop ~/.local/share/krita/pykrita
cp -r TenBrushSizesPlugin/ ~/.local/share/krita/pykrita
