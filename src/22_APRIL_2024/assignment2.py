# Selenium Mini project #2
#
#
# Open the URL - https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage
# Enter all the fields excepts the username
# Verify that the error message comes when you click on the submit button.
import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium import webdriver


def test_mini_project02():
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    time.sleep(2)
    driver.switch_to.frame(driver.find_element(By.ID, "result"))
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("nitesh.test.com")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("541541")
    driver.find_element(By.XPATH, "//input[@id='password2']").send_keys("252525")
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="empty-username", attachment_type=AttachmentType.PNG)
    assert (driver.find_element(By.XPATH,
                                "//input[@id='username']/following::small").text
            == "Username must be at least 3 characters")
