from selenium import webdriver
from selenium.webdriver.common.by import By
from main_tests_folder.fixture.session import SessionHelper
from main_tests_folder.fixture.group import GroupHelper
from main_tests_folder.fixture.contact import ContactHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.by = By
        #self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        By = self.by
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements(By.NAME, "Number of results")) > 0):
            wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()