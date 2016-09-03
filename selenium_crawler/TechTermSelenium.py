'''
This script concatenates searches by iterating over the alphabet in a search box from a given URL.
Results are stored as txt files.
'''

from string import ascii_lowercase

from selenium import webdriver

caselist = ascii_lowercase + "1"
categories = []
catfile = open("out/categories.txt", "w")
fout = open("out/tech_words.txt", "w")
browser = webdriver.Firefox()

# Main loop
for letter in ascii_lowercase:
    print(letter)
    url = 'http://www.techterms.com/list/' + letter
    browser.get(url)
    table = browser.find_element_by_tag_name('tbody')
    for i, x in enumerate(table.find_elements_by_class_name('sorting_1')):
        word = str(x.text.encode('utf-8').decode('ASCII', 'ignore'))
        category = table.find_element_by_xpath("//*/tbody/tr[" + str(i + 1) + "]/td[2]").text
        # category = table.find_element_by_xpath("//*[@id='alphatable']/tbody/tr[" + str(i + 1) + "]/td[2]").text
        category = str(category.encode('utf-8').decode('ASCII', 'ignore'))
        if category not in categories:
            categories.append(category)
            catfile.write(category + "\n")
        fout.write(word + "\n")
browser.close()
