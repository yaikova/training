from fixture.wd_helper import WDH
from fixture.group_helper import GroupHelper
from fixture.contact_helper import ContactHelper
from fixture.session_helper import SessionHelper
from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self, host = 'http://localhost'):
        self.wd = WebDriver()
        #self.wd.implicitly_wait(10)
        self.wd_helper = WDH(self)
        self.group_helper = GroupHelper(self)
        self.contact_helper = ContactHelper(self)
        self.session_helper = SessionHelper(self)
        self.host = host

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def destroy(self):
        print('Finish test run and destroy webdriver')
        self.wd.quit()
