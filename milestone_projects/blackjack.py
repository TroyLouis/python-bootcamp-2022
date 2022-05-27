#Automated blackjack hit under 16, stand 16 and up
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck():

    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

class Game():
    player = Player("Gary")
    dealer = Player("Mark")
    deck = Deck()
    deck.shuffle()

    player_hand = 0
    dealer_hand = 0

    game_on = True

    while game_on:
        player.add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())
        player.add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())

        for card in player.hand:
            player_hand += values[card.rank]

        for card in dealer.hand:
            dealer_hand += values[card.rank]

        if player_hand == 21 and dealer_hand != 21:
            print(f'You had {player_hand} the dealer has {dealer_hand}.')
            print("Player Wins")
            game_on = False
            break

        elif dealer_hand == 21:
            print(f'You had {player_hand} the dealer has {dealer_hand}.')
            print("Dealer Wins")
            game_on = False
            break

        while player_hand < 16:
            player.add_card(deck.deal_one())
            player_hand += player.hand[-1].value

        if player_hand > 21:
            print(f'You had {player_hand} the dealer has {dealer_hand}.')

            print("Dealer Wins")
            game_on = False
            break

        while dealer_hand < 16:
            dealer.add_card(deck.deal_one())
            dealer_hand += dealer.hand[-1].value

        if dealer_hand > 21:
            print(f'You had {player_hand} the dealer has {dealer_hand}.')
            print("Player Wins")
            game_on = False
            break

        print(f'You had {player_hand} the dealer has {dealer_hand}.')

        if player_hand > dealer_hand:
            print("Player Wins")
        elif player_hand == dealer_hand:
            print("Push")
        else:
            print("Dealer Wins")

        game_on = False

if __name__ == "__main__":
    Game()