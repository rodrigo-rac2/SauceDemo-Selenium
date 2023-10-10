# Python Version: 3.9.6
# Author: Rodrigo Alves Costa
# Date: Oct 10, 2023

"""Constants for login credentials"""
STANDARD_USER = {
    "username": "standard_user",
    "password": "secret_sauce",
}

LOCKED_OUT_USER = {
    "username": "locked_out_user",
    "password": "secret_sauce",
}

INVALID_USER = {
    "username": "invalid_user",
    "password": "invalid_password",
}

EMPTY_USERNAME = {
    "username": "",
    "password": "secret_sauce",
}

EMPTY_PASSWORD = {
    "username": "standard_user",
    "password": "",
}

SQL_INJECTION_USER = {
    "username": "not a user",
    "password": "'); DROP TABLE *;--",
}
