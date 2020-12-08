import allure
import pytest
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from page_objects.main_page import SearchField, CartButton, CurrencyMenu, ProductCard, MainPage


def test_main_page_url(browser):
    driver = browser
    if "http://localhost/index.php" == driver.current_url:
        assert True
    else:
        assert False


""" Проверка строки поиска """
@allure.feature("main search field")
@allure.story("search parametrized tests")
@pytest.mark.parametrize("values", ['iphone', 'Book', "3"])
def test_search_field(browser, values):
    driver = browser
    with allure.step(f'search for {values}'):
        SearchField(driver).fill(values)
        SearchField(driver).click()
        driver.save_screenshot(f'./REPORTS/SCREENSHOTS/Mainpage/{values}search.png')
    with allure.step(f'{values} отображается в URL params'):
        if values in driver.current_url:
            assert True
        else:
            assert False


""" Сумма заказа равна 0, без авторизации """
@allure.feature("cart button tests")
@allure.story("Cart empty by default")
def test_cart_amount_equal_zero_when_logout(browser):
    driver = browser
    cart_total_amount = CartButton(driver).get_cart_amount()
    if '0 item(s) - $0.00' in cart_total_amount:
        assert True
    else:
        assert False


""" Меню корзины закрыто по умолчанию """
@allure.feature("cart button tests")
@allure.story("Cart closed by default")
def test_cart_button_closed_by_default(browser):
    driver = browser
    if CartButton(driver).is_closed():
        assert True
    else:
        assert False


""" меню "Корзина" расхлопывается по нажатию """
@allure.feature("cart button tests")
@allure.story("Cart opend by default")
def test_cart_button_opened_after_click(browser):
    driver = browser
    with allure.step(f'cart button click'):
        CartButton(driver).click()
    with allure.step(f'cart shown'):
        if CartButton(driver).is_open():
            assert True
        else:
            assert False


"""  В выпадаеющем меню "Корзина" нет товаров, если пользователь не авторизован """
def test_cart_dropdown_menu_empty_when_logout(browser):
    driver = browser
    if CartButton(driver).is_closed():
        CartButton(driver).click()
        assert CartButton(driver).get_text() == "Your shopping cart is empty!"
    else:
        print("cart is opened")
        assert False


""" Валюта в меню Валюта, в аннотации Корзины и на карточках товаров совпадает """
@allure.feature("currency tests")
@allure.story("currencies equality test")
def test_currency_equals(browser):
    driver = browser
    with allure.step(f'get currencies from diff points'):
        currency_menu = CurrencyMenu(driver).get_currency()
        cart_currency = CartButton(driver).get_currency()
        product_card_currency = ProductCard(driver).get_currency()
    with allure.step(f'check currencies equality'):
        if cart_currency == currency_menu == product_card_currency:
            assert True
        else:
            assert False


"""" Меню выбора валюты закрыто по умолчанию """
@allure.feature("currency tests")
@allure.story("Currency menu closed by default")
def test_currency_menu_is_closed_by_default(browser):
    driver = browser
    if CurrencyMenu(driver).is_closed():
        assert True
    else:
        assert False


""" При смене валюты, меняется валюта во всех позициях, где показана  """
@allure.feature("currency tests")
@allure.story("Change currency")
def test_currency_change(browser):
    driver = browser
    with allure.step(f'get default currency'):
        default_currency = CurrencyMenu(driver).get_currency()
    with allure.step(f'chenge currency'):
        CurrencyMenu(driver).change_currency("£ Pound Sterling")
    with allure.step(f'get new currency'):
        new_currency = CurrencyMenu(driver).get_currency()
    # FiringDriver не кушает конкатенированные строки
    with allure.step(f'compare currencies'):
        if default_currency != new_currency:
            assert True
        else:
            assert False


"""Меню Account расхолопывается """
@allure.feature("user login")
@allure.story("account menu successful expanded")
def test_account_btn_click(browser):
    driver = browser
    MainPage(driver).account_btn_click()
    if MainPage(driver).is_expanded():
        assert True
    else:
        assert False

""" Тест перехода к форме авторизации """
@allure.feature("user login")
@allure.story("account/login page exists test")
def test_navigate_to_auth_page(browser):
    driver = browser
    try:
        MainPage(driver).account_btn_click()
        MainPage(driver).login_link_click()
        if "account/login" in driver.current_url:
            assert True
        else:
            assert False
    except StaleElementReferenceException:
        assert False


""" Авторизация пользователя """
@allure.feature("user login")
@allure.story("User login login positive")
def test_user_login(browser):
    driver = browser
    url = "http://localhost/index.php?route=account/login"
    with allure.step(f'navigate to user login page'):
        MainPage(driver).goto_login(url)
    try:
        with allure.step(f'input username'):
            MainPage(driver).login(email='test@test.com')
        with allure.step(f'input password'):
            MainPage(driver).passwd(pwd='password')
        with allure.step(f'login'):
            MainPage(driver).login_btn_click()
        with allure.step(f'Проверка Title на соответствие'):
            if driver.title == "My Account":
                assert True
            else:
                assert False
    except NoSuchElementException:
        assert False
