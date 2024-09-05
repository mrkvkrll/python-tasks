# -*- coding: utf-8 -*-

from main_tests_folder.model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_new_one(Group(name="first_group", description="description", other="something else"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_new_one(Group(name="KRL", description="", other=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    # old_groups.append(Group(name="", description="", other=""))
    # assert old_groups.__eq__(new_groups)