#!/bin/bash
set -x 

cd "$(dirname "$0")"
export PYTHONPATH=$(pwd)
# Current OS is MAC OS. 
# If you use window, refer to https://docs.python.org/ko/3/library/venv.html
source env/bin/activate 
# python3 cmd/main.py /Users/jwahn37/Dropbox/제테크/돈관리_2022.xlsx '투자' C2:C36 D2:D36 --dollar W1
# python3 cmd/main.py /Users/jwahn37/Dropbox/제테크/돈관리?z_2022.xlsx 'Data' D24:D58 E24:E58 --dollar Y3
python3 C:\\Users\\jwahn\\Dropbox\\investment\\money_2022.xlsx '투자' C2:C36 D2:D36 --dollar W1

