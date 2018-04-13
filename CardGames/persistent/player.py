class Player:
    def __repr__(self):
        return self.id
        
    def __init__(self, playerId):
        self.id, self.hand, self.numCards = playerId, None, 0
    
    def getId(self):
        return self.id

    def startTurn(self):
        self.isPlaying = True;
    
    def endTurn(self):
        self.isPlaying = False

    def getIsPlaying(self):
        return self.isPlaying
    
    def viewHand(self):
        if self.hand == None:
            print("Empty hand.")
        self.hand.showHand()
        
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
        
    
        
        
