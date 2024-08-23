

class SessionHelper:
    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        wd = self.app.wd
        by = self.app.by
        wd.get("http://localhost/addressbook/")
        wd.find_element(by.NAME, "user").send_keys(username)
        wd.find_element(by.NAME, "pass").send_keys(password)
        wd.find_element(by.XPATH, "//input[@value='Login']").click()


    def logout(self):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.LINK_TEXT, "Logout").click()