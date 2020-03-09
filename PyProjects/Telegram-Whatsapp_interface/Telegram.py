import pickle
import time

from selenium import webdriver
location = "C:\\Users\\Mariano\\Desktop\\Mariano\\Projects\\Workspace\\Python\\PyProjects\\Telegram-Whatsapp_interface\\cookies.pkl"
def save_cookies(driver, location):
    pickle.dumps(driver.get_cookies(), open(location, "wb"))
    pickle.dump
def load_cookies(driver, location):
    cookies = pickle.loads(open(location, "rb"))
    driver.delete_all_cookies()
    driver.get("https://google.com")
    time.sleep(5)
    for cookie in cookies:
        driver.add_cookie(cookie)

if __name__ == "__main__":
    #driver = webdriver.Chrome()
    #load_cookies(driver, location)
    #driver.get("https://web.whatsapp.com/")
    #input("Is It Ready?")
    #save_cookies(driver, location)
    #driver.quit()
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=./User_Data')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://web.telegram.org/#/im?p=@TECCRbot')
