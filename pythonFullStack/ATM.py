# ATM.py


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def __repr__(self):
        return str(self.balance)

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def check_withdrawal(self, amount):
        if self.balance - amount <= 0:
            return False
        else:
            return True

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


new_account = Account()
print(new_account)
print(new_account.check_balance())
new_account.deposit(50)
print(new_account)
print(new_account.check_withdrawal(25))
new_account.withdraw(25)
print(new_account)
