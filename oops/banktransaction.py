"""
# State:

Suppose we want to model a bank account with support for
deposit and withdraw operations.

One way to do that is by using global state as shown in
the following example.
"""
# Single Model Bank Account Example
# Creating a Function
balance = 5

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    balance -= amount
    return balance

# Accessing a Function
print(deposit(10))
print(withdraw(20))
