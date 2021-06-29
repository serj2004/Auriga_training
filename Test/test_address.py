import re


def test_address_on_home_page(app):
    contact_address_from_home_page = app.contact.get_contact_list()[0]
    contact_address_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert clear(contact_address_from_home_page.address) == \
           merge_address_like_on_home_page(contact_address_from_edit_page)


def clear(s):
    return re.sub("[() +]", "", s)


def merge_address_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.address]))))
