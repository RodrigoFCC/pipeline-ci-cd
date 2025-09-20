import unittest
import os
from datetime import datetime
from main import main

class TestMain(unittest.TestCase):
    
    def setUp(self):
        """Executado antes de cada teste"""
        if os.path.exists("output.txt"):
            os.remove("output.txt")
    
    def tearDown(self):
        """Executado após cada teste"""
        if os.path.exists("output.txt"):
            os.remove("output.txt")
    
    def test_main_creates_file(self):
        """Testa se o arquivo output.txt é criado"""
        main()
        self.assertTrue(os.path.exists("output.txt"))
    
    def test_file_contains_timestamp(self):
        """Testa se o arquivo contém a string 'Última execução:'"""
        main()
        with open("output.txt", "r") as file:
            content = file.read()
            self.assertIn("Última execução:", content)
    
    def test_file_format(self):
        """Testa se o arquivo tem o formato correto"""
        main()
        with open("output.txt", "r") as file:
            content = file.read()
            # Verifica se começa com o texto esperado
            self.assertTrue(content.startswith("Última execução: "))
            # Verifica se tem pelo menos 20 caracteres (texto + timestamp)
            self.assertGreaterEqual(len(content), 20)

if __name__ == "__main__":
    unittest.main()