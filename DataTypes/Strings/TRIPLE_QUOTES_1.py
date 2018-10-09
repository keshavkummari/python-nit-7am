#!/usr/bin/python3

para_str = '''this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
'''
print ("Lets access triples",para_str,type(para_str),id(para_str),sep="\n")


# Below is the multiline comment
'''
Some text
linux
unix
'''
# Below is the multiline comment
"""
Some text
perl
python
django
"""
