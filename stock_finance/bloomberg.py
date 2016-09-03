'''
Scrapping from bloomberg, parsing json response
'''
import json
import urllib

url = "http://www.bloomberg.com/markets/watchlist/recent-ticker/AAPL:US"
htmlfile = urllib.urlopen(url)
data = json.load(htmlfile)
print "Last Closing price of AAPL today is (bloomberg):",data["last_price"]
