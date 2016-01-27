# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group
from wd_helper import WDH

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class my_test(unittest.TestCase):
    def setUp(self):
        self.wd_helper = WDH(WebDriver())
        self.wd_helper.wd.implicitly_wait(60)
    
    def test_add_group(self):
        wd_helper = self.wd_helper
        wd_helper.open_url("http://localhost/addressbook/")
        wd_helper.login(login="admin", pwd="secret")
        self.open_group_page(wd_helper.wd)
        self.add_group(wd_helper.wd, Group('lalala','lalala','lalala'))
        self.return_to_group_page(wd_helper.wd)
        self.logout(wd_helper.wd)

    def test_add_empty_group(self):
        wd_helper = self.wd_helper
        wd_helper.open_url("http://localhost/addressbook/")
        wd_helper.login(login="admin", pwd="secret")
        self.open_group_page(wd_helper.wd)
        self.add_group(wd_helper.wd, Group('','',''))
        self.return_to_group_page(wd_helper.wd)
        self.logout(wd_helper.wd)

    def test_add_symbols_group(self):
        wd_helper = self.wd_helper
        wd_helper.open_url("http://localhost/addressbook/")
        wd_helper.login(login="admin", pwd="secret")
        self.open_group_page(wd_helper.wd)
        self.add_group(wd_helper.wd, Group('~!@#$%^&*()_+-=`','~!@#$%^&*()_+-=`','~!@#$%^&*()_+-=`'))
        self.return_to_group_page(wd_helper.wd)
        self.logout(wd_helper.wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def add_group(self, wd, group):
        #click group creation button
        wd.find_element_by_name("new").click()
        #fill group params
        self.wd_helper.fill_field(field_name='group_name', field_text=group.name)
        self.wd_helper.fill_field(field_name='group_header', field_text=group.header)
        self.wd_helper.fill_field(field_name='group_footer', field_text=group.footer)
        #click submit button
        wd.find_element_by_name("submit").click()



    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def tearDown(self):
        self.wd_helper.wd.quit()

if __name__ == '__main__':
    unittest.main()
