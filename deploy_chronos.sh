#!/bin/bash
# deploy_chronos.sh - Automated Chronos Git Deployment Protocol
set -e

PROJECT_DIR="Chronos_Identity_Engine_2026"
cd "$(dirname "$0")"

if [ ! -d "$PROJECT_DIR" ]; then
  echo "[ERROR] $PROJECT_DIR not found. Place this script one level above the project folder."
  exit 1
fi

cd "$PROJECT_DIR"

echo "[CHRONOS] Initializing git repository..."
git init

echo "[CHRONOS] Staging all files..."
git add .

echo "[CHRONOS] Committing core payload..."
git commit -m "CHRONOS V2026: Core Initialization - Level 9 Modules Active"

echo "[CHRONOS] Enter your GitHub repository URL (e.g., git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git):"
read REPO_URL

echo "[CHRONOS] Linking remote..."
git remote add origin "$REPO_URL"

echo "[CHRONOS] Renaming branch to main..."
git branch -M main

echo "[CHRONOS] Pushing to remote..."
git push -u origin main

echo "[CHRONOS] Deployment complete."
