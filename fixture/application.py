from fixture.wd_helper import WDH
from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd_helper = WDH(WebDriver())
        self.wd_helper.wd.implicitly_wait(60)

    def return_to_group_page(self):
        self.wd_helper.wd.find_element_by_link_text("group page").click()

    def add_group(self, group):
        #click group creation button
        self.wd_helper.wd.find_element_by_link_text("groups").click()
        self.wd_helper.wd.find_element_by_name("new").click()
        #fill group params
        self.wd_helper.fill_field(field_name='group_name', field_text=group.name)
        self.wd_helper.fill_field(field_name='group_header', field_text=group.header)
        self.wd_helper.fill_field(field_name='group_footer', field_text=group.footer)
        #click submit button
        self.wd_helper.wd.find_element_by_name("submit").click()

    def add_contact(self, contact):
        self.wd_helper.wd.find_element_by_link_text("add new").click()
        #fill contact params
        for key in contact.data:
            self.wd_helper.fill_field(key, contact.data[key])
        #click enter
        self.wd_helper.wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def destroy(self):
        self.wd_helper.wd.quit()