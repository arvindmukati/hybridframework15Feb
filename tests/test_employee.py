import time

from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper
import pytest
from utilities import data_source


class TestAddEmployee(WebDriverWrapper):
    @pytest.mark.parametrize('username, password, firstname, middlename, lastname, expected_name1, expected_first_name', data_source.test_add_employee_data)
    def test_valid_login(self,username, password, firstname, middlename, lastname, expected_name1, expected_first_name):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.LINK_TEXT,"PIM").click()
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()
        self.driver.find_element(By.NAME,"firstName").send_keys(firstname)
        self.driver.find_element(By.NAME, "middleName").send_keys(middlename)
        self.driver.find_element(By.NAME, "lastName").send_keys(lastname)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(7)
        header = self.driver.find_element(By.XPATH,"//h6[contains(@class,'oxd-text oxd-text--h6 --strong')]").text
        print(header)
        fname = self.driver.find_element(By.NAME, "firstName").get_attribute("placeholder")
        assert_that(expected_name1).is_equal_to(header)
        assert_that(expected_first_name).is_equal_to(fname)
        time.sleep(3)
