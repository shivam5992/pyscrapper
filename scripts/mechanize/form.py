from mechanize import Browser
import re

br = Browser()
response = br.open('https://www.google.co.in/')
print response.code

#forms in website
for form in br.forms():
	print form

br.set_handle_robots(False)
br.addheaders = [('User-agent','Safari')]
br.open("https://www.google.co.in/")
br.select_form('f')
br.form['q'] = 'foo'
br.submit()


resp = None

for link in br.links():
	siteMatch = re.compile('www.foofighters.com').search(link.url)

	if siteMatch:
		resp = br.follow_link(link)
		break

content = resp.get_data()
print content