from hand import Hand
from deck import Card, Deck

class Player:
    def __repr__(self):
        return self.id
        
    def __init__(self, id):
        self.id = id
        self.hand = None
        self.numCards = 0
    
    def getId(self):
        return self.id

    def setIsPlaying(self, isPlaying):
        self.isPlaying = isPlaying;

    def getIsPlaying(self):
        return self.isPlaying
    
    def viewHand(self):
        if self.hand == None:
            print("Empty hand.")
        self.hand.showHand()
    
    def setHand(self, hand):
        self.hand = hand
        self.numCards = hand.getNumCardsInHand()

    def playCard(self):
        self.numCards = self.numCards - 1
        return self.hand.getFirstCard()
        
        
