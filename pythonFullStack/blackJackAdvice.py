

cardValue = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
def blkJkAdvice(card1, card2, card3):
    cardTotal = cardValue[card1] + cardValue[card2] + cardValue[card3]
    # <17: hit!
    if cardTotal < 17:
        return f"{cardTotal} Hit"
    # >= 17 and < 21: stay.
    elif cardTotal >= 17 > 21:
        return f"{cardTotal} Stay"
    # Exactly 21: Blackjack!
    elif cardTotal == 21:
        return f"{cardTotal} *Blackjack!*"
    # >21: Busted
    else:
        return f"{cardTotal} -Busted-"


card1 = input("What is your first card (number/letter only): ").upper()
card2 = input("What is your second card (number/letter only): ").upper()
card3 = input("What is your third card (number/letter only): ").upper()
print(blkJkAdvice(card1, card2, card3))
