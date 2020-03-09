from selenium import webdriver

#driver = webdriver.Chrome()
#driver.get('https://web.whatsapp.com/')

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/Mariano/Desktop/Mariano/Projects/Workspace/Chrome profiles/User_Data_Whatsapp_spammer')
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of the target : ')
msg = input('Enter the payload message : ')
count = int(input('Enter the amount of shots : '))

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
k = 0
for i in range(count):
    k = k+1
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
    print("Hit " + str(k) + "!")
