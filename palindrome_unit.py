import unittest
import palindrome

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(palindrome.verify("aba"), True);

    def test_add2(self):
        self.assertEqual(palindrome.verify("aba"), False);

    def test_add3(self):
        self.assertEqual(palindrome.verify("ab a"), True);

    def test_add4(self):
        self.assertEqual(palindrome.verify("ab a"), False);

    def test_add5(self):
        self.assertEqual(palindrome.verify("123321"), True);

    def test_add6(self):
        self.assertEqual(palindrome.verify("123321"), False);

if __name__ == '__main__':
    unittest.main()
