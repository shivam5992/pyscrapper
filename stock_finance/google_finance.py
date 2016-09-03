
'''
Fetching stock value from google finance website using network response!!
'''

import urllib

url = "https://www.google.com/finance/getprices?q=AAPL&x=NASD&i=120&p=25m&f=c&df=cpct&auto=1&ts=1383288707413&ei=cJ9yUujREYnHkgWoIw"
htmlfile = urllib.urlopen(url)
htmltext = htmlfile.read().decode('utf-8').split()
print "Last closing price for AAPL today is:",htmltext[len(htmltext)-1]