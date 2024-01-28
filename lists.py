# list in python is same work like an array
fruitList = ["apple", "banana", "mango"]
print(fruitList)
print(fruitList[0])

print("\n-------------------------\n")

# get list length
x = len(fruitList)
y = "length of fruitList is {}"
print(y.format(x))

print("\n-------------------------\n")

# list in python can be assign by many data type
myList = ["faisal", 20]
print("My name is", myList[0], "i am {} years old".format(myList[1]))

print("\n-------------------------\n")

# you can get the type of list
print(type(myList))

print("\n-------------------------\n")

# check if item is exist on the list
fruitList = ["apple", "banana", "mango"]
if "apple" in fruitList:
    print("Yes, apple is exist on fruitList")
    
print("\n-------------------------\n")

# change item value
fruitList[0] = "watermelon" # apple will be replace with watermelon
print(fruitList)

print("\n-------------------------\n")

# add new value to the list using insert()
fruitList.insert(3, "apple") # add apple on index 3
print(fruitList)

# add new value to the list using append()
fruitList.append("pear")
print(fruitList)

# NOTE : different between insert and append is insert can add value with specific index, but if append it just add value to the last of the list

# combine list using extend
languageList = ["java", "python", "php", "node"]
fruitList.extend(languageList)
print(fruitList)

print("\n-------------------------\n")

# remove item from the list
fruitList.remove("pear")
print(fruitList)

# remove item from the list with specific index using pop
fruitList.pop(1)
print(fruitList)

# remove item from the list with specific index using del
del fruitList[1]
print(fruitList)

# remove all item
fruitList.clear()
print(fruitList)

# remove all item include the fruitList
del fruitList
# print(fruitList) this will be return error, because fruitList has been removed

print("\n-------------------------\n")

# print value of the list using loop(for-in)
fruitList = ["apple", "banana", "mango"]
for x in fruitList:
    print(x)
    
# print value of the list using loop(for-in) with range
fruitList = ["apple", "banana", "mango"]
for x in range(len(fruitList)):
    print(fruitList[x])
    
# print value of the list using loop(whiles)
fruitList = ["apple", "banana", "mango"]
i = 0
while i < len(fruitList):
    print(fruitList[i])
    i += 1
    
print("\n-------------------------\n")

# list comprehension
fruitList = ["apple", "banana", "mango"]
newList = []

for x in fruitList:
    if "n" in x:
        newList.append(x)
        
print(newList)

myList = [x for x in fruitList if "n" in x]
print(myList)

print("\n-------------------------\n")

# sorting list
fruitList = ["dragonfruit", "pineapple", "jackFruit", "pear", "apple", "banana", "mango"]

fruitList.sort() # asc
print(fruitList)

fruitList.sort(reverse = True) # desc
print(fruitList)

# NOTE 1 : if you sorting the list of string, Please note that it is case-sensitive, example
fruitList = ["Dragonfruit", "pineapple", "JackFruit", "pear", "apple", "banana", "mango"]
fruitList.sort()
print(fruitList) # see the output if you need to know

# NOTE 2 : if you need to ignoring case-sensitive, you should do this
fruitList.sort(key = str.lower) # or fruitList.sort(key=str.upper)
print(fruitList)

# sorting numeric
numList = [10, 40, 29, 19, 39, 30, 18]

numList.sort()
print(numList)

# customize sort function
def myFunc(n):
    return abs(n - 20)

numList.sort(key = myFunc)
print(numList)

# reverse order
fruitList.reverse()
print(fruitList)

print("\n-------------------------\n")

# join list

# use + operator
fruitList = ["Dragonfruit", "pineapple", "JackFruit", "pear", "apple", "banana", "mango"]
numList = [10, 40, 29, 19, 39, 30, 18]
numList += fruitList
print(numList)

# use extend()
fruitList = ["Dragonfruit", "pineapple", "JackFruit", "pear", "apple", "banana", "mango"]
numList = [10, 40, 29, 19, 39, 30, 18]
numList.extend(fruitList)
print(numList)

# list methods
# append()	|   Adds an element at the end of the list
# clear()	|   Removes all the elements from the list
# copy()	|   Returns a copy of the list
# count()	|   Returns the number of elements with the specified value
# extend()	|   Add the elements of a list (or any iterable), to the end of the current list
# index()	|   Returns the index of the first element with the specified value
# insert()	|   Adds an element at the specified position
# pop()	    |   Removes the element at the specified position
# remove()	|   Removes the item with the specified value
# reverse()	|   Reverses the order of the list
# sort()	|   Sorts the list