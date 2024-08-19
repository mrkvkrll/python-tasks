from selenium.webdriver.common.by import By

class SessionHelper:
    def __init__(self, app):
        self.app = app
        #self.name = app
        #self.xpath = app
        #self.LINK_TEXT = app


    def login(self, username, password):
        wd = self.app.wd
        #wdn = self.name.wdn
        #wdx = self.xpath.wdx
        #wd.find_element(wdn.By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        #wd.find_element(wdn.By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()


    def logout(self):
        wd = self.app.wd
        #wdl = self.LINK_TEXT.wdl
        wd.find_element(By.LINK_TEXT, "Logout").click()