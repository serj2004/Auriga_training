from Fixture.orm import ORMFixture
from Model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_not_in_group(Group(id="97"))
    for i in l:
        print(i)
    print(len(l))
finally:
    pass  #db.destroy()