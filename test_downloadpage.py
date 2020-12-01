import os
import random
import re
import time
import autoit

from selenium.common.exceptions import NoSuchElementException
from page_objects.admin import AuthPage, DashboardPage
from page_objects.admin.catalog import DownloadsPage

from utilities.db_connection import connect, delete_row

""""" Загрузка нового файла """
def test_new_download(browser):
    driver = browser

    download_name = "1Test name"
    # Количесто записей в таблице. Можно и без базы строки парсить.
    db_items_default = len(connect("SELECT * FROM oc_download"))

    AuthPage(driver).login(username='admin', password='admin')
    menu_catalog = DashboardPage(driver).get_menu_item(menu_option="Catalog")
    menu_catalog.click()
    catalog_id = driver.find_element_by_id("collapse1")
    while True:
        if catalog_id.get_attribute("class") != "collapse in":
            continue
        else:
            break
    submenu_item = DashboardPage(driver).get_submenu_item(menu_catalog, submenu_option="Downloads")
    submenu_item.click()  # TODO Вынести переход до нужной страницы в Base.
    DownloadsPage(driver).goto_new_download_page()
    DownloadsPage(driver).name_input_fill(download_name)
    # ActionChains(driver).move_to_element(download_name_input).click().send_keys(download_file_name).perform()
    DownloadsPage(driver).upload_btn_click()
    """ 
    Тудусик: уйти от autoit потому что на линуксе и headless не заработает.
    С другой стороны похер, ибо задолбал кастомный инпут 
    """
    time.sleep(1)
    autoit.win_activate("Открытие")
    autoit.control_focus("Открытие", "Edit1")
    autoit.control_set_text("Открытие", "Edit1",
                            "G:\\Projects\\SeleniumOpenCart\\page_objects\\admin\\catalog\\ruins.jpg")
    time.sleep(1)
    autoit.control_click("Открытие", "Button1")
    time.sleep(1)
    driver.switch_to.alert.accept()
    DownloadsPage(driver).save_btn_click()
    db_items_new = len(connect("SELECT * FROM oc_download"))

    # Удаление созданной записи из базы
    last_item_id = connect(
        "SELECT download_id FROM oc_download WHERE download_id=(SELECT max(download_id) FROM oc_download)")
    parsed_id = re.findall("\\d+", str(last_item_id))
    row = ("DELETE FROM oc_download WHERE download_id=%s" % parsed_id[0])
    delete_row(row)
    row_desc = "DELETE FROM oc_download_description WHERE download_id=%s" % parsed_id[0]
    delete_row(row_desc)
    assert db_items_default + 1 == db_items_new


def test_edit_download(browser):
    new_name = f"New download name{random.randint(0, 100)} "
    driver = browser
    AuthPage(driver).login(username='admin', password='admin')
    menu_catalog = DashboardPage(driver).get_menu_item(menu_option="Catalog")
    menu_catalog.click()
    catalog_id = driver.find_element_by_id("collapse1")
    while True:
        if catalog_id.get_attribute("class") != "collapse in":
            continue
        else:
            break
    submenu_item = DashboardPage(driver).get_submenu_item(menu_catalog, submenu_option="Downloads")
    submenu_item.click()
    driver.save_screenshot("G:\Projects\SeleniumOpenCart\REPORTS\SCREENSHOTS\Downloadpage\EditItem.png")
    try:
        DownloadsPage(driver).edit_btn_click()
        DownloadsPage(driver).change_name(value=new_name)
        DownloadsPage(driver).save_btn_click()
        driver.save_screenshot("G:\Projects\SeleniumOpenCart\REPORTS\SCREENSHOTS\Downloadpage\EditedItem.png")
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
    DownloadsPage._create_new_download()

    AuthPage(driver).login(username='admin', password='admin')
    menu_catalog = DashboardPage(driver).get_menu_item(menu_option="Catalog")
    menu_catalog.click()
    catalog_id = driver.find_element_by_id("collapse1")
    while True:
        if catalog_id.get_attribute("class") != "collapse in":
            continue
        else:
            break
    submenu_item = DashboardPage(driver).get_submenu_item(menu_catalog, submenu_option="Downloads")
    submenu_item.click()

    """ Количество элементов в таблице до удаления """
    default_count = DownloadsPage(driver).get_downloaded_elements()
    driver.save_screenshot("G:\\Projects\\SeleniumOpenCart\\REPORTS\\SCREENSHOTS\\Downloadpage\\tableItemsBeforeDel.png")

    DownloadsPage(driver).get_select_element().click()
    time.sleep(1)
    is_checked = DownloadsPage(driver).get_select_element()
    if is_checked:
        DownloadsPage(driver).click_del_btn()
    else:
        raise Exception("Nothing chosen")
    time.sleep(1)
    driver.switch_to.alert.accept()
    new_count = DownloadsPage(driver).get_downloaded_elements()
    driver.save_screenshot("G:\\Projects\\SeleniumOpenCart\\REPORTS\\SCREENSHOTS\\Downloadpage\\tableItemsAfterDel.png")
    assert (default_count - 1) == new_count
