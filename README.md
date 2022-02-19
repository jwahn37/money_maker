# money_maker

## stock_manager

stock manager은 주식, 펀드, 코인, 원자재, 환율의 실시간 시세를 받아와서 엑셀에 업로드합니다. 
### 사용 방법

1. python3 이 사전에 설치되어 있어야 합니다.
2. 코드를 다운로드 받습니다. 
   - `git clone https://github.com/jwahn37/money_maker.git`
   - `cd stock_manager`
3. 가상환경을 실행합니다.
   - Linux, MacOS
       - `python3 -m venv env`
       - `source env/bin/activate`
   - Window
       - `python3 -m venv env`
       - `env\Scripts\activate.bat`
4. 관련 패키지를 설치합니다. 
   - `pip install -r requirements.txt`
5. 프로그램을 실행합니다.
  - `python3 cmd/main.py [엑셀 파일 이름] [엑셀 sheet 이름] [이름 열] [시세 열] --dollar [환율 cell]`
  - 예시
    - stock_manager/example.xlsx는 example 엑셀 파일이 있습니다.
    - `python3 cmd/main.py example.xlsx Sheet1 A2:A40 B2:B40 --dollar D2`
      - example.xlsx 파일의 Sheet1에서 A2:A40 범위의 열을 읽어와서 해당 주식 이름에 대응하는 시세정보를 B2:B40에 기록합니다. 또, D2에는 실시간 환율이 기입됩니다. 
      - `--dollar [환율 cell]`은 생략할 수 있습니다.
    - 사용할 때에는 [엑셀 파일 이름]에 파일의 절대 경로를 입력하세요.