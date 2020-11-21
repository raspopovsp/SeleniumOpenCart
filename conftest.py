import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://www.localhost/index.php", help="choose your browser")


@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--kiosk")
        driver = webdriver.Chrome(options=options)
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(20)
    request.addfinalizer(driver.close)
    driver.get(request.config.getoption("--url"))

    return driver
