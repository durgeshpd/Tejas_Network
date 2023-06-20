"""Run Page Module"""

from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Utility.logger import LogGen


class RunPage(BasePage, LogGen):
    """Run page class"""

    Run_Option = By.XPATH, '//*[@id="root"]/nav/div/a[4]/strong'
    Create_Run = By.XPATH, '//*[@id="root"]/main/button'
    Select_Device = By.XPATH, '//*[@id="selectList"]'
    DUT_IP = By.XPATH, '//*[@id="root"]/main/div[3]/div/input[1]'
    DUT_Ser_No = By.XPATH, '//*[@id="root"]/main/div[3]/div/input[2]'
    Customer = By.XPATH, '//*[@id="root"]/main/input'
    Search_Test_Stations = By.XPATH, '//*[@id="root"]/main/div[4]/div[1]/div[1]/div[2]/input'
    Search_Test_Plans = By.XPATH, '//*[@id="root"]/main/div[4]/div[2]/div[1]/div/input'
    Radio_Buttons = By.XPATH, '//input[@type="radio"]'
    Submit = By.XPATH, '//*[@id="root"]/main/button'

    def __init__(self, driver):
        super().__init__(driver)

    def click_run(self):
        """To check click run functionality"""
        self.do_click(self.Run_Option)

    def dropdown_fun(self):
        """To check add run functionality"""
        self.do_click(self.Run_Option)
        self.do_click(self.Create_Run)
        self.dropdown_select(self.Select_Device, 0)
        self.dropdown_select(self.Select_Device, 1)
        self.dropdown_select(self.Select_Device, 2)

    def check_station_radio_button(self):
        self.do_click(self.Run_Option)
        self.do_click(self.Create_Run)
        radio_buttons = self.driver.find_elements(*self.Radio_Buttons)
        for radio_button in radio_buttons:
            radio_button.click()

    def check_dut_ip(self):
        self.do_click(self.Run_Option)
        self.do_click(self.Create_Run)
        self.dropdown_select(self.Select_Device, 0)
        self.do_send_keys(self.DUT_IP, '192.36.255')

    def check_dut_ser_no(self):
        self.do_click(self.Run_Option)
        self.do_click(self.Create_Run)
        self.dropdown_select(self.Select_Device, 0)
        self.do_send_keys(self.DUT_Ser_No, '1')

    def check_customer_name(self):
        self.do_click(self.Run_Option)
        self.do_click(self.Create_Run)
        self.dropdown_select(self.Select_Device, 0)
        self.do_send_keys(self.Customer, 'BSNL')

    def check_search_test_stations(self):
        self.do_click(self.Run_Option)
        self.do_click(self.Create_Run)
        self.dropdown_select(self.Select_Device, 0)
        self.do_send_keys(self.Search_Test_Stations, 'Tejas')

    def check_search_test_plans(self):
        self.do_click(self.Run_Option)
        self.do_click(self.Create_Run)
        self.dropdown_select(self.Select_Device, 0)
        self.do_send_keys(self.Search_Test_Plans, 'Resources')

    def check_submit_button(self):
        self.do_click(self.Run_Option)
        self.do_click(self.Create_Run)
        self.dropdown_select(self.Select_Device, 0)
        self.do_click(self.Submit)

