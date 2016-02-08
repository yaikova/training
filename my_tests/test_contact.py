
from model.contact import Contact


def test_add_empty_contact(app):
    app.wd_helper.open_home_page(app)
    app.session_helper.login(login="admin", pwd="secret")
    app.contact_helper.add(Contact())
    app.session_helper.logout()


def test_add_contact(app):
    app.wd_helper.open_home_page(app)
    app.session_helper.login(login="admin", pwd="secret")
    #fill all fields with '123' value
    app.contact_helper.add(Contact('123'))
    app.session_helper.logout()


def test_delete_first_contact(app):
    app.wd_helper.open_home_page(app)
    app.session_helper.login(login="admin", pwd="secret")
    app.contact_helper.select_first()
    app.contact_helper.delete()
    app.wd_helper.confirm_alert()
    app.session_helper.logout()


def test_cancel_delete(app):
    app.wd_helper.open_home_page(app)
    app.session_helper.login(login="admin", pwd="secret")
    app.contact_helper.select_first()
    app.contact_helper.delete()
    app.wd_helper.decline_alert()
    app.session_helper.logout()


def test_delete_not_selected_contact(app):
    app.wd_helper.open_home_page(app)
    app.session_helper.login(login="admin", pwd="secret")
    app.contact_helper.delete()
    app.wd_helper.confirm_alert()
    app.session_helper.logout()


def test_edit_contact(app):
    app.wd_helper.open_home_page(app)
    app.session_helper.login(login="admin", pwd="secret")
    app.contact_helper.edit_record(1)
    app.session_helper.logout()


def test_delete_from_edit(app):
    app.wd_helper.open_home_page(app)
    app.session_helper.login(login="admin", pwd="secret")
    app.contact_helper.delete_record_from_edit_page(1)
    app.session_helper.logout()