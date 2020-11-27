import os
import time

import autoit
from selenium.webdriver import ActionChains
from page_objects.admin import AuthPage, DashboardPage
from page_objects.admin.catalog import DownloadsPage

# def sleep_test_download_page_url(browser):
#     driver = browser
#     AuthPage(driver).login(username='admin', password='admin')
#     menu_catalog = DashboardPage(driver).get_menu_item(menu_option="Catalog")
#     menu_catalog.click()
#     submenu = DashboardPage(driver).get_submenu_item(menu_catalog, submenu_option="Downloads")
#     WebDriverWait(driver, 3).until(EC.visibility_of(submenu))
#     submenu.click()
#     assert "catalog/download" in driver.current_url


""" Загрузка нового файла """


def sleep_test_new_item_download(browser):
    driver = browser

    download_file_name = "1Test name"

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

    print(f'Download page {driver.current_window_handle}')

    download_name_input = DownloadsPage(driver).get_name_input()
    ActionChains(driver).move_to_element(download_name_input).click().send_keys(download_file_name).perform()

    DownloadsPage(driver).upload_btn_click()

    """ 
    Тудусик: уйти от autoit потому что на линуксе не заработает.
    С другой стороны похер, ибо задолбал кастомный инпут 
    """
    autoit.win_activate("Открытие")
    autoit.control_focus("Открытие", "Edit1")
    autoit.control_set_text("Открытие", "Edit1",
                            "G:\\Projects\\SeleniumOpenCart\\page_objects\\admin\\catalog\\ruins.jpg")
    time.sleep(1)
    autoit.control_click("Открытие", "Button1")
    time.sleep(1)

    driver.switch_to.alert.accept()

    # filename_input = DownloadsPage(driver).get_filename_input()
    # ActionChains(driver).move_to_element(filename_input).click().send_keys("Test filename").perform()

    # mask_input = DownloadsPage(driver).get_mask_input()
    # ActionChains(driver).move_to_element(mask_input).click().send_keys("Test mask").perform()

    DownloadsPage(driver).save_btn_click()
    time.sleep(2)

    downloaded_element_name = DownloadsPage(driver).get_downloads_list_element_text()
    assert download_file_name == downloaded_element_name


def sleep_test_edit_downloaded_file(browser):
    new_name = "New download name"

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
    edited_element = DownloadsPage(driver).get_downloads_list_element_text()
    DownloadsPage(driver).edit_btn_click()
    download_name = DownloadsPage(driver).get_download_name_input_value()
    if edited_element == download_name:
        DownloadsPage(driver).download_name_input_change(value=new_name)
    else:
        print("Имена файлов не совпадают")
    DownloadsPage(driver).save_btn_click()
    downloaded_element_name = DownloadsPage(driver).get_downloads_list_element_text()
    time.sleep(1)
    assert new_name == downloaded_element_name


def sleep_test_delete_downloaded_file(browser):
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

    """ Количество элементов в таблице до удаления """
    default_count = DownloadsPage(driver).get_downloaded_elements()

    DownloadsPage(driver).get_select_element().click()
    time.sleep(1)
    is_checked = DownloadsPage(driver).get_select_element()
    if is_checked:
        DownloadsPage(driver).click_del_btn()
    else:
        print("Nothing chosen")
    time.sleep(2)
    driver.switch_to.alert.accept()
    new_count = DownloadsPage(driver).get_downloaded_elements()
    print(new_count)
    assert default_count - 1 == new_count
