#!/usr/bin/env python
# coding: utf-8

# In[6]:


fruits = ["apple", "banana", "cherry", "date"]

# append "elderberry"
fruits.append("elderberry")
print(fruits)

# remove "banana"
fruits.remove("banana")
print(fruits)

# Use the pop() method to remove and return the last item in the list
last_item = fruits.pop()
print(fruits)


