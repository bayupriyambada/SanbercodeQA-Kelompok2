import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

url = "https://itera-qa.azurewebsites.net/"
driverInstall = ChromeDriverManager().install()


class TestLogin(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(
            options=options, service=Service(driverInstall))
        self.browser.maximize_window()

    def test_a_success_logout(self):
        # stepds
        browser = self.browser  # buka web browser
        browser.get(url)  # buka situs
        time.sleep(3)

        # isi email
        browser.find_element(
            By.XPATH, "/html/body/nav/div/form/ul/li[2]/a").click()
        browser.find_element(By.ID, "Username").send_keys(
            "testing01")  # isi email
        time.sleep(1)
        browser.find_element(By.ID, "Password").send_keys(
            "123456")  # isi password
        time.sleep(1)
        browser.find_element(By.NAME, "login").click()  # klik tombol sign in
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(
            By.XPATH, "/html/body/nav/div/form/ul/li[2]/a").click()

        # validasi
    #     response_data = browser.find_element(By.ID,"swal2-title").text
    #     response_message = browser.find_element(By.ID,"swal2-content").text

    #     self.assertIn('Welcome', response_data)
    #     self.assertEqual(response_message, 'Anda Berhasil Login')

    # def test_a_failed_login_with_empty_password(self):
    #     # steps
    #     browser = self.browser #buka web browser
    #     browser.get(url) # buka situs
    #     time.sleep(3)
    #     browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
    #     time.sleep(1)
    #     browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # isi password
    #     time.sleep(1)
    #     browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
    #     time.sleep(1)

    #     # validasi
    #     response_data = browser.find_element(By.ID,"swal2-title").text
    #     response_message = browser.find_element(By.ID,"swal2-content").text

    #     self.assertIn('not found', response_data)
    #     self.assertEqual(response_message, 'Email atau Password Anda Salah')

    # def test_a_failed_login_with_empty_email_and_password(self):
    #     # steps
    #     browser = self.browser #buka web browser
    #     browser.get(url) # buka situs
    #     time.sleep(3)
    #     browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") # isi email
    #     time.sleep(1)
    #     browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # isi password
    #     time.sleep(1)
    #     browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
    #     time.sleep(1)

    #     # validasi
    #     response_data = browser.find_element(By.ID,"swal2-title").text
    #     response_message = browser.find_element(By.ID,"swal2-content").text

    #     self.assertIn('tidak valid', response_data)
    #     self.assertEqual(response_message, 'Cek kembali email anda')

    # def tearDown(self):
    #     self.browser.close()


if __name__ == "__main__":
    unittest.main()
