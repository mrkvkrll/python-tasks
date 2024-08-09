# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
    
    def test_add_new_contact(self):
        wd = self.wd
        self.open_addressbook(wd)
        self.login(wd)
        self.open_add_contact_page(wd)
        self.create_contact(wd, name="petr", middle_name="petrovich", last_name="petrov", nickname="ptr", company="yandex", address="minin strasse", home="587676586896",
                            phone="56253687263", work="2342341323", email="petr@yandex.ru")
        self.save_contact(wd)
        self.go_to_homepage(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def go_to_homepage(self, wd):
        wd.find_element(By.LINK_TEXT, "home page").click()

    def save_contact(self, wd):
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()

    def create_contact(self, wd, name, middle_name, last_name, nick, company, address, home, mobile, work, email):
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").send_keys(name)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").send_keys(middle_name)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").send_keys(last_name)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").send_keys(nick)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").send_keys(company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").send_keys(address)
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").send_keys(home)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").send_keys(mobile)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").send_keys(work)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").send_keys(email)

    def open_add_contact_page(self, wd):
        wd.find_element(By.LINK_TEXT, "add new").click()

    def login(self, wd):
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_addressbook(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
