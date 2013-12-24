from BeautifulSoup import BeautifulSoup
import getHtml

def getArticleText(webtext):
	articletext = ""
	soup = BeautifulSoup(webtext)
	
	#can chage this for any general website to get p tags of a webpage, remove attrs thing:: ,attrs={"itemprop":"articleBody"}

	for tag in soup.findAll('p',attrs={"itemprop":"articleBody"}):
		articletext += tag.contents[0]
	return articletext.encode('ascii', 'ignore')

def getArticle(url):
	htmtext = getHtml.getHtmlText(url)
	return getArticleText(htmtext)

def getKeywords(articletext):
	common = open("common.txt").read().split('\n')
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
