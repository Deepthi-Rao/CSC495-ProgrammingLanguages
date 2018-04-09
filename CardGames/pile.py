from deck import Card

class Pile:

    def __init__(self):
        self.cards = list()
        self.numCards = 0
        self.topCard = None
        self.secondCard = None
        self.thirdCard = None
    
    def getFirstCard(self): #first from top
        if(self.numCards > 0):
            return self.cards[self.numCards - 1] #last card in array is the top card
        else:
            return None

    def getSecondCard(self):
        if(self.numCards > 1):
            return self.cards[self.numCards - 2] #second to last card in array is the second card
        else:
            raise IndexError

    def getThirdCard(self):
        if(self.numCards > 2):
            return self.cards[self.numCards - 3] #third to last card in array is the third card
        else:
            raise IndexError

    def addCardToTop(self, newCard):
        self.cards.append(newCard)
        self.numCards = self.numCards + 1
    
    def clearCardsFromPile(self): #returns cards until that point in time
        retList = self.cards
        self.cards= list() #clear card in the pile
        return retList


    
