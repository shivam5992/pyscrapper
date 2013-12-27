'''
Python Class to scrap google movies show times according to location.
This script outputs list of Theaters, their address, movies list, movies genere etc.

'''

from BeautifulSoup import BeautifulSoup
import re,urllib
from pprint import pprint
import json

'''
Python class to scrap google-movies webpage.
webpage : www.google.com/movies
'''
class google_movie_scrapper:
	
	'''
	Constructor for google_movie_scrapper class
	'''

	def __init__(self,city):
		self.city = city
		if city is "":
			url = "http://www.google.com/movies"
		else:
			url = "http://www.google.com/movies?near=" + city
		htmltext = urllib.urlopen(url).read()
		self.soup = BeautifulSoup(htmltext)

	'''
	Function which scraps the movies, theaters, address, generes and movie times and building the response as list of dictionaries.
	'''
	def scrap(self):
		soup_object = self.soup
		output = []
		for theater in soup_object.findAll("div", {"class":re.compile("theater")}):
			resp = {}
			resp['theater'] = theater.a.string
			resp['address'] = theater.find("div", {"class":re.compile("info")}).contents[0]
			movie_list = []
			for movie in theater.find("div", {"class":re.compile("showtimes")}).findAll("div", {"class":re.compile("movie")}):
				movie_dict = {}
				movie_dict['movie_name'] = movie.a.string 
				movie_dict['genere'] = re.sub('[^a-zA-Z/\n\.]', ' ', str(movie.span.text)).strip().replace("                 "," - ").replace("         Trailer","")
				showtimeslist = []
				for time in movie.findAll("div",{"class":re.compile("times")})[0].findAll("span"):
					time_string = re.sub('[^a-z0-9:\n\.]', ' ', str(time.text)).replace("8206","").replace("nbsp","").strip()
					if time_string is not "":
						showtimeslist.append(time_string)
				movie_dict['showtimes'] = showtimeslist
				movie_list.append(movie_dict)

				resp['movieslist'] = movie_list
			output.append(resp)
		return output

'''
Printing the output.
'''
if __name__ == '__main__':
	
	'''
	Set 'city' parameter as valid name of the location
	it is optional, if not set then default location is used by this script
	'''
	city = "delhi"
	
	obj = google_movie_scrapper(city)
	output = obj.scrap()
	
	'''
	Printing the list
	'''
	print pprint(output)
	
	'''
	Printing using response
	'''
	print "*"*35
	print "Showing the response for:", obj.city
	print "*"*35
	print ""

	for i,j in enumerate(output):
		print "Following are the movie details for >>", output[i]['theater'], "<< located at '", output[i]['address'], "'" 
		for x,y in enumerate(output[i]['movieslist']):
			print "Showtimes for", y['movie_name'], "are", y['showtimes'], "Genere is:", y['genere']
		print "-"*150


'''
RESPONSE Format:
		
	[   {
		'theater': name of the theater
		'address': address of the theater
		'movieslist':
				'movie_name': name of the movie
				'showtimes': [1,2,3,4,5,6,7,8]
				'genere': genere of the movies

				'movie_name': name of the movie
				'showtimes': [1,2,3,4,5,6,7,8]
				'genere': genere of the movies

				'movie_name': name of the movie
				'showtimes': [1,2,3,4,5,6,7,8]
				'genere': genere of the movies
		},

		{
		'theater': name of the theater
		'address': address of the theater
		'movieslist':
				'movie_name': name of the movie
				'showtimes': [1,2,3,4,5,6,7,8]
				'genere': genere of the movies

				'movie_name': name of the movie
				'showtimes': [1,2,3,4,5,6,7,8]
				'genere': genere of the movies

				'movie_name': name of the movie
				'showtimes': [1,2,3,4,5,6,7,8]
				'genere': genere of the movies
		},

		{
		'theater': name of the theater
		'address': address of the theater
		'movieslist':
				'movie_name': name of the movie
				'showtimes': [1,2,3,4,5,6,7,8]
				'genere': genere of the movies

				'movie_name': name of the movie
				'showtimes': [1,2,3,4,5,6,7,8]
				'genere': genere of the movies

				'movie_name': name of the movie
				'showtimes': [1,2,3,4,5,6,7,8]
				'genere': genere of the movies
		}
	]
'''
	