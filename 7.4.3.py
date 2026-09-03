#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest

def calculate_average(numbers):
    # Check if the list is empty
    if not numbers:
        raise ValueError("The list cannot be empty.")

    # Check if all elements are numeric (int or float)
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements in the list must be numbers.")

    total = sum(numbers)
    count = len(numbers)

    return total / count

class TestCalculateAverage(unittest.TestCase):

    def test_empty_list_raises_value_error(self):
        """Test that an empty list raises a ValueError."""
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_valid_integers(self):
        """Test with a standard list of positive integers."""
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)

    def test_valid_floats(self):
        """Test with a list containing floating-point numbers."""
        self.assertEqual(calculate_average([1.5, 2.5, 3.5]), 2.5)

    def test_negative_numbers(self):
        """Test with a list containing negative numbers."""
        self.assertEqual(calculate_average([-10, -5, 0, 5, 10]), 0.0)

    def test_non_numeric_raises_type_error(self):
        """Test that a list with strings or other types raises a TypeError."""
        with self.assertRaises(TypeError):
            calculate_average([1, 2, 'three', 4])

        with self.assertRaises(TypeError):
            calculate_average([1, None, 3])

# Code to run the tests directly within your Jupyter Notebook
if __name__ == '__main__': 
    unittest.main()


# In[ ]:




