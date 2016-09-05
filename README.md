PyScrapper
==========

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](http://www.repostatus.org/badges/latest/wip.svg)](https://github.com/ivannieto/PyScrapper) [![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?maxAge=2592000)](https://github.com/ivannieto/PyScrapper/blob/master/LICENSE) [![GitHub forks](https://img.shields.io/github/forks/badges/shields.svg?style=social&label=Fork&maxAge=2592000)](https://github.com/ivannieto/PyScrapper/fork) [![Twitter URL](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&maxAge=2592000)](https://twitter.com/intent/tweet?text=Wanna%20learn%20to%20scrap%20websites?%20Check%20PyScrapper%20&url=https%3A%2F%2Fgithub.com%2Fivannieto%2FPyScrapper%2F) [![Twitter Follow](https://img.shields.io/twitter/follow/shields_io.svg?style=social&label=Follow&maxAge=2592000)](https://twitter.com/intent/follow?original_referer=https://twitter.com/follow-button&screen_name=IvanNietoS)



##### WIP DISCLAIMER

Some of the projects inside this repo are broken due to updates on the websites used, 
so they are being reworked to be fully functional. Contributions are welcome. Just fork the repo and pull request your updates.

### Web Scrapping series in python.

Forked and mantained by Ivan Nieto <ivan.n.s@tuta.io> 

Original work by Shivam Bansal <shivam5992@gmail.com>


## Module dependencies:

mechanize, BeautifulSoup (for Python 2.x) | bs4 (for Python 3.x), json, re, requests, urlparse, urllib

        pip install <module_name>

# Projects

#### Google Movies

        Script to scrap google movies, retrieving a list of theaters, their address, movies list, 
        movies genere and showtimes for a given location. 
             
        This script outputs a JSON file with the response. 

#### Zomato Top Restaurants
	
        Script to scrap the top 25 trending restaurants with their rank, rating, details... 
        for the mentioned cities on the zomato.com website.
        
        It outputs a separate JSON response for each city.


#### Finance and Stock
	
        Scrapping the last closing price for all the quotes from various sites 
        like google, yahoo, bloomberg etc

#### Live Weather

        Scrap the weather details for morning, afternoon and night time for a particular website.

#### Daily Horoscope
	
        Scrapping the daily horoscope details for each sign and creating the output as text files. 
        Multiple websites are scrapped to get the details.

#### Train Details

        Scrap the details of train from irctc by inputting train number.

#### Website Top Keywords
	
        Create a list of most occured words in a website.
        Also counts thier frequency.

#### News Scrapping

        Scrap the news from various news sources.

#### Alexa Top Websites
	
        Get the list of top 25 websites of a country.

#### Movie Details

        Get the movie details from IMDB and RottenTomatoes.

#### US President State of Union Speech
	
        Scrap the speech transcripts of all Us Presidents from 1700 to Present.

#### Spider Algorithm

        Spider algorithm is a typical web scrapping technique to fetch all urls (etc) of a webpage.
        By all means, even those urls which are not part of the requested page. 
        It fetches all urls of current urls as well.
        Implemented using two ways, one normal and second using mechanize.


## Rework ToDo

- [x] Google Movies
- [ ] Zomato Top Restaurants
- [ ] Finance and Stock
- [ ] Live Weather
- [ ] Daily Horoscope
- [ ] Train Details
- [ ] Website Top Keywords
- [x] News Scrapping
- [ ] Alexa Top Websites
- [ ] Movie Details
- [ ] US President State of Union Speech
- [ ] Spider Algorithm