# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from wd_helper import WDH
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_contact(unittest.TestCase):
    def setUp(self):
        self.wd_helper = WDH(WebDriver())
        self.wd_helper.wd.implicitly_wait(60)
    
    def test_add_empty_contact(self):
        wd_helper = self.wd_helper
        wd_helper.open_url("http://localhost/addressbook/")
        wd_helper.login(login="admin", pwd="secret")
        self.open_new_contact_page(wd_helper.wd)
        self.add_contact(wd_helper.wd, Contact())
        wd_helper.wd.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        wd_helper = self.wd_helper
        wd_helper.open_url("http://localhost/addressbook/")
        wd_helper.login(login="admin", pwd="secret")
        self.open_new_contact_page(wd_helper.wd)
        #fill all fields with '123' value
        contact=Contact()
        contact.fill_data_with_trash()
        self.add_contact(wd_helper.wd, contact)
        wd_helper.wd.find_element_by_link_text("Logout").click()

    def add_contact(self, wd, contact):
        #fill contact params
        for key in contact.data:
            self.wd_helper.fill_field(key, contact.data[key])
        #click enter
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_new_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def tearDown(self):
        self.wd_helper.wd.quit()

if __name__ == '__main__':
    unittest.main()
