from page_objects.admin import AuthPage
from utilities.loggerconf import LogGen

logger = LogGen.loggen(__name__)


def sleep_test_login_page_init():
    logger.warning("TEST FOR LOGIN PAGE INITIATED")


""" Проверка на соответствие лейбла Username """
def sleep_test_username_label(browser):
    driver = browser
    AuthPage(driver).goto_login_page()
    if "Username" == AuthPage(driver).get_username_input_label():
        logger.info("LOGIN SUCCESSFUL")
        assert True
    else:
        logger.exception("LOGIN DECLINE")
        assert False

""" Проверка на соответствие лейбла Password """
def sleep_test_password_label(browser):
    driver = browser
    AuthPage(driver).goto_login_page()
    assert "Password" == AuthPage(driver).get_password_input_label()


""" Проверка плейсхолдера Username """
def sleep_test_username_placeholder(browser):
    driver = browser
    print(AuthPage(driver).get_username_input_placeholder())
    assert "Username" == AuthPage(driver).get_username_input_placeholder()


""" Проверка плейсхолдера Password """
def sleep_test_password_placeholder(browser):
    driver = browser
    AuthPage(driver).goto_login_page()
    assert "Password" == AuthPage(driver).get_password_input_placeholder()


""" Проверка плейсхолдера Email """
def sleep_text_email_input_placeholder(browser):
    driver = browser
    AuthPage(driver).goto_login_page()
    assert "E-Mail Address" in AuthPage(driver).get_email_input_placeholder()


""" позитивный тест на авторицацию с проверкой по URLу перехода """
def sleep_test_login_positive(browser):
    driver = browser
    admin_url = AuthPage.get_admin_panel_url()
    AuthPage(driver).login(username="admin", password="admin")
    if admin_url in driver.current_url:
        assert True
    else:
        assert False


""" Переход на страницу восстановление пароля с проверкой URLа перехода """
def sleep_test_restore_btn_navigate(browser):
    driver = browser
    restore_url = AuthPage.get_pass_restore_url()
    AuthPage(driver).goto_login_page()
    AuthPage(driver).goto_pass_restore()
    assert restore_url == driver.current_url


""" Позитивный тест на срабатывание кноки восстановление пароля и проверки появления alert success"""
def sleep_test_password_restoration(browser):
    driver = browser
    AuthPage(driver).goto_login_page()
    AuthPage(driver).reset_pwd("email@email.com")
    alert = AuthPage(driver).get_alert_success()
    default_alert_success_text = AuthPage.get_alert_success_text()
    #logger.warning("PASSWORD RESTORATION SUCCESSFUL")
    assert default_alert_success_text in alert.text


""" Негативный тест восстановления пароля и проверки появления alert success"""
def sleep_test_password_restoration_with_wrong_email(browser):
    driver = browser
    AuthPage(driver).goto_login_page()
    AuthPage(driver).reset_pwd("wrong@email")
    alert = AuthPage(driver).get_alert_danger()
    default_alert_danger_text = AuthPage.get_alert_danger_text()
    assert default_alert_danger_text in alert.text


""" Тест кнопки Отмена с проверкой URLа перехода """
def sleep_test_cancel_password_restoration(browser):
    driver = browser
    AuthPage(driver).goto_login_page()
    AuthPage(driver).goto_pass_restore()
    AuthPage(driver).cancel_btn_click()
    assert "common/login" in driver.current_url



