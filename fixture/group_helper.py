
from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        current_url = self.app.wd.current_url
        if current_url != self.app.host + '/group.php':
            self.app.wd.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        self.app.wd.find_element_by_link_text("group page").click()

    def select_first(self):
        self.open_group_page()
        self.app.wd.find_element_by_name("selected[]").click()

    def click_delete(self):
        self.open_group_page()
        self.app.wd_helper.click_button('delete')

    def click_edit(self):
        self.open_group_page()
        self.app.wd_helper.click_button('edit')

    def click_update(self):
        self.app.wd.find_element_by_name('update').click()

    def change_fields(self, group):
        self.click_edit()
        self.app.wd_helper.fill_field(field_name='group_name', field_text=group.name)
        self.app.wd_helper.fill_field(field_name='group_header', field_text=group.header)
        self.app.wd_helper.fill_field(field_name='group_footer', field_text=group.footer)
        self.click_update()

    def edit_all_fields(self):
        self.app.group_helper.open_group_page()
        self.click_edit()
        #fill group params
        group = Group(self.app.wd_helper.get_field_val('group_name') + '_edit',
                      self.app.wd_helper.get_field_val('group_header') + '_edit',
                      self.app.wd_helper.get_field_val('group_footer') + '_edit')
        self.app.wd_helper.fill_field(field_name='group_name', field_text=group.name)
        self.app.wd_helper.fill_field(field_name='group_header', field_text=group.header)
        self.app.wd_helper.fill_field(field_name='group_footer', field_text=group.footer)
        self.click_update()

    def add(self, group):
        #click group creation button
        self.open_group_page()
        self.app.wd.find_element_by_name("new").click()
        #fill group params
        self.app.wd_helper.fill_field(field_name='group_name', field_text=group.name)
        self.app.wd_helper.fill_field(field_name='group_header', field_text=group.header)
        self.app.wd_helper.fill_field(field_name='group_footer', field_text=group.footer)
        #click submit button
        self.app.wd.find_element_by_name("submit").click()

