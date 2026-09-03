#!/usr/bin/env python
# coding: utf-8

# In[3]:


import unittest

# The function to be tested
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

# The unit tests
class TestDivideFunction(unittest.TestCase):

    def test_divide_positive_numbers(self):
        # Test that dividing two positive numbers returns the correct result
        self.assertEqual(divide(10, 5), 2.0)
        self.assertEqual(divide(8, 4), 2.0)
        self.assertEqual(divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        # Test that dividing by zero raises a ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()

