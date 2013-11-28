import urllib2
import httplib
import types
import json

from utility import *


BASE_URL = "http://query.yahooapis.com/v1/public/yql"
APPEND_URL = "&diagnostics=true&env=http%3A%2F%2Fdatatables.org%2Falltables.env"
QUERY = "select %s from yahoo.finance.quotes where symbol in "
RESPONSE_FORMAT = "json"


class Yql(object):

    def __init__(self, symbols, fields='*'):
        self.base_url = BASE_URL
        self.append_url = APPEND_URL
        self.query = QUERY
        self.format= RESPONSE_FORMAT
        self.url = ''
        self.symbols = symbols
        self.fields = fields
        self.encoded_url = ''
        self.res_data = ''

    def _build_url(self):
        
        #only specific fields are required
        if isinstance(self.fields, types.ListType):
            #Field 'Symbol' is required in the response for further processing
            if 'Symbol' not in self.fields:
                self.fields.append('Symbol')
            #All fields should be separated by ','
            field_str = ",".join(self.fields)
            #print field_str
            self.query = self.query % (field_str)
           
        #all fields are required 
        elif self.fields == '*':
            self.query = self.query % (self.fields)
        
        #only one field required    
        else:
            if self.fields != 'Symbol':
                field_str = self.fields + ", " + 'Symbol'
            else:
                field_str = self.fields
            self.query = self.query % (self.fields)
            
        if isinstance(self.symbols, types.ListType):
            for index, symbol in enumerate(self.symbols):
                self.symbols[index] = '\"' + symbol +'\"'
            self.url = ','.join(self.symbols) 
            #print self.url           
        else:
            self.url = '\"' + self.symbols + '\"'
            
        encoded_url=urllib2.quote((self.query + "(" + self.url + ")").encode('utf8'))
        #print encoded_url
        self.encoded_url= self.base_url + "?q=" + encoded_url + self.append_url + "&format=" + self.format
        #print "**************************************"
        #print self.encoded_url

    def _parse_response(self, response):
        #print type(response)
        json_data=json.loads(response)
        count = json_data['query']['count']
        #print 'count : ', count
        data = json_data['query']['results']['quote']
        return { 'count' : count, 'data' : data}


    def query_yql(self):
        self._build_url()
        res = UrlFetch(self.encoded_url)
        self.res_data = res.Get()
        print self._parse_response(self.res_data)
        #self.res_quotes = {}
        #root = ElementTree.XML(self.res_data)
        #xmldict = XmlDictConfig(root)
 
        #for quote in xmldict["results"]["quote"]:
        #    self.res_quotes[quote['Symbol']] = quote
        #return self.res_quotes

if __name__ == '__main__':

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
    lis.append("GOOG")
    lis.append("MFST")
    yql_ob = Yql(lis, fields)
    print type(yql_ob)
    yql_ob.query_yql()
