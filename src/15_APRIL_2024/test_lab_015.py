
# Selenium -open website app.vwo.com and verify the erorr msg displying
# on wrong entered of password


from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_open_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    time.sleep(5)
    driver.find_element(By.NAME,"username").send_keys("username")
    driver.find_element(By.NAME,"password").send_keys("<PASSWORD>")
    driver.find_element(By.ID, "js-login-btn").click()
    time.sleep(6)

    error_msg = driver.find_element(By.ID, "js-notification-box-msg")
    assert error_msg.text == "Your email, password, IP address or location did not match"







