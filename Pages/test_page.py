"""Test Page Module"""

from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Utility.logger import LogGen


class TestPage(BasePage, LogGen):
    """Test page class"""

    Test_Option = By.XPATH, '//*[@id="root"]/nav/div/a[3]/strong'
    Add_Test_Plan = By.XPATH, '//*[@id="root"]/main/div/button[1]'
    Plan_Name = By.XPATH, '//*[@id="stationName"]'
    Test_Path = By.XPATH, '//*[@id="stationName"]'
    Submit = By.XPATH, '//*[@id="root"]/main/button'
    Select_Test = By.XPATH, '//*[@id="root"]/main/div/div[10]'
    Delete_Test = By.XPATH, '//*[@id="root"]/main/div/button[2]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_test(self):
        """To check click test functionality"""
        self.do_click(self.Test_Option)

    def add_test(self):
        """To check add test functionality"""
        self.do_click(self.Test_Option)
        self.do_click(self.Add_Test_Plan)
        self.do_send_keys(self.Plan_Name, '28')
        self.do_send_keys(self.Test_Path, 'bdsjdbjsdbjs')
        self.do_click(self.Submit)

    def delete_test(self):
        """To check delete test functionality"""
        self.do_click(self.Test_Option)
        self.do_click(self.Select_Test)
        self.do_click(self.Delete_Test)
