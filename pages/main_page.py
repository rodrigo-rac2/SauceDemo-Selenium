from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.constants import INVENTORY_URL


class MainPage():
    """ Main page of the application, after login """
    def __init__(self, driver):
        self.driver = driver
        self.hamburger_menu_selector = (By.ID, "react-burger-menu-btn")
        self.logout_selector = (By.ID, "logout_sidebar_link")
        self.menu_button_container = (By.ID, "menu_button_container")
        self.init_site()

    def init_site(self, wait_time=5):
        """ Waits until the page is loaded """
        WebDriverWait(self.driver, wait_time).until(
            EC.url_matches(INVENTORY_URL)
        )

    def click_element(self, selector, wait_time=5):
        """
        Click on an element identified by 'selector'
        Waits for the element to be clickable but clicks as soon as
        it is clickable (explicit wait).
        :param selector: The selector of the element to click
        :param wait_time: Time to wait before timing out, default 5 seconds
        :return: None
        """
        element = WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable(selector)
        )
        element.click()

    def click_hamburger_menu(self):
        """ Open the hamburger menu. """
        self.click_element(self.hamburger_menu_selector)

    def click_logout(self):
        """ Click the product sort menu. """
        self.click_element(self.logout_selector)

    def logout(self):
        """ Logout of the application. """
        self.click_hamburger_menu()
        self.click_logout()
        # Times out and fails if the URL does not change within 5 seconds.
        WebDriverWait(self.driver, 5).until(EC.url_changes)
