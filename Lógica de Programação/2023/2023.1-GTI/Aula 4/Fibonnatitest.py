import unittest
from fibonnati import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_two(self):
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_three(self):
        self.assertEqual(fibonacci(3), 2)

    def test_fibonacci_ten(self):
        self.assertEqual(fibonacci(10), 55)

if __name__ == '__main__':
    unittest.main()
