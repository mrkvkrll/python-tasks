from main_tests_folder.model.group import Group
class GroupHelper:
    def __init__(self, app):
        self.app = app


    def open_groups_page(self):
        wd = self.app.wd
        by = self.app.by
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(by.NAME, "new")) > 0):
            wd.find_element(by.LINK_TEXT, "groups").click()


    def create_new_one(self, group):
        wd = self.app.wd
        by = self.app.by
        self.app.open_home_page()
        self.open_groups_page()
        wd.find_element(by.NAME, "new").click()
        self.filling_out_forms(group)
        wd.find_element(by.NAME, "submit").click()
        self.return_to_groups_page()


    def edit_first_one(self ,group):
        wd = self.app.wd
        by = self.app.by
        self.app.open_home_page()
        self.open_groups_page()
        self.select_first_group()
        wd.find_element(by.NAME, "edit").click()
        self.filling_out_forms(group)
        wd.find_element(by.NAME, "update").click()
        self.return_to_groups_page()


    def select_first_group(self):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.NAME, "selected[]").click()


    def filling_out_forms(self, group):
        self.change_field_name("group_name", group.name)
        self.change_field_name("group_header", group.description)
        self.change_field_name("group_footer", group.other)

    def change_field_name(self, field_name, text):
        wd = self.app.wd
        by = self.app.by
        if text is not None:
            wd.find_element(by.NAME, field_name).click()
            wd.find_element(by.NAME, field_name).clear()
            wd.find_element(by.NAME, field_name).send_keys(text)

    def delete_first_one(self):
        wd = self.app.wd
        by = self.app.by
        self.app.open_home_page()
        self.open_groups_page()
        self.select_first_group()
        wd.find_element(by.NAME, "delete").click()
        self.return_to_groups_page()


    def return_to_groups_page(self):
        wd = self.app.wd
        by = self.app.by
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(by.NAME, "new")) > 0):
            wd.find_element(by.LINK_TEXT, "group page").click()


    def count(self):
        wd = self.app.wd
        by = self.app.by
        self.app.open_home_page()
        self.open_groups_page()
        return len(wd.find_elements(by.NAME, "selected[]"))


    def get_group_list(self):
        wd = self.app.wd
        by = self.app.by
        self.open_groups_page()
        groups = []
        for element in wd.find_elements(by.CSS_SELECTOR, "span.group"):
            text = element.text
            id = element.find_element(by.NAME, "selected[]").get_attribute("value")
            groups.append(Group(name=text,id=id))
        return groups

