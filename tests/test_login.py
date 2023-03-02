from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By
import pytest


class TestLoginUI:
    @pytest.fixture(scope="function",autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        yield
        self.driver.quit()

    def test_title(self):
        actual_title = self.driver.title
        assert_that("OrangeHRM").is_equal_to(actual_title)
        #assert actual_title == "OrangeHRM"

    def test_header(self):
        text = self.driver.find_element(By.XPATH,"//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title']").text
        assert_that("Login").is_equal_to(text)

