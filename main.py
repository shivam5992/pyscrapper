#download the source code of a website
import urllib.request
import re

urls = ["http://google.com","http://nytimes.com","http://CNN.com"]
i = 0
regex = b'<title>(.+?)</title>'
pattern = re.compile(regex)

while i < len(urls): 
	htmlfile = urllib.request.urlopen(urls[i])
	htmltext = htmlfile.read()
	titles = re.findall(pattern,htmltext)
	print (titles)
	i += 1

