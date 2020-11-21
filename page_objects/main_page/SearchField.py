from page_objects.BasePage import BasePage


class SearchField(BasePage):

    bar = {"css": "input.input-lg"}
    btn = {"css": "button.btn-default.btn-lg"}

    def fill(self, value):
        self._click(self.bar)
        self._input(self.bar, value)

    def click(self):
        self._click(self.btn)
