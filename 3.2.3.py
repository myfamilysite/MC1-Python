# Loop through numbers from 1 to 10
for i in range(1, 11):
    # Check if the number is odd using the modulo operator
    # If the remainder when divided by 2 is not 0, it is odd
    if i % 2 != 0:
        # Skip the rest of the loop for odd numbers
        continue
    # Print the number if it is even
    print(i)







