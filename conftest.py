import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="browser choice")
    parser.addoption("--url", "-U", action="store", default="http://localhost/index.php", help="url basic")


@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        options = Options()
        # options.add_argument("--headless")
        # options.add_argument("--kiosk")
        driver = webdriver.Chrome(options=options)
    elif browser_param == "firefox":
        capabilities = webdriver.DesiredCapabilities().FIREFOX
        capabilities['acceptSslCerts'] = False
        driver = webdriver.Firefox(capabilities=capabilities)
        driver.maximize_window()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(10)
    request.addfinalizer(driver.close)
    driver.get(request.config.getoption("--url"))

    return driver
