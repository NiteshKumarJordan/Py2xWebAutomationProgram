# selenium = WAITS
# selenium -Fluent waits

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait


def test_open_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    # time.sleep(5)
    driver.implicitly_wait(5)

    name_element = driver.find_element(By.NAME, "username")
    name_element.send_keys("nitesh.kumar@360realtors.com")
    password_element = driver.find_element(By.NAME, "password")
    password_element.send_keys("Jordan@test")
    submit = driver.find_element(By.ID, "js-login-btn")
    submit.click()
    # Explicit Wait
    wait = WebDriverWait(driver=driver, timeout=15)
    wait.until
    (Ec.presence_of_element_located((By.CSS_SELECTOR, ".page-heading"))
     )

    # error_msg = driver.find_element(By.ID, "js-notification-box-msg")
    # assert error_msg.text == "Your email, password, IP address or location did not match"
    msg = driver.find_element(By.XPATH, "//h1[contains(text(),'Dashboard')]")
    assert msg.text == "Dashboard", "Error - valid message"
