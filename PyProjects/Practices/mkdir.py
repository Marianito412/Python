import os
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://tecdigital.tec.ac.cr/dotlrn/courses")

driver.find_element_by_name("username").send_keys("2020142918")
driver.find_element_by_name("password").send_keys("holasoymariano")
driver.find_element_by_name("formbutton:style").click()
#driver.find_element_by_partial_link_text("/dotlrn/courses").click()
time.sleep(5)
course_list = driver.find_element_by_class_name("portlet")
courses = course_list.find_elements_by_tag_name("li")
for course in courses:
    print(course.text)


#courses = ["Apreciacion de cine", "Comunicación escrita", "Dibujo técnico", "Elementos de computación", "Física general II", "Intr ciencia y tecnología", "Lab Física II", "Algebra Lineal"]
#for course in courses:
#    course_path = path + "/" + course
#    os.mkdir(course_path)
#    print("creating directory {}".format(course_path))