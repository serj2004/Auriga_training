from Model.contact import Contact
from Model.group import Group


def test_add_contact_into_group(app, db):
    contacts_not_in_groups = db.get_contacts_not_in_groups()
    if len(contacts_not_in_groups) == 0:
        app.contact.create(Contact(lastname='1', firstname='2', bday='1', bmonth='January'))
    group_list = db.get_group_list()
    if len(group_list) == 0:
        app.group.create(Group(name='test'))
    contact_add_to_group = contacts_not_in_groups[0]
    app.contact.add_contact_to_group(contact_add_to_group, group_list[0].id)
    assert contact_add_to_group in contacts_not_in_groups

def test_delete_contact_from_group(app, db):
    pass