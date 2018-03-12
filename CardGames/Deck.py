import sys, traceback, time, random

class Card:
    def __repr__(self):
        return self.__class__.__name__
        
    def __str__(self):
        return str(self.rank) + " of " + self.suit
        
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.isDealt = False
    
    def getSuit(self):
        return self.suit
        
    def getRank(self):
        return self.rank
        
    def isJoker(self):
        if self.rank == "joker":
            return true
        return false
    
    def isDealt(self):
        return self.isDealt
        
    def dealMe(self):
        self.isDealt = True

class Deck:
    def __repr__(self):
        return self.__class__.__name__
        
    def __init__(self, jokers=False):
        suits = ["Hearts","Diamonds","Spades","Clubs"]
        ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        if jokers:
            self.cards.append(Card(None, "joker"))
            self.cards.append(Card(None, "joker"))
        self.total = 52
            
    def shuffle(self):
        random.shuffle(self.cards)
  
    def deal(self, handSize):
        i = 0
        while i < handSize:
            if not self.cards[i].isDealt:
                self.cards[i].dealMe()
                i += 1
                yield self.cards[i]
                