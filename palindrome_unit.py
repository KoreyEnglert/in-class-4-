import unittest
import palindrome

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assert(palindrome.verify("aba"));
