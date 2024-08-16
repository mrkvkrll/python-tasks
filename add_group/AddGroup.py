# -*- coding: utf-8 -*-

import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_group_page()
    app.create_new_group(Group(name="first_group", description="description", other="something else"))
    app.return_to_group_page()
    app.logout()

def test_add_empty_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_group_page()
    app.create_new_group(Group(name="", description="", other=""))
    app.return_to_group_page()
    app.logout()
