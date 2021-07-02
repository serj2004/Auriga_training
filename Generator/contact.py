import jsonpickle
import os.path
from Model.contact import Contact
import string
import random
import sys
import getopt


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "Data/contacts.json"
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    simbols = string.ascii_letters + string.digits + string.punctuation + ""*10
    return prefix + "".join([random.choice(simbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", middlename="")] + [Contact(firstname=random_string("firstname", 10),
                                                                          lastname=random_string("lastname", 10),
                                                                          middlename=random_string("middlename", 10))
                                                                  for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as fl:
    jsonpickle.set_encoder_options("json", indent=2)
    fl.write(jsonpickle.encode(testdata))