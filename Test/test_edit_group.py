# -*- coding: utf-8 -*-
from Model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.edit_first_group(Group(name="group2"))


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.edit_first_group(Group(header="group2"))
