# -*- coding: utf-8 -*-
from random import randrange
from Model.contact import Contact


def test_del_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname='1', firstname='2', bday='1', bmonth='January'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

