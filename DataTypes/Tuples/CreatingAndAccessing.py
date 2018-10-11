#!/usr/bin/python


tup1 = ('python', 'linux', 1997, 2000)

tup2 = (1, 2, 3, 4, 5 )

#tup3 = "A", "B", "C", "E"

tup3 = """A""","""B""","""C""","""E"""

#tup4 = 'a', 'b', 'c', 'd'

tup4 = '''a''', '''b''', '''c''', '''d'''

print (tup1,type(tup1),id(tup1),len(tup1),tuple(enumerate(tup1)))
print("")
print (tup2,type(tup2),id(tup1),len(tup2),tuple(enumerate(tup2)))
print("")
print (tup3,type(tup3),id(tup1),len(tup3),tuple(enumerate(tup3)))
print("")
print (tup4,type(tup4),id(tup1),len(tup4),tuple(enumerate(tup4)))
print("")
# Call the tuple using index:
print (tup3[1])
print("")

