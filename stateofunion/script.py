import json

from BeautifulSoup import BeautifulSoup
from mechanize import Browser

br = Browser()
br.open("http://stateoftheunion.onetwothree.net/texts/index.html")

urllist = []

print "Fetching urllist ..."
count = 0
for link in br.links():
	count += 1
	context = link.text.split(",")
	urllist.append(link.base_url.replace("index.html", "") + link.url)
	print "Fetched link", count

for url in urllist[5:-2]:
	br.open(url)
	soup = BeautifulSoup(br.response().read())
	speech = ""
	for p in soup.findAll("p"):
		speech += p.text
	name = soup.find("h2").text
	date = soup.find("h3").text
	resp = {
	'name': name,
	'date': date,
	'speech': speech
	}
	outfile = open("ScrapedData/"+name+date+".json","w")
	json.dump(resp, outfile, indent = 4)
	print "Creating response for", name, date
