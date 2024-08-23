from main_tests_folder.model.group import Group

def test_edit_first_group_name(app):
    app.open_home_page()
    app.group.open_creating_page()
    app.group.edit_first_one(Group(name="edited_Group"))
    app.group.return_to_groups_page()

def test_edit_first_group_2fields(app):
    app.open_home_page()
    app.group.open_creating_page()
    app.group.edit_first_one(Group(name="edited Group", description="hello"))
    app.group.return_to_groups_page()