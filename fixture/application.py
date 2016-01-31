from fixture.wd_helper import WDH
from fixture.group_helper import GroupHelper
from fixture.contact_helper import ContactHelper
from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.wd_helper = WDH(self)
        self.group_helper = GroupHelper(self)
        self.contact_helper = ContactHelper(self)

    def destroy(self):
        self.wd.quit()