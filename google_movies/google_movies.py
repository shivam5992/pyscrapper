#!/usr/bin/python
# encoding=utf-8

'''
Python Class to scrap google movies show times according to a given location.
This script outputs list of theaters, their address, movies list, movies genere and showtimes.
'''

from pprint import pprint
import re
from bs4 import BeautifulSoup
import json
import requests

outputjson = open("out/response.json", "w")

# Python class to scrap Google Movies webpage.
# webpage : www.google.com/movies

class google_movie_scrapper:
    # Constructor for google_movie_scrapper class
    def __init__(self, city):

        self.city = city

        if city is "":
            url = "http://www.google.com/movies"
        else:
            url = "http://www.google.com/movies?near=" + city

        req = requests.get(url)
        textohtml = req.text
        self.soup = BeautifulSoup(textohtml, "lxml")

    # Function which scraps the movies, theaters, address, generes and showtimes.
    # Returns a list of dictionaries.
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
    city = "Madrid"

    obj = google_movie_scrapper(city)
    output = obj.scrap()

    # Printing the list
    pprint(output)

    # Writing response to json file prettified
    jsondump = json.dumps(output, indent=4, ensure_ascii=False).encode('utf8')
    outputjson.write(jsondump)

    # Printing STDOUT using response
    print("*" * 35)
    print("Response for: ")
    print(obj.city)
    print("*" * 35)

    for i, j in enumerate(output):
        print("\n")
        print("*" * 35)
        print("\nMovies and showtimes for:")
        print(output[i]['theater'])
        print(output[i]['address'])
        print("\n")

        for x, y in enumerate(output[i]['movieslist']):
            print(y['movie_name'])
            print(y['genere'])
            print(y['showtimes'])
            print("-" * 100)


            # RESPONSE Format:

            # The output list is returned in Unicode codification

            # [
            # [...]
            # [{'address': u'C/ DOCTOR CORTEZO, 6, Madrid, Spain - 913 69 06 69',
            #   'movieslist': [{'genere': u'1hr 37min',
            #                   'movie_name': u'Cuerpo de \xe9lite',
            #                   'showtimes': ['18:20', '22:50']},
            #                  {'genere': u'1hr 46min',
            #                   'movie_name': u'Lejos del mar',
            #                   'showtimes': ['19:40', '21:55']},
            #                  {'genere': u'1hr 36min',
            #                   'movie_name': u'Caf\xe9 society V.O.S.E.',
            #                   'showtimes': ['16:30', '18:30', '20:35', '22:35']},
            #                  {'genere': u'2hr 9min',
            #                   'movie_name': u'Ben-Hur (2016) V.O.S.E.',
            #                   'showtimes': ['17:00', '19:30', '22:00']},
            #                  {'genere': u'1hr 28min',
            #                   'movie_name': u'No respires V.O.S.E.',
            #                   'showtimes': ['16:10', '18:10', '20:10', '22:10']},
            #                  {'genere': u'1hr 50min',
            #                   'movie_name': u'Los visitantes la l\xedan V.O.S.E.',
            #                   'showtimes': ['16:00', '18:15', '20:30', '22:45']},
            #                  {'genere': u'1hr 26min',
            #                   'movie_name': u'Mascotas V.O.S.E.',
            #                   'showtimes': ['16:05', '18:00', '19:55']},
            #                  {'genere': u'1hr 42min',
            #                   'movie_name': u'Kubo y las dos cuerdas m\xe1gicas V.O.S.E.',
            #                   'showtimes': ['16:00', '18:05', '20:15']},
            #                  {'genere': u'1hr 40min',
            #                   'movie_name': u'Star Trek: M\xe1s all\xe1 V.O.S.E.',
            #                   'showtimes': ['19:15', '21:45']},
            #                  {'genere': u'2hr 10min',
            #                   'movie_name': u'Escuadr\xf3n suicida V.O.S.E.',
            #                   'showtimes': ['17:15', '21:50']},
            #                  {'genere': u'1hr 56min',
            #                   'movie_name': u'Cazafantasmas V.O.S.E.',
            #                   'showtimes': ['16:45', '22:20']},
            #                  {'genere': u'1hr 43min',
            #                   'movie_name': u'Peter y el drag\xf3n V.O.S.E.',
            #                   'showtimes': ['16:05']},
            #                  {'genere': u'2hr 0min',
            #                   'movie_name': u'Jason Bourne V.O.S.E.',
            #                   'showtimes': ['20:20']}],
            #   'theater': u'YELMO CINES IDEAL'},
            # [...]
            #
            # ]


            # [...]
            # ***********************************
            # Response for:
            # Madrid
            # ***********************************
            #
            #
            # ***********************************
            #
            # Movies and showtimes for:
            # YELMO CINES IDEAL
            # C/ DOCTOR CORTEZO, 6, Madrid, Spain - 913 69 06 69
            #
            #
            # Cuerpo de élite
            # 1hr 37min
            # ['18:20', '22:50']
            # ----------------------------------------------------------------------------------------------------
            # Lejos del mar
            # 1hr 46min
            # ['19:40', '21:55']
            # ----------------------------------------------------------------------------------------------------
            # Café society V.O.S.E.
            # 1hr 36min
            # ['16:30', '18:30', '20:35', '22:35']
            # ----------------------------------------------------------------------------------------------------
            # Ben-Hur (2016) V.O.S.E.
            # 2hr 9min
            # ['17:00', '19:30', '22:00']
            # ----------------------------------------------------------------------------------------------------
            # No respires V.O.S.E.
            # 1hr 28min
            # ['16:10', '18:10', '20:10', '22:10']
            # ----------------------------------------------------------------------------------------------------
            # Los visitantes la lían V.O.S.E.
            # 1hr 50min
            # ['16:00', '18:15', '20:30', '22:45']
            # ----------------------------------------------------------------------------------------------------
            # Mascotas V.O.S.E.
            # 1hr 26min
            # ['16:05', '18:00', '19:55']
            # ----------------------------------------------------------------------------------------------------
            # Kubo y las dos cuerdas mágicas V.O.S.E.
            # 1hr 42min
            # ['16:00', '18:05', '20:15']
            # ----------------------------------------------------------------------------------------------------
            # Star Trek: Más allá V.O.S.E.
            # 1hr 40min
            # ['19:15', '21:45']
            # ----------------------------------------------------------------------------------------------------
            # Escuadrón suicida V.O.S.E.
            # 2hr 10min
            # ['17:15', '21:50']
            # ----------------------------------------------------------------------------------------------------
            # Cazafantasmas V.O.S.E.
            # 1hr 56min
            # ['16:45', '22:20']
            # ----------------------------------------------------------------------------------------------------
            # Peter y el dragón V.O.S.E.
            # 1hr 43min
            # ['16:05']
            # ----------------------------------------------------------------------------------------------------
            # Jason Bourne V.O.S.E.
            # 2hr 0min
            # ['20:20']
            # ----------------------------------------------------------------------------------------------------
            # [...]
            #
