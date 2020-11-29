from selenium.common.exceptions import InvalidArgumentException

from page_objects.BasePage import BasePage

nav_top = {"css": "nav@top"}
form_currency = {"css": "#form-currency"}
currency_button = {"css": "#form-currency > .btn-group"}
currency_menu = {"css": "#form-currency > div > ul.dropdown-menu"}


class CurrencyMenu(BasePage):

    def is_open(self):
        status = self._get_element_attribute(currency_button, attr='class')
        if 'open' in status:
            return True
        else:
            return False

    def is_closed(self):
        status = self._get_element_attribute(currency_button, attr='class')
        if 'open' not in status:
            return True
        else:
            return False

    def click(self):
        return self._click(form_currency)

    def get_currency(self):
        currency_form = self._get_element_text(form_currency)
        if "$" in currency_form:
            currency = '$'
        elif "€" in currency_form:
            currency = '€'
        else:
            currency = '£'
        return currency

    def change_currency(self, cur):
        self.click()
        elems = self._get_elements_list(currency_menu)
        for item in elems:
            if cur in item.text:
                item.click()
                break
            else:
                raise Exception("Currency not found")
