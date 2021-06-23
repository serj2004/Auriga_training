# -*- coding: utf-8 -*-
from Model.group import Group


def test_edit_group(app):
    app.session.login(username='admin', password='secret')
    app.group.edit_first_group(Group(name="group2", header="group header2", footer="group footer2"))
    app.session.logout()


