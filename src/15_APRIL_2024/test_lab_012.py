# navigate command is used to navigate to different places
from selenium import webdriver
import time



def test_navigate():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    time.sleep(20)
    driver.get("https://www.flipkart.com")