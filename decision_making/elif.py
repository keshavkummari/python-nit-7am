"""
#!/usr/bin/python

fee_1 = 10
if fee_1 == 20:
   print("1 - Got a true expression value")
   print(fee_1)
elif fee_1 == 10:
   print("2 - Got a true expression value")
   print(fee_1)
elif fee_1 == 12:
   print("3 - Got a true expression value")
   print(fee_1)
elif fee_1 == 13:
   print("2 - Got a true expression value")
   print(fee_1)
elif fee_1 == 10:
   print("3 - Got a true expression value")
   print(fee_1)
else:
   print("Else Block 4 - Got a false expression value")
   print(fee_1)

print("Good bye!")

"""

#!/usr/bin/python

number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here

print('Done')
# This last statement is always executed,
# after the if statement is executed.