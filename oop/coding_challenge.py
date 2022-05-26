#create a bank account class with bank account interactions

class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Your account only has ${self.balance}, you cannot withdraw ${amount}.')
        else:
            self.balance -= amount
            print(f'You have withdrawn ${amount}, your remaining balance is ${self.balance}.')

    def deposit(self, amount):
        self.balance += amount
        print(f'You deposited ${amount}, your new balance is ${self.balance}.')

    def __str__(self):
        return f'{self.owner}\'s account has ${self.balance}.'

if __name__ == "__main__":
    account = Account('Mike', 500)

