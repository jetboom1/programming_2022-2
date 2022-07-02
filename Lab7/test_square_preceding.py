import unittest
from square_preceding import *
import coverage

class TestFunction(unittest.TestCase):
    def setUp(self) -> None:
        self.a = [3,5,8]
        self.b = [0, 0, 0]
        self.c = []
        self.d = [1,2,'abc', 4]
        self.f = [1, 2.5, 1.2, 4]
    def test_regular_case(self):
        square_preceding(self.a)
        self.assertEqual(self.a, [0,9,25])
    def test_all_zeros(self):
        square_preceding(self.b)
        self.assertEqual(self.b, [0, 0, 0])
    def test_empty_list(self):
        square_preceding(self.c)
        self.assertEqual(self.c, [])
    def test_not_numbers(self):
        square_preceding(self.d)
        self.assertEqual(self.d, [0, 1, 4, 'abc'])
    def test_floats(self):
        square_preceding(self.f)
        self.assertEqual(self.f, [0, 1, 6.25, 1.44])

if __name__ == '__main__':
    unittest.main()