from BeautifulSoup import BeautifulSoup
import mechanize

'''
Function to get htmltext from webpage
'''
def getHtmlText(url):
	br = mechanize.Browser()
	htmltext = br.open(url).read()
	return htmltext

def getHtmlFile(url):
	br = mechanize.Browser()
	htmltext = br.open(url)
	return htmltext

'''
Get text from webpage.
'''
def getArticleText(webtext):
	articletext = ""
	soup = BeautifulSoup(webtext)
	
	'''
	Can chage the following code for any general website to get text
	from particular tags of a webpage
	'''
	for tag in soup.findAll('p',attrs={"itemprop":"articleBody"}):
		articletext += tag.contents[0]
	return articletext.encode('ascii', 'ignore')

def getArticle(url):
	htmtext = getHtmlText(url)
	return getArticleText(htmtext)