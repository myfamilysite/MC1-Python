# Initialize the counter variable at 10
count = 10

# Continue the loop as long as count is greater than 0
while count > 0:
    # Check if the current number is divisible by 3 using the modulo operator
    if count % 3 == 0:
        # If divisible by 3, skip the print statement and decrement the count
        count -= 1
        continue

    # Print the current number if it is not divisible by 3
    print(count)

    # Decrement the count for the next iteration
    count -= 1






