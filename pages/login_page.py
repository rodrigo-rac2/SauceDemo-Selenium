# Python Version: 3.9.6
# Author: Rodrigo Alves Costa
# Date: Oct 10, 2023

import lib.constants as Constants

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    """Login page object"""
    def __init__(self, driver):
        self.driver = driver
        self.url = Constants.URL
        self.username_input_box_selector = (By.ID, "user-name")
        self.password_input_box_selector = (By.ID, "password")
        self.login_button_selector = (By.CLASS_NAME, "btn_action")
        self.error_message_selector = (
            By.XPATH, '//*[@id="login_button_container"]/div/form'
        )
        self.init_site()

    def init_site(self):
        """ Initialize the URL """
        self.driver.get(self.url)

    def click_selector(self, selector, wait_time=5):
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

    def send_keys_to_selector(self, selector, text, wait_time=5):
        """ Enter a username into the username textbox. """
        element = WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable(selector)
        )
        element.send_keys(text)

    def click_login(self):
        """ Click the login button. """
        self.click_selector(self.login_button_selector)
        WebDriverWait(self.driver, 5).until(EC.url_changes)

    def type_password(self, password):
        """ Enter a password into the password textbox. """
        self.send_keys_to_selector(
            self.password_input_box_selector, password
        )

    def type_username(self, username):
        """ Enter a username into the username textbox. """
        self.send_keys_to_selector(self.username_input_box_selector, username)

    def is_error_displayed(self):
        """ Returns true if an error message exists on the page,
        false otherwise. """
        error_message = self.driver.find_elements(
            By.XPATH,
            self.error_message_selector[1]
        )
        return len(error_message) > 0

    def get_error_text(self):
        """ Returns the text of the error message on the page, if one exists.
        Returns None otherwise. """
        if self.is_error_displayed():
            return self.driver.find_elements(
                By.XPATH,
                self.error_message_selector[1]
            )[0].text
        return None

    def login(self, username, password):
        """ Perform a complete login using username and password. """
        self.type_username(username)
        self.type_password(password)
        self.click_login()
