#!/usr/bin/env python
# coding: utf-8

# In[6]:


fruits = {'apple': 3, 'banana': 5, 'orange': 2}

# To get the number of 'bananas' in the dictionary using the get() method

quantity_banana = fruits.get ('banana')

print(quantity_banana)

# Use the keys() method to print all keys in the dictionary.

keys = fruits.keys()

print(keys)

# Use the values() method to print all values in the dictionary.

values = fruits.values()

print(values)

# Use the items() method to print all key-value pairs in the dictionary.

items = fruits.items()

print(items)

