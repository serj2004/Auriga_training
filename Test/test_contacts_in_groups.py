from Model.contact import Contact


def test_add_contact_into_group(app, db):
    contacts_not_in_groups = db.get_contacts_not_in_groups()
    if len(contacts_not_in_groups) == 0:
        app.contact.create(Contact(lastname='1', firstname='2', bday='1', bmonth='January'))
    print(contacts_not_in_groups)