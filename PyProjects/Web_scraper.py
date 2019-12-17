from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

url = "http://www.lappylist.com/laptops/best-programming-laptops/"

uClient = ureq(url)
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")
print(page_soup)
