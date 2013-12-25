from BeautifulSoup import BeautifulSoup
import re,urllib

class google_movie_scrapper:
	
	def __init__(self):
		url = "http://www.google.com/movies?near=noida"
		htmltext = urllib.urlopen(url).read()
		self.soup = BeautifulSoup(htmltext)

	def scrap(self):
		soup_object = self.soup
		resp = []
		for theater in soup_object.findAll("div", {"class":re.compile("theater")}):
			print "Theater:", theater.a.string
			print "Theater Info:", theater.find("div", {"class":re.compile("info")}).contents[0]
			for movie in theater.find("div", {"class":re.compile("showtimes")}).findAll("div", {"class":re.compile("movie")}):
				print "Movie:", movie.a.string
				print "Movie genere", re.sub('[^a-zA-Z/\n\.]', ' ', str(movie.span.text)).strip().replace("                 "," - ").replace("         Trailer","")
				print "Movie Times:"
				for time in movie.findAll("div",{"class":re.compile("times")})[0].findAll("span"):
					time_string = re.sub('[^a-z0-9:\n\.]', ' ', str(time.text)).replace("8206","").replace("nbsp","").strip()
					if time_string is not "":
						print time_string

			print "***"

obj = google_movie_scrapper()
obj.scrap()

'''

Dictionary:

RESP_for_Noida:
	
	Theater: 	
		Name: abc
		Address: xyz
		MoviesList:
			Moive: 
				Name: aaa
				ShowTimes: [a,a,a,a,,a,a,a]
				genere: bbb
			
			Moive: 
				Name: aaa
				ShowTimes: [a,a,a,a,,a,a,a]
				genere: bbb

			Moive: 
				Name: aaa
				ShowTimes: [a,a,a,a,,a,a,a]
				genere: bbb

	Theater2:
	Theater3: 	
	
'''
	