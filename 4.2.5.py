#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create a void function named print_even_numbers that takes a number n and prints all even numbers from 0 to n. 
def print_even_numbers(n):
    for i in range(n+1):
        if i%2==0:
            print(i)

# Testing the function
print_even_numbers(10)



# In[ ]:




