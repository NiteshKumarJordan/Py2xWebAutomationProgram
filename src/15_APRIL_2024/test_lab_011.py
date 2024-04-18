

#selenium --driver .quit() is used to close the entire browser window and close the all active session also.

from selenium import webdriver
import time
import pytest
import logging

#@pytest.mark.smoke
def test_open_vwo_login():

    driver = webdriver.Chrome()
    # session is created of a 16 digit number
    # fresh copy of browser is created
    # open new tabs, open url, those will be different from the normal browser
    driver.get("https://app.vwo.com")

    print(driver.title)
    driver.maximize_window()
    #print(driver.page_source)
    #print(driver.session_id)
    assert driver.title == "Login - VWO"
    time.sleep(5)
    driver.quit()