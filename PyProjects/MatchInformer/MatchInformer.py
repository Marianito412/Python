from selenium import webdriver
import pandas as pd
url = "https://www.google.com/search?source=hp&ei=9ULwXYfJJ43isAfUtLAo&q=Milan+vs+Barcelona&oq=Milan+vs+Barcelona&gs_l=psy-ab.3...3522.3889..3921...0.0..0.0.0.......0....1..gws-wiz.....0.pAAE2Xf1334#sie=m;/g/11f5h9xrtk;2;/m/0_s0sq4;dt;fp;1;;"

driver = webdriver.Chrome()
driver.get(url)

league = driver.find_element_by_class_name("imso_mh__pst-m-stts-l").text
print(league)
driver.close()
