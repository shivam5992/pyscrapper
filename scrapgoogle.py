import urllib2
import re
# fetching stock value from google finance website!!
url = "https://www.google.com/finance/getprices?q=AAPL&x=NASD&i=120&p=25m&f=c&df=cpct&auto=1&ts=1383288707413&ei=cJ9yUujREYnHkgWoIw"
htmlfile = urllib2.urlopen(url)
htmltext = htmlfile.read().decode('utf-8').split()
print (htmltext[len(htmltext)-1])