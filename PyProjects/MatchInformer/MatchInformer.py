from selenium import webdriver
import pandas as pd
import WhatsappSpammer
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/?gws_rd=ssl')
#DO google search for match
Match = "arsenal vs liverpool"#input("Enter the name of tha match: ")
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
url = driver.current_url
time.sleep(1)
#Get all stats
league = driver.find_element_by_class_name("imso_mh__pst-m-stts-l").text
print(league)
team1 = driver.find_element_by_class_name("imso_mh__first-tn-ed").text
team2 = driver.find_element_by_class_name("imso_mh__second-tn-ed").text 
score1 = driver.find_element_by_class_name("imso_mh__l-tm-sc").text 
score2 = driver.find_element_by_class_name("imso_mh__r-tm-sc").text
Stats = driver.find_elements_by_class_name("MzWkAb")

#print(score1 + "-" + score2)
#print(team1 + "-" + team2)
#String handling and beautifying
message = """"""+'{:#^25}'.format(league)
message = message + "\n" +'{:#^25}'.format(team1 + "-" + team2) + "\n" + '{:#^25}'.format(score1 + "-" + score2)
for stat in Stats:
    message = message + "\n"+ '{:#^25}'.format(stat.text)
print(message)
driver.close()
WhatsappSpammer.StartWhatsapp("TestContact", message)