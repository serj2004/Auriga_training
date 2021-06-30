from Model.group import Group
import string
import random


testdata = [
    Group(name="group1", header="header1", footer="footer1"),
    Group(name="group2", header="header2", footer="footer2")
]


# def random_string(prefix, maxlen):
#     simbols = string.ascii_letters + string.digits + string.punctuation + ""*10
#     return prefix + "".join([random.choice(simbols) for i in range(random.randrange(maxlen))])
#
#
# test_data = [Group(name="", header="", footer="")] + [Group(name=random_string("name", 10),
#                                                             header=random_string("header", 10),
#                                                             footer=random_string("footer", 10)) for i in rang]e(5)