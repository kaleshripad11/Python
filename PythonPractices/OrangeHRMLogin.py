'''
Created on 07-Jun-2020

@author: shree
https://opensource-demo.orangehrmlive.com/
'''
from selenium import webdriver as w
import time as t

print("1. Modules imported")

class OrangeHRMLogin:
    driver = w.Firefox()
    print("2. Driver instantiated")
        
    def openURL(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.fullscreen_window()
        print("3. URL and Window loaded")
    def loginHRM(self):
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        print("4. Login Succeded")
        
    def closeBrowser(self):
        t.sleep(20)
        self.driver.close()
        print("5. Closing browser")
        
cms = OrangeHRMLogin()
cms.openURL()
cms.loginHRM()
cms.closeBrowser()
