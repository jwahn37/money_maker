from stock.stock import Stock
from excel.excel import Excel

# import excel
# from excel import Excel
import unittest
from pathlib import Path

class TestExcel(unittest.TestCase):
    file = 'excel/test.xlsx'
    sheet = 'Sheet1'
    nameRange = 'A2:A40'
    priceRange = 'B2:B40'

    def test_get_stock_prices(self):
        excel_ = Excel(filePath=self.file, sheetName=self.sheet, stock=Stock())
        self.assertRaises(TypeError, excel_.getStockPrice, True)
        pass
    def test_get_USD(self):
        pass
