"""Test Page Test Module"""
from Config.config import TestData
from Pages.test_page import TestPage
from Pages.login_page import LoginPage
from Tests.test_base import BaseTest

# pylint: disable=W0201


class TestStation(BaseTest):
    """Test page test class"""

    def driver(self, driver):
        """driver method"""
        self.driver = driver

    def test_click_test(self):
        """To test click functionality of test option"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.test_page = TestPage(self.driver)
        self.test_page.click_test()

    def test_add_test(self):
        """To test add test functionality"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.test_page = TestPage(self.driver)
        self.test_page.add_test()
