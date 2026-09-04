# Write a function called check_positive that takes a number as an argument. If the number is positive, print "Positive number." If it is zero or negative, return None.
def check_positive(num):
    if num > 0:
        print("Positive number.")
    else:
        return None

# Testing the function
check_positive(5)
check_positive(-3)
check_positive(0)




