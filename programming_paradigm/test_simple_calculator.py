import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Tests for add() ---
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)

    def test_addition_with_negatives(self):
        self.assertEqual(self.calc.add(-2, 3), 1)
        self.assertEqual(self.calc.add(-5, -5), -10)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 7), 7)
        self.assertEqual(self.calc.add(9, 0), 9)

    # --- Tests for subtract() ---
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(3, 8), -5)

    def test_subtraction_with_negatives(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-2, 5), -7)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(0, 7), -7)
        self.assertEqual(self.calc.subtract(9, 0), 9)

    # --- Tests for multiply() ---
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiplication_with_negatives(self):
        self.assertEqual(self.calc.multiply(-4, 5), -20)
        self.assertEqual(self.calc.multiply(-3, -6), 18)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(7, 0), 0)

    # --- Tests for divide() ---
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_with_negatives(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-9, -3), 3)

    def test_division_with_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))  # edge case


if __name__ == "__main__":
    unittest.main()
