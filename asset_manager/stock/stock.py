
# Refer to
# beautifulSoap https://wikidocs.net/85739
# json https://www.freecodecamp.org/news/python-json-how-to-convert-a-string-to-json/
import re
import requests
import json
from stock import data

status_ok = 200

class Stock:
    def __init__(self):
        pass

    def getStockCode(self, name):
        print(name)
        try:
            url = 'https://m.stock.naver.com/api/search/stock?keyword='+name
            response = requests.get(url)
            if response.status_code == status_ok:
                resTxt = response.text
                resJson = json.loads(resTxt)
                print(resJson)
                stocks = resJson["searchStocks"]
                for stock in stocks:
                    if stock["stockName"]==name:
                        code = stock["reutersCode"]
                        return code
        except:
            return ""
        return ""

    def getUSD(self):
        try:
            url = data.USD_URL
            response = requests.get(url)
            if response.status_code == status_ok:
                resTxt = response.text
                resJson = json.loads(resTxt)
                USD = resJson["exchangeInfo"]["calcPrice"]
                print("USD: ", USD)
                return USD
        except:
            return ""
        return ""

    def getPriceFromCode(self, code):
        try:
            print (code)
            urls = [
                "https://m.stock.naver.com/api/stock/"+code+"/basic",
                "https://api.stock.naver.com/stock/"+code+"/basic",
                "https://api.stock.naver.com/etf/"+code+"/basic"
            ]
            for url in urls:
            #url = "https://m.stock.naver.com/api/stock/"+code+"/basic"
                response = requests.get(url)
                if response.status_code == status_ok:
                    resTxt = response.text
                    resJson = json.loads(resTxt)
                    price = resJson["closePrice"]
                    print(price)
                    return price
        except:
            return ""
        return ""
    
    def getPrice(self, name): 
        price = self.getStockPrice(name)
        if price != "":
            return price
        price = self.getCoinPrice(name)
        if price != "":
            return price
        price = self.getMetalPrice(name)
        if price != "":
            return price
        price = self.getFundPrice(name)
        if price != "":
            return price
        # price = self.getTempData(name)
        return price

    def getStockPrice(self, name):
        code = self.getStockCode(name)
        if code != "":
            price = self.getPriceFromCode(code)
            return price
        return ""

    def getCoinCode(self, name):
        try:
            url = data.COIN_URL
            response = requests.get(url)
            if response.status_code == status_ok:
                resTxt = response.text
                resJson = json.loads(resTxt)
                for coin in resJson:
                    if coin["korean_name"] == name:
                        print(coin["market"])
                        return coin["market"]
        except:
            return ""
        return ""

    def getCoinPrice(self, name):
        code = self.getCoinCode(name)
        try:
            url = 'https://api.upbit.com/v1/ticker?markets='+code
            response = requests.get(url)
            if response.status_code == status_ok:
                resTxt = response.text
                resJson = json.loads(resTxt)
                print(resJson[0]["trade_price"])
                return resJson[0]["trade_price"]
        except:
            return ""
        return ""

    def getMetalCode(self, name):
        try:
            url = data.COIN_URL
            response = requests.get(url)
            if response.status_code == status_ok:
                resTxt = response.text
                resJson = json.loads(resTxt)
                for coin in resJson:
                    if coin["korean_name"] == name:
                        print(coin["market"])
                        return coin["market"]
        except:
            return ""
        return ""

    def getMetalPrice(self, name):
        try:
            url = data.METAL_URL
            response = requests.get(url)
            if response.status_code == status_ok:
                resTxt = response.text
                resJson = json.loads(resTxt)
                for metal in resJson:
                    if metal["name"] == name:
                        print(metal["closePrice"])
                        return metal["closePrice"]
        except:
            return ""
        return ""

    def getFundPrice(self, name):
        try:
            fundData = self.getFundData(name)
            response = requests.post(data.FUND_URL, headers=data.FUND_HEADERS, data=fundData)
            if response.status_code == status_ok:
                resTxt = response.text
                resJson = json.loads(resTxt)
                print(resJson['json']['resList'][0]['NAV'])
                return resJson['json']['resList'][0]['NAV']
        except:
            return ""
        return ""

    def getFundData(self, name):
        fundData = data.FUND_DATA
        fundData["fundName2"] = name
        return fundData

    # def getTempData(self, name):
    #     # Get Anchor protocol price
    #     if(name != "앵커프로토콜"):
    #         return ""

    #     try:
    #         URL = 'https://api.anchorprotocol.com/api/v1/anc'
    #         response = requests.get(URL)
    #         if response.status_code == status_ok:
    #             resTxt = response.text
    #             resJson = json.loads(resTxt)
    #             price = resJson['anc_price']
    #             print(price)
    #             return price
    #     except:
    #         return ""
    #     return ""        