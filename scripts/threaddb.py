'''
Use of threads and mysql database in scrapping 

Create a database in mysql named 'stock_data' containing table
'tutorial' with 2 fields 'symbol' and 'last'.
'''

from threading import Thread
import urllib
import re
import pymysql

gmap = {}


def thread_func(ur):
	base = "http://finance.yahoo.com/q?s="+ur
	htmltext = urllib.urlopen(base).read()
	regex = '<span id="yfs_l84_' + ur.lower() + '">(.+?)</span>'
	pattern = re.compile(regex)
	results = re.findall(pattern,htmltext)
	print "the price of " + str(ur) +  " is " + str(results[0])
	try:
		gmap[ur] = results[0]
	except:
		print "Got an error"

symbolslist = open("less_symbols.txt").read().split("\n")
threadlist = []

'''
Thread with an argument
'''
for u in symbolslist:
	t = Thread(target = thread_func, args = (u,))
	t.start()
	threadlist.append(t)

for b in threadlist:
	b.join()

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='stock_data')

for key in gmap.keys():
	x = conn.cursor()
	query = "INSERT INTO tutorial (symbol,last) values("
	query = query + "'" + key + "'," + gmap[key]+")"
	x.execute(query)
	row = x.fetchall()