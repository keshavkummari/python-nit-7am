count=0

name=input("Enter your Name to Find out number of Vowels in your name: ")

#KeyWord  VariableExpression  MembershipOperator   Variable  suit
#for      letter              in                   name      :

for letter in name:
    if (letter in ['A','E','I','O','U','a','e','i','o','u']):
        count=count+1
print ("You have", count, "Vowels in your name")
'''
G
u
i
d
o 
V
a
n
R
o
s
s
u
m
'''