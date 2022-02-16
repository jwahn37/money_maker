from excel import excel
from stock import stock

if __name__ == "__main__":
    filePath = "example.xlsx"
    sheetName = "Sheet1"
    dollarCell = 'D2'
    nameRange = 'A2:A40'
    priceRange = 'B2:B40'

    excel = excel.Excel(filePath=filePath, sheetName=sheetName, stock=stock.Stock())
    excel.getStockPrice(nameRange = nameRange, priceRange = priceRange)
    excel.getUSD(dollarCell)
