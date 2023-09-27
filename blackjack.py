import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}
playing = True


class Card():
    def __init__(self,suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f'your card is the {self.rank} of {self.suit} '
    
class Deck():
    def __init__(self):
        self.deck = [] #object starts with a blank list
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.deck.append(created_card)

    def __str__(self):
            deck_comp = ''  # start with an empty string
            for card in self.deck:
             deck_comp += '\n '+card.__str__() # add each Card object's print string
            return 'The deck has:' + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


test_deck = Deck()
three_of_clubs =Card('Clubs','Three')
print(three_of_clubs)
print(test_deck)


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces =0


    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces +=1 #add to self.aces

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -=10
            self.aces -=1


class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.bet += self.total

    def lose_bet(self):
        self.bet -=self.total

def take_bet():
    pass

# test_deck = Deck()
# test_deck.shuffle()
# test_player = Hand()
# test_player.add_card(test_deck.deal())
# test_player.add_card(test_deck.deal())
# test_player.value


for card in test_player.cards:
    print(card)