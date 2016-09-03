'''
Implementation of spider algorithm, fetches ALL the urls and links of a website.
'''

import urllib
import urlparse

from BeautifulSoup import BeautifulSoup

url = "http://www.nytimes.com"
urls = [url] # Stack of urls to scrape
visited = [url] # Historic record of urls

while len(urls):
	try:
		htmltext = urllib.urlopen(urls[0]).read()
	except:
		i = 1

	soup = BeautifulSoup(htmltext)
	urls.pop(0)
	
	for tag in soup.findAll('a',href=True):
		tag['href'] = urlparse.urljoin(url,tag['href'])
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])

for i,j in enumerate(visited):
	print visited[i]

