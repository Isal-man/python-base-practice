# python lambda
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# example
x = lambda a: a + 10
print(x(10))

print("\n-------------------------\n")

# Lambda functions can take any number of arguments:
# example
x = lambda a, b: a + b
print(x(10, 10))

print("\n-------------------------\n")

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
# example
def myFunction(n):
    return lambda a: a * n

myDoubler = myFunction(2)
print(myDoubler(10))