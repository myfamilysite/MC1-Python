#!/usr/bin/env python
# coding: utf-8

# In[11]:


class NegativeNumberError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
   number = int(input("Please enter a number greater than zero: "))

    # Add a condition to check if the number is negative
   if number < 0:
        raise NegativeNumberError("The number must be positive.")
   else:
        print(f"Correct! The number {number} which you entered is greater than zero")

except NegativeNumberError as e:
   print(f"Error: {e.message}")

except ValueError:
    # This catches errors if the user types a letter instead of a number
   print("Error: Please enter a valid integer.")


# In[ ]:





# In[ ]:




