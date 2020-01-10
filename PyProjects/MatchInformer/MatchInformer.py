from selenium import webdriver
import pandas as pd
import WhatsappSpammer
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/?gws_rd=ssl')
#DO google search for match
def Lookup():
    Match = "leicester city vs liverpool"#input("Enter the name of tha match: ")
    searchbox = driver.find_element_by_css_selector(".gLFyf.gsfi")  #gLFyf gsfi
    searchbox.click()
    searchbox.send_keys(Match)
    searchbox.submit()
    try:
        button = driver.find_element_by_class_name("PUDfGe")
        button.click()
    except:
        table = driver.find_element_by_class_name("imspo_mt__mit")
         #liveresults-sports-immersive__match-tile imso-hov 
        table.click()
Lookup()
time.sleep(1)
def teams():
    team1 = driver.find_element_by_class_name("imso_mh__first-tn-ed").text
    team2 = driver.find_element_by_class_name("imso_mh__second-tn-ed").text
    return team1 + "-" + team2

def scores():
    score1 = driver.find_element_by_class_name("imso_mh__l-tm-sc").text 
    score2 = driver.find_element_by_class_name("imso_mh__r-tm-sc").text
    return score1 + "-" + score2
Stats = driver.find_elements_by_class_name("MzWkAb")
try:
    league = driver.find_element_by_class_name("imso_mh__pst-m-stts-l").text
except:
    print("league not found")
    league = "League not found"

#String handling and beautifying
message = """"""+'{:#^25}'.format(league)
message = message + "\n" +'{:#^25}'.format(teams()) + "\n" + '{:#^25}'.format(scores())
for stat in Stats:
    message = message + "\n"+ '{:#^25}'.format(stat.text)
print(message)
driver.close()
WhatsappSpammer.StartWhatsapp("Contact", message)
