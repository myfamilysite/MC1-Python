#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Define a global variable
score = 10

def update_score():
    # Define a local variable
    bonus_points = 5

    # Declare intent to modify the global variable
    global score 

    # Print the global variable before modification
    print("Value before modification:", score)

    # Modify the global variable using the local variable
    score = score + bonus_points

    # Print the global variable after modification
    print("Value after modification:", score)

# Call the function
update_score()

# Print outside the function to prove the global variable was changed
print("Value outside the function:", score)


# In[ ]:




