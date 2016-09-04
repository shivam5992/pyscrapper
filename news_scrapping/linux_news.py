#!/usr/bin/python
# encoding=utf-8

import json
import re
from bs4 import BeautifulSoup

import requests

'''
Python class to scrap latest news from linux.com
'''


class linux_news:
    def __init__(self):
        url = "https://www.linux.com/news/"
        req = requests.get(url)
        htmltext = req.text
        # doc = html5lib.parse(htmltext, treebuilder="lxml")
        self.soup = BeautifulSoup(htmltext, "lxml")

    # Function which scraps the news in the given URL.
    # Needs to be reworked as every website has a different tag structure
    # Returns a list of dictionaries.
    def scrap(self):
        soup_object = self.soup
        output = []

        for tag in soup_object.findAll("div", {"class": re.compile("views-row")}):
            dict = {}

            dict['title'] = tag.find("h3").find("a").string
            dict['resume'] = tag.find("div", attrs={"class": "article-list__summary"}).string
            dict['from'] = tag.find("div", attrs={"class": "article-list__submitted"}).find("a").string
            dict['link'] = "https://www.linux.com/" + tag.find("div", attrs={"class": "article-list__links"}).find(
                "span").a.get('href')

            output.append(dict)

        return output


if __name__ == '__main__':
    scrap_object = linux_news()
    response = scrap_object.scrap()
    jsondump = json.dumps(response, indent=4, ensure_ascii=False).encode('utf8')
    print(jsondump)
