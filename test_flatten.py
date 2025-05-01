import unittest
from flatten import flatten

class TestFlatten(unittest.TestCase):
    def test_flatten(self):
        self.assertEqual(flatten([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten([1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]), [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8])
        self.assertEqual(flatten([1, 2, [3, 4], [5, [6, 7]]]), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(flatten([]), [])
        self.assertEqual(flatten([1, [2], [[3]], [[[4]]]]), [1, 2, 3, 4])
        self.assertEqual(flatten([[[[1]]], [[[[2]]]], [[[[[3]]]]]]), [1, 2, 3])
        self.assertEqual(flatten([1, [2], [3], [4], [5]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten([1, [2, [3, [4]]], 5]), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main() 