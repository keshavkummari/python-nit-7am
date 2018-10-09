#!/usr/bin/python

"""
27	rfind(str, beg=0,end=len(string))
	Same as find(), but search backwards in string.
"""

str1 = "Python number string examples"

str2 = "num"

print (str1.find(str2)) # Looking for index 

print (str1.find(str2, 10)) # Start index 10

print (str1.find(str2, 0,10)) # Start and ending index i.e. 15,20
