from main_tests_folder.model.contact import Contact


def test_edit_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.download()
    app.session.logout()