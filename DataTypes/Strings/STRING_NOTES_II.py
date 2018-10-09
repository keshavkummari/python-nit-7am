# 12. isdigit() Method :

"""Checks whether the string consists of digits only.

Syntax : str.isdigit()

Note: 
Returns true if all characters in the string are digits and
there is at least one character, false otherwise."""

#!/usr/bin/python

str = "03948274";  # Only digit in this string
print (str.isdigit())

str = "Linux Unix Perl Python and django...etc!!!";
print (str.isdigit())

'''Output:
True
False'''
"""*****************************************************************"""
# 13. islower() Method :

"""
Checks whether all the case-based characters (letters) of the string
are lowercase.

Syntax : str.islower()

Note:
It returns true if all cased characters in the string are lowercase
and there is at least one cased character, false otherwise."""

#!/usr/bin/python

mac = "python with django framework!"
print (mac.islower())

mac = "Linux Unix Perl Python and django...etc!!!"
print (mac.islower())
    
"""*****************************************************************"""
# 14. isnumeric() Method :

"""It checks whether the string consists of only numeric characters.
This method is present only on unicode objects.

Note: To define a string as Unicode, one simply prefixes a 'u' to
the opening quotation mark of the assignment.

Syntax : str.isnumeric()

Note: It returns true if all characters in the string are numeric,
false otherwise."""

#!/usr/bin/python

str = u"year 1995";  
print (str.isnumeric())

str = u"78 6786";
print (str.isnumeric())
"""*****************************************************************"""
# 15. isspace() Method :

"""
The method isspace() checks whether the string consists of whitespace..

Syntax : str.isspace()

Note: It returns true if there are only whitespace characters in the
string and there is at least one character, false otherwise."""

#!/usr/bin/python

str = "       "; 
print (str.isspace())

str = "Linux Unix Perl Python and django...etc!!!";
print (str.isspace())
"""*****************************************************************"""
# 16. istitle() Method :

"""
It checks whether all the case-based characters in the string
following non-casebased letters are uppercase and all other
case-based characters are lowercase.

Syntax :str.istitle()

It returns true if the string is a titlecased string and there is at
least one character, for example uppercase characters may only follow
uncased characters and lowercase characters only cased ones.
It returns false otherwise.
"""

#!/usr/bin/python

str = "Linux Unix Perl Python And Django...Etc!!!";
print (str.istitle())

str = "Linux unix perl python and django...etc!!!";
print (str.istitle())

"""*****************************************************************"""
# 17. isupper() Method :

"""It checks whether all the case-based characters (letters)
of the string are uppercase.

Syntax : str.isupper()

Note:
This method returns true if all cased characters in the string are uppercase and
there is at least one cased character, false otherwise.
"""

#!/usr/bin/python

str = "THIS IS STRING EXAMPLE....WOW!!!"; 
print (str.isupper())

str = "THIS is string example....wow!!!";
print (str.isupper())

"""*****************************************************************"""
# 18. join() Method :

"""It returns a string in which the string elements of
   sequence have been joined by str separator.

Syntax : str.join(sequence)

Note: sequence : This is a sequence of the elements to be joined.
Returns a string, which is the concatenation of the strings in the sequence seq.
The separator between elements is the string providing this method."""

#!/usr/bin/python

s = "-";
seq = ("a", "b", "c"); # This is sequence of strings.
print (s.join( seq ))

"""*****************************************************************"""
# 19. len() Method :

'''It returns the length of the string.

Syntax : len( str )'''

#!/usr/bin/python

intel = "this is string example....wow!!!"

print ("Length of the string: ", len(intel))

"""*****************************************************************"""
# 20. ljust() Method :

'''It returns the string left justified in a string of length width.
Padding is done using the specified fillchar (default is a space).

The original string is returned if width is less than len(s).

Syntax : str.ljust(width[, fillchar])

width -- This is string length in total after padding.
fillchar -- This is filler character, default is a space.'''

#!/usr/bin/python

str = "this is string example....wow!!!";

print (str.ljust(50, '0'))

"""*****************************************************************"""
# 21. lower() Method :

'''It returns a copy of the string in which all case-based characters have been lowercased.
Syntax : str.lower()'''

#!/usr/bin/python

str = "PYTHON SCRIPTING";

print (str.lower())
    
"""*****************************************************************"""
# 22. lstrip() Method :

'''
It returns a copy of the string in which all chars have been stripped
from the beginning of the string (default whitespace characters).

Syntax : str.lstrip([chars])

chars -- You can supply what chars have to be trimmed.
'''
#!/usr/bin/python

intel = "     python django sql perl...!!!  "
print (intel.lstrip())
mac = "88888888this is string example....wow!!!8888888"
print (mac.lstrip('8'))

"""*****************************************************************"""
# 23. maketrans() Method :

'''It returns a translation table that maps each character in the intabstring
into the character at the same position in the outtab string.

Then this table is passed to the translate() function.

Note: Both intab and outtab must have the same length.

Syntax : str.maketrans(intab, outtab)

intab -- This is the string having actual characters.
outtab -- This is the string having corresponding mapping character.

#!/usr/bin/python

#from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!"
print (str.translate(trantab))'''

"""*****************************************************************"""
# 24. max() Method :

'''It returns the max alphabetical character from the string str.

Syntax : max(str)

str -- This is the string from which max alphabetical character needs to be returned.'''

#!/usr/bin/python

str = "this is really a string example....wow!!!";
print ("Max character: " + max(str))

str = "this is a string example....wow!!!";
print ("Max character: " + max(str))

"""*****************************************************************"""
# 25. min() Method :

'''It returns the min alphabetical character from the string str.

Syntax : min(str)

str -- This is the string from which min alphabetical character needs to be returned.'''

#!/usr/bin/python

str = "this-is-real-string-example....wow!!!";
print ("Min character: " + min(str))

str = "this-is-a-string-example....wow!!!";
print ("Min character: " + min(str))
"""*****************************************************************"""
# 26. replace() Method :
'''
It returns a copy of the string in which the occurrences of old have been replaced with new,
optionally restricting the number of replacements to max.

Syntax : str.replace(old, new[, max])

old -- This is old substring to be replaced.
new -- This is new substring, which would replace old substring.
max -- If this optional argument max is given, only the first count occurrences are replaced.
'''
#!/usr/bin/python

str = "this is string example....wow!!! this is really string";
print (str.replace("is", "was"))
print (str.replace("is", "was", 3))
"""*****************************************************************"""
# 27. rfind() Method :
'''
It returns the last index where the substring str is found,
or -1 if no such index exists, optionally restricting the search to string[beg:end].

Syntax: str.rfind(str, beg=0 end=len(string))

str -- This specifies the string to be searched.
beg -- This is the starting index, by default its 0.
end -- This is the ending index, by default its equal to the length of the string.
'''
#!/usr/bin/python

str1 = "this is really a string example....wow!!!";
str2 = "is";

print (str1.rfind(str2))

print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 0))

print (str1.find(str2))
print (str1.find(str2, 0, 10))
print (str1.find(str2, 10, 0))
"""*****************************************************************"""
# 28. rindex() Method :
'''
It returns the last index where the substring str is found,
or raises an exception if no such index exists,
optionally restricting the search to string[beg:end].

Syntax : str.rindex(str, beg=0 end=len(string))

str -- This specifies the string to be searched.
beg -- This is the starting index, by default its 0
len -- This is ending index, by default its equal to the length of the string.
'''
#!/usr/bin/python

str1 = "this is string example....wow!!!";
str2 = "is";

print (str1.rindex(str2))
print (str1.index(str2))
"""*****************************************************************"""
# 29. rjust() Method :
'''
It returns the string right justified in a string of length width.
Padding is done using the specified fillchar (default is a space).
The original string is returned if width is less than len(s).

Syntax : str.rjust(width[, fillchar])

width -- This is the string length in total after padding.
fillchar -- This is the filler character, default is a space.
'''
#!/usr/bin/python

str = "this is string example....wow!!!";

print (str.rjust(50, '0'))
"""*****************************************************************"""
# 30. rstrip() Method :
'''
It returns a copy of the string in which all chars have been stripped from the
end of the string (default whitespace characters).

Syntax : str.rstrip([chars])

chars -- You can supply what chars have to be trimmed.
'''
#!/usr/bin/python

str = "     this is string example....wow!!!     ";
print (str.rstrip())
str = "88888888this is string example....wow!!!8888888";
print (str.rstrip('8'))
"""*****************************************************************"""
# 31. split() Method :
'''
It returns a list of all the words in the string, using str as the separator
(splits on all whitespace if left unspecified),
optionally limiting the number of splits to num.

Syntax : str.split(str="", num=string.count(str)).

str -- This is any delimeter, by default it is space.
num -- this is number of lines to be made
'''
#!/usr/bin/python

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print (str.split( ))
print (str.split(' ', 1 ))
"""*****************************************************************"""
# 32 splitlines() Method :
'''
It returns a list with all the lines in string,
optionally including the line breaks (if num is supplied and is true)

Syntax : str.splitlines( num=string.count('\n'))

num -- This is any number,
if present then it would be assumed that line breaks need to be included in the lines.
'''
#!/usr/bin/python

str = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d";
print (str.splitlines( ))
print (str.splitlines( 0 ))
print (str.splitlines( 3 ))
print (str.splitlines( 4 ))
print (str.splitlines( 5 ))
"""*****************************************************************"""
# 33. startswith() Method :
'''
It checks whether string starts with str,
optionally restricting the matching with the given indices start and end.

Syntax : str.startswith(str, beg=0,end=len(string));

str -- This is the string to be checked.
beg -- This is the optional parameter to set start index of the matching boundary.
end -- This is the optional parameter to end start index of the matching boundary.
'''
#!/usr/bin/python

str = "this is string example....wow!!!";
print (str.startswith( 'this' ))
print (str.startswith( 'is', 2, 4 ))
print (str.startswith( 'this', 2, 4 ))
"""*****************************************************************"""
# 34. strip() Method :
'''
It returns a copy of the string in which all chars have been stripped
from the beginning and the end of the string (default whitespace characters).

Syntax : str.strip([chars]);

chars -- The characters to be removed from beginning or end of the string.
'''
#!/usr/bin/python

str = "0000000this is string example....wow!!!0000000";
print (str.strip( '0' ))
"""*****************************************************************"""
# 35. swapcase() Method :
'''
It returns a copy of the string in which all the case-based
characters have had their case swapped.

Syntax : str.swapcase();
'''
#!/usr/bin/python

str = "this is string example....wow!!!";
print (str.swapcase())

str = "THIS IS STRING EXAMPLE....WOW!!!";
print (str.swapcase())
"""*****************************************************************"""
