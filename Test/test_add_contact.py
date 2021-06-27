# -*- coding: utf-8 -*-
import os
from Model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='firstname', middlename='middlename', lastname='lastname', nickname='nickname',
                      photo=os.path.join(os.path.join(os.getcwd(), 'photo'), 'eo4qjv87_thumb.jpg'),
                      title='title', company='company', address='address',
                      home='home', mobile='1234567890', work='work', fax='1234567890', email='1@mail.ru',
                      email2='2@mail.ru', email3='3@mail.ru', homepage='homepage', bday='1',
                      bmonth='January', byear='1980', address2='address2', phone2='0987654321', notes='notes')
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



