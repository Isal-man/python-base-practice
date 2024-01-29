# if else python
# Python supports the usual logical conditions from mathematics:
# - Equals: a == b
# - Not Equals: a != b
# - Less than: a < b
# - Less than or equal to: a <= b
# - Greater than: a > b
# - Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.
# An "if statement" is written by using the if keyword.
# example:
a = 20
b = 30
if a < b:
    print("a smalller than b")

print("\n-------------------------\n")

# indention
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
# Other programming languages often use curly-brackets for this purpose. 
# example
# if b > a:
# print("b greater than a") -> this code will be error, remove the comment if you need to see

# elif
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 30
if a < b:
    print("a smaller than b")
elif a == b:
    print("a same with b")
    
print("\n-------------------------\n")

# short hand

# if statement
# example
a = 40
if a > b: print("a greater than b")

# if else statement
# example
b = 50
print("a greater than b") if a > b else print("b greater than a")

print("\n-------------------------\n")

# and(&&) logical
c = 30
b = 30
if a > b and a > c:
    print("both condition is true")
    
print("\n-------------------------\n")

# or(||) logical
if a > b or c > a:
    print("there just one condition true", a > b, c > a)

print("\n-------------------------\n")

# not(!) logical
if not a < b:
    print("Yes, a not smaller than b")
    
print("\n-------------------------\n")

# nested if
if a > b:
    print("Yes, a greater than b")
    if not c > a:
        print("Yes, c not greater than a")
        
# NOTE : if statement cant be empty, it will raised error, but you can solve it with pass statement
# example
if b > c:
    pass