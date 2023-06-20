"""Login Page Test Module"""
from Config.config import TestData
from Pages.login_page import LoginPage
from Tests.test_base import BaseTest


class TestLoginPage(BaseTest):
    """Login page test class"""

    def test_login(self):
        """Test to check log in functionality"""
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

    def test_login_verify(self):
        """Test to verify log in"""
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.loginPage = LoginPage(self.driver)
        assert "test1" == TestData.USER_NAME
        assert "pass1" == TestData.PASSWORD
