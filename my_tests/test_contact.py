
from model.contact import Contact


def test_add_empty_contact(app):
    app.contact_helper.add(Contact())


def test_add_contact(app):
    #fill all fields with '123' value
    app.contact_helper.add(Contact('123'))


def test_delete_first_contact(app):
    app.contact_helper.select_first()
    app.contact_helper.delete()
    app.wd_helper.confirm_alert()


def test_cancel_delete(app):
    app.contact_helper.select_first()
    app.contact_helper.delete()
    app.wd_helper.decline_alert()


def test_delete_not_selected_contact(app):
    app.contact_helper.delete()
    app.wd_helper.confirm_alert()


def test_edit_contact(app):
    app.contact_helper.edit_record(1)


def test_delete_from_edit(app):
    app.contact_helper.delete_record_from_edit_page(1)
