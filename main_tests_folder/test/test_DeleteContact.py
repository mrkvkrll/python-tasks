from main_tests_folder.model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_one(Contact(name="test_delete"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_one()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts