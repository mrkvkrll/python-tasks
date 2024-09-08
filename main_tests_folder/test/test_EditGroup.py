from main_tests_folder.model.group import Group
from random import randrange


def test_edit_first_group_name(app):
    group = Group(name="test_modify")
    if app.group.count() == 0:
        app.group.create_new_one(group)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edit_first_group_2fields(app):
#     if app.group.count() ==  0:
#         app.group.create_new_one(Group(name="test_modify"))
#     app.group.edit_first_one(Group(name="edited Group", description="hello"))