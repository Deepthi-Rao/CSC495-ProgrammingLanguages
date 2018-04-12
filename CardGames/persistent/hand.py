from persistent_abstractions.faceup import FaceUp

class Hand(FaceUp):
    def __repr__(self):
        hand = ','.join(self.cards)
        return hand
        
    def __init__(self, cards, handSize):
        self.cards = cards
        self.numCards = handSize

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
        
