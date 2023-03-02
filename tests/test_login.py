from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By


class TestLoginUI:
    def test_title(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        actual_title = driver.title
        assert_that("OrangeHRM").is_equal_to(actual_title)
        #assert actual_title == "OrangeHRM"

    def test_header(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        text = driver.find_element(By.XPATH,"//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title']").text
        assert_that("Login").is_equal_to(text)

