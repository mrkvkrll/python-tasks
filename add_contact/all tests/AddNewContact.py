# -*- coding: utf-8 -*-
import pytest
from add_contact.contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_add_contact_page()
    app.create_contact(Contact(name="petr", middle_name="petrovich", last_name="petrov", nickname="ptr", company="yandex", address="minin strasse", home="587676586896",
                            phone="56253687263", work="2342341323", email="petr@yandex.ru"))
    app.save_contact()
    app.go_to_homepage()
    app.logout()


