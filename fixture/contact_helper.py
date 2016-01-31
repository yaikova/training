
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        self.app.wd.find_element_by_link_text("add new").click()
        #fill contact params
        for key in contact.data:
            self.app.wd_helper.fill_field(key, contact.data[key])
        #click enter
        self.app.wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()