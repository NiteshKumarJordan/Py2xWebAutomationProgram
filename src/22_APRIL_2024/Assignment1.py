
# Selenium Mini Project: 1
# open ebay website
# search 16 Gb
# print the price of all products
# find the cheapest of the products

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_ebay():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com")
    time.sleep(10)
    driver.find_element(By.XPATH, "//input[@id='gh-ac']").click()
    driver.find_element(By.XPATH, "//input[@id='gh-ac']").send_keys('16 GB')
    driver.find_element(By.XPATH, "//input[@id='gh-btn']").click()
    driver.maximize_window()
    time.sleep(12)
    price_data = driver.find_element(By.XPATH, "//span[starts-with(text(),'$')]")
    time.sleep(5)
    print(price_data)

