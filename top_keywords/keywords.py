import urllib

from BeautifulSoup import BeautifulSoup

'''
function to get top keywords from the whole text
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


url = "http://en.wikipedia.org/wiki/In-memory_database"
htmltext = urllib.urlopen(url).read()
soup = BeautifulSoup(htmltext)

'''
Collect all text from url
'''
article = ""
for text in soup.findAll(text=True):
	article += text.encode("utf-8")

#print article

print getKeywords(article)
