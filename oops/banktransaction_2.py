# Classes and Objects :

class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

# Calling/Accessing a class
a = BankAccount()
b = BankAccount()

print(a.deposit(100))
print(b.deposit(50))
print(b.withdraw(10))
print(a.withdraw(10))
