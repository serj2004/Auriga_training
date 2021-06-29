import re


def test_full_name_on_home_page(app):
    contact_full_name_from_home_page = app.contact.get_contact_list()[0]
    contact_full_name_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert contact_full_name_from_home_page.firstname + contact_full_name_from_home_page.lastname == \
           merge_names_like_on_home_page(contact_full_name_from_edit_page)


def clear(s):
    return re.sub("[() +-]", "", s)


def merge_names_like_on_home_page(contact):
    return "".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.firstname, contact.lastname]))))
