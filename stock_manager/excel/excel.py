import pandas as pd
import xlwings as xw
# from stock import stock

class Excel:
    def __init__(self, filePath, sheetName, stock):
        self.stock = stock
        # https://docs.xlwings.org/en/stable/quickstart.html
        self.wb = xw.Book(filePath)
        self.sheet = self.wb.sheets[sheetName]
        
    def getStockPrice(self, nameCol, priceCol):
        # self.dataFrame = sheet['A1:M41'].options(pd.DataFrame, index=False, header=True).value
        for i in range(2, 41):
            # self.sheet.range(priceCol+str(i)).value = self.stock.getPrice(self.sheet.range(nameCol+str(i)).value)
            price = self.stock.getPrice(self.sheet.range(nameCol+str(i)).value)
            if price != "":
                self.sheet.range(priceCol+str(i)).value = price

    def getUSD(self, addr):
        self.sheet.range(addr).value = self.stock.getUSD()
