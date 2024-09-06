import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestGoogleDoodle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_meu_ifmg(self):
        self.driver.get("https://www.ifmg.edu.br/sabara/meu-ifmg")
        self.assertIn("meu-ifmg", self.driver.current_url.lower())

    def test_cpa(self):
        self.driver.get("https://www.ifmg.edu.br/sabara/cpa")
        self.assertIn("cpa", self.driver.current_url.lower())

    def test_contato(self):
        self.driver.get("https://www.ifmg.edu.br/sabara/contato")
        self.assertIn("contato", self.driver.current_url.lower())

    def test_ex_aluno(self):
        self.driver.get("https://www.ifmg.edu.br/sabara/formulario-contato-ex-alunos")
        self.assertIn("formulario-contato-ex-alunos", self.driver.current_url.lower())

    def test_acesso_sistema(self):
        self.driver.get("https://www.ifmg.edu.br/sabara/acesso-a-sistemas")
        self.assertIn("acesso-a-sistemas", self.driver.current_url.lower())

    def test_search(self):
        self.driver.get("https://www.ifmg.edu.br/sabara")
        search = self.driver.find_element(By.NAME, "SearchableText")

        search.send_keys("meuifmg")
        search.send_keys(Keys.ENTER)

        time.sleep(4)
        self.assertIn("busca", self.driver.current_url.lower())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()