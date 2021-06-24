from selenium.webdriver.firefox.webdriver import WebDriver
from Fixture.contact import ContactHelper
from Fixture.group import GroupHelper
from Fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.open_home_page()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()