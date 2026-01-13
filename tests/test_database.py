"""Tests unitaires pour DatabaseManager."""
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from src.database.manager import DatabaseManager

class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.test_db = "test.db"
        self.db = DatabaseManager(self.test_db)
        self.db.connect()
        self.db.create_table()
    
    def tearDown(self):
        self.db.close()
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
    
    def test_add_contact(self):
        result = self.db.add_contact("Dupont", "Jean", "514-555-1234", "jean@test.com")
        self.assertTrue(result)
        contacts = self.db.get_all_contacts()
        self.assertEqual(len(contacts), 1)

if __name__ == "__main__":
    unittest.main()
