import unittest
import word_count

class TestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(word_count.count("I like pie."), 3);

    def test_add2(self):
        self.assertEqual(word_count.count("I like pie."), 4);

    def test_add3(self):
        self.assertEqual(word_count.count("I li ke pie."), 3);

    def test_add4(self):
        self.assertEqual(word_count.count("I li ke pie."), 4);

    def test_add5(self):
        self.assertEqual(word_count.count("I li       ke pie."), 3);

    def test_add6(self):
        self.assertEqual(word_count.count("I li       ke pie."), 4);

if __name__ == '__main__':
    unittest.main()
