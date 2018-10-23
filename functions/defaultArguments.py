"""
#!/usr/bin/python

# Function definition is here
def info( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call info function
info( age=50, name="Guido" )
# Calling a Funtion
info(name="Rossum" )

"""

#!/usr/bin/python

# Function definition is here
def info( name="Guido", age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call info function
info( age=50, name="Guido" )
# Calling a Funtion
info()
