# list of numbers from 1 to 30 that are both multiples of 3 and even, using a conditional list comprehension with multiple conditions.
numbers = [x for x in range(1, 31) if x % 3 == 0 and x % 2 == 0]
print(numbers)


