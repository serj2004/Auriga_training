# -*- coding: utf-8 -*-
import os
from Model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(photo=os.path.join(os.path.join(os.getcwd(), 'photo'), 'eo4qjv87_thumb.jpg'),
                                   bday='1', bmonth='January'))
    app.contact.delete_first_contact()

