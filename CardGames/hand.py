class Hand:
    def __repr__(self):
        hand = ','.join(self.cards)
        return hand
        
    def __init__(self, cards, handSize):
        self.cards = cards
        self.numCards = handSize

    def getFirstCard(self): #first from top
        if(self.numCards > 0):
            return self.cards.pop(self.cards.__len__() - 1) #last card in array is the top card
        else:
            raise IndexError

    def getCardsInHand(self):
        return self.cards
    
    def getNumCardsInHand(self):
        return self.numCards
    
    def showHand(self):
        print(list(self.cards))
    
    def addCards(self, cards):
        self.cards.extend(cards)
        self.numCards += len(cards)
    
    def addCard(self, card):
        self.cards.append(card)
        self.numCards += 1
        
    def discard(self, card):
        self.cards.remove(card)
        self.numCards -= 1
        
