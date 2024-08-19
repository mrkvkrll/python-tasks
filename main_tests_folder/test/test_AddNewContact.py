# -*- coding: utf-8 -*-

from main_tests_folder.model.contact import Contact


def test_add_new_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_creating_page()
    app.contact.create_new_one(Contact(name="petr", middle_name="petrovich", last_name="petrov", nickname="ptr", company="yandex", address="minin strasse", home="587676586896",
                                       phone="56253687263", work="2342341323", email="petr@yandex.ru"))
    app.contact.save()
    app.contact.return_to_homepage()
    app.session.logout()