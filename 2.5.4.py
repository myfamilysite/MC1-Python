#!/usr/bin/env python
# coding: utf-8

# In[31]:


temperature = int(input("What is the temperature?"))
humidity = int(input("What is the humidity?"))

if temperature > 30:
    print("It's hot outside.")
    if humidity > 70:
        print("It's also humid.")
else:
    print("The weather is nice.")



# In[ ]:




