

def test_delete_first_group(app):
    app.open_home_page()
    app.group.open_creating_page()
    app.group.delete_first_one()
    app.group.return_to_groups_page()