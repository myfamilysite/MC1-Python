class AgeTooYoungError(Exception):
   pass

try:
   age = int(input("Please enter your age: "))

    # Add a condition to check if the age is greater than or equal to 18
   if age < 18:
        raise AgeTooYoungError("You must be 18 years or older to vote.")
   else:
        print("You are eligible to vote")

except AgeTooYoungError as e:
   print(f"Error: {e}")

except ValueError:
    # This catches errors if the user types a letter instead of a number
   print("Error: Please enter a valid integer.")




