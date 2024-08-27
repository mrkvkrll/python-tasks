from main_tests_folder.model.group import Group

def test_delete_first_group(app):
    if app.group.count() ==  0:
        app.group.create_new_one(Group(name="test_delete"))
    app.group.delete_first_one()