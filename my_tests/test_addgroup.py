# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.wd_helper.open_url("http://localhost/addressbook/")
    app.wd_helper.login(login="admin", pwd="secret")
    app.add_group(Group('lalala','lalala','lalala'))
    app.return_to_group_page()
    app.wd_helper.logout()

def test_add_empty_group(app):
    app.wd_helper.open_url("http://localhost/addressbook/")
    app.wd_helper.login(login="admin", pwd="secret")
    app.add_group(Group('','',''))
    app.return_to_group_page()
    app.wd_helper.logout()

def test_add_symbols_group(app):
    app.wd_helper.open_url("http://localhost/addressbook/")
    app.wd_helper.login(login="admin", pwd="secret")
    app.add_group(Group('~!@#$%^&*()_+-=`','~!@#$%^&*()_+-=`','~!@#$%^&*()_+-=`'))
    app.return_to_group_page()
    app.wd_helper.logout()

