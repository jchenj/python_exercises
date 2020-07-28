#! /usr/bin/python3
# scrapeInventPython -> find first element with class name "dropdown-item"

from selenium import webdriver
browser = webdriver.Chrome('/Users/jchen/Desktop/chromedriver')
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('dropdown-item')
    print('Found <%s> element with that class name. Text is "%s".' %
          (elem.tag_name, elem.location))
except:
    print('No element found with that class name.')
