# selenium 3


from selenium import webdriver


def test_open_browser(self):
    driver_path = "C:/Users/new ssd/Downloads/chromedriver-win64/chromedriver-win64"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    driver.close()
    driver.quit()
