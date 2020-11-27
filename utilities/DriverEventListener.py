from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

from utilities.loggerconf import LogGen

logger = LogGen.loggen(__name__)


class CustomEventListener(AbstractEventListener):

    def after_navigate_to(self, url, driver):
        logger.info(f"GO TO {driver.current_url}")

    def after_find(self, by, value, driver):
        logger.info(f"element {value} found")

    def after_click(self, element, driver):
        logger.info(f"{element.text} clicked")

    def on_exception(self, exception, driver):
        driver.save_screenshot('../REPORTS/SCREENSHOTS/exception.png')
        logger.exception(exception, f"EXCEPTION IN {__class__.__name__}")

