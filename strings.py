# strings in python can use single or double quotes
print("python")
print('python')

print("\n-------------------------\n")

# assign string to variable
x = "python"
print(x)

print("\n-------------------------\n")

# multiline strings
x = """
    pyhton is awesome
    so learn pyhton
    """
print(x)

# NOTE : it can be use single quote too

print("\n-------------------------\n")

# strings are array
x = "python"
print(x[1])

# print string using loop(for-in)
x = "python"
for y in x:
    print(y)
    
# get string length
x = "python"
print(len(x))

# check string

# check if string is exist
x = "python is awesome and useful"
if "awesome" in x:
    print("good")

print("awesome" in x) # the return will be bool

# check if string is not exist
x = "python is awesome and useful"
if "good" not in x:
    print("awesome")

print("good" not in x) # the return will be bool

print("\n-------------------------\n")

# slicing strings
x = "python"
print(x[2:5]) # it will be slice from index 2 to 5 (but character on index 5 not include)
print(x[:5])  # it will be slice from first index(index 0) to 5
print(x[2:])  # it will be slice from index 2 to last index

# negative indexing and slicing
# for simple, negative slicing will start from last index, so if positive slicing start from 0, negative start from -1
# example, i will print "n" on "python", and i use negative index, it will be like this
print(x[-1])

# so if i need to slice "tho" with negative slicing, it will be like this
print(x[-4:-1])

print("\n-------------------------\n")

# modify strings
# make string uppercase
x = "PyThOn"
print(x.upper())

# make string lowercase
x = "PyThOn"
print(x.lower())

# remove whitespace
x = " python is awesome "
print(x.strip())

# replace string
print(x.replace("p", "h"))

# split string
print(x.split(" "))

print("\n-------------------------\n")

# concat string
x = "python"
y = "java"
z = x + y # it will be "pythonjava", if you need make "python java" it will be like this z = x + " " + z
print(z)

z = x + " " + y
print(z)

print("\n-------------------------\n")

# format string

# you can concat string with integer or else without , but you can use {} inside the string
x = 20
y = "My name is faisal, i am {} years old"
print(y.format(x))

# you can use multiple variable like this
x = 2003
y = 20
z = 7
a = "My name is faisal, i am {} years old, i born {} juni {}"
print(a.format(x, y, z)) # it look like not make sense right 😂, so you can use index for make that string become make sense
a = "My name is faisal, i am {1} years old, i born {2} juni {0}"
print(a.format(x, y, z))

print("\n-------------------------\n")

# escape character
# x = "python is "very" awesome" if you assign value string like this, it will be error, you should use escape character(\)
x = "python is \"very\" awesome"
print(x)

print("\n-------------------------\n")

# string methods
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle() 	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning