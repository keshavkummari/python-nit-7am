Python Strings:

Strings are amongst the most popular types in Python. 
We can create them simply by enclosing characters in quotes. 
Python treats single quotes the same as double quotes. 
Creating strings is as simple as assigning a value to a variable. 
For example :

var1 = 'Hello World!'
var2 = "Python Programming"
----------------------------------------------------------
Accessing Values in Strings:

Python does not support a character type; these are treated as strings of length one, thus also considered a substring.

To access substrings, use the square brackets for slicing along with the index or indices to obtain your substring.
 
For example :

#!/usr/bin/python3
       #0123456789                      -9-8-7-6-5-4-3-2-1
var1 = 'Hello to Python World and Python Version is 3.6.0!'
var2 = "Python Programming"

print ("var1[0]: ", var1[0])
print ("var1[0]: ", var1[-1])
print ("var2[1:5]: ", var2[1:5])

Output:
var1[0]:  H
var2[1:5]:  ytho
----------------------------------------------------------

Updating Strings:

You can "update" an existing string by (re)assigning a variable to another string. 

The new value can be related to its previous value or to a completely different string altogether. 

For example :

#!/usr/bin/python3
var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Python')

Output:
('Updated String :- ', 'Hello Python')
----------------------------------------------------------

Escape Characters:

Following table is a list of escape or non-printable characters that can be represented with backslash notation.

An escape character gets interpreted; in a single quoted as well as double quoted strings.


Backslash notation	Hexadecimal character	Description
\a			0x07					Bell or alert
\b			0x08					Backspace
\cx	 							Control-x
\C-x	 							Control-x
\e			0x1b					Escape
\f			0x0c					Formfeed
\M-\C-x	 		        				Meta-Control-x
\n			0x0a					Newline
\nnn	 		        				Octal notation, where n is in the range 0.7
\r			0x0d					Carriage return
\s			0x20					Space
\t			0x09					Tab
\v			0x0b					Vertical tab
\x	 							Character x
\xnn	 							Hexadecimal notation, where n is in 
								the range 0.9, a.f, or A.F
----------------------------------------------------------

String Special Operators: a="Hello"

Assume string variable a holds 'Hello' and variable b holds 'Python'.

Operator    : + 			
Description : Concatenation - Adds values on either side of the operator 	
Example     : a + b will give HelloPython

Operator    : * 	
Description : Repetition - Creates new strings, concatenating multiple
              copies of the same string 	
Example     : a*2 will give -HelloHello

Operator    : [] 	
Description : Slice - Gives the character from the given index 	
Example     : a[1] will give e 

Operator    : [ : ]	
Description : Range Slice - Gives the characters from the given range 	
Example     :   a[1:4] will give ell
#########################################################

Operator    :  in	
Description : Membership - Returns true if a character exists in the given string.
Example     : H in a will give 1

Operator    :  not in 	
Description : Membership - Returns true if a character does not exist in the given string.
Example     : M not in a will give 1


Operator    : r/R	
Description : Raw String - Suppresses actual meaning of Escape characters.
The syntax for raw strings is exactly the same as for normal strings
with the exception of the raw string operator,
the letter "r," which precedes the quotation marks. The "r" can be lowercase (r) or uppercase (R)
and must be placed immediately preceding the first quote mark.	

Example     : print r'\n' prints \n and print R'\n'prints \n

Operator    :  %	
Description :  Format - Performs String formatting	
----------------------------------------------------------
String Formatting Operator:

One of Python's coolest features is the string format operator %. 

This operator is unique to strings and makes up for the pack of having functions from C's printf() family. 

Following is a simple example :

#!/usr/bin/python3

print ("My name is %s and weight is %d kg!" % ('Minnu', 21)) 

Output:

My name is Minnu and weight is 21 kg!

----------------------------------------------------------
Below are the list of complete set of symbols which can be used
along with % :

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
Other supported symbols and functionality are listed in the below:  

Symbol		Functionality
*			argument specifies width or precision
-			left justification
+			display the sign
<sp>		leave a blank space before a positive number
#			add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', 
			depending on whether 'x' or 'X' were used.
0			pad from left with zeros (instead of spaces)
%			'%%' leaves you with a single literal '%'
(var)		mapping variable (dictionary arguments)
m.n.		m is the minimum total width and n is the number of digits to display after the decimal point (if appl.)
----------------------------------------------------------
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
Raw strings do not treat the backslash as a special character at all. 

Every character you put into a raw string stays the way you wrote it :

#!/usr/bin/python3
print ('C:\\nowhere')

Output:
C:\nowhere

Now let's make use of raw string. 
We would put expression in r'expression' as follows −

#!/usr/bin/python3

print (r'C:\\nowhere')

Output:
C:\\nowhere
-----------------------------------------------------------------

Unicode String :

In Python 3, all strings are represented in Unicode.

In Python 2 are stored internally as 8-bit ASCII,
hence it is required to attach 'u' to make it Unicode. 

It is no longer necessary now.

-----------------------------------------------------------------
# Built-in String Methods:

Python includes the following built-in methods to manipulate strings :

Python 3 - String capitalize() Method:

1. capitalize() : Capitalizes first letter of string :

It returns a copy of the string with only its first character capitalized.

Syntax: 
str.capitalize()

Example: 

#!/usr/bin/python3
str = "this is string example....wow!!!"
print ("str.capitalize() : ", str.capitalize())

Output:
str.capitalize() :  This is string example....wow!!!
-----------------------------------------------------------------
Python 3 - String center() Method:

2. center(width, fillchar) : Returns a string padded with fillchar with the original string centered to a total of width columns.

The method center() returns centered in a string of length width. 
Padding is done using the specified fillchar. Default filler is a space.

Syntax :
str.center(width[, fillchar])

Parameters: 
    width -- This is the total width of the string.
    fillchar -- This is the filler character.

Note: This method returns a string that is at least width characters wide, 
created by padding the string with the character fillchar (default is a space)	

Example :
#!/usr/bin/python3
str = "this is string example....wow!!!"
print ("str.center(40, 'a') : ", str.center(40, 'a'))

Output:
str.center(40, 'a') :  aaaathis is string example....wow!!!aaaa
-----------------------------------------------------------------
Python 3 - String count() Method:

Description : 
The method count() returns the number of occurrences of substring sub in the range [start, end].
Optional arguments start and end are interpreted as in slice notation.

Syntax :
str.count(sub, start= 0,end=len(string))

Parameters : 
    sub -- This is the substring to be searched.

    start -- Search starts from this index. First character starts from 0 index. By default search starts from 0 index.

    end -- Search ends from this index. First character starts from 0 index. By default search ends at the last index.

Note : Centered in a string of length width.

Example :
#!/usr/bin/python3
str="this is string example....wow!!!"
sub='i'
print ("str.count('i') : ", str.count(sub))
sub='exam'
print ("str.count('exam', 10, 40) : ", str.count(sub,10,40))

Output:
str.count('i') :  3
str.count('exam', 4, 40) :  1

-----------------------------------------------------------------
