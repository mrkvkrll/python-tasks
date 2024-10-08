from main_tests_folder.model.contact import Contact
import re

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
        self.contact_cache = None



    def filling_out_contact_forms(self, contact):
        self.change_field_name("firstname", contact.first_name)
        self.change_field_name("middlename", contact.middle_name)
        self.change_field_name("lastname", contact.last_name)
        self.change_field_name("nickname", contact.nickname)
        self.change_field_name("company", contact.company)
        self.change_field_name("address", contact.address)
        self.change_field_name("home", contact.home_phone)
        self.change_field_name("mobile", contact.phone)
        self.change_field_name("work", contact.work_phone)
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


    def edit_first_one_contact(self):
        self.edit_contact_by_index(0)


    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        by = self.app.by
        self.app.open_home_page()
        self.open_contacts_page()
        self.select_contact_by_index(index)
        wd.find_element(by.XPATH, "//img[@alt='Edit']").click()
        self.filling_out_contact_forms(contact)
        wd.find_element(by.XPATH, "//input[@value='Update']").click()
        self.return_to_homepage()
        self.contact_cache = None


    def delete_first_one(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        by = self.app.by
        self.app.open_home_page()
        self.open_contacts_page()
        self.select_contact_by_index(index)
        wd.find_element(by.XPATH, "//input[@value='Delete']").click()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        by = self.app.by
        wd.find_elements(by.NAME, "selected[]")[index].click()

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

    contact_cache = None


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            by = self.app.by
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements(by.CSS_SELECTOR, "tr[name = 'entry']"):
                td_elements = element.find_elements(by.TAG_NAME, "td")
                id = td_elements[0].find_element(by.TAG_NAME, "input").get_attribute("value")
                last_name = td_elements[1].text
                first_name = td_elements[2].text
                all_phones = td_elements[5].text
                self.contact_cache.append(Contact(last_name=last_name, first_name=first_name, id=id,
                all_phones_from_home_page =all_phones))
        return list(self.contact_cache)


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        by = self.app.by
        self.app.open_home_page()
        self.open_contacts_page()
        element = wd.find_elements(by.CSS_SELECTOR, "tr[name = 'entry']")[index]
        cell = element.find_elements(by.TAG_NAME, "td")[7]
        cell.find_element(by.TAG_NAME, "a").click()


    def open_view_contact_by_index(self, index):
        wd = self.app.wd
        by = self.app.by
        self.app.open_home_page()
        self.open_contacts_page()
        element = wd.find_elements(by.CSS_SELECTOR, "tr[name = 'entry']") [index]
        cell = element.find_elements(by.TAG_NAME, "td") [6]
        cell.find_element(by.TAG_NAME, "a").click()


    def get_contact_info_from_edit_page(self, index):
            wd = self.app.wd
            by = self.app.by
            self.open_contact_to_edit_by_index(index)
            id = wd.find_element(by.NAME, "id").get_attribute("value")
            first_name = wd.find_element(by.NAME, "firstname").get_attribute("value")
            last_name = wd.find_element(by.NAME, "lastname").get_attribute("value")
            home_phone = wd.find_element(by.NAME, "home").get_attribute("value")
            phone = wd.find_element(by.NAME, "mobile").get_attribute("value")
            work_phone = wd.find_element(by.NAME, "work").get_attribute("value")
            return Contact(id=id, first_name=first_name, last_name=last_name,
                           home_phone=home_phone, phone=phone, work_phone=work_phone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        by = self.app.by
        self.open_view_contact_by_index(index)
        text = wd.find_element(by.ID, "content").text
        home_phone = re.search("H: (.*)", text).group(1)
        phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        return Contact(home_phone=home_phone, phone=phone, work_phone=work_phone)








