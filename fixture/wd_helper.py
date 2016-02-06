
class WDH:

    def __init__(self, app):
        self.app = app

    def open_url(self, url):
        self.app.wd.get(url)

    def open_home_page(self, app):
        self.app.wd.get(app.host + '/addressbook/')

    def confirm_alert(self):
        self.app.wd.switch_to_alert().accept()

    def decline_alert(self):
        self.app.wd.switch_to_alert().dismiss()

    def fill_field(self, field_name, field_text):
        self.app.wd.find_element_by_name(field_name).click()
        self.app.wd.find_element_by_name(field_name).clear()
        self.app.wd.find_element_by_name(field_name).send_keys(field_text)

    def get_field_val(self, field_name):
        z = self.app.wd.find_element_by_name(field_name)
        return z.get_attribute('value')

    def click_button(self, button_name):
        self.app.wd.find_element_by_name(button_name).click()