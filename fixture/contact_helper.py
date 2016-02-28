from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def select_first(self):
        self.app.wd.find_element_by_name("selected[]").click()

    def contact_exists(self):
        return self.count() > 0

    def count(self):
         return len(self.app.wd.find_elements_by_name("selected[]"))

    def click_delete(self):
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()

    def add(self, contact):
        self.app.wd.find_element_by_link_text("add new").click()
        #fill contact params
        for key in contact.data:
            self.app.wd_helper.fill_field(key, contact.data[key])
        #click enter
        self.app.wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def edit_record(self, num):
        self.click_edit(num)
        contact = Contact()
        for key in contact.data:
            self.app.wd_helper.fill_field(key, self.app.wd_helper.get_field_val(key) + '_edit')
        self.app.wd_helper.click_button('update')

    def delete_record_from_edit_page(self, num):
        self.click_edit(num)
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()

    def click_edit(self, num):
        self.app.wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(num + 1) + "]/td[8]/a/img").click()