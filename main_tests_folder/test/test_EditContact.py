from main_tests_folder.model.contact import Contact
from random import randrange

def test_edit_contact_part(app):
    if app.contact.count() == 0:
        app.contact.create_new_one(Contact(name="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(name="test")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_edit_contact_phone(app):
#     if app.contact.count() == 0:
#         app.contact.create_new_one(Contact(name="test_modify"))
#     app.contact.edit_first_one_contact(Contact(phone="+7253687999"))
