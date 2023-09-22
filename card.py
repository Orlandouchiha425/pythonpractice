import random
#this is a global variable, since is outside of a function
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        #since values is global variable, we decided to call it in my class
        #self. value = values means, we get the values, and assuming we say Three. it will match it with my values dictionary and give us a digit
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit
    
three_of_clubs = Card('Clubs', "Three")
# print(three_of_clubs)
two_hearts = Card('Hearts', "Two")

#this will print 2, because im calling values , with whatever Two matches with
# print(values[two_hearts.rank])

print(two_hearts.value < three_of_clubs.value)


class Deck():
    def __init__(self):
        self.all_cards = []
#this is just a forloop it goes through every suits and ranks and then combines them
#note: there wont be repeating because is just a for loop
        for suit in suits:
            for rank in ranks:
                #create card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()



new_deck = Deck()
new_deck.shuffle()
mycard = new_deck.deal_one()
print(mycard)
print(len(new_deck.all_cards))
#this will print all cards in object memory ex: 
# <__main__.Card object at 0x100ffe350>,
#lets test it, 
# first_card = new_deck.all_cards[0]
# bottom_card = new_deck.all_cards[-1]
# new_deck.shuffle()
# print(new_deck.all_cards[0])
# print(bottom_card)
# for card_object in new_deck.all_cards:
#     print(card_object)