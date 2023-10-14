# Python Version: 3.9.6
# Author: Rodrigo Alves Costa
# Date: Oct 10, 2023

"""Test configuration for pytest."""
import time
import pytest

from selenium import webdriver
from lib.constants import Mode


@pytest.fixture
def driver(request, browser, mode, device):
    """Creates test fixtures for pytest."""
    if browser == webdriver.Chrome:
        options = webdriver.ChromeOptions()
        if mode == Mode.MOBILE:
            mobile_emulation = {"deviceName": device}
            options.add_experimental_option(
                "mobileEmulation", mobile_emulation
            )
            options.set_capability("browserName", "iPhone")
        else:
            options.set_capability("browserName", "chrome")

        web_driver = webdriver.Remote(
            command_executor='http://localhost:4444',
            options=options
        )
    elif browser == webdriver.Firefox:
        options = webdriver.FirefoxOptions()
        options.set_capability("browserName", "firefox")
        web_driver = webdriver.Remote(
            command_executor='http://localhost:4444',
            options=options
        )
    else:
        raise NameError("Unsupported browser: %s" % browser)

    web_driver.delete_all_cookies()

    # Close/quit browser after the test is completed.
    request.addfinalizer(lambda *args: mac_finalizer(web_driver))
    return web_driver


def mac_finalizer(web_driver):
    """Close/quit browser after the test is completed."""
    web_driver.close()
    web_driver.quit()
    time.sleep(2)
