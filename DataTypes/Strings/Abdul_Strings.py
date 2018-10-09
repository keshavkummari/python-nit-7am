#!/usr/bin/python

#strLower = "python"
strLower = "this is a lower case string"
strLower0 = " this is a lower a case a string"
strLower1 = "@this is a lower case string"
strUpper = "THIS IS AN UPPER CASE STRING"
alphaNumSet = "123abc"
alphaSet = 'abc'
numSet = '123'


print (strLower.capitalize())
print (strLower0.capitalize())
print (strLower1.capitalize())

print (strLower.center(7, '+'))

print (strLower0.count('a',2,100))
'''
#print (strLower.encode('utf_8', 'strict'))
print (strLower.encode('cp1252', 'strict'))

tempStr = "dGhpcyBpcyBhIGxvd2VyIGNhc2Ugc3RyaW5n"

#print (tempStr.decode('utf_8', 'strict'))
print (tempStr.decode('cp1252', 'strict'))
'''
print (strUpper.endswith('string'))

print (strLower.find('lower'))

print (numSet.isdigit())
