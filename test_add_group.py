import unittest
from selenium.webdriver.firefox.webdriver import WebDriver


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_group(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_xpath("xpath=//input[@value='Login']").click()
        wd.find_element_by_link_text("link=groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").send_keys("group1")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").send_keys("group_header")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").send_keys("group_footer")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()