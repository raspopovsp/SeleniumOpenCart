from page_objects.BasePage import BasePage
from locators.login_page_locators import LoginPageLocators as locator


class AuthPage(BasePage):

    @staticmethod
    def get_admin_panel_url():
        return locator.login_url + locator.admin_panel_path

    @staticmethod
    def get_pass_restore_url():
        return locator.login_url + locator.forgotten_pass_path

    @staticmethod
    def get_alert_success_text():
        return locator.alert_success_text

    @staticmethod
    def get_alert_danger_text():
        return locator.alert_danger_text

    def goto_login_page(self):
        self.navigate_to(locator.login_url)

    def login(self, username, password):
        self.goto_login_page()
        self._input(locator.username_input, username)
        self._input(locator.password_input, password)
        self._click(locator.submit)

    def get_username_input_placeholder(self):
        return self._get_element_attribute(locator.username_input, "placeholder")

    def get_password_input_placeholder(self):
        return self._get_element_attribute(locator.password_input, "placeholder")

    def get_email_input_placeholder(self):
        return self._get_element_attribute(locator.email_input, "placeholder")

    def goto_pass_restore(self):
        self._click(locator.password_restore_btn)

    def input_email(self, email):
        self._input(locator.email_input, email)

    def reset_btn_click(self):
        self._click(locator.reset_pwd_btn)

    def cancel_btn_click(self):
        self._click(locator.cancel_btn)

    def reset_pwd(self, email):
        self.goto_pass_restore()
        self.input_email(email)
        self.reset_btn_click()

    def get_alert_success(self):
        return self._wait_for_visible(locator.alert_success)

    def get_alert_danger(self):
        return self._wait_for_visible(locator.alert_danger)

    def get_username_input_label(self):
        return self._get_element_text(locator.username_label)

    def get_password_input_label(self):
        return self._get_element_text(locator.password_label)
