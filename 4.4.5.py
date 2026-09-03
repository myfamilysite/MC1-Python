#!/usr/bin/env python
# coding: utf-8

# In[3]:


# You have a list of dictionaries representing students and their grades. Sort the list by grades in ascending order using a lambda function. 

students = [

    {"name": "Alice", "grade": 85},

    {"name": "Bob", "grade": 75},

    {"name": "Charlie", "grade": 90}

]

sorted_list = sorted(students, key=lambda x:x["grade"])
print(sorted_list)


# In[ ]:




