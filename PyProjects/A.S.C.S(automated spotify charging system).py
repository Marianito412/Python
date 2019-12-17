from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

names = ["S", "R", "S", "F"]
msg = "Spotify. couta grupal: 8.99 dolares. Couta por persona: 800 colones(Este es un mensaje automatizado,no responder solo obedecer)"
i = 0

input("Scan QR code and confirm ")
search = driver.find_element_by_css_selector(".jN-F5.copyable-text.selectable-text")
search.send_keys("S-")
for name in names:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_xpath('//div[@dir = "ltr"]')
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
    print("Hit " + name)
