import random

tries = 1
npcNum = random.randint(1, 10)

while True:
    guess = input("Guess the number! ")
    guess = int(guess)
    if guess == npcNum:
        print(f"Yup, I picked {npcNum}! You win!")
        print(f"It took you {tries} tries.")
        break
    else:
        print("Nope, try again!")
        tries += 1
