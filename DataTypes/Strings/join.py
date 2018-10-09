#!/usr/bin/python

s = "  &  "
seq = ("a", "b", "c") # This is sequence of strings.

print("Calling A Variable i.e. ",s, id(s),type(s),len(s))
print("")
print("Calling A Variable i.e. ",seq, id(seq),type(seq),len(seq))

print (s.join(seq))

#print (len(seq))
#print (type(seq))
#print (id(seq))

joiner = "-"

title="10 20 30 Abc"

#title = "my first blog post"
#title = ("my", "first", "blog", "post")
strLower = "abc"

print(title)

print (joiner.join(title))

#print (len(strLower))
#print (strLower.ljust(10, '$'))
#print (strLower.rjust(10, '$'))

#print (strLower.strip('this is a '))

#print (strLower.rstrip('string'))

"""
18	join(seq)
	Merges (concatenates) the string representations of elements in sequence seq into a string,
	with separator string.
"""	
