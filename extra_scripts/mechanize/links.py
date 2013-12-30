'''
Get all links
'''
import mechanize

br = mechanize.Browser()
#br.set_all_readonly(False) # allow everthing in write mode
br.set_handle_robots(False) #no robots.txt
br.set_handle_refresh(False) # can sometimes hang without this
br.addheaders = [('User-agent','Mozilla/5.0')]
br.open("https://www.irctc.co.in/cgi-bin/bv60.dll/irctc/services/register.do?click=true")

for link in br.links():
	#print link.text, link.url
	request = br.click_link(link)
	response = br.follow_link(link)
	print response.geturl()


