from Fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
try:
    l = db.get_contact_list()
    for i in l:
        print(i)
    print(len(l))
finally:
    pass  #db.destroy()