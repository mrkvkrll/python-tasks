from main_tests_folder.model.contact import Contact


def test_edit_contact_part(app):
    if app.contact.count() == 0:
        app.contact.create_new_one(Contact(name="test", middle_name="test", last_name="test"))
    app.contact.edit_first_one_contact(Contact(name="Petr", middle_name="Petrovich", last_name="Petrov", nickname="ptr", company="yandex",address="Minin strasse", home="+7676586896", ))

# def test_edit_contact_phone(app):
#     if app.contact.count() == 0:
#         app.contact.create_new_one(Contact(name="test_modify"))
#     app.contact.edit_first_one_contact(Contact(phone="+7253687999"))
