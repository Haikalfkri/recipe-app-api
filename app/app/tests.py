"""
Sample Test
"""

from django.test import SimpleTestCase
from . import Calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""
    
    def test_add_numbers(self):
        """Testing adding numbers together"""
        res = Calc.add(5, 6)
        
        self.assertEqual(res, 11)
        
    def test_subtract_numbers(self):
        """Testing subtracting numbers"""
        res = Calc.subtract(15, 10)
        
        self.assertEqual(res, 5)