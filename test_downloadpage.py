import os
import random
import re
import time

import allure
import autoit

from selenium.common.exceptions import NoSuchElementException
from page_objects.admin import AuthPage, DashboardPage
from page_objects.admin.catalog import DownloadsPage

from utilities.db_connection import connect, delete_row


""""" Загрузка нового файла """
@allure.feature(f'new download')
@allure.story(f'Add new downaload')
def test_new_download(browser):
    driver = browser
    download_name = "1Test name"

    # Количесто записей в таблице. Можно и без базы через gui парсить.
    with allure.step(f'count downloads'):
        db_items_default = len(connect("SELECT * FROM oc_download"))
    with allure.step(f'login auth'):
        AuthPage(driver).login(username='admin', password='admin')
    with allure.step(f'go to Downloads page'): # TODO Вынести переход до нужного блока в Base.
        DashboardPage(driver).navigate_to(dashboard_menu='Catalog', submenu='Downloads')
    with allure.step(f'go to Add download'):
        DownloadsPage(driver).goto_new_download_page()
    with allure.step(f'input download name'):
        DownloadsPage(driver).name_input_fill(download_name)
        # ActionChains(driver).move_to_element(download_name_input).click().send_keys(download_file_name).perform()
    with allure.step(f"Download file with autoIt"):
        DownloadsPage(driver).upload_btn_click()
        """ 
        Тудусик: уйти от autoit ибо headless не заработает.
        С другой стороны похер, задолбал кастомный инпут и тестировать чужой JavaScript не охота. 
        """
        time.sleep(1)
        autoit.win_activate("Открытие")
        autoit.control_focus("Открытие", "Edit1")
        autoit.control_set_text("Открытие", "Edit1",
                                "G:\\Projects\\SeleniumOpenCart\\page_objects\\admin\\catalog\\ruins.jpg")
        time.sleep(1)
        autoit.control_click("Открытие", "Button1")
        time.sleep(1)

    with allure.step(f'accept and save download'):
        driver.switch_to.alert.accept()
        DownloadsPage(driver).save_btn_click()
    with allure.step(f'delete created download form database '):
        # Удаление созданной записи из базы
        db_items_new = len(connect("SELECT * FROM oc_download"))
        last_item_id = connect(
            "SELECT download_id FROM oc_download WHERE download_id=(SELECT max(download_id) FROM oc_download)")
        parsed_id = re.findall("\\d+", str(last_item_id))
        row = ("DELETE FROM oc_download WHERE download_id=%s" % parsed_id[0])
        delete_row(row)
        row_desc = "DELETE FROM oc_download_description WHERE download_id=%s" % parsed_id[0]
        delete_row(row_desc)
    assert db_items_default + 1 == db_items_new


def test_edit_download(browser):
    new_name = f"Edited download name{random.randint(0, 100)} "
    driver = browser
    AuthPage(driver).login(username='admin', password='admin')
    DashboardPage(driver).navigate_to(dashboard_menu='Catalog', submenu='Downloads')

    driver.save_screenshot("G:\\Projects\\SeleniumOpenCart\\REPORTS\\SCREENSHOTS\\Downloadpage\\EditItem.png")
    try:
        DownloadsPage(driver).edit_btn_click()
        DownloadsPage(driver).change_name(value=new_name)
        DownloadsPage(driver).save_btn_click()
        driver.save_screenshot("G:\\Projects\\SeleniumOpenCart\\REPORTS\\SCREENSHOTS\\Downloadpage\\EditedItem.png")
        time.sleep(1)
        if "Success: You have modified downloads!" in DownloadsPage(driver).get_alert_text():
            assert True
        else:
            assert False
    except NoSuchElementException:
        print(NoSuchElementException)


def test_delete_download(browser):
    driver = browser
    """ Создание новой записи в базе данных """
    DownloadsPage.create_new_download()

    AuthPage(driver).login(username='admin', password='admin')
    DashboardPage(driver).navigate_to(dashboard_menu='Catalog', submenu='Downloads')

    """ Количество элементов в таблице до удаления """
    default_count = DownloadsPage(driver).get_downloaded_elements()
    driver.save_screenshot("G:\\Projects\\SeleniumOpenCart\\REPORTS\\SCREENSHOTS\\Downloadpage\\tableItemsBeforeDel.png")

    DownloadsPage(driver).get_select_element().click()
    time.sleep(1)
    is_checked = DownloadsPage(driver).get_select_element()
    if is_checked:
        DownloadsPage(driver).click_delete()
    else:
        raise Exception("Nothing chosen")
    time.sleep(1)
    driver.switch_to.alert.accept()
    new_count = DownloadsPage(driver).get_downloaded_elements()
    driver.save_screenshot("G:\\Projects\\SeleniumOpenCart\\REPORTS\\SCREENSHOTS\\Downloadpage\\tableItemsAfterDel.png")
    assert (default_count - 1) == new_count
