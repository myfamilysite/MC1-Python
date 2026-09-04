try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator/denominator
    print (result)

except ZeroDivisionError:
    print ("You cannot divide by zero. Please enter a non-zero number for the denominator")

except ValueError:
    print ("Please enter only numbers")

