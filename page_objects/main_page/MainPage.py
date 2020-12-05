from selenium.common.exceptions import StaleElementReferenceException

from page_objects.BasePage import BasePage

main_top_links = {'css': '#top-links'}
user_link = {'css': '#top-links > ul > li.dropdown > a[title="My Account"]'}
user_link_open = {'css': "#top-links > ul > li.dropdown.open > a"}
login_link = {'css': '#top-links > ul > li.dropdown.open > ul > li:nth-child(2)'}

user_email = {'css': '#input-email'}
user_pwd = {'css': '#input-password'}

login_btn = {'css': '#content > div > div:nth-child(2) > div > form > .btn-primary'}


class MainPage(BasePage):

    def goto_login(self, url):
        self._goto(url)

    def account_btn_click(self):
        self._click(user_link)

    def is_expanded(self):
        if self._get_element_attribute(user_link_open, attr='aria-expanded') == 'true':
            return True
        else:
            return False

    def login_link_click(self):
        self._click(login_link)

    def login(self, email):
        self._input(user_email, email)

    def passwd(self, pwd):
        self._input(user_pwd, pwd)

    def login_btn_click(self):
        self._click(login_btn)
