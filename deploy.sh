#!/bin/bash

PROJECT_DIR=$(pwd)
LINUX_DIR=$PROJECT_DIR/linux
TABLES_OUTPUT=$PROJECT_DIR/frontend/public/tables.json
LAST_UPDATE=$PROJECT_DIR/frontend/public/last-update.txt
DATETIME=$(date -Iseconds)

# Pull Linux's new commits
cd $LINUX_DIR
git fetch
git fetch
output=$(git pull)
if [[ $output == *"Already up to date."* ]]; then
    echo "No updates found. Exiting."
    exit 0
else
    echo "Updates were found."
fi

# Extract Syscalls
cd $PROJECT_DIR/backend
source venv/bin/activate
python src/main.py $LINUX_DIR $TABLES_OUTPUT
deactivate

# Update datetime.txt
echo $DATETIME > $LAST_UPDATE

# Rebuild frontend
cd $PROJECT_DIR/frontend
npm run build

# Deploy to GitHub
./node_modules/.bin/gh-pages -d dist -m "[UPDATE] $DATETIME"


