# python maths
# Python has a set of built-in math functions, including an extensive math module,
# that allows you to perform mathematical tasks on numbers.
# example

# built-in math functions

# min and max
# The min() and max() functions can be used to find the lowest or highest value in an iterable:
# example
x = min(5, 10, 15, 20, 25)
y = max(5, 10, 15, 20, 25)
print(x, y)

print("\n-------------------------\n")

# abs
# The abs() function returns the absolute (positive) value of the specified number:
# example
x = abs(-2)
print(x)

print("\n-------------------------\n")

# pow
# The pow(x, y) function returns the value of x to the power of y (x^y).
# example
x = pow(2, 4)
print(x)

# math module
import math

print("\n-------------------------\n")

# math.sqrt()
# The math.sqrt() method for example, returns the square root of a number:
# example
x = math.sqrt(64)
print(x)

print("\n-------------------------\n")

# math.ceil() and math.floor()
# The math.ceil() method rounds a number upwards to its nearest integer, 
# and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:
# example
x = math.ceil(1.5)
y = math.floor(1.5)
print(x, y)

print("\n-------------------------\n")

# math.pi
# The math.pi constant, returns the value of PI (3.14...):
# example
x = math.pi
print(x)