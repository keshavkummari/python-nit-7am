#!/usr/bin/python

mac = "welcome to python world";
mac = mac.encode('base64','strict');

print ("Encoded String: " + mac)
print ("Decoded String: " + mac.decode('base64','strict'))
