import time

from page_objects.admin import AuthPage


def sleep_test_login(browser):
    driver = browser
    admin_url = AuthPage.get_admin_panel_url()
    AuthPage(driver).login(username="admin", password="admin")
    assert admin_url in driver.current_url


def sleep_test_username_placeholder(browser):
    driver = browser
    AuthPage(driver).goto_login_page()
    print(AuthPage(driver).get_username_input_placeholder())
    assert "Username" == AuthPage(driver).get_username_input_placeholder()


def sleep_test_password_placeholder(browser):
    driver = browser
    AuthPage(driver).goto_login_page()
    assert "Password" == AuthPage(driver).get_password_input_placeholder()


def sleep_text_email_input_placeholder(browser):
    driver = browser
    AuthPage(driver).goto_login_page()
    assert "E-Mail Address" in AuthPage(driver).get_email_input_placeholder()


def sleep_test_restore_btn_navigate(browser):
    driver = browser
    restore_url = AuthPage.get_pass_restore_url()
    AuthPage(driver).goto_login_page()
    AuthPage(driver).goto_pass_restore()
    assert restore_url == driver.current_url


def sleep_test_password_restoration(browser):
    driver = browser
    AuthPage(driver).goto_login_page()
    AuthPage(driver).reset_pwd("email@email.com")
    alert = AuthPage(driver).get_alert_success()
    default_alert_success_text = AuthPage.get_alert_success_text()
    assert default_alert_success_text in alert.text


def sleep_test_password_restoration_with_wrong_email(browser):
    driver = browser
    AuthPage(driver).goto_login_page()
    AuthPage(driver).reset_pwd("wrong@email")
    alert = AuthPage(driver).get_alert_danger()
    default_alert_danger_text = AuthPage.get_alert_danger_text()
    assert default_alert_danger_text in alert.text


def sleep_test_cancel_password_restoration(browser):
    driver = browser
    AuthPage(driver).goto_login_page()
    AuthPage(driver).goto_pass_restore()
    AuthPage(driver).cancel_btn_click()
    assert "common/login" in driver.current_url


def sleep_test_username_label(browser):
    driver = browser
    AuthPage(driver).goto_login_page()
    assert "Username" == AuthPage(driver).get_username_input_label()


def sleep_test_password_label(browser):
    driver = browser
    AuthPage(driver).goto_login_page()
    assert "Password" == AuthPage(driver).get_password_input_label()

