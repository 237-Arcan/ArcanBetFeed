#!/data/data/com.termux/files/usr/bin/bash

# Script d’auto-push vers GitHub
DATE=$(date '+%Y-%m-%d %H:%M:%S')
MESSAGE="Auto push $DATE"

echo "[🔄] Ajout des fichiers modifiés..."
git add .

echo "[📝] Commit avec message : $MESSAGE"
git commit -m "$MESSAGE"

echo "[📤] Push vers GitHub (branche main)..."
git push origin main

echo "[✅] Push terminé à $DATE"
