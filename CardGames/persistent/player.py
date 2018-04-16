class Player:
    def __repr__(self):
        return self.id
        
    def __init__(self, playername):
        self.name, self.hand, self.numCards = playername, None, 0
    
    def getName(self):
        return self.name

    def startTurn(self):
        self.isPlaying = True;
    
    def endTurn(self):
        self.isPlaying = False

    def getIsPlaying(self):
        return self.isPlaying
    
    def viewHand(self):
        if self.hand == None:
            return "Empty hand."
        return str(self.hand)
        
    def getHand(self):
        return self.hand
    
    def getCardsInHand(self):
        return self.hand.getCardsInHand()
    
    def setHand(self, hand):
        self.hand = hand
        self.numCards = hand.getNumCardsInHand()

    def playTopCard(self):
        self.numCards -= 1
        return self.hand.getTopCard()
    
    def playCard(self, card):
        self.numCards -= 1
        if self.hand.getCardsInHand().contains(card):
            return self.hand.discard(card)
        
    
        
        
