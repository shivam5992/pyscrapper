'''
Reading symbols from file, Scrapping from bloomberg's chart (network response) for day stock price, writing it to a file in new folder
'''

import json
import urllib

symbolslist = open("symbols_less.txt").read()
symbolslist = symbolslist.split("\n")
for symbol in symbolslist:
	myfile = open("daily_prices/" + symbol + ".txt", "w+")
	myfile.close()

	htmltext = urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/" + symbol + ":US")
	data = json.load(htmltext)
	datapoints = data['data_values']
	
	myfile = open("daily_prices/" + symbol + ".txt","a")
	for point in datapoints:
		myfile.write(str(symbol + "," + str(point[0]) + "," + str(point[1]) + "\n"))
	myfile.close()
