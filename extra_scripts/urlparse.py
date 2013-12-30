'''
Extracting all the links of a webpage using urlparse
'''

import urllib
from BeautifulSoup import BeautifulSoup
import urlparse

htmltext = urllib.urlopen("http://www.nytimes.com/").read()
soup = BeautifulSoup(htmltext)

for tag in soup.findAll('a',href = True):
	raw = tag['href']
	b1 = urlparse.urlparse(tag['href']).hostname
	b2 = urlparse.urlparse(tag['href']).path
	print "http://" + str(b1) + str(b2)