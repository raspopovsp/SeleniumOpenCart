from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.BasePage import BasePage

menu = {'css': '#menu'}
menu_li = {'css': menu['css'] + ' >li'}
submenu_list = {'css': menu_li['css'] + ' > ul'}

menu_list_id = {
    'Dashboard': 'menu-dashboard',
    'Catalog': 'menu-catalog',
    'Extension': 'menu-extension',
    'Design': 'menu-design',
    'Sales': 'menu-sale',
    'Customers': 'menu-customers',
    'Marketing': 'menu-marketing',
    'System': 'menu-system',
    'Report': 'menu-report'
}


class DashboardPage(BasePage):

    def _get_menu(self):
        return self._get_elements_list(menu_li)

    def get_menu_item(self, menu_option):
        menu_item = None
        for item in self._get_menu():
            if item.get_attribute('id') == menu_list_id[menu_option]:
                menu_item = item
                break
        return menu_item

    def get_submenu_item(self, main_menu, submenu_option):
        submenu_item = None
        submenu = main_menu.find_elements_by_css_selector('li')
        for item in submenu:
            if submenu_option in item.text:
                submenu_item = item
                break
        return submenu_item
