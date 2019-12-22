from selenium import webdriver
import time
#feel free to play around with the .sleep() times, i used this due to my slow wifi speed
url = "https://www.epicgames.com/id/login?lang=es_ES&redirectUrl=https%3A%2F%2Fwww.epicgames.com%2Fstore%2Fes-ES%2F%3FsessionInvalidated%3Dtrue&client_id=875a3b57d3a640a6b7f9b4e883463ab4&noHostRedirect=true"
driver = webdriver.Chrome()

email = "insert your email"
password = "you get the idea"

def SignIn(driver):
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_id("email").send_keys("jmarianosot@gmail.com")
    driver.find_element_by_id("password").send_keys("holasoymariano412\n")

def getGame(driver):
    obtain = driver.find_element_by_class_name("PurchaseButton-button_0fd80531")
    obtain.click()
    time.sleep(1)
    purchase = driver.find_element_by_class_name("btn-primary")
    purchase.click()

def findGame(driver):
    category = driver.find_elements_by_class_name("Discover-section_c504570a")
    free = category[3]
    print(free.text)
    game = free.find_element_by_class_name("Card-root_06ca652d")
    game.click()

if __name__ == "__main__":
    SignIn(driver)
    time.sleep(10)
    findGame(driver)
    getGame(driver)
