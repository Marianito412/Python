from selenium import webdriver
import pandas as pd
url = "https://www.google.com/search?source=hp&ei=9ULwXYfJJ43isAfUtLAo&q=Milan+vs+Barcelona&oq=Milan+vs+Barcelona&gs_l=psy-ab.3...3522.3889..3921...0.0..0.0.0.......0....1..gws-wiz.....0.pAAE2Xf1334#sie=m;/g/11f5h9xrtk;2;/m/0_s0sq4;dt;fp;1;;"

driver = webdriver.Chrome()
driver.get(url)

league = driver.find_element_by_class_name("imso_mh__pst-m-stts-l").text
team1 = driver.find_element_by_xpath('//div[@data-df-team-mid = "/m/011v3"]').text
team2 = driver.find_element_by_xpath('//div[@data-df-team-mid = "/m/0hvgt"]').text 
score1 = driver.find_element_by_class_name("imso_mh__l-tm-sc").text #imso_mh__l-tm-sc imso_mh__scr-it imso-light-font
score2 = driver.find_element_by_class_name("imso_mh__r-tm-sc").text              #imso_mh__r-tm-sc imso_mh__scr-it imso-light-font
print(str(team1)+ "-" + str(team2))
print(score1 + "-" + score2)
driver.close()
