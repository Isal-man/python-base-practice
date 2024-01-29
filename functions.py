# python functions
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# example
def myFunction():
    print("this is my function")
    
myFunction()

print("\n-------------------------\n")

# function with arguments
def myFunction(name):
    print("My name is", name)
    
myFunction("Faisal")
myFunction("John")
myFunction("Jane")

# you can also add more than one arguments
def myFunction(fname, mname, lname):
    print("My name is", fname, mname, lname)
    
myFunction("Ahmad", "Faisal", "Hidayat")

# NOTE : if you just add one argument, it will be error, but you can do arbitrary arguments to solve it

print("\n-------------------------\n")

# arbitrary arguments
# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def myFunction(*args):
    print("My name is", args[1])

myFunction("John", "Faisal", "Jane")

print("\n-------------------------\n")

# keyword arguments
def myFunction(person1, person3, person2):
    print("My name is", person1)
    print("My name is", person2)
    print("My name is", person3)
    
myFunction(person1="Faisal",person2="John",person3="Jane")

# arbitrary keyword arguments
def myFunction(**kwargs):
    print("My name is", kwargs["fname"], kwargs["mname"], kwargs["lname"])

myFunction(fname="Ahmad",mname="Faisal",lname="Hidayat")

print("\n-------------------------\n")

# default parameters
def myFunction(name="Faisal"):
    print("My name is",name)
    
myFunction()
myFunction("John")
myFunction("Jane")

# passing list a list as an argument
def myFunction(names):
    for x in names:
        print(x)

names = ["Faisal", "John", "Jane"]
myFunction(names)

print("\n-------------------------\n")

# returning values
def myFunction(a, b):
    return a * b

print(myFunction(10, 10))