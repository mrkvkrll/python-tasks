# -*- coding: utf-8 -*-

from main_tests_folder.model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="first_group", description="description", other="something else")
    app.group.create_new_one(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="KRL", description="", other="")
    app.group.create_new_one(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)