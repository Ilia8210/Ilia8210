#!/bin/bash
set -e

echo "=== Installing Python dependencies ==="
pip install -r requirements.txt

echo ""
echo "=== Downloading DejaVu fonts (Unicode support for PDF) ==="
mkdir -p fonts
FONT_URL="https://github.com/dejavu-fonts/dejavu-fonts/releases/download/version_2_37/dejavu-fonts-ttf-2.37.tar.bz2"
wget -q "$FONT_URL" -O /tmp/dejavu.tar.bz2
tar -xjf /tmp/dejavu.tar.bz2 -C /tmp/
cp /tmp/dejavu-fonts-ttf-2.37/ttf/DejaVuSans.ttf fonts/
cp /tmp/dejavu-fonts-ttf-2.37/ttf/DejaVuSans-Bold.ttf fonts/
rm -f /tmp/dejavu.tar.bz2
echo "Fonts installed."

echo ""
echo "=== Setup complete! ==="
echo ""
echo "Next steps:"
echo "  1. cp .env.example .env  — then fill in your credentials"
echo "  2. python auth.py        — one-time Telegram authentication"
echo "  3. python main.py        — test a manual run"
echo "  4. Add cron job for daily reports:"
echo "       crontab -e"
echo "       0 9 * * * cd $(pwd) && python main.py >> logs/run.log 2>&1"
