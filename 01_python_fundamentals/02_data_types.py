# Python Data Types Explained

# 1. Numeric Types:

# int (Integer): Represents whole numbers, positive or negative, without decimals.
my_int = 10
print(f"Type of my_int: {type(my_int)}")   # Output: <class 'int'>

# float (Floating-point): Represents real numbers with decimal points.
my_float = 3.14
print(f"Type of my_float: {type(my_float)}") # Output: <class 'float'>

# complex (Complex):  Represents numbers with a real and an imaginary part (j or J).
my_complex = 2 + 3j 
print(f"Type of my_complex: {type(my_complex)}") # Output: <class 'complex'>



# 2. Text Type:

# str (String): Represents sequences of characters enclosed in single, double, or triple quotes.
my_string = "Hello, world!"
print(f"Type of my_string: {type(my_string)}") # Output: <class 'str'>
another_string = 'Python'
triple_quoted = """This is a
multi-line string."""  # Useful for docstrings


# 3. Sequence Types:

# list (List):  Ordered, mutable (changeable) collection of items.  Can contain mixed data types.
my_list = [1, 2.5, "apple", True]
print(f"Type of my_list: {type(my_list)}")    # Output: <class 'list'>
my_list.append("banana") # Modifying the list (mutable)


# tuple (Tuple): Ordered, immutable (unchangeable) collection of items. Can contain mixed data types.
my_tuple = (10, 20, "orange")
print(f"Type of my_tuple: {type(my_tuple)}")  # Output: <class 'tuple'>
# my_tuple[0] = 5  # This would raise an error because tuples are immutable


# range (Range): Represents a sequence of numbers, commonly used in loops.
my_range = range(5)  # Numbers from 0 up to (but not including) 5: 0, 1, 2, 3, 4
print(f"Type of my_range: {type(my_range)}")  # Output: <class 'range'>



# 4. Mapping Type:

# dict (Dictionary):  Unordered collection of key-value pairs. Keys must be immutable (e.g., strings, numbers, tuples).
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Type of my_dict: {type(my_dict)}") # Output: <class 'dict'>
print(my_dict["name"]) # Accessing the value associated with the key "name"



# 5. Set Types:

# set (Set): Unordered collection of unique items.
my_set = {1, 2, 2, 3} # Duplicates are removed
print(f"Type of my_set: {type(my_set)}")   # Output: <class 'set'>
print(my_set)  # Output: {1, 2, 3}


# frozenset (Frozenset): Immutable version of a set.
my_frozenset = frozenset({1, 2, 3})
print(f"Type of my_frozenset: {type(my_frozenset)}") # Output: <class 'frozenset'>



# 6. Boolean Type:

# bool (Boolean): Represents truth values, either True or False.
my_bool = True
print(f"Type of my_bool: {type(my_bool)}")  # Output: <class 'bool'>


# 7. Binary Types:

# bytes:  Sequence of bytes (integers from 0 to 255).
# bytearray: Mutable sequence of bytes.
# memoryview: Allows access to the internal data of an object without copying. (Less common)



# 8. None Type:

# NoneType: Represents the absence of a value.
my_none = None
print(f"Type of my_none: {type(my_none)}") # Output: <class 'NoneType'>