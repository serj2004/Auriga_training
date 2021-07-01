# -*- coding: utf-8 -*-
from random import randrange
from Model.contact import Contact


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname='1', firstname='2', bday='1', bmonth='January'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New firstname", lastname="New lastname")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

