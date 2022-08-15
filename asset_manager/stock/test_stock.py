from stock import stock
import unittest
from unittest.mock import patch
class TestExcel(unittest.TestCase):
    @patch("requests.get")
    def test_get_stock_code(self, mock_get):
        response = mock_get.return_value
        response.status_code = 200
        response.json.return_value = {

        }

        code = stock.Stock().getStockCode("hello")

        pass
    def test_get_USD(self):
        pass
    def test_get_price_from_code(self):
        pass
    def test_get_price(self):
        pass
    def test_get_stock_price(self):
        pass
    def test_get_coin_price(self):
        pass
    def test_get_metal_code(self):
        pass
    def test_get_fund_price(self):
        pass
    def test_fund_data(self):
        pass
    def test_get_temp_data(self):
        pass
