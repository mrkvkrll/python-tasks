from main_tests_folder.model.contact import Contact


def test_edit_contact_part(app):
    contact = Contact(name="test", middle_name="test", last_name="test")
    if app.contact.count() == 0:
        app.contact.create_new_one(contact)
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.edit_first_one_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_edit_contact_phone(app):
#     if app.contact.count() == 0:
#         app.contact.create_new_one(Contact(name="test_modify"))
#     app.contact.edit_first_one_contact(Contact(phone="+7253687999"))
