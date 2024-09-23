# -*- coding: utf-8 -*-

from main_tests_folder.model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Peter", middle_name="petrovich", last_name="petrov", nickname="ptr", company="yandex",
            address="minin strasse", home_phone="587 676 586896",
            phone="+56253687263", work_phone="2(342)341323",
                      email="petr@yandex.ru")
    app.contact.create_new_one(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


