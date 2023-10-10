# Python Version: 3.9.6
# Author: Rodrigo Alves Costa
# Date: Oct 10, 2023

import lib.constants as Constants

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
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
        """ Initialize the URL. """
        self.driver.get(self.url)

    def click_element(self, selector, wait_time=5):
        """
        Click on aan element identified by 'selector'
        Waits for the element to be clickable but clicks as soon as
        it is clickable (explicit wait).
        :param selector: The selector of the element to click
        :param wait_time: Time to wait before timing out, default 5 seconds
        :return: None
        """
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(selector)
        )
        element.click()

    def send_keys_to_element(self, selector, text, wait_time=5):
        """ Enter a username into the username textbox. """
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(selector)
        )
        element.send_keys(text)

    def click_login(self):
        """ Click the login button. """
        self.click_element(self.login_button_selector)
        WebDriverWait(self.driver, 5).until(EC.url_changes)

    def enter_password(self, password):
        """ Enter a password into the password textbox. """
        self.send_keys_to_element(
            self.password_input_box_selector, password
        )

    def enter_username(self, username):
        """ Enter a username into the username textbox. """
        self.send_keys_to_element(self.username_input_box_selector, username)

    def error_message_exists(self):
        """ Returns true if an error message exists on the page,
        false otherwise. """
        error_message = self.driver.find_elements("xpath",
                                                  self.error_message_selector[1]
                                                  )
        return len(error_message) > 0

    def get_error_message_text(self):
        """ Returns the text of the error message on the page, if one exists.
        Returns None otherwise. """
        if self.error_message_exists():
            return self.driver.find_elements("xpath",
                                             self.error_message_selector[1]
                                             )[0].text
        return None

    def login(self, username, password):
        """ Perform a complete login using username and password. """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

# import pytest
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.username_field = driver.find_element(By.ID, "user-name")
#         self.password_field = driver.find_element(By.ID, "password")
#         self.login_button = driver.find_element(By.ID, "login-button")
#         self.error_message = driver.find_element(By.CSS_SELECTOR, ".error-message")
#
#     def login(self, username, password):
#         self.username_field.clear()
#         self.username_field.send_keys(username)
#         self.password_field.clear()
#         self.password_field.send_keys(password)
#         self.login_button.click()
#
#     def get_error_message(self):
#         return self.error_message.text
#
#
# @pytest.fixture(scope="class")
# def driver():
#     # Initialize the WebDriver (you may need to specify the path to your WebDriver executable)
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     yield driver
#     # Close the browser after all tests are finished
#     driver.quit()
#
#
# @pytest.fixture(autouse=True)
# def navigate_to_login_page(driver):
#     # Navigate to the website before each test
#     driver.get("https://www.saucedemo.com/")
