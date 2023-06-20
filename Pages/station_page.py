"""Station Page Module"""

from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Utility.logger import LogGen


class StationPage(BasePage, LogGen):
    """Station page class"""

    Station_Option = By.XPATH, '//*[@id="root"]/div/nav/div/a[2]/strong'
    Add_Station = By.XPATH, '//*[@id="root"]/div/button[1]'
    Station_Name = By.XPATH, '//*[@id="stationName"]'
    KeySight_IP = By.XPATH, '//*[@id="exampleInputPassword1"]'
    Submit = By.XPATH, '//*[@id="addStationForm"]/button'
    Delete_Station = By.XPATH, '//*[@id="root"]/main/button[2]'
    Select_Station = By.XPATH, '//*[@id="root"]/main/div/div[9]/input'

    def __init__(self, driver):
        super().__init__(driver)

    def click_station(self):
        """To check click station functionality"""
        self.do_click(self.Station_Option)

    def add_station(self):
        """To check add station functionality"""
        self.do_click(self.Station_Option)
        self.do_click(self.Add_Station)
        self.do_send_keys(self.Station_Name, 'S1')
        self.do_send_keys(self.KeySight_IP, '192.165.1.224')

    def delete_station(self):
        """To check delete station functionality"""
        self.do_click(self.Station_Option)
        self.do_click(self.Select_Station)
        self.do_click(self.Delete_Station)
