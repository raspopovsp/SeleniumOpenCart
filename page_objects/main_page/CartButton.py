from page_objects.BasePage import BasePage

cart = {"css": "#cart"}
cart_total = {'css': '#cart-total'}

cart_dropdown_menu = {'css': '#cart>ul.dropdown-menu'}


class CartButton(BasePage):

    def click(self):
        self._click(cart)

    def get_cart_amount(self):
        return self._get_element_text(cart_total)

    def get_currency(self):
        cart_amount = self.get_cart_amount()
        if "$" in cart_amount:
            currency = '$'
        elif "€" in cart_amount:
            currency = '€'
        else:
            currency = '£'
        return currency

    def is_closed(self):
        status = self._get_element_attribute(cart, attr='class')
        if "open" not in status:
            return True
        else:
            return False

    def is_open(self):
        status = self._get_element_attribute(cart, attr='class')
        if "open" in status:
            return True
        else:
            return False

    def get_text(self):
        return self._get_element_text(cart_dropdown_menu)