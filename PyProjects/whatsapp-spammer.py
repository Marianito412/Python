from selenium import webdriver

class WhatsappBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://web.whatsapp.com/')
    
    def sendMsg(self, msg):
        msg_box = self.driver.find_element_by_xpath('//div[@dir= "ltr"][@spellcheck = "true"][@contenteditable = "true"]')
        msg_box.send_keys(f"{msg}\n")

    def getChat(self, contact):
        search = self.driver.find_element_by_class_name("copyable-text")
        search.send_keys(name)
        user = self.driver.find_element_by_xpath(f'//span[@title = "{name}"][@dir = "auto"]')
        user.click()

if __name__ == "__main__":
    bot = WhatsappBot()
    name = "Me"
    msg = "Hello"
    times = 3
    input("Ready?")
    bot.getChat(name)
    for i in range(times):
        bot.sendMsg(msg)