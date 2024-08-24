#!/bin/bash

PROJECT_DIR=$(pwd)
LINUX_DIR=~/Dev/linux/
TABLES_OUTPUT=~/Dev/syscall-table/frontend/public/tables.json
LAST_UPDATE=~/Dev/syscall-table/frontend/public/last-update.txt
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
# ./node_modules/.bin/gh-pages -d dist -m "[UPDATE] $DATETIME"


