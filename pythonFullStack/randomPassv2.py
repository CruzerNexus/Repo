import random

entry = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
count = 0
password = ("Your password is: ")
while True:
    n = input("How long would you like your password to be (6-20 characters)? ")
    n = int(n)
    if 5 < n < 21:
        break
print("Generating password...")
while count < n:
    print("...")
    password += random.choice(entry)
    count += 1

print(password)
