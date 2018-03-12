import sys, traceback, time, random

class Card:
    def __repr__(self):
        return self.__class__.__name__
        
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def getSuit(self):
        return self.suit
        
    def getRank(self):
        return self.rank
        
    def isJoker(self):
        if self.rank == "joker":
            return true
        return false

class Deck:
    def __repr__(self):
        return self.__class__.__name__
        
    def __init__(self, jokers=False):
        suits = ["hearts","diamonds","spades","clubs"]
        ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        if jokers:
            self.cards.append(Card(None, "joker"))
            self.cards.append(Card(None, "joker"))
            
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self, handSize):
        self.shuffle()
        for i in range(handSize):
            yield self.cards[i]