from selenium import webdriver
import pytest

class WebDriverWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        browser_name = "Chrome"
        if browser_name == "edge":
            self.driver = webdriver.Edge()
        elif browser_name == "ff":
            self.driver = webdriver.Firefox()
        else:
            self.driver =webdriver.Chrome()

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        yield
        self.driver.quit()
