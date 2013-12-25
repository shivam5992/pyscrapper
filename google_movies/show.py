from BeautifulSoup import BeautifulSoup
import re,urllib
from pprint import pprint
import json


class google_movie_scrapper:
	
	def __init__(self):
		url = "http://www.google.com/movies?near=noida"
		htmltext = urllib.urlopen(url).read()
		self.soup = BeautifulSoup(htmltext)

	def scrap(self):
		soup_object = self.soup
		output = []
		for theater in soup_object.findAll("div", {"class":re.compile("theater")}):
			resp = {}
			resp['theater'] = theater.a.string
			resp['info'] = theater.find("div", {"class":re.compile("info")}).contents[0]
			#print "Theater:", theater.a.string
			#print "Theater Info:", theater.find("div", {"class":re.compile("info")}).contents[0]
			movie_list = []
			for movie in theater.find("div", {"class":re.compile("showtimes")}).findAll("div", {"class":re.compile("movie")}):
				movie_dict = {}
				movie_dict['movie_name'] = movie.a.string 
				movie_dict['movie_genere'] = re.sub('[^a-zA-Z/\n\.]', ' ', str(movie.span.text)).strip().replace("                 "," - ").replace("         Trailer","")
				#print "Movie:", movie.a.string
				#print "Movie genere", re.sub('[^a-zA-Z/\n\.]', ' ', str(movie.span.text)).strip().replace("                 "," - ").replace("         Trailer","")
				#print "Movie Times:"
				showtimeslist = []
				for time in movie.findAll("div",{"class":re.compile("times")})[0].findAll("span"):
					time_string = re.sub('[^a-z0-9:\n\.]', ' ', str(time.text)).replace("8206","").replace("nbsp","").strip()
					if time_string is not "":
						showtimeslist.append(time_string)
						#print time_string
				movie_dict['showtimes'] = showtimeslist
				movie_list.append(movie_dict)

				resp['movie'] = movie_list
			output.append(resp)
		return output

if __name__ == '__main__':
	obj = google_movie_scrapper()
	output = obj.scrap()
	d = json.dumps(output)
	f = open('respnse.json', 'w')
	print >> f, d
	f.close()
	#print pprint(output)


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
	