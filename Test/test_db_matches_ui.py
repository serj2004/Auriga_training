from Model.group import Group
import allure


def test_group_list(app, db):
    with allure.step("Given the group list from home page"):
        ui_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    with allure.step("Given the group list from database"):
        db_list = map(clean, db.get_group_list())
    with allure.step("Then home page group list is equal to the database list"):
        assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
