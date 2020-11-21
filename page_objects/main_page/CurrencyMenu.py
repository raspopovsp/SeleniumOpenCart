from page_objects.BasePage import BasePage

nav_top = {"css": "nav@top"}
form_currency = {"css": "#form-currency"}
currency_button = {"css": form_currency['css'] + " .btn-group"}
currency_menu = {"css": currency_button['css'] + ' .dropdown-menu'}
currency_menu_item = {"css": currency_menu['css'] + ' .currency-select'}


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

    def get_dropdown_menu(self):
        menu = self._get_elements_list(currency_menu_item)
        return menu

    def change_currency(self, number):
        menu = self._get_elements_list(currency_menu_item)
        try:
            menu[number].click()
        except IndexError:
            print("There is no such currency in menu, '$' chosen")
            return menu[2].click()
    #
    # def change_currency(self):
    #     currency = self.get_currency()
    #     print("currency", currency)
    #     menu = self.get_dropdown_menu()
    #     for item in menu:
    #         print('loop - ', item.text)
    #         if item.text not in currency:
    #             print("Переключение валюты", item.text + ' not ' + currency)
    #             item.click()
    #             break
    #         else:
    #             print("Валюта совпадает с пунктом меню", item.text + ' equal ' + currency)
    #             menu[2].click()
    #             time.sleep(5)
