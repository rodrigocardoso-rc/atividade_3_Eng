import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestGoogleDoodle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_google_doodle(self):
        self.driver.get("https://www.google.com")

        btn = self.driver.find_element(By.NAME, "btnI")
        self.driver.execute_script("arguments[0].click();", btn)

        time.sleep(10)
        self.assertIn("google doodle", self.driver.title.lower())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()