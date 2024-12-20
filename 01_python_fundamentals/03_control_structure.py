# Python Control Structures

# 1. Conditional Statements (if, elif, else)

# 'if' statement: Executes a block of code only if a condition is True.
age = 20
if age >= 18:
    print("You are an adult.")


# 'if-else' statement: Executes one block if the condition is True, and another if it's False.
temperature = 25
if temperature > 30:
    print("It's a hot day!")
else:
    print("It's not too hot.")


# 'if-elif-else' statement:  Tests multiple conditions sequentially.
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")


# Nested 'if' statements: 'if' statements inside other 'if' statements.
x = 10
y = 5
if x > 5:
    if y < 10:
        print("Both conditions are True.")


# 2. Looping Statements (for, while)

# 'for' loop: Iterates over a sequence (list, tuple, string, range, etc.).
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using 'range' to control iterations:
for i in range(5):  # Iterates from 0 to 4
    print(i)

# 'while' loop:  Repeats a block of code as long as a condition is True.
count = 0
while count < 3:
    print(count)
    count += 1 # Important: Update the loop variable, or it will loop infinitely!


# 3. Loop Control Statements (break, continue, pass)

# 'break': Terminates the loop prematurely.
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)

# 'continue': Skips the rest of the current iteration and proceeds to the next.
for i in range(10):
    if i % 2 == 0:  # Check if i is even
        continue # Skip even numbers
    print(i)


# 'pass':  Does nothing. Used as a placeholder when a statement is syntactically required but no action is needed.
for i in range(5):
    if i == 2:
        pass #  Don't do anything when i is 2 (but don't break the loop either)
    print(i)
