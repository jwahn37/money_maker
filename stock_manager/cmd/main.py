from excel import excel
from stock import stock

if __name__ == "__main__":
    filePath = "/Users/jwahn37/Dropbox/제테크/돈관리_2022.xlsx"
    sheetName = "투자2월"
    excel = excel.Excel(filePath=filePath, sheetName=sheetName, stock=stock.Stock())
    excel.getStockPrice(nameRange = 'D2:D40', priceRange = 'F2:F40')
    excel.getUSD('M84')
