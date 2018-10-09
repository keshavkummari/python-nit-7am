#!/usr/bin/python

Var_Value = "this is a string example"

Var_Value = str.encode('base64','strict')

print("Encoded string : " + Var_Value)
print("Decoded string : " + str.decode('base64','strict'))
