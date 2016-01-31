from selenium import webdriver

class WDH:

    def __init__(self, wd):
        self.wd = wd

    def open_url(self, url):
        self.wd.get(url)

    def login(self, login, pwd):
        self.wd.find_element_by_name("user").click()
        self.wd.find_element_by_name("user").clear()
        self.wd.find_element_by_name("user").send_keys(login)
        self.wd.find_element_by_name("pass").click()
        self.wd.find_element_by_name("pass").clear()
        self.wd.find_element_by_name("pass").send_keys(pwd)
        self.wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def fill_field(self, field_name, field_text):
        self.wd.find_element_by_name(field_name).click()
        self.wd.find_element_by_name(field_name).clear()
        self.wd.find_element_by_name(field_name).send_keys(field_text)

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()