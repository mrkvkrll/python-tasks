

def test_delete_first_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_contacts_page()
    app.contact.delete_first_one()
    app.session.logout()