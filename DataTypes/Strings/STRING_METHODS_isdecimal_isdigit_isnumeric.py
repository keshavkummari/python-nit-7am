'''
str.isdecimal()
    Return true if all characters in the string are decimal characters 
and there is at least one character, false otherwise. Decimal characters 
are those from general category “Nd”. This category includes digit 
characters, and all characters that can be used to form decimal-radix 
numbers, e.g. U+0660, ARABIC-INDIC DIGIT ZERO.

str.isdigit()
    Return true if all characters in the string are digits and there is 
at least one character, false otherwise. Digits include decimal 
characters and digits that need special handling, such as the 
compatibility superscript digits. Formally, a digit is a character that 
has the property value Numeric_Type=Digit or Numeric_Type=Decimal.

str.isnumeric()
    Return true if all characters in the string are numeric characters, 
and there is at least one character, false otherwise. Numeric characters 
include digit characters, and all characters that have the Unicode 
numeric value property, e.g. U+2155, VULGAR FRACTION ONE FIFTH. Formally, 
numeric characters are those with the property value Numeric_Type=Digit, 
Numeric_Type=Decimal or Numeric_Type=Numeric.
'''
# Examples:
#c = "\u0123456789" # decimal-radix numbers
#c = '\u2155'
#c = '\u214675'
#c = r'\u2155'
c = "77"
print(c)

print(c.isdecimal(), c.isdigit(), c.isnumeric())
# Output : (False, False, True)
'''
import unicodedata
print(unicodedata.numeric(c))

c = '\u00B2'
print(c)

print(c.isdecimal(), c.isdigit(), c.isnumeric())
# Output : (False, True, True)

unicodedata.numeric(c)
# Output : 2.0
'''






