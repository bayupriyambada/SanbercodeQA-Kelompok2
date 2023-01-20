import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestCreate(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_01_success_create(self): 
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
        browser.find_element(By.XPATH,"/html/body/div/div/p[1]/a").click() # klik tombol create
        time.sleep(1)
        browser.find_element(By.ID,"Name").send_keys("ilham") # isi name
        time.sleep(1)
        browser.find_element(By.ID,"Company").send_keys("go-to") # isi company
        time.sleep(1)
        browser.find_element(By.ID,"Address").send_keys("jl.blablabla") # isi address
        time.sleep(1)
        browser.find_element(By.ID,"City").send_keys("klaten") # isi city
        time.sleep(1)
        browser.find_element(By.ID,"Phone").send_keys("089786780") # isi phone
        time.sleep(1)
        browser.find_element(By.ID,"Email").send_keys("ilham@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/form/div/div[7]/div/input").click() # klik tombol create
        time.sleep(1)

    def test_02_failed_create_with_balnk_data(self): 
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
        browser.find_element(By.XPATH,"/html/body/div/div/p[1]/a").click() # klik tombol create
        time.sleep(1)
        browser.find_element(By.ID,"Name").send_keys("") # isi name
        time.sleep(1)
        browser.find_element(By.ID,"Company").send_keys("") # isi company
        time.sleep(1)
        browser.find_element(By.ID,"Address").send_keys("") # isi address
        time.sleep(1)
        browser.find_element(By.ID,"City").send_keys("") # isi city
        time.sleep(1)
        browser.find_element(By.ID,"Phone").send_keys("") # isi phone
        time.sleep(1)
        browser.find_element(By.ID,"Email").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/form/div/div[7]/div/input").click() # klik tombol create
        time.sleep(2)

unittest.main()