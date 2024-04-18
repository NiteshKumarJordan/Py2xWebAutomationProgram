from selenium import webdriver
import time
import pytest


@pytest.mark.smoke
def test_open_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    time.sleep(5)


