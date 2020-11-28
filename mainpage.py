import time

import pytest
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from page_objects.main_page import SearchField, CartButton, CurrencyMenu, ProductCard, MainPage
from utilities.loggerconf import LogGen

logger = LogGen.loggen(__name__)

@pytest.mark.skip(reason='Чтоб не мешался')
def test_mainpage_url(browser):
    driver = browser
    logger.warning("=============MAIN PAGE TEST START===============")
    if "http://localhost/index.php" == driver.current_url:
        logger.warning(f"URL = {driver.current_url}")
        assert True
    else:
        logger.error(f"URL = {driver.current_url}")
        assert False


""" Проверка строки поиска """
@pytest.mark.skip(reason='Чтоб не мешался')
@pytest.mark.parametrize("values", ['iphone', 'Book', "3"])
def test_search_field(browser, values):
    logger.info("%s SEARCH FIELD TEST", values)
    driver = browser
    SearchField(driver).fill(values)
    SearchField(driver).click()
    driver.save_screenshot(f'./REPORTS/SCREENSHOTS/Mainpage/{values}search.png')

    assert values in driver.current_url


""" Сумма заказа равна 0, без авторизации """
@pytest.mark.skip(reason='Чтоб не мешался')
def test_cart_amount_equal_zero_when_logout(browser):
    driver = browser
    cart_total_amount = CartButton(driver).get_cart_amount()
    assert '0 item(s) - $0.00' in cart_total_amount


""" Меню корзины закрыто по умолчанию """
@pytest.mark.skip(reason='Чтоб не мешался')
def test_cart_button_closed_by_default(browser):
    driver = browser
    assert CartButton(driver).is_closed() == True


""" При клике на кнопку "Корзина", появляется выпадающий список  """
@pytest.mark.skip(reason='Чтоб не мешался')
def test_cart_button_opened_after_click(browser):
    driver = browser
    CartButton(driver).click()
    assert CartButton(driver).is_open() == True


"""  В выпадаеющем меню "Корзина" нет товаров, если пользователь не авторизован """
@pytest.mark.skip(reason='Чтоб не мешался')
def test_cart_dropdown_menu_empty_when_logout(browser):
    driver = browser
    if CartButton(driver).is_closed():
        CartButton(driver).click()
    else:
        print("cart is opened")
        pass
    assert CartButton(driver).get_cart_dropdown_text() == "Your shopping cart is empty!"


"""" Меню выбора валюты закрыто по умолчанию """
@pytest.mark.skip(reason='Чтоб не мешался')
def test_currency_menu_is_closed_by_default(browser):
    driver = browser
    status = CurrencyMenu(driver).is_closed()
    assert status == True


""" Валюта в меню Валюта, в аннотации Корзины и на карточках товаров совпадает """
@pytest.mark.skip(reason='Чтоб не мешался')
def test_currency_equals(browser):
    driver = browser
    currency_menu = CurrencyMenu(driver).get_currency()
    cart_currency = CartButton(driver).get_currency()
    product_card_currency = ProductCard(driver).get_currency()
    assert cart_currency == currency_menu == product_card_currency


""" При смене валюты, меняется валюта во всех позициях, где показана  """
@pytest.mark.skip(reason='Чтоб не мешался')
def test_currency_change(browser):
    driver = browser
    logger.info("TEST CURRENCY CHANGE")
    default_currency = CurrencyMenu(driver).get_currency()
    default_cart_currency = CartButton(driver).get_currency()
    default_product_card_currency = ProductCard(driver).get_currency()

    if default_currency == default_cart_currency == default_product_card_currency:
        logger.info("currencies equal")
        CurrencyMenu(driver).click()
        CurrencyMenu(driver).change_currency(1)  # TODO Автоматизировать проверку на изначальную волюту
    else:
        raise Exception("Currencies not equal")

    new_currency = CurrencyMenu(driver).get_currency()
    new_cart_currency = CartButton(driver).get_currency()
    new_product_card_currency = ProductCard(driver).get_currency()

    if new_currency == new_cart_currency == new_product_card_currency:
        # FiringDriver не кушает конкатенированные строки
        logger.info(f"{default_currency} != {new_cart_currency}")
        logger.info("new currencies equal")
        logger.info("currencies change successful")
        assert default_currency != new_currency
    else:
        logger.exception("currencies change test fail")
        assert False


""" Добавление в корзину авторизованным пользователем. Через раздел Featured главного экрана """
@pytest.mark.skip(reason='Чтоб не мешался')
def test_account_btn_click(browser):
    driver = browser
    MainPage(driver).account_btn_click()
    if MainPage(driver).is_expanded():
        logger.info("Menu expanded")
        assert True
    else:
        logger.exception("Menu closed")
        assert False

@pytest.mark.skip(reason='Чтоб не мешался')
def test_navigate_to_auth_page(browser):
    driver = browser
    try:
        MainPage(driver).account_btn_click()
        MainPage(driver).login_link_click()
        logger.info("navigate to auth page successful")
        assert "account/login" in driver.current_url
    except StaleElementReferenceException:
        logger.exception(f"Menu elem doesn't exist{StaleElementReferenceException}")
        assert False

@pytest.mark.skip(reason='Чтоб не мешался')
def test_user_login(browser):
    driver = browser
    url = "http://localhost/index.php?route=account/login"
    MainPage(driver).goto_url(url)
    try:
        MainPage(driver).input_email(email='test@test.com')
        MainPage(driver).input_pwd(pwd='password')
        driver.save_screenshot('./REPORTS/SCREENSHOTS/Mainpage/userlogin.png')
        MainPage(driver).login_btn_click()
        if driver.title == "My Account":
            logger.warning("USER LOGIN SUCCESSFUL")
            assert True
        else:
            logger.exception("USER LOGIN DECLINE")
            assert False
    except NoSuchElementException:
        logger.exception('inputs not found', NoSuchElementException)

#def test_forgotten_pwd(browser):