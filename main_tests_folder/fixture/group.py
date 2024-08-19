from selenium.webdriver.common.by import By

class GroupHelper:
    def __init__(self, app):
        self.app = app


    def open_creating_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()


    def create_new_one(self, group):
        wd = self.app.wd
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.description)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.other)
        wd.find_element(By.NAME, "submit").click()


    def delete_first_one(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.NAME, "delete").click()


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()


