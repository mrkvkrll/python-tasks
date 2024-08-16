from selenium import webdriver
from selenium.webdriver.common.by import By

class Application:


    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_group_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def create_new_group(self, group):
        wd = self.wd
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

    def open_group_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        wd = self.wd
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def go_to_homepage(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def save_contact(self):
        wd = self.wd
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()

    def create_contact(self, contact):
        wd = self.wd
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").send_keys(contact.name)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middle_name)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").send_keys(contact.last_name)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").send_keys(contact.home)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").send_keys(contact.phone)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").send_keys(contact.work)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").send_keys(contact.email)

    def open_add_contact_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "add new").click()


    def destroy(self):
        self.wd.quit()