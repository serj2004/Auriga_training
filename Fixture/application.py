from selenium.webdriver.firefox.webdriver import WebDriver
from Fixture.contact import ContactHelper
from Fixture.group import GroupHelper
from Fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(1)
        self.open_home_page()
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
        url = "https://localhost/addressbook/"
        if not (wd.current_url == url):
            wd.get(url)

    def destroy(self):
        self.wd.quit()