"""*******************************************************************"""
# Pass by reference vs value:
"""
All parameters (arguments) in the Python language are passed by reference.

It means if you change what a parameter refers to within a function,
the change also reflects back in the calling function."""

# Example:
#!/usr/bin/python

# Function definition is here
def CentOS( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4])
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function

a = [10,20,30]

CentOS(a)

print ("Values outside the function: ", a)

'''Note: Here, we are maintaining reference of the passed object and appending values
in the same object.'''