#!/usr/bin/python

#!  = Shebang
# /usr/bin/python = Absolute path of where python is installed

# Comments in python

# Single-Line Comments are : 1. #, 2. '', 3. "", 4. ''' ''' & 5. """ """

# Multi-Line Comments are : 1. ''' ''' & 2. """ """

# Creating variables in python

''' Rule of Creating Variables in Python
1. A-Z
2. a-z
3. 0-9   : Integer Value should not created as prefix of any variable name
4. A-Za-z
5. A-Za-z0-9
6. _
7. A-Za-z0-9_
'''

# Creating String Variables:
FNAME = 'Guido'         # Single Quotes
mname = "Van"           # Double Quotes
_lname = """Rossum"""    # Double Triples Quotes
software_001 = '''Python 3.6.0''' # Single Triples Quotes

# Accessing variables with the help of print()
print(FNAME)
print("")
print(mname)
print("")
print(_lname)
print("")
print(software_001)

# Verify the Variable Data Type using type():
print(type(FNAME))
print("")
print(type(mname))
print("")
print(type(_lname))
print("")
print(type(software_001))
