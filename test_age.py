import unittest
from age import categorize_by_age

class TestCategorizeByAge(unittest.TestCase):
    def test_child(self):
        self.assertEqual(categorize_by_age(6), "Child")
    def test_adolescent(self):
        self.assertEqual(categorize_by_age(15), "Adolescent")
    def test_adult(self):
        self.assertEqual(categorize_by_age(40), "Adult")
    def test_golden_age(self):
        self.assertEqual(categorize_by_age(75),"Golden age")
    def negative_age(self):
        self.assertEqual(categorize_by_age(-10), "Invalid age: -1")
    def test_too_old(self):
        self.assertEqual(categorize_by_age(200), "Invalid age: 200")
        
if __name__ == "__main__":
    unittest.main()