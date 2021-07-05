# -*- coding: utf-8 -*-
import random
from Model.group import Group


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    group = Group(name="New New group 1", header="New header", footer="New footer")
    group.id = random_group.id
    app.group.edit_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    for gr in old_groups:
        if str(gr)[:3] == random_group.id:
            index = old_groups.index(gr)
            old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

