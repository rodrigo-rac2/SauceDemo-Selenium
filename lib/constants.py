# Python Version: 3.9.6
# Author: Rodrigo Alves Costa
# Date: Oct 10, 2023

"""Constant variables used throughout the framework"""
from enum import Enum
from selenium import webdriver


class Mode(Enum):
    """Browsers modes used for test fixtures."""
    HEADLESS = "headless"
    MOBILE = "mobile"
    DESKTOP = "desktop"


# Devices
IPHONE_X = "iPhone X"

# Webdrivers
CHROME_MOBILE = (webdriver.Chrome, Mode.MOBILE, IPHONE_X)
CHROME_DESKTOP = (webdriver.Chrome, Mode.DESKTOP, None)
CHROME_HEADLESS = (webdriver.Chrome, Mode.HEADLESS, None)
FIREFOX_HEADLESS = (webdriver.Firefox, Mode.HEADLESS, None)
DEFAULT = CHROME_HEADLESS

# URL
URL = "https://www.saucedemo.com/"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
