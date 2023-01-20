import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestSearch(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_01_success_delete(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://itera-qa.azurewebsites.net/") # buka situs
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/nav/div/form/ul/li[2]/a").click() # klik tombol login
        time.sleep(1)
        browser.find_element(By.ID,"Username").send_keys("test-login") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"Password").send_keys("login123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() # klik tombol login
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr[3]/td[7]/a[3]").click() # klik tombol delete   
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div/form/div/input").click() # klik tombol delete   
        time.sleep(2)

    def test_02_failed_delete(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://itera-qa.azurewebsites.net/") # buka situs
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/nav/div/form/ul/li[2]/a").click() # klik tombol login
        time.sleep(1)
        browser.find_element(By.ID,"Username").send_keys("test-login") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"Password").send_keys("login123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() # klik tombol login
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr[3]/td[7]/a[3]").click() # klik tombol delete   
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div/form/div/a").click() # klik tombol back to list   
        time.sleep(2)

unittest.main()
