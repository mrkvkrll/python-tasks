from selenium.webdriver.common.by import By

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_creating_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()


    def create_new_one(self, contact):
        wd = self.app.wd
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


    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def delete_first_one(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()

    def save(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()


    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()