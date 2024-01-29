# dictionary

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# example
myDictionary = {
    "name": "Ahmad Faisal Hidayat",
    "age": 20,
    "gender": "man"
}

print(myDictionary)

print("\n-------------------------\n")

# dictionary items
# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
print(myDictionary["name"])

print("\n-------------------------\n")

# dictionary not allowed duplicate values
# example
myDictionary = {
    "name": "Ahmad Faisal Hidayat",
    "age": 20,
    "gender": "man", # if there is a key with a gender name, the value man will be replaced
    "gender": "woman"
} 

print(myDictionary) 

print("\n-------------------------\n")

# dictionary constructor
myDictionary = dict(name = "Ahmad Faisal Hidayat", age = 20, gender = "man")
print(myDictionary)

print("\n-------------------------\n")

# accessing items
# you can use like this myDictionary["name"] or like this myDictionary.get("name")
# example
name = myDictionary["name"]
print(name)
age = myDictionary.get("age")
print(age)

print("\n-------------------------\n")

# get keys from dictionary
keys = myDictionary.keys()
print(keys)

print("\n-------------------------\n")

# get values from dictionary
values = myDictionary.values()
print(values)

print("\n-------------------------\n")

# get items as tuple in a list from dictionary
items = myDictionary.items()
print(items)

print("\n-------------------------\n")

# checking if key is exist on a dictionary
if "name" in myDictionary:
    print("Yes, your name is", myDictionary["name"])
    
print("\n-------------------------\n")

# change items
# you can change items of dictionary using specific key or method update()
# example
print(myDictionary["name"]) # before update
myDictionary["name"] = "Goo Youn Jung"
print(myDictionary["name"]) # after update
print(myDictionary["age"]) # before update
myDictionary.update({"age": 27})
print(myDictionary["age"]) # after update

# NOTE : you can do this method too, for adding items to dictionary
# example
myDictionary["role"] = "Backend Developer"
print(myDictionary)

print("\n-------------------------\n")

# remove items
# you can use method pop() and popitem() to remove items from dictionary
# example
myDictionary.pop("age")
print(myDictionary)
myDictionary.popitem()
print(myDictionary)

# NOTE : different between pop() and popitem() : method pop() can remove specific item from dictionary, but popitem() just remove the last item from dictionary

# you also can use del and clear() to remove items from dictionary
del myDictionary["gender"]
print(myDictionary)
myDictionary.clear()
print(myDictionary)

# NOTE : if you use del without specific items, that will remove all values of dictionary include your dictionary too
# so if you try to print you dictionary, that will be error, because your dictionary not longer exist
# and if you need to remove all values without remove your dictionary, use clear() method

print("\n-------------------------\n")

# loop dictionary
myDictionary = {
    "name": "Ahmad Faisal Hidayat",
    "age": 20,
    "gender": "man"
}

# to print all keys of dictionary
for x in myDictionary:
    print(x)
    
# you can also use myDictionary.keys()
for x in myDictionary:
    print(x)

# to print all values of dictionary
for x in myDictionary:
    print(myDictionary[x])
    
# you can also use myDictionary.values()
for x in myDictionary.values():
    print(x)
    
# to print both use myDictionary.items()
for x, y in myDictionary.items():
    print(x, y)
    
print("\n-------------------------\n")

# copy dictionary

# you can use copy() method to copy your dictionary to another dictionary
# example
yourDictionary = myDictionary.copy()
print(yourDictionary)

# NOTE : you cant do like this yourDictionary = myDictionary to copy dictionary, because it will be reference,
# so if myDictionary has change, yourDictionary will be change too
# example
yourDictionary.clear() # clear all values of yourDictionary first
print(yourDictionary)

yourDictionary = myDictionary # and then copy all values of myDictionary to yourDictionary
print(yourDictionary) # print to see values of yourDictionary
myDictionary["role"] = "Frontend Developer" # make changes of myDictionary
print(yourDictionary) # if you print this, yourDictionary is change too, but we just change myDictionary
# but if we use copy() method
yourDictionary.clear() # this will clear myDictionary too, so we need to make myDictionary again
myDictionary = {
    "name": "Ahmad Faisal Hidayat",
    "age": 20,
    "gender": "man"
}

print(yourDictionary)
yourDictionary = myDictionary.copy()  
print(yourDictionary) 
myDictionary["role"] = "Frontend Developer" 
print(yourDictionary) # see the different

# another way to copy dictionary, we can use the constructor
yourDictionary.clear()
print(yourDictionary)
yourDictionary = dict(myDictionary)
print(yourDictionary) 

print("\n-------------------------\n")

# nested dictionary
myDictionary = {
    "person1": {
        "name": "Ahmad Faisal Hidayat",
        "age": 20,
        "gender": "man"
    },
    "person2": {
        "name": "John Doe",
        "age": 20,
        "gender": "man"
    },
    "person3": {
        "name": "Jane Doe",
        "age": 20,
        "gender": "woman"
    }
}

print(myDictionary)

# you can do this too
person1 = {
        "name": "Ahmad Faisal Hidayat",
        "age": 20,
        "gender": "man"
    }
person2 = {
        "name": "John Doe",
        "age": 20,
        "gender": "man"
    }
person3 = {
        "name": "Jane Doe",
        "age": 20,
        "gender": "woman"
    }

myDictionary = {
    "person1": person1,
    "person2": person2,
    "person3": person3
}

print(myDictionary)

# this is how to access nested dictionary
print(myDictionary["person1"]["name"])

# dictionary methods
# Method 	Description
# clear()        |	Removes all the elements from the dictionary
# copy()         |	Returns a copy of the dictionary
# fromkeys()     |	Returns a dictionary with the specified keys and value
# get()          |	Returns the value of the specified key
# items()        |	Returns a list containing a tuple for each key value pair
# keys()         |	Returns a list containing the dictionary's keys
# pop()          |	Removes the element with the specified key
# popitem()      |	Removes the last inserted key-value pair
# setdefault()   |	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()       |	Updates the dictionary with the specified key-value pairs
# values()       |	Returns a list of all the values in the dictionary