# -*- coding: utf-8 -*-
import random
from Model.contact import Contact
import allure


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(lastname='1', firstname='2', bday='1', bmonth='January'))
    with allure.step("Given a non-empty contact list"):
        old_contacts = db.get_contact_list()
    with allure.step("Given a random contact from the list"):
        random_contact = random.choice(old_contacts)
        contact = Contact(firstname="New f", lastname="New l")
        contact.id = random_contact.id
    with allure.step("When I edit the contact from the list"):
        app.contact.edit_contact_by_id(contact.id, contact)
    with allure.step("Then the new contact list is equal to the old list with the edited contact"):
        new_contacts = db.get_contact_list()
        index = old_contacts.index(random_contact)
        old_contacts[index] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)

