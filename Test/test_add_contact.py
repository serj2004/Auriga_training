# -*- coding: utf-8 -*-
import pytest
from Fixture.application import Application
from Model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.create(Contact(firstname='firstname', middlename='middlename', lastname='lastname', nickname='nickname',
                               title='title', company='company', address='address',
                               home='home', mobile='1234567890', work='work', fax='1234567890', email='1@mail.ru',
                               email2='2@mail.ru', email3='3@mail.ru', homepage='homepage', bday='1',
                               bmonth='January', byear='1980', address2='address2', phone2='0987654321', notes='notes'))
    app.session.logout()


