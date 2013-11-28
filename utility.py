import urllib2
import httplib

class UrlFetch(object):

    def __init__(self, url, debug=False):
        self.response_data =''
        try:
            response = urllib2.urlopen(url)
            if  debug == True:
                print "Url : ", url
                print "Response : ", response
            self.response_data = response.read()
            response.close()
        except urllib2.URLError, e:
            print "URL Error >> ", str(e.reason)
        except urllib2.HTTPError, e:
            print "HTTP Error >> ", str(e.code)
        except httplib.HTTPException, e:
            print "HTTP Exception"
        except Exception:
            import traceback
            print traceback.format_exc()

    def Get(self):
        return self.response_data