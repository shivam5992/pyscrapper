from BeautifulSoup import BeautifulSoup
import getHtml

def getArticleText(webtext):
	articletext = ""
	soup = BeautifulSoup(webtext)
	for tag in soup.findAll('p',attrs={"itemprop":"articleBody"}):
		articletext += tag.contents[0]
	return articletext.encode('ascii', 'ignore')

def getArticle(url):
	htmtext = getHtml.getHtmlText(url)
	return getArticleText(htmtext)


