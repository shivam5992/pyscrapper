PyScrapper
==========

Web Scrapping series in python

## Module dependencies:

mechanize, BeautifulSoup (for Python 2.x) | bs4 (for Python 3.x), json, re, requests, urlparse, urllib

`pip install <module_name>`

## Projects

**1. Google Movies:**
	
	Script to scrap google movies, retrieving a list of theaters, 
	their address, movies list, movies genere and showtimes for a given location. 
	 
	This script outputs a JSON file with the response. 

**2. Zomato Top Restaurants:**
	
	Script to scrap the top 25 trending restaurants with their rank, rating, details etc 
	for the mentioned cities on the zomato.com website and creating a seperate json response for each city.


**3. Finance and Stock:**
	
	Scrapping the last closing price for all the quotes from various sites like google, yahoo, bloomberg etc

**4. Live Weather:**

	Scrap the weather details for morning, afternoon and night time for a particular website.

**5. Daily Horoscope:**
	
	Scrapping the daily horoscope details for each sign and creating the output as text files. 
	Multiple websites are scrapped to get the details.

**6. Train Details:**

	Scrap the details of train from irctc by inputting train number.

**7. Website Top Keywords:** 
	
	Create a list of most occured words in a website.
	Also counts thier frequency.

**8. News Scrapping:**

	Scrap the news from various news sources.

**9. Alexa Top Websites:**
	
	Get the list of top 25 websites of a country.

**10. Movie Details:**

	Get the movie details from IMDB and RottenTomatoes.

**11. US President State of Union Speech:**
	
	Scrap the speech transcripts of all Us Presidents from 1700 to Present.

## Spider Algorithm

Spider algorithm is a typical web scrapping technique to fetch all urls (etc) of a webpage. By all means, 
even those urls which are not part of the requested page. It fetches all urls of current urls as well.
Implemented using two ways, one normal and second using mechanize.