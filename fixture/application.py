from fixture.wd_helper import WDH
from fixture.group_helper import GroupHelper
from fixture.contact_helper import ContactHelper
from fixture.session_helper import SessionHelper
from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self, host = 'http://localhost'):
        print('Start test run and create webdriver')
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.wd_helper = WDH(self)
        self.group_helper = GroupHelper(self)
        self.contact_helper = ContactHelper(self)
        self.session_helper = SessionHelper(self)
        self.host = host

    def destroy(self):
        print('Finish test run and destroy webdriver')
        self.wd.quit()
