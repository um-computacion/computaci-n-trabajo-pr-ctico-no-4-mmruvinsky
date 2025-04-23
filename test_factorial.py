
import unittest
from factorial import factorial_iterativo
from factorial import factorial_recursivo

class TestFactorial(unittest.TestCase):
    def test_factorial_recursivo(self):
        self.assertEqual(factorial_recursivo(0), 1)
        self.assertEqual(factorial_recursivo(1), 1)
        self.assertEqual(factorial_recursivo(2), 2)
        self.assertEqual(factorial_recursivo(3), 6)
        self.assertEqual(factorial_recursivo(4), 24)
        self.assertEqual(factorial_recursivo(5), 120)

if __name__ == '__main__':
    unittest.main()
