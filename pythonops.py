# -*- coding: utf-8 -*-
"""pythonops.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h58BA8pzjtGoyhOYDLqOZip73flQe_pc
"""

# prompt: list the operation of python with examples and usage of them

# Arithmetic Operators
# Addition
x = 10
y = 5
print(x + y)  # Output: 15

# Subtraction
print(x - y)  # Output: 5

# Multiplication
print(x * y)  # Output: 50

# Division
print(x / y)  # Output: 2.0

# Modulus
print(x % y)  # Output: 0

# Exponentiation
print(x ** y)  # Output: 100000

# Floor Division
print(x // y)  # Output: 2


# Comparison Operators
# Equal to
print(x == y)  # Output: False

# Not equal to
print(x != y)  # Output: True

# Greater than
print(x > y)  # Output: True

# Less than
print(x < y)  # Output: False

# Greater than or equal to
print(x >= y)  # Output: True

# Less than or equal to
print(x <= y)  # Output: False


# Assignment Operators
# Assign value
x = 10
print(x)  # Output: 10

# Add and assign
x += 5
print(x)  # Output: 15

# Subtract and assign
x -= 5
print(x)  # Output: 10

# Multiply and assign
x *= 5
print(x)  # Output: 50

# Divide and assign
x /= 5
print(x)  # Output: 10.0

# Modulus and assign
x %= 3
print(x)  # Output: 1.0

# Exponentiation and assign
x **= 2
print(x)  # Output: 1.0

# Floor division and assign
x //= 2
print(x)  # Output: 0.0


# Logical Operators
# and
x = True
y = False
print(x and y)  # Output: False

# or
print(x or y)  # Output: True

# not
print(not x)  # Output: False


# Bitwise Operators
# Bitwise AND
x = 10  # Binary: 1010
y = 4   # Binary: 0100
print(x & y)  # Output: 0 (Binary: 0000)

# Bitwise OR
print(x | y)  # Output: 14 (Binary: 1110)

# Bitwise XOR
print(x ^ y)  # Output: 14 (Binary: 1110)

# Bitwise NOT
print(~x)  # Output: -11

# Left shift
print(x << 2)  # Output: 40

# Right shift
print(x >> 2)  # Output: 2


# Membership Operators
x = [1, 2, 3]
print(1 in x)  # Output: True
print(4 in x)  # Output: False
print(4 not in x)  # Output: True


# Identity Operators
x = 10
y = 10
print(x is y)  # Output: True
print(x is not y)  # Output: False

x = 10
x += 5
x -= 5
x *= 5
x /= 5
x %= 5
x //= 5
x **= 5

print(x)  #