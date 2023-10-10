# Python Version: 3.9.6
# Author: Rodrigo Alves Costa
# Date: Oct 10, 2023


"""This test file verifies the login page of saucedemo.com"""
import pytest
import lib.login_credentials as LoginCreds
from lib.constants import CHROME_MOBILE, CHROME_HEADLESS
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "browser, mode, device, user",
    [
        (*CHROME_MOBILE, LoginCreds.STANDARD_USER),
        (*CHROME_HEADLESS, LoginCreds.STANDARD_USER),
    ],
)
@pytest.mark.login
@pytest.mark.login_success
def test_login_valid_user(driver, browser, mode, device, user):
    """Test logging in with a valid username/password."""
    login_page = LoginPage(driver)
    login_page.enter_username(user["username"])
    login_page.enter_password(user["password"])
    login_page.click_login()
    assert not login_page.error_message_exists()
    print("Test finished.")


@pytest.mark.parametrize(
    "browser, mode, device, user",
    [
        (*CHROME_MOBILE, LoginCreds.LOCKED_OUT_USER),
        (*CHROME_HEADLESS, LoginCreds.LOCKED_OUT_USER),
    ],
)
@pytest.mark.login
@pytest.mark.login_lockedout
def test_login_locked_out_user(driver, browser, mode, device, user):
    """Test logging in with a user who is locked out."""
    login_page = LoginPage(driver)
    login_page.login(user["username"], user["password"])
    assert login_page.error_message_exists()
    print(login_page.get_error_message_text())
    print("test_login_locked_out_user finished successfully.")


@pytest.mark.parametrize(
    "browser, mode, device, user",
    [
        (*CHROME_MOBILE, LoginCreds.INVALID_USER),
        (*CHROME_HEADLESS, LoginCreds.SQL_INJECTION_USER),
    ]
)
@pytest.mark.login
@pytest.mark.login_incorrect
def test_login_incorrect_credentials(driver, browser, mode, device, user):
    """Test attempting to log in with invalid credentials."""
    login_page = LoginPage(driver)
    login_page.login(user["username"], user["password"])
    assert login_page.error_message_exists()
    print(login_page.get_error_message_text())
    print("test_login_incorrect_credentials finished successfully.")


@pytest.mark.parametrize(
    "browser, mode, device, user",
    [
        (*CHROME_MOBILE, LoginCreds.EMPTY_USERNAME),
        (*CHROME_HEADLESS, LoginCreds.EMPTY_USERNAME),
    ],
)
@pytest.mark.login
@pytest.mark.login_incorrect
def test_login_missing_username(
        driver, browser, mode, device, user):
    """Test attempting to log in with a blank username."""
    login_page = LoginPage(driver)
    login_page.login(user["username"], user["password"])
    assert login_page.error_message_exists()
    print(login_page.get_error_message_text())
    print("test_login_missing_username finished successfully.")


@pytest.mark.parametrize(
    "browser, mode, device, user",
    [
        (*CHROME_MOBILE, LoginCreds.EMPTY_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.EMPTY_PASSWORD),
    ],
)
@pytest.mark.login
@pytest.mark.login_nopassword
def test_login_missing_password(
        driver, browser, mode, device, user):
    """Test attempting to log in with a blank password."""
    login_page = LoginPage(driver)
    login_page.login(user["username"], user["password"])
    assert login_page.error_message_exists()
    print(login_page.get_error_message_text())
    print("test_login_missing_password finished successfully.")
