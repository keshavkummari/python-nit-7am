#!/usr/bin/python
"""
seq = ('name', 'age', 'Gender') # A Tuple Variable

dict1 = dict.fromkeys(seq)  # Calling a Tuple Variable part of dict.fromkeys method

print ("New dictionary : %s" %  str(dict1))

dict2 = dict.fromkeys(seq,10) # Assigning values to Keys

print ("New dictionary : %s" %  str(dict2))

"""
var1 = {'Name': 'minnu', 'Age': 7, 'course':'Python'}

print ("Value : %s" %  var1.setdefault('Age', None))

print ("Value : %s" %  var1.setdefault('course', 'Perl'))