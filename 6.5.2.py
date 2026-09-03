#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Create a Vehicle class with a method fuel_efficiency
class Vehicle:
    def fuel_efficiency(self):
        return "Something MPG"

# Create a subclass called Car
class Car(Vehicle):
    def __init__(self, mpg):
        self.mpg = mpg

    def fuel_efficiency(self):
        return f"Car = {self.mpg} MPG"       # Overide the method for Truck

# Create a subclass called Truck
class Truck(Vehicle):
    def __init__(self, mpg):
        self.mpg = mpg

    def fuel_efficiency(self):
        return f"Truck = {self.mpg} MPG"       # Overide the method for Truck

# Call the functions
my_car = Car(30)
print (my_car.fuel_efficiency())

my_truck = Truck(15)
print (my_truck.fuel_efficiency())

