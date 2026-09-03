#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Create a class called Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating meat."

# Create a class called Mammal that inherits from Animal
class Mammal(Animal):
    def walk(self):
        return f"{self.name} is walking on the grass."

# Create a class called Dog that inherits from Mammal
class Dog(Mammal):
    def bark(self):
        return f"{self.name} is barking at the people."

my_dog = Dog("Spotty")

print(my_dog.eat())
print(my_dog.walk())
print(my_dog.bark())

