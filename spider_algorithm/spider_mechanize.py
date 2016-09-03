'''
Spider Algorithm using mechanize
'''

import urlparse

import mechanize

url = "http://www.shivambansal.com"
br = mechanize.Browser()

urls = [url]
visited = [url]
while len(urls):
	try: 
		br.open(urls[0])
		urls.pop(0)
		for link in br.links():
			newurl = urlparse.urljoin(link.base_url,link.url)
			newurl =  "http://" + urlparse.urlparse(newurl).hostname + urlparse.urlparse(newurl).path
			if newurl not in visited and urlparse.urlparse(url).hostname in newurl:
				urls.append(newurl)
				visited.append(newurl)
				print newurl
	except:
		print "error"
		urls.pop(0)