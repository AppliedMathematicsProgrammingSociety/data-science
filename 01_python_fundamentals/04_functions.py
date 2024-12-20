# Python Functions

# Defining a function:
def greet(name):  # 'def' keyword, function name, parameters in parentheses
    """This function greets the person passed in as a parameter."""  # Docstring (optional but recommended)
    print(f"Hello, {name}!")

# Calling a function:
greet("Alice")  # Output: Hello, Alice!


# Function with a return value:
def add(x, y):
    """This function adds two numbers and returns the sum."""
    return x + y

result = add(5, 3)
print(result)  # Output: 8


# Default arguments:
def greet_with_title(name, title="Mr."):  # 'title' has a default value
    print(f"Hello, {title} {name}!")

greet_with_title("Bob")         # Output: Hello, Mr. Bob!
greet_with_title("Alice", "Ms.") # Output: Hello, Ms. Alice!


# Variable number of arguments (*args):
def print_all(*args): #  *args allows any number of positional arguments
    print("Arguments:")
    for arg in args:
        print(arg)

print_all(1, 2, "apple", True)


# Keyword arguments (**kwargs):
def print_details(**kwargs):  # **kwargs allows any number of keyword arguments
    print("Details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_details(name="Alice", age=30, city="New York")



# Scope and Lifetime of Variables:
# Variables defined inside a function have local scope.
def my_function():
    local_var = 10  # 'local_var' is only accessible inside the function
    print(local_var)

my_function()  # Output: 10
# print(local_var)  # This would cause an error (local_var is not defined outside)

# Global variables:
global_var = 20  # Defined outside any function

def access_global():
    print(global_var)  # Accessing the global variable

access_global() # Output: 20