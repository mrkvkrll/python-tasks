

class GroupHelper:
    def __init__(self, app):
        self.app = app


    def open_creating_page(self):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.LINK_TEXT, "groups").click()


    def create_new_one(self, group):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.NAME, "new").click()
        self.filling_out_forms(group)
        wd.find_element(by.NAME, "submit").click()


    def edit_first_one(self,group):
        wd = self.app.wd
        by = self.app.by
        self.select_first_group()
        wd.find_element(by.NAME, "edit").click()
        self.filling_out_forms(group)
        wd.find_element(by.NAME, "update").click()


    def select_first_group(self):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.NAME, "selected[]").click()


    def filling_out_forms(self,group):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.NAME, "group_name").click()
        wd.find_element(by.NAME, "group_name").clear()
        wd.find_element(by.NAME, "group_name").send_keys(group.name)
        wd.find_element(by.NAME, "group_header").click()
        wd.find_element(by.NAME, "group_header").clear()
        wd.find_element(by.NAME, "group_header").send_keys(group.description)
        wd.find_element(by.NAME, "group_footer").click()
        wd.find_element(by.NAME, "group_footer").clear()
        wd.find_element(by.NAME, "group_footer").send_keys(group.other)


    def delete_first_one(self):
        wd = self.app.wd
        by = self.app.by
        self.select_first_group()
        wd.find_element(by.NAME, "delete").click()


    def return_to_groups_page(self):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.LINK_TEXT, "group page").click()


