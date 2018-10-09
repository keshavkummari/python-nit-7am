#!/usr/bin/python

#Str = ":-d"
Str = "redhat"
Str = Str.encode('cp1252','strict')
#Str = Str.encode('UTF-8','strict')

print ("Encoded String: ", Str)
print ("Decoded String: ", Str.decode('UTF-8','strict'))

'''
4	decode(encoding='UTF-8',errors='strict')
	Decodes the string using the codec registered for encoding.
	encoding defaults to the default string encoding.

5	encode(encoding='UTF-8',errors='strict')
	Returns encoded string version of string; on error, default is to raise a
	ValueError unless errors is given with 'ignore' or 'replace'.
'''	
