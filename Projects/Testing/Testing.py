from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import Request, urlopen


driver = webdriver.Chrome()
driver.get('https://www.google.com/?gws_rd=ssl')
#DO google search for match
Match = "Milan vs Barcelona"#input("Enter the name of tha match: ")
searchbox = driver.find_element_by_css_selector(".gLFyf.gsfi")  #gLFyf gsfi
searchbox.click()
searchbox.send_keys(Match)
searchbox.submit()
button = driver.find_element_by_class_name("PUDfGe")
button.click()
url = driver.current_url



# /Team 1 = imso_mh__first-tn-ed imso_mh__tnal-cont imso-tnol 
# / Team 2 = imso_mh__second-tn-ed imso_mh__tnal-cont imso-tnol 
# / Score = imso_mh__scr-sep
# / time left = imso_mh__ft-mtch imso-medium-font
def scrape(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page_html = urlopen(req).read()
    page_soup = soup(page_html, "html.parser")
    time_left = page_soup.find("span", {"class": "imso_mh__ft-mtch imso-medium-font"})
    date = page_soup.find("div", {"class":"imso-hide-overflow"})
    print(str(time_left), date)
print(url)

