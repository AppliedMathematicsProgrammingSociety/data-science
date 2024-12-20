# Basic lambda function: adds two numbers
add = lambda x, y: x + y
print(f"Adding 5 and 3: {add(5, 3)}")  # Output: Adding 5 and 3: 8

# Lambda function with a single argument: squares a number
square = lambda x: x**2
print(f"Squaring 7: {square(7)}")  # Output: Squaring 7: 49


# Lambda function that checks if a number is even
is_even = lambda x: x % 2 == 0
print(f"Is 10 even? {is_even(10)}")  # Output: Is 10 even? True
print(f"Is 7 even? {is_even(7)}")  # Output: Is 7 even? False


# Using lambda with map:  squares each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Numbers squared: {squared_numbers}")  # Output: Numbers squared: [1, 4, 9, 16, 25]


# Using lambda with filter: filters out odd numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")  # Output: Even numbers: [2, 4]


# Using lambda with reduce (requires functools):  calculates the product of numbers in a list
from functools import reduce  #Import reduce function
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of numbers: {product}")  # Output: Product of numbers: 120


# Lambda function with multiple conditions (slightly more complex example)
check_grade = lambda score: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Grade for 85: {check_grade(85)}")  #Output: Grade for 85: B
print(f"Grade for 65: {check_grade(65)}")  #Output: Grade for 65: F



#Limitations:  Lambda functions are best for short, simple expressions.  Avoid complex logic.

# This is generally discouraged - better to use a regular function for readability
#complex_lambda = lambda x, y, z: (x + y) * z if x > y else (x - y) / z if z != 0 else 0  #Avoid this

def better_function(x, y, z):
    if x > y:
        return (x + y) * z
    elif z != 0:
        return (x - y) / z
    else:
        return 0

print(f"Result from complex lambda (avoid this style): {better_function(10,5,2)}") #Output: Result from complex lambda (avoid this style): 30