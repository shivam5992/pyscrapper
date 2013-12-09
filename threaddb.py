from threading import Thread
import urllib
import re
import pymysql

gmap = {}

'''
Create a database in mysql first, named 'stock_data' containing database
'tutorial' with 2 fields "symbol" and "last".
'''

'''
Function which is called by thread
'''
def th(ur):
	base = "http://finance.yahoo.com/q?s="+ur
	htmltext = urllib.urlopen(base).read()
	regex = '<span id="yfs_l84_' + ur.lower() + '">(.+?)</span>'
	pattern = re.compile(regex)
	results = re.findall(pattern,htmltext)
	print "the price of " + str(ur) +  " is " + str(results[0])
	# add results in a distionary
	try:
		gmap[ur] = results[0]
	except:
		print "Got an error"

'''
Start reading symbols from a file
'''
symbolslist = open("symbols1.txt").read().split("\n")
threadlist = []

# call a thread with an argument
for u in symbolslist:
	t = Thread(target = th, args = (u,))
	t.start()
	threadlist.append(t)

for b in threadlist:
	b.join()

'''
Add dictionarie to mysql database
'''
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='stock_data')

for key in gmap.keys():
	x = conn.cursor()
	query = "INSERT INTO tutorial (symbol,last) values("
	query = query + "'" + key + "'," + gmap[key]+")"
	x.execute(query)
	row = x.fetchall()