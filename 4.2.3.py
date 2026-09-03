#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create a function named min_max that takes a list of numbers as an argument and returns the smallest and largest numbers in the list

def min_max(numbers):
    return min(numbers), max(numbers)

# Testing the function
result = min_max([3, 1, 4, 1, 5, 9])
print (result)

