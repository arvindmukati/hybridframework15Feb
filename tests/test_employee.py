import time

from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper

class TestAddEmployee(WebDriverWrapper):
    def test_valid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.LINK_TEXT,"PIM").click()
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()
        self.driver.find_element(By.NAME,"firstName").send_keys("Jhon")
        self.driver.find_element(By.NAME, "middleName").send_keys("J")
        self.driver.find_element(By.NAME, "lastName").send_keys("Wick")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        name = self.driver.find_element(By.XPATH,"//h6[contains(normalize-space(),'Jhon Wick')]").text
        assert_that("Jhon Wick").is_equal_to(name)
        time.sleep(3)
