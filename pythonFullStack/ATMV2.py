# ATM.py


class Account:
    def __init__(self, balance=0):
        self.balance = balance
        self.transaction = []

    def __repr__(self):
        return str(self.balance)

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transaction.append(amount)
        return self.balance

    def check_withdrawal(self, amount):
        if self.balance - amount <= 0:
            return False
        else:
            return True

    def withdraw(self, amount):
        self.balance -= amount
        self.transaction.append(amount * -1)
        return self.balance

    def print_transaction(self):
        for i in range(len(self.transaction)):
            if self.transaction[i] > 0:
                print(f"User deposited +{self.transaction[i]}.")
            else:
                print(f"User withdrew {self.transaction[i]}.")


new_account = Account()
print(new_account)
print(new_account.check_balance())
new_account.deposit(50)
print(new_account)
print(new_account.check_withdrawal(25))
new_account.withdraw(25)
print(new_account)
new_account.print_transaction()
