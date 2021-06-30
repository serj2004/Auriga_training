import json
import os.path
from Model.group import Group
import string
import random
import sys
import getopt


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "Data/groups.json"
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    simbols = string.ascii_letters + string.digits + string.punctuation + ""*10
    return prefix + "".join([random.choice(simbols) for i in range(random.randrange(maxlen))])


test_data = [Group(name="", header="", footer="")] + [Group(name=random_string("name", 10),
                                                            header=random_string("header", 10),
                                                            footer=random_string("footer", 10)) for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as fl:
    fl.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))