import re
from BeautifulSoup import BeautifulSoup
import urllib
from pprint import pprint
import json

class zomato_top_restaurants:

	def __init__(self,city):
		self.city = city
		url = "http://www.zomato.com/" + city + "/top-restaurants"
		htmltext = urllib.urlopen(url)
		self.soup = BeautifulSoup(htmltext)

	def scrap(self):
		soup = self.soup
		resp = []
		print soup.title.string
		for box in soup.findAll("div",attrs={"class": "top-res-box-details"}):
			rest_details = {}
			rest_details['restaurant_name'] = box.span.string 
			rest_details['cuisine'] = re.sub('[^a-zA-Z0-9\n,]', ' ', str(box.find(attrs={"class": "top-res-box-cuisine" }).string))
			rest_details['location'] =  box.find("a",attrs={"class" : "cblack" }).string.strip()
			rest_details['rating'] = box.find("div",attrs={"class" : re.compile("rating-for") }).string.strip()
			resp.append(rest_details)
		return resp

if __name__ == '__main__':
	cities = open("cities.txt").read().split(",")
	for city in cities:
		city = city.lower().replace(" ","")
		if city == "riodejaneiro":
			city = "rio"
		elif city == "delhincr":
			city = "ncr"
		elif city == "metromanila":
			city = "manila"
		obj = zomato_top_restaurants(city)
		resp = obj.scrap()
		d = json.dumps(resp)
		f = open(city+".json","w")
		print >> f, d
		f.close()
		print pprint(resp)