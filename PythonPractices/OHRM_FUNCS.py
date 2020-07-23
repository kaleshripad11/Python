'''
Created on 08-Jun-2020

@author: shree
'''
from selenium import webdriver as w


class OrangeHRMFuncs:
    def __init__(self):
        self.driver = w.Firefox()
        #driver.get("")
        
    def loginHRM(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        
    def logoutHRM(self):
        #t.sleep(1)
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_link_text("Logout").click()
        #print("5. Logout successful")
        
hrm = OrangeHRMFuncs()
hrm.loginHRM()
        