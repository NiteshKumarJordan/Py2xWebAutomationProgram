# Selenium 1st prograam to open the url and click particular button.
# https://katalon-demo-cura.herokuapp.com/


from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def test_open_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(5)
    element=driver.find_element(By.ID,"btn-make-appointment")
    element.click()
    time.sleep(5)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    driver.close()



