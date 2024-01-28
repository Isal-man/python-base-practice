# sets

# set is a collection which is unordered, unchangeable, and unindexed
# NOTE : set is unchangeable, but can add and remove item

mySet = {"apple", "grape", "banana"}
print(mySet)

# set item

# unordered, that means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Duplicates Not Allowed
# Sets cannot have two items with the same value.

mySet = {"apple", "grape", "banana", True, 1, 2} # in mySet there are values ​​true and 1, where True and 1 are the same, so 1 cannot be printed
print(mySet)

print("\n-------------------------\n")

# set constructor
# NOTE : to set the constructor of the set, use double round bracket
mySet = set(("apple", "grape", "banana"))
print(mySet)

print("\n-------------------------\n")

# add set items

# add items
mySet.add("manggo")
print(mySet)

# add set
# to add another set, use update()
mySecSet = {"red", "purple", "yellow", "green"}
mySet.update(mySecSet)
print(mySet)

# add any iterable
# you can any list, dictionaries, etc, using update()
fruitList = ["apple", "banana", "mango"]
mySet.update(fruitList)
print(mySet)

print("\n-------------------------\n")

# remove set items
# you can remove set items using remove() or discard()

# using remove()
mySet.remove("apple")
print(mySet)

# using discard()
mySet.discard("red")
print(mySet)

# NOTE : different between remove() and discard()
# if you use remove() with specific item and the item is not on the set, it will send error
# but if you use discard with specific item and the item is not on the set, it will not send error

print("\n-------------------------\n")

# you can use pop() too, but since set is unordered, it will remove random item and you cant sure what item was removed
mySet.pop()
print(mySet)

print("\n-------------------------\n")

# join sets

# join two sets, you can use union() or update
# using union, you need one more variable to accomodate
myThirdSet = mySet.union(mySecSet)
print(myThirdSet)

# using update, you needn't one more variable to accomodate, just use set you have defined before\
mySet = {1, 2, 3}
myThirdSet = {4, 5, 6}
mySet.update(myThirdSet)
print(mySet)

# set methods
# Method 	                       |     Description
# add()	Adds                       |     an element to the set
# clear()	                       |     Removes all the elements from the set
# copy()	                       |     Returns a copy of the set
# difference()	                   |     Returns a set containing the difference between two or more sets
# difference_update()	           |     Removes the items in this set that are also included in another, specified set
# discard()	                       |     Remove the specified item
# intersection()	               |     Returns a set, that is the intersection of two other sets
# intersection_update()	           |     Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	                   |     Returns whether two sets have a intersection or not
# issubset()	                   |     Returns whether another set contains this set or not
# issuperset()	                   |     Returns whether this set contains another set or not
# pop()	                           |     Removes an element from the set
# remove()	                       |     Removes the specified element
# symmetric_difference()	       |     Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	   |     inserts the symmetric differences from this set and another
# union()	                       |     Return a set containing the union of sets
# update()	                       |     Update the set with the union of this set and others