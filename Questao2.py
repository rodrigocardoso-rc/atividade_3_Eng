import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestGoogleDoodle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        self.driver.get("http://the-internet.herokuapp.com/login")

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
        password.send_keys(Keys.ENTER)

        time.sleep(2)
        self.assertIn("secure", self.driver.current_url.lower())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()