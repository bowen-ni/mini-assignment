# unitTest_math_functions.py
import unittest
from math_functions import power, divide

class TestMathFunctions(unittest.TestCase):

    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)  # 5^0 = 1

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(power(4, -2), 0.0625)  # 4^-2 = 1/16

    def test_power_zero_base(self):
        self.assertEqual(power(0, 3), 0)  # 0^3 = 0

    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)  # 0 divided by any number is 0

    def test_divide_negative_values(self):
        self.assertEqual(divide(-10, 2), -5)  # Negative numerator

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)  # Division by zero raises ValueError

if __name__ == '__main__':
    unittest.main()

