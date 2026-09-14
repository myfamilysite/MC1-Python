# Create a set named fruits 

fruits = {"apple", "banana", "cherry", "apple"}

print(fruits)

# Create another set named vegetables using the set() function 

vegetables = set(["carrot", "lettuce", "spinach"])

print(vegetables)

# Add the fruit "orange" to the fruits set

fruits.add("orange")

print (fruits)

# Remove "banana" from the fruits set using the remove() method.

fruits.remove('banana')

print(fruits)

# Use the discard() method to remove "grape" from the fruits set 

fruits.discard('grape')

print(fruits)

# Check how many unique items are in the fruits set

print(len(fruits))

# Clear all elements from the vegetables set.

vegetables.clear()

print(vegetables)

# Create a set named citrus_fruits 

citrus_fruits = {"orange", "lemon", "lime"}

print (citrus_fruits)

# Find the union of fruits and citrus_fruits.

result = fruits.union(citrus_fruits)

print(result)

# Find the intersection of fruits and citrus_fruits.

result = fruits.intersection(citrus_fruits)

print(result)

# Find the difference between fruits and citrus_fruits.

result = fruits.difference(citrus_fruits)

print(result)

# Create a set named berries

berries = {"strawberry", "blueberry", "raspberry"}

print(berries)

# Find the symmetric difference between fruits and berries

result = fruits.symmetric_difference(berries)

print(result)



