from main_tests_folder.model.group import Group

def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create_new_one(Group(name="test_modify"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_one(Group(name="edited_Group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

# def test_edit_first_group_2fields(app):
#     if app.group.count() ==  0:
#         app.group.create_new_one(Group(name="test_modify"))
#     app.group.edit_first_one(Group(name="edited Group", description="hello"))