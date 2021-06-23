# -*- coding: utf-8 -*-
from Model.group import Group


def test_edit_group_name(app):
    app.group.edit_first_group(Group(name="group2"))


def test_edit_group_header(app):
    app.group.edit_first_group(Group(header="group2"))
