import time

import pytest

from page_objects.main_page import SearchField, CartButton, CurrencyMenu, ProductCard


""" Проверка строки поиска """
@pytest.mark.parametrize("values" , ['iphone', 'Book', "2"])
def sleep_test_search_field(browser, values):
    driver = browser
    SearchField(driver).fill(values)
    SearchField(driver).click()
    assert values in driver.current_url


""" Сумма заказа равна 0, без авторизации """
def sleep_test_cart_amount_equal_zero_when_logged_out(browser):
    driver = browser
    cart_total_amount = CartButton(driver).get_cart_amount()
    assert '0 item(s) - $0.00' in cart_total_amount

""" Меню корзины закрыто по умолчанию """
def sleep_test_cart_button_closed_by_default(browser):
    driver = browser
    assert CartButton(driver).is_closed() == True

""" При клике на кнопку "Корзина", появляется выпадающий список  """
def sleep_test_cart_button_opened_after_click(browser):
    driver = browser
    CartButton(driver).click()
    assert CartButton(driver).is_open() == True

"""  В выпадаеющем меню "Корзина" нет товаров, если пользователь не авторизован """
def sleep_test_cart_dropdown_menu_empty_when_logged_out(browser):
    driver = browser
    if CartButton(driver).is_closed():
        CartButton(driver).click()
    else:
        print("cart is opened")
        pass
    assert CartButton(driver).get_cart_dropdown_text() == "Your shopping cart is empty!"

"""" Меню выбора валюты закрыто по умолчанию """
def sleep_test_currency_menu_is_closed_by_default(browser):
    driver = browser
    status = CurrencyMenu(driver).is_closed()
    assert status == True

""" Валюта в меню Валюта, в аннотации Корзины и на карточках товаров совпадает """
def sleep_test_currency_equals(browser):
    driver = browser
    currency_menu = CurrencyMenu(driver).get_currency()
    cart_currency = CartButton(driver).get_currency()
    product_card_currency = ProductCard(driver).get_currency()
    assert cart_currency == currency_menu == product_card_currency

""" При смене валюты, меняется валюта во всех позициях, где показана  """
def sleep_test_currency_change(browser):
    driver = browser
    default_currency = CurrencyMenu(driver).get_currency()
    default_cart_currency = CartButton(driver).get_currency()
    default_product_card_currency = ProductCard(driver).get_currency()

    if default_currency == default_cart_currency == default_product_card_currency:
        CurrencyMenu(driver).click()
        CurrencyMenu(driver).change_currency(1)  # TODO Автоматизировать проверку на изначальную волюту
    else:
        raise Exception("Currencies not equal")

    new_currency = CurrencyMenu(driver).get_currency()
    new_cart_currency = CartButton(driver).get_currency()
    new_product_card_currency = ProductCard(driver).get_currency()

    if new_currency == new_cart_currency == new_product_card_currency:
        print(default_currency, ' != ', new_currency)
        assert default_currency != new_currency
    else:
        raise Exception("New currencies not equal")
