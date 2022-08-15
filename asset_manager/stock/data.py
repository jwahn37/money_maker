
USD_URL = 'https://api.stock.naver.com/marketindex/exchange/FX_USDKRW'
COIN_URL = 'https://api.upbit.com/v1/market/all'
METAL_URL = 'https://api.stock.naver.com/marketindex/metals'

FUND_URL = 'https://www.fosskorea.com/fmm/FMM1010301/selectFundList.do'
FUND_HEADERS = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'Accept': 'text/plain, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'Origin': 'https://www.fosskorea.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.fosskorea.com/fmm/FMM1010301/main.do',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            }
FUND_DATA = {
  'fsType01': 'B1',
  'fstChk02': 'BB',
  'fstChk03': '',
  'fstChk04': 'T',
  'fstChk05': 'T',
  'fstChk06': 'T',
  'fstChk07': 'T',
  'rlzRt': '',
  'type01_con1': '-9999',
  'type01_con2': '9999',
  'type02_con1': '0',
  'type02_con2': '-999',
  'type03_con1': '0',
  'type03_con2': '20',
  'saleRate': 'ON',
  'afrcvRate': 'ON',
  'gradeGbn': '1',
  'zeroin': 'T',
  'mstar': '',
  'kfr': '',
  'fng': '',
  'type04_con1': '0',
  'type04_con2': '100',
  'type05_con1': '0',
  'type05_con2': '100',
  'type06_con1': '0',
  'type06_con2': '100',
  'sClass': 'N',
  'eClass': 'N',
  'fundName2': 'KB 중국본토A주증권자투자신탁',
  'pageNo': '1',
  'pageCnt': '20',
  'openAbleYn': 'Y'
            }