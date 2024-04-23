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
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import time
import pytest
import allure_pytest
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@allure.title("Verify the login is working fine")
def test_open_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(5)
    driver.find_element(By.ID, "btn-make-appointment").click()

    time.sleep(5)
    print(driver.current_url)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(15)
    username = driver.find_element(By.NAME, "username")
    username.send_keys("John Doe")
    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID, "btn-login").click()

    allure.attach(driver.get_screenshot_as_png(), name = "Screenshot", attachment_type=AttachmentType.PNG)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    time.sleep(10)
    driver.close()
