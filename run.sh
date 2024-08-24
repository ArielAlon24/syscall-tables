#!/bin/bash

if [ -z "$1" ]; then
  echo "No enviorment provided. Please provide an enviorment \"dev\" or \"prod\""
  exit 1
fi

ENV=$1


if [ "$ENV" = "dev" ]; then
  LINUX_DIR=~/Dev/linux
  OUTPUT=~/Dev/syscall-table/frontend/public/tables.json
  echo "Using $LINUX_DIR"
  ./src/main.py $LINUX_DIR $OUTPUT

elif [ "$ENV" = "prod" ]; then
  echo "todo"

else
  echo "Invalid argument: $ENV"
  echo "Usage: $0 {dev|prod}"
  exit 1
fi
