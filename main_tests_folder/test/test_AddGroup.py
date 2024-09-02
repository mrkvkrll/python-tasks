# -*- coding: utf-8 -*-

from main_tests_folder.model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_new_one(Group(name="first_group", description="description", other="something else"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
def test_add_empty_group(app):
    app.open_home_page()
    app.group.open_groups_page()
    app.group.create_new_one(Group(name="", description="", other=""))