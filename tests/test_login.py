from selenium import webdriver
from assertpy import assert_that
class TestLoginUI:
    def test_title(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        actual_title = driver.title
        assert_that("OrangeHRM").is_equal_to(actual_title)
        #assert actual_title == "OrangeHRM"
