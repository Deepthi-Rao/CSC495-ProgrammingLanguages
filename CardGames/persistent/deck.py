from persistent.card import Card
from utils.stack import Stack

class Deck(Stack):
    def __repr__(self):
        return self.__class__.__name__
        
    def __init__(self, jokers=False):
        suits = ["Hearts","Diamonds","Spades","Clubs"]
        ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        self.stack = [Card(rank, suit) for rank in ranks for suit in suits]
        self.total = 52
        if jokers:
            self.cards.append(Card("joker", None))
            self.cards.append(Card("joker", None))
        self.total = 54
        
    def __len__(self):
        return self.size
  
    def deal(self, handSize):
        draw = [self.cards[i] for i in range(handSize)]
        return draw