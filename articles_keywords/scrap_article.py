import articleText

url = "http://www.nytimes.com/2013/12/22/magazine/finding-inner-peace-with-the-angriest-punk-of-70s-new-york.html"
url1 = "http://bleacherreport.com/articles/1898074-he-shield-must-feud-with-the-wyatt-family-before-inevitable-split"

'''
Get article from nytimes(or any website)
'''
article = articleText.getArticle(url)
print article


'''
Top keywords from website
'''
#article1 = articleText.getHtmlText(url1)
#print articleText.getKeywords(article1)
