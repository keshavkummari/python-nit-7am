# Python Strings:

'''
Strings are amongst the most popular types in Python. 
We can create them simply by enclosing characters in quotes. 
Python treats single quotes the same as double quotes. 
Creating strings is as simple as assigning a value to a variable.
'''

Example:

#!/usr/bin/python

course='python'
course_1="python"

print ("Single Quotes :, course")
print ("Double Quotes :, course_1")

********************************************************************
# Accessing Values in Strings :

These are treated as strings of length one, thus also considered a substring.
To access substrings, use the square brackets for slicing along with the index or indices to obtain your substring.

#!/usr/bin/python

course='python'
course_1="python programming"

print ("course[0]: ", course[0])
print ("course_1[1:5]: ", course_1[1:5])

********************************************************************
# Updating Strings :
"""
You can "update" an existing string by (re)assigning a variable to another string. 

The new value can be related to its previous value or to a completely different string altogether. """

#!/usr/bin/python
course = 'Hello World!'

print ("Updated String :- ", course[:6] + 'Redhat')

********************************************************************
Escape Characters :

Following table is a list of escape or non-printable characters that can be represented with
backslash notation.

An escape character gets interpreted; in a single quoted as well as double quoted strings.

Backslash notation	Hexadecimal character	Description
\a			0x07			Bell or alert
\b			0x08			Backspace
\cx	 					Control-x
\C-x	 					Control-x
\e			0x1b			Escape
\f			0x0c			Formfeed
\M-\C-x	 		        		Meta-Control-x
\n			0x0a			Newline
\nnn	 		        		Octal notation, where n is in the range 0.7
\r			0x0d			Carriage return
\s			0x20			Space
\t			0x09			Tab
\v			0x0b			Vertical tab
\x	 					Character x
\xnn	 					Hexadecimal notation, where n is in 
								    the range 0.9, a.f, or A.F
********************************************************************
# String Special Operators:

Assume string variable a holds 'Hello' and variable b holds 'Python', then :

Operator    : + 			
Description : Concatenation - Adds values on either side of the operator 	
Example     : a + b will give HelloPython

Operator    : * 	
Description : Repetition - Creates new strings, concatenating multiple copies of the same string 	
Example     : a*2 will give -HelloHello

Operator    : [] 	
Description : Slice - Gives the character from the given index 	
Example     : a[1] will give e 

Operator    : [ : ]	
Description : Range Slice - Gives the characters from the given range 	
Example     :   a[1:4] will give ell


Operator    :  in	
Description : Membership - Returns true if a character exists in the given string.
Example     : H in a will give 1

Operator    :  not in 	
Description : Membership - Returns true if a character does not exist in the given string.
Example     : M not in a will give 1


Operator    : r/R	
Description : Raw String - Suppresses actual meaning of Escape characters.
The syntax for raw strings is exactly the same as for normal strings with
the exception of the raw string operator, the letter "r,"
which precedes the quotation marks. The "r" can be lowercase (r) or uppercase (R) and
must be placed immediately preceding the first quote mark.	

Example     : print r'\n' prints \n and print R'\n'prints \n

Operator    :  %	
Description :  Format - Performs String formatting	
********************************************************************
# String Formatting Operator :
One of Pythons coolest features is the string format operator %. 

This operator is unique to strings and makes up for the pack of having functions 
from C's printf() family.

#!/usr/bin/python

print ("My name is %s and weight is %d kg!" % ('Python', 1981))
********************************************************************
Below are the list of complete set of symbols which can be used along with % :

Format Symbol	Conversion
%c 				character
%s 				string conversion via str() prior to formatting
%i 				signed decimal integer
%d 				signed decimal integer
%u 				unsigned decimal integer
%o 				octal integer
%x 				hexadecimal integer (lowercase letters)
%X 				hexadecimal integer (UPPERcase letters)
%e 				exponential notation (with lowercase 'e')
%E 				exponential notation (with UPPERcase 'E')
%f 				floating point real number
%g 				the shorter of %f and %e
%G 				the shorter of %f and %E
----------------------------------------------------------
# Other supported symbols and functionality are listed in the below:  

Symbol		Functionality
*		argument specifies width or precision
-		left justification
+		display the sign
<sp>		leave a blank space before a positive number
#		add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', 
		depending on whether 'x' or 'X' were used.
0		pad from left with zeros (instead of spaces)
%		'%%' leaves you with a single literal '%'
(var)		mapping variable (dictionary arguments)
m.n.		m is the minimum total width and n is the number of digits to display after the
decimal point (if appl.)
********************************************************************
Triple Quotes:

Python's triple quotes comes to the rescue by allowing strings to span multiple lines, including verbatim NEWLINEs, TABs, and any other special characters.

The syntax for triple quotes consists of three consecutive single or double quotes.

#!/usr/bin/python3

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)

When the above code is executed, it produces the following result. 
Note how every single special character has been converted to its printed form, 
right down to the last NEWLINE at the end of the string between the "up." and closing triple quotes. 
Also note that NEWLINEs occur either with an explicit carriage return at the end of a line or its escape code (\n)

Output:

this is a long string that is made up of
several lines and non-printable characters such as
TAB (    ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ 
], or just a NEWLINE within
the variable assignment will also show up.

-----------------------------------------------------------------
# Raw strings do not treat the backslash as a special character at all. 

#!/usr/bin/python3
print ('d:\\nowhere')

Output:
d:\nowhere

# Now let's make use of raw string. 
We would put expression in r'expression' as follows:

#!/usr/bin/python3

print (r'd:\\nowhere')

Output:
d:\\nowhere

********************************************************************
# String Methods:

SN	Methods with Description
1	capitalize()
	Capitalizes first letter of string
2	center(width, fillchar)
	Returns a space-padded string with the original string centered to a total of width columns.
3	count(str, beg= 0,end=len(string))
	Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.
4	decode(encoding='UTF-8',errors='strict')
	Decodes the string using the codec registered for encoding.
	encoding defaults to the default string encoding.
5	encode(encoding='UTF-8',errors='strict')
	Returns encoded string version of string; on error, default is to raise a
	ValueError unless errors is given with 'ignore' or 'replace'.
6	endswith(suffix, beg=0, end=len(string))
	Determines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise.
7	expandtabs(tabsize=8)
	Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not provided.
8	find(str, beg=0 end=len(string))
	Determine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.
9	index(str, beg=0, end=len(string))
	Same as find(), but raises an exception if str not found.
10	isalnum()
	Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.
11	isalpha()
	Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.
12	isdigit()
	Returns true if string contains only digits and false otherwise.
13	islower()
	Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.
14	isnumeric()
	Returns true if a unicode string contains only numeric characters and false otherwise.
15	isspace()
	Returns true if string contains only whitespace characters and false otherwise.
16	istitle()
	Returns true if string is properly "titlecased" and false otherwise.
17	isupper()
	Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.
18	join(seq)
	Merges (concatenates) the string representations of elements in sequence seq into a string,
	with separator string.
19	len(string)
	Returns the length of the string
20	ljust(width[, fillchar])
	Returns a space-padded string with the original string left-justified to a total of
	width columns.
21	lower()
	Converts all uppercase letters in string to lowercase.
22	lstrip()
	Removes all leading whitespace in string.
23	maketrans()
	Returns a translation table to be used in translate function.
24	max(str)
	Returns the max alphabetical character from the string str.
25	min(str)
	Returns the min alphabetical character from the string str.
26	replace(old, new [, max])
	Replaces all occurrences of old in string with new or at most max occurrences if max given.
27	rfind(str, beg=0,end=len(string))
	Same as find(), but search backwards in string.
28	rindex( str, beg=0, end=len(string))
	Same as index(), but search backwards in string.
29	rjust(width,[, fillchar])
	Returns a space-padded string with the original string right-justified to a total of width columns.
30	rstrip()
	Removes all trailing whitespace of string.
31	split(str="", num=string.count(str))
	Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given.
32	splitlines( num=string.count('\n'))
	Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.
33	startswith(str, beg=0,end=len(string))
	Determines if string or a substring of string (if starting index beg and ending index end are given) starts with substring str; returns true if so and false otherwise.
34	strip([chars])
	Performs both lstrip() and rstrip() on string
35	swapcase()
	Inverts case for all letters in string.
36	title()
	Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.
37	translate(table, deletechars="")
	Translates string according to translation table str(256 chars), removing those in the del string.
38	upper()
	Converts lowercase letters in string to uppercase.
39	zfill (width)
	Returns original string leftpadded with zeros to a total of width characters; intended for numbers, zfill() retains any sign given (less one zero).
40	isdecimal()
	Returns true if a unicode string contains only decimal characters and false otherwise.

********************************************************************
1. capitalize() Method :
# Note: string with only its first character capitalized.

#!/usr/bin/python

abc_string = "welcome to python world"

print ("abc_string.capitalize() : ", abc_string.capitalize())
********************************************************************
2. center() Method:

Note: 
Returns centered in a string of length width. 
Padding is done using the specified fillchar. Default filler is a space.

Syntax : str.center(width[, fillchar])

width -- This is the total width of the string.
fillchar -- This is the filler character.

#!/usr/bin/python
abc_string = "Welcome to python world"
print ("abc_string.center(40, 'a') : ", abc_string.center(40, 'a'))
********************************************************************
3. count() Method :

It returns the number of occurrences of substring sub in the range [start, end].
Optional arguments start and end are interpreted as in slice notation.

Syntax : str.count(sub, start= 0,end=len(string))

# sub -- This is the substring to be searched.

# start -- Search starts from this index. First character starts from 0 index.
By default search starts from 0 index.

# end -- Search ends from this index.
First character starts from 0 index. By default search ends at the last index.

Note: Centered in a string of length width.

#!/usr/bin/python
mac = "Welcome to python world";

sub = "o";
print "mac.count(sub, 4, 40) : ", mac.count(sub, 4, 40)
sub = "python";
print "mac.count(sub) : ", mac.count(sub)

********************************************************************
4. decode() Method :

# Decodes the string using the codec registered for encoding.
It defaults to the default string encoding.

Syntax : Str.decode(encoding='UTF-8',errors='strict')

encoding -- This is the encodings to be used. 

errors -- This may be given to set a different error handling scheme. 
The default for errors is 'strict', meaning that encoding errors raise a UnicodeError. 

Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace'
and any other name registered via codecs.register_error()..

Note: Decoded string.

#!/usr/bin/python

mac = "welcome to python world";
mac = mac.encode('base64','strict');

print "Encoded String: " + mac
print "Decoded String: " + mac.decode('base64','strict')
********************************************************************
5. encode() Method :

Returns an encoded version of the string. 
Default encoding is the current default string encoding. 
The errors may be given to set a different error handling scheme.

Syntax : str.encode(encoding='UTF-8',errors='strict')

encoding -- This is the encodings to be used. 

errors -- This may be given to set a different error handling scheme. The default for errors is 'strict', meaning that encoding errors raise a UnicodeError. Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' and any other name registered via codecs.register_error().

Note : Decoded string.

Example
#!/usr/bin/python

str = "Welcome to python world";

print "Encoded String: " + str.encode('base64','strict')
********************************************************************
6. endswith() Method :

It returns True if the string ends with the specified suffix,
otherwise return False optionally restricting the matching with the given indices start and end.

Syntax : str.endswith(suffix[, start[, end]])

suffix -- This could be a string or could also be a tuple of suffixes to look for.

start -- The slice begins from here.

end -- The slice ends here.

#!/usr/bin/python

str = "Welcome to python world";

suffix = "world";
print str.endswith(suffix)
print str.endswith(suffix,20)

suffix = "to";
print str.endswith(suffix, 2, 4)
print str.endswith(suffix, 2, 6)
********************************************************************
7. expandtabs() Method :

It returns a copy of the string in which tab characters ie. '\t' are expanded using spaces,
optionally using the given tabsize (default 8).

Syntax : str.expandtabs(tabsize=8)

tabsize -- This specifies the number of characters to be replaced for a tab character '\t'.

This method returns a copy of the string in which tab characters i.e., '\t' have
been expanded using spaces.

#!/usr/bin/python

str = "this is\tstring example....rock!!!";


print "Original string: " + str
print "Defualt exapanded tab: " +  str.expandtabs()
print "Double exapanded tab: " +  str.expandtabs(16)
********************************************************************
8. find() Method  : 

It determines if string str occurs in string,
or in a substring of string if starting index beg and ending index end are given.

Syntax : str.find(str, beg=0, end=len(string))

str -- This specifies the string to be searched.

beg -- This is the starting index, by default its 0.

end -- This is the ending index, by default its equal to the length of the string.

Note : Index if found and -1 otherwise.

#!/usr/bin/python

str1 = "Python number string examples";
str2 = "exam";

print str1.find(str2)
print str1.find(str2, 10)
print str1.find(str2, 40)
********************************************************************
9. index() Method : 

It determines if string str occurs in string or in a substring of string if starting index
beg and ending index end are given. This method is same as find(), but raises an exception if sub is not found.

Syntax : str.index(str, beg=0 end=len(string))

str -- This specifies the string to be searched.
beg -- This is the starting index, by default its 0.
end -- This is the ending index, by default its equal to the length of the string.

Note: Index if found otherwise raises an exception if str is not found.

Example
#!/usr/bin/python

str1 = "Its python world....wow!!!";
str2 = "exam";

print str1.index(str2)
print str1.index(str2, 10)
print str1.index(str2, 40)

********************************************************************
10. isalnum() Method :

Checks whether the string consists of alphanumeric characters.

Syntax
Following is the syntax for isalnum() method:

str.isalnum()
Parameters
NA

Note: 
This method returns true if all characters in the string are alphanumeric
and there is at least one character, false otherwise.


#!/usr/bin/python

str = "this2020";  # No space in this string
print str.isalnum()

str = "Python world....wow!!!";
print str.isalnum()

********************************************************************
11.  isalpha() Method:

Checks whether the string consists of alphabetic characters only.

Syntax : str.isalpha()

Note: 
This method returns true if all characters in the string are alphabetic and there is at least one character, false otherwise.

#!/usr/bin/python

str = "this";  # No space & digit in this string
print str.isalpha()

str = "Python and perl....linux!!!";
print str.isalpha()
********************************************************************

********************************************************************

********************************************************************


********************************************************************
