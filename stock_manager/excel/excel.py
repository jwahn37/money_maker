import pandas as pd
import xlwings as xw
# from stock import stock

class Excel:
    def __init__(self, filePath, sheetName, stock):
        self.stock = stock
        # https://docs.xlwings.org/en/stable/quickstart.html
        self.wb = xw.Book(filePath)
        self.sheet = self.wb.sheets[sheetName]
        
    def getStockPrice(self, nameRange, priceRange):
        nameRange = self.sheet.range(nameRange)
        priceRange = self.sheet.range(priceRange)
        
        for priceRow, nameRow in zip(priceRange.rows, nameRange.rows):
            priceRow.value = self.stock.getPrice(nameRow.value)

    def getUSD(self, addr):
        self.sheet.range(addr).value = self.stock.getUSD()
