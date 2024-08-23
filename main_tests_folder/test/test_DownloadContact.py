from main_tests_folder.model.contact import Contact


def test_edit_contact(app):
    app.open_home_page()
    app.contact.open_contacts_page()
    app.contact.download()
