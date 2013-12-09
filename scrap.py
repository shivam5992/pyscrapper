import urllib
import re
import json

'''
1. Scrapping the website titles
'''

# List of URLS where titles will be scraped
urls = ["http://google.com","http://nytimes.com","http://CNN.com","http://www.linkedin.com/"]
# Using RE to get titles
regex = b'<title>(.+?)</title>'
pattern = re.compile(regex)

print "Scraped Titles are: "
for i,j in enumerate(urls): 
	htmlfile = urllib.urlopen(urls[i])
	htmltext = htmlfile.read()
	titles = re.findall(pattern,htmltext)
	print (titles[0])



'''
2. Fetching stock value from google finance website using network response!!
'''

url = "https://www.google.com/finance/getprices?q=AAPL&x=NASD&i=120&p=25m&f=c&df=cpct&auto=1&ts=1383288707413&ei=cJ9yUujREYnHkgWoIw"
htmlfile = urllib.urlopen(url)
htmltext = htmlfile.read().decode('utf-8').split()
print ""
print "Last closing price for AAPL today is: ",htmltext[len(htmltext)-1]



'''
3. Scrapping last price of various companies, input taken from a file
'''

symbolfile = open("symbols1.txt")
symbolslist = symbolfile.read()
newsymbolslist = symbolslist.split("\n")

print ""
for i,j in enumerate(newsymbolslist):
	url = "http://in.finance.yahoo.com/q?s=" + newsymbolslist[i] 
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read().decode('utf-8')

	regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)

	print "the price of", newsymbolslist[i],"is", price[0]

'''
4. Scrapping from bloomberg, parsing json response
'''

url = "http://www.bloomberg.com/markets/watchlist/recent-ticker/AAPL:US"
htmlfile = urllib.urlopen(url)
data = json.load(htmlfile)
print "Last Closing price of AAPL today is (bloomberg):",data["last_price"]
