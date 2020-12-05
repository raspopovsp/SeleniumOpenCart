import re

from page_objects.BasePage import BasePage
from utilities.db_connection import connect, delete_row, insert_row

download_files_table_element = {'css': 'tbody > tr > .text-left'}
edit_btn = {'css': 'tbody > tr > td > a.btn-primary'}

add_new_btn = {'tag': 'a[data-original-title="Add New"]'}
delete_btn = {'tag': 'button[data-original-title="Delete"]'}
save_btn = {'tag': 'button[data-original-title="Save"]'}
cancel_btn = {'tag': 'a[data-original-title="Cancel"]'}

download_form = {'css': 'panel-body > form.form-horizontal'}
form_inputs = {'css': '.panel-body > form.form-horizontal > .form-group'}
upload_new_btn = {'css': '#button-upload'}

download_list = {'css': '#form-download > div > table > tbody > tr'}

name_input = {'css': "#form-download > div:nth-child(1) > div > div > input"}
alert_success = {'css': '#content > .container-fluid > div.alert.alert-success.alert-dismissible'}


class DownloadsPage(BasePage):
    @staticmethod
    def create_new_download():
        insert_row(
            "INSERT INTO oc_download(download_id, filename, mask, date_added) VALUES (DEFAULT, 'Ясделие.jpg.123', 'MaskDB', CURRENT_TIMESTAMP())")
        new_download_id = connect(
            "SELECT download_id FROM oc_download WHERE download_id=(SELECT max(download_id) FROM oc_download)")
        new_download_id_parsed = re.findall("\\d+", str(new_download_id))
        complete_req = "INSERT INTO oc_download_description(download_id, language_id, name) VALUES (%s, %s, '%s')" % (
            *new_download_id_parsed, 1, '11FromDB')
        print(complete_req)
        insert_row(complete_req)

    def goto_new_download_page(self):
        self._click(add_new_btn)

    def _get_form_inputs(self):
        return self._get_elements_list(form_inputs)

    def get_alert_text(self):
        return self._get_element_text(alert_success)

    def get_name_input(self):
        return self._get_form_inputs()[0]

    def name_input_fill(self, value):
        return self._input(name_input, value)

    def get_filename_input(self):
        return self._get_form_inputs()[1]

    def get_mask_input(self):
        return self._get_form_inputs()[2]

    def get_table_element_text(self):
        return self._get_element_text(download_files_table_element)

    def get_name_input_value(self):
        name_input = self.get_name_input()
        value = name_input.find_element_by_css_selector(".input-group > input.form-control") \
            .get_attribute('value')
        return value

    def upload_btn_click(self):
        self._click(upload_new_btn)

    def save_btn_click(self):
        self._click(save_btn)

    def edit_btn_click(self):
        self._click(edit_btn)

    def change_name(self, value):
        return self._input(name_input, value)

    def get_downloaded_elements(self):
        rows = []
        table = self._get_elements_list(download_list)
        for row in table:
            rows.append(row)
        return len(rows)

    def get_first_element(self):
        table = self._get_elements_list(download_list)
        return next(iter(table))

    def get_select_element(self):
        row = self.get_first_element()
        return row.find_element_by_tag_name("td.text-center > input[type=checkbox]")

    def click_delete(self):
        self._click(delete_btn)

    # Для работы скрипта в папке Storage/Downloads должен лежать файл с именем добавленным при создании.
    # Иначе не подтягивает данные.
    # def make_download_input_visible(self):
    #     self.driver.execute_script(
    #         """
    #             const form = document.createElement("form");
    #             form.id = "form-upload";
    #             form.style.display = "block";
    #             form.enctype = "multipart/form-data";
    #             input = document.createElement("input");
    #             input.type = "file"
    #             input.name = "file"
    #             form.appendChild(input)
    #             body = document.getElementsByTagName("body")[0];
    #             body.insertBefore(form, body.firstChild);
    #         """
    #     )
    #
    # def download_file(self):
    #     dirname = os.path.dirname(__file__)
    #     print(dirname)
    #     filename = os.path.join(dirname, "Ясделие.jpg.123")
    #     input_manager = self.driver.find_element_by_css_selector('input[name="file"]')
    #     print(filename)
    #     input_manager.send_keys(filename)
