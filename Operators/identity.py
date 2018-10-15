'''--------------------------------------------------------------'''
# 7. Identity Operators :
'''--------------------------------------------------------------'''

'''
is and is not are the identity operators in Python. 

They are used to check if two values (or variables) are located on the same part of the memory. 

Two variables that are equal does not imply that they are identical.

# Identity operators compare the memory locations of two objects.

1. is		= x is y, here is results in 1 if id(x) equals id(y).
2. is not	= x is not y, here is not results in 1 if id(x) is not equal to id(y).
'''

#!/usr/bin/python
#Identity operators in Python

x1 = 5
y1 = 5

x2 = 'Hello'
y2 = 'Hello'

x3 = [1,2,3]
y3 = [1,2,3]

# Output: True
print(id(x1),type(x1))
print(id(y1),type(y1))
print(x1 is y1)

# Output: True
print(id(x2),type(x2))
print(id(y2),type(y2))
print(x2 is y2)

# Output: False
print(id(x3),type(x3))
print(id(y3),type(y3))

print(x3 is y3)


