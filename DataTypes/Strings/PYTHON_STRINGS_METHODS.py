'''****************** PYTHON STRING METHODS ******************************'''
# 31. split() Method :
"""
Split method is used to break a given string by the specified delimiter like a comma.

Syntax : str.split(str=" ", num=string.count(str)).

str -- This is any delimeter, by default it is space.
num -- this is number of lines to be made
"""

#!/usr/bin/python3
name = "The string split method"
print (name.split())

#!/usr/bin/python3
ruchita = "ABC123 ABC123 ABC123 ABC123 ABC123 ABC123"
print (ruchita.split( ))
print (ruchita.split('BC',6))
print (ruchita.split('1',))

#!/usr/bin/python3
str_split = "a ,b ,c ,d ,e ,f ,g ,h"

str_list = str_split.split(',')

for i in str_list:
    print i
	
	
'''*******************************************************************************'''
# 32. splitlines() Method :
"""
Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.

It returns a list with all the lines in string, optionally including the line breaks (if num is supplied and is true)

Syntax : str.splitlines( num=string.count('\n'))

num -- This is any number, if present then it would be assumed that line breaks need to be included in the lines.
"""
#!/usr/bin/python3
str = "Python Variables \nOperators\nFunctions\nMethods"
str_a = "Variables \nData Types\nBuiltin Functions\nList of Methods"
print (str.splitlines( ))
print (str_a.splitlines( ))

Output:
['Python Variables ', 'Operators', 'Functions', 'Methods']
['Variables ', 'Data Types', 'Builtin Functions', 'List of Methods']

Note:
The Python splitlines method splits the given string at the line boundaries. The supported boundaries are the subset of universal newlines. For example,

\n for line feed
\r means carriage return
\x1c for file separator

By using the splitlines method in a string, it returns a list of lines broken from these boundaries. Note that, it does not include line breaks in a string.

'''*******************************************************************************'''
# 33. startswith() Method :

This method returns true if found matching string otherwise false.

Syntax : str.startswith(str, beg=0,end=len(string));

str -- This is the string to be checked.
beg -- This is the optional parameter to set start index of the matching boundary.
end -- This is the optional parameter to set start index of the matching boundary.


#!/usr/bin/python3
str = "this is python world....lets rock!!!"
print (str.startswith( 'this' ))
print (str.startswith( 'python', 8 ))
print (str.startswith( 'world',15, 20))

Output:
True
True
True
'''*******************************************************************************'''
# 34. strip() Method :
'''
Performs both lstrip() and rstrip() on string

Syntax : str.strip([chars]);

chars -- The characters to be removed from beginning or end of the string.
'''
#!/usr/bin/python3

str = "*****this is python world....wow!!!*****"
print (str.strip( '*,.wow,!' ))

Output: this is python world
'''*******************************************************************************'''
# 35. swapcase() Method :
'''
It returns a copy of the string in which all the case-based characters have had their case swapped.

Syntax : str.swapcase();
'''
#!/usr/bin/python3
alph_lower = "abcdefghijklmnopqrstuvwxyz"
print (alph_lower.swapcase())

alph_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print (alph_upper.swapcase())

Output : 
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz

'''*******************************************************************************'''
# 36. title() Method :
"""
It returns a copy of the string in which first characters of all the words are capitalized.

Syntax : str.title()
"""
#!/usr/bin/python

title_1 = "variables datatypes numbers list tuples dictionaries sets"
print title_1.title()

Output:
Variables Datatypes Numbers List Tuples Dictionaries Set
'''*******************************************************************************'''
# 37.  translate() Method :

"""
Translates string according to translation table str(256 chars), removing those in the del string.

It returns a copy of the string in which all characters have been translated using table (constructed with the maketrans() function in the string module), optionally deleting all characters found in the string deletechars.

Syntax : str.translate(table[, deletechars]);

table -- You can use the maketrans() helper function in the string module to create a translation table.
deletechars -- The list of characters to be removed from the source string.
"""
#!/usr/bin/python

from string import maketrans # Required to call maketrans function.

a="aeiou"
b="12345"
translate_1 = maketrans(a, b)

str="abcdefghijklmnopqrstuvwxyz"

print str.translate(translate_1)

Output:
1bcd2fgh3jklmn4pqrst5vwxyz


Below example to delete 'x' and 'm' characters from the string −

#!/usr/bin/python

from string import maketrans   # Required to call maketrans function.

a="aeiou"
b="12345"
translate_1 = maketrans(a, b)

str="abcdefghijklmnopqrstuvwxyz"
print str.translate(translate_1, 'klmn')

Output : 1bcd2fgh3j4pqrst5vwxyz

'''*******************************************************************************'''
# 38. upper() Method :
'''
Converts lowercase letters in string to uppercase.

Syntax : str.upper()
'''
#!/usr/bin/python

str = "abcdefghijklmnopqrstuvwxyz";

print str.upper()

Output : ABCDEFGHIJKLMNOPQRSTUVWXYZ
'''*******************************************************************************'''
# 39. zfill() Method :
'''
Returns original string leftpadded with zeros to a total of width characters; 
intended for numbers, zfill() retains any sign given (less one zero).

zfill() pads string on the left with zeros to fill width.

Syntax : str.zfill(width)

width -- This is final width of the string. This is the width which we would get after filling zeros.
'''
#!/usr/bin/python

str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

print str.zfill(30)
print str.zfill(40)

Output:
0000ABCDEFGHIJKLMNOPQRSTUVWXYZ
00000000000000ABCDEFGHIJKLMNOPQRSTUVWXYZ
'''*******************************************************************************'''
# 40. isdecimal() Method :

Returns true if a unicode string contains only decimal characters and false otherwise.

It checks whether the string consists of only decimal characters. 

Note: To define a string as Unicode, one simply prefixes a 'u' 
to the opening quotation mark of the assignment. 

Syntax : str.isdecimal()

#!/usr/bin/python
str = u"this1985";

print str.isdecimal();

str = u"695979";
print str.isdecimal();

Output:
False
True
'''*******************************************************************************'''
