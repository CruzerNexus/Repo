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
                print(f"User deposited $+{self.transaction[i]}.")
            else:
                print(f"User withdrew ${self.transaction[i]}.")


'''new_account = Account()
print(new_account)
print(new_account.check_balance())
new_account.deposit(50)
print(new_account)
print(new_account.check_withdrawal(25))
new_account.withdraw(25)
print(new_account)
new_account.print_transaction()'''

new_account = Account()
user_input = ''
while True:
    while True:
        accepted_commands = ['deposit', 'd', 'withdraw', 'w', 'check_balance', 'c', 'history', 'h', 'exit', 'e']
        user_input = input("What would you like to do ((d)eposit, (w)ithdraw, (c)heck balance, (h)istory, (e)xit)? ")
        if user_input in accepted_commands:
            break
    if user_input == ('deposit') or user_input == ('d'):
        give_money = input("How much would you like to deposit? $")
        new_account.deposit(int(give_money))
    elif user_input == ('withdraw') or user_input == ('w'):
        take_money = input("How much would you like to withdraw? $")
        new_account.withdraw(int(take_money))
    elif user_input == ('check_balance') or user_input == ('c'):
        print(f"You have ${new_account} in your account.")
    elif user_input == ('e') or user_input == ("exit"):
        print("Thank you! Goodbye")
        break
    else:
        new_account.print_transaction()
