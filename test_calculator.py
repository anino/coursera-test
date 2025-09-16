"""
Test suite for the Calculator class.
This demonstrates various testing concepts and techniques.
"""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_addition(self):
        """Test addition operation."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
    
    def test_subtraction(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-2, -3), 1)
    
    def test_multiplication(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-5, -2), 10)
    
    def test_division(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertAlmostEqual(self.calc.divide(7, 3), 2.333333, places=5)
    
    def test_division_by_zero(self):
        """Test division by zero raises appropriate exception."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_power(self):
        """Test exponentiation operation."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(10, 2), 100)
        self.assertEqual(self.calc.power(-2, 3), -8)
    
    def test_is_even(self):
        """Test even number detection."""
        self.assertTrue(self.calc.is_even(2))
        self.assertTrue(self.calc.is_even(0))
        self.assertTrue(self.calc.is_even(-4))
        self.assertFalse(self.calc.is_even(3))
        self.assertFalse(self.calc.is_even(-5))


if __name__ == '__main__':
    unittest.main()