"""Conftest File"""
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        serv_obj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        request.cls.driver = driver
        yield
        driver.close()
