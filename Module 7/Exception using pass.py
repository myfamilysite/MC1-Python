# 1. Define the custom exception using the clean, inherited approach
class MyCustomError(Exception):
    pass


def check_age(age):
    if age < 18:
        # 2. Raise the custom error when a condition fails
        raise MyCustomError("Access denied: You must be at least 18 years old.")
    else:
        print("Access granted! Welcome.")


# 3. Handle the custom exception using a try-except block
try:
   check_age(19)

except MyCustomError as e:
    # 4. Catch the specific error and print the message stored inside it
    print(f"Caught a custom error -> {e}")

finally:
    print("Execution complete.")