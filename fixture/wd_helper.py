
class WDH:

    def __init__(self, app):
        self.app = app

    def open_url(self, url):
        self.app.wd.get(url)

    def login(self, login, pwd):
        self.app.wd.find_element_by_name("user").click()
        self.app.wd.find_element_by_name("user").clear()
        self.app.wd.find_element_by_name("user").send_keys(login)
        self.app.wd.find_element_by_name("pass").click()
        self.app.wd.find_element_by_name("pass").clear()
        self.app.wd.find_element_by_name("pass").send_keys(pwd)
        self.app.wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def fill_field(self, field_name, field_text):
        self.app.wd.find_element_by_name(field_name).click()
        self.app.wd.find_element_by_name(field_name).clear()
        self.app.wd.find_element_by_name(field_name).send_keys(field_text)

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()