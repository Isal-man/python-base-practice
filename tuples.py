# tuples python

# tuple is unchangeable, immutable, can have duplicate values, and ordered
myTuple = ("apple", "mango", "banana", "orange", "pear", "grape")
print(myTuple)

print("\n-------------------------\n")

# get tuple length
x = len(myTuple)
print(x)

print("\n-------------------------\n")

# NOTE : if you make tuple with just one value, you should add comma after the value
myTuple = ("apple",)
print(type(myTuple))
myTuple = ("apple") # this will cant read the type as tuple, but will read as string
print(type(myTuple))

print("\n-------------------------\n")

# since tuple is unchangeable, there is one way to update the value of tuple, you can do like this
# update tuple
myTuple = ("apple", "mango", "banana", "orange", "pear", "grape")
print(myTuple)

# first you should convert tuple into list
myList = list(myTuple)

# and then you change the value of the list
myList[1] = "watermelon"

# and last you convert again the list to tuple
myTuple = tuple(myList)

print(myTuple)

# delete tuple
# first you should convert tuple into list
myList = list(myTuple)

# and then you remove value the list to tuple
myList.remove("watermelon")

# and last you convert again the list to tuple
myTuple = tuple(myList)

print(myTuple)

print("\n-------------------------\n")

# unpack tuples

# this is how to extract the tuple
fruits = ("apple", "banana", "manggo")

(red, yellow, green) = fruits

print(red)
print(yellow)
print(green)

# NOTE : You must extract the value of the tuple with the same number of variables as the value of the tuple, 
# but if you dont know how much the value of the tuple, you can use asterisk(*) to defined variable as list
# example

fruits = ("apple", "banana", "manggo", "grape", "pear")

(red, yellow, *green) = fruits

print(red)
print(yellow)
print(green) # this variable will be a list

print("\n-------------------------\n")

# join tuple

# join two tuples
fruits = ("apple", "banana", "grape")
colors = ("red", "yellow", "purple")
combine = fruits + colors
print(combine)

# multiply tuple
combine *= 2
print(combine)

# tuple methods
# count() | Returns the number of times a specified value occurs in a tuple
# index() | Searches the tuple for a specified value and returns the position of where it was found