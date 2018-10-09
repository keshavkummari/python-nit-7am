# str.format() method :

Used_For="App Development"
Version='3.3.3'

# Example 1:
# Note: Call or Access a variable using curly braces {}, are used as placeholders.

print('Python is used for {} and course is {}'.format(Used_For,Version)) 


# Example 2: 
# We can specify the order in which it is printed by using numbers (tuple index).
phone='Ipone7'
laptop="Mac Book Pro"
print('I like {0} and {1}'.format('Ipone7','Mac Book Pro'))
print('I like {1} and {0}'.format(phone,laptop))


# Example 3:
# We can use keyword arguments to format the string:

print('Hello {name}, {greeting}'.format(greeting='Goodmorning',name='John')) 

# Exmaple 4: 
# Using % operator:
#x = 12.3456789
#print('The value of x is %' %x)

# This program adds two numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


print('The sum is %.1f' %(float(input('Enter first number: '))+float(input('Enter second number: '))))



#********************************************************************
# Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
num1 = 10
num2 = 14
num3 = 12

# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3

print("The largest number between",num1,",",num2,"and",num3,"is",largest)

