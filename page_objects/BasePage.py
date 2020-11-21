from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as actions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        return self.driver.get(url)

    def __element(self, selector: dict, index: int, link_text: str = None):
        by = None
        if 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        elif link_text:
            by = By.LINK_TEXT
        return self.driver.find_elements(by, selector)[index]

    def _get_elements_list(self, selector: dict):
        by = None
        if 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.driver.find_elements(by, selector)

    def _click(self, selector, index=0):
        actions(self.driver).move_to_element(self.__element(selector, index)).click().perform()

    def _input(self, selector, value, index=0):
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, link_text=None, index=0, wait=3):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector, index, link_text)))

    def _get_element_text(self, selector, index=0):
        return self.__element(selector, index).text.strip()

    def _get_element_attribute(self, selector, attr, index=0):
        return self.__element(selector, index).get_attribute(attr)

