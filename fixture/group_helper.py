
from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        self.app.wd.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        self.app.wd.find_element_by_link_text("group page").click()

    def select_first_group(self):
        self.open_group_page()
        self.app.wd.find_element_by_name("selected[]").click()

    def delete_group(self):
        self.app.wd_helper.click_button('delete')

    def edit_group(self):
        self.app.wd_helper.click_button('edit')
        #fill group params
        group = Group(self.app.wd_helper.get_field_val('group_name') + '_edit',
                      self.app.wd_helper.get_field_val('group_header') + '_edit',
                      self.app.wd_helper.get_field_val('group_footer') + '_edit')
        self.app.wd_helper.fill_field(field_name='group_name', field_text=group.name)
        self.app.wd_helper.fill_field(field_name='group_header', field_text=group.header)
        self.app.wd_helper.fill_field(field_name='group_footer', field_text=group.footer)
        self.app.wd.find_element_by_name('update').click()

    def add_group(self, group):
        #click group creation button
        self.open_group_page()
        self.app.wd.find_element_by_name("new").click()
        #fill group params
        self.app.wd_helper.fill_field(field_name='group_name', field_text=group.name)
        self.app.wd_helper.fill_field(field_name='group_header', field_text=group.header)
        self.app.wd_helper.fill_field(field_name='group_footer', field_text=group.footer)
        #click submit button
        self.app.wd.find_element_by_name("submit").click()