

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_creating_page(self):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.LINK_TEXT, "add new").click()


    def create_new_one(self, contact):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.NAME, "firstname").click()
        wd.find_element(by.NAME, "firstname").send_keys(contact.name)
        wd.find_element(by.NAME, "middlename").click()
        wd.find_element(by.NAME, "middlename").send_keys(contact.middle_name)
        wd.find_element(by.NAME, "lastname").click()
        wd.find_element(by.NAME, "lastname").send_keys(contact.last_name)
        wd.find_element(by.NAME, "nickname").click()
        wd.find_element(by.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(by.NAME, "company").click()
        wd.find_element(by.NAME, "company").send_keys(contact.company)
        wd.find_element(by.NAME, "address").click()
        wd.find_element(by.NAME, "address").click()
        wd.find_element(by.NAME, "address").click()
        wd.find_element(by.NAME, "address").click()
        wd.find_element(by.NAME, "address").send_keys(contact.address)
        wd.find_element(by.NAME, "home").click()
        wd.find_element(by.NAME, "home").send_keys(contact.home)
        wd.find_element(by.NAME, "mobile").click()
        wd.find_element(by.NAME, "mobile").send_keys(contact.phone)
        wd.find_element(by.NAME, "work").click()
        wd.find_element(by.NAME, "work").send_keys(contact.work)
        wd.find_element(by.NAME, "email").click()
        wd.find_element(by.NAME, "email").send_keys(contact.email)


    def open_contacts_page(self):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.LINK_TEXT, "home page").click()


    def open_edit_page(self):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.XPATH, "//table[@id='maintable']/tbody/tr[3]/td[8]/a/img").click()



    def edit_first_one(self, contact):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.NAME, "firstname").click()
        wd.find_element(by.NAME, "firstname").clear()
        wd.find_element(by.NAME, "firstname").send_keys(contact.name)
        wd.find_element(by.NAME, "middlename").click()
        wd.find_element(by.NAME, "middlename").clear()
        wd.find_element(by.NAME, "middlename").send_keys(contact.middle_name)
        wd.find_element(by.NAME, "lastname").click()
        wd.find_element(by.NAME, "lastname").clear()
        wd.find_element(by.NAME, "lastname").send_keys(contact.last_name)
        wd.find_element(by.NAME, "nickname").click()
        wd.find_element(by.NAME, "nickname").clear()
        wd.find_element(by.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(by.NAME, "company").click()
        wd.find_element(by.NAME, "company").clear()
        wd.find_element(by.NAME, "company").send_keys(contact.company)
        wd.find_element(by.NAME, "address").click()
        wd.find_element(by.NAME, "address").clear()
        wd.find_element(by.NAME, "address").send_keys(contact.address)
        wd.find_element(by.NAME, "home").click()
        wd.find_element(by.NAME, "home").clear()
        wd.find_element(by.NAME, "home").send_keys(contact.home)
        wd.find_element(by.NAME, "mobile").click()
        wd.find_element(by.NAME, "mobile").clear()
        wd.find_element(by.NAME, "mobile").send_keys(contact.phone)
        wd.find_element(by.NAME, "work").click()
        wd.find_element(by.NAME, "work").clear()
        wd.find_element(by.NAME, "work").send_keys(contact.work)
        wd.find_element(by.NAME, "email").click()
        wd.find_element(by.NAME, "email").clear()
        wd.find_element(by.NAME, "email").send_keys(contact.email)


    def update(self):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.XPATH, "//input[@value='Update']").click()






    def delete_first_one(self):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.NAME, "selected[]").click()
        wd.find_element(by.XPATH, "//input[@value='Delete']").click()

    def save(self):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.XPATH, "//div[@id='content']/form/input[20]").click()


    def return_to_homepage(self):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.LINK_TEXT, "home page").click()