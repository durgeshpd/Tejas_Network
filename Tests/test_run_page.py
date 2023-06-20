"""Run Page Test Module"""
from Config.config import TestData
from Pages.login_page import LoginPage
from Pages.run_page import RunPage
from Tests.test_base import BaseTest

# pylint: disable=W0201


class TestRun(BaseTest):
    """Run page test class"""

    def driver(self, driver):
        """driver method"""
        self.driver = driver

    def test_click_run(self):
        """To test click functionality of run option"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.run_page = RunPage(self.driver)
        self.station_page.click_run()

    def test_dropdown_fun(self):
        """To test add run functionality"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.station_page = RunPage(self.driver)
        self.station_page.dropdown_fun()

    def test_radio(self):
        self.login_page = LoginPage(self.driver)
        self.station_page = RunPage(self.driver)
        self.station_page.check_station_radio_button()

    def test_check_dup_ip(self):
        self.login_page = LoginPage(self.driver)
        self.station_page = RunPage(self.driver)
        self.station_page.check_dut_ip()

    def test_check_dut_serial_no(self):
        self.login_page = LoginPage(self.driver)
        self.station_page = RunPage(self.driver)
        self.station_page.check_dut_ser_no()

    def test_customer_name(self):
        self.login_page = LoginPage(self.driver)
        self.station_page = RunPage(self.driver)
        self.station_page.check_customer_name()

    def test_search_test_stations(self):
        self.login_page = LoginPage(self.driver)
        self.station_page = RunPage(self.driver)
        self.station_page.check_search_test_stations()

    def test_search_test_plan(self):
        self.login_page = LoginPage(self.driver)
        self.station_page = RunPage(self.driver)
        self.station_page.check_search_test_plans()

    def test_submit(self):
        self.login_page = LoginPage(self.driver)
        self.station_page = RunPage(self.driver)
        self.station_page.check_submit_button()
