# Python Version: 3.9.6
# Author: Rodrigo Alves Costa
# Date: Oct 10, 2023


"""This test file verifies the logout functionality of saucedemo.com"""
import pytest
import lib.login_credentials as LoginCreds
from lib.constants import CHROME_MOBILE, CHROME_HEADLESS
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.parametrize(
    "browser, mode, device, user",
    [
        (*CHROME_MOBILE, LoginCreds.STANDARD_USER),
        (*CHROME_HEADLESS, LoginCreds.STANDARD_USER),
    ],
)
@pytest.mark.logout
def test_logout(driver, browser, mode, device, user):
    """Test logging in and logging out with a valid username/password."""
    login_page = LoginPage(driver)
    login_page.login(user["username"], user["password"])
    main_page = MainPage(driver)
    main_page.logout()
    assert driver.current_url == login_page.url
