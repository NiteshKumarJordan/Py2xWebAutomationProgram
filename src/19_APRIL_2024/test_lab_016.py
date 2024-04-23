
# Selenium -open website app.vwo.com and verify the errors msg displaying
# on wrong entered of password
# using object storage

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_open_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    time.sleep(5)
    name_element=driver.find_element(By.NAME,"username")
    name_element.send_keys("nitesh")
    password_element = driver.find_element(By.NAME,"password")
    password_element.send_keys("<PASSWORD>")
    submit = driver.find_element(By.ID, "js-login-btn")
    submit.click()
    time.sleep(6)

    error_msg = driver.find_element(By.ID, "js-notification-box-msg")
    assert error_msg.text == "Your email, password, IP address or location did not match"







