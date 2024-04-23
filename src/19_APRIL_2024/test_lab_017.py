# SELENIUM = MINI project
# Selenium Project#1 - Mini Project
#
# open the url - https://katalon-demo-cura.herokuapp.com/
# click on the make appoinment button
# verify that url changes - assert
# time.sleep(3)
# enter the username, password
# next page verify the current url
# make appointment text on the web page.

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_open_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(5)
    #driver.find_element(By.ID,"btn-make-appointment").click()

    #Link text
    # make_appointment_button = driver.find_element(By.LINK_TEXT, "Make Appointment")
    # make_appointment_button.click()

    #Partial text
    # make_appointment_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Make Appointment")
    # make_appointment_button.click()

    # TAG NAME
    list_of_a_tags= driver.find_elements(By.TAG_NAME, "a")
    make_appointment_button = list_of_a_tags[5]
    make_appointment_button.click()






    time.sleep(15)









