# -*- coding: utf-8 -*-

import pytest
from main_tests_folder.model.group import Group
from main_tests_folder.fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_creating_page()
    app.group.create_new_one(Group(name="first_group", description="description", other="something else"))
    app.group.return_to_groups_page()
    app.session.logout()

def test_add_empty_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_creating_page()
    app.group.create_new_one(Group(name="", description="", other=""))
    app.session.logout()