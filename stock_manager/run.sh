#!/bin/bash
cd $(pwd)
export PYTHONPATH=$(pwd)
source env/bin/activate 
python3 cmd/main.py