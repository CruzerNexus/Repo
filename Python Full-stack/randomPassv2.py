import random

entry = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
count = 0
password = ("Your password is: ")
n = input("How long would you like your password to be? ")
n = int(n)
while count < n:
    password += random.choice(entry)
    count += 1
print(password)
