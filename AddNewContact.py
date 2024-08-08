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
        wd.get("http://localhost/addressbook/")
        wd.find_element(By.NAME,"user").clear()
        wd.find_element(By.NAME,"user").send_keys("admin")
        wd.find_element(By.NAME,"pass").clear()
        wd.find_element(By.NAME,"pass").send_keys("secret")
        wd.find_element(By.XPATH,"//input[@value='Login']").click()
        wd.get("http://localhost/addressbook/")
        wd.find_element(By.LINK_TEXT,"add new").click()
        wd.find_element(By.NAME,"firstname").click()
        wd.find_element(By.NAME,"firstname").clear()
        wd.find_element(By.NAME,"firstname").send_keys("petr")
        wd.find_element(By.NAME,"middlename").click()
        wd.find_element(By.NAME,"middlename").clear()
        wd.find_element(By.NAME,"middlename").send_keys("petrovich")
        wd.find_element(By.NAME,"lastname").click()
        wd.find_element(By.NAME,"lastname").clear()
        wd.find_element(By.NAME,"lastname").send_keys("petrov")
        wd.find_element(By.NAME,"nickname").click()
        wd.find_element(By.NAME,"nickname").clear()
        wd.find_element(By.NAME,"nickname").send_keys("ptr")
        wd.find_element(By.NAME,"company").click()
        wd.find_element(By.NAME,"company").clear()
        wd.find_element(By.NAME,"company").send_keys("yandex")
        wd.find_element(By.NAME,"address").click()
        wd.find_element(By.NAME,"address").click()
        wd.find_element(By.NAME,"address").click()
        wd.find_element(By.NAME,"address").click()
        wd.find_element(By.NAME,"address").clear()
        wd.find_element(By.NAME,"address").send_keys("minin strasse")
        wd.find_element(By.NAME,"home").click()
        wd.find_element(By.NAME,"home").clear()
        wd.find_element(By.NAME,"home").send_keys("587676586896")
        wd.find_element(By.NAME,"mobile").click()
        wd.find_element(By.NAME,"mobile").clear()
        wd.find_element(By.NAME,"mobile").send_keys("56253687263")
        wd.find_element(By.NAME,"work").click()
        wd.find_element(By.NAME,"work").clear()
        wd.find_element(By.NAME,"work").send_keys("2342341323")
        wd.find_element(By.NAME,"email").click()
        wd.find_element(By.NAME,"email").clear()
        wd.find_element(By.NAME,"email").send_keys("petr@yandex.ru")
        wd.find_element(By.XPATH,"//div[@id='content']/form/input[20]").click()
        wd.find_element(By.LINK_TEXT,"home page").click()
        wd.find_element(By.LINK_TEXT,"Logout").click()
    
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
