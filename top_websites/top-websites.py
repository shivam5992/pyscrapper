'''
Python class to get top 25 websites of a country from alexia.com
'''

import mechanize
from BeautifulSoup import BeautifulSoup
import re

class top_websites:
	def scrap(self,city):
		url = "http://www.alexa.com/topsites/countries"
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.set_handle_refresh(False)
		br.addheaders= [("User-Agent","Mozilla/5.0")]
		br.open(url)

		countries = [''.join(link.text).lower() for link in br.links()]

		if city.lower() in countries:
			for link in br.links():
				if link.text.lower() == city.lower():
					br.follow_link(link)
					html = br.response().read()
					soup = BeautifulSoup(html)
					print soup.title.string.replace("Alexa - ","")
					print "*"*200
					print ""
					for i,li in enumerate(soup.findAll('li',attrs={"class":"site-listing"})):
						print i+1,":",li.a.string
						first =  li.find('div',attrs={"class":"description"})
						print first.text.replace("...More","-").encode("utf-8").replace("&nbsp;","No Description Available ")
						print " "
		else:
			print "please enter a valid country name"

if __name__ == '__main__':
	city = "india"
	o = top_websites()
	o.scrap(city)

	