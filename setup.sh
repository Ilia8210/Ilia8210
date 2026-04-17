#!/bin/bash
set -e

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Downloading fonts..."
mkdir -p fonts
wget -q "https://github.com/dejavu-fonts/dejavu-fonts/releases/download/version_2_37/dejavu-fonts-ttf-2.37.tar.bz2" -O /tmp/dejavu.tar.bz2
tar -xjf /tmp/dejavu.tar.bz2 -C /tmp/
cp /tmp/dejavu-fonts-ttf-2.37/ttf/DejaVuSans.ttf fonts/
cp /tmp/dejavu-fonts-ttf-2.37/ttf/DejaVuSans-Bold.ttf fonts/
rm /tmp/dejavu.tar.bz2

echo "Done! Run: python main.py"
