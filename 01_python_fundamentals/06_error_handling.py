# Python Error Handling

# try-except blocks:

try:
    # Code that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Code to handle the specific exception
    print("Error: Cannot divide by zero.")


# Handling multiple exceptions:

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")



# try-except-else block:
# The 'else' block executes if no exceptions occur in the 'try' block.

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ZeroDivisionError, ValueError):  # Handling multiple exceptions in a single except block
    print("Error: Invalid input or division by zero.")
else:
    print(f"Result: {result}")



# try-except-finally block:
# The 'finally' block always executes, regardless of whether an exception occurred or not.

file = None #Initialize to None

try:
    file = open("my_file.txt", "r")
    content = file.read()
    # ... process the file content ...
except FileNotFoundError:
    print("Error: File not found.")
finally:
    if file is not None and not file.closed:
        file.close()


# Raising exceptions:

def calculate_square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")  # Raise a ValueError explicitly
    # ... calculate square root if x is non-negative

try:
    calculate_square_root(-5)
except ValueError as e: # Catch the exception and access its message using 'as e'
    print(f"Error: {e}")



# Custom exceptions:

class InvalidAgeError(Exception): # Create a custom exception class by inheriting from the 'Exception' class
    pass  # You can add custom logic here if needed.


def validate_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")


try:
    validate_age(-2)
except InvalidAgeError as e:
    print(f"Error: {e}")