#!/usr/bin/python3

import re # Module has been imported

line = "Python and Perl are programming and scripting languages" # String Variable

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I) # Variable and calling the module and expression

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
   print ("matchObj.groups() : ", matchObj.groups())
else:
   print ("No match!!")
