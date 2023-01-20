import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url="https://itera-qa.azurewebsites.net/"
class TestLogout(unittest.TestCase): 
   

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_01_a_success_logout(self): 
        # stepds
        browser = self.browser #buka web browser
        browser.get(url) # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/nav/div/form/ul/li[2]/a").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.ID,"Username").send_keys("test-login") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"Password").send_keys("login123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/nav/div/form/ul/li[2]/a").click() # klik tombol sign in
        time.sleep(1)
        
unittest.main()