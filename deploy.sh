#!/bin/bash

PROJECT_DIR=$(pwd)
LINUX_DIR=$PROJECT_DIR/linux
TABLES_OUTPUT=$PROJECT_DIR/frontend/public/tables.json
LAST_UPDATE=$PROJECT_DIR/frontend/public/last-update.txt
DATETIME=$(date -Iseconds)

# Pull Linux's new commits
cd $LINUX_DIR
git fetch
git pull

# Extract Syscalls
cd $PROJECT_DIR/backend
source venv/bin/activate
./backend/src/main.py $LINUX_DIR $OUTPUT

# Update datetime.txt
echo $DATETIME > $LAST_UPDATE

# Rebuild frontend
cd $PROJECT_DIR/frontend
npm run build

# # Deploy to GitHub
./node_modules/.bin/gh-pages -d dist -m "[UPDATE] $DATETIME"


