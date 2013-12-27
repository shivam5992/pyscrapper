'''
Implementation of spider algorithm, it fetches ALL the urls and links of a website.
'''

import urlparse
import urllib
from BeautifulSoup import BeautifulSoup 

url = "http://www.shivambansal.com"
urls = [url] #stack of urls to scrape
visited = [url] #historic record of urls

while len(urls):
	try:
		htmltext = urllib.urlopen(urls[0]).read()
	except:
		# do nothing
		i = 1

	soup = BeautifulSoup(htmltext)
	urls.pop(0)
	#print len(urls)

	#normalised
	for tag in soup.findAll('a',href=True):
		tag['href'] = urlparse.urljoin(url,tag['href'])
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])

for i,j in enumerate(visited):
	print visited[i]