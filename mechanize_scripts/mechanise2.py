'''
Reference : https://views.scraperwiki.com/run/python_mechanize_cheat_sheet/
'''

import mechanize

br = mechanize.Browser()
#br.set_all_readonly(False) # allow everthing in write mode
br.set_handle_robots(False) #no robots.txt
br.set_handle_refresh(False) # can sometimes hang without this
br.addheaders = [('User-agent','Mozilla/5.0')]
br.open("https://www.irctc.co.in/cgi-bin/bv60.dll/irctc/services/register.do?click=true")


'''
getting the source code using mechanize
'''

#opn a webpage and inspect its contents
#url = "http://www.bodybuilding.com"
#response = br.open(url)
#print response.read()


'''
list all the forms in the webpage
'''

for form in br.forms():
	print "Form Name", form.name
	#print form

'''
Selecting a form
'''
#br.select_form("f")
# or use this
br.form = list(br.forms())[0]

'''
Form Control
'''

for control in br.form.controls:
	#print control
	#print control.type
	#print control.name
	#print br[control.name]

	'''
	finding controls by name
	'''
	#control = br.form.find_control("controlname")

	'''
	Control : Select
	'''

	if control.type == "Select":
		for item in control.items:
			print item.name


'''
when the form is ready, you can submit item
'''
response = br.submit()
print response.read()
br.back() # go back
