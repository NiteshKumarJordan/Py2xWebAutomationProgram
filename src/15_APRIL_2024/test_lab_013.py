# Navigate commands in selenium(refresh, back, forward)
from selenium import webdriver
import time



def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    #driver.navigate()----don't exist in python.

    driver.back()
    driver.get("https://bing.com/chat")
    print(driver.title)

    driver.forward()
    print(driver.title)

    driver.refresh()

    time.sleep(15)





