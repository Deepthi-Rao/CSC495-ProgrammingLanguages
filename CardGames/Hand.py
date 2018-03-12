import Deck

class Hand:
    def __repr__(self):
        return self.__class__.__name__
        
    def __init__(self, deck, handSize):
        self.cards = deck.deal(handSize)
        
    def showHand(self):
        print(*self.cards, sep=",")