from page_objects.BasePage import BasePage
from utilities.DriverEventListener import logger

main_top_links = {'css': '#top-links'}

user_link = {'css': '#top-links > ul > li.dropdown > a[title="My Account"]'}

user_link_open = {'css': "#top-links > ul > li.dropdown.open > a"}

class MainPage(BasePage):
    def account_btn_click(self):
        self._click(user_link)

    def is_expanded(self):
        try:
            self._get_element_attribute(user_link_open, attr='aria-expanded')
        except AttributeError:
            logger.exception("element not expanded")

