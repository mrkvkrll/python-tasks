from main_tests_folder.model.group import Group

def test_edit_first_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_creating_page()
    app.group.edit_first_one(Group(name="edited group", description="edited description", other="edited something else"))
    app.group.return_to_groups_page()
    app.session.logout()