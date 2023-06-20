"""Login Page Module"""
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.base_page import BasePage
from Pages.station_page import StationPage


class LoginPage(BasePage):
    """Login page class"""

    EMAIL = By.XPATH, '//*[@id="root"]/form/label[1]/input'
    PASSWORD = By.XPATH, '//*[@id="root"]/form/label[2]/input'
    LOGIN_BUTTON = By.XPATH, '//*[@id="root"]/form/button'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_login(self, username, password):
        """To check login functionality"""
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return StationPage(self.driver)
    