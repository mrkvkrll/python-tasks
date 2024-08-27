

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


    def ensure_logout(self):
        wd = self.app.wd
        by = self.app.by
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        by = self.app.by
        return len(wd.find_elements(by.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        by = self.app.by
        return wd.find_element(by.XPATH, "//div[@id='top']/form/b").text == "("+username+")"


    def ensure_login(self, username, password):
        wd = self.app.wd
        by = self.app.by
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)