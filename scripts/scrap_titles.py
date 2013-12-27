import urllib
import re
import json

'''
1. Scrapping the website titles using regex
'''
urls = ["http://google.com","http://nytimes.com","http://CNN.com","http://www.linkedin.com/"]
regex = b'<title>(.+?)</title>'
pattern = re.compile(regex)

print "Scraped Titles are: "
for i,j in enumerate(urls): 
	htmlfile = urllib.urlopen(urls[i])
	htmltext = htmlfile.read()
	titles = re.findall(pattern,htmltext)
	print (titles[0])