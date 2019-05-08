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
       self.base_url = "https://google.com"
       self.verificationErrors = []
       self.accept_next_alert = True
  
   def test_hhh041219(self):
       driver = self.driver
       driver.get(self.base_url + "/search?source=hp&ei=-XKxXKn7LZGCk-4P-Jq5oA8&q=demo&btnK=Google+Search&oq=demo&gs_l=psy-ab.3..0i131j0l3j0i131j0l5.14237.14569..15148...0.0..0.66.246.4......0....1..gws-wiz.....0.7S_fl0HTvuA")
       driver.find_element_by_name("q").click()
       driver.find_element_by_name("q").clear()
       driver.find_element_by_name("q").send_keys("demo plugin")
  
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