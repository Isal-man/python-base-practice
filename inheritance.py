# python inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
# example
# create parent class
class myClass:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        
    def myFunc(self):
        print(self.firstName, self.lastName)
        
myObject = myClass("Ahmad", "Faisal")
myObject.myFunc()

class myPerson(myClass):
    pass

mySecObject = myPerson("John", "Doe")
mySecObject.myFunc()