from main_tests_folder.model.group import Group

def test_delete_first_group(app):
    if app.group.count() ==  0:
        app.group.create_new_one(Group(name="test_delete"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_one()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups