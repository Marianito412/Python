from selenium import webdriver
import time

#email: "jmarianosoto@gmail.com"
#password: "dfghfg"
#rememberMe: true
#

driver = webdriver.Chrome()
driver.get("https://www.epicgames.com/store/es-ES/?sessionInvalidated=true") #Check if that is the real url

def getGame():
    #Click obtain
    driver.find_element_by_tag_name("").click()
    #Click back
    driver.find_elements_by_class_name("")
time.sleep(3)
games = driver.find_elements_by_class_name("CardGrid-groupWrapper_37469a6b")
free_games = games[2].find_element_by_class_name("CardGrid-card_d639e18a")
free_games.click()
