#!/usr/bin/python

# Function definition is here
def info( arg1, *vartuple ):
   #This prints a variable passed arguments
   print (arg1)
   for i in vartuple:
      print(i)
   return

# Now you can call printinfo function
info("Welcome to Python World",10,20,30,40,50,"Guido","Van","Rossum")