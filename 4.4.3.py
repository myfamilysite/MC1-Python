#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Given a list of numbers, use a lambda function to create a new list that contains the squares of each number.

numbers = [1, 4, 5, 6]

squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

