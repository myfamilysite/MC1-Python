# a list of all odd numbers from 1 to 20, using a conditional list comprehension to filter out the odd numbers

odd_numbers = [x for x in range(1, 21) if x % 2 != 0]
print(odd_numbers)

