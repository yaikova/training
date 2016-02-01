
from model.group import Group

def test_add_group(app):
    app.wd_helper.open_home_page(app)
    app.wd_helper.login(login="admin", pwd="secret")
    app.group_helper.add_group(Group('lalala','lalala','lalala'))
    app.group_helper.return_to_group_page()
    app.wd_helper.logout()

def test_add_empty_group(app):
    app.wd_helper.open_home_page(app)
    app.wd_helper.login(login="admin", pwd="secret")
    app.group_helper.add_group(Group('','',''))
    app.group_helper.return_to_group_page()
    app.wd_helper.logout()

def test_add_symbols_group(app):
    app.wd_helper.open_home_page(app)
    app.wd_helper.login(login="admin", pwd="secret")
    app.group_helper.add_group(Group('~!@#$%^&*()_+-=`','~!@#$%^&*()_+-=`','~!@#$%^&*()_+-=`'))
    app.group_helper.return_to_group_page()
    app.wd_helper.logout()

