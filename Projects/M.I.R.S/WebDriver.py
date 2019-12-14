from selenium import webdriver
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

driver = webdriver.Chrome()
driver.get('https://calendar.google.com/calendar/r/week?tab=wc&pli=1&t=AKUaPmYCYUwEvphGytdq_Nb4v9siB5-UG35kfJm2bWnAdd53vQMU7wMxvneUDvOQrALjcrQS_QJ1vZdc5PWBX2xiNPK-jH0Lww%3D%3D')
driver.get("https://mail.google.com/mail/u/0/?tab=cm#inbox")

url = "https://mail.google.com/mail/u/0/?tab=cm#inbox"
uClient = ureq(url)
page_html = uClient.read()
i = 0
uClient.close()

#Google Calendar Shit


#Gmail Shit
mail = driver.find_element_by_class_name("bog")

    

#The Symphony
