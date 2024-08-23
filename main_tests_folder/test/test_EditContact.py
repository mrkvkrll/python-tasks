from main_tests_folder.model.contact import Contact


def test_edit_contact_part(app):
    app.open_home_page()
    app.contact.open_contacts_page()
    app.contact.edit_first_one_contact(Contact(name="Petr", middle_name="Petrovich", last_name="Petrov", nickname="ptr", company="yandex", address="Minin strasse", home="+7676586896",))
    app.contact.return_to_homepage()

def test_edit_contact_phone(app):
    app.open_home_page()
    app.contact.open_contacts_page()
    app.contact.edit_first_one_contact(Contact(phone="+7253687999"))
    app.contact.return_to_homepage()