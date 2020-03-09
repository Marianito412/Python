import pickle
import time
from selenium import webdriver

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:/Users/Mariano/Desktop/Mariano/Projects/Workspace/Chrome profiles/User_Data_Telegram')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://web.telegram.org/#/im?p=@TECCRbot')
