# List Comprehensions in Python

# Basic list comprehension:
squares = [x**2 for x in range(10)]  # Creates a list of squares from 0 to 81
print(squares)


# List comprehension with a condition:
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # Squares of even numbers only
print(even_squares)



# List comprehension with nested loops:
matrix = [[i * j for j in range(3)] for i in range(2)]  # Creates a 2x3 matrix
print(matrix)


# List comprehension with string manipulation:
words = ["apple", "banana", "cherry"]
upper_words = [word.upper() for word in words]  # Converts words to uppercase
print(upper_words)


# List comprehension with function calls:
def double(x):
    return x * 2

numbers = [1, 2, 3, 4]
doubled_numbers = [double(num) for num in numbers]  # Doubles each number
print(doubled_numbers)


# List comprehension with if-else:
numbers = [1, 2, 3, 4, 5]
result = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(result) #Output: ['odd', 'even', 'odd', 'even', 'odd']


# Flattening a list of lists using list comprehension:
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]  # Flattens the nested list
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]



# Dictionary comprehension (similar to list comprehension, but creates dictionaries):
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)


# Set comprehension (creates sets):
unique_chars = {char for word in words for char in word}  # Gets unique characters from a list of words
print(unique_chars)


# Generator expression (similar syntax, but creates a generator, which is evaluated lazily)
# useful for memory efficiency with large datasets

very_large_list = range(1000000) #This can be huge, list comp may take lots of time/mem
generator_squares = (x*x for x in very_large_list)

#The generator doesn't calculate the squares instantly
#It calculates each square when accessed using next or when iterated.

for _ in range(10): # print first 10 squares
    print(next(generator_squares))

# Converting the generator to list later when/if needed
#squares_list = list(generator_squares)