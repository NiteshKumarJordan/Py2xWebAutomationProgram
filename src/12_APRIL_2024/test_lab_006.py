# Maximize windows screen

from selenium import webdriver
import time
import pytest
import logging

#@pytest.mark.smoke
def test_open_vwo_login():

    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.title)
    driver.maximize_window()
    assert driver.title == "Login - VWO"
    time.sleep(5)
