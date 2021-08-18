from Model.contact import Contact
from Model.group import Group
import allure


def test_add_contact_into_group(app, db):
    old_contacts_not_in_groups = db.get_contacts_not_in_groups()
    if len(old_contacts_not_in_groups) == 0:
        app.contact.create(Contact(lastname='1', firstname='2', bday='1', bmonth='January'))
    with allure.step("Given a non-empty group list"):
        group_list = db.get_group_list()
        if len(group_list) == 0:
            app.group.create(Group(name='test'))
    with allure.step("Given a contact to add into group"):
        contact_add_to_group = db.get_contacts_not_in_groups()[0]
        group = db.get_group_list()[0].id
    with allure.step("When I add the contact %s to the group %s" % (contact_add_to_group, group)):
        app.contact.add_contact_to_group(contact_add_to_group, group)
    with allure.step("Then added contact is in group"):
        new_contacts_not_in_groups = db.get_contacts_not_in_groups()
        assert contact_add_to_group not in new_contacts_not_in_groups


def test_delete_contact_from_group(app, db):
    with allure.step("Given a non-empty contact list"):
        contact_id_list = db.get_contacts_not_in_groups()
        if len(contact_id_list) == 0:
            app.contact.create(Contact(lastname='1', firstname='2', bday='1', bmonth='January'))
    with allure.step("Given a non-empty group list"):
        group_list = app.group.get_group_list()
        if len(group_list) == 0:
            app.group.create(Group(name='test'))
    with allure.step("Given a group name and contact not in groups"):
        group_name = app.group.get_group_list()[0].name
        old_contacts_not_in_groups = db.get_contacts_not_in_groups()
    with allure.step("When I delete the contact %s from the group %s" % (old_contacts_not_in_groups[0], group_name)):
        contact_delete_from_group = old_contacts_not_in_groups[0]
        group_id = app.group.get_group_list()[0].id
        app.contact.add_contact_to_group(contact_delete_from_group, group_id)
        id = app.contact.delete_contact_from_group(contact_delete_from_group, group_name)
        new_contacts_not_in_groups = db.get_contacts_not_in_groups()
    with allure.step("Then deleted contact is not in group"):
        assert id in new_contacts_not_in_groups
