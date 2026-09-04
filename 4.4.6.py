# Write a lambda function that takes a string and returns its length. Then use this lambda function with the map() function on the following list of strings

words = ["Python", "Lambda", "Functions"]

# Define the lambda function and use map()
lengths = list(map(lambda x: len(x), words))
print(lengths)


