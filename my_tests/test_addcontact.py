# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_empty_contact(app):
    app.wd_helper.open_url("http://localhost/addressbook/")
    app.wd_helper.login(login="admin", pwd="secret")
    app.contact_helper.add(Contact())
    app.wd_helper.logout()

def test_add_contact(app):
    app.wd_helper.open_url("http://localhost/addressbook/")
    app.wd_helper.login(login="admin", pwd="secret")
    #fill all fields with '123' value
    app.contact_helper.add(Contact('123'))
    app.wd_helper.logout()



