# Selenium Mini Project #3

# Open the URL - https://www.idrive360.com/enterprise/login
# Enter the username, password
# Verify that Trial is fnished and current URL also
# Add a logic to add Allure Screen for the Trail end



import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium import webdriver


def test_mini_project03():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #username = "augtest_040823@idrive.com"
    #password = "123456"
    driver.get("https://www.idrive360.com/enterprise/login")
    time.sleep(5)
    driver.find_element(By.ID, "username").send_keys("augtest_040823@idrive.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "frm-btn").click()
    time.sleep(20)
    current_url = driver.current_url
    time.sleep(15)
    message = driver.find_element(By.XPATH,"//h5[@class='id-card-title']").text
    print(message)
    assert message == "Your free trial has expired", "Error - Invalid message"
    allure.attach(driver.get_screenshot_as_png(), name="empty-username", attachment_type=AttachmentType.PNG)



