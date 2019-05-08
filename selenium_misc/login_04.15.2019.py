# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False

class Hhh041219(unittest.TestCase):
   def setUp(self):
       self.driver = webdriver.Firefox(capabilities=cap)
       self.driver.implicitly_wait(30)
       self.base_url = "http://localhost:32181/ords/f?p=100:LOGIN_DESKTOP"
       self.verificationErrors = []
       self.accept_next_alert = True
  
   def test_hhh041219(self):
       driver = self.driver
       driver.get(self.base_url)
       driver.find_element_by_name("P9999_USERNAME").send_keys("Hayden")
       driver.find_element_by_name("P9999_PASSWORD").send_keys("Oradoc_db1")
       driver.find_element_by_class_name('t-Button').click()
       time.sleep(5)
  
   def is_element_present(self, how, what):
       try: self.driver.find_element(by=how, value=what)
       except NoSuchElementException as e: return False
       return True
  
   def is_alert_present(self):
       try: self.driver.switch_to_alert()
       except NoAlertPresentException as e: return False
       return True
  
   def close_alert_and_get_its_text(self):
       try:
           alert = self.driver.switch_to_alert()
           alert_text = alert.text
           if self.accept_next_alert:
               alert.accept()
           else:
               alert.dismiss()
           return alert_text
       finally: self.accept_next_alert = True
  
   def tearDown(self):
       self.driver.quit()
       self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
   unittest.main()