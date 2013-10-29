import urllib.request
import re

symbolfile = open("symbols1.txt")

symbolslist = symbolfile.read()

newsymbolslist = symbolslist.split("\n")

i = 0
while i < len(newsymbolslist):
	url = "https://www.google.com/finance?q=" + newsymbolslist[i] 
	htmlfile = urllib.request.urlopen(url)
	htmltext = htmlfile.read().decode('utf-8')

	regex = '<span id="ref_[^.]*_l" class="unchanged"></span>'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)

	print ("the price of",newsymbolslist[i],"is",price)
	i += 1