"""Station Page Test Module"""
from Config.config import TestData
from Pages.station_page import StationPage
from Pages.login_page import LoginPage
from Tests.test_base import BaseTest

# pylint: disable=W0201


class TestStation(BaseTest):
    """Station page test class"""

    def driver(self, driver):
        """driver method"""
        self.driver = driver

    def test_click_station(self):
        """To test click functionality of station option"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.station_page = StationPage(self.driver)
        self.station_page.click_station()

    def test_add_station(self):
        """To test add station functionality"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.station_page = StationPage(self.driver)
        self.station_page.add_station()

    def test_delete_station(self):
        """To test add station functionality"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.station_page = StationPage(self.driver)
        self.station_page.delete_station()
