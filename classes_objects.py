# python classes/objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.
# example
class myClass:
    x = 5

myObject = myClass
print(myObject.x)

print("\n-------------------------\n")

# ___init___function()
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created:
# example
class myClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
myObject = myClass("Faisal", 20)
print("My name is {}, I am {} years old".format(myObject.name, myObject.age))

print("\n-------------------------\n")

# ___str___function()
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:
# example
class myClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"My name is {self.name}, I am {self.age} years old"
        
myObject = myClass("Faisal", 20)
print(myObject)

# object methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Let us create a method in the Person class:
# example
class myClass:
    def __init__(self, name):
        self.name = name
    
    def myFunction(self):
        return "hello " + self.name
        
myObject = myClass("python")
print(myObject.myFunction())

# NOTE :
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
# example
class myClass:
    def __init__(this, name):
        this.name = name
    
    def myFunction(this):
        return "hello " + this.name
        
myObject = myClass("python")
print(myObject.myFunction())

print("\n-------------------------\n")

# modifying objects

# modify values
class myClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
myObject = myClass("John", 30)
print(myObject.name, myObject.age)
myObject.name = "Faisal"
myObject.age = 20
print(myObject.name, myObject.age)

# delete object properties
del myObject.age
# print(myObject.name, myObject.age) this code will be error, because age has been removed from myClass

# delete object
del myObject
# print(myObject.name, myObject.age) this code will be error, because myObject has not defined/no longer exist

# pass statement
class myClass:
    pass
