import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.events import EventFiringWebDriver

from utilities.DriverEventListener import CustomEventListener


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://localhost/index.php", help="choose your browser")


@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--kiosk")
        driver = webdriver.Chrome(options=options)
        ef_driver = EventFiringWebDriver(driver, CustomEventListener())
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
        ef_driver = EventFiringWebDriver(driver, CustomEventListener())
        ef_driver.maximize_window()
    else:
        raise Exception(f"{request.param} is not supported!")

    ef_driver.implicitly_wait(20)
    request.addfinalizer(ef_driver.close)
    ef_driver.get(request.config.getoption("--url"))

    return ef_driver
