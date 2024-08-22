from main_tests_folder.model.contact import Contact


def test_edit_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_contacts_page()
    app.contact.open_edit_page()
    app.contact.filling_out_contact_forms(Contact(name="Petr", middle_name="Petrovich", last_name="Petrov", nickname="ptr", company="yandex", address="Minin strasse", home="+7676586896",
                                       phone="+7253687263", work="+7342341323", email="test@yande.ru"))
    app.contact.update()
    app.contact.return_to_homepage()
    app.session.logout()