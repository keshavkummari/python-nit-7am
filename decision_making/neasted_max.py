#Find out the maximum value:

#!/usr/bin/python

#x = float(input("1st Number: "))
#y = float(input("2nd Number: "))
#z = float(input("3rd Number: "))

x = int(input("1st Number: "))
y = int(input("2nd Number: "))
z = int(input("3rd Number: "))

if x > y:
    if x > z:
        maximum = x
    else:
        maximum = z
else:
    if y > z:
        maximum = y
    else:
        maximum = z

print("The maximam value is: " + str(maximum))