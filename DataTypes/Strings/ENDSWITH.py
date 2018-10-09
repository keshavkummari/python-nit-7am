#!/usr/bin/python

str = "abc mahesh"

suffix = "mahesh";
print (str.endswith(suffix))
print (str.endswith(suffix,0))

suffix = "mahesh";
print (str.endswith(suffix, 0, 3))
print (str.endswith(suffix, 4, 10))
