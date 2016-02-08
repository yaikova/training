
from model.group import Group

def test_add_group(app):
    app.wd_helper.open_home_page(app)
    app.session_helper.login(login="admin", pwd="secret")
    app.group_helper.add(Group('lalala', 'lalala', 'lalala'))
    app.group_helper.return_to_group_page()
    app.session_helper.logout()

def test_add_empty_group(app):
    app.wd_helper.open_home_page(app)
    app.session_helper.login(login="admin", pwd="secret")
    app.group_helper.add(Group('', '', ''))
    app.group_helper.return_to_group_page()
    app.session_helper.logout()

def test_add_symbols_group(app):
    app.wd_helper.open_home_page(app)
    app.session_helper.login(login="admin", pwd="secret")
    app.group_helper.add(Group('~!@#$%^&*()_+-=`', '~!@#$%^&*()_+-=`', '~!@#$%^&*()_+-=`'))
    app.group_helper.return_to_group_page()
    app.session_helper.logout()

def test_delete_first_group(app):
    app.wd_helper.open_home_page(app)
    app.session_helper.login(login="admin", pwd="secret")
    app.group_helper.open_group_page()
    app.group_helper.select_first()
    app.group_helper.delete()
    app.group_helper.return_to_group_page()
    app.session_helper.logout()

def test_delete_not_selected_group(app):
    app.wd_helper.open_home_page(app)
    app.session_helper.login(login="admin", pwd="secret")
    app.group_helper.open_group_page()
    app.group_helper.delete()
    app.group_helper.return_to_group_page()
    app.session_helper.logout()

def test_edit_first_group(app):
    app.wd_helper.open_home_page(app)
    app.session_helper.login(login="admin", pwd="secret")
    app.group_helper.open_group_page()
    app.group_helper.select_first()
    app.group_helper.edit()
    app.group_helper.return_to_group_page()
    app.session_helper.logout()

def test_edit_not_selected_group(app):
    app.wd_helper.open_home_page(app)
    app.session_helper.login(login="admin", pwd="secret")
    app.group_helper.open_group_page()
    app.group_helper.edit()
    app.group_helper.return_to_group_page()
    app.session_helper.logout()