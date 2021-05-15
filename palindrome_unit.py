import unittest
import palindrome

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(palindrome.verify("aba"), True);

if __name__ == '__main__':
    unittest.main()
