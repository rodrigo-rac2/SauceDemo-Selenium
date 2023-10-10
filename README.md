# Interview Task: Login/Logout Functionality Tests for www.saucedemo.com

This project demonstrates automated tests for the login/logout functionality of [www.saucedemo.com](https://www.saucedemo.com/). The tests cover both positive and negative cases to provide an optimal level of coverage. This task is part of an interview process and should be completed within 1.5 hours.

This project was developed using Python 3.9.6.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup](#setup)
- [Running Tests](#running-tests)
- [Results](#results)
- [Repository Link](#repository-link)

## Project Structure

The project is structured as follows:

- `drivers`: Contains the Chromedriver executable for Selenium testing.
- `lib`: Contains modules for login credentials (`login_credentials.py`) and error messages (`login_error_messages.py`).
- `pages`: Contains the `LoginPage` class, which provides page object methods for interacting with the login page.
- `tests`: Contains the test cases for login/logout functionality (`test_login.py`).

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/rodrigo-rac2/saucedemo-selenium.git
    ```
   
2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running Tests
To run the tests, execute the following command from the root directory of the project:
   
   ```bash
   python -m pytest -c selenium_config.cfg
   ```

This config has reporting enabled. If you want to generate a report, run the tests with (the `log` directory isn't shared through git):
    
   ```bash
   python -m pytest -c selenium_config.cfg --html=./log/report.html
   ```

You can also enable parallel execution by adding the `-n` flag:
   
   ```bash
   python -m pytest -c selenium_config.cfg -n 2
   ```

Or you can run the tests using the `run_tests.sh` script:
   ```bash
    ./run_tests.sh
   ```

Feel free to check the selenium_config.cfg file and check for the markdowns, so you can run tagged tests such as:
   ```bash
    ./run_tests.sh login
   ```

## Results
The test results will be displayed in the terminal, showing the status of each test case. Successful login tests should result in the URL containing "inventory," indicating a successful login. Any failed tests will provide error messages.

## Repository Link
The repository for this project is available on GitHub at the following repository:
[SauceDemo-Selenium](https://github.com/rodrigo-rac2/saucedemo-selenium/)

Feel free to explore the code, run the tests, and review the project structure.
