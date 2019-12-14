from selenium import webdriver
import pandas as pd
# This a basic test to use selenium webdriver for scraping sites, this is done as a work-around for websites that hold their data on javascript 
# generated code.
driver = webdriver.Chrome()
driver.get('https://www.goodreads.com/work/quotes/71198843-permanent-record')

quotes = driver.find_elements_by_class_name("quote")
items = len(quotes)

total = []

for i in range(items):

    for quote in quotes:
            quote_text = quote.find_element_by_class_name('quoteText').text
            author = quote.find_element_by_class_name('authorOrTitle').text
            new = ((quote_text,author))
            total.append(new)
for item in total:
    print(item)
    print("")
    print("_______________________________________________________________________________________")