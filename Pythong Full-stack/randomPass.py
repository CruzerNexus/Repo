import random

entry = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
count = 0
password = ("Your password is: ")
while count < 11:
    password += random.choice(entry)
    count += 1
print(password)
