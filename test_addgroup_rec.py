# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class my_test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        wd = self.wd
        self.open_url(wd, "http://localhost/addressbook/")
        self.login(wd, login="admin", pwd="secret")
        self.open_group_page(wd)
        self.add_group(wd, Group('lalala','lalala','lalala'))
        self.return_to_group_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_url(wd, "http://localhost/addressbook/")
        self.login(wd, login="admin", pwd="secret")
        self.open_group_page(wd)
        self.add_group(wd, Group('','',''))
        self.return_to_group_page(wd)
        self.logout(wd)

    def test_add_symbols_group(self):
        wd = self.wd
        self.open_url(wd, "http://localhost/addressbook/")
        self.login(wd, login="admin", pwd="secret")
        self.open_group_page(wd)
        self.add_group(wd, Group('~!@#$%^&*()_+-=`','~!@#$%^&*()_+-=`','~!@#$%^&*()_+-=`'))
        self.return_to_group_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def add_group(self, wd, group):
        #click group creation button
        wd.find_element_by_name("new").click()
        #fill group params
        self.fill_field(wd, field_name='group_name', field_text=group.name)
        self.fill_field(wd, field_name='group_header', field_text=group.header)
        self.fill_field(wd, field_name='group_footer', field_text=group.footer)
        #click submit button
        wd.find_element_by_name("submit").click()

    def fill_field(self, wd, field_name, field_text):
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).clear()
        wd.find_element_by_name(field_name).send_keys(field_text)

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, login, pwd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(pwd)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_url(self, wd, url):
        wd.get(url)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
