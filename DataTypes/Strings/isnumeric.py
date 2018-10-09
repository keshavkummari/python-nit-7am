#!/usr/bin/python

_007 = u"$6"
print (_007.isnumeric())

_008 = u"786786"
print (_008.isnumeric())

_008 = "786786"
print (_008.isnumeric())


_009 = "03948274"  # Only digit in this string
print (_009.isdigit())

_006 = "Linux Unix Perl Python and django...etc!!! 0009"
print (_006.isdigit())

"""
14	isnumeric()
	Returns true if a unicode string contains only numeric
	characters and false otherwise.
"""
