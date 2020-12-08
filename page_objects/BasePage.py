from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as actions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities import loggerconf
import logging


class BasePage:
    log = loggerconf.loggen(logging.INFO)

    def __init__(self, driver, wait=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)

    """ метод для просмотра аттрибутов элемента в отладочных целях """
    @staticmethod
    def get_element_attributes(element):
        attrs = []
        for attr in element.get_property('attributes'):
            attrs.append([attr['name'], attr['value']])
        return attrs

    def _goto(self, url):
        return self.driver.get(url)

    def _element(self, selector: dict, index: int, link_text: str = None):
        by = None
        element = None
        if 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        elif link_text:
            by = By.LINK_TEXT
        elif 'tag' in selector.keys():
            by = By.TAG_NAME
            selector = selector['tag']
        try:
            element = self.driver.find_elements(by, selector)[index]
            self.log.info(f'Element with locator: {str(selector)} found')
        except (NoSuchElementException, IndexError):
            self.log.info(f'Element with {selector} not found')
        return element

    def _get_elements_list(self, selector: dict):
        by = None
        elems = None
        if 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        try:
            elems = self.driver.find_elements(by, selector)
            self.log.info(f'Elements with locator: {str(selector)} found')
        except NoSuchElementException:
            self.log.exception(f"Elements by {selector} not found")
        return elems

    def _click(self, selector, index=0):
        # actions(self.driver).move_to_element(self._element(selector, index)).click().perform()
        try:
            element = self._element(selector, index)
            element.click()
            self.log.info(f'Element with locator: {str(selector)} clicked')
        except NoSuchElementException:
            self.log.info(f'Element with {selector} not found')

    def _input(self, selector, value, index=0):
        try:
            self.log.info(f'Input with locator: {str(selector)} found')
            element = self._element(selector, index)
            element.clear()
            element.send_keys(value)
            self.log.info(f'Input {selector} filled with {value}')
        except NoSuchElementException:
            self.log.info(f'Element with {selector} not found')

    def _wait_for_visible(self, selector, link_text=None, index=0, wait=3):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self._element(selector, index, link_text)))

    def _get_element_text(self, selector, index=0):
        text = None
        try:
            text = self._element(selector, index).text.strip()
            self.log.info(f'Text {text} from {selector} captured')
        except NoSuchElementException:
            self.log.exception(f"Element {selector} not found")
        return text

    def _get_element_attribute(self, selector, attr):
        elem = None
        try:
            elem = self._wait_for_visible(selector)
            self.log.info(f"Element with attr = {elem.get_attribute(attr)} found")
        except NoSuchElementException:
            self.log.info(f"Element with attr = {elem.get_attribute(attr)} not found")
        return elem.get_attribute(attr)
