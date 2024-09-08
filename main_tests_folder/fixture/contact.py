from main_tests_folder.model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app


    def create_new_one(self, contact):
        wd = self.app.wd
        by = self.app.by
        self.app.open_home_page()
        self.open_contacts_page()
        wd.find_element(by.LINK_TEXT, "add new").click()
        self.filling_out_contact_forms(contact)
        wd.find_element(by.XPATH, "//div[@id='content']/form/input[20]").click()
        self.return_to_homepage()



    def filling_out_contact_forms(self, contact):
        self.change_field_name("firstname", contact.name)
        self.change_field_name("middlename", contact.middle_name)
        self.change_field_name("lastname", contact.last_name)
        self.change_field_name("nickname", contact.nickname)
        self.change_field_name("company", contact.company)
        self.change_field_name("address", contact.address)
        self.change_field_name("home", contact.home)
        self.change_field_name("mobile", contact.phone)
        self.change_field_name("work", contact.work)
        self.change_field_name("email", contact.email)

    def change_field_name(self, field_name, text):
        wd = self.app.wd
        by = self.app.by
        if text is not None:
            wd.find_element(by.NAME, field_name).click()
            wd.find_element(by.NAME, field_name).clear()
            wd.find_element(by.NAME, field_name).send_keys(text)

    def open_contacts_page(self):
        wd = self.app.wd
        by = self.app.by
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements(by.CSS_SELECTOR, "tr[name = 'entry']")) > 0):
            wd.find_element(by.LINK_TEXT, "home").click()

    def download(self):
        wd = self.app.wd
        by = self.app.by
        wd.find_element(by.XPATH, "//img[@alt='vCard']").click()


    def edit_first_one_contact(self, contact):
        wd = self.app.wd
        by = self.app.by
        self.app.open_home_page()
        self.open_contacts_page()
        # wd.find_element(by.XPATH, "//table[@id='maintable']/tbody/tr[3]/td[8]/a/img").click()
        wd.find_element(by.NAME, "selected[]").click()
        wd.find_element(by.XPATH, "//img[@alt='Edit']").click()
        self.filling_out_contact_forms(contact)
        wd.find_element(by.XPATH, "//input[@value='Update']").click()
        self.return_to_homepage()


    def delete_first_one(self):
        wd = self.app.wd
        by = self.app.by
        self.app.open_home_page()
        self.open_contacts_page()
        wd.find_element(by.NAME, "selected[]").click()
        wd.find_element(by.XPATH, "//input[@value='Delete']").click()



    def return_to_homepage(self):
        wd = self.app.wd
        by = self.app.by
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements(by.CSS_SELECTOR, "tr[name = 'entry']")) > 0):
            wd.find_element(by.LINK_TEXT, "home page").click()


    def count(self):
        wd = self.app.wd
        by = self.app.by
        self.app.open_home_page()
        self.open_contacts_page()
        return len(wd.find_elements(by.NAME, "selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        by = self.app.by
        self.open_contacts_page()
        cards = []
        for element in wd.find_elements(by.CSS_SELECTOR, "tr[name = 'entry']"):
            id = element.find_element(by.NAME, "selected[]").get_attribute("value")
            td_elements = element.find_elements(by.TAG_NAME, "td")
            text_element = td_elements[2].text
            cards.append(Contact(name=text_element, id=id))
        return cards
