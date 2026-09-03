#!/usr/bin/env python
# coding: utf-8

# In[12]:


class Student:
    def __init__(self, name:str, age:int, grade:str):
        self.name = name  # Attribute for student name
        self.age = age  # Attribute for student age
        self.grade = grade  # Attribute for student grade

    def get_info(self):  # Method to get student information
        return f"My name is {self.name} , I am {self.age} years old and I am in the {self.grade}."

    def update_grade(self, new_grade): # Method to change the grade
        self.grade = new_grade
        print(f"The grade has been updated to {self.grade}.")


student1 = Student("Alice", 14, "8th Grade")
student2 = Student("Bob", 15 , "9th Grade")
student3 = Student("Charlie", 13, "7th Grade")

print(student1.get_info()) 
print(student2.get_info())  
print(student3.get_info())  

student1.update_grade("9th Grade")
print(student1.get_info())



# In[ ]:




