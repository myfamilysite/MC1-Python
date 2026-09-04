# Create the vehicle class

class Vehicle:
    def __init__(self, make, model):       # Initialise the class
        self.make = make
        self.model = model

    def info(self):              # Define the method
        return f"Car Make: {self.make}, Model: {self.model}"

# Create the Car subclass

class Car(Vehicle):
    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)       # Passes make & model to the Vehicle class
        self.number_of_doors = number_of_doors

    def info(self):         # Overide the method
        return f"Car Make: {self.make}, Model: {self.model}, Doors: {self.number_of_doors}"

# Create the Truck class

class Truck(Vehicle):
    def __init__(self, make, model, payload_capacity):
        super().__init__(make, model)    # Passes make & model to the Vehicle class
        self.payload_capacity = payload_capacity

    def info(self):            # Overide the method 
        return f"Truck Make: {self.make}, Model: {self.model}, Payload Capacity: {self.payload_capacity} kg"

my_car = Car("Toyota", "Corolla", 4)
print(my_car.info())  

my_truck = Truck("Ford", "F-150", 1000)
print(my_truck.info())



