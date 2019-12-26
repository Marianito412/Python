from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

names = ["Deporte 2019", "Química CCSG 2018", "Español Undécimo CCC Gte", "Casa"]
msg = "Feliz Navidad!"
i = 0

input("Scan QR code and confirm ")

for name in names:
    search = driver.find_element_by_xpath('//input[@title = "Search or start new chat"]')
    search.send_keys(name)
    user = driver.find_element_by_xpath('//span[@title = "{}"][@dir = "auto"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_xpath('//div[@dir= "ltr"][@spellcheck = "true"][@contenteditable = "true"]')
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
    print("Hit " + name)
