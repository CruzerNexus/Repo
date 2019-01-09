import random

tries = 1
npcNum = random.randint(1, 20)

while tries <= 10:
    guess = input("Guess the number! ")
    guess = int(guess)
    if guess == npcNum:
        print(f"Yup, I picked {npcNum}! You win!")
        break
    else:
        print("Nope, try again!")
        tries += 1
    if tries == 11:
        print(f"Sorry, I picked {npcNum}. You lose.")
