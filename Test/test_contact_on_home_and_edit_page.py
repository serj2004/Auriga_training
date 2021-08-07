import re
from Model.contact import Contact


def test_info_on_homepage_and_db(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    for i in contact_from_db:
        i.all_email_from_home_page = merge_data_like_on_home_page(i.all_email_from_home_page)
        i.all_phones_from_home_page = merge_data_like_on_home_page(i.all_phones_from_home_page)
    assert sorted(contact_from_db, key=Contact.id_or_max) == sorted(contact_from_home_page, key=Contact.id_or_max)


def test_info_on_home_and_edit_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page_by_index(0)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)
    assert clear(contact_from_home_page.address) == clear(contact_from_edit_page.address)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page_by_index(0)
    contact_from_edit_page = app.contact.get_contact_from_edit_page_by_index(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2,
                                                                                contact.email3])))


def merge_data_like_on_home_page(list):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, list))))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.homephone, contact.mobilephone,
                                                                               contact.workphone, contact.phone2]))))


def clear(s):
    return re.sub("[() +-]", "", s)