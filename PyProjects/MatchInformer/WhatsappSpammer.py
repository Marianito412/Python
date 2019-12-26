from selenium import webdriver

def StartWhatsapp(name, msg):
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    input('Scan the QR code and confirm ')
    input("Ready, standing by for confirmation ")
    try:
        search = driver.find_element_by_xpath('//input[@title = "Search or start new chat"]')
    except:
        search = driver.find_element_by_xpath('//input[@title = "Buscar o empezar un chat nuevo"]')
    search.send_keys(name)
    user = driver.find_element_by_xpath('//span[@title = "{}"][@dir = "auto"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_xpath('//div[@dir= "ltr"][@spellcheck = "true"][@contenteditable = "true"]')
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
