import requests
from bs4 import BeautifulSoup as soup
import wget
import os.path
import csv

base = "http://link.springer.com"
bookdict = {} 
headers = requests.utils.default_headers()
with open("Springer Ebooks (1).csv", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    counter = 1
    for row in csv_reader:
        if counter == 1:
            counter = counter + 1 
        else:
            try:
                bookdict[row[1]] = row[4]
                counter = counter + 1
            except:
                counter = counter + 1

bookdict.pop("Book Title")
bookdict.pop("")

for i in bookdict:
    print(i, bookdict[i])
    if os.path.isfile("C:/Users/Mariano/Desktop/Mariano/Documents/Books/" + i + ".pdf"):
        print("Already downloaded, moving on")
    else:
        req = requests.get(bookdict[i], headers)
        soups = soup(req.content, 'html.parser')
        try:
            a = soups.find("a", title="Download this book in PDF format")
            uri = a.get("href")
        except:
            a = soups.find("a", {"class": "content-type-list__action-label test-book-toc-download-link"})
            uri = a.get("href")
        wget.download(base+uri, "C:/Users/Mariano/Desktop/Mariano/Documents/Books/" + i + ".pdf")
        print("")



