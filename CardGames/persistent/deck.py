from persistant.card import Card
from utils.stack import Stack

class Deck(Stack):
    def __repr__(self):
        return self.__class__.__name__
        
    def __init__(self, jokers=False):
        suits = ["Hearts","Diamonds","Spades","Clubs"]
        ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        self.total = 52
        if jokers:
            self.cards.append(Card("joker", None))
            self.cards.append(Card("joker", None))
            self.total = 54
        
    def __len__(self):
        return self.size
  
    def deal(self, handSize):
        i = 0
        j = 0
        while i < handSize and j < self.total:
            if not self.cards[j].isDealt:
                self.cards[j].dealMe()
                i += 1
                yield self.cards.pop(j)
            j += 1
