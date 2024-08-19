from selenium import webdriver
from main_tests_folder.fixture.session import SessionHelper
from main_tests_folder.fixture.group import GroupHelper
from main_tests_folder.fixture.contact import ContactHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        #self.wdn = By.NAME()
        #self.wdx = By.XPATH()
        #self.wdl = By.LINK_TEXT()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()