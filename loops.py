# python loops

# while loops
# With the while loop we can execute a set of statements as long as a condition is true.
# example
i = 1
while i < 10:
    if (i % 2 == 0):
        print("Fizz")
    else:
        print("Buzz")
    i+=1

print("\n-------------------------\n")

# break statement
i = 1
while i < 10:
    if (i % 5 == 0):
        break
    else:
        print("FizzBuzz")
    i+=1

print("\n-------------------------\n")

# continue statement
i = 1
while i < 10:
    i+=1
    if (i % 5 == 0):
        continue
    else:
        print("FizzBuzz")

print("\n-------------------------\n")

# else statement
i = 1
while i < 10:
    if (i % 2 == 0):
        print("Fizz")
    else:
        print("Buzz")
    i+=1
else:
    print("loops is done")
    
print("\n-------------------------\n")

# for loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, 
# and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
# example
fruits = ["apple", "banana", "grape"]
for x in fruits:
    print(x)
    
print("\n-------------------------\n")

# looping through a string
for x in fruits[1]:
    print(x)
    
print("\n-------------------------\n")

# break statement
for x in fruits:
    if x == "banana":
        break
    else:
        print(x)
        
print("\n-------------------------\n")

# continue statement
for x in fruits:
    if x == "banana":
        continue
    else:
        print(x)
        
print("\n-------------------------\n")

# for with range
for x in range(10):
    print(x)
        
print("\n-------------------------\n")

# NOTE 1 : range() always start from 0, if you need start with specific number give parameter on that range
# example
for x in range(2, 10):
    print(x)
    
print("\n-------------------------\n")
    
# NOTE 2 : range() always increment by 1, if you need increment with specific number give parameter on that range
# example
for x in range(0, 100, 10):
    print(x)
    
# range(start, end, increment)

print("\n-------------------------\n")

# else statement
for x in range(10):
    print(x)
else:
    print("for loop is done")

# NOTE : else statement cant be execute if there have break statement

print("\n-------------------------\n")

# nested loops
colors = ["red", "yellow", "purple"]
fruits = ["apple", "banana", "grape"]
for x in colors:
    for y in fruits:
        print(y, x)
        
# pass statement
# loops cant be empty, but you can solve it with pass statement
for x in colors:
    pass