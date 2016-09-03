'''
Python class to scrap weather details for a city from the website
www.weather-forecast.com

Uses Mechanize to submit the city name in the form
'''

from pprint import pprint

import mechanize
from BeautifulSoup import BeautifulSoup


class weather_scrap:

	def __init__(self,city):
		self.city = city
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.set_handle_refresh(False)
		br.addheaders= [("User-Agent","Mozilla/5.0")]
		br.open("http://www.weather-forecast.com/")
		br.select_form(nr = 0)
		br.form['query'] = city
		br.submit()

		html = br.response().read()
		self.soup = BeautifulSoup(html)
	
	def scrap(self):	
		soup = self.soup
		report = {}
		
		date_time_div = soup.find("img",attrs={"class":"print_only"})
		report['date'] = str(date_time_div.parent.p.string.split(":")[1].strip().replace('\n', '').replace('           ',' '))
		report['city'] = city

		table = soup.find("table",attrs={"class":"forecasts"})
		maxT = soup.find(text="Max.&nbsp;Temp").findNext("td")
		minT = soup.find(text="Min.&nbsp;Temp").findNext("td")

		morning = {}
		afternoon = {}
		night = {}
		weather = [morning,afternoon,night]

		for i,j in enumerate(weather):
			weather[i]['summary'] = str(table.findAll("td",attrs={"class":"med wphrase"})[i].text)
			weather[i]['freezing_level'] = str(soup.findAll("span",attrs={"class":"height"})[0].text) + "m"
			
			rain = str(soup.findAll("span",attrs={"class":"rain"})[i].text)
			if rain == "-":
				weather[i]['rain'] = "Not Available"
			else:
				weather[i]['rain'] = rain + " IN"

			snow = str(soup.findAll("span",attrs={"class":"snow"})[i].text)
			if snow == "-":
				weather[i]['snow'] = "Not Available"
			else:
				weather[i]['snow'] = snow + " IN"
			
			sunrise = str(soup.findAll("td",attrs={"class":"sunrise"})[0].text)
			sunset = str(soup.findAll("td",attrs={"class":"sunset"})[0].text)
			if sunset == "-":
				sunset = "Not Available"
			if sunrise == "-":
				sunrise = "Not Available"
			weather[i]['sunset'] = sunset
			weather[i]['sunrise'] = sunrise


			if i == 0:
				weather[i]['max_temp'] = str(maxT.text) + " C"
				weather[i]['min_temp'] = str(minT.text) + " C"
			if i == 1:
				weather[i]['max_temp'] = str(maxT.findNext("td").text) + " C"
				weather[i]['min_temp'] = str(minT.findNext("td").text) + " C"
			if i == 2:
				weather[i]['max_temp'] = str(maxT.findNext("td").findNext("td").text) + " C"
				weather[i]['min_temp'] = str(minT.findNext("td").findNext("td").text) + " C"

		report['weather_morning'] = weather[0]
		report['weather_afternoon'] = weather[1]
		report['weather_night'] = weather[2]

		return report

'''
Change city name to get weather details for different cities.
Enter a valid city name.
'''
if __name__ == '__main__':
	city = "new york"
	obj = weather_scrap(city)
	response = obj.scrap()
	print pprint(response)




