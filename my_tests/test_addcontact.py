# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
import pytest
from wd_helper import WDH
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_empty_contact(app):
    app.wd_helper.open_url("http://localhost/addressbook/")
    app.wd_helper.login(login="admin", pwd="secret")
    app.add_contact(Contact())
    app.wd_helper.logout()

def test_add_contact(app):
    app.wd_helper.open_url("http://localhost/addressbook/")
    app.wd_helper.login(login="admin", pwd="secret")
    #fill all fields with '123' value
    contact=Contact()
    contact.fill_data_with_trash()
    app.add_contact(contact)
    app.wd_helper.logout()



