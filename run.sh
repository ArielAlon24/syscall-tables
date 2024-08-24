#!/bin/bash


WORKING_DIRECTORY=pwd
LINUX_DIR=~/Dev/linux/
OUTPUT=~/Dev/syscall-table/frontend/public/tables.json

# Pull Linux's new commits
cd $LINUX_DIR
git fetch
git pull

# Extract Syscalls


echo "Using $LINUX_DIR"
./src/main.py $LINUX_DIR $OUTPUT
