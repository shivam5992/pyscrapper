import urllib.request
import re

symbolslist = ["aapl","spy","goog","nflx"]
i = 0
while i < len(symbolslist):
	url = "http://in.finance.yahoo.com/q?s=" + symbolslist[i] 
	htmlfile = urllib.request.urlopen(url)
	htmltext = htmlfile.read().decode('utf-8')

	regex = '<span id="yfs_l84_'+ symbolslist[i] + '">(.+?)</span>'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)

	print ("the price of",symbolslist[i],"is",price)
	i += 1