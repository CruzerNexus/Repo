import random

choice = ("")
while True:
    choice = input("Let's play! Rock, Paper, Scissors, shoot: ").strip().lower()
    if choice in ['rock', 'paper', 'scissors']:
        break
npcChoice = ["rock", "paper", "scissors"]
rando = random.SystemRandom()
rando = rando.choice(npcChoice)
if choice == rando:
    print(f"{choice} vs {rando}. TIE!")
elif choice == "rock":
    if rando == "paper":
        print(f"{choice} vs {rando}, you lose.")
    else:
        print(f"{choice} vs {rando}, you win!")
elif choice == "paper":
    if rando == "scissors":
        print(f"{choice} vs {rando}, you lose.")
    else:
        print(f"{choice} vs {rando}, you win!")
else:
    if rando == "rock":
        print(f"{choice} vs {rando}, you lose.")
    else:
        print(f"{choice} vs {rando}, you win!")
