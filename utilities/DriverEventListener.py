# from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
#
# class CustomEventListener(AbstractEventListener):
#
#     def after_navigate_to(self, url, driver):
#         logger.info(f"GO TO {driver.current_url}")
#
#     def after_find(self, by, value, driver):
#         logger.info(f"element {value} found")
#
#     # after_click выбрасывает ошибку StaleElement. Т.к. меню закрывается после нажатия
#     def before_click(self, element, driver):
#         logger.info(f"{element.text} ready to click")
#
#     def on_exception(self, exception, driver):
#         driver.save_screenshot('../REPORTS/SCREENSHOTS/exception.png')
#         logger.exception(exception, f"EXCEPTION IN {__class__.__name__}")
#
