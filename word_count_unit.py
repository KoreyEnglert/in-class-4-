import unittest
import word_count

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(word_count.count("I like pie."), 3);
