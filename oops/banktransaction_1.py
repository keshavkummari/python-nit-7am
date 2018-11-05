# Multiple Model Bank Account Example
# Creating Functions
def make_account():
    return {'balance': 0}

def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']


# Calling/Accessing Functions
a = make_account()
b = make_account()

print(deposit(a, 100))
print(deposit(b, 50))
print(withdraw(b, 10))
print(withdraw(a, 10))
