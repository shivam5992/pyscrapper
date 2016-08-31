#! /usr/bin/python3

'''
Python Class to scrap google movies show times according to location.
This script outputs list of Theaters, their address, movies list, movies genere etc.
'''
import bs4
from bs4 import BeautifulSoup
import re
import requests
from pprint import pprint


# Python class to scrap google-movies webpage.
# webpage : www.google.com/movies

class google_movie_scrapper:
    
    # Constructor for google_movie_scrapper class
    def __init__(self, city):
        self.city = city
        if city is "":
            url = "http://www.google.com/movies"
        else:
            url = "http://www.google.com/movies?near=" + city
        r = requests.get(url)
        textohtml = r.text
        self.soup = BeautifulSoup(textohtml, "lxml")

    # Function which scraps the movies, theaters, address, generes and movie times and building the response as list of dictionaries.
    def scrap(self):
        soup_object = self.soup
        output = []

        for theater in soup_object.findAll("div", {"class": re.compile("theater")}):
            resp = {}
            resp['theater'] = theater.find("a").contents[0]
            resp['address'] = theater.find("div", {"class": re.compile("info")}).contents[0]

            movie_list = []
            for movie in theater.find("div", {"class": re.compile("showtimes")}).findAll("div", {
                "class": re.compile("movie")}):
                dict = {}
                dict['movie_name'] = movie.a.string
                dict['genere'] = movie.find("span", {"class": re.compile("info")}).contents[0]

                show_timings_list = []
                for time in movie.findAll("div", {"class": re.compile("times")})[0].findAll("span"):
                    time_string = re.sub('[^a-z0-9:\n\.]', ' ', str(time.text)).replace("8206", "").replace("nbsp",
                                                                                                            "").strip()
                    if time_string is not "":
                        show_timings_list.append(time_string)

                dict['showtimes'] = show_timings_list
                movie_list.append(dict)
                resp['movieslist'] = movie_list
            output.append(resp)
        return output


# Printing the output
if __name__ == '__main__':

    # Setting 'city' param as valid name of location is optional.
    # If not set then default location is used by this script.

    city = "Dehli"

    obj = google_movie_scrapper(city)
    output = obj.scrap()

    # Printint the list
    print(pprint(output))

    # Printing using response
    print("\n", "*" * 35)
    print("Response for: ", obj.city)
    print("*" * 35)
    print("")

    for i, j in enumerate(output):
        print("Movies and showtimes for: \n\n", output[i]['theater'], "\n", output[i]['address'], "\n")
        for x, y in enumerate(output[i]['movieslist']):
            print(y['movie_name'], ": ", y['showtimes'], y['genere'])
        print("-" * 100)





    # RESPONSE Format:

    #
    # [
    # [...]
    #     {'address': 'Shree Rang Palace - Zadeshwar Road, Bharuch, India - 02642 228 '
    #                 '844',
    #      'movieslist': [{'genere': '2hr 31min - '
    #                                'Action/Adventure/Romance/Suspense/Thriller - '
    #                                'Hindi',
    #                      'movie_name': 'A Flying Jatt',
    #                      'showtimes': ['9:10',
    #                                    '10:00am',
    #                                    '1:00',
    #                                    '3:05',
    #                                    '4:05',
    #                                    '6:10',
    #                                    '10:15pm']},
    #                     {'genere': '1hr 39min - Action/Adventure/Suspense/Thriller - '
    #                                'English - ',
    #                      'movie_name': 'Mechanic: Resurrection',
    #                      'showtimes': ['9:35am', '5:20', '10:30pm']},
    #                     {'genere': '2hr 28min - Drama/Suspense/Thriller - Hindi',
    #                      'movie_name': 'Rustom',
    #                      'showtimes': ['11:45am', '7:30pm']},
    #                     {'genere': '2hr 6min - Comedy/Romance - Hindi',
    #                      'movie_name': 'Happy Bhaag Jayegi',
    #                      'showtimes': ['2:45', '7:11pm']},
    #                     {'genere': '2hr 20min - Drama - Telugu',
    #                      'movie_name': 'Janatha Garage',
    #                      'showtimes': ['9:16pm']},
    #                     {'genere': '2hr 13min - Comedy/Drama - Gujarati',
    #                      'movie_name': 'Navri Bazar',
    #                      'showtimes': ['12:15pm']}],
    #      'theater': 'INOX Bharuch'},
    # [...]
    #
    # ]



    # [...]
    # ----------------------------------------------------------------------------------------------------
    # Movies and showtimes for:
    #
    #  INOX Bharuch
    #  Shree Rang Palace - Zadeshwar Road, Bharuch, India - 02642 228 844
    #
    # A Flying Jatt :  ['9:10', '10:00am', '1:00', '3:05', '4:05', '6:10', '10:15pm'] 2hr 31min - Action/Adventure/Romance/Suspense/Thriller - Hindi
    # Mechanic: Resurrection :  ['9:35am', '5:20', '10:30pm'] 1hr 39min - Action/Adventure/Suspense/Thriller - English -
    # Rustom :  ['11:45am', '7:30pm'] 2hr 28min - Drama/Suspense/Thriller - Hindi
    # Happy Bhaag Jayegi :  ['2:45', '7:11pm'] 2hr 6min - Comedy/Romance - Hindi
    # Janatha Garage :  ['9:16pm'] 2hr 20min - Drama - Telugu
    # Navri Bazar :  ['12:15pm'] 2hr 13min - Comedy/Drama - Gujarati
    # ----------------------------------------------------------------------------------------------------
    # [...]
