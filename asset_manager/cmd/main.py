from excel import excel
from stock import stock
import argparse

if __name__ == "__main__":
    # Refer to https://docs.python.org/3/library/argparse.html#the-add-argument-method
    parser = argparse.ArgumentParser(description='Update stock price to excel')
    parser.add_argument('filePath', metavar="example.xlsx", type=str, help='an excel file path')
    parser.add_argument('sheet', metavar="Sheet1", type=str, help='an excel\'s sheet name')
    parser.add_argument('--dollar', dest="dollarCell", type=str, default='', help='Cell address for converting won(₩) to dollar($)')
    parser.add_argument('nameRange', metavar="A2:A40", type=str, help='Column range which have stock name')
    parser.add_argument('priceRange', metavar="B2:B40", type=str, help='Column range which will store stock price')
    args = parser.parse_args()

    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                 help='an integer for the accumulator')
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                 const=sum, default=max,
    #                 help='sum the integers (default: find the max)')
    
    excel = excel.Excel(filePath=args.filePath, sheetName=args.sheet, stock=stock.Stock())
    excel.getStockPrice(nameRange = args.nameRange, priceRange = args.priceRange)
    if args.dollarCell != "":
        excel.getUSD(args.dollarCell)
