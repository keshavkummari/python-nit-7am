'''
String Special Operators:
                                 0 1 2 3 4 # Left to Right index
								-5-4-3-2-1 # Right to Left index
Assume string variable a holds ' H e l l o' and variable b holds 'Python', then :
'''

# Creating of String Variables in Python
a = 'Hello'
b = "Python"

# Accessing Variables in python
'''
print("Left to Right Index i.e. a : ",a[1:5])
print("")
print("Right to Left index i.e. a : ",a[0:4])

print (r'\n')
print (R'c:\\Users\\keshavkummari')


print ("My name is %s and I born in %d" % ('Python', 1981))

var1='Python'
var2=1981
print ("My name is %s and I born in %d" % (var1,var2))

var1='Python'
var2=1981

print("My name is {} and I born in {}".format('Guido Van Rossum',1981))

print("My name is {} and I born in {}".format(var1,var2))

print("My name is {var3} and I born in {var4}".format(var3='python',var4=1981))

print("My name is {0} and I born in {1}".format(var1,var2))

firstname='Guido'
lastname="Rossum"

FullName= firstname[0] + " & " + lastname[0]

print(FullName)

print(firstname*5)
'''

#!/usr/bin/python
       #01234567891011
       #-11-10-9-8-7-6-5-4-3-2-1
str1 = "Hello World!"  # 11 characters
str2 = 'This is an example string'
          #0123456789
alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num='0123456789'

#print (str1[0])
#print (str1[-1])
#print (str1[2:6])
#print (str1[:5])
#print (str1 * 3)

print(alphabets[0::6]) # Zero Based Indexing
print(num[0::3]) # Zero Based Indexing


#print ("updated string ", str1[:6] + "planet")
#print ("updated string ", str1[:12] + "Perl")

# formatting of strings

#print ("Your name is %s and your account id is %d" %("Kevin",14456))

#print ("Calling str1 {0} and calling str2 {1}".format(str1,str2))

#print ("Value1 {} Value2 {} and Value3 {}".format("python",100,"pycharm"))

#print ("Value1 {1} Value2 {0} and Value3 {2}".format("python",100,"pycharm"))

