# Deck.py
import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f'Card({self.rank}, {self.suit})'

    def __eq__(self, card):
        return self.rank == card.rank


class Deck:
    def __init__(self):
        ranks = ['A'] + list(range(2, 11)) + list('JQK')
        suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def __repr__(self):
        return str(self.cards)

    def __getitem__(self, i):
        return self.cards[i]

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def cut(self, i):
        self.cards = self.cards[i:] + self.cards[:i]

    def draw(self):
        return self.cards.pop()


'''
deck = Deck()
print(deck)
print(len(deck))
deck.cut(26)
print(deck)
print(deck[0])
card = deck.draw()
print(card)
print(deck)
deck.shuffle()
print(deck)
print(len(deck))
'''
