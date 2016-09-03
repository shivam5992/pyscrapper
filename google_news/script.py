import urllib
from pprint import pprint

from BeautifulSoup import BeautifulSoup

'''
Python class to scrap latest news from google news
'''
class google_news:
	def __init__(self):
		url = "https://news.google.com/"
		htmltext = urllib.urlopen(url).read()
		self.soup = BeautifulSoup(htmltext)
		
	def scrap(self):
		soup = self.soup
		resp = []	
		for tag in soup.findAll("div",attrs={"class":"blended-wrapper esc-wrapper"}):
			dic = {}
			td = tag.table.tr.find("td",attrs={"class":"esc-layout-article-cell"})
			dic['title'] = td.find("span",attrs={"class":"titletext"}).getText()
			dic['source'] = td.find("span",attrs={"class":"al-attribution-source"}).string
			dic['timestamp'] = td.find("span",attrs={"class":"al-attribution-timestamp"}).string.replace("&lrm;","")
			dic['description'] = tag.find("div",attrs={"class":"esc-lead-snippet-wrapper"}).getText()
			resp.append(dic)
		return resp

if __name__ == '__main__':
	o = google_news()
	response = o.scrap()
	print pprint(response)