# -*- coding: utf-8 -*-
import random
import allure
from Model.group import Group


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    with allure.step("Given a non-empty group list"):
        old_groups = db.get_group_list()
    with allure.step("Given a random group from the list"):
        random_group = random.choice(old_groups)
        group = Group(name="New New group 1", header="New header", footer="New footer")
        group.id = random_group.id
    with allure.step("When I edit the group from the list"):
        app.group.edit_group_by_id(group.id, group)
    with allure.step("Then the new group list is equal to the old list with the edited group"):
        new_groups = db.get_group_list()
        index = old_groups.index(random_group)
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

