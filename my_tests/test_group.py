
from model.group import Group

def test_add_group(app, group):
    app.group_helper.add(Group('lalala', 'lalala', 'lalala'))
    app.group_helper.return_to_group_page()


def test_add_empty_group(app, group):
    app.group_helper.add(Group())
    app.group_helper.return_to_group_page()


# Спецсимволы в полях ввода
def test_add_symbols_group(app, group):
    app.group_helper.add(Group('~!@#$%^&*()_+-=`', '~!@#$%^&*()_+-=`', '~!@#$%^&*()_+-=`'))
    app.group_helper.return_to_group_page()


def test_delete_first_group(app, group):
    app.group_helper.select_first()
    app.group_helper.click_delete()
    app.group_helper.return_to_group_page()


def test_delete_not_selected_group(app, group):
    app.group_helper.click_delete()
    app.group_helper.return_to_group_page()


def test_change_first_group_header(app, group):
    app.group_helper.select_first()
    app.group_helper.change_fields(Group(name = 'new name'))
    app.group_helper.return_to_group_page()


def test_edit_first_group(app, group):
    app.group_helper.select_first()
    app.group_helper.edit_all_fields()
    app.group_helper.return_to_group_page()


def test_edit_not_selected_group(app, group):
    app.group_helper.edit_all_fields()
    app.group_helper.return_to_group_page()
