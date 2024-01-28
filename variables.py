x = 5 # this will be int
print(type(x)) # this will print the type of variables

x = 5.5 # this will be float
print(type(x))

x = "5" # this will be str
print(type(x))

x = True # this will be bool
print(type(x))

print("\n-------------------------\n")

# casting variables
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

# in python string can be write with single or double quotes
x = 'python'
y = "python"
print(x, y)

print("\n-------------------------\n")

# in python variables are case sensitive
# a and A is different
a = 10
A = 20
print(a, A)

print("\n-------------------------\n")

# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

#     A variable name cannot start with a number
#     A variable name must start with a letter or the underscore character
#     A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#     Variable names are case-sensitive (age, Age and AGE are three different variables)
#     A variable name cannot be any of the Python keywords.

# assign many values to many variables
x, y, z = "Apple", "Manggo", "Banana"
print(x)
print(y)
print(z)

# assign one values to many variables
x = y = z = "Apple"
print(x)
print(y)
print(z)

# extract collection such like list, tuple, etc
fruits = ["Apple", "Manggo", "Banana"]
x , y, z = fruits
print(x)
print(y)
print(z)

print("\n-------------------------\n")

# output variables
# basic output
x = "learn python with isal"
print(x)

# output from many variables
x = "learn"
y = "python"
z = "with"
a = "isal"
print(x, y, z, a)

# output with +
x = "learn "
y = "python "
z = "with "
a = "isal "
print(x + y + z + a)

# NOTE 1 : if string it will be concat the string, but if its other than string will works as math operator
x = 10
y = 10
print(x + y)

# NOTE 2 : if string + not string it will be error

# this code will be error
# x = 10
# y = "20"
# print(x + y)

# if you want concat string with other use ,
x = 10
y = "20"
print(x , y)

print("\n-------------------------\n")

# global variables
x = "python"

def myFunc():
    print("I learn " + x)
    
myFunc()

# NOTE 1 : If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
x = "python"

def myFunc():
    x = "java"
    print("I learn " + x)
    
myFunc()

# NOTE 2 : If you want variable on function be global, you can use global before name of variable
def myFunc():
    global x
    x = "awesome"
    
myFunc()

print("python is", x)