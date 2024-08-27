# Не отрабатывает из за бага на UI. Чтобы действительно удалить контакт, надо дергать БД
from main_tests_folder.model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_one(Contact(name="test_delete"))
    app.contact.delete_first_one()