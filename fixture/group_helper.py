
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
            self.app.wd.find_element_by_link_text("group page").click()

    def add_group(self, group):
        #click group creation button
        self.app.wd.find_element_by_link_text("groups").click()
        self.app.wd.find_element_by_name("new").click()
        #fill group params
        self.app.wd_helper.fill_field(field_name='group_name', field_text=group.name)
        self.app.wd_helper.fill_field(field_name='group_header', field_text=group.header)
        self.app.wd_helper.fill_field(field_name='group_footer', field_text=group.footer)
        #click submit button
        self.app.wd.find_element_by_name("submit").click()