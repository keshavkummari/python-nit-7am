#!/usr/bin/python

#Values#   1         2      3     4    5
       #   0         1      2     3    4  # Left to Right Indexing
       #  -5        -4     -3    -2   -1  # Right to Left Indexing
tup1 = ('python', 'linux', 1997, 2000,70.25)

tup2 = (1, 2, 3, 4, 5, 6, 7 )

print(tup1,tuple(enumerate(tup1)))

print(tup2,tuple(enumerate(tup2)))

print(tup1,type(tup1),id(tup1))

print(tup2,type(tup2), id(tup2))

print ("tup1[-3]: ", tup1[-3])

print ("tup2[1:5]: ", tup2[1:5])  # end-1 : 5-1=4

