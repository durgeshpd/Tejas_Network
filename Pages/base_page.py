"""Base Page Module"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage:
    """Base page class"""

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        """To click functionality"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        """To send Keys functionality"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_url(self, url):
        """To get URL functionality"""
        WebDriverWait(self.driver, 10).until(EC.title_is(url))
        return self.driver.current_url

    def get_element_text(self, by_locator):
        """To get text functionality"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        """To check element is visible or not"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        """To get title of webpage"""
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    @staticmethod
    def down_scroll(driver):
        """To scroll down functionality"""
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    @staticmethod
    def up_scroll(driver):
        """To check scroll up functionality"""
        driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

    def dropdown_select(self, by_locator, index):
        """To select an option from a dropdown by index"""
        select = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)))
        return select.select_by_index(index)

    def do_clear(self, by_locator):
        """To clear the text"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def radio_buttons(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
