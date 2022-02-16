#!/bin/bash

cd $(pwd)
export PYTHONPATH=$(pwd)
# Current OS is MAC OS. 
# If you use window, refer to https://docs.python.org/ko/3/library/venv.html
source env/bin/activate 
python3 cmd/main.py
