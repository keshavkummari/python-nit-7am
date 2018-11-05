# Inheritance:
class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

"""
Let us try to create a little more sophisticated account
type where the account holder has to maintain a
pre-determined minimum balance.
"""

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount)

x=MinimumBalanceAccount(5)
y=MinimumBalanceAccount(5)

print(x(10))
print(y(20))
