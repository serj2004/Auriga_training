import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Model.contact import Contact


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
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cashe = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.return_to_home_page()
        self.contact_cashe = None

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.return_to_home_page()
        self.contact_cashe = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_value('firstname', contact.firstname)
        self.change_contact_value('middlename', contact.middlename)
        self.change_contact_value('lastname', contact.lastname)
        self.change_contact_value('nickname', contact.nickname)
        self.change_contact_value('title', contact.title)
        self.change_contact_value('company', contact.company)
        self.change_contact_value('address', contact.address)
        self.change_contact_value('home', contact.homephone)
        self.change_contact_value('mobile', contact.mobilephone)
        self.change_contact_value('work', contact.workphone)
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
        wd.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        WebDriverWait(wd, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        self.contact_cashe = None

    def delete_contact_by_id(self, id):
        wd = self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        WebDriverWait(wd, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        self.contact_cashe = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id(id).click()
        return wd

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cashe = None

    def get_contact_list(self):
        if self.contact_cashe is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cashe = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id_cont = cells[0].find_element_by_tag_name("input").get_attribute("value")
                last_name = cells[1].text
                first_name = cells[2].text
                address = cells[3].text
                all_phones = cells[5].text
                all_email = cells[4].text
                self.contact_cashe.append(Contact(firstname=first_name, lastname=last_name, id=id_cont, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_email_from_home_page=all_email))
        return list(self.contact_cashe)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_edit_page_by_index(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, phone2=phone2, address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page_by_index(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, phone2=phone2)

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_value(group_id)
        wd.find_element_by_css_selector("select[name='to_group']>option[value='%s']" % group_id).click()
        wd.find_element_by_name("add").click()

    def delete_contact_from_group(self, contact_id, group_name):
        wd = self.app.wd
        wd.find_element_by_link_text("group page \"%s\"" % group_name).click()
        wd.find_element_by_id(contact_id).click()
        wd.find_element_by_name("remove").click()
        return contact_id

