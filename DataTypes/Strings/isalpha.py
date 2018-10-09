#!/usr/bin/python
 
str_alpha = "this" # Only String

alpha_space = "this "  # String with Space

alpha_specialChar = "this *" # String with Special Char

str_digits = "this007"  # No space & digit in this string

print(str_alpha.isalpha())

print(alpha_space.isalpha())

print(alpha_specialChar.isalpha())

print (str_digits.isalpha())

rossum = "Pythonandperllinux"

print (rossum.isalpha())

"""
11	isalpha()
	Returns true if string has at least 1 character and all
	characters are alphabetic and false otherwise.
"""
