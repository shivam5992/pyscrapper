'''
Scrapping last price of various companies from yahoo finance
input taken from a file
'''

import re
import urllib

symbolfile = open("symbols_less.txt")
symbolslist = symbolfile.read()
newsymbolslist = symbolslist.split("\n")

for i,j in enumerate(newsymbolslist):
	url = "http://in.finance.yahoo.com/q?s=" + newsymbolslist[i] 
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read().decode('utf-8')

	regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)

	print "the price of", newsymbolslist[i],"is", price[0]