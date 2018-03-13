import sys, traceback, time, random

class Card:
    def __repr__(self):
        if self.rank == None or self.suit == None:
            return "Joker"
        return str(self.rank) + " of " + self.suit
        
    def __str__(self):
        if self.rank == None or self.suit == None:
            return "Joker"
        return str(self.rank) + " of " + self.suit
        
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.isDealt = False
    
    def getSuit(self):
        return self.suit
        
    def getRank(self):
        return self.rank
        
    def isJoker(self):
        if self.rank == "joker":
            return True
        return False
    
    def isDealt(self):
        return self.isDealt
        
    def dealMe(self):
        self.isDealt = True
    
    def match(self, other):
        if self.isJoker() and other.isJoker():
            return True
        elif str(self.rank) == str(other.rank) and self.suit == other.suit:
            return True
        return False

class Deck:
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
        
            
    def shuffle(self):
        random.shuffle(self.cards)
  
    def deal(self, handSize):
        i = 0
        j = 0
        while i < handSize and j < self.total:
            if not self.cards[j].isDealt:
                self.cards[j].dealMe()
                i += 1
                yield self.cards.pop(j)
            j += 1