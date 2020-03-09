from selenium import webdriver

whatsapp = "https://web.whatsapp.com/"
telegram = "https://web.telegram.org/#/im?p=u490181666_4123860700758848275"

# 1. listen on whatsap web for user requests
# P6z4j
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/Mariano/Desktop/Mariano/Projects/Workspace/Chrome profiles/User_Data_Telegram')
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://web.whatsapp.com/')
# 2. send revieved message to @TECCRbot
# 3. return response from bot to same user