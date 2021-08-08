from Model.contact import Contact
from Model.group import Group


def test_add_contact_into_group(app, db):
    old_contacts_not_in_groups = db.get_contacts_not_in_groups()
    if len(old_contacts_not_in_groups) == 0:
        app.contact.create(Contact(lastname='1', firstname='2', bday='1', bmonth='January'))
    group_list = db.get_group_list()
    if len(group_list) == 0:
        app.group.create(Group(name='test'))
    contact_add_to_group = db.get_contacts_not_in_groups()[0]
    group = db.get_group_list()[0].id
    app.contact.add_contact_to_group(contact_add_to_group, group)
    new_contacts_not_in_groups = db.get_contacts_not_in_groups()
    assert contact_add_to_group not in new_contacts_not_in_groups


def test_delete_contact_from_group(app, db):
    contact_list = app.contact.get_contact_list()
    if len(contact_list) == 0:
        app.contact.create(Contact(lastname='1', firstname='2', bday='1', bmonth='January'))
    group_list = app.group.get_group_list()
    if len(group_list) == 0:
        app.group.create(Group(name='test'))
    group_name = app.group.get_group_list()[0].name
    old_contacts_not_in_groups = db.get_contacts_not_in_groups()
    contact_delete_from_group = old_contacts_not_in_groups[0]
    group_id = app.group.get_group_list()[0].id
    app.contact.add_contact_to_group(contact_delete_from_group, group_id)
    id = app.contact.delete_contact_from_group(contact_delete_from_group, group_name)
    new_contacts_not_in_groups = db.get_contacts_not_in_groups()
    assert id in new_contacts_not_in_groups
