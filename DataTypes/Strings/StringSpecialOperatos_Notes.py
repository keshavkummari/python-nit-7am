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
                                 0 1 2 3 4 # Left to Right index
								-5-4-3-2-1 # Right to Left index
Assume string variable a holds ' H e l l o' and variable b holds 'Python', then :

Operator    : +
Description : Concatenation - Adds values on either side of the operator
Example     : a + b will give HelloPython

Operator    : *
Description : Repetition - Creates new strings,
              concatenating multiple copies of the same string
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

Example     : print r'\n' prints \n and print R'\n' prints \n

Operator    :  %
Description :  Format - Performs String formatting
********************************************************************
# String Formatting Operator :
One of Pythons coolest features is the string format operator %.

This operator is unique to strings and makes up for the pack of having functions
from C's printf() family.

#!/usr/bin/python

print ("My name is %s and I born in %d" % ('Python', 1981))
********************************************************************
Below are the list of complete set of symbols which can be used along with % :

Format Symbol	Conversion
%c 				character
%s 				string conversion via str()
                                prior to formatting
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

para_str = '''this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
'''
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