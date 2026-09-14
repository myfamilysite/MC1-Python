# Given a list of integers, use a lambda function to filter out all the odd numbers.

numbers = [10, 15, 20, 25, 30]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)



