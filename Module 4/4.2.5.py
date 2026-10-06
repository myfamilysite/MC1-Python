# Create a void function named print_even_numbers that takes a number n and prints all even numbers from 0 to n. 
def print_even_numbers(n):
    for i in range(n+1):
        if i%2==0:
            print(i)

# Testing the function
print_even_numbers(10)

#Alternative method
def print_even_numbers(n):
    for i in range(0, n + 1, 2): #This gives the start and end of range but counts in 2's
        print(i)


# Test and Evaluate
print_even_numbers(10)




