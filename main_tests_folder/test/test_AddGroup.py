# -*- coding: utf-8 -*-

from main_tests_folder.model.group import Group


def test_add_group(app):
    app.open_home_page()
    app.group.open_creating_page()
    app.group.create_new_one(Group(name="first_group", description="description", other="something else"))
    app.group.return_to_groups_page()

def test_add_empty_group(app):
    app.open_home_page()
    app.group.open_creating_page()
    app.group.create_new_one(Group(name="", description="", other=""))