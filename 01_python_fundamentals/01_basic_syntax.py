# 01_python_fundamentals - Basic Syntax

# Comments:
# Lines starting with # are comments and are ignored by the interpreter.
# They are crucial for explaining your code.

# Indentation:
# Python uses indentation (typically 4 spaces) to define code blocks. 
# This is unlike many other languages that use braces {}.
# Consistent indentation is essential; incorrect indentation will cause errors.

# Statements:
# A statement is a single line of code that performs an action.

# Variable assignment:
name = "Alice"  # Assigns the string "Alice" to the variable 'name'
age = 30     # Assigns the integer 30 to the variable 'age'

# Printing:
print("Hello, world!")  # Prints the string to the console
print(name)          # Prints the value of the variable 'name'
print(f"My name is {name} and I am {age} years old.") # f-strings for formatted output


# Multi-line statements:
# Long statements can be continued on the next line using the backslash character \
total = 10 + 20 + 30 + \
        40 + 50 + 60

# Or using parentheses: (preferred for readability)
total = (10 + 20 + 30 +
         40 + 50 + 60)

print(total)


# Multiple statements on a single line (generally discouraged for readability):
a = 5; b = 10; print(a + b)


# Identifiers:
# Names used for variables, functions, etc.
# Must start with a letter or underscore _, followed by letters, numbers, or underscores.
# Case-sensitive:  `my_variable` is different from `My_Variable`

# Valid identifiers:
my_variable = 10
_count = 0
name2 = "Bob"

# Invalid identifiers (will cause errors):
# 2name = "Invalid"  # Starts with a number
# my-variable = 5  # Contains a hyphen

# Keywords:
# Reserved words with special meanings in Python. Cannot be used as identifiers.
# Examples:  if, else, for, while, def, class, True, False, and, or, not, return, import, etc.

# Showing a keyword used in a statement:
if age > 18:
    print("Adult") # 'if' is a keyword
