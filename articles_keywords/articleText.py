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

'''
Get keywords with their frequency in sorted manner from a webpage.
'''
def getKeywords(articletext):
	common = open("common_words.txt").read().split('\n')
	word_dict = {}
	word_list = articletext.lower().split()
	for word in word_list:
		if word not in common and word.isalnum():
			if word not in word_dict:
				word_dict[word] = 1
			if word in word_dict:
				word_dict[word] += 1
	top_words =  sorted(word_dict.items(),key=lambda(k,v):(v,k),reverse=True)[0:50]
	top50 = []
	for w in top_words:
		top50.append(w)
	return top50
