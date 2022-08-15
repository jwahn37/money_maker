#!/bin/bash

cd "$(dirname "$0")"
export PYTHONPATH="$(pwd)"
# Current OS is MAC OS. 
# If you use window, refer to https://docs.python.org/ko/3/library/venv.html
source env/bin/activate 
python3 cmd/main.py example.xlsx Sheet1 A2:A40 B2:B40 --dollar D2