#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_user_input():
    while True:
        user_input = input("Enter a number: ")
        try:
            # Attempt to convert the input to an integer
            return int(user_input)
        except ValueError:
            # Catch the error if the input is not a valid integer
            print("Invalid input. Please enter a valid integer.")

result = get_user_input()
print(f"You entered: {result}")


# In[ ]:




