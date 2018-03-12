from Hand import Hand
from Deck import Card, Deck

class Player:
    def __repr__(self):
        return self.__class__.__name__
        
    def __init__(self, id):
        self.id = id
        self.hand = None
    
    def getId(self):
        return self.id

    def setIsPlaying(self, isPlaying):
        self.isPlaying = isPlaying;

    def getIsPlaying(self):
        return self.isPlaying
    
    def viewHand(self):
        self.hand.showHand()
    
    def setHand(self, hand):
        self.hand = hand
