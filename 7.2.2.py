#!/usr/bin/env python
# coding: utf-8

# In[5]:


try:
    file = open("data.txt", "r")
    content = file.read()

except FileNotFoundError:
    print("File not found.")

finally:
    if 'file' in locals(): # use the if statement to check if the file was opened in the first place.
        file.close()
        print("File closed.")


# In[ ]:




