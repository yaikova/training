
class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login_as_admin(self):
        self.login(login="admin", pwd="secret")

    def login(self, login, pwd):
        self.app.wd.find_element_by_name("user").click()
        self.app.wd.find_element_by_name("user").clear()
        self.app.wd.find_element_by_name("user").send_keys(login)
        self.app.wd.find_element_by_name("pass").click()
        self.app.wd.find_element_by_name("pass").clear()
        self.app.wd.find_element_by_name("pass").send_keys(pwd)
        self.app.wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()