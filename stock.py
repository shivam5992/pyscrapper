import urllib.request
import re

symbolslist = ["AAPL","SPY","GOOG","NFLX"]
i = 0
while i < len(symbolslist):
	url = "http://in.finance.yahoo.com/q?s=" + symbolslist[i] 
	htmlfile = urllib.request.urlopen(url)
	htmltext = htmlfile.read()

	symbol = bytes(symbolslist[i], 'Utf-8')

	regex = b'<span id="yfs_l84_'+ symbol + b'">(.+?)</span>'
	print(regex)
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)

	print ("the price of",symbolslist[i],"is",str(price))
	i += 1