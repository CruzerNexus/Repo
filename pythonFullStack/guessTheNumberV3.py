import random

tries = 1
npcNum = random.randint(1, 100)

while True:
    guess = input("Guess the number! ")
    guess = int(guess)
    if guess == npcNum:
        print(f"Yup, I picked {npcNum}! You win!")
        print(f"It took you {tries} tries.")
        break
    elif guess < npcNum:
        print("Nope, too low. Try again!")
    else:
        print("Nope, too high. Try again!")
    tries += 1
