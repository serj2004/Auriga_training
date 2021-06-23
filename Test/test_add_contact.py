# -*- coding: utf-8 -*-
import os
from Model.contact import Contact


def test_add_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.create(Contact(firstname='firstname', middlename='middlename', lastname='lastname', nickname='nickname',
                               photo=os.path.join(os.path.join(os.getcwd(), 'photo'), 'eo4qjv87_thumb.jpg'),
                               title='title', company='company', address='address',
                               home='home', mobile='1234567890', work='work', fax='1234567890', email='1@mail.ru',
                               email2='2@mail.ru', email3='3@mail.ru', homepage='homepage', bday='1',
                               bmonth='January', byear='1980', address2='address2', phone2='0987654321', notes='notes'))
    app.session.logout()


