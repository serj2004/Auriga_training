from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        file = wd.find_element_by_xpath("//input[@type='file']")
        file.send_keys(contact.photo)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_value('firstname', contact.firstname)
        self.change_contact_value('middlename', contact.middlename)
        self.change_contact_value('lastname', contact.lastname)
        self.change_contact_value('nickname', contact.nickname)
        self.change_contact_value('title', contact.title)
        self.change_contact_value('company', contact.company)
        self.change_contact_value('address', contact.address)
        self.change_contact_value('home', contact.home)
        self.change_contact_value('mobile', contact.mobile)
        self.change_contact_value('work', contact.work)
        self.change_contact_value('fax', contact.fax)
        self.change_contact_value('email', contact.email)
        self.change_contact_value('email2', contact.email2)
        self.change_contact_value('email3', contact.email3)
        self.change_contact_value('homepage', contact.homepage)
        self.change_contact_value('address2', contact.address2)
        self.change_contact_value('phone2', contact.phone2)
        self.change_contact_value('notes', contact.notes)
        self.change_contact_value('byear', contact.byear)

    def change_contact_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))
