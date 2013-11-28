import unittest
import yql

class TestYql(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testquery_yql(self):
        lis = []
        fields = []
        fields.append('Symbol')
        fields.append('Name')
        fields.append('StockExchange')
        fields.append('Ask')
        fields.append('Bid')
        fields.append('Change')
        fields.append('ChangeinPercent')
        fields.append('Open')
        fields.append('TradeDate')
        fields.append('PreviousClose')
        fields.append('PercentChange')
        fields.append('LastTradeDate')
        fields.append('LastTradeTime')
        fields.append('LastTradePriceOnly')
        fields.append('DaysRange')
        fields.append('DaysHigh')
        fields.append('DaysLow')
        fields.append('YearLow')
        fields.append('YearHigh')
        fields.append('PercebtChangeFromYearHigh')
        fields.append('PercentChangeFromYearLow')
        fields.append('ChangeFromYearHigh')
        fields.append('ChangeFromYearLow')
        lis.append("TCS.NS")
        lis.append("HINDALCO.NS")
        yql_ob = yql.Yql(lis, fields )
        print yql_ob.query_yql()


if __name__ == '__main__':
    unittest.main()
