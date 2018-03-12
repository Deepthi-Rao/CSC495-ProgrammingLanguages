from Deck import Card, Deck

class Hand:
    def __repr__(self):
        hand = ','.join(self.cards)
        return self.__class__.__name__
        
    def __init__(self, deck, handSize):
        self.cards = deck.deal(handSize)
        self.numCards = handSize
    
    def getFirstCard(self): #first from top
        if(numCards < 1):
            return cards[numCards - 1] #last card in array is the top card
        else:
            raise IndexError

    def getCardsInHand(self):
        return self.cards
    
    def getNumCardsInHand(self):
        return self.numCards
    
    def showHand(self):
        print(*self.cards, sep=",")
        