# blackJackLab.py
from Deck import Card, Deck


class Hand:
    def __init__(self, card1, card2):
        self.cards = [card1, card2]
        face = {k: 10 for k in 'JQK'}
        number = {k: k for k in range(2, 11)}
        self.points = {'A': 1}
        self.points.update(number)
        self.points.update(face)

    def __repr__(self):
        return str(self.cards)

    def score(self):

        # sum up cards in hand
        return sum([self.points[card.rank] for card in self.cards])

        '''
        total = 0
        for card in self.cards:
            total += points[card.rank]
        return total
        '''

    def add(self, card):
        self.cards.append(card)


class Dealer(Hand):
    def __init__(self, card1, card2):
        super().__init__(card1, card2)

    def one_face_down(self):
        '''
        prints dealer's hand with first card hidden
        '''
        hidden = Card('Hidden', 'Hidden')
        return [hidden] + self.cards[1:]
        # for i in range(1, len(self.cards)):
        #     print(self.cards[i])

    def visible_score(self):
        hidden_card = self.cards[0]
        return self.score() - self.points[hidden_card.rank]


class Game:
    def __init__(self, cut_index, num_players=2):
        # set up deck
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.cut(cut_index)

        # create player hands
        self.players = []
        for i in range(num_players):
            player = Hand(self.deck.draw(), self.deck.draw())
            self.players.append(player)

        # create dealer
        self.dealer = Dealer(self.deck.draw(), self.deck.draw())

    def play(self):
        print('-'*48)
        print("Dealer's hand")
        print(self.dealer.one_face_down())
        print("Dealer's score:", self.dealer.visible_score())
        print(self.dealer.visible_score())
        print('-'*48)

        for i, player in enumerate(self.players):
            print(player)  # display player's hand
            while player.score() < 21:  # loop while player is hitting
                while True:
                    move = input('Hit or stay: ').strip().lower()
                    if move in ['hit', 'h', 'stay', 's']:
                        break
                if move.startswith('h'):
                    player.add(self.deck.draw())
                    print(player)
                else:
                    break
            if player.score() > 21:
                print('Player busted')
            elif player.score() == 21:
                print('Blackjack!')

        # dealer's move
        dealer_score = self.dealer.score()
        print('-'*48)
        print("Dealer's turn")
        print('-'*48)
        print(self.dealer.one_face_down())
        while self.dealer.score() < 21:
            print("Dealer hits!")
            self.dealer.add(self.deck.draw())
            print(self.dealer.one_face_down())
            # >= 17 and < 21: stay.
        if self.dealer.score() < 21:
            print("Dealer Stays!")

            # Exactly 21: Blackjack!
        elif self.dealer.score() == 21:
            print("*Dealer Blackjack!*")

            # >21: Busted
        else:
            print("-Dealer Busted-")

        print('-'*48)
        print("Dealer's final hand")
        print('-'*48)
        print(self.dealer)
        print("Dealer's score: ", self.dealer.score())

        for i, player in enumerate(self.players):
            print('-'*48)
            print(f"Player {i}'s hand")
            print(player)
            print(f"Score: {player.score()}")
            print('-'*48)
            if (21 >= player.score() > self.dealer.score()) or self.dealer.score() < 21:
                print(f'Player {i} wins!')
            else:
                print(f'Player {i} loses :(')


blackjack = Game(1)
blackjack.play()


'''
deck = Deck()
hand = Hand(deck.draw(), deck.draw())
print(hand)
print(hand.score())
dealer = Dealer(deck.draw(), deck.draw())
dealer.one_face_down()
print(dealer.score())
print(dealer.one_face_down())
print(dealer.visible_score())
blackjack = Game(26)
print(blackjack.deck)
print(blackjack.players)
print(blackjack.dealer)
for player in blackjack.players:
    print(player.score())
print(blackjack.dealer.one_face_down())
print(blackjack.dealer.visible_score())
print(blackjack.dealer)
print(blackjack.dealer.score())
'''
