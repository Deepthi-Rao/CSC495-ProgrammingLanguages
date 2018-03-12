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
            raise IndexError

    def getSecondCard(self):
        if(self.numCards > 1):
            return self.cards[self.numCards - 1] #second to last card in array is the second card
        else:
            raise IndexError

    def getThirdCard(self):
        if(self.numCards > 2):
            return self.cards[self.numCards - 1] #third to last card in array is the third card
        else:
            raise IndexError

    def addCardToTop(self, newCard):
        self.cards.append(newCard)
        self.numCards = self.numCard + 1
    
    def clearCardsFromPile(self): #returns cards until that point in time
        retList = self.cards
        self.cards= list() #clear card in the pile
        return retList
    
