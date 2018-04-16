from persistent_abstractions.faceup import FaceUp

class Hand(FaceUp):
    def __repr__(self):
        return ', '.join(self.cards)
        
    def __str__(self):
        return ', '.join(self.cards)

    def __init__(self, cards, handSize):
        self.cards, self.numCards = cards, handSize

    def getCardsInHand(self):
        return self.cards
    
    def getNumCardsInHand(self):
        return self.numCards
    
    def addCards(self, cards):
        self.cards.extend(cards)
        self.numCards += len(cards)
    
    def addCard(self, card):
        self.cards.append(card)
        self.numCards += 1
        
    def discard(self, card):
        self.numCards -= 1
        return self.cards.remove(card)
        
