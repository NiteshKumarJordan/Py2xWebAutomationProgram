from selenium import webdriver
import time
import pytest
import logging

#@pytest.mark.smoke
def test_open_vwo_login():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.title)
    LOGGER.info("Test print logs")
    assert driver.title == "Login - VWO"
    time.sleep(5)
