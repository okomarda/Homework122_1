import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], -3, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 2), [2])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([], 0, 5), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 6), [2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, -10), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 3, 1), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -3, 1), [2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -5, 1), [1, 2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 0, -2), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -1), "Ошибка, необходимо задать числовое значение для end")
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -2, -2), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -2, -1), [3, 4])
        self.assertEqual(arrs.my_slice([], 0), [])
