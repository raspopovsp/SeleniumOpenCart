import os

from page_objects.BasePage import BasePage

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

class DownloadsPage(BasePage):
    def goto_new_download_page(self):
        self._click(add_new_btn)

    def _get_form_inputs(self):
        return self._get_elements_list(form_inputs)

    def get_name_input(self):
        return self._get_form_inputs()[0]

    def get_filename_input(self):
        return self._get_form_inputs()[1]

    def get_mask_input(self):
        return self._get_form_inputs()[2]

    def get_downloads_list_element_text(self):
        return self._get_element_text(download_files_table_element)

    def get_download_name_input_value(self):
        name_input = self.get_name_input()
        value = name_input.find_element_by_css_selector(".input-group > input.form-control")\
            .get_attribute('value')
        return value

    def upload_btn_click(self):
        self._click(upload_new_btn)

    def save_btn_click(self):
        self._click(save_btn)

    def edit_btn_click(self):
        self._click(edit_btn)

    def download_name_input_change(self, value):
        input_el = self.driver.find_element_by_css_selector("#form-download > div:nth-child(1) > div > div > input")
        input_el.clear()
        input_el.send_keys(value)

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

    def click_del_btn(self):
        self._click(delete_btn)

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
    #     filename = os.path.join(dirname, "ruins.jpg")
    #     input_manager = self.driver.find_element_by_css_selector('input[name="file"]')
    #     print(filename)
    #     input_manager.send_keys(filename)
