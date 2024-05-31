# data driven testing
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver

# def read_credentials_from_excel(file_path):
#
#
#
#
#
# def test_vwo_login(user_cred):
#     username = user_cred['username']
#     password = user_cred['password']
#     test_open_vwo_login(usernamme=username,
#                         password=password)


def test_open_vwo_login():
    username = "nitesh.kumar@360realtors.com"
    password = "Jordan@test"

    driver = webdriver.Chrome()

    driver.get("https://app.vwo.com")
    # time.sleep(5)
    driver.implicitly_wait(5)


    name_element = driver.find_element(By.NAME, "username")
    name_element.send_keys(username)
    password_element = driver.find_element(By.NAME, "password")
    password_element.send_keys(password)
    submit = driver.find_element(By.ID, "js-login-btn")
    submit.click()
    # time.sleep(6)
    driver.implicitly_wait(10)

    # error_msg = driver.find_element(By.ID, "js-notification-box-msg")
    # assert error_msg.text == "Your email, password, IP address or location did not match"
    msg = driver.find_element(By.XPATH, "//h1[contains(text(),'Select Products')]")
    assert msg.text == "Select Products", "Error - Invalid message"







