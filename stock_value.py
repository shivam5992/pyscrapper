import urllib2
import re

symbolfile = open("symbols1.txt")

symbolslist = symbolfile.read()

newsymbolslist = symbolslist.split("\n")

i = 0
while i < len(newsymbolslist):
	url = "http://in.finance.yahoo.com/q?s=" + newsymbolslist[i] 
	htmlfile = urllib2.urlopen(url)
	htmltext = htmlfile.read().decode('utf-8')

	regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)

	print ("the price of",newsymbolslist[i],"is",price)
	i += 1


#comments section
