'''--------------------------------------------------------------'''
# 3. Assignment Operators :
'''--------------------------------------------------------------'''
# Assignment operators are used in Python to assign values to variables.
'''
a = 5 is a simple assignment operator that assigns the value 5 on the right to the variable a on the left.
There are various compound operators in Python like a += 5 that adds to the variable and later assigns the same. 

-------------------------------------------
Operator |	    Example	 |	Equivatent to
-------------------------------------------
1.   =			x = 5		x = 5
2.  +=			x += 5		x = x + 5	[+= Add AND]
3.  -=			x -= 5		x = x - 5	[-= Subtract AND]
4.  *=			x *= 5		x = x * 5	[*= Multiply AND]
5.  /=			x /= 5		x = x / 5	[/= Divide AND]
6.  %=			x %= 5		x = x % 5	[%= Modulus AND]
7.  //=			x //= 5		x = x // 5	[//= Floor Division]
8.  **=			x **= 5		x = x ** 5	[**= Exponent AND]
9.  &=			x &= 5		x = x & 5    ### NOOOOOOOTTTEEEEEE
10. |=			x |= 5		x = x | 5
11. ^=			x ^= 5		x = x ^ 5
12. >>=			x >>= 5		x = x >> 5
13. <<=			x <<= 5		x = x << 5
'''


#!/usr/bin/python3
a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", id(a),id(b),id(c),type(c),c)

print(c)
c += a
print ("Line 2 - Value of c is ", id(a),id(b),id(c),type(c),"c + a", c , sep=':')

print(c)
c *= a
print ("Line 3 - Value of c is ", id(a),id(b),id(c),type(c),c )

print(c)
c /= a
print ("Line 4 - Value of c is ", id(a),id(b),id(c),type(c),c )

c = 2
print(c)
c %= a
print ("Line 5 - Value of c is ", id(a),id(b),id(c),type(c),c)

print(c)
c **= a
print ("Line 6 - Value of c is ", id(a),id(b),id(c),type(c),c)

print(c)
c //= a
print ("Line 7 - Value of c is ", id(a),id(b),id(c),type(c),c)

